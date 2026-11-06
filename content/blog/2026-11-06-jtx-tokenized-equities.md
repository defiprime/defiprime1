---
layout: blog
title: "JTX launches tokenized equities with Backpack and Ondo quotes"
url: /jtx-tokenized-equities.html
h1title: "JTX launches tokenized equities with Backpack and Ondo quotes"
pagetitle: "JTX launches tokenized equities with Backpack and Ondo quotes"
metadescription: "JTX adds tokenized equities with direct issuer quotes from Backpack and Ondo, whose redemption rights, trading windows and eligibility rules differ."
category: blog
featured-image: /images/blog/jtx-tokenized-equities-ogp.png
intro: "JTX has opened trading in tokenized United States and international equities from Backpack and Ondo through direct issuer quotes."
author: sawinyh
tags: ["News"]
date: 2026-11-06T08:28:56+00:00
---

On November 5, 2026, JTX [announced live trading in tokenized United States and international equities](https://x.com/jtx_trade/status/2118387870155346291) from Backpack and Ondo. The launch adds direct issuer quotes through a request-for-quote flow, alongside live pricing and equities research data.

The [Equities application](https://app.jtx.com/equities) is publicly accessible. It displays a sector market map, gainers and losers, earnings reactions and an earnings calendar. An [earlier JTX explainer](https://jtx.com/learn/can-you-trade-stocks-on-solana) said that, as of September 25, 2026, it had neither a tokenized-equities product nor an Equities tab. That explainer still carries the earlier description.

## Issuer quotes alongside stock research

The [Apple detail page](https://app.jtx.com/equities/AAPL) combines a chart with options sentiment, analyst consensus, short-interest information, earnings information and Buy and Sell controls. JTX attributes its market data to Intrinio, including Zacks consensus and ratings, FINRA short interest and SEC filings. It credits Databento for the chart. These providers supply the application's research data; Backpack and Ondo supply the tokenized instruments.

Users have a choice of wallet arrangements. The application says it can create a self-custodial JTX wallet that users fund from a Solana wallet. Users can also connect Phantom, Backpack or another Solana extension, approve each trade in that wallet and keep funds there. The interface identifies Jito as the infrastructure behind its trading experience.

Ondo's [pricing documentation](https://docs.ondo.finance/ondo-stocks/token-and-quote-pricing) separates the displayed price from the price available for execution. Its main price is indicative. An executable quote depends on the particular order, taking account of order size, available inventory and market conditions. The quote is the price at which Ondo offers to buy or sell the specified tokens during its validity period. It can differ from the indicative display.

Trading hours also depend on the issuer. Ondo's [overview](https://docs.ondo.finance/ondo-stocks/overview) describes general availability as 24/5, subject to interruptions between sessions, corporate actions and platform risk limits. Selected assets also have off-hours sessions on weekends and United States market holidays. The JTX announcement does not enumerate which instruments have those extended sessions.

## Backpack's route back to securities

Backpack's [product documentation](https://support.backpack.exchange/backpack-securities/tokenized-securities) connects eligible brokerage securities to tokens issued on Solana. Investors can convert securities into tokens and redeem supported tokens back into the corresponding security entitlement through Backpack Securities. Its comparison table describes the tokenized form as a claim on a special-purpose vehicle holding the underlying assets. The traditional account form is a security entitlement under New York law.

The two forms handle distributions differently. Brokerage holdings receive cash dividends through traditional securities infrastructure. For tokenized holdings, Backpack says dividends are automatically reinvested into additional tokenized shares. Applicable corporate actions produce proportional balance adjustments intended to preserve economic equivalence with the underlying security. Withdrawing securities into a wallet changes how the holder receives distributions.

Conversion requires a separate account relationship. Backpack's [conversion instructions](https://support.backpack.exchange/backpack-securities/tokenized-securities/conversion-flow) require a Backpack Exchange account with completed identity verification and a Solana wallet. Withdrawing eligible securities tokenizes them and sends them onto Solana. Depositing a supported token from a wallet converts it back into traditional securities holdings. These procedures describe conversion through Backpack; they do not establish that JTX provides brokerage accounts.

Backpack quotes an estimated withdrawal platform fee of approximately $0.50, paid in the tokenized security being withdrawn, with no additional withdrawal fees. It charges no deposit fee, although the wallet may incur a Solana network fee. Its instructions warn users to verify the token contract address against the deposit page. Tokens sent under a different address may not be recoverable.

## Ondo exposure and access restrictions

Ondo's overview says its tokens provide economic exposure to underlying assets, with redemption for cash or stablecoins at their then-value. Holders receive neither direct title to the underlying securities nor shareholder voting rights, statutory information rights or other shareholder rights from the companies whose securities the tokens reference.

The tokens track total return, including reinvested dividends net of applicable withholding taxes. On Solana, supported wallets and explorers use a display multiplier to reflect changes in shares represented by each token. The displayed balance adjusts alongside the price per displayed unit. Ondo says this presentation changes neither the on-chain token balance nor the holder's economic exposure. Unsupported wallets can instead show the change through the token price.

Ondo's [eligibility page](https://docs.ondo.finance/ondo-stocks/eligibility) prohibits United States persons, people placing buy orders from within the United States, and people acting for United States persons from subscribing for, acquiring or redeeming its stocks. Those jurisdictional restrictions apply to the instrument, including when users access it outside Ondo's own interface.

Buying or selling directly through Ondo requires its know-your-customer onboarding process. The overview says onboarding currently accepts institutional participants, with individual and retail onboarding still forthcoming. JTX announced access through its own trading interface, but its announcement describes no change to Ondo's direct-platform onboarding policy.

Ondo lists no mint or burn fees. It says the quoted purchase or sale price is the amount paid or received, though that quote may differ from its own execution price for the underlying security. The overview also describes minting and burning as instant: tokens or stablecoins arrive in a single atomic transaction. Fractional token purchases are supported. These terms cover Ondo's platform; JTX's launch statement does not specify its own equities fee schedule.

Ondo says its investor protections include a bankruptcy-remote special-purpose vehicle, an independent director, full asset backing with overcollateralization and a first-priority security interest held by a third-party security agent. It also lists daily attestations of assets held at regulated United States entities, monthly reconciliations and annual audits. These are the issuer's stated protections. This report did not independently verify its reserves.

JTX's launch statement does not provide an equities-specific fee schedule, a complete jurisdictional eligibility matrix or the token contract addresses for its supported instruments.
