---
layout: blog
title: "Jupiter launches YOLO beta with house-backed profit queue"
url: /jupiter-yolo-beta-trades-against-house-pool.html
h1title: "Jupiter YOLO beta trades against a house pool"
pagetitle: "Jupiter launches YOLO beta for 1,000x crypto trades"
metadescription: "Jupiter's YOLO beta offers up to 1,000x leverage, with profits paid by a house pool and queued when the pool cannot cover them."
category: blog
featured-image: /images/blog/jupiter-yolo-beta-trades-against-house-pool-ogp.png
intro: "Jupiter has opened an unaudited beta for leveraged $SOL, $BTC, and $ETH positions whose profits depend on a house-funded pool."
author: sawinyh
tags: ["News"]
date: 2026-10-16T09:18:47+00:00
---

Jupiter [introduced YOLO](https://x.com/JupiterExchange/status/2110708473793257503) on October 15 as a live beta for leveraged $SOL, $BTC, and $ETH price trades. The [product interface](https://jup.ag/yolo/?market=SOL) was live the following day with leverage settings from 500 to 1,000 times and a default payment amount of $10.00.

The product is an unaudited Jupiter Labs experiment. Its structure differs from an order book or a conventional perpetual futures venue because each trader faces a house pool rather than another trader. Trader losses add money to that pool. Winning traders receive profit from the same pool.

## How a YOLO position works

YOLO supports three markets: $SOL, $BTC, and $ETH. The interface accepts market orders only. It does not offer take-profit or stop-loss orders. A liquidation consumes the collateral assigned to the position.

Leverage starts at 500 times and reaches 1,000 times. Jupiter warns that small price moves at those settings can wipe out the entire position. The collateral placed on a trade therefore defines the amount immediately at risk, while the selected leverage determines the position's exposure to price movement.

The interface separates collateral from position size. Its stated limits apply to position size, not to the collateral paid by the trader. Long and short capacity are also separate. Available capacity can change before a submitted trade executes. A user who sees room on one side of a market is not guaranteed the same capacity on the other side or at execution.

Pricing has two references. Jupiter displays Pyth prices as indicative data, but says orders execute at the on-chain DOVES price. The displayed Pyth price is therefore not the execution commitment. A trader must use the executed DOVES price when checking the entry or exit recorded for a position.

The fee schedule depends on the result. A winning move of 0.2 basis points or less produces no profit. Larger winning moves receive a profit adjustment, followed by a 2% fee on adjusted profit. Jupiter says losing trades have no trading fee, while wallet network fees still apply.

## The house pool controls profit payment

The house takes the opposite side of every position. Trader losses fund it, and trader profits are claims on its available funds. That makes pool liquidity part of the settlement path for a winning trade.

Closing a position returns the trader's remaining collateral immediately in $JupUSD. Profit follows a different path. If the house can cover the profit, it can pay from the pool. If the house cannot cover it, the unpaid amount enters a queue. Earlier winning claims receive payment first when new trader losses replenish the pool.

Jupiter gives no fixed waiting time for queued profit. Its rules state that queued profit may never be paid. A closed position therefore fixes the trading result without guaranteeing that all profit has reached the wallet. The distinction matters when a trader evaluates available funds after closing. Returned collateral and unpaid profit do not have the same liquidity.

Position history also has a short finalization period. Jupiter says closed positions finalize on chain in about 15 seconds. Until finality, the history view labels the close as finalizing. Users checking a recent close need to distinguish this brief on-chain state from the separate profit queue, which has no guaranteed payment time.

## What changes for traders and operators

For traders, the full stake can disappear after a small adverse move because the available leverage begins at 500 times. There is no stop-loss order to cap that process from within the product. Risk control therefore happens through the collateral committed before execution and through a manual close while the position remains open.

A profitable close creates a second risk to track. The trade can finish in profit while some or all of that profit remains unpaid. Jupiter says queued claims are paid automatically to the wallet as the pool receives funds, but the queue is first in, first out and has no deadline. Traders cannot treat a displayed profit and spendable wallet balance as interchangeable.

For wallet interfaces, portfolio trackers, and accounting systems, a closed position can have three distinct states: collateral returned, close awaiting on-chain finality, and profit queued for payment. Systems that record only open or closed status can miss whether a winning claim is still outstanding. The product's history label covers finalization, while the house queue determines payment.

Operators also need to account for capacity changing before execution. Long and short limits are separate, and the displayed Pyth price is indicative rather than the fill price. A trade preview can change in both available size and execution price by the time the order reaches the on-chain DOVES system.

The fee rules create another reconciliation step. A small favorable move can close without profit when it is at or below the stated threshold. A larger win is adjusted before the profit fee is charged. The resulting wallet payment can then differ from the raw price move shown on the chart, even before any profit enters the house queue. Network fees remain separate from that calculation.

The queue also separates trading performance from counterparty liquidity. Earlier unpaid wins have priority over later ones, and fresh trader losses replenish the pool used for payment. A later winner may therefore wait behind claims created before that trade closed. The rules promise automatic wallet payment when funds become available, but they do not promise when that replenishment will occur.

The unresolved issue is the durability of the house pool under one-sided winning flow. Jupiter's rules explain the queue and payment order, but they do not give a maximum delay or a guaranteed backstop. The next observable milestone is whether queued profit appears and how quickly subsequent trader losses replenish the pool.
