---
layout: blog
title: "Cap Finances Wake With Onchain Collateral Behind Film Credit"
url: /cap-wake-film-credit-guarantees.html
h1title: "Cap Finances Wake With Onchain Collateral Behind Film Credit"
pagetitle: "Cap Finances Wake With Onchain Collateral Behind Film Credit"
metadescription: "Cap financed Wake against anticipated production tax credits, using underwriter collateral to back repayment without tokenizing the film's assets."
category: blog
featured-image: /images/blog/cap-wake-film-credit-guarantees-ogp.png
intro: "Cap has expanded into film financing with an advance for Wake, pairing offchain production tax credits with an onchain collateral guarantee."
author: sawinyh
tags: ["News"]
date: 2026-11-04T18:33:59+00:00
---

On November 4, 2026, Cap [announced financing for Wake](https://x.com/CapApp/status/2118019807715144170), an upcoming feature film starring Cole Sprouse, Riki Lindhome and Chris Parnell. The transaction expands its credit marketplace into film and media through an advance against anticipated production tax credits.

Cap says it has already provided the financing. Its [public borrower page](https://cap.app/overview/borrowers/wake-2026) lists Wake, names Legacy as its underwriter and identifies Coinbase Wrapped Bitcoin as the collateral asset. Depositors can inspect the borrower and its backing asset on that page as the platform adds credit demand from outside crypto-native strategies.

## Tax credits stay offchain

The production receives capital before the expected tax-credit proceeds arrive, according to [Cap's distributed press release](https://markets.businessinsider.com/news/stocks/cap-expands-onchain-credit-marketplace-into-film-and-media-financing-1036715411). Its anticipated credits support the financing arrangement. A separate pool of liquid onchain collateral backs the lender's repayment protection. Cap describes an advance against those credits, not a sale of tokenized film rights or future box-office revenue.

Specialized underwriters assess the offchain credit risk and escrow their own onchain assets to guarantee individual loans, Cap says. Borrowers retain the collateral structures already used in their industries. Underwriters take on the associated offchain risk in exchange for a premium. They commit their own capital alongside their credit assessment; lenders do not have to evaluate the production's tax credits directly.

“Wake's loan at Cap is collateralized with @coinbase [$BTC],” the team [said in its announcement thread](https://x.com/CapApp/status/2118019849242972566). The borrower interface identifies that asset as $cbBTC. Cap's statement and interface are the sources for this collateral arrangement. Neither provides an independently verified contract balance or a reading of the production's legal financing documents.

The company says its marketplace has [16 independent underwriters](https://x.com/CapApp/status/2118019864359322059). Cap plans to expand through their industry expertise and capital, without building an internal credit team for each sector. The announcement describes a film-financing use of the marketplace, but does not identify all those underwriters as participants in Wake's loan.

## How the loan reaches Cap's lenders

Cap's [documentation](https://docs.cap.app/overview/readme.md) describes an Ethereum credit platform where each loan carries escrowed underwriter collateral. Whitelisted borrowers must obtain sufficient collateral delegations before drawing liquidity from reserves. Once that backing is in place, the borrower can access funds through the protocol's contracts. This collateral requirement applies separately from the production's offchain financing arrangement.

Depositors follow the [documented lending flow](https://docs.cap.app/overview/protocol-overview/stcusd-mechanics.md): they deposit approved dollar-pegged assets into the reserve and receive $cUSD. Staking $cUSD produces the yield-bearing $stcUSD. Before borrowers draw reserve assets, those assets can earn returns directly or through integrated lending protocols, including Aave and Morpho. Wake borrows from this credit platform; the announcement introduces no standalone token for film investors.

The protocol's [interest-rate formula](https://docs.cap.app/concepts/lender/interest-rates.md) combines a minimum rate, a utilization component and an underwriting premium. The minimum is the higher of Cap's benchmark and an external market rate. The utilization component adjusts borrowing costs as reserves are used. Each borrower and underwriter negotiates the underwriting premium as a fixed annual rate. These mechanics set rates across the platform. The Wake announcement promises lenders no disclosed fixed return.

Cap's documentation also requires borrowers to offer more than the base yield available on idle assets. New credit demand must compete with the reserve's existing earning opportunities. An underwriter's willingness to support a film loan sits alongside that cost of reserve liquidity when determining the protocol borrowing rate. The production's tax-credit financing alone does not set the rate.

## The collateral can be liquidated

Cap's [lending mechanics](https://docs.cap.app/overview/protocol-overview/stcusd-mechanics.md) use a health-factor test based on collateral and debt to determine when a position can be liquidated. A fall in the underwriter's collateral value or growth in the borrower's debt can breach the threshold. The protocol measures that trigger onchain. It does not need a determination that a film failed commercially or that a tax-credit claim was rejected.

The detailed [liquidation documentation](https://docs.cap.app/concepts/lender/liquidation.md) says a liquidator starts the process and ordinarily gives the borrower a 12-hour grace period to repair the position. It lists a default liquidation threshold of 80% loan-to-value. An emergency threshold of 90% bypasses the grace period. These are the protocol's documented defaults; Wake-specific settings have not been independently checked at a pinned block.

During liquidation, a liquidator repays borrowed assets to reduce the outstanding debt and receives underwriter collateral plus a bonus through the shared-security network. The liquidation window closes when the borrower's health recovers. The process sells the underwriter's capital to restore the lending position. Any recovery involving the production's offchain collateral falls under the separate credit arrangement.

The auction bonus increases linearly after the grace period and reaches a maximum of 10% at expiry. Emergency liquidations offer the maximum bonus immediately. The incentive can be paid only when total delegated collateral exceeds total debt, and the protocol prevents liquidation beyond the available collateral. The documentation sets a target health factor of 1.25 for calculating the maximum liquidatable amount. That recovery target sits above the threshold that triggered intervention.

The liquidation period expires three days after the grace period ends. If the borrower remains unhealthy at expiry, any liquidator can restart the process. Expiry also stops an old liquidation window from remaining available indefinitely after a position recovers. If the position deteriorates later, liquidation requires a new process and its applicable grace period.

Cap's [risk disclosures](https://docs.cap.app/overview/risks.md) acknowledge that volatile delegation assets increase the likelihood of liquidation. They also warn that reserve assets can depeg or be frozen, seized or forfeited. Liquid crypto collateral gives lenders a different asset to draw on for repayment, while leaving them exposed to changes in collateral prices and risks affecting reserve assets.

The same disclosures place holder protections in smart-contract code and warn of possible code vulnerabilities. Redemptions can also be delayed when reserve assets are fully utilized. Cap's financial guarantees depend on the collateral and the protocol's execution. Holders' withdrawal timing depends on available reserves as well, even with those guarantees in place.

Cap's documentation allows offchain guarantor agreements to set recourse provisions, loan terms and strategy constraints. The Wake announcement and linked borrower page do not publish the production's tax-credit jurisdiction, expected payment date or guarantor agreement.
