import {
  baseUnits,
  claimMessage,
  cleanFields,
  submissionDigest,
  transferCalldata,
  utf8Hex,
} from "./listing-core.mjs";

const STORAGE_KEY = "defiprime-listing-pending";
const POLL_MS = 6000;
const POLL_LIMIT = 100;
const FINAL_REFUSALS = [400, 402, 403, 409];

const root = document.getElementById("listing-checkout");
const form = root?.querySelector("form");
const statusLine = root?.querySelector("[data-status]");
const payButton = root?.querySelector("[data-pay]");
const resumePanel = root?.querySelector("[data-resume]");
const checkout = root ? JSON.parse(root.dataset.config) : null;

function say(text, tone = "info") {
  statusLine.textContent = text;
  statusLine.dataset.tone = tone;
}

function selectedPayment() {
  const [chainId, symbol] = form.elements.payment.value.split(":");
  const chain = checkout.chains.find((candidate) => String(candidate.id) === chainId);
  const token = chain?.tokens.find((candidate) => candidate.symbol === symbol);
  return { chain, token };
}

function formFields() {
  const data = new FormData(form);
  return Object.fromEntries(Array.from(data.entries()).filter(([name]) => name !== "payment"));
}

function walletError(error) {
  if (error?.code === 4001) return "You cancelled the request in your wallet.";
  if (error?.code === 4902) return "Add this network to your wallet first, then try again.";
  return error?.message || "The wallet returned an error.";
}

async function ensureChain(provider, chainId) {
  const hex = "0x" + chainId.toString(16);
  if ((await provider.request({ method: "eth_chainId" })) === hex) return;
  await provider.request({ method: "wallet_switchEthereumChain", params: [{ chainId: hex }] });
}

function savePending(pending) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(pending));
}

function loadPending() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY));
  } catch {
    return null;
  }
}

async function deliver(pending) {
  for (let attempt = 0; attempt < POLL_LIMIT; attempt += 1) {
    let response;
    try {
      response = await fetch("/api/listing", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(pending),
      });
    } catch {
      say("Network error. Retrying...");
      await new Promise((resolve) => setTimeout(resolve, POLL_MS));
      continue;
    }
    const payload = await response.json().catch(() => ({}));
    if (response.status === 200) {
      localStorage.removeItem(STORAGE_KEY);
      form.hidden = true;
      resumePanel.hidden = true;
      say("Payment confirmed and submission received. We review every listing and reply by email.", "success");
      return;
    }
    if (!FINAL_REFUSALS.includes(response.status)) {
      say(`${payload.reason || payload.error || "Waiting for the chain"}. Keep this page open.`);
      await new Promise((resolve) => setTimeout(resolve, POLL_MS));
      continue;
    }
    say(`${payload.error || `Submission refused (${response.status})`}. If you paid, message us on Telegram (t.me/defiprime) with transaction ${pending.txHash} and we will sort it out.`, "error");
    return;
  }
  say("Still waiting on the chain. Your submission is saved in this browser; reopen this page later to finish it.", "error");
}

async function pay(event) {
  event.preventDefault();
  const cleaned = cleanFields(formFields());
  if (cleaned.error) {
    say(cleaned.error, "error");
    form.elements[cleaned.field]?.focus();
    return;
  }
  const { chain, token } = selectedPayment();
  if (!chain || !token) return say("Choose a network and stablecoin.", "error");
  const provider = window.ethereum;
  if (!provider) return say("No browser wallet found. Install MetaMask, Rabby or another EVM wallet and reload.", "error");

  payButton.disabled = true;
  try {
    say("Checking that checkout is available...");
    const ready = await fetch("/api/listing", { cache: "no-store" }).then((response) => response.ok).catch(() => false);
    if (!ready) {
      say("Checkout is temporarily unavailable, so nothing was charged. Please try again later.", "error");
      return;
    }
    say("Connect your wallet...");
    const [account] = await provider.request({ method: "eth_requestAccounts" });
    say(`Switching to ${chain.name}...`);
    await ensureChain(provider, chain.id);
    say("Step 1 of 2: sign the submission in your wallet. This is free.");
    const digest = await submissionDigest(cleaned.fields);
    const message = claimMessage({ project: cleaned.fields.project, chainId: chain.id, digest });
    const signature = await provider.request({ method: "personal_sign", params: [utf8Hex(message), account] });
    say(`Step 2 of 2: confirm the ${checkout.price} ${token.symbol} payment in your wallet.`);
    const txHash = await provider.request({
      method: "eth_sendTransaction",
      params: [{ from: account, to: token.address, data: transferCalldata(chain.receiver, baseUnits(checkout.price, token.decimals)) }],
    });
    const pending = { fields: cleaned.fields, chainId: chain.id, txHash, signature };
    savePending(pending);
    say("Payment sent. Waiting for confirmations...");
    await deliver(pending);
  } catch (error) {
    say(walletError(error), "error");
  } finally {
    payButton.disabled = false;
  }
}

if (root && form) {
  form.addEventListener("submit", pay);
  const pending = loadPending();
  if (pending) {
    resumePanel.hidden = false;
    resumePanel.querySelector("[data-resume-project]").textContent = pending.fields?.project ?? "";
    resumePanel.querySelector("button").addEventListener("click", () => {
      resumePanel.hidden = true;
      deliver(pending);
    });
  }
}
