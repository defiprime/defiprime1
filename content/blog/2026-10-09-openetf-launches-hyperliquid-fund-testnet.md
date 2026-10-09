---
layout: blog
title: "OpenETF launches tokenized fund testnet on Hyperliquid"
url: /openetf-launches-hyperliquid-fund-testnet.html
h1title: "OpenETF launches tokenized fund testnet on Hyperliquid"
pagetitle: "OpenETF launches Hyperliquid fund testnet"
metadescription: "OpenETF has opened a Hyperliquid testnet for tokenized trading funds, with wallet-held shares, rule-based redemptions and managed execution."
category: blog
featured-image: /images/blog/openetf-launches-hyperliquid-fund-testnet-ogp.png
intro: "OpenETF has opened a testnet for Hyperliquid trading funds whose shares can be held and transferred as tokens."
author: sawinyh
tags: ["News"]
date: 2026-10-09T13:19:13+00:00
---

At 04:23 UTC on October 6, OpenETF [introduced](https://x.com/openetfxyz/status/2107325794817372294) a testnet system that turns Hyperliquid portfolios into funds with wallet-held share tokens. The current deployment uses test assets with no value, and the [documentation](https://docs.openetf.xyz/) says real funds have no place in it.

The product gives each fund a name, symbol, public terms and an ERC-20-compatible share token. A manager trades the portfolio on Hyperliquid while investors hold the shares in their own wallets. The first release accepts subscriptions in $USDC at net asset value, with a minimum subscription of 100 $USDC unless the manager sets a higher floor.

## How the fund spans Hyperliquid

Each fund is a vault that operates across HyperCore and HyperEVM. The vault contract on HyperEVM issues shares, prices subscriptions and redemptions, and pays holders. The same vault acts as the trading account on HyperCore, where it holds and trades the portfolio. The contract reads HyperCore directly, so the docs say a subscription or redemption uses on-chain portfolio data in the same transaction.

That structure separates ownership from trading authority. Investors keep the share tokens. The manager directs trading but never receives the vault's trading key and has no withdrawal path through the contract or OpenETF's execution service. This does not remove manager risk. A manager, or an attacker who gains trading authority, can still damage the fund through losing or abusive trades.

OpenETF also sits in the execution path. Its shared service checks every order against the fund's rules before signing it. Trading therefore depends on that service. The same dependency currently applies when the system prices new redemptions and raises the cash needed to pay them. The planned Mandate layer, which would enforce each manager's published trading limits on every order, is still marked as coming soon.

Managers can create a fund without approval or a creation fee. A manager must buy at least 100 $USDC of the same shares sold to investors and select a commitment ratio of at least 5%. The manager cannot reduce their holding below that ratio. Eligible portfolios can use Hyperliquid's main exchange perpetuals, eligible spot markets and admitted HIP-3 markets. The docs state that there is no exposure cap for an individual supported market.

## Subscriptions, fees and exits

Investors subscribe and redeem in $USDC at net asset value. Redemptions can be requested at any time without a lock-up, minimum size or manager approval. Shares transfer between wallets with their redemption rights. Every subscription, redemption and daily accounting point leaves a receipt that users can recompute, while each fund has a Passport containing sourced facts about its terms and history.

A redemption can still take time. OpenETF's service may need to unwind positions and raise cash on HyperCore before moving it to HyperEVM for payment. Trading losses or market conditions can also reduce the amount ultimately paid.

For a holder, the absence of manager approval removes one discretionary exit gate, but it does not make redemption automatic or immediate. The execution service still prices the request and turns portfolio positions into cash. A transferable share also carries the redemption right to its new wallet, so custody of the token determines who can present that claim. Users therefore need to assess both the manager's strategy and the platform dependencies before treating the share like an immediately redeemable balance.

The testnet applies an exit adjustment fee to each priced redemption portion except the final shares leaving a fund. The fee starts at 0.1%, adds 0.05% for each unit of notional leverage, and is capped at 1%. It stays in the fund for remaining holders rather than going to the manager or OpenETF.

Managers choose a performance fee from 0% to 50% of pooled profit, with a 20% default, and a management fee from 0% to 2% a year, with a 0% default. Both rates freeze when the fund issues shares. That makes the terms visible before a subscription, but it does not protect an investor from leverage, thin markets or a poor strategy.

The fee design separates compensation for the manager from the cost assigned to an exiting holder. Performance fees settle yearly against pooled profit, while management fees accrue as an annual rate. The exit adjustment is different: it stays inside the fund and rises with notional leverage until it reaches the 1% cap. A prospective holder can inspect those fixed manager rates before subscribing, then compare them with the portfolio's market exposure and the extra cost that leverage can add at redemption.

## What changes from Hyperliquid vaults

OpenETF presents the product as a different wrapper around managed Hyperliquid strategies. In its comparison, a legacy Hyperliquid user vault records an internal $USDC balance, charges a 10,000 $USDC creation fee and imposes a one-day lock after a deposit. OpenETF instead gives the investor a transferable share token, charges no creation fee and has no redemption lock-up. The manager starts with 100 $USDC of their own capital.

The share token opens another route for integrations because wallets and applications can read it as a standard token. Collateral use and deeper integrations remain roadmap items rather than current functions. The roadmap also lists allowlisted subscriptions, AI-assisted fund creation, HIP-4 outcome markets, HyperEVM DeFi positions and funds holding other OpenETF funds.

The main user trade-off is visible in the control model. A manager cannot simply withdraw the portfolio, yet investors rely on OpenETF's execution service, Hyperliquid and $USDC. They also bear the strategy's trading losses and may wait while positions are unwound for a redemption. The docs describe the deployment as testnet only and do not give a dated mainnet launch. The next unresolved milestone is when OpenETF will open the system to assets with value and whether the Mandate controls will be live before that happens.
