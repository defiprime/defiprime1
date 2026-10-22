---
layout: blog
title: "Dune launches live trading feeds with filtered market coverage"
url: /dune-market-data-feeds.html
h1title: "Dune launches live trading feeds with filtered market coverage"
pagetitle: "Dune launches live onchain market data feeds"
metadescription: "Dune's live spot and perpetual feeds include block-pinned prices, reorg corrections and a filtered catalog for trading and tokenized-asset monitoring."
category: blog
featured-image: /images/blog/dune-market-data-feeds-ogp.png
intro: "Dune launched live spot and perpetual trading feeds with explicit corrections and a restricted instrument catalog for pricing and execution review."
author: sawinyh
tags: ["News"]
date: 2026-10-22T12:28:10+00:00
---

On October 22, 2026, Dune [launched Market Data Feeds](https://dune.com/blog/dune-market-data-feeds-are-live), streaming spot and perpetual trades for desks pricing positions, reviewing execution and monitoring tokenized assets. Its product page lists coverage across 200+ venues on 12 chains. The feed uses a filtered instrument catalog, with admission requirements for liquidity, pricing integrity and venue registration.

Dune says trades arrive about a second after the block containing them. Each record identifies the instrument, venue and taker's side, plus the executed price in quote per base. Its dollar valuation uses an oracle price pinned to that block. If a reliable mark is unavailable, the record reports the trade as unpriced and supplies a reason.

The [product page](https://dune.com/feeds) lists spot-feed latency at 1.34s, p95. Dune gives a more specific performance claim here than in the launch announcement, which describes trades arriving about a second after the block.

## A catalog built for marking positions

Pools must clear Dune's admission thresholds before their trades enter the feed, excluding some onchain activity. The launch post cites pairs without usable oracle prices and short-lived pools as examples of activity that can distort aggregates used to value positions. The service selects a market universe intended to provide usable marks for positions.

For analysts screening launches in their first hours, Dune points instead to its DEX datasets. Customers seeking an instrument outside the feed catalog can request a review of the universe. Dune says it publishes its methodology. The announcement leaves the numerical liquidity thresholds and full admission test unspecified.

The records also let customers check the underlying trade. Spot messages identify the venue and pool and link to the transaction that settled the trade. A consumer checking a particular price can trace the print back to that transaction and check the normalized record supplied by the vendor.

Dune also assigns stable identifiers and classifications to assets, venues and markets. Those identifiers distinguish the instrument from its addresses on individual chains. Within each feed, venues use the same data model; Dune says adding another venue does not require the customer to change its integration. Reference data comes from its registry.

The product page lists several asset classes within spot coverage: native crypto tokens, stablecoins, liquid staking tokens and yield-bearing tokens, alongside tokenized equities, ETFs, treasuries, funds, commodities and private credit. Perpetual coverage includes equities and ETFs, commodities, foreign exchange, pre-IPO names and crypto tokens. These are the categories Dune advertises, subject to the catalog's admission rules.

Dune describes using the feed to monitor stablecoin selling by venue and trade size while it happens. For tokenized-fund issuers, it proposes secondary-market volume alerts and comparisons of trading prices with net asset value. These monitoring uses cover activity on venues outside the issuer's control, separate from a desk's review of its own fills.

## Corrections arrive as messages

The feed publishes when a block arrives rather than waiting for it to settle. If a chain reorganizes, Dune resends the affected block and delivers corrections as messages. The launch announcement contrasts this with silently changing figures that a trading team has already recorded or filed.

Execution review is one of the uses Dune describes. A desk comparing a fill against the wider market needs trades in the same pair, on other venues, at the time of execution. The Spot Feed supplies that comparison in a common format as trades happen. Dune says the same records can reprice open positions between scheduled marks.

For market makers quoting on centralized venues, the onchain prints provide another price signal. Dune identifies cross-venue spreads and concentration of activity on particular venues as measurements customers can make from the resolved trades. Dune presents these measurements as applications for customers using the feed.

Tokenized assets add an out-of-hours use case. The launch post describes desks following spot and perpetual markets through the weekend while a listed position's conventional market is closed. That monitoring includes the gap into Monday's open. The product supplies the trade records desks can use to make that comparison.

## Perpetual and Solana coverage

Dune's [product changelog](https://docs.dune.com/docs/changelog) describes Hyperliquid perpetual coverage on HyperCore, including first-party markets and HIP-3 builder-deployed markets. Those trades carry dollar notionals, side, size and effect, together with taker and maker information. Instrument codes and venue identifiers accompany the feed's other enrichments.

Counterparty fields differ by market. Dune says each spot trade identifies the taker and the pool it traded against, while each Hyperliquid fill carries both accounts. The product page presents these fields as inputs for counterparty and flow analysis, alongside the prices and sizes used for market monitoring.

For Solana, the changelog describes decoding across 41 program IDs. Coverage spans automated market makers, request-for-quote fills, central limit order books and proprietary automated market makers. It also names Jupiter, DFlow, OKX and Titan among the supported routers and aggregators. Trades receive token metadata from multiple sources, dollar quotes and reference identifiers.

## Live delivery and historical access

Customers receive the live feeds over WebSocket and reference data through a REST API. Historical records are available through an API or through datashare in Snowflake, BigQuery, Databricks and S3. The announcement directs prospective customers to Dune's data-solutions team to arrange access. It leaves the feed subscription price unspecified.

Historical Spot Trades uses the same code, universe, pricing and identifiers as the live Spot Feed, according to Dune. The standard trial contains six months of history across EVM chains and Solana, extended nightly. Separately, the product page advertises eight years of history available outside that trial package.

History for the chain powered by $BNB is still listed as forthcoming in the launch announcement's trial description. Dune has not given a delivery date there.
