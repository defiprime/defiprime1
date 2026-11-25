import { createPublicClient, http } from "viem";
import checkout from "../data/listing_checkout.json" with { type: "json" };
import { d1ClaimsStore } from "./claims-store.mjs";
import { sendEmail } from "./notify.mjs";
import { checkReady, handleSubmission } from "./submit.mjs";

const MAX_BODY_BYTES = 16384;

function json(payload, status, extraHeaders = {}) {
  return Response.json(payload, { status, headers: { "cache-control": "no-store", ...extraHeaders } });
}

async function listing(request, env) {
  const store = d1ClaimsStore(env.DB);
  if (request.method === "GET") {
    const [status, payload] = await checkReady({ checkout, store, env });
    return json(payload, status);
  }
  if (request.method !== "POST") return json({ error: "Use GET or POST" }, 405, { allow: "GET, POST" });
  const text = await request.text();
  if (text.length > MAX_BODY_BYTES) return json({ error: "Submission is too large" }, 413);
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    return json({ error: "Invalid JSON" }, 400);
  }
  const [status, payload] = await handleSubmission(body, {
    checkout,
    clientFor: (chain) => createPublicClient({ transport: http(env[`LISTING_RPC_${chain.id}`] || chain.rpc) }),
    store,
    notify: (record, chain) => sendEmail(record, chain, env),
  });
  return json(payload, status);
}

function tagPageAtHtmlUrl(request, env, url) {
  const extensionless = new URL(url);
  extensionless.pathname = url.pathname.slice(0, -".html".length);
  return env.ASSETS.fetch(new Request(extensionless, request));
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/listing") return listing(request, env);
    if (url.pathname.startsWith("/t/") && url.pathname.endsWith(".html")) return tagPageAtHtmlUrl(request, env, url);
    return env.ASSETS.fetch(request);
  },
};
