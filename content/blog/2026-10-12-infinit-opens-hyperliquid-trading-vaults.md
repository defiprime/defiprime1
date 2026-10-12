---
layout: blog
title: "INFINIT opens managed trading vaults on Hyperliquid"
url: /infinit-opens-hyperliquid-trading-vaults.html
h1title: "INFINIT opens managed trading vaults on Hyperliquid"
pagetitle: "INFINIT launches Hyperliquid trading vaults"
metadescription: "INFINIT's managed vaults use multisig custody, restricted trading credentials and risk controls, with the next APEX deposit window opening October 28."
category: blog
featured-image: /images/blog/infinit-opens-hyperliquid-trading-vaults-ogp.png
intro: "INFINIT has introduced managed trading vaults that accept $USDC and run fixed-term strategies through restricted Hyperliquid trading accounts."
author: sawinyh
tags: ["DeFi", "News"]
date: 2026-10-12T19:18:30+00:00
---

At 12:02 UTC on October 12, 2026, INFINIT [introduced its managed trading-vault framework](https://x.com/Infinit_Labs/status/2109615759022555510), with APEX Multi-Strategy as the first named vault. The framework restricts vaults to eligible Hyperliquid markets with at least $100 million in open interest.

Depositors enter with $USDC during a defined window and receive a receipt token representing their share. A strategy manager trades for a fixed term. At the end, holders can redeem the receipt token for their share of the vault's $USDC value after fees. Each manager sets the fees, lock period, deposit window, risk limits and strategy before deposits open.

This structure gives the manager trading authority without giving it withdrawal access. INFINIT says deposits sit behind a 3-of-4 multisig, with keys divided between INFINIT and the operating team. Trading credentials can open and close positions but cannot withdraw depositor funds. The company also publishes a shared trading wallet and provides weekly performance reports to depositors.

## How the controls work

INFINIT calls the common infrastructure INFINIT OS. It covers strategy research and testing, vault setup, accounting for depositor shares, controlled execution, risk monitoring and investor reporting. The company says it also supports legal structuring, regulated fund licensing and fund administration for strategy managers.

Managers must pass what INFINIT calls the INFINIT Standard before they can take deposits. The manager and its beneficial owners must complete identity checks and screening. The manager must contribute first-loss capital alongside depositors and show a live trading record rather than relying only on a backtest. It must also declare market, leverage, exposure and drawdown limits.

The trade gateway enforces those restrictions at order entry. It blocks orders outside the approved market list and any order that violates the vault's declared restrictions. Monitoring agents separately compare trading activity with the manager's published mandate and risk limits. INFINIT's risk team reviews suspected breaches. The manager must correct a confirmed breach, while an unresolved breach causes INFINIT to pause trading access.

The custody design separates several powers, but depositors still depend on INFINIT's controls and the operating team's key arrangement. A strategy can produce trading losses within its permitted mandate. Receipt-token redemption also occurs at the end of a fixed term, rather than as an on-demand withdrawal described in the announcement. Fees differ by manager and must be read in the terms for the specific vault.

The manager-screening process adds another layer before a vault can collect deposits. INFINIT requires identity checks for the manager and its beneficial owners. It also requires a live trading record and first-loss capital from the manager. That capital puts manager funds in the same strategy, but the announcement does not state the amount or the loss-allocation sequence. Those details belong in the vault terms that prospective depositors receive before a window opens.

Declared risk limits cover markets, leverage, exposure and drawdown. They are separate from the manager's investment thesis. A permitted losing position can comply with all four limits. Conversely, an order can fit the thesis and still be rejected if it falls outside an approved market or another declared restriction. Depositors need both parts of the disclosure to understand what the manager intends to trade and what the gateway will allow.

The $100 million open-interest threshold narrows the Hyperliquid market set available to each vault. INFINIT says the gateway automatically blocks orders outside that eligible list. The announcement does not say how often open interest is measured or what happens when an already-open market falls below the threshold. That is a practical rule to check in each vault's disclosed risk controls.

INFINIT says receipt tokens represent depositor shares and that integrations with other DeFi protocols are planned. That makes the current receipt an accounting and redemption claim under the vault terms. The announcement does not identify a live lending, collateral or secondary-market integration for it.

## The first vault trades a neutral book

APEX Multi-Strategy is the first vault under the framework. Apex Quantitative Capital operates it. INFINIT says the team's members have close to 50 years of combined experience across banks, buy-side institutions, crypto trading firms and exchanges.

The strategy is a systematic CTA momentum model. Its AI-led engine ranks markets by relative strength, goes long the strongest and shorts the weakest across stocks, commodities and crypto. INFINIT says the book stays dollar-neutral so returns come from market selection. Equity and commodity exposure comes through perpetual contracts on Hyperliquid, and all APEX returns come from trading profit and loss.

For depositors, the distinction between transparent positions and enforceable limits matters. The shared wallet lets them inspect activity, while weekly reports cover performance, exposure and trading. Neither replaces the disclosed mandate. The gateway determines which orders are allowed, and INFINIT's monitoring process determines how a suspected breach is escalated.

The open question is how consistently those controls will constrain a live manager during fast markets. INFINIT's announcement describes automatic order blocking, agent monitoring and a human risk review, but it does not publish latency, intervention thresholds or a completed audit in the announcement. Prospective depositors will need the vault-specific risk controls, audit details, fees and lock-up period that managers must disclose before accepting funds.

## The next deposit window

INFINIT says onchain lending-vault deposits grew from $1.5 billion in September 2024 to $10 billion in September 2026. It presents trading vaults as a separate extension of managed onchain products. The comparison is context supplied by INFINIT, not a measure of deposits already committed to its trading vaults.

The next operational dates concern APEX. Vault 1 becomes redeemable on October 28, 2026. INFINIT says Vault 2 is separate, so existing holders must redeem from Vault 1 before depositing into Vault 2. The next APEX Multi-Strategy deposit window is planned for October 28 through November 11, 2026, with participation details still to be announced.
