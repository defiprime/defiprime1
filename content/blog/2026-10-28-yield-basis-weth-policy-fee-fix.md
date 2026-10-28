---
layout: blog
title: "Yield Basis discloses fee-extraction route in WETH upgrade"
url: /yield-basis-weth-policy-fee-fix.html
h1title: "Yield Basis discloses fee-extraction route in WETH upgrade"
pagetitle: "Yield Basis WETH upgrade includes deposit fee fix"
metadescription: "Yield Basis proposes Pyth-linked WETH pool fees and a deposit-withdraw fix. Governance remains active, with parameters differing from announcement estimates."
category: blog
featured-image: /images/blog/yield-basis-weth-policy-fee-fix-ogp.png
intro: "Yield Basis has disclosed a deposit-and-withdraw fee-extraction route alongside a proposed Pyth-linked pricing policy for its WETH market."
author: sawinyh
tags: ["News"]
date: 2026-10-28T18:22:52+00:00
---

On October 28, 2026, Yield Basis [disclosed a deposit-and-withdraw route](https://x.com/yieldbasis/status/2115461852368900558) that lets traders extract pool value without paying proper fees. The disclosure accompanied its permissionless propAMM announcement, a proposed overhaul of pricing for the protocol's $WETH market on Curve.

The team said the update closes that route and that technical details will follow after all pools receive the fix. Its announcement describes the new pricing design in the present tense, but also says the upgrades remain subject to governance approval and successful deployment. [Yield Basis proposal 60](https://yieldbasis.com/proposal/60) was still marked active when checked, with voting scheduled to end on October 29.

## A fee fix alongside the oracle change

The [Curve governance proposal](https://gov.curve.finance/t/curve-part-of-turning-weth-crvusd-yieldbasis-pool-into-a-permissionless-propamm/11194) describes the protection more narrowly than the announcement does. New liquidity-token deposits must add debt proportional to their minted LP collateral within 1 bp. The proposal identifies this constraint as protection against value extraction through a deposit followed by a withdrawal. The operator has withheld the remaining details until the rollout reaches every pool.

The same proposal would attach the YBOraclizedPolicy contract to the existing $WETH/$crvUSD Curve pool, leaving the underlying Curve pool contract unchanged. Yield Basis says its DAO owns the policy, while the Curve emergency DAO can switch it off.

The proposal names [0xaea95d551154443e73565be724d59d63d72f8a7d](https://etherscan.io/address/0xaea95d551154443e73565be724d59d63d72f8a7d) as the policy address. A public-RPC reading at Ethereum block 26292974 confirmed deployed code there. That check establishes that the policy contract was deployed. It does not establish that the production pool uses it or that either governance vote has completed.

Yield Basis proposal 60 explicitly depends on execution of Curve vote 1508. It sets a donation APY of 2.60% and a releverage fee of 150 bps. These are the parameters in the executable proposal. The operator's launch article gives a lower donation estimate, so the two documents describe conflicting settings if the announcement is read as the final deployed configuration.

## Fees follow signed market prices

The [research behind the proposal](https://forum.yieldbasis.com/t/oracle-reports-for-yieldbasis-pools-a-new-price-scale-and-fee-policy-for-the-weth-market/40) describes the previous configuration as a native Twocrypto fee curve ranging from 1.36% to 2.82%. It re-centers liquidity toward an average of the pool's own trade prices. The proposed policy uses an external price to determine both swap fees and where the pool concentrates liquidity.

Pyth Pro publishes signed $ETH/USD reports once a second. Anyone can deliver a report, but the policy checks its signature and requires it to be newer than the stored report. It accepts reports only within 12 seconds of observation. Arbitrageurs can bundle a report with their swap because a fresh reference price can reduce their fee. The announcement also describes a keeper delivering reports when the pool has gone an hour without a price or a trade.

Corrective swaps receive the discount. For a trade moving the pool toward the reported market price, the proposed charge starts at 0.50%. When the trader's edge exceeds that threshold, the pool charges the base fee plus 67.5% of the excess, subject to a 1.75% ceiling. Other trades pay 1.75%.

The discount fades as the report ages and disappears after 5 minutes. A corrective trade submitted with a valid report can carry a different fee from the same trade against an older stored report. Arbitrageurs can still choose among eligible recent reports. Yield Basis says it selected the one-second channel to limit the choice of reports available to them.

The reference price also guides `price_scale`, the center of the Curve pool's liquidity. The design uses market-price averages over about 80 and 160 minutes to distinguish a trend from short-lived movement. In a sideways market it stays near the faster average; in a trend it moves toward the current market price.

An accepted report governs the fee and liquidity positioning. The Curve pool formula continues to determine the trade price. Yield Basis says a delivered price cannot block withdrawals, and ordinary pool access remains permissionless even though the policy requires Pyth signatures on its external price reports.

## Backtested returns, with a slower recovery in a rally

Yield Basis reports that a simulated $WETH position earned 8.5% annually in $ETH under the proposed design, compared with 3.6% under the existing settings. The test covers 18 months. These are simulated returns, not returns observed from an activated policy.

The simulator replays Binance trades for each 12-second Ethereum block using historical Pyth prices. Within each block, its arbitrageur selects the eligible report that maximizes profit. The team chose the parameters on the same period it used to report performance. The simulation includes neither ordinary trading flow nor liquidations, limiting how directly the results can be compared with a live pool.

The announcement also identifies a period when the proposed design tracked the market worse. During an August 2026 rally in which $ETH rose 30% in a few days, its simulated `price_scale` fell as much as 12.4% behind the market and remained at least 5% behind for about 11 days. The current settings' maximum lag was 6.3%. The proposed design earned more over the full test period but took longer to catch up with the market during that rally.

The team also tested nearby parameter combinations. It reports that 44 of 49 settings completed the same 18-month simulation with annual returns between 7.4% and 9.9%. Those tests vary the configuration within the historical sample. The team identifies the live $WETH pool as the first test on new data.

A higher amplification parameter is a separate item on the roadmap. Yield Basis says early simulations suggest higher returns at a higher setting, but promises a separate note before making that change.

The planned sequence starts with $WETH, followed by separate votes for the $cbBTC, $WBTC and $tBTC pools after deployment of the first policy. Details of the deposit-and-withdraw issue remain withheld until all pools have the fix; the announcement does not establish that rollout as complete.
