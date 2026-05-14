---
git-date:
layout: [blog]
title: "Papertrade Is a Loss-Funded Casino on Hyperliquid. The Mechanism Is What Makes It Work."
permalink: papertrade-hyperliquid-1000x-perps
h1title: "Papertrade: How a 1000x Casino on Hyperliquid Funds Itself From Losses"
pagetitle: "Papertrade Is a Loss-Funded Casino on Hyperliquid. The Mechanism Is What Makes It Work."
metadescription: "Papertrade is a synthetic perpetuals protocol on Hyperliquid where the LP starts at zero, fills only from trader losses, and mints its native token PAPER only to losers. The mechanism design is genuine. So is the extraction."
category: blog
featured-image: /images/blog/papertrade-hyperliquid-1000x-perps-ogp.png
intro: "Papertrade is a synthetic perpetuals protocol on Hyperliquid where the LP starts at zero, fills only from trader losses, and mints its native token PAPER only to losers. The mechanism design is genuine. So is the extraction."
author: sawinyh
tags: ["Analysis"]
---

Papertrade is a synthetic perpetuals protocol on Hyperliquid where the liquidity pool starts at zero, fills only from cumulative user losses, and mints its native token PAPER exclusively to traders who close at a loss or get liquidated. Winners get paid when the LP has the USDC; when it doesn't, the profit portion of their trade goes into a FIFO queue and clears as future losses refill the pool. The mechanism is set out in a [whitepaper](https://docs.papertrade.xyz/martingaler-whitepaper.pdf) called *Martin Galer: A Bootstrapping Mechanism for Sustainable Asynchronous Speculation Games of Chance*, co-authored by Jez (@izebel_eth) and Blurr, the latter known on-chain as "Refund Contract Deployer." Headline markets at launch are BTC and ETH, both with up to 1000x leverage and a $10M per-user position cap.

The mechanism is a genuine onchain contribution. It is also one of the most efficient retail-trader extraction surfaces anyone has shipped to chain, and the cleverness is precisely what makes the extraction work. Both descriptions are accurate at the same time. Walking through how the protocol funds itself is also walking through how it transfers wealth from the people who show up with 1000x leverage to the people who stake the token those people minted by losing.

## How the LP Fills From Losses

Three buckets handle the accounting. A `treasury` holds the LP balance and cannot go negative. A `sideBucket` parks LP gains while the payout queue is non-empty. A FIFO `payout queue` holds unpaid winning closes. A permissionless `harvest()` keeper drains the side bucket into queue payouts as it can.

The flow is straightforward. A user opens a position; the contract reads Hyperliquid's best-bid/offer precompile at `0x000000000000000000000000000000000000080e`, takes the midpoint, and locks it as entry. On close it reads again and settles synthetic PnL against the LP — no perpetual contract actually trades on Hyperliquid through papertrade. If the user wins and the LP can pay, the user gets paid. If the LP can't pay, the profit portion goes to the back of the queue and the user's margin returns immediately. If the user loses, the loss credits the LP (queue empty) or the side bucket (queue non-empty). Net protocol equity is `treasury + sideBucket − queueTotal`, and that figure can go negative; the docs name this "temporary insolvency by design."

What makes this contribution real is that prior onchain casinos all needed bankrolls. SatoshiDice in 2012, Bustabit in 2015, Etheroll in 2017, EtherCrash in 2018 — each required an LP seeded upfront so winners could be paid on demand. That seed had to come from somewhere, which made every prior protocol either custodial in spirit or a token-incentive game; in EtherCrash's case the LP got drained by a bad actor and the protocol died. The Martin Galer payout queue removes the seed entirely. The cost is real but contained: winners can wait on the profit portion of a win during deficit periods, while margin is always returned. The mechanism makes onchain speculation games launchable without raising risk capital, and that is a step forward in the lineage.

Treat the rest of this piece as a working-through of what that step forward enables.

## PAPER's Mint Curve Is a Wealth Transfer

PAPER is described in the docs as a "fair launch." On supply, the claim is accurate: zero pre-mint, no team allocation, no VC allocation, no airdrop, no vesting. Every token has to be minted through one path — a trader closing at a loss or being liquidated. The mint rate is 100 PAPER per $1 of LP gain while the LP balance is below $2M, including any period the LP is underwater. Above $2M the rate decays as `100 × (S / (S + H))²` with `S = $120M` and `H` the cumulative LP gain past the threshold. The decay is a strict high-water-mark ratchet: once the cumulative tail-region gain has advanced, the rate stays decayed even if stakers drain the LP back down.

What stakers receive in return is a continuous USDC dividend out of LP revenue, plus a sweep of any LP balance above $5M. Stake and unstake are instant.

The fairness framing is doing more work than it admits. The first $2M of LP gain mints at the flat 100 PAPER/$1 rate. After that, the rate decays. A trader showing up after the protocol crosses $50M of cumulative LP gain mints PAPER at roughly 51 per $1 of loss. A trader showing up at $100M mints at ~30 per $1. The implication is that the supply distribution structurally favors traders who lose money early, who then stake their PAPER and start collecting USDC dividends from the losses of every trader who shows up later. That is not fundamentally different from a pre-allocated insider tranche with a cliff vest. The asymmetry is timing-based rather than identity-based, but the wealth transfer from late losers to early stakers is the same shape.

The team that builds this can also trade on it. Their PAPER mints come from documented on-chain losses, which technically satisfies "no team allocation," but anyone with insider knowledge of the parameter set the timelock owner controls — when impact-curve constants will change, when new markets will be listed, when OI caps will shift — has an information advantage over later traders. The fair-launch label is supply-fair. It is not opportunity-fair.

## "No Trading Fees" Means a Hidden Fee

The marketing says no trading fees, no spread, no funding cost, no gas charged to the user. All of that is mechanically true. What papertrade charges instead is an asymmetric impact curve on winning closes only:

```
adjustedPnl = rawPnl × scale
scale       = (1 − baseRate) / (1 + term1 + term2)
term1       = 1 / (move × rateMultiplier)
term2       = referenceNotional / (move × positionMultiplier)
```

The curve is steepest on the smallest moves and softens as the price move grows. Losses pay nothing extra. A 0.2 basis-point jitter-protection deadband zeros sub-spread wins entirely before the curve runs. Trailing per-asset open-interest caps prevent an attacker who briefly distorts Hyperliquid's BBO from sizing into the distortion.

The structural property worth being clear about is that this is a fee. It is invisible at entry, applied only to winning closes, and shaped so that a trader catching a tiny scalp wins less than the curve's haircut, while a trader catching a large directional move keeps most of the gain. Compared to a published spread or a fixed taker fee, the impact curve is less transparent — a retail user cannot price the haircut without modeling the curve — and structurally more extractive on the kind of small-move trades a 1000x leverage product naturally generates. The Rollbit lineage the design borrows from is precisely the lineage of casino economics where the house edge is mathematical rather than disclosed.

The curve also funds the LP. That is the design's coherent piece: an oracle-manipulation defense and the protocol's revenue stream are the same mechanism. Sub-spread BBO distortions can't generate profitable closes because the curve eats sub-move-size gains. That is genuinely clever. It is also what guarantees that retail traders catching small wins are subsidizing both the LP and the protocol's oracle integrity.

## 1000x Selects the User Base the Design Needs

At 1000x leverage on BTC or ETH with a 5-basis-point bust-price buffer, the per-trade dynamics are punishing. Extending Hyperliquid's documented maintenance-margin formula to 1000x puts the liquidation threshold around a five-basis-point adverse move. The 0.2-basis-point jitter deadband zeros the smallest possible wins. The asymmetric impact curve haircuts the next tier of wins most aggressively. A trader needs a directional move large enough to clear the steep part of the curve, fast enough to avoid the bust buffer biting, with timing precise enough that the position doesn't sit through funding-like decay. None of those constraints reward skill in a directional-trading sense. They reward correctly-timed leverage on volatile moments and punish everything else.

The user base this attracts is the user base the LP depends on losing. Traders showing up for 1000x leverage on BTC are gambling, are exploiting BBO jitter inside the curve's tolerance band, or are unfamiliar with the mathematics of leveraged speculation. The first group loses by definition. The second group is precisely what the impact curve plus the OI cap plus the deadband are designed to neutralize. The third group loses through ignorance. The marketing copy on the front page — "1000x leverage, 0 slippage, 0 market impact, fully onchain perpetual exchange" — selects for exactly the audience the design needs.

This is the structurally important point about the marketing-vs-docs gap that's worth naming directly. The front page is not lying. There is no slippage in the sense Hyperliquid traders use the word; there is no orderbook to walk; the leverage cap is real. What the front page omits is that the design's economic engine requires the user base to lose on aggregate, and the term "casino" — which the whitepaper applies to the protocol freely — is absent from anything a prospective trader sees before depositing.

## The Oracle Belongs to Hyperliquid

Papertrade's execution price is Hyperliquid's BBO mid, read through a precompile from HyperEVM. There is no separate price feed, no oracle committee, no admin signer who can rewrite the mark. That is good for trust-minimization in the normal case. It is also a hard dependency on Hyperliquid's order-book integrity for BTC and ETH.

The JELLYJELLY incident in March 2025 established that Hyperliquid's validators are willing to intervene when book-level manipulation distorts a thin perp market. BTC and ETH spot are not thin — a JELLY-style attack on them is structurally harder and economically larger. But a coordinated attempt to drive a meaningful BBO distortion on BTC or ETH for one or two blocks would be readable by papertrade's contracts as a real price and settled against them. The impact curve and OI caps defend against sub-spread distortions of a few basis points. They do not defend against a real fifty-basis-point book-thinning attack. The protocol has no fallback feed and no circuit breaker.

Whether that risk is material depends on how deep BTC and ETH books stay on Hyperliquid as papertrade's OI grows. The dependency is structural, the protection is partial, and the docs do not name the failure mode.

## The "Fair Launch" Doesn't Reach the Parameters

The contract owner sits behind a 7-day timelock and can change every numeric knob in the system: the flat-region mint rate, the $2M threshold, the $120M decay scale, the impact-curve constants per market, the OI caps, the bust-price buffer, the fee rates routed to stakers, and ultimately the contract implementation itself. Every action queues publicly for 7 days before it can execute. Users have a week to withdraw before any change lands.

That is the right mitigation. It is not the same as no mitigation. The fair-launch claim describes the supply genesis. It does not describe the ongoing economic surface, every constant of which is owner-controlled. A future owner action could materially change which traders mint how much PAPER, what the LP captures from each losing trade, and what stakers earn — and existing PAPER holders' dividend stream is a function of those constants. "Trust the team to keep parameters where they are, or exit within 7 days of a proposal" is a meaningful trust commitment.

Compare this to most DeFi protocols and it is in line with industry practice. Compare it to the "fair launch, no team control" framing the marketing implies and the gap is real.

## Regulation Is the Largest Unaddressed Surface

A leveraged speculation product distributing USDC dividends to token holders, operated by anonymous authors, with 1000x leverage on synthetic price exposure and a documented house edge — that is a product profile every relevant regulator has shown interest in. The CFTC, the SEC, and the FCA have all moved against substantially similar products in 2024-2025. The Rollbit framing the docs invoke is precisely the framing that has drawn enforcement attention.

The design choices the team has made all read as responses to a regulatory environment the docs do not name. The team is anonymous. The contract owner sits behind a timelock rather than a named legal entity. The frontend is one of many possible permissionless frontends. The word "casino" does not appear on the marketing site, only in the whitepaper. None of this is illegal. All of it is consistent with a product that expects regulatory attention and has designed around being structurally hard to enforce against.

This is the part of the analysis that becomes determinative the moment a regulator looks. Until then, the protocol's structural risk profile reads cleanly. After that, every design choice in the previous sections is recontextualized as a defense against an attack that wasn't named in the docs.

## What to Watch When Trading Goes Live

Four metrics will tell you whether the design works as described and which users it works on.

The flat-rate window fill time. The first $2M of LP growth mints PAPER at 100/$1. The speed at which the LP fills through this window is the realised house edge expressed in calendar time. A slow fill means the trader population is closer to break-even than the design implies. A fast fill confirms the design is doing what the math says it does.

The queue overhang ratio. The closer queue total runs to LP balance, the more often winning closes wait. Early protocol life is queue-heavy by definition. Whether the queue clears reasonably as flow accumulates is the user-experience proxy and a leading indicator of whether the bootstrap converges.

The first owner action through the timelock. A trivial parameter tweak is the boring outcome. An impact-curve recalibration is informative. A mint-curve constant change is a serious signal about how the team treats the existing PAPER holder base — and the test of how much the "fair launch" claim survives contact with live economics.

The regulatory clock. De-anonymization tied to an institutional relationship, a named regulator action, or a long enough silence to make the omission its own answer. Whichever comes first changes the analysis.

Papertrade is a piece of serious mechanism design that ships an efficient retail-trader extraction surface as its product. The two are not in tension; the first is what makes the second efficient. The LP curve and the queue dynamics, once trading is live, will say how efficient.

For related defiprime coverage on Hyperliquid: [Hyperliquid vs. Aster](/hyperliquid-vs-aster) and the [Hyperliquid Chain ecosystem deep dive](/hyperliquid-chain-deep-dive). The product page for [Hyperliquid](/product/hyperliquid) sits in the [perps](/perps) collection.
