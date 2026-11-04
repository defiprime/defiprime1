---
layout: blog
title: "Robin Markets winds down V1 and ends yield subsidies"
url: /robin-markets-v1-shutdown.html
h1title: "Robin Markets winds down V1 and ends yield subsidies"
pagetitle: "Robin Markets winds down V1 and ends yield subsidies"
metadescription: "Robin Markets is winding down its prediction-market yield product, ending bonus accrual while keeping withdrawals open and planning a replacement."
category: blog
featured-image: /images/blog/robin-markets-v1-shutdown-ogp.png
intro: "Robin Markets is winding down its first yield product after thin matching and weaker Polygon yields undermined its subsidized returns."
author: sawinyh
tags: ["News"]
date: 2026-11-04T07:35:44+00:00
---

On November 3, 2026, Robin Markets [announced the wind-down of its V1 yield product](https://x.com/robinmarketsxyz/status/2117727114040389862), blaming thin matching between opposing prediction-market positions and deteriorating yields on Polygon. The team said the product would remain online until a replacement launches before year-end, with withdrawals continuing afterward.

Robin has already stopped the subsidies. Its [updated yield terms](https://docs.robin.markets/yield-guarantee) say the minimum 6% APY guarantee and extra 1% APY matching bonus ended on November 3 at 20:00 UTC. The points programme ended at the same time. Previously accrued bonuses remain payable on withdrawal; positions staked after the cutoff earn organic vault yield only.

Existing depositors can withdraw now. The announcement sets no withdrawal deadline. Robin wrote: “Withdrawals will also work afterwards, but if you have an open position, you can withdraw it now.”

## Matching left early deposits idle

Robin's product took Polymarket YES and NO tokens and matched opposing positions within each market. The vault could merge matched tokens into $USDC and deploy the proceeds into yield strategies. According to the shutdown statement, maximum capital efficiency required a reasonably balanced distribution of both sides.

Early depositors could leave their tokens idle until someone deposited the opposite side. Traders waited instead of providing the initial liquidity. Robin said its product “frequently left the earliest users earning nothing.” The operator described thin pools and unattractive yields reinforcing each other, leaving the product short of the traction it had expected.

The [product documentation](https://docs.robin.markets/how-it-works) explains how a depositor's market exposure survives the merge. Depositors receive vault shares representing their position and proportional claim on future yield, with a distinct share token for each market side. The vault can deploy the underlying capital while the shares continue to track the depositor's original outcome position.

Yield allocation also depends on the market and side represented by those shares. The docs allocate returns to markets according to their contribution of collateral from paired tokens, then weight the YES and NO sides using Robin's time-weighted average price oracle. Internal yield indices track the amount owed to each user. Matching determines how much capital can earn yield; those allocation rules determine how the earnings are distributed.

Robin said the external yield environment weakened alongside the matching problem. It had partnered with Yearn and initially found viable sources for $USDC.e on Polygon, but said more venues subsequently wound down or became uncompetitive. Robin funded the guarantees itself, and weaker yields put more pressure on those subsidies. The shutdown statement gives no current vault balance or quantified subsidy bill to accompany the operator's account.

## What stops accruing and what remains payable

Robin funded the former guarantee through a top-up from its own wallet. It calculated what 6% APY would have paid and covered any shortfall in the vault's return. A position whose vault return exceeded the guarantee kept the higher amount. Robin calculated the guarantee independently for each market, so a stronger return in one market did not subsidize a weaker one elsewhere.

The matching bonus rewarded deposits on the minority side of an unbalanced pool. Under the former terms, the extra 1% APY locked in when a qualifying deposit arrived and continued even if the pool subsequently rebalanced. The new cutoff notice ends that continuing accrual: nothing accrues under the guarantee or matching bonus after the stated cutoff.

The [points programme notice](https://docs.robin.markets/points-program) separately says points no longer accrue or burn, and users can no longer create referral codes. Before closure, referrals generated points that burned automatically while a user had an active stake, adding an extra 1% APY on eligible stake. Points yield earned before closure is still scheduled for payment with the next withdrawal.

Bonus settlement remains separate from the vault redemption. Robin's terms say guarantee top-ups, matching bonuses and points yield are calculated at withdrawal and sent together in a separate $USDC transaction from Robin's wallet. The stated arrival window is a few seconds to a few minutes after the withdrawal confirms. This report has not independently verified a payout through that documented process.

The portfolio's Activity tab provides a line-by-line breakdown of those bonus components. The terms also say Robin may skip very small amounts when transaction costs exceed the payout. To check what an exit paid, a depositor must reconcile the vault withdrawal with the separate bonus transaction from Robin's wallet.

## Withdrawals and supported markets

Under Robin's documented withdrawal flow, the vault burns a user's shares and returns the underlying YES or NO outcome tokens plus earned yield in $USDC. Where capital has been deployed to a strategy, the vault first withdraws it and reconstructs the outcome tokens from collateral within the same transaction. Users need not wait for market resolution to request that redemption.

Robin's [risk guide](https://docs.robin.markets/contracts/risks) warns that lending-pool utilization can temporarily prevent immediate withdrawals when too much liquidity has been borrowed. The same guide says the currently used Split Vault has no liquidity constraints. These are the guide's descriptions of withdrawal capacity; this report has not tested that capacity during the wind-down.

Funds that remain deposited stay exposed to contract risk. The risk guide covers vulnerabilities in Robin's contracts and in the third-party protocols receiving funds, and explicitly says audits cannot eliminate undiscovered bugs. Those disclosed risks remain with an open position after the subsidy programmes end.

A separate [compatibility notice](https://docs.robin.markets/polymarket-v2) limits the current vault to Polymarket's Conditional Tokens Framework markets, using $USDC.e as collateral. Newly created Polymarket Protocol V2 markets use a different token ledger and condition identifiers and cannot be staked in the current vault. Robin marks them unsupported; the existing stakeable list shrinks as its markets resolve.

Robin says the replacement will address matching economics and yield sourcing. The shutdown statement targets a launch before the end of the year but gives neither an exact launch day nor the redesigned mechanism.
