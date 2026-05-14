---
git-date:
layout: [blog]
title: "Inside Papertrade: 1000x Synthetic Perps Built on a Zero-LP Bootstrap"
permalink: papertrade-hyperliquid-1000x-perps
h1title: "Inside Papertrade: 1000x Synthetic Perps and the Martin Galer Bootstrap"
pagetitle: "Inside Papertrade: 1000x Synthetic Perps Built on a Zero-LP Bootstrap"
metadescription: "Papertrade isn't a HIP-3 perp DEX. It's a peer-vs-pool synthetic casino on HyperEVM that uses Hyperliquid's BBO as an oracle, bootstraps its LP from zero through a payout queue, and mints its token only to traders who lose."
category: blog
featured-image: /images/blog/papertrade-hyperliquid-1000x-perps-ogp.png
intro: "Papertrade isn't a HIP-3 perp DEX. It's a peer-vs-pool synthetic casino on HyperEVM that uses Hyperliquid's BBO as an oracle, bootstraps its LP from zero through a payout queue, and mints its token only to traders who lose."
author: sawinyh
tags: ["Analysis"]
---

A quick first read of papertrade.xyz suggests yet another HIP-3 deployer chasing extreme leverage on Hyperliquid: 1000x, "fair launch," "synthetic perpetuals." Read the actual documentation and the picture flips. Papertrade isn't a HIP-3 deployer at all. It doesn't trade perp contracts on Hyperliquid. It runs its own smart contracts on HyperEVM that read Hyperliquid's best-bid/offer price through a precompile and use that price to settle synthetic swaps between users and a self-bootstrapping LP. The product surface looks like a perp DEX. The mechanism underneath is something much closer to an academically-grounded on-chain casino.

This is genuinely interesting. The whitepaper, [*Martin Galer: A Bootstrapping Mechanism for Sustainable Asynchronous Speculation Games of Chance*](https://docs.papertrade.xyz/martingaler-whitepaper.pdf) by Jez (@izebel_eth) and Blurr (Refund Contract Deployer), cites Tarun Chitra and Guillermo Angeris' CFMM-theory papers and explicitly positions itself in the SatoshiDice → Bustabit → Etheroll → EtherCrash → Rollbit lineage. The result is a leveraged-perp surface that mechanically resembles a CFD broker more than a Hyperliquid market, with a token economy designed so the supply can only be created by losing money. That last property is rarer than it sounds.

## What's Actually On Chain

Papertrade's contracts live on HyperEVM, Hyperliquid's L1 EVM layer. There is no order book on papertrade, no matching engine, no other trader on the other side of your trade. The counterparty on every trade is "the LP," a single USDC pool inside the protocol's Exchange contract.

When you open a position, the Exchange contract reads Hyperliquid's BBO precompile at `0x000000000000000000000000000000000000080e`, takes the midpoint of the best bid and best ask on Hyperliquid's native book, and locks that price as your entry. When you close, it reads the precompile again and settles your PnL against the LP. No actual perpetual contract is opened on Hyperliquid through papertrade. Hyperliquid is purely the price source.

That single architectural choice unlocks most of papertrade's marketing claims. There are no funding costs because no real perp position is being held. There is no slippage at execution because every trade clears at the precompile-read BBO mid regardless of size, subject only to per-instrument open-interest caps the protocol enforces internally. There are no trading fees on notional, because the protocol's revenue model is built around a different mechanism (the asymmetric impact curve, below). USDC balances live on HyperCore (Hyperliquid's native spot ledger); the bridge between HyperEVM contract state and HyperCore balances runs through the `CoreWriter` precompile and per-user CREATE2 deposit proxies.

Live markets at launch are BTC and ETH, both with up to 1000x leverage and a per-user position cap of $10M. The protocol can list any Hyperliquid perp, including HIP-3 ones; new markets are added by the contract owner through a 7-day timelock.

## The Martin Galer Mechanism: Zero-LP Bootstrap

The reason the docs and the whitepaper matter together is that papertrade's LP starts at zero. No seed capital, no founders' deposit, no upfront fundraise. There is no way for anyone to deposit *into* the LP directly. The LP grows entirely from cumulative user losses. That is not a marketing line; it is the structural property the protocol was designed around.

The mechanism that makes this work is the Martin Galer payout queue. Traditional onchain casinos (SatoshiDice, Bustabit, EtherCrash) all needed an LP pool seeded upfront so winners could be paid on demand. That seed had to come from somewhere, usually centralised capital or token-funded liquidity mining. Martin Galer replaces instant payout with a FIFO queue:

- A user wins. If the LP has enough USDC, pay the user immediately. If not, the unpaid portion of the win goes to the back of the queue. The user's *margin* is always returned immediately; only the profit portion can land in the queue.
- A user loses. If the queue is empty, the loss credits the LP directly. If the queue is non-empty, the loss is parked in a `sideBucket` instead of the LP.
- A keeper periodically calls `harvest()`, which drains the `sideBucket` into queue payouts in order. Anyone can run the keeper. When the queue empties, residual `sideBucket` funds flow into the LP as a normal gain.

The accounting is three buckets: `treasury` (LP balance, never negative), `sideBucket` (parked LP gains during a queue), and the payout queue. Net protocol equity is `treasury + sideBucket − queueTotal`, and that figure **can go negative**. The docs are explicit about this — "temporary insolvency by design." What guarantees winners eventually get paid is the assumption that the user base is positive-EV for the protocol on aggregate (the house edge), so future losses will refill the LP faster than queued wins drain it.

Crucially, the queue overhang doesn't block anything else. New positions open whether the queue is empty or not. Margin is always under the user's control. The only thing that's delayed when the LP can't pay is the profit portion of a particular winning close. The UI is designed to show this explicitly: an "available" balance and a "queued" balance, where queued balance still counts as collateral for new opens.

The whitepaper also discusses a stuck-participant escape valve (queued winners can forfeit their winnings to reclaim original wager input) but the live protocol doesn't expose that escape, on the bet that the LP rarely sits in deep deficit.

## PAPER: A Token Minted Only By Losers

Papertrade's native token, $PAPER, is the protocol's mechanism for paying anyone to put money into the LP — because there's no other way to put money in. The design is unusual enough to spell out precisely:

- Total supply at genesis: zero.
- No pre-mint. No team allocation. No VC allocation. No airdrop. No vesting schedule.
- Every PAPER token that will ever exist must be minted through one specific path: a trader closing at a loss or being liquidated.
- The mint rate is governed by a flat-then-decay curve. While the LP balance is below $2 million (including any time it's underwater), the rate is a flat **100 PAPER per $1 of LP gain**. Past $2M, the rate decays as `100 × (S / (S + H))²` where `S = $120M` and `H` is the cumulative LP gain past the threshold.
- The decay is a strict high-water-mark ratchet. If stakers drain LP back below the threshold, the rate stays decayed; subsequent gain past the prior HWM picks up where it left off. Early traders mint at materially higher rates than late traders, by design.

What stakers earn in return is a continuous USDC dividend from the LP, in two streams. First, every settlement that credits the LP (the asymmetric impact on a winning close, or an outright loss) carves a small slice for stakers. Second, once the LP grows past a $5M cap, every dollar of LP gain past that point sweeps fully to stakers via a public `pushStakerFees()` call. Stake and unstake are both instant: no cooldown, no lockup, no minimum.

This is a clean reinterpretation of the "loyalty token" pattern. Every PAPER holder is, by definition, someone who put real USDC into the LP through a losing trade. They are buying back a claim on future LP revenue by absorbing the early variance. The flat-region mint rate is what makes that trade attractive even when the LP is underwater: a loser early in the protocol's life walks away with a much bigger fraction of the eventual revenue pool than a loser later on.

## Asymmetric Impact: The LP's Real Income

If there are no trading fees and no spread, the natural question is what funds the LP at all. The answer is the asymmetric impact curve, a Rollbit-inspired mechanism papertrade has adapted for its own constraints.

On a winning close, the protocol applies a smooth scale factor to the raw PnL:

```
adjustedPnl   = rawPnl × scale
scale         = (1 − baseRate) / (1 + term1 + term2)
term1         = 1 / (move × rateMultiplier)
term2         = referenceNotional / (move × positionMultiplier)
move          = |exitPrice − entryPrice| / entryPrice
```

As `move` grows, both terms in the denominator shrink, the scale factor approaches `(1 − baseRate)`, and the trader keeps most of the raw gain. As `move` approaches zero, the terms blow up and the gain collapses toward zero. Losing closes pay nothing extra — the loss is the loss, and that's the end of it.

The key word is *asymmetric*. The cost of trading on papertrade lives entirely on the win side, scaled by how far price moved. Bigger moves keep more; tiny moves are scaled most aggressively. Papertrade's twist on the Rollbit formula is that the position-size factor (`term2`) is replaced with a per-instrument constant. At 1000x leverage the original formulation would have penalised larger trades and pushed users into many small positions, which is bad on gas, state, and UX. Papertrade fixes the haircut percentage to depend on the move, not on the trade size.

This curve does more than fund the LP. It is also the protocol's main defence against oracle manipulation. The BBO precompile is consensus-verified and cannot be lied to, but a sub-spread distortion is cheap: a single small limit order on Hyperliquid's book can shift the BBO mid by a tick. An attacker who used that distortion to engineer a small profitable close on papertrade would find the gain almost entirely consumed by the impact curve, because the curve is steepest on the smallest moves. Stack a 0.2 basis-point jitter-protection deadband (small wins below `entryPrice / 50000` are zeroed) and trailing per-asset open-interest caps on top, and the attack stops being economically viable. The docs are explicit that this is why papertrade can read BBO directly with no circuit breaker and no off-chain oracle.

## What Liquidation Means When There's No Order Book

Liquidations on papertrade do not run through Hyperliquid's order book, and there's no HLP backstop relationship. Each position has a "bust price": the BBO at which the position's equity would hit zero, less a fixed buffer of approximately 5 basis points. When BBO crosses bust, any keeper can call `liquidate(positionId)`. The contract closes the position at the bust price and credits the margin to the LP. The trader loses their margin and receives PAPER for the loss, the same way they would on a regular losing close.

The buffer exists so the LP captures the full position before the close even if price drifts during keeper round-trip. Liquidation is permissionless, run by whoever shows up first; the protocol team runs a keeper but doesn't have exclusive access.

The structural point worth flagging: papertrade's solvency stack stops at its own contracts. There is no HLP exposure, no validator-set intervention vector, no JELLY-style precedent that applies. If the protocol's three-bucket accounting goes deep into deficit because users keep winning faster than the queue can clear, the consequence lands on PAPER holders (their dividends slow) and on queued winners (their payouts wait), not on Hyperliquid's solvency layer.

## Admin Surface and Real Risks

Three admin roles are documented, each scoped:

- A **pause guardian** can halt new opens on any market or globally, and doing so freezes the BBO at the moment of pause for any subsequent close on that market.
- An **owner** sits behind a 7-day timelock and can tune impact curve and fee parameters, swap signers and keepers, list new markets, and ultimately upgrade the proxied contracts. Every owner action queues publicly for 7 days before execution.
- A **market keeper** moves the trailing per-asset directional OI caps as organic OI moves.

Pause-opens and the owner upgrade path are the centralised levers that exist; the 7-day timelock on owner actions is what the team points to as the trust-minimisation knob. Existing positions can always be closed at the BBO frozen at pause time, so a freeze doesn't strand collateral.

The documented risks worth flagging on the user side: queue overhang means a winning close can take time to actually arrive, especially in the early life of the protocol when the LP is still bootstrapping. The 7-day timelock is meaningful but not eliminative — the team can upgrade the contracts, and a sufficiently motivated proposal could materially change protocol behaviour after the timelock window. The bridging UX has a known race-condition deposit bug, mitigated by a separate 7-day-timelock admin key whose only purpose is to credit orphaned deposits.

None of those are unusual for a contract proxied behind a timelock. They are worth knowing.

## Where This Sits in the Landscape

Papertrade is structurally different from the things it gets compared to.

It is not a HIP-3 deployer. The HIP-3 surface — 500,000 HYPE staked, validator slashing, deployer-side oracle and leverage configs, HLP backstop exposure — does not apply. trade.xyz's tokenized stocks and opt.fun's options are different products built on different relationships with Hyperliquid; papertrade uses Hyperliquid the same way an HyperEVM DeFi app uses any precompile.

It is not the typical perp DEX. There is no order book. There is no margin engine in the GMX or dYdX sense. The closest structural cousin in DeFi is the GMX peer-to-pool perp design, but GMX uses a multi-asset GLP pool seeded with real liquidity and quotes against Chainlink oracles; papertrade uses a single-USDC LP that starts at zero and reads HL's BBO directly through a precompile. The queue mechanism and the loss-mint token are not present in GMX.

It is not a generic crypto casino. The Martin Galer mechanism design is academically grounded, the whitepaper cites Chitra-Angeris CFMM literature, and the on-chain architecture (precompile reads, CoreWriter bridges, CREATE2 proxies, 7-day-timelock proxy upgrades) is serious systems work. The product surface is a leveraged perp; the framing as a "speculation game" in the whitepaper is honest about what it is, but the implementation is closer to a CFD broker built on Hyperliquid's pricing infrastructure than to a Rollbit-style centralized casino.

The interesting thing is the combination. A peer-vs-pool perp surface with no orderbook, bootstrapped from zero capital, with a token minted only to losers, with an asymmetric impact curve that doubles as oracle-manipulation defence, all running on Hyperliquid's price feed without depending on Hyperliquid's solvency or governance — that is a different shape than the rest of the HyperEVM ecosystem. Whether it scales to meaningful volume depends on whether the user base ends up positive-EV for the LP (it has to, for the queue to ever clear), and on whether PAPER holders find the dividend stream attractive enough to keep absorbing variance.

There is a real product question worth thinking about. At 1000x leverage with a bust-price buffer of about 5 bps and an asymmetric impact curve that haircuts wins, the per-trade economics are unfriendly to the trader and friendly to the LP. The protocol bets that traders will show up anyway, because at 1000x the variance is the point. The PAPER emissions curve front-loads the reward for early traders, who carry the most variance risk. That is the only thing turning a structurally trader-unfriendly product into something a participant might rationally show up for.

It is a coherent design. Whether it works is an empirical question about traffic, queue dynamics, and how long the flat-region of the mint curve lasts. The next interesting data point will be the live LP trajectory once trading is open and the first wave of losses starts feeding the bootstrap.

For related defiprime coverage on Hyperliquid: [Hyperliquid vs. Aster](/hyperliquid-vs-aster) and the [Hyperliquid Chain ecosystem deep dive](/hyperliquid-chain-deep-dive). The product page for [Hyperliquid](/product/hyperliquid) sits in the [perps](/perps) collection.
