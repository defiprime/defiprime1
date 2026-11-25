import { test } from "node:test";
import assert from "node:assert/strict";
import {
  TransactionReceiptNotFoundError,
  encodeAbiParameters,
  encodeEventTopics,
  encodeFunctionData,
  erc20Abi,
  verifyMessage,
} from "viem";
import { generatePrivateKey, privateKeyToAccount } from "viem/accounts";
import realCheckout from "../data/listing_checkout.json" with { type: "json" };
import {
  activeChains,
  claimMessage,
  cleanFields,
  submissionDigest,
  transferCalldata,
} from "../assets/js/listing-core.mjs";
import { checkReady, handleSubmission } from "../netlify/lib/submit.mjs";
import { emailText } from "../netlify/lib/notify.mjs";

const RECEIVER = "0x1111111111111111111111111111111111111111";
const USDC = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913";
const OTHER_TOKEN = "0x2222222222222222222222222222222222222222";
const TX = "0x" + "ab".repeat(32);

const checkout = {
  price: 1000,
  chains: [
    {
      id: 8453,
      name: "Base",
      receiver: RECEIVER,
      startBlock: 50,
      confirmations: 5,
      rpc: "http://unused",
      explorer: "https://basescan.org/tx/",
      tokens: [{ symbol: "USDC", address: USDC, decimals: 6 }],
    },
    { id: 1, name: "Ethereum", receiver: "", startBlock: 0, confirmations: 3, rpc: "http://unused", explorer: "", tokens: [] },
  ],
};

const fields = {
  project: "Example Protocol",
  website: "https://example.org",
  category: "Lending",
  chains: "Base",
  description: "Lends things.\nOn Base.",
  twitter: "",
  email: "team@example.org",
  telegram: "",
  notes: "",
};

function transferLog({ token = USDC, from, to = RECEIVER, value = 1000_000000n }) {
  return {
    address: token,
    topics: encodeEventTopics({ abi: erc20Abi, eventName: "Transfer", args: { from, to } }),
    data: encodeAbiParameters([{ type: "uint256" }], [value]),
  };
}

function fakeStore() {
  const data = new Map();
  return {
    data,
    async setJSON(key, value, options = {}) {
      if (options.onlyIfNew && data.has(key)) return { modified: false };
      data.set(key, structuredClone(value));
      return { modified: true };
    },
    async get(key) {
      return data.has(key) ? structuredClone(data.get(key)) : null;
    },
  };
}

function fakeClient({ receipt, latest = 200n, missing = false, rpcDown = false }) {
  return {
    async getTransactionReceipt() {
      if (missing) throw new TransactionReceiptNotFoundError({ hash: TX });
      return receipt;
    },
    async getBlockNumber() {
      if (rpcDown === "block") throw new Error("429");
      return latest;
    },
    async verifyMessage(args) {
      if (rpcDown === "verify") throw new Error("429");
      return verifyMessage(args);
    },
  };
}

async function scenario({ payer, signer = payer, submitted = fields, logs, status = "success", latest, missing, rpcDown, blockNumber = 100n, store = fakeStore(), notify }) {
  const receipt = { status, blockNumber, logs: logs ?? [transferLog({ from: payer.address })] };
  const digest = await submissionDigest(cleanFields(submitted).fields);
  const signature = await signer.signMessage({ message: claimMessage({ project: submitted.project, chainId: 8453, digest }) });
  const sent = [];
  const result = await handleSubmission(
    { fields: submitted, chainId: 8453, txHash: TX, signature },
    {
      checkout,
      clientFor: () => fakeClient({ receipt, latest, missing, rpcDown }),
      store,
      notify: notify ?? (async (record) => sent.push(record)),
      now: () => new Date("2026-11-25T00:00:00Z"),
    },
  );
  return { result, sent, store };
}

const payer = privateKeyToAccount(generatePrivateKey());
const stranger = privateKeyToAccount(generatePrivateKey());

test("a paid, signed submission is recorded and notified once", async () => {
  const { result, sent, store } = await scenario({ payer });
  assert.deepEqual(result, [200, { status: "received" }]);
  assert.equal(sent.length, 1);
  assert.equal(sent[0].from, payer.address);
  assert.equal(sent[0].amountDisplay, "1000");
  assert.equal(store.data.get(`8453-${TX}`).notified, true);
});

test("resubmitting the same submission is idempotent and does not notify again", async () => {
  const store = fakeStore();
  await scenario({ payer, store });
  const again = await scenario({ payer, store });
  assert.equal(again.result[0], 200);
  assert.equal(again.sent.length, 0);
});

test("a failed notification is retried on the next post", async () => {
  const store = fakeStore();
  const first = await scenario({ payer, store, notify: async () => { throw new Error("down"); } });
  assert.equal(first.result[0], 502);
  assert.equal(store.data.get(`8453-${TX}`).notified, false);
  const second = await scenario({ payer, store });
  assert.equal(second.result[0], 200);
  assert.equal(second.sent.length, 1);
});

test("a payment already claimed by another submission is rejected", async () => {
  const store = fakeStore();
  await scenario({ payer, store });
  const other = await scenario({ payer, store, submitted: { ...fields, project: "Copycat" } });
  assert.equal(other.result[0], 409);
});

test("someone else's payment cannot be claimed without the payer's signature", async () => {
  const { result } = await scenario({ payer, signer: stranger });
  assert.equal(result[0], 403);
});

test("underpayment, wrong receiver, unknown token and reverted transactions are refused", async () => {
  const cases = [
    [transferLog({ from: payer.address, value: 999_999999n })],
    [transferLog({ from: payer.address, to: OTHER_TOKEN })],
    [transferLog({ from: payer.address, token: OTHER_TOKEN })],
    [],
  ];
  for (const logs of cases) {
    const { result, sent } = await scenario({ payer, logs });
    assert.equal(result[0], 402);
    assert.equal(sent.length, 0);
  }
  const reverted = await scenario({ payer, status: "reverted" });
  assert.equal(reverted.result[0], 402);
});

test("unmined and under-confirmed transactions return pending", async () => {
  assert.equal((await scenario({ payer, missing: true })).result[0], 202);
  assert.equal((await scenario({ payer, latest: 103n })).result[0], 202);
  assert.equal((await scenario({ payer, latest: 104n })).result[0], 200);
});

test("RPC failures are retryable errors, never a signature refusal", async () => {
  assert.equal((await scenario({ payer, rpcDown: "verify" })).result[0], 502);
  assert.equal((await scenario({ payer, rpcDown: "block" })).result[0], 502);
});

test("transfers made before checkout opened cannot be claimed", async () => {
  const { result, sent } = await scenario({ payer, blockNumber: 49n });
  assert.equal(result[0], 402);
  assert.equal(sent.length, 0);
});

test("readiness requires an open chain, the email environment and a working store", async () => {
  const env = { MJ_APIKEY_PUBLIC: "a", MJ_APIKEY_PRIVATE: "b", LISTING_EMAIL_FROM: "c", LISTING_EMAIL_TO: "d" };
  assert.equal((await checkReady({ checkout, store: fakeStore(), env }))[0], 200);
  assert.equal((await checkReady({ checkout, store: fakeStore(), env: { ...env, LISTING_EMAIL_TO: "" } }))[0], 503);
  assert.equal((await checkReady({ checkout: realCheckout, store: fakeStore(), env }))[0], 503);
  const broken = { setJSON: async () => { throw new Error("blobs down"); }, get: async () => null };
  assert.equal((await checkReady({ checkout, store: broken, env }))[0], 503);
});

test("chains without a receiver address are not accepted", async () => {
  const [status] = await handleSubmission(
    { fields, chainId: 1, txHash: TX, signature: "0x" + "00".repeat(65) },
    { checkout, clientFor: () => assert.fail("no RPC call expected"), store: fakeStore(), notify: async () => {} },
  );
  assert.equal(status, 400);
  assert.deepEqual(activeChains(checkout).map((chain) => chain.id), [8453]);
});

test("field validation enforces required fields, URLs, emails and length caps", () => {
  assert.equal(cleanFields({ ...fields, project: " " }).field, "project");
  assert.equal(cleanFields({ ...fields, website: "javascript:alert(1)" }).field, "website");
  assert.equal(cleanFields({ ...fields, email: "nope" }).field, "email");
  assert.equal(cleanFields({ ...fields, description: "x".repeat(601) }).field, "description");
  assert.ok(cleanFields(null).error);
});

test("cleaning strips control characters, keeps newlines in long fields and is idempotent", async () => {
  const dirty = { ...fields, project: "Ex\u0007ample\r\n", description: "a\r\nb\u0000c" };
  const once = cleanFields(dirty).fields;
  assert.equal(once.project, "Ex ample");
  assert.equal(once.description, "a \nb c");
  assert.deepEqual(cleanFields(once).fields, once);
  assert.equal(await submissionDigest(once), await submissionDigest(cleanFields(once).fields));
});

test("browser transfer calldata matches viem's ERC-20 encoding", () => {
  const amount = 1000_000000n;
  assert.equal(
    transferCalldata(RECEIVER, amount),
    encodeFunctionData({ abi: erc20Abi, functionName: "transfer", args: [RECEIVER, amount] }),
  );
});

test("the email carries the submission and an explorer link", () => {
  const text = emailText(
    { fields, from: payer.address, token: "USDC", amountDisplay: "1000", txHash: TX, createdAt: "2026-11-25T00:00:00.000Z" },
    checkout.chains[0],
  );
  assert.match(text, /Project: Example Protocol/);
  assert.match(text, new RegExp(`https://basescan.org/tx/${TX}`));
});

test("the shipped config lists only six-decimal stablecoins with well-formed addresses", () => {
  for (const chain of realCheckout.chains) {
    assert.ok(chain.receiver === "" || /^0x[0-9a-fA-F]{40}$/.test(chain.receiver));
    assert.ok(Number.isInteger(chain.startBlock));
    for (const token of chain.tokens) {
      assert.match(token.address, /^0x[0-9a-fA-F]{40}$/);
      assert.equal(token.decimals, 6);
    }
  }
});
