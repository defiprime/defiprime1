---
git-date:
layout: [blog]
title: "Papertrade Before Launch: Mechanism Design, Marketing Gaps, and the Questions the Docs Don't Answer"
permalink: papertrade-hyperliquid-1000x-perps
h1title: "Papertrade Before Launch: What the Docs Show and the Marketing Hides"
pagetitle: "Papertrade Before Launch: Mechanism Design, Marketing Gaps, and the Questions the Docs Don't Answer"
metadescription: "Papertrade.xyz's marketing pitches 1000x leverage synthetic perps; the trading interface is still 'coming soon'. The docs and Martin Galer whitepaper describe a peer-vs-pool casino on Hyperliquid with a zero-LP bootstrap. Here's what the design buys, what the framing buries, and what the protocol doesn't say."
category: blog
featured-image: /images/blog/papertrade-hyperliquid-1000x-perps-ogp.png
intro: "Papertrade.xyz's marketing pitches 1000x leverage synthetic perps; the trading interface is still 'coming soon'. The docs and Martin Galer whitepaper describe a peer-vs-pool casino on Hyperliquid with a zero-LP bootstrap. Here's what the design buys, what the framing buries, and what the protocol doesn't say."
author: sawinyh
tags: ["Analysis"]
---

The papertrade.xyz front page says "trade coming soon" in small text under the 1000x-leverage marketing copy. The trading interface isn't live, the mobile app isn't live, the agent integration isn't live. What is live is a docs site at [docs.papertrade.xyz](https://docs.papertrade.xyz/) and a [whitepaper](https://docs.papertrade.xyz/martingaler-whitepaper.pdf) — *Martin Galer: A Bootstrapping Mechanism for Sustainable Asynchronous Speculation Games of Chance* — authored by Jez (@izebel_eth) and Blurr, the latter known on-chain as "Refund Contract Deployer." This piece is a pre-launch read of the design. Nothing is on chain yet; nothing in here is observed product behavior. It is what the docs commit to and what the marketing leaves out.

The headline shape of the product is straightforward. Papertrade is a peer-vs-pool synthetic perp running on HyperEVM that uses Hyperliquid's best-bid/offer precompile as a price oracle. No order book, no matching engine, no other trader on the other side; the protocol's internal LP is the counterparty on every trade. The LP starts at $0 and is designed to grow only from cumulative user losses. The native token, PAPER, is minted exclusively to traders who close at a loss. None of this is hidden in the docs. All of it is hidden in the marketing.

That gap between docs and marketing is the first thing worth being clear about, because the rest of the analysis depends on which document you trust as the protocol's self-description.

## What the Docs Commit To, in Plain Language

Stripped of jargon, the design is a casino with a few unusual properties.

The price comes from Hyperliquid. Papertrade reads the BBO precompile at `0x000000000000000000000000000000000000080e`, takes the midpoint of the best bid and best ask on Hyperliquid's native order book, and uses it as both the entry price and the exit price for synthetic positions opened against the LP. No perpetual contract actually trades on Hyperliquid through papertrade. There is no funding cost in the protocol, because no real perp position is being held; there is no slippage at execution, because the trade clears at a precompile-read mid regardless of size.

The LP doesn't exist yet. There is no seed deposit, no pre-fund, no LP onboarding flow at all. The first time it has any USDC in it will be after a real user closes at a loss on the live protocol. Three buckets handle the accounting: a treasury (the LP balance, never negative), a side bucket (parked LP gains while the queue is non-empty), and a FIFO payout queue of unpaid winning closes. When a user wins and the LP can pay, they're paid. When the LP can't pay, the profit portion of the win goes to the back of the queue and the user's margin is returned immediately. When a user loses, the loss credits the LP if the queue is empty or parks in the side bucket if it isn't. A permissionless `harvest()` keeper drains the side bucket into queue payouts. Net protocol equity is `treasury + sideBucket − queueTotal`, and the docs explicitly note this can go negative.

The token is fair on supply, not on governance. PAPER has zero pre-mint, no team allocation, no VC allocation, no airdrop, no vesting. Every token has to be minted through one specific path: a trader closing at a loss or being liquidated. The mint rate is 100 PAPER per $1 of LP gain while the LP is below $2M (including underwater); above $2M the rate decays as `100 × (S / (S + H))²` with `S = $120M`. A strict high-water-mark ratchet means stakers can drain LP without resetting the rate. Stakers earn USDC dividends out of LP revenue: a continuous share of every settlement that credits the LP, plus a sweep of any LP balance above $5M.

Trading isn't actually free. The protocol charges no fee on notional, no spread, no funding, and the relayer covers gas. What it does charge is an asymmetric impact curve on winning closes only, adapted from Rollbit. The scale factor is steepest on the smallest moves and softens as the move grows; the docs publish the formula. Losing closes pay the full loss with no haircut on top. A 0.2 basis-point jitter-protection deadband zeros sub-spread wins. Trailing per-asset open-interest caps prevent an attacker who briefly distorts Hyperliquid's BBO from sizing into the distortion.

Live markets at launch are BTC and ETH, with up to 1000x leverage and a per-user position cap of $10M. The contract owner can list any Hyperliquid perp through a 7-day timelock, including HIP-3 markets.

## The Genuine Contribution

The Martin Galer mechanism is the part of the design that's worth taking seriously on its own terms. Onchain casinos have historically needed bankrolls — SatoshiDice (2012), Bustabit (2015), Etheroll (2017), EtherCrash (2018) all needed an LP seeded upfront so winners could be paid on demand. That requirement made every onchain casino either custodial in spirit or a token-incentive game, and in EtherCrash's case the LP got drained by a bad actor and the protocol died.

The Martin Galer payout queue removes the seed requirement. The cost is that winners might have to wait, but only on the profit portion of a winning close, and only when the LP is in deficit. Margin is always returned. The cost is real but contained, and the mechanism makes onchain speculation games launchable without raising risk capital up front. As a contribution to the lineage of bankroll-free game design, it's a real piece of work.

The PAPER tokenomics are similarly clean as a supply mechanism. Every token comes from a documented on-chain loss. The mint curve is front-loaded so early variance-takers are rewarded most. The ratchet ensures the rate decays monotonically. Stakers absorb the LP's variance through a continuous USDC dividend rather than a vesting schedule. Compared to recent "fair launch" attempts that ship with significant insider allocations behind cliff vests (Friend.tech) or where the bootstrap actually depended on a separate pre-funded incentive pool (most LRT protocols' "points" phases), PAPER's supply story is cleaner than most.

Whether the Chitra-Angeris CFMM citations in the whitepaper actually load-bear the mechanism is a separate question. The Martin Galer queue itself is a FIFO scheme with a solvency-ratio check; the heavy CFMM math doesn't show up in the actual protocol logic. The references function more as a signal of academic-mindedness than as proof of mechanism quality.

## The Counter-Read That Doesn't Get Disclosed

The thing the docs are careful about and the marketing isn't: papertrade is a leveraged speculation product with an asymmetric payout curve where winners are scaled, losers pay in full, and the protocol's economic engine depends on aggregate user flow being negative-EV for the user.

At 1000x leverage on BTC or ETH with a 5-basis-point bust-price buffer, the per-trade dynamics are punishing for the user. Maintenance margin extrapolated from Hyperliquid's documented formula would put liquidation around a 5-basis-point adverse move. Add the asymmetric impact haircut that's steepest on small moves and the 0.2-basis-point deadband that zeros sub-spread wins, and the trader needs a directional move large enough to escape the steep part of the curve, fast enough to avoid bust, without sitting in position long enough for the buffer to bite. The expected return per trade for an uninformed trader is meaningfully negative. That's the design. The LP can bootstrap from zero precisely because the design is structurally trader-unfriendly enough to guarantee losses on aggregate.

The whitepaper is explicit about this — it describes the protocol as a "game of chance" and walks through worked examples of fair coin flips and games with positive house edge. The marketing page is not. The marketing page says "perpetual futures exchange," "1000x leverage," "0 slippage," "0 market impact," "no funding costs," "no trading fees." It does not say "casino." It does not say "house edge." It does not say "the LP needs you to lose for the protocol to work."

That gap is not an accident. "Onchain casino" is a regulatory category. "Perpetual futures exchange" is a different one, and the second one has more room to operate in the US and EU. The team is anonymous (Jez/@izebel_eth and Blurr, the latter previously deployed a refund contract on Ethereum and is otherwise unidentified) which is consistent with regulatory caution about who carries the legal exposure of a product distributing leveraged speculative payouts to US users. None of this is dispositive, but a defiprime reader should know the framing choice is doing work.

## The Risks the Docs Note and the Risks They Don't

The docs are direct about three protocol-level risks. Queue overhang during the early life of the protocol means winning closes can wait for the LP to refill. A 7-day timelock on the contract owner gives users a week to exit before any parameter change or implementation upgrade. A known race-condition bug on the deposit sweep is mitigated by a separate 7-day-timelock admin key whose only job is to credit orphaned deposits. The team flags all of these.

The risks the docs don't engage with are at least as material.

Oracle dependency on Hyperliquid is not zero just because there's no HIP-3 relationship. Papertrade's execution price is Hyperliquid's BBO mid. The impact curve and OI caps defend against sub-spread manipulation. They do not defend against a coordinated attack on Hyperliquid's order book itself — the JELLYJELLY incident from March 2025 showed validators willing to intervene in cases where book-level manipulation distorts a thin perp market. Papertrade reads BBO on BTC and ETH spot, which are deep, but the dependency is real and the protocol has no fallback feed.

Governance is centralized despite the fair-launch framing. The contract owner sits behind a 7-day timelock and can rewrite every parametric knob in the system: the flat-region mint rate, the $2M threshold, the $120M decay scale, the impact curve constants per market, the OI caps, the bust-price buffer, the fee rates. PAPER is fair in *supply*. It is not fair in *governance*. A future owner action could materially change which traders mint how much PAPER, what the LP captures per losing trade, and what stakers earn. The timelock is the right mitigation. It is not no mitigation.

Regulation is the largest unaddressed surface. A protocol that offers 1000x leverage on synthetic price exposure, takes losses through what the whitepaper calls a "house edge," distributes the proceeds as USDC dividends to token holders, and is operated by an anonymous team is on every relevant regulator's radar. The CFTC, the SEC, and the FCA have all moved against substantially similar products in 2024-2025. The Rollbit framing the docs invoke is also the framing that has drawn regulatory attention. The team's anonymity, the offshore-leaning structure, and the omission of "casino" or "speculation" language from the marketing all read as design responses to a regulatory environment the docs do not name.

Aggregate-EV failure is the mathematical risk. The Martin Galer mechanism only settles if cumulative user flow is positive-EV for the LP across time. At 1000x with the documented impact curve, it almost certainly is for an uninformed trader population. If the realised user base is dominated by traders with edge — automated systems exploiting BBO jitter inside the impact curve's tolerance, or insiders trading parameter changes — the queue grows without bound and the protocol never settles. This is structurally unlikely but not zero.

## What's Worth Watching, If You're Watching

Once papertrade ships and the trading interface goes live, the data that matters won't be the leverage offer. It'll be more concrete:

The first ~$2M of LP growth is the flat-rate window. The rate at which the LP fills through this window is the realised house edge — the speed at which 100-PAPER/$1 mints accumulate against actual user losses. If the LP fills slowly, the protocol is closer to fair to users than the design implies. If it fills fast, the design works as advertised, which is bad for users and good for early stakers.

The queue overhang ratio is the user-experience proxy. The closer queue total runs to LP balance, the more often winning closes will wait. Early protocol life will look queue-heavy by definition; the question is how quickly the queue clears once aggregate flow tips into positive-EV territory for the LP.

The first owner action through the timelock will tell you what kind of protocol governance is in practice. A trivial parameter tweak is the boring outcome. An impact-curve recalibration in either direction is informative. A mint-curve constant change is a serious signal about how the team thinks about the existing PAPER holder base.

And the regulatory surface will move first — either because the team de-anonymizes ahead of an institutional relationship, or because a regulator names the product and the team makes a structural change in response, or because nothing happens for long enough that the omission becomes the answer.

What papertrade is, in the end, depends on which document you trust. The docs describe a serious mechanism-design exercise with a real contribution to the onchain speculation-game lineage and an unusually clean supply-side tokenomics design. The marketing describes a leveraged perpetual futures exchange. The team has chosen to publish both. A practitioner reading defiprime should hold both in view: this is a more carefully reasoned piece of casino engineering than most onchain casinos, and it is a leveraged speculation product whose regulatory positioning depends on no one calling it that out loud. Both readings are accurate. They are not the same protocol.

For related defiprime coverage on Hyperliquid: [Hyperliquid vs. Aster](/hyperliquid-vs-aster) and the [Hyperliquid Chain ecosystem deep dive](/hyperliquid-chain-deep-dive). The product page for [Hyperliquid](/product/hyperliquid) sits in the [perps](/perps) collection.
