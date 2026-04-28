---
git-date:
layout: [blog]
title: "On-Chain Interest Rate Swaps in 2026: Yield Stripping Won, Synthetic IRS Keeps Trying"
permalink: onchain-interest-rate-swaps-yield-stripping
h1title: "On-Chain IRS in 2026: Yield Stripping Won"
pagetitle: "On-Chain Interest Rate Swaps in 2026: Yield Stripping Won, Synthetic IRS Keeps Trying"
metadescription: "Pendle and Exponent dominate the on-chain rate market through yield tokenization. True synthetic IRS protocols keep launching and keep staying small. Here's why."
category: blog
featured-image: /images/blog/onchain-interest-rate-swaps-yield-stripping-ogp.png
intro: "Pendle and Exponent dominate the on-chain rate market through yield tokenization. True synthetic IRS protocols keep launching and keep staying small. Here's why."
author: sawinyh
tags: ["Analysis", "Yield"]
---

The on-chain interest rate swap category has been six years in the making. [Defiprime first wrote about it in 2020](/defi-interest-rate-swaps), back when SwapRate was running early order-book IRS markets and the question was whether the primitive could exist on chain at all. By 2022 Voltz had built a concentrated-liquidity virtual AMM that processed more than $20 billion in cumulative notional across its life and got benchmarked against TradFi SOFR. By April 2026 Voltz is in sunset, IPOR sits in low-single-digit-millions of TVL, and the dominant on-chain rate venue is Pendle, which technically does not run swaps at all.

What actually clears at scale on-chain is yield tokenization. Split a yield-bearing asset into a fixed-yield principal token and a floating-yield token, list both on a time-aware AMM, and the result is economically equivalent to a fixed-vs-floating rate swap on whatever underlying the asset references. Pendle has built that into a top-20 DeFi protocol by TVL with billions of monthly notional. Exponent has built the Solana version into roughly $80M of TVL and $2B in traded yield volume. Pure synthetic IRS protocols, the ones that look like the TradFi product, have not converted comparable interest into comparable scale. Kairos is the most recent attempt and the one most worth watching, but the same audience and primitive constraints that capped Voltz are still in place.

This is the part of the rates story that gets understated. The category is real, on-chain, growing, and increasingly institutional. It is also lopsided in a way that has held for three years and is unlikely to flip soon, for reasons that overlap with what the [on-chain forex post last week](/onchain-forex-asset-primitive-gap) called the asset-primitive gap and what the [40 basis point illusion](/defi-yield-risk-premium) called the demand-side audience problem.

## What's Actually Live in April 2026

Five protocols carry meaningful weight in the on-chain rate market right now. Two of them (Pendle, Exponent) drive almost all the volume. Two (Kairos, IPOR) are the active synthetic IRS attempts. One (Voltz) is the cautionary tale.

[Pendle](/derivatives) on EVM is the dominant venue. Yield-bearing assets — Lido stETH, Ethena USDe, Aave aUSDC, Morpho vault positions, restaking LRTs, Treasury-backed RWAs — get deposited into Pendle and split into PT (principal token, fixed yield to maturity) and YT (yield token, floating yield through expiry). Both trade on a time-aware AMM that adjusts liquidity as expiry approaches, with a complementary orderbook layer for tighter execution on the larger pairs. TVL has cycled between roughly $5 billion and $13 billion across 2025–2026 depending on whether stablecoin and LRT seasons are running hot, and monthly notional sits in the billions. The franchise extends now into Boros, a separate module that tokenizes perpetual funding rates from major venues like Binance and Hyperliquid into leveraged long/short rate exposure. Boros is the closest thing in the Pendle stack to a classical IRS product, and it depends on Chainlink Data Standard feeds with TWAP smoothing for the off-chain rates it imports.

[Exponent](/decentralized-lending) is the Solana counterpart, often described as the Pendle of Solana, though the architecture leans more on a hybrid orderbook-to-CLMM design than on a time-aware AMM. Users wrap variable-yield Solana DeFi positions — Jito staking (JitoSOL), Marinade (mSOL), Kamino lending and liquidity, Marginfi credit — into income tokens and yield tokens, then trade for fixed-rate exposure or leveraged variable-rate bets. The on-record figures the team highlights are roughly $2B in cumulative yield-volume traded, $250M-plus of yield settled to users, 35,000+ users, around $80M TVL, sub-second median execution, and zero security incidents since its 2024 launch. A v2 is in private beta. Pendle is also expanding onto Solana through PT issuance against Kamino positions with Chainlink CCIP wiring, which sets up the first real cross-chain rate-trading footprint.

Kairos is the active synthetic IRS attempt. The protocol launched on Ethereum mainnet in early 2026 with a beta on Base and raised $2.4M in seed funding in March. The pitch is permissionless rate-market creation: anyone can open a swap market against any oracle-supported reference rate (Aave borrow rate, Morpho vault APY, Lido stETH yield, RWA cash flows, off-chain benchmarks routed through Pyth or Stork), set tenor and collateral parameters, and let traders take leveraged fixed-vs-floating positions, with capital efficiency the team describes as up to roughly 5,000x notional-to-collateral. Positions are ERC-721 NFTs that compose into vaults and structured products downstream. Beta cumulative notional is reported at over $300M. That is real activity for a six-month-old protocol and small relative to a single day on Pendle.

[IPOR](/decentralized-lending) is the longer-running synthetic IRS protocol on EVM, live since 2022 on Ethereum, [Arbitrum](/arbitrum), and [Base](/base). It runs an AMM-based fixed-vs-floating market on top of its own decentralized rate index (the IPOR Index), originally calibrated against blue-chip stablecoin lending rates. Total TVL across deployments sits in the low single millions in early 2026. The protocol has shipped continuous improvements and has institutional partners, but it has not crossed the threshold where rate-trading flow finds it organically. Notably, IPOR weathered a mitigated oracle manipulation event early in its life when a large position spiked the underlying index — a reminder that synthetic IRS is structurally more oracle-dependent than yield stripping is.

Voltz is the precedent the category cannot avoid. The Voltz vAMM was the most capital-efficient synthetic IRS design built on-chain in its generation, ran fixed-vs-floating markets against Aave, Compound, stETH, rETH and even SOFR on Avalanche, and processed more than $20 billion in cumulative notional across its life. The protocol is being sunset in favor of a successor project, with users encouraged to wind down positions through direct contract interaction. The headline cumulative number is real; what it does not capture is that the volume came in concentrated bursts around specific yield events rather than as a continuous rate-trading flow, which is the part that matters when assessing whether the next attempt will land differently.

Older or niche projects round out the picture. Element, Tempus, and Strips were active fixed-yield or rate-trading protocols in the prior cycle and are mostly absorbed, deprecated, or running at minimal volume in 2026. Pendle holds essentially the entire EVM yield-stripping category by share of TVL and notional. Exponent holds essentially the entire Solana version of it.

## Why Yield Stripping Won

The cleanest way to frame the divergence is to look at what each design asks the user to believe.

A synthetic IRS asks the user to take a directional view on a reference rate. To use Voltz or IPOR or Kairos productively, a trader needs an opinion about where the Aave USDC borrow rate is going, or where Lido staking yield is heading, or where Binance perp funding will settle next month. The product is rate speculation. The audience for rate-direction speculation specifically — distinct from the much larger audience for locking in a yield — is small. Crypto-native traders mostly care about the directional move on the underlying asset, not the funding curve attached to it. TradFi rate desks, who do live and breathe the rate curve, do not have an incentive to migrate execution onto a permissionless venue with crypto-native counterparties when their existing prime-broker rails work fine.

Yield stripping does not require any rate view. A user holding stETH or aUSDC or a Morpho vault position can deposit into Pendle to lock in a fixed yield through expiry without forming any opinion about where rates go. They are buying certainty on an asset they already hold. That is the same product institutional fixed-income desks have used for fifty years through zero-coupon stripping of Treasury and corporate bonds. The audience for "lock in my yield" is much larger than the audience for "speculate on the curve." That is the whole game.

The architecture amplifies the demand difference. PT and YT tokens are composable ERC-20s that flow into other DeFi products. Pendle PTs sit as collateral in lending markets, get wrapped into curated yield vaults, and feed into stablecoin and LRT structured products as a fixed-yield base layer. The downstream integrations create constant rebalancing and rolling demand independent of any user actively trading rates. That is a stickiness profile that pure synthetic IRS positions do not have, because a synthetic swap does not produce composable principal-and-yield legs as a natural byproduct.

There is also an oracle-surface argument that runs in the same direction. Yield stripping produces fixed-yield tokens whose price is driven by the underlying asset price plus the time-decay of the implied yield curve. The yield is whatever the underlying actually paid, observed natively on-chain. A synthetic IRS, by contrast, references an external rate that has to be measured, smoothed, and fed to the contract for every settlement. That oracle dependency is where the failure modes live, and it is the reason the next section is its own.

## Oracle Risk Is the Synthetic-IRS-Specific Tax

Every on-chain rate product depends on oracles somewhere in the stack. The exposure is not equal across designs.

Yield-stripping protocols inherit oracle risk from the underlying yield-bearing asset. A Pendle PT on stETH depends on Lido's accounting plus the price feeds Pendle uses to mark the position; an Exponent income token on JitoSOL depends on the Solana-side feeds Pendle's Solana competitors and integrators commonly route through (Pyth being the dominant choice). The oracle surface is the same surface the underlying lending or staking protocol already lives with, plus a thin layer of timing oracles for the AMM's yield-curve math. There is no separate reference rate that has to be oracleized; the rate is whatever the asset accrues, observed directly.

Synthetic IRS protocols have to oracleize the reference rate itself. Kairos markets reference Aave borrow rates, Lido yields, RWA cash flows, or off-chain benchmarks; each one needs a feed that updates frequently enough for fair settlement and is robust against manipulation. Boros funding-rate markets reference Binance and Hyperliquid funding numbers, smoothed through TWAP windows and Chainlink Data Standard feeds. IPOR runs its own decentralized index, which is itself an oracle of last resort and is what got manipulated in the early incident.

The failure modes these protocols document in their own threat models cluster into a few patterns.

The first is manipulation through the underlying. A flash-loan attacker spikes or suppresses a lending-pool rate that a synthetic IRS references, forces settlements at off-market values, and exits before the rate normalizes. That is the shape of the IPOR-style incident. Mitigations are TWAP windows, deviation caps, and rate sources that aggregate across pools, each of which adds lag and reduces responsiveness as the cost of robustness.

The second is stale or unavailable feeds. When a rate oracle stops updating during a volatility spike or chain congestion, settlements happen at the last good price, which can diverge meaningfully from where the market actually is. Liquidations either fire incorrectly or fail to fire at all. Confidence intervals on Pyth and decentralized publisher networks on Chainlink address the failure mode without eliminating it.

The third is centralization in off-chain benchmarks. Boros funding-rate markets reference Binance and Hyperliquid, both operated by centralized actors with their own incentives and outage histories. Chainlink relays add a trust-minimized transport layer but do not fix the source-of-truth question. Multi-source aggregation across exchanges helps, and Boros is among the more conservative implementations here, but the off-chain dependency is structural to the product.

The fourth is basis risk against the user's actual exposure. A trader hedging a Morpho vault position with an IPOR market, or a Boros funding-rate book, is hedging against a generalized oracle of the rate, not against the specific rate they are paying or receiving. Over long tenors and across volatility regimes the basis compounds, leaving the hedge underwater even when the oracle is reporting correctly.

The fifth is leverage amplification. Kairos's roughly-5,000x capital-efficiency design, Voltz's roughly-3,000x legacy vAMM, and Boros's high-leverage funding-rate book all magnify the consequences of any oracle error. A momentary feed glitch becomes a liquidation event, and a liquidation cascade can drain a protocol's insurance fund before circuit breakers engage.

Yield stripping has none of this in the same form. The fixed yield is whatever the underlying actually pays; the oracle question is the same one Aave, Morpho, or Lido already live with; and there is no separate reference rate whose manipulation rewrites the settlement. That is most of the answer to why Pendle's growth has scaled cleanly and most of why synthetic IRS protocols keep running into walls at the volume threshold where their oracle surface starts to matter.

## What Kairos Would Have to Prove

The Kairos pitch is the most credible synthetic IRS attempt in the current cycle. The architecture is permissionless rate-market creation, oracle-agnostic so each market can pick its feed, ERC-721 positions that compose into structured products, and capital efficiency well above prior generations. The seed round and the $300M+ beta notional are real signals that builders and traders are showing up. None of those, on its own, predicts that Kairos will break the pattern Voltz and IPOR settled into.

The questions the protocol would have to answer affirmatively to be the breakout:

Does meaningful flow form on a non-stablecoin-lending reference rate? Voltz at peak was almost entirely a play on stETH and Aave USDC. Sticky rate-trading volume across RWAs, restaking yield, off-chain benchmarks, or funding curves would be a different and more durable demand picture.

Does any tier-one institutional rate desk publicly commit liquidity to a Kairos market? Permissionless market creation is the supply-side innovation; it does not by itself attract the kind of two-way flow that traditional IRS markets have.

Does the oracle-agnostic design produce a manipulation event in its first major drawdown? Every prior synthetic IRS protocol that scaled past a certain threshold encountered an oracle stress test, and the response (or absence of one) shaped its trajectory.

Does Boros, which has the deepest distribution and the cleanest CEX integrations, capture the leveraged-rate-trading audience first? Boros is the obvious incumbent for funding-rate IRS, and Kairos competing on broader rate types is the differentiation, but the funding-rate trade is where the volume currently is.

The protocol may answer all four well. None of them are answered yet.

## The Solana Picture and the Cross-Chain Step

Solana's on-chain rate market is more concentrated than EVM's. Exponent runs essentially the whole of the yield-tokenization category, with integrations across the major Solana DeFi primitives — Jito, Marinade, Kamino, Marginfi — and a v2 that the team has flagged as opening institutional fixed-income use cases at the portfolio-construction layer. The figures the team publicly cites — around $80M TVL, $2B+ in cumulative yield volume, 35,000+ users, no security incidents — put it in the largest-Solana-DeFi-protocols cohort and at the same order of magnitude as the smaller EVM yield-stripping deployments, though still a fraction of Pendle.

Two things are worth watching on the Solana side specifically.

The first is whether Pendle's Solana expansion through Kamino and Chainlink CCIP scales into a meaningful cross-chain PT market. If a Solana-native Kamino position can be wrapped as a PT and that PT trades on Pendle's existing EVM infrastructure with cross-chain settlement, the result is the first liquid bridge between EVM and Solana yield markets. It also creates a direct competitive overlap with Exponent's home-court product, which until now has had Solana to itself.

The second is whether any synthetic IRS protocol launches on Solana in 2026. Port Finance shipped fixed-rate lending and IRS-adjacent features earlier in the cycle; the category has been quiet since. Solana's faster execution and lower fees should be advantageous for high-frequency rate trading, in principle, but the same demand-side gravity that has held synthetic IRS small on EVM applies on Solana too. Pure rate speculation requires an audience with rate views, and that audience is small everywhere.

## Three Signals to Watch Through Q3 2026

The category framing that matters for an active practitioner is narrower than the category framing in research reports. The signals worth checking are demand-side and pair-specific.

The first is whether a Pendle Boros funding-rate pair crosses $1B in cumulative notional on a single underlying. Boros is the cleanest live test of whether on-chain rate trading can scale beyond what Voltz reached, because it sits inside Pendle's existing liquidity and distribution machine and has the deepest CEX integrations. A $1B+ pair would be the first time a synthetic-IRS-style product on a single reference rate has cleared meaningful volume on-chain. It has not happened yet.

The second is whether Kairos closes a Series A, hits $1B+ in cumulative notional, and either (a) ships a public risk dashboard with multi-oracle aggregation per market or (b) experiences and survives an oracle-manipulation event without socializing losses. Either outcome would be a substantive update to the synthetic-IRS-can't-scale prior. Beta notional of $300M is interesting, not yet conclusive.

The third is whether Exponent v2 or Pendle's Solana deployment unlocks fixed-yield supply against tokenized Treasury or RWA positions on Solana with $250M+ in TVL. The cross-chain RWA-as-PT trade is the closest current candidate to a category that brings TradFi-shaped fixed-income flow on-chain in size, and it would be the first time an on-chain rate market is genuinely competing with traditional fixed-income execution rather than serving crypto-native rate speculators.

For DeFi users, the practical takeaway is that the on-chain rate market in 2026 sells yield-locking far better than it sells rate speculation. Pendle and Exponent are doing real work for users who hold yield-bearing positions and want predictable cash flow on them. The synthetic IRS layer can be useful for hedging a specific exposure, but it has been small for three consecutive years now for reasons the architecture alone does not fix. Treat the specific numbers above (TVLs, notional volumes, capital-efficiency claims) as point-in-time snapshots from late April 2026. The structural picture — yield stripping at scale, synthetic IRS at the margin, oracle risk taxing the synthetic side — is the part that has held across multiple cycles.
