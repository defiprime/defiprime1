---
layout: blog
title: "Papertrade Tightens OI Caps After BBO Manipulation Attempts"
url: /papertrade-tightens-caps-after-bbo-manipulation.html
h1title: "Papertrade Tightens OI Caps After BBO Manipulation Attempts"
pagetitle: "Papertrade Tightens Caps After BBO Manipulation"
metadescription: "Papertrade is tightening open-interest caps after manipulation attempts targeted the Hyperliquid BBO used to price its 1000x synthetic trades."
category: blog
featured-image: /images/blog/papertrade-tightens-caps-after-bbo-manipulation-ogp.png
intro: "Papertrade said it is tightening open-interest caps after traders targeted the Hyperliquid best-bid-and-offer midpoint that prices positions on its synthetic perpetuals exchange."
author: sawinyh
tags: ["News", "DeFi"]
date: 2026-10-11T23:20:08+00:00
---

On October 11, Papertrade [acknowledged overnight manipulation attempts](https://x.com/papertrade_xyz/status/2109308773231911359) against the Hyperliquid best-bid-and-offer feed used for its $BTC and $ETH markets. The team said the exchange had a $5m liquidity pool one day after launch and had paid 25M to stakers. It also said it had begun tightening open-interest caps onchain and at the relayer level.

The statement did not identify the wallets, give transaction hashes, or quantify the LP loss from the attempts. Papertrade said one user who initially won continued through new accounts and ultimately returned almost all of that profit to the house. It also said some users agreed to undo manipulated trades in exchange for the PAPER they had farmed. Those assertions came from the team and were not accompanied by an onchain incident report.

## Why the BBO can be moved

Papertrade does not execute a corresponding perpetual trade on Hyperliquid. Its [smart contract creates a synthetic swap](https://docs.papertrade.xyz/#/intro/what-is-papertrade) between the trader and Papertrade's LP. The contract records Hyperliquid's order-book midpoint at entry, reads it again at close, and settles the resulting profit or loss against the LP. There is no Papertrade order book, matching engine, or second trader on the other side.

The protocol reads the best bid and best ask through Hyperliquid's [BBO precompile](https://docs.papertrade.xyz/#/how/pricing-bbo) at `0x000000000000000000000000000000000000080e`. Its execution price is the midpoint of those two values. The documentation says the precompile returns consensus-verified HyperCore state, with no offchain signer or separate oracle committee.

That direct connection also creates the manipulation path. Papertrade's documentation says an actor can try to widen the spread or move the inside quote on Hyperliquid for a block, then trade against the distorted midpoint on Papertrade. The oracle rejects a zero value or a crossed book where the ask is below the bid. It has no maximum-deviation check, time-weighted-price check, or lookback breaker. A nonzero, uncrossed quote can therefore pass even when someone has moved it.

Papertrade's [risk documentation](https://docs.papertrade.xyz/#/how/risk) gives a smaller-scale version of the same problem. A limit order can sit inside Hyperliquid's natural spread without filling, change the best bid or ask, and shift the midpoint by a tick or two. The pricing pipeline has no independent reference price against which it can reject that quote.

## What the cap change does

Papertrade said the launch caps were deliberately permissive because queued demand had congested the exchange. The team argued that tighter caps during that period would have made the queue slower, while uncertain confirmation times made the manipulation strategy harder to time. Once congestion declined, it started reducing caps both in the contract and in the relayer.

The caps constrain how much new directional exposure can be added. Each instrument has separate long and short limits, and an opening trade reverts if it would take the selected side above its cap. The published launch policy targeted current open interest plus $1 billion of additional asset exposure on each side. The keeper was meant to leave that limit unchanged while headroom remained inside a 10% band, from $900M to $1.1B.

A lower cap reduces the position size available to a trader trying to profit from a moved quote. It does not validate the BBO or limit the loss on positions already open. Papertrade's own risk page says the caps are neither a total-open-interest ceiling nor a protocol-loss ceiling. The team described manipulation as always possible in this design and said its objective is to set parameters that make an attempt almost never profitable.

The protocol also uses two economic controls. A 0.2 bps deadband removes very small gains before the profit calculation proceeds. An asymmetric-impact curve then applies its largest haircut to the smallest profitable price moves. The documentation says neither control proves manipulation is unprofitable, and a manipulated quote can still pass the oracle.

## What traders and stakers face

Papertrade offers $BTC and $ETH positions with leverage up to 1000x. A single position can have at most $10M of notional exposure. Positions execute without slippage at the observed midpoint, and profitable closes pay a 2% win fee after the asymmetric-impact adjustment. These terms make the integrity of one block's BBO directly relevant to both the trader and the LP.

Every trade settles against the same $USDC LP. The LP takes the opposite side of each position, so a payout caused by a distorted close comes from the same bankroll used for other winners. If the LP cannot pay a profitable close immediately, the unpaid profit enters a first-in, first-out queue and future trader losses refill it. The documentation says original margin from an available balance is returned immediately, while only unpaid profit is queued. A moved BBO can therefore affect LP capital, the timing of winner payouts, and the rewards available to PAPER stakers.

Operators retain two direct controls over new risk. The market keeper can lower a market's long or short cap to zero without freezing the live BBO used for closes. The pause guardian can permanently retire a market identifier, freeze its BBO at retirement, and leave existing positions closeable at that frozen price. A separate global gate can halt new positions across all markets while closes continue against live prices.

Papertrade has also [scheduled an LP reward-cap change](https://x.com/papertrade_xyz/status/2108992674187354553) from $5m to $10m shortly after 18:45 UTC on October 17. Excess bankroll above that cap is distributable to stakers, so the higher threshold changes when LP gains become available for distribution. The next risk check is whether the tighter directional caps prevent another profitable BBO manipulation attempt before that parameter change takes effect.
