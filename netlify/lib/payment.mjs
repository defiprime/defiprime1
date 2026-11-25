import { decodeEventLog, erc20Abi, getAddress } from "viem";
import { baseUnits } from "../../assets/js/listing-core.mjs";

export function findPayment(receipt, chain, price) {
  if (receipt.status !== "success") return { error: "The transaction reverted on-chain" };
  const receiver = getAddress(chain.receiver);
  for (const log of receipt.logs) {
    const token = chain.tokens.find((candidate) => candidate.address.toLowerCase() === log.address.toLowerCase());
    if (!token) continue;
    let event;
    try {
      event = decodeEventLog({ abi: erc20Abi, data: log.data, topics: log.topics });
    } catch {
      continue;
    }
    if (event.eventName !== "Transfer") continue;
    if (getAddress(event.args.to) !== receiver) continue;
    if (event.args.value < baseUnits(price, token.decimals)) continue;
    return { from: getAddress(event.args.from), token: token.symbol, amount: event.args.value };
  }
  return { error: `No transfer of at least ${price} in an accepted stablecoin to the defiprime address in this transaction` };
}

export function hasConfirmations(latestBlock, receiptBlock, required) {
  return latestBlock - receiptBlock + 1n >= BigInt(required);
}
