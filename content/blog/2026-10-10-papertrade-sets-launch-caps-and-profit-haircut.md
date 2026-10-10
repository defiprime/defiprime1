---
layout: blog
title: "Papertrade Sets Launch Caps and Profit Haircut for HyperEVM Trading"
url: /papertrade-sets-launch-caps-and-profit-haircut.html
h1title: "Papertrade sets launch caps and profit haircut for HyperEVM trading"
pagetitle: "Papertrade sets HyperEVM launch caps and profit haircut"
metadescription: "Papertrade scheduled HyperEVM trading for 14:00 UTC with $1 billion of per-side OI headroom, relayer-controlled flow and asymmetric profit fees."
category: blog
featured-image: /images/blog/papertrade-sets-launch-caps-and-profit-haircut-ogp.png
intro: "Papertrade has set a 14:00 UTC start for its HyperEVM perpetuals venue, with $1 billion of new per-side OI headroom and relayer-controlled launch traffic."
author: sawinyh
tags: ["News"]
date: 2026-10-10T10:19:29+00:00
---

Papertrade [scheduled live trading](https://x.com/papertrade_xyz/status/2108852108766437759) for 14:00 UTC on October 10, 2026, after the planned HyperEVM network upgrade. The launch configuration gives each market and side $1 billion of new open-interest headroom, while the protocol frontend controls transaction submission through a relayer.

The schedule turns the earlier pre-deposit phase into a fixed launch window. Papertrade plans to pause deposits at 13:45 UTC, fifteen minutes before trading starts, so the relayer can give trading traffic priority. Users who want to take part at launch need to fund their accounts before that pause.

## How the launch queue works

Papertrade expects congestion when trading opens. The team warned that smaller-notional trades may wait longer for confirmation. Its relayer determines how transactions reach HyperEVM, while operations such as staking distributions run separately in large batches. The team also said the chain will appear to use half of its available gas because pushing beyond that point would quickly make fees unaffordable.

The arrangement makes the frontend part of the launch mechanism rather than a simple interface. Papertrade's [staged rollout](https://x.com/papertrade_xyz/status/2105735549822919150) requires all phase-one transactions to use whitelisted relayers. Direct contract interaction remains closed during this phase. Each signed action enters an adaptive intent system that ranks activity mainly by transaction type and notional value. Liquidations rank above position opens, and a user can cancel a trade while it is still waiting in the relayer.

That ordering has two direct effects for traders. Pre-depositing avoids putting account creation and funding behind live trading. A submitted position is also not final merely because it appears in the relayer queue, since the user can cancel it before execution. The launch post does not give a date for direct contract access. It says that phase two begins after congestion has passed and the team no longer sees a risk of MEV competition.

## Position limits and settlement economics

The launch sets an individual atomic-position limit of 10 million. A trader may hold more than one position at that size. Papertrade also uses floating OI headroom for each market and direction to limit how much exposure can open over a short period. The initial setting is $1 billion for every market and side.

The [risk documentation](https://docs.papertrade.xyz/#/how/risk) describes that number more precisely. A keeper targets current OI plus $1 billion of exposure valued at the current best bid and offer. It leaves the cap unchanged while headroom stays within a 10% band, from $900M to $1.1B, and rebuilds the cap toward $1 billion after headroom leaves that range. The setting limits new directional exposure. It is not a total OI ceiling or a maximum-loss guarantee.

Papertrade does not use a conventional notional trading fee, spread or funding payment. Its [asymmetric PnL mechanism](https://docs.papertrade.xyz/#/how/asymmetric-impact) instead reduces profitable closes. The contract first measures a gain after moving the exit price 0.2 bps against the trader. A smaller gain becomes zero. The remaining profit goes through an impact formula, followed by a 2% win fee. The trader receives 98% of the scaled gain. Losing positions pay no additional amount beyond their loss.

At launch, the formula uses a 10% base rate, a 15,000 rate multiplier and a $100,000 reference notional for both $BTC and $ETH. The position multiplier is 814.598 for $BTC and 483.979 for $ETH. A profitable close cannot retain more than 90% of raw profit before the separate win fee. Papertrade's example says a 1% $BTC move keeps about 88% of raw profit after the deadband but before the win fee, while a 0.1% move keeps about 74%.

Position size does not change the percentage haircut. The documentation says the same curve applies to a $100 close and a $100K close because Papertrade substitutes a fixed reference notional for actual position size. The percentage penalty instead falls as the entry-to-exit price move grows. This makes very small profitable moves the most heavily reduced.

For traders, the fee schedule makes the size of the market move more important to the haircut than the size of the position. A close after a gain below 0.2 bps becomes zero before impact scaling. Above that threshold, larger moves retain a higher share, while a $100 close and a $100K close face the same percentage curve.

## Controls and the unresolved price risk

The launch gives protocol administrators three roles. A two-of-three multisig held by Ize-bel, Blurr and Ungus Trade controls those roles. The guardian can halt new opens or freeze a market while allowing existing positions to close against the frozen midpoint. The owner can change the impact curve and fees, replace relayers and keepers, list markets, and upgrade contracts. Contract upgrades carry a seven-day timelock. The markets role controls directional OI headroom, minimum margin and minimum position size.

Users still sign every relayed intent with their wallet or session key, according to the risk documentation. The relayer cannot act on an account without that signature. Withdrawals remain user-controlled, and the contract has no administrator function that can directly stop withdrawals from user balances.

The unresolved risk is the price input. Papertrade reads Hyperliquid's best-bid-and-offer midpoint without an independent reference price. Its own documentation says an attacker could place an unfilled order inside the natural spread, shift the midpoint by a tick or two, and try to profit when the quote returns. The 0.2 bps deadband, profit haircut and OI caps reduce the possible payoff but do not prove that manipulation is unprofitable.

The next dated milestone is the 13:45 UTC deposit pause, followed by the planned 14:00 UTC trading start. After that, the open question is whether the relayer can clear launch demand without making smaller trades wait long enough for their intended entry to lose relevance.
