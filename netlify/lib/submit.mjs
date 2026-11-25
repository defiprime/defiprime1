import { TransactionReceiptNotFoundError, formatUnits } from "viem";
import { activeChains, claimMessage, cleanFields, submissionDigest } from "../../assets/js/listing-core.mjs";
import { findPayment, hasConfirmations } from "./payment.mjs";

const TX_HASH = /^0x[0-9a-f]{64}$/;
const SIGNATURE = /^0x[0-9a-f]{130,4000}$/;

export async function handleSubmission(body, { checkout, clientFor, store, notify, now = () => new Date() }) {
  const cleaned = cleanFields(body?.fields);
  if (cleaned.error) return [400, cleaned];
  const { fields } = cleaned;

  const chain = activeChains(checkout).find((candidate) => candidate.id === Number(body?.chainId));
  if (!chain) return [400, { error: "This chain is not accepted for listing payments" }];

  const txHash = String(body?.txHash ?? "").toLowerCase();
  if (!TX_HASH.test(txHash)) return [400, { error: "Missing or malformed transaction hash" }];
  const signature = String(body?.signature ?? "").toLowerCase();
  if (!SIGNATURE.test(signature)) return [400, { error: "Missing or malformed signature" }];

  const client = clientFor(chain);
  let receipt;
  try {
    receipt = await client.getTransactionReceipt({ hash: txHash });
  } catch (error) {
    if (error instanceof TransactionReceiptNotFoundError || error?.name === "TransactionReceiptNotFoundError") {
      return [202, { status: "pending", reason: "Waiting for the transaction to be mined" }];
    }
    return [502, { error: "Could not reach the chain, try again shortly" }];
  }
  const latest = await client.getBlockNumber();
  if (!hasConfirmations(latest, receipt.blockNumber, chain.confirmations)) {
    return [202, { status: "pending", reason: "Waiting for confirmations" }];
  }

  const payment = findPayment(receipt, chain, checkout.price);
  if (payment.error) return [402, payment];

  const digest = await submissionDigest(fields);
  const message = claimMessage({ project: fields.project, chainId: chain.id, digest });
  const signedByPayer = await client.verifyMessage({ address: payment.from, message, signature }).catch(() => false);
  if (!signedByPayer) return [403, { error: "The submission was not signed by the wallet that made the payment" }];

  const token = chain.tokens.find((candidate) => candidate.symbol === payment.token);
  const key = `${chain.id}-${txHash}`;
  const record = {
    digest,
    fields,
    chainId: chain.id,
    txHash,
    from: payment.from,
    token: payment.token,
    amount: payment.amount.toString(),
    amountDisplay: formatUnits(payment.amount, token.decimals),
    createdAt: now().toISOString(),
    notified: false,
  };

  let current = record;
  const write = await store.setJSON(key, record, { onlyIfNew: true });
  if (!write.modified) {
    const existing = await store.get(key, { type: "json" });
    if (!existing || existing.digest !== digest) {
      return [409, { error: "This payment is already attached to a different submission" }];
    }
    current = existing;
  }

  if (!current.notified) {
    try {
      await notify(current, chain);
    } catch {
      return [502, { error: "Payment verified, but we could not record the submission. Retry in a minute; you will not be charged again." }];
    }
    await store.setJSON(key, { ...current, notified: true });
  }
  return [200, { status: "received" }];
}
