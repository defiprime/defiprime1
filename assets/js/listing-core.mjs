export const FIELDS = [
  { name: "project", max: 100, required: true },
  { name: "website", max: 200, required: true, kind: "url" },
  { name: "category", max: 60, required: true },
  { name: "chains", max: 200 },
  { name: "description", max: 600, required: true, multiline: true },
  { name: "twitter", max: 200 },
  { name: "email", max: 200, required: true, kind: "email" },
  { name: "telegram", max: 100 },
  { name: "notes", max: 1000, multiline: true },
];

const SINGLE_LINE_CONTROL = /[\u0000-\u001f\u007f]/g;
const MULTI_LINE_CONTROL = /[\u0000-\u0009\u000b-\u001f\u007f]/g;
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function isHttpUrl(value) {
  try {
    const url = new URL(value);
    return url.protocol === "https:" || url.protocol === "http:";
  } catch {
    return false;
  }
}

export function cleanFields(input) {
  if (!input || typeof input !== "object") return { error: "Missing submission fields" };
  const fields = {};
  for (const field of FIELDS) {
    const raw = typeof input[field.name] === "string" ? input[field.name] : "";
    const value = raw.replace(field.multiline ? MULTI_LINE_CONTROL : SINGLE_LINE_CONTROL, " ").trim();
    if (field.required && !value) return { error: `${field.name} is required`, field: field.name };
    if (value.length > field.max) return { error: `${field.name} must be at most ${field.max} characters`, field: field.name };
    if (value && field.kind === "url" && !isHttpUrl(value)) return { error: "website must start with https://", field: field.name };
    if (value && field.kind === "email" && !EMAIL.test(value)) return { error: "email is not a valid address", field: field.name };
    fields[field.name] = value;
  }
  return { fields };
}

export async function submissionDigest(fields) {
  const canonical = JSON.stringify(FIELDS.map((field) => [field.name, fields[field.name] ?? ""]));
  const hash = await globalThis.crypto.subtle.digest("SHA-256", new TextEncoder().encode(canonical));
  return "0x" + Array.from(new Uint8Array(hash), (byte) => byte.toString(16).padStart(2, "0")).join("");
}

export function claimMessage({ project, chainId, digest }) {
  return [
    "defiprime listing submission",
    `Project: ${project}`,
    `Chain: ${chainId}`,
    `Submission: ${digest}`,
  ].join("\n");
}

export function baseUnits(price, decimals) {
  return BigInt(price) * 10n ** BigInt(decimals);
}

export function transferCalldata(receiver, amount) {
  const to = receiver.toLowerCase().replace(/^0x/, "").padStart(64, "0");
  const value = amount.toString(16).padStart(64, "0");
  return "0xa9059cbb" + to + value;
}

export function utf8Hex(text) {
  return "0x" + Array.from(new TextEncoder().encode(text), (byte) => byte.toString(16).padStart(2, "0")).join("");
}

export function activeChains(config) {
  return config.chains.filter((chain) => /^0x[0-9a-fA-F]{40}$/.test(chain.receiver));
}
