---
layout: blog
title: "NEAR Intents Adds Ondo Portfolios to 1Click API"
url: /near-intents-ondo-portfolios.html
h1title: "NEAR Intents Adds Ondo Portfolios to 1Click API"
pagetitle: "NEAR Intents Adds Ondo Portfolios to 1Click API"
metadescription: "Ondo Intelligent Portfolios reach the NEAR Intents API, with issuer eligibility, dealing windows and portfolio fees still applying."
category: blog
featured-image: /images/blog/near-intents-ondo-portfolios-ogp.png
intro: "NEAR Intents has added Ondo Intelligent Portfolios to its API, bringing tokenized investment baskets to cross-chain integrations subject to issuer restrictions."
author: sawinyh
tags: ["News"]
date: 2026-11-06T08:28:56+00:00
---

On November 5, 2026, NEAR Intents [made Ondo Intelligent Portfolios available through its 1Click API](https://x.com/near_intents/status/2118393138515710096). Product developers can integrate tokenized investment baskets into the same routing service used for cross-chain swaps. Access remains subject to jurisdiction and investor eligibility.

The announcement names $BLKHIon, Ondo High Income Powered by BlackRock; $BLKDIGon, Ondo Diversified Growth Powered by BlackRock; and $BLKGRWon, Ondo High Growth Powered by BlackRock. Each is a single token representing a portfolio strategy BlackRock developed for Ondo. NEAR Intents says the integration sits alongside Confidential Execution and cross-chain execution across more than 100 assets and tokenized stocks on more than 35 chains.

A [follow-up in the announcement thread](https://x.com/near_intents/status/2118393141850210365) adds portfolios designed by Ondo: $MAG7Xon, Magnificent 7 & Crypto; $BRAINon, AI Leaders Portfolio; $YLD5on, 5% Targeted Income; and $YLD8on, 8% Targeted Income. Those percentages are part of the product names. They are not guaranteed returns.

## What the portfolio token represents

Ondo describes the products as curated baskets of tokenized stocks and ETFs built on its Ondo Stocks platform. Its [product overview](https://docs.ondo.finance/intelligent-portfolios/overview.md) says a weighted basket of those instruments, together with any cash in transit, fully backs each token. Investors outside the United States can hold a single token instead of buying and maintaining the individual positions themselves.

Ondo Global Markets (BVI) Limited issues the tokens. The [legal documentation](https://docs.ondo.finance/intelligent-portfolios/legal-regulatory.md) describes them as structured notes issued by a bankruptcy-remote special purpose vehicle organized in the British Virgin Islands. Holders receive economic exposure to the basket, not direct ownership of the underlying stocks or ETFs. The tokens confer no shareholder voting rights, statutory information rights or other shareholder rights from the securities issuers.

BlackRock supplies portfolio strategies for the named BlackRock-powered products. Ondo implements the allocations onchain, executes basket trades, rebalances holdings and operates minting and redemption. The [model-provider documentation](https://docs.ondo.finance/intelligent-portfolios/model-providers.md) limits the model provider's role: it does not issue, sponsor, manage or administer the tokens, custody their backing assets, or have any relationship with or obligations to tokenholders.

Portfolio returns include price movements and reinvested income from the constituents. Dividends go back into portfolio assets after applicable withholding taxes, and the portfolio token price reflects that reinvestment. Holders receive that income through the value of their tokens rather than direct dividend payments from each company in the basket.

## Rebalancing, dealing hours and costs

The model provider selects assets and base weights. Actual portfolio weights drift as constituent prices move. Ondo generally rebalances portfolios quarterly, though the model provider sets the approach and frequency for each portfolio. Each product page shows its rebalance frequency and most recent rebalance date.

Holders need not submit a transaction for a rebalance. Ondo adjusts the basket behind the token, leaving the token balance unchanged. Its [rebalancing documentation](https://docs.ondo.finance/intelligent-portfolios/rebalancing-reconstitution.md) distinguishes this from reconstitution, which adds or removes assets. Dynamic portfolios can be reconstituted whenever the model provider updates its model, without a fixed schedule. Portfolios with a fixed asset set generally retain that set, apart from cases such as a terminal corporate action.

Direct minting and redemption generally run from 9:30 a.m. to 3:45 p.m. Eastern Time. The issuer closes that window 15 minutes before the regular 4:00 p.m. United States market close. If any constituent is closed for trading, minting and redemption pause until the full basket is open. Corporate actions and platform risk limits can also interrupt availability. Secondary-market trading can continue around the clock, subject to the applicable restrictions.

When direct minting or redemption is available, Ondo says the investor receives tokens or stablecoins in a single atomic transaction. The portfolio tokens are currently available on Ethereum, $BNB Chain and Solana. These are the deployment networks listed in the issuer's documentation. The wider chain count in the NEAR Intents announcement covers its cross-chain execution service.

Each portfolio charges an annual service fee that accrues daily in its value. The [fee documentation](https://docs.ondo.finance/intelligent-portfolios/fees-taxes.md) says holders receive no separate bill and keep the same token balance. Rates vary by portfolio and appear on the relevant product page. Minting and redemption also incur constituent-level fees. Quoted purchase or sale prices can differ from the platform's underlying execution prices, and the platform retains those differences and fees. Investors pay their own gas costs.

Withholding taxes apply to income from the constituent securities before reinvestment, so a portfolio's effective withholding rate depends on its asset mix. Ondo shows dividend yields before and after estimated withholding on product pages. Investors who acquire tokens on a secondary market may also pay fees charged by other parties.

## Access through the API still has conditions

The [1Click documentation](https://docs.near-intents.org/integration/distribution-channels/1click-api/about-1click-api.md) describes a routing and settlement API that requests market-maker quotes, constructs swaps and tracks execution. Assets move to a quote-specific deposit address and settle onchain. The operator says 1Click does not take custody of them. Developers can now use that API to offer portfolio exposure, subject to the issuer's dealing rules.

Ondo's [eligibility documentation](https://docs.ondo.finance/intelligent-portfolios/eligibility.md) says buying a token on a secondary market does not automatically qualify its holder to mint or redeem directly with the issuer. Direct access requires Ondo Stocks know-your-customer onboarding and satisfaction of the applicable eligibility requirements. A wallet can receive a portfolio token even when its owner is ineligible for direct redemption.

Defiprime previously reported on [a NEAR Intents contract exploit and recovery](/near-intents-recovers-3-8m-after-contract-exploit.html), a separate event from this portfolio integration.

Ondo says its documentation is informational. Each token is issued under a prospectus and additional offering documents available to qualified purchasers on its asset page.

The NEAR Intents launch announcement does not specify a jurisdiction-by-jurisdiction access list or portfolio-specific service-fee rates.
