---
layout: blog
title: "Papertrade Opens Pre-Deposits Before HyperEVM Perpetuals Launch"
url: /papertrade-opens-predeposits-before-hyperevm-launch.html
h1title: "Papertrade opens pre-deposits before HyperEVM perpetuals launch"
pagetitle: "Papertrade opens pre-deposits for HyperEVM launch"
metadescription: "Papertrade has opened pre-deposits before its HyperEVM perpetuals launch, with a zero-funded LP, queued profits and loss-based PAPER emissions."
category: blog
featured-image: /images/blog/papertrade-opens-predeposits-before-hyperevm-launch-ogp.png
intro: "Papertrade has opened pre-deposits for a staged HyperEVM launch built around synthetic perpetuals, a self-funded liquidity pool and queued profit claims."
author: sawinyh
tags: ["News"]
date: 2026-10-09T08:35:54+00:00
---

At 16:33 UTC on October 8, 2026, Papertrade [opened phase-zero pre-deposits](https://x.com/papertrade_xyz/status/2108234249904275922) on HyperEVM for a perpetuals venue whose liquidity pool starts at $0. The team expects live trading to begin around one hour after HyperEVM's scheduled October 10 network upgrade, although it said the upgrade time was not known in advance and could slip into October 11.

The deposit window separates account creation and funding from the expected launch traffic. Papertrade said deposits and new accounts will receive much lower priority once trading starts. Depositing earlier within the pre-launch window does not earn an advantage.

## A venue where traders face the pool

Papertrade describes the protocol as a [fully on-chain perpetuals exchange](https://docs.papertrade.xyz/#/intro/what-is-papertrade) with leverage up to 1000 times. Trades are synthetic swaps between each user and the protocol liquidity pool. There is no order book, matching engine or external counterparty for the trade.

The contract reads Hyperliquid's best-bid-and-offer midpoint through a HyperCore precompile when a position opens and again when it closes. That midpoint fixes the entry and exit prices. No perpetual contract changes hands on Hyperliquid. Papertrade therefore charges no funding cost and states that users receive the midpoint without slippage, subject to open-interest limits for each instrument.

The fee model moves the cost to profitable closes. Papertrade [applies an asymmetric impact haircut](https://docs.papertrade.xyz/#/learn/wins-losses) to raw gains, with smaller price moves losing a larger share of their profit. A 2% win fee then applies to the remaining gain. Losing positions pay their raw loss without an additional charge and receive PAPER according to the emissions curve.

That design makes the pool the direct counterparty to every trade. User losses add funds to it. User wins remove funds. The balance begins without seed capital, a founder deposit or an upfront LP raise, and users cannot deposit directly into it. This makes early solvency depend on the sequence and size of trading outcomes.

For an early trader, quoted execution and settlement are separate concerns. The contract can close a position at the stated midpoint while the pool lacks cash for the profit. The trade record then becomes a queue claim rather than an immediately available balance. Users evaluating leverage therefore need to account for both liquidation exposure and the pool's ability to settle a winning result.

## What happens when a winner cannot be paid

The protocol uses a [first-in, first-out payout queue](https://docs.papertrade.xyz/#/learn/lp-queue) when the pool lacks enough $USDC to settle a winning close. The unpaid profit becomes an on-chain debt claim. Future trading losses refill the pool and pay claims from the front of the queue.

For a position funded from a user's available balance, the original $USDC margin returns immediately at close. Only unpaid profit enters the queue. A position opened using a queued balance behaves differently because its margin was already a debt claim. The surviving claim can return to the queue when that position closes.

This distinction matters for traders deciding whether to recycle an unpaid claim. A displayed win does not guarantee immediately withdrawable profit when the pool is short. The docs call the queue a delay rather than a haircut, but its payment timing depends on later users losing enough money to restore solvency.

The mechanism also changes the economics of PAPER. Supply starts at zero, with no pre-mint, team allocation, venture allocation, airdrop or vesting. Realized losses mint the token. While tracked LP remains below $2M, including when it is underwater, the stated rate is 100 PAPER for every $1 of eligible loss basis. The rate then declines along the emissions curve. PAPER will support staking and unstaking at launch but will not initially move between wallets.

Stakers receive $USDC from two documented routes. When the payout queue is empty and the pool can cover distributions, stakers receive 1% of realized profit and loss from settled trades, subject to the protocol's listed exceptions. Once tracked LP exceeds the $5M staker reward cap, further LP gains can be distributed in full through the keeper function. Below that cap, the 1% share is the only stated staker distribution.

## Launch controls and the oracle risk

Papertrade's [launch plan](https://x.com/papertrade_xyz/status/2105735549822919150) initially routes transactions through its frontend and whitelisted relayers. The contract will not accept direct public interaction during phase one. The relayer uses an intent system that prioritizes activity by transaction type and notional value, with liquidations ranked ahead of position opens. Pending trades can be cancelled before processing.

Direct contract access is planned for phase two after launch congestion passes. Builder codes are planned for phase three, allowing frontends and routers to collect a 1% frontend fee. Token transfers are assigned to phase four. The team has not supplied dates for those later phases.

The documentation names [best-bid-and-offer manipulation](https://docs.papertrade.xyz/#/how/risk) as the main unresolved protocol-level risk. An attacker could place a small limit order inside Hyperliquid's natural spread without filling it, shifting the midpoint used by Papertrade. The pricing pipeline has no independent reference price that can reject such a quote. Open-interest caps and the profit haircut can reduce the possible payoff, but the docs say manipulation and LP loss remain possible.

The relayer cannot act without a wallet or session-key signature, according to the same risk disclosure. Users retain a direct withdrawal path, and the contract has no administrative kill switch over user balances. Those controls limit the relayer's authority, while the pool, queue and oracle still determine settlement risk.

Live trading is the next test. It is expected roughly one hour after the October 10 HyperEVM upgrade, with timing dependent on the network event. The first sessions will show whether pre-deposits reduce account congestion, how quickly the zero-funded pool gains solvency, and whether winning traders receive $USDC immediately or begin filling the payout queue.
