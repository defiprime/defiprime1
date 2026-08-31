---
git-date:
layout: [blog]
title: "The Weekend Float Squeeze: How a Memecoin Cornered a Tokenized Stock"
permalink: tokenized-stock-float-squeeze
h1title: "A Memecoin Cornered a Tokenized Stock"
pagetitle: "The Weekend Float Squeeze: How a Memecoin Cornered a Tokenized Stock"
metadescription: "A memecoin paired against tokenized HIMS pushed the stock token 112% above its NYSE close over a weekend. The mints that crushed it arrived Sunday night."
category: blog
featured-image: /images/blog/tokenized-stock-float-squeeze-ogp.png
intro: "A memecoin paired against tokenized Hims & Hers equity absorbed most of the token's onchain float over a weekend and pushed it as much as 112% above its NYSE close. The issuer's mints crushed the premium within two hours, and the whole cycle ran before Monday's opening bell."
author: sawinyh
tags: ["Analysis", "RWAs"]
---

At 23:36:14 UTC on Sunday, August 30, 2026, tokenized Hims & Hers stock printed $61.15 in its main dollar pool on Robinhood Chain. The real share had closed Friday on the NYSE at $28.84. Nothing had happened to the company. The wrapper was trading at more than double its net asset value because a memecoin called BONER had spent the evening pulling most of the token's onchain float into its own liquidity pool, and the only entity able to mint more was not minting on a Sunday.

At 00:43:30 UTC on Monday, in block 50,444,949, the first new supply arrived: a round 1,000-token mint, five seconds after the pool printed $54.50. Within 12 minutes the premium fell from 93% to 12%. Within two hours it was gone. All of it, the squeeze and the unwind, ran inside Robinhood's overnight equity session, before the NYSE opened.

This piece reflects the chain as of block 50,772,447, 09:54 UTC on Monday, August 31. The supply figures, pool prices, and mint events below are read directly from Robinhood Chain contracts at pinned blocks, with addresses cited so you can check them. The trigger for looking was [a thread by @0xSammy](https://x.com/0xSammy/status/2094217003523334417) that circulated overnight; where a figure comes from his snapshot rather than our own reads, it is attributed.

## The Setup Robinhood Built

We covered [Robinhood Chain at launch](/robinhood-chain) in July: an [Arbitrum](/arbitrum) Orbit L2 settling to [Ethereum](/ethereum), built for tokenized stocks, with [Uniswap](/exchanges) v4 as its day-one AMM. That piece established two structural facts that matter here.

First, the stock tokens are not shares. They are tokenized debt securities issued by a Robinhood subsidiary, redeemable for cash through authorized participants, tracking the stock's price. The HIMS token on Robinhood Chain ([0xCceE82fE…3D09](https://robinhoodchain.blockscout.com/address/0xCceE82fE024c36fA15E1005edE3E9e4787e23D09), deployed August 10) calls itself "Hims & Hers Health • Robinhood Token." Supply is elastic: an issuer address mints tokens when its broker acquires shares and burns them on redemption. That elasticity is the token's peg mechanism, and it only operates when there is a stock market to hedge against.

Second, the tokens are freely transferable. There is no allowlist on the ERC-20 itself; a transfer to an arbitrary address succeeds. That is the composability Robinhood advertised, and it means anyone can pool the token on Uniswap against anything, without asking. Someone did.

The July piece ended on what we called the liquidity question nobody had answered: whether equities can trade well on an AMM against a reference price that updates only during market hours. The answer arrived two months later, delivered by a memecoin.

## The Pair

BONER ([0x98096d17…1E18](https://robinhoodchain.blockscout.com/address/0x98096d17e191B3dA1d5f99a6D7b3584351b11E18)) deployed on August 20 with a supply of one billion. The joke writes itself: Hims & Hers sells erectile dysfunction treatment, so the memecoin attached to its stock is called BONER. The joke is also the market structure, because BONER's canonical pool is not BONER/USDG or BONER/ETH. It is BONER/HIMS, [pool 0x9c89b043…640d](https://dexscreener.com/robinhood/0x9c89b04303dfa76f3f6fb02c2b77be0e8a00ab8fa00d507119acd54ab3e8640d), created in the same minute as the token, and it is where nearly all of the liquidity sits: roughly $1.2M at the time of writing, against about $160K in the largest BONER/USDG pool.

That routing choice is the whole mechanism. A trader entering BONER with dollars or ETH gets routed through HIMS for any meaningful size, because that is where the depth is: buy HIMS first, then swap HIMS into the BONER pool. Every net dollar of memecoin demand becomes a buy order for the stock token, and the HIMS ends up locked in the pool as the other side of BONER's liquidity. The memecoin is a machine that converts degenerate flow into inventory pressure on a tokenized equity.

This was a known pattern, not an accident. A GME-themed memecoin ran the same structure against tokenized GameStop in July, [pitched explicitly](https://www.tapbit.com/en/learn/article/what-is-gme-on-robinhood-chain-memecoin-stock-token-risks-20260727) on the idea that memecoin buying forces stock-token buying, before fading roughly 99% from its peak. @0xSammy [ran the numbers on an NVDA-paired memecoin](https://x.com/0xSammy/status/2093782862671573455) called AI two days before the HIMS event, noting its ecosystem already touched about 17% of the chain's tokenized NVIDIA supply and that weekends expose the fault line most clearly. He then watched the fault line fail in real time on a smaller stock.

Because that is the other ingredient: HIMS was small. Total onchain supply going into the weekend was 15,226.8 tokens, worth about $440K at Friday's close, against roughly 225 million real shares outstanding. The float was a rounding error on the equity and a feast for a memecoin.

## The Float Going Into the Weekend

The supply and pool state below are read from the token contract and the Uniswap v4 singleton ([PoolManager 0x8366a39c…0951](https://robinhoodchain.blockscout.com/address/0x8366a39cc670b4001a1121b8f6a443a643e40951)) at pinned blocks. The onchain HIMS price is the main HIMS/USDG pool's spot price; the premium is measured against Friday's [$28.84 NYSE close](https://stockanalysis.com/stocks/hims/).

| Time (UTC) | Block | HIMS supply | In Uniswap v4 pools | Onchain price | vs. close |
|---|---|---|---|---|---|
| Fri 19:40 | 48,555,213 | 16,126.8 | 12,689.1 (78.7%) | $28.17 | -2.3% |
| Sat 11:40 | 49,125,754 | 15,226.8 | 12,085.3 (79.4%) | $30.36 | +5.3% |
| Sun 11:40 | 49,980,825 | 15,226.8 | 12,424.2 (81.6%) | $29.68 | +2.9% |
| Sun 19:40 | 50,265,277 | 15,226.8 | 11,964.4 (78.6%) | $29.38 | +1.9% |
| Sun 23:53 | 50,415,299 | 15,226.8 | 13,883.2 (91.2%) | $43.27 | +50.0% |
| Mon 09:54 | 50,772,447 | 33,977.3 | 32,086.5 (94.4%) | $29.48 | +2.2% |

The first rows carry two details worth pausing on. The float shrank going into the weekend: two burns, of 500 and 400 tokens, executed at 20:37 and 21:21 UTC on Friday, within 90 minutes of the NYSE close, from a redemption wallet ([0xa8553db0…3c74](https://robinhoodchain.blockscout.com/address/0xa8553db0049fc6843c0d00d0efc08d31848e3c74)). Someone redeemed 900 HIMS for cash right before the two-day window in which no more could be created, cutting the float by 5.6% at the worst possible moment.

And the market-making wallets carried nothing across the weekend. The address that receives all newly minted HIMS ([0xcfaece21…0a94](https://robinhoodchain.blockscout.com/address/0xcfaece2151502da2a21d47234ae1f08618a60a94)) and the wallet it forwards to ([0x1a18a8b9…a4e7](https://robinhoodchain.blockscout.com/address/0x1a18a8b96eac3f980133a18402d04194f1faa4e7)) both held zero HIMS at every snapshot from Friday through the squeeze. Inventory management here is just-in-time: mint, forward, sell. Which works until the mint switch is off and the float you would normally replenish is being eaten by a token named after an erection.

## Sunday Night

BONER had actually drifted down through the weekend, from about $0.0036 on Friday to $0.0024 by Sunday evening, priced through its HIMS pool. Then, at around 22:00 UTC on Sunday, the buying started.

The main HIMS/USDG pool never had the depth to absorb what came next. At our 23:53 UTC reference block, mid-squeeze, its in-range reserves were on the order of a few hundred HIMS; @0xSammy's snapshot during the event put it at roughly 92 HIMS against $135K of USDG. Almost all of the actual HIMS inventory sat inside BONER/HIMS instead: our estimate from the pool's live liquidity at 23:53 UTC puts about 13,100 of the 15,227 tokens there, assuming full-range positions (his earlier snapshot: 12,284, or 81%). Inside that pool the HIMS was the denominator of a memecoin pump, not an offer waiting to be lifted.

So the dollar pool's price did what a nearly empty pool does. Sampled at roughly eight-minute intervals from the HIMS/USDG pool's slot0:

| Time (UTC) | Onchain HIMS | vs. $28.84 close |
|---|---|---|
| Sun 21:46 | $29.73 | +3.1% |
| Sun 22:28 | $36.22 | +25.6% |
| Sun 23:02 | $39.94 | +38.5% |
| Sun 23:36 | $61.15 | +112.0% |
| Sun 23:53 | $43.27 | +50.0% |
| Mon 00:13 | $34.33 | +19.0% |
| Mon 00:43 | $54.50 | +89.0% |
| Mon 00:47 | $55.61 | +92.8% |
| Mon 00:55 | $32.37 | +12.3% |
| Mon 01:59 | $29.31 | +1.6% |

![Line chart of the tokenized HIMS spot price in its HIMS/USDG pool on Robinhood Chain from Sunday 19:40 UTC to Monday 08:26 UTC. The price holds near the $28.84 NYSE Friday close until about 22:00 UTC Sunday, spikes twice to $61.15 and $55.61, then collapses within minutes of the first 1,000-token mint at 00:43:30 UTC, marked with a vertical line, and stays within 2% of the close from 02:00 UTC on. Source: slot0 reads at pinned blocks.](/images/blog/tokenized-stock-float-squeeze-premium.png)

These are spot samples, so prints between them may be higher; the pool crossed 2x NAV at least once. The swings of 30% or more between adjacent samples are the point: with a few hundred tokens of depth at best, individual swaps were repricing the "stock" by more than the stock moves in a bad quarter. @0xSammy's thread quoted about $39 and a 37% premium; that was a real print from the calmer part of the window, and understated the extreme.

The premium also fed back into how big the memecoin looked. BONER's displayed market cap is its HIMS-pool price times a dollar mark for HIMS, so with the wrapper at $43 instead of $28.84, a screenshot showed $9.4M where Friday's marks implied about $6.9M. His arithmetic on that point checks out against the pool ratios at our reference block. Roughly a quarter of the memecoin's headline valuation was the premium on its quote currency.

Nothing happened to Hims & Hers in any of this. No shares traded, and nobody's short position was touched. The company has around 225 million shares outstanding; the entire squeezed float was 15,227 wrapper tokens. This was a corner in a warehouse receipt, not in the commodity.

## The Mint Response

Robinhood's 24/5 equity session reopens at 8:00 pm Eastern on Sunday, which is 00:00 UTC Monday. The first HIMS mint since Friday landed at 00:43:30 UTC, 43 minutes into that session: 1,000 tokens to the issuer's distribution wallet, in [tx 0x459aee54…066b](https://robinhoodchain.blockscout.com/tx/0x459aee54624bbef4ccabb6e872ec08414c97cd97bda4f92048cabb011e5a066b), called directly on the token contract by an issuer signer ([0x2b94105f…3a87](https://robinhoodchain.blockscout.com/address/0x2b94105fff37630f98e1f24811dad588fc5c3a87)). The next three 1,000-token clips followed within 25 minutes.

The timing tells you what gates issuance. Monday's opening bell had nothing to do with it. Mints resumed once a venue existed where the issuer's broker could buy the underlying, plus the operational lag of acting on it; whether the viral post 30 minutes earlier hurried the desk along is unknowable from the chain, but nothing could have minted before the venue opened either way. From Friday's burns at 21:21 UTC until 00:43:30 UTC Monday, a span covering the entire weekend, the mint function was silent. Then, in the nine hours between the first mint and our final snapshot, the issuer minted 294 times for a total of 18,750.5 new HIMS, every event a transfer from the zero address to the same distribution wallet, more than doubling the token's supply. Half of that volume had landed by 01:56 UTC. There were no burns.

The distribution wallet forwarded the tokens to the market-making wallet, which sold them into the pools as they arrived (it ended the morning holding under 25 HIMS), which is why the premium died the way it did: $55.61 at 00:47, $32.37 at 00:55, back inside 2% of Friday's close by 02:00 UTC. The economics of that trade are the disciplining force in this design. Whoever mints at NAV and sells into a 90% premium keeps the difference, and the flip side is that everyone who paid $40 or $55 for a $28.84 wrapper on Sunday night handed that difference over. There was no short seller on the other side of this squeeze, only future supply.

A final number from the aftermath: the mints did not kill the memecoin. BONER's HIMS-denominated price kept climbing through the unwind, and at our 09:54 UTC snapshot it stood at roughly $0.0147, about 4x its Friday level, an implied cap around $14.7M on the fixed billion-token supply, with about $4.9M of 24-hour volume through the HIMS pair per DexScreener. The squeeze resolved; the flow that caused it did not.

## What This Mechanic Actually Is

Calling it a short squeeze, as half of crypto Twitter did overnight, gets the flavor right and the mechanism wrong. Nobody was forced to buy. The accurate frame, and the one @0xSammy himself used, is a float squeeze: demand absorbed a fixed float faster than the issuer could expand it, during a window in which the issuer could not expand it at all.

The general rule: any wrapper whose supply elasticity follows the underlying market's calendar will trade like a closed-end fund whenever that market is closed. Premiums and discounts to NAV are then set entirely by the wrapper's own float and flow. Tokenized equities on a 24/7 AMM have this property for the 48 hours between Robinhood's Friday-evening close and its Sunday-evening reopen, and the float side is not hypothetical: on this chain, a memecoin can be deliberately plumbed into a stock token's routing so that its demand lands on a four-hundred-thousand-dollar float. In the [Distributed vs. Represented framing](/distributed-vs-represented-rwa-framework) we use for RWAs, the token is Distributed enough to be composable into anything, while the thing that keeps it honest, issuance against the real asset, stays Represented, permissioned, and on a Monday-to-Friday schedule. The squeeze lived exactly in that gap.

Who bears the risk deserves precision. The issuer's mint-at-NAV arbitrage is riskless in direction; it earned the premium. The company's stock never traded. The loss concentrates on whoever bought the wrapper above NAV without understanding that the ceiling was two days of market closure, and the depth of that loss was set by a dollar pool holding a few hundred tokens at best. The July launch piece flagged thin AMM books against an external reference price as the structural worry; a memecoin turned out to be the stress test, and the books were thinner than even the bears assumed.

The audience is split oddly, too. Robinhood's stock tokens are blocked for US retail, the exact crowd that made GameStop a phenomenon. The memecoins paired against them carry no such gate. The practical effect is a two-tier market in which the people barred from the wrapper can still trade the memecoin whose only pricing leg runs through it.

## What to Watch

@0xSammy's follow-up pointed at [the most-shorted-stocks list as a target menu](https://x.com/0xSammy/status/2094217003523334417) for the next iteration, and replies flagged a memecoin already paired against tokenized Lockheed Martin. The playbook is public now, and it is cheap: pick a stock token with a small float, launch the joke, pool it against the stock, and let weekend routing do the work. Larger floats resist the corner better; by @0xSammy's own accounting two days earlier, the AI memecoin's ecosystem had absorbed about 17% of tokenized NVDA's 42,664-token supply without a comparable dislocation. The candidates are the small, freshly listed wrappers.

For the issuer, the fixes are mundane and all cost money: carry standing inventory across weekends, pre-mint against Friday buying pressure, or accept that the wrapper trades at whatever its float trades at for two days a week. For everyone else, the practical takeaways are narrower. A tokenized stock's onchain price is only NAV while the mint window is open; check the supply and where it sits before treating the print as the stock. And a memecoin's market cap, when its quote currency is a wrapper trading above NAV, is marked against a number that a few swaps can manufacture.

The whole episode, corner, premium, mint, collapse, ran in under five hours on a Sunday night, and the second-order effects landed nowhere: the NYSE opened Monday to a stock that never knew anything happened. That is either the system working, an arbitrage closing exactly as designed the moment it could, or a small-scale rehearsal of what happens when the float is bigger, the memecoin is angrier, and the weekend is longer. On the evidence of the last two months of Robinhood Chain, we will not have to wait long to find out which.
