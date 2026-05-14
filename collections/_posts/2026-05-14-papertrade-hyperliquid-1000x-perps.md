---
git-date:
layout: [blog]
title: "Papertrade Is the Cleanest Onchain Casino Anyone's Shipped, Dressed as a Perp DEX"
permalink: papertrade-hyperliquid-1000x-perps
h1title: "Papertrade: The Cleanest Onchain Casino, Dressed as a Perp DEX"
pagetitle: "Papertrade Is the Cleanest Onchain Casino Anyone's Shipped, Dressed as a Perp DEX"
metadescription: "Papertrade's 1000x leverage and 'fair-launched fully onchain perpetual exchange' framing buries the real story: an academically-grounded onchain casino with a zero-LP bootstrap and a token minted only by losers, sitting on top of Hyperliquid's price feed."
category: blog
featured-image: /images/blog/papertrade-hyperliquid-1000x-perps-ogp.png
intro: "Papertrade's 1000x leverage and 'fair-launched fully onchain perpetual exchange' framing buries the real story: an academically-grounded onchain casino with a zero-LP bootstrap and a token minted only by losers, sitting on top of Hyperliquid's price feed."
author: sawinyh
tags: ["Analysis"]
---

The pitch on papertrade.xyz reads like every other extreme-leverage perp protocol: 1000x leverage, 0 slippage, 100% user owned, fully onchain. Read the docs and the whitepaper and that framing falls apart. Papertrade is not a perp DEX. It is the most carefully-engineered onchain casino anyone has shipped to date, with a token-economics design that's the rarest thing in DeFi — actually fair — and it runs on top of Hyperliquid without taking any of Hyperliquid's solvency risk. The "1000x perp" packaging is what gets it past the DeFi/gambling line in people's heads. The mechanism underneath is straight out of [Tarun Chitra and Guillermo Angeris' CFMM literature](https://docs.papertrade.xyz/martingaler-whitepaper.pdf).

Three things make this protocol worth paying attention to, none of them is the leverage number.

## It Doesn't Touch Hyperliquid's Risk Stack At All

The first surprise from the docs is that papertrade is not a [HIP-3](/hyperliquid-vs-aster) deployer. No 500,000 HYPE staked, no validator slashing exposure, no relationship with HLP. Papertrade runs its own contracts on HyperEVM — Hyperliquid's L1 EVM layer — and uses Hyperliquid's best-bid/offer precompile at `0x000000000000000000000000000000000000080e` purely as a price feed. No perp contract trades on Hyperliquid through papertrade. When you open a position, the Exchange contract reads the BBO mid, locks it as your entry, and creates a synthetic swap between you and the protocol's internal LP. When you close, it reads the BBO mid again and settles your PnL against that same LP.

That single architectural choice changes the risk picture entirely. The recent conversation about builder-deployed perps has centered on whether deployer stakes are calibrated to the bad-debt envelope deployers can route into HLP. Papertrade is outside that conversation. The protocol's three-bucket accounting (treasury, side bucket, payout queue) cannot route losses to HLP, because there's no relationship to HLP. If papertrade's LP blows up, the consequence lands on PAPER holders' dividends and on queued winners waiting longer — not on Hyperliquid validators, not on HLP depositors, not on anyone outside papertrade's own contracts.

Papertrade is doing to Hyperliquid what Polymarket did to UMA: consuming the upstream's price infrastructure as a free public good, building a self-contained product on top, taking exactly zero exposure to the upstream's governance or solvency layer. The 7-day timelock on the contract owner is the only centralized lever, and it's exactly the same trust assumption you make using any proxied DeFi protocol.

## The LP Starts at Zero. That's the Whole Point.

Most onchain casinos die for the same reason: they need a bankroll. SatoshiDice, Bustabit, Etheroll, EtherCrash all needed an LP seeded upfront before they could pay winners on demand. The seed had to come from somewhere — centralized capital, token-funded liquidity mining, or in EtherCrash's case, the LP getting drained by a bad actor — and that requirement made every onchain casino either custodial in spirit or a token-incentive game.

Papertrade's LP starts at $0. There is no seed, no founders' deposit, no upfront raise, and crucially, **no way for anyone to deposit directly into the LP**. The pool grows entirely from cumulative user losses. The mechanism that lets that work is the Martin Galer payout queue, written up in [a whitepaper](https://docs.papertrade.xyz/martingaler-whitepaper.pdf) co-authored by Jez (@izebel_eth) and Blurr that cites a wall of Chitra-Angeris papers on CFMM theory.

The mechanics are clean enough to spell out. Three buckets: `treasury` (the LP, never negative), `sideBucket` (parked LP gains during a queue), and a FIFO `payout queue` of unpaid winning closes. When a user wins and the LP can pay, the user gets paid. When the LP can't pay, the profit portion of the win goes to the back of the queue and the user's margin returns immediately. When a user loses and the queue is empty, the loss credits the LP directly. When a user loses and the queue is non-empty, the loss is parked in the side bucket. A permissionless `harvest()` keeper periodically drains the side bucket into queue payouts in order.

Net protocol equity is `treasury + sideBucket − queueTotal`, and the docs spell out the consequence: **that figure can go negative.** "Temporary insolvency by design." What guarantees winners eventually get paid is the assumption that aggregate user flow is positive-EV to the LP, which at 1000x leverage with the impact curve described below is almost certainly true.

The thing that makes this a different category of design is that nobody is asked to put up risk capital. Traders show up to bet. Losses fund the LP. Winners may have to wait, but only on the profit portion, and only when the LP is in temporary deficit. Margin is always returned immediately. Nothing about this requires trust in a centralized treasury and nothing about it requires a token incentive that lies about what's actually happening.

## Every PAPER Token Is Minted By a Loser

The PAPER tokenomics are the most honest design I've seen in DeFi this cycle. Total supply at genesis: zero. No pre-mint. No team allocation. No VC allocation. No airdrop. No vesting. The only way a PAPER token comes into existence is for a trader to close a position at a loss or get liquidated, at which point the protocol mints PAPER to that trader's wallet against the loss.

The rate is mathematical. While the LP balance is below $2M (including any time it's underwater), the rate is a flat 100 PAPER per $1 of LP gain. Above $2M, the rate decays as `100 × (S / (S + H))²` where `S = $120M` and `H` is the cumulative LP gain past the threshold. The decay is a strict high-water-mark ratchet — if stakers drain LP back below the threshold, the rate stays decayed forever. The cumulative tail HWM only ever ratchets up.

What stakers get in return: a continuous USDC dividend out of LP revenue, paid in two streams. Every settlement that credits the LP carves a slice for stakers. Once the LP balance grows past $5M, every dollar of LP gain past that point sweeps fully to stakers. Stake and unstake are both instant — no cooldown, no lockup, no minimum.

This works as an economic loop in a way most "fair launch" tokens don't. A PAPER holder is, by definition, someone who paid real USDC into the LP through a losing trade. They are buying back a fractional claim on future LP revenue by absorbing the early variance. The flat-region mint rate is what makes that trade attractive when the LP is small or underwater — exactly the period where most protocols would either need a token-incentive program or a seed deposit. Here the participation incentive is mechanically tied to the protocol's bootstrapping need. A loser at LP = -$50K mints flat at the full 100/$ rate. A loser at LP = $50M mints far less. By design.

Compare this to any recent "fair launch" you can name. PAPER has no premise of equality, no insider allocation hidden in a vesting cliff, no liquidity bootstrap built on top of pre-allocated tokens. The supply curve is the protocol's economic engine and the protocol's economic engine is the supply curve. There is one mechanism, and it is legible from the source code.

## The Asymmetric Impact Curve Tells You Who the Product Is For

If trades have no fees, no spread, no funding cost, and no gas — and they don't — the natural question is what feeds the LP at all. The answer is an asymmetric impact curve, adapted from Rollbit. On a winning close the protocol applies a scale factor that depends on how far price moved between entry and exit:

```
adjustedPnl = rawPnl × scale
scale       = (1 − baseRate) / (1 + term1 + term2)
term1       = 1 / (move × rateMultiplier)
term2       = referenceNotional / (move × positionMultiplier)
```

Losing closes pay the full loss with no haircut. Winning closes are scaled. Bigger price moves keep more of the gain; tiny moves are scaled most aggressively. Papertrade's twist on the Rollbit formulation is that the position-size factor (`term2`) uses a fixed per-instrument reference notional rather than the trader's actual size, so the haircut percentage is the same on a $100 close and a $100K close.

This curve does two jobs. It funds the LP, which is the visible job. The less visible job is that it makes BBO oracle manipulation unprofitable. The natural attack on a perp that reads BBO directly is to place a small limit order on Hyperliquid's book to shift the mid by a tick, then open and close a position against the distorted price. The impact curve is steepest on the smallest moves, so a sub-spread manipulation produces a gain that gets eaten almost entirely by the haircut. Stack a 0.2 basis-point jitter-protection deadband on top (small wins below `entryPrice / 50000` are zeroed) and trailing per-asset open-interest caps, and the attack stops being economically viable. That is why papertrade can read BBO directly with no circuit breaker and no off-chain oracle.

What the curve tells you about the target user is more interesting. At 1000x leverage with a haircut that's harshest on the smallest moves and a bust-price buffer of 5 basis points, the per-trade economics are aggressive on the LP's side. To actually make money, a trader needs to catch directional moves big enough to escape the steep part of the curve, fast enough to avoid bust, without trying to scalp small ticks (which get haircut to zero) and without sitting in positions long enough for the bust buffer to bite. This isn't a serious trader's product. It's a high-variance product for users who understand they are betting, designed to be honest about that. The PAPER emissions curve front-loads the consolation prize for the early variance-takers. The asymmetric impact funds the LP. Both mechanisms align around a specific user: someone showing up for the lottery, not for the directional edge.

## What Can Actually Go Wrong

Three real risks, in order of likelihood.

**Queue overhang.** In the early life of the protocol, the LP is small or negative, and a string of winning closes can queue up profit payouts that wait until losses refill the side bucket. Margin is always returned immediately, but the profit portion can sit. This is the visible cost of the zero-LP bootstrap. The protocol is honest about it. Whether users tolerate it is the empirical question of the first six months.

**The 7-day timelock owner.** The contracts are proxied. The contract owner can tune the impact-curve parameters, the mint-rate constants, the OI caps, the fee rates, and ultimately upgrade the implementation. Every owner action queues publicly for 7 days before it can execute, so users have a week to withdraw and exit if they disagree. This is a real trust assumption. It's the same one you make with most DeFi protocols, but it's worth naming because the mint curve and the impact curve are both parametric.

**Aggregate trader EV.** The Martin Galer mechanism mathematically only works if cumulative user flow is positive-EV for the LP over time. If, hypothetically, papertrade attracted a population of users who were systematically winning against the BBO oracle through some pattern the impact curve didn't price in, the queue would grow without bound and the protocol would never settle. This is structurally unlikely at 1000x leverage on BTC and ETH — the impact curve and the bust buffer are designed to make sub-move-size profit extraction uneconomic. But it is the load-bearing assumption of the whole design, and the data to confirm it will only exist after users actually trade.

The two risks that aren't there are worth naming too. There's no HLP exposure, so a bad day on papertrade doesn't drain anyone else's vault. There's no validator-intervention vector, because there's no HIP-3 market to delist. The protocol's bad outcomes are contained inside its own three-bucket accounting and its own token holders.

## What This Actually Is

The honest framing for papertrade is that it's an onchain casino, designed with the seriousness of a DeFi protocol, that has chosen to present itself as a perp DEX because that framing gets through filters that "onchain casino" doesn't. The whitepaper is explicit about the lineage — SatoshiDice through EtherCrash through Rollbit — and the mechanism design is the next step in that lineage rather than a divergence from it.

That's not a criticism. It is a more interesting product than most of the actual perp DEXs in the ecosystem right now, because it is solving a real mechanism-design problem that perp DEXs don't have. Onchain casinos need bankrolls and onchain casinos need fair token distribution and onchain casinos need oracle integrity. Papertrade has a paper, a code base, and a deployment that addresses all three at once.

What it asks of the user is something most DeFi protocols don't ask: be honest about why you're here. If you are here because you want directional exposure to BTC at moderate leverage with predictable funding, this is not your product — go use Hyperliquid's native perps. If you are here because you want a lottery ticket with a token-rebate built in, the design is coherent and the math is documented and the LP can't run with your money because there is no LP custodian to run anywhere. That is rare. It is worth recognizing on its own terms.

For related defiprime coverage on Hyperliquid: [Hyperliquid vs. Aster](/hyperliquid-vs-aster) and the [Hyperliquid Chain ecosystem deep dive](/hyperliquid-chain-deep-dive). The product page for [Hyperliquid](/product/hyperliquid) sits in the [perps](/perps) collection.
