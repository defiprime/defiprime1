import { getStore } from "@netlify/blobs";
import { createPublicClient, http } from "viem";
import checkout from "../../data/listing_checkout.json" with { type: "json" };
import { sendEmail } from "../lib/notify.mjs";
import { handleSubmission } from "../lib/submit.mjs";

const MAX_BODY_BYTES = 16384;

function clientFor(chain) {
  return createPublicClient({ transport: http(process.env[`LISTING_RPC_${chain.id}`] || chain.rpc) });
}

function claimsStore(context) {
  const scope = context?.deploy?.context === "production" ? "production" : "preview";
  return getStore({ name: `listing-claims-${scope}`, consistency: "strong" });
}

export default async (request, context) => {
  if (request.method !== "POST") return Response.json({ error: "Use POST" }, { status: 405 });
  const text = await request.text();
  if (text.length > MAX_BODY_BYTES) return Response.json({ error: "Submission is too large" }, { status: 413 });
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    return Response.json({ error: "Invalid JSON" }, { status: 400 });
  }
  const [status, payload] = await handleSubmission(body, {
    checkout,
    clientFor,
    store: claimsStore(context),
    notify: sendEmail,
  });
  return Response.json(payload, { status });
};

export const config = { path: "/api/listing" };
