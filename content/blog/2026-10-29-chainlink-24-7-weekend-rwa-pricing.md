---
layout: blog
title: "Chainlink Launches Weekend RWA Pricing With Aave Horizon"
url: /chainlink-24-7-weekend-rwa-pricing.html
h1title: "Chainlink launches weekend RWA pricing with Aave Horizon"
pagetitle: "Chainlink 24/7 Adds Weekend Pricing for RWA Collateral"
metadescription: "Chainlink 24/7 uses perpetual-market quotes when traditional exchanges close. Aave Horizon is adopting the feeds for tokenized equity collateral."
category: blog
featured-image: /images/blog/chainlink-24-7-weekend-rwa-pricing-ogp.png
intro: "Chainlink has launched continuous RWA pricing that combines weekday market data with perpetual-market quotes during weekends and holidays."
author: sawinyh
tags: ["News"]
date: 2026-10-29T15:32:26+00:00
---

On October 29, 2026, Chainlink [launched Chainlink 24/7](https://chain.link/blog/introducing-chainlink-24-7), extending its real-world asset pricing to weekends and holidays. The company says Aave is using the Data Feeds version in Horizon, its institutional lending platform, starting with high-volume U.S. equities used as collateral.

The new reference combines prices from traditional trading sessions with quotes from perpetual futures venues when those markets close. The weekend price is a derivatives-market reference linked to the underlying asset. Chainlink says it is not a live quote from the closed traditional exchange. Lending markets would use this derivatives reference to value eligible collateral while the underlying exchange is closed.

## What replaces the weekend freeze

Chainlink's earlier weekday service covered pre-market, regular, post-market and overnight trading. Its launch announcement identifies the remaining gap as running from 8 p.m. ET Friday to 8 p.m. ET Sunday, plus market holidays. Applications previously had to pause, retain the last available price or construct their own off-hours methodology and switching logic.

During active sessions, the new service draws on existing Chainlink 24/5 data. Once the traditional market closes, it aggregates quotes from multiple perpetual venues, filters stale inputs and limits the influence of outliers. Chainlink says supported assets must meet its requirements for market coverage, liquidity and pricing consistency. The announcement does not name the contributing perpetual venues or publish their weights.

Chainlink calls its method for moving between these inputs session-aware stitching. The company says this builds on the blending engine used for its tokenized equity pricing, maintaining continuity while preserving immediate price discovery at the regular-session opening bell. Developers receive a continuous reference per supported asset instead of assembling the session-selection layer themselves.

The [existing weekday equities guide](https://docs.chain.link/data-streams/rwa-streams/24-5-us-equities-user-guide) shows the integration work this replaces. Instruments have separate regular, extended and overnight streams, and users must switch between them according to the reported market status. The guide also requires custom handling for unknown status and closures. That documentation describes the older session-specific streams, not a requirement to rebuild the new unified reference.

Delivery depends on the application. Data Feeds publish prices onchain for lending contracts to read. Data Streams allow perpetual exchanges and prediction markets to retrieve low-latency reports offchain. The [public Data Streams documentation](https://docs.chain.link/data-streams) describes signed reports available through SDKs, REST and WebSocket interfaces, with onchain verification in the transaction that consumes them.

Chainlink also identifies short-duration prediction markets as a use case. Its announcement proposes time-weighted average pricing as the reference for resolving asset-price outcomes and helping prevent price manipulation.

## What changes for collateral valuation

According to Chainlink, Horizon is using the feeds to price tokenized real-world assets pledged as collateral, beginning with high-volume U.S. equities. The announcement identifies that starting asset class but does not enumerate the tokens, publish Horizon's new feed addresses or specify collateral-factor changes. The scope of adoption across Aave equity markets is unspecified.

Chainlink says the continuously updated valuation is designed for liquidations, allowing lending risk parameters to operate beyond traditional market hours. For positions using the new feeds, collateral valuation can respond to off-hours derivatives trading instead of waiting for the underlying exchange to reopen. The announcement does not provide a new borrowing limit or liquidation threshold for those positions.

Streams also carry market-session information and bid and ask prices during open sessions. Chainlink says applications can use that context to adapt risk settings as conditions change. The session information lets an operator distinguish active exchange pricing from the off-hours component when deciding which risk settings to apply.

The public weekday guide separates market status from freshness. Status determines which session is active, while timestamps describe when data was recorded. Its mid-price timestamp applies only to the mid price, not to bid and ask prices or their volumes. Those fields may have different update times, so a fresh mid-price timestamp cannot establish freshness for the entire report. The guide also says bid and ask volumes represent one order book at a time, not combined liquidity across equity venues. Operators should not treat them as a measure of total market depth.

The same guide warns that extended and overnight weekday streams currently rely on a single data provider, unlike multi-sourced regular-hours prices. It describes cases where a technically fresh report can contain an incorrect mid price produced by an outlier quote. The documented safeguards include spread checks, value bounds and price-deviation checks, alongside staleness monitoring. Those are limitations of the existing weekday inputs, distinct from the launch's multi-venue off-hours methodology.

The weekday guide directs operators to monitor exchange notifications for trading halts, which are not reflected in the market-status field. It also warns that corporate actions can interrupt symbol-specific overnight data without changing that status. Continuous delivery still requires application-level decisions about when a reported price is safe to use for a trade or liquidation.

## The feed methodology remains asset-specific

Chainlink already publishes [extended-hours feed documentation](https://docs.chain.link/data-feeds/24-7-extended-hours-data-feeds) covering precious metals and forex. Each asset class has a separate methodology and risk profile, the documentation warns. The new announcement's perpetual-based description should not be read as a replacement specification for every feed carrying a round-the-clock label.

The documented metals approach uses spot prices during open market hours. During closures, it starts from the last observed spot price and adjusts it with a blended signal from tokenized precious-metals streams. The forex documentation describes crypto-derived exchange rates and warns that they measure a different market from official, interbank or institutional references. Such rates can diverge materially from the prices available through banking channels.

Chainlink's launch post leaves the supported-asset roster, perpetual-venue weights and Horizon feed addresses unspecified. Teams seeking to integrate the new service are directed to contact Chainlink.
