---
layout: blog
title: "MetaMask brings Agent Wallet to Grok Bot, with deposit-only perps limits"
url: /metamask-grok-bot-wallet-guardrails.html
h1title: "MetaMask brings Agent Wallet to Grok Bot, with deposit-only perps limits"
pagetitle: "MetaMask Grok Bot wallet: where trading guardrails stop"
metadescription: "MetaMask Agent Wallet is live on Grok Bot. Guard Mode limits Hyperliquid deposits, not leveraged positions, while vault supply routes through LiFi."
category: blog
featured-image: /images/blog/metamask-grok-bot-wallet-guardrails-ogp.png
intro: "MetaMask has opened Agent Wallet to Grok Bot, with wallet controls that check Hyperliquid funding but leave subsequent position sizing to the trader and agent."
author: sawinyh
tags: ["News"]
date: 2026-10-28T22:21:51+00:00
---

On October 28, 2026, MetaMask [made Agent Wallet available as a Grok Bot plugin](https://metamask.com/news/metamask-agent-wallet-grok-bot), giving the agent access to swaps, bridges, Hyperliquid perpetuals, Polymarket and yield vaults. Its recommended Guard Mode imposes a rolling 24-hour outflow limit. For perpetuals, that limit checks the deposit into Hyperliquid, not the positions the agent opens afterward.

The plugin connects an existing wallet product to Grok Bot, an always-on agent running on its own cloud computer. MetaMask says it simulates and threat-scans supported transactions before execution. The checks depend on the venue. A swap passes through wallet controls directly; trading on an already-funded Hyperliquid account sits outside them.

## What the wallet checks

In server-wallet mode, signing keys stay inside a trusted execution environment. Grok Bot can request transactions without accessing the user's main wallet or Secret Recovery Phrase. MetaMask says it scans supported transactions with Blockaid and routes them through Smart Transactions with MEV protection where the chain supports it.

Guard Mode adds network, address and recipient allowlists to the outflow budget. An action outside those boundaries pauses for approval through an email link or MetaMask Mobile push notification. The wallet enforces these controls separately from instructions given to the agent.

Beast Mode removes the allowlist and spending-limit layer. According to MetaMask's [security explanation](https://metamask.io/news/agentic-wallet-security), threat scanning stays active in both modes. Transactions flagged as malicious or contracts flagged as risky still require two-factor approval. The mode determines which otherwise legitimate transactions can proceed unattended.

For a swap or bridge, the wallet evaluates the transaction amount against the outflow limit. MetaMask warns against asking Grok Bot to retry a swap while it waits for approval, because the retry risks a duplicate. The pending request needs approval before execution.

Polymarket separates deposits from orders. Funding the account counts as an outflow, while placing and canceling orders happen off-chain on its order book. Guard Mode does not evaluate each order. Grok Bot flags regional access restrictions during setup.

## Hyperliquid exposure can exceed the funding limit

MetaMask's [perpetuals guide](https://metamask.io/news/trade-perps-metamask-agent-wallet) describes the deposit as the sole EVM transaction in the workflow that its wallet controls evaluate. Threat scanning applies in both modes, and Guard Mode also checks the deposit against the outflow budget. The trading-mode controls apply to server wallets, not bring-your-own-wallet setups.

Opening, modifying and closing Hyperliquid positions do not consume that budget. These actions bypass wallet-level threat scanning, allowlist checks and two-factor authentication, regardless of their size. The guide gives an example of a $2,000 deposit followed by a $50,000 position at 25x leverage. The wallet checks the deposit; the position receives no second wallet-level check. MetaMask uses these amounts as an illustration, not a record of observed trades.

The funding command sources $USDC from Arbitrum by default. Users funding from another chain must specify the source chain. Collateral already in the venue's spot balance can instead move into its perpetuals balance. The deposit sets how much collateral reaches the venue, while the subsequent order determines leveraged exposure.

Both opening and closing commands accept a maximum slippage cap in basis points. MetaMask's guide says the documentation publishes no default for that cap. An agent instructed to close a position needs an exit constraint as well as any constraint supplied when opening it.

## Vault routing and approvals

The plugin also includes Agent Wallet's yield-vault workflow. The [vault documentation](https://docs.metamask.io/agent-wallet/guides/earn-yield-vaults/) says the agent lists available vaults, compares APYs and TVL, confirms the user's choice and executes. Users can filter discovery by chain, token, protocol and minimum TVL. Supplying a vault address bypasses automatic selection.

The positions query defaults to the active wallet, but accepts another wallet address. It can filter existing holdings by chain, token, protocol or vault, separately from the market-discovery command used to select a new allocation.

Supply and withdrawal operations route through LiFi for cross-chain support. Cross-chain supply combines bridging and supplying in one operation. The source token is required whenever the source chain differs from the vault's chain. The CLI polls for completion with a 10-minute timeout. A request to supply funds can involve a bridge before the funds reach the destination vault.

The CLI automatically handles token approval when the vault's allowance is insufficient. On a first supply, it sends an approval transaction before the supply transaction. In server-wallet mode, that approval may require two-factor authentication depending on the trading mode. Withdrawal supports a specified amount or the full position. For Aave rebasing aTokens, the full-withdrawal option uses a small dust buffer to account for interest accrued between the balance query and execution.

Transaction Protection covers only some of the risks of these positions. The launch announcement advertises coverage for eligible transactions that pass the wallet's checks. MetaMask's security explanation describes Transaction Shield reimbursement of up to $10,000 a month in $mUSD. It explicitly excludes ordinary market losses, protocol-level exploits, compromised keys or recovery phrases, and peer-to-peer transfers. A vault exploit or a losing leveraged trade falls outside the listed protection.

## Setup determines which wallet gets funded

The plugin includes an Agent Wallet skill describing the commands and when the agent must ask permission. At the start of a new session, it checks whether the CLI is installed and signed in. If installation is needed, Grok Bot asks first. The plugin does not install it autonomously.

The sign-in method determines the wallet address. Google, passwordless email and MetaMask Mobile QR resolve to different server wallets, even when the same email is used. An account funded under one method will appear unfunded after switching to another. The perpetuals guide says the collateral remains at the original address.

The published perps guide leaves the default slippage cap unspecified. Orders submitted without an explicit cap depend on the CLI's unstated setting.
