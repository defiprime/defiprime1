---
layout: blog
title: "Lynq and TBMC test institutional settlement into RLUSD"
url: /lynq-tbmc-test-rlusd-institutional-settlement.html
h1title: "Lynq and TBMC complete live RLUSD settlement test"
pagetitle: "Lynq and TBMC complete live RLUSD settlement test"
metadescription: "Lynq and TBMC used live production accounts to convert a client's assets into RLUSD while preserving interest during settlement."
category: blog
featured-image: /images/blog/lynq-tbmc-test-rlusd-institutional-settlement-ogp.png
intro: "Lynq and The Better Money Company completed a live proof of concept that converted a client's assets into $RLUSD through a pre-funded institutional workflow."
author: sawinyh
tags: ["Stablecoins", "News"]
date: 2026-10-14T03:17:54+00:00
---

Lynq and The Better Money Company announced on October 13, 2026 that they had completed a live institutional settlement proof of concept. TBMC converted a client's assets held on Lynq into $RLUSD in a few minutes, although the announcement did not disclose the value transferred or identify the institutional counterparties.

The test matters to treasury and settlement teams because it joined three functions in one live workflow: conversion into the stablecoin required at the destination, settlement outside traditional banking windows, and continued interest accrual while assets were held in transit. It was a small production test rather than a general product launch. Lynq said native stablecoin support remains targeted for the end of 2026.

## What the production test did

The [official announcement](https://lynq.network/lynq-and-the-better-money-company-complete-live-proof-of-concept-for-institutional-stablecoin-settlement-in-minutes/) describes the workflow as pre-funded and calls it the first phase of the companies' collaboration. TBMC took assets that a client already held on Lynq and converted them into $RLUSD. The conversion and settlement finished in a few minutes.

Lynq and TBMC said they used live production accounts and real institutional counterparties. That distinction is useful but limited. The announcement gives no transaction identifier, chain, transferred amount, fee, exchange rate, or exact elapsed time. Readers therefore have the companies' production claim, but not enough public information to reproduce or independently verify the transfer.

The workflow did not use a credit facility to make the transfer appear faster. TBMC founder and CEO Sam Broner described the design as onchain collateral movement that avoids credit and traditional bank settlement as the bridge. Lynq CEO Jerald David said the proof of concept was small by design and settled a digital dollar between institutions without a credit facility standing in for speed.

The release also says the transfer bypassed traditional banking windows. That is narrower than a claim of continuous availability. It shows that this test did not wait for a bank settlement window, while the announcement does not state operating hours, service levels, or whether the same path is available to all Lynq clients.

## How interest stayed attached to the workflow

Assets continued to accrue interest while Lynq held them during settlement. Lynq attributed the calculation to Tassat's Yield in Transit functionality, which determines accrued interest from the duration of the holding period. The stated result is that interest remains intact through settlement rather than being interrupted while funds wait to move.

For a treasury operator, this changes the cost comparison with a conventional pre-funding process. The operational claim is specific: assets held during the Lynq leg keep accruing interest, and the calculation uses holding duration. The release does not state the interest rate, asset type, calculation interval, or who ultimately pays the accrued amount. Those terms would determine whether the benefit is material for a larger transfer or a longer queue.

Lynq describes itself as a broker-dealer-operated settlement network for institutional digital asset markets. Its [platform page](https://lynq.network/) says it offers institutional clients a segregated account framework and charges no onboarding costs or transaction fees. The same page characterizes the product as a real-time settlement solution that offers interest to institutional clients. These are the standing product terms around the test, not evidence that every future stablecoin conversion will share the same economics.

The legal structure is more specific than the product description. Lynq's site says Digital Asset Settlement Network does business as Lynq but is not itself a registered broker-dealer, investment adviser, or investment manager. The platform is operated by tZERO Securities, an SEC-registered broker-dealer and FINRA and SIPC member. The site says tZERO Digital Asset Securities, a special purpose broker-dealer, provides custody for digital asset securities. It also warns that some digital asset securities may fall outside the Securities Investor Protection Act definition of securities and may not receive SIPA customer protections. Treasury teams therefore need to identify which entity holds each asset and which protections apply before treating the workflow like an ordinary brokerage transfer.

## TBMC's clearinghouse role

TBMC supplied the conversion layer. Its [clearinghouse description](https://bettermoney.com/) says clients can accept one stablecoin and settle into a preferred stablecoin. It also describes swaps as redemption-based, at par, and subject to fixed fees rather than pricing that changes with market liquidity. In TBMC's formulation, one dollar in produces one dollar out, including for custom stablecoins.

That model addresses a practical problem for institutions that receive several stablecoins but have a preferred asset for compliance, security, or yield. TBMC says its clearinghouse can route supported stablecoins across issuers or chains without requiring the recipient to seed market liquidity. In this proof of concept, the destination asset was $RLUSD. The announcement does not identify the client's starting asset, so it does not show which issuer or chain pair TBMC handled.

The design also separates pre-funding from credit. The assets were already held on Lynq before TBMC converted them. This can reduce dependence on an intermediary extending intraday credit, but it also means operators need assets positioned on Lynq before the conversion starts. The public materials do not provide the minimum balance, eligibility rules, custody path, or redemption process for this workflow.

## What comes next

The proof of concept is one step in Lynq's plan to connect stablecoin creation, redemption, settlement, and capital movement. Native stablecoin support on Lynq is targeted for the end of 2026. Until then, the test demonstrates a live path with production accounts, not a generally available native stablecoin feature.

The next useful disclosure would be the production specification behind that launch: supported assets and chains, operating hours, settlement guarantees, fees, custody treatment, and the transaction evidence clients receive. The October 13 announcement leaves those points open, along with the amount and exact timing of the completed test.
