---
layout: blog
title: "Variational raises $110M to expand Omni swaps markets"
url: /variational-series-b-omni-swaps.html
h1title: "Variational raises $110M to expand Omni swaps markets"
pagetitle: "Variational raises $110M to expand Omni swaps markets"
metadescription: "Variational's Bain-led Series B funds more Omni markets and higher position limits. Its docs explain swap carry, collateral segregation and counterparty risk."
category: blog
featured-image: /images/blog/variational-series-b-omni-swaps-ogp.png
intro: "Variational raised $110M to expand Omni's derivatives markets and trading capacity, with wider swaps access and higher open interest caps on its roadmap."
author: sawinyh
tags: ["News", "DEXs"]
date: 2026-11-18T23:23:02+00:00
---

On November 18, 2026, Variational announced a [$110M Series B at a $1.5B valuation](https://www.businesswire.com/news/home/20261116481769/en/Variational-Raises-%24110M-Series-B-at-%241.5B-Valuation-To-Scale-On-Chain-Access-To-Global-Markets), led by Bain Capital Crypto. Dragonfly, HSG, Peak XV and 50T Funds also participated. The derivatives protocol says the capital will fund more markets on Omni and higher open interest caps. Traders are increasingly reaching the existing caps.

The round follows the September launch of swaps, Variational's instrument for bringing traditional financial institutions' liquidity to on-chain traders. Omni already offers leveraged exposure across more than 550 crypto and traditional markets. The release reports more than $475B in trading volume since the platform launched in early 2025, more than $1.3B in open interest and more than 100k accounts. These figures come from Variational; they have not been independently checked on-chain.

Traditional markets now account for more than half of daily volume, according to the announcement. Variational says swaps have processed more than $80B since launch. To support additional swap markets, the company is expanding its network of institutions supplying liquidity. It is seeking counterparties able to quote equities, commodities and foreign exchange around the clock.

## What the funding is meant to expand

The [original swaps launch post](https://www.variational.io/blog/swaps-live) sets out the earlier capacity limits. Variational introduced gold and US100 swap markets with conservative open interest limits of around $10M per market while it tested its liquidity provider's hedging flows. At that time, it planned to raise those limits to more than $50M per market. The funding announcement promises further capacity but gives no revised market-by-market cap schedule.

Swaps give traders exposure to an underlying asset through quotes sourced from traditional finance. The launch documentation describes a carry rate primarily benchmarked to dollar borrowing costs in place of volatile perpetual funding. Omni charges no trading fees, but traders still pay spreads and carry. The company says it designed the instrument to make holding costs more predictable.

Swaps trade alongside Omni's existing traditional-market perpetuals. At launch, Variational specified opening and closing hours for swaps, with each market's schedule available in Omni and its documentation. On-chain settlement is continuous; liquidity is subject to market hours. The November release still describes around-the-clock swaps trading as something the team is working toward.

The release says OLP already sources swap liquidity from traditional financial institutions, including an unnamed tier-1 market maker. Variational plans to add counterparties that can continuously quote United States and global equities, commodities and currency pairs. Its roadmap for the remainder of 2026 also includes a trading API and additional swap markets.

## Quotes, collateral and the sole counterparty

Omni's [product documentation](https://docs.variational.io/omni/about-omni) describes a request-for-quote architecture instead of an order book. Traders use a single cross-margined account across crypto and traditional assets. The platform draws on liquidity already available at centralized exchanges, decentralized exchanges and traditional dealers. It does not assemble a separate order book for every listed market.

The Variational Oracle aggregates market data from multiple venues to supply pricing. The Variational Protocol clears and settles trades on-chain. The Omni Liquidity Provider, or OLP, supplies direct quotes and is the sole market maker and counterparty to user trades. This description of the trading system comes from the operator. The contracts have not been independently inspected for this article.

The [OLP documentation](https://docs.variational.io/omni/the-omni-liquidity-provider-olp) describes a vault, a market-making engine and a risk-management system. The vault holds $USDC capital used for OLP's margin and accumulates market-making profits. Proprietary algorithms quote prices and manage or hedge the resulting positions. When users trade at those quotes, OLP can hedge its directional exposure on external venues.

Spreads pay the operator. The docs say Variational takes 20% of spreads paid to OLP for its protocol treasury. Omni charges no maker or taker fees, while the spread embedded in each quote supplies revenue to the liquidity provider and protocol. The funding release also identifies OLP's spread earnings as the basis for the no-trading-fee model.

Both the trader and OLP must maintain margin in a settlement pool. Either can face liquidation when its margin falls below the required level. Each trader has a segregated pool with OLP, and the trader's funds remain on-chain as collateral for open positions, according to the docs. Each pool is a bilateral collateral arrangement, with the same liquidity provider acting as counterparty to all users.

For external hedging, OLP transfers its own capital to other venues. Traders' collateral stays on the Variational Protocol. If an external exchange loses funds in a hack or other incident, the docs say OLP depositors may lose capital while traders can still withdraw funds held on the protocol. Traders remain exposed to OLP's solvency: if it becomes insolvent, realized or unrealized profit accruing afterward becomes bad debt that cannot be paid to the user.

The OLP docs say the Variational team initially supplied the liquidity provider's seed capital. Before opening a community vault to user deposits, the team plans to prove system stability on mainnet and establish a record of market-neutral yield. The docs explicitly warn that OLP can lose money. They describe planned vault access; the funding release does not announce it as live.

For each additional listing, OLP needs a reliable price feed, a quoting strategy and a hedging mechanism, according to the docs. All can be built and maintained in-house. Quoting a new asset requires those pricing and hedging components as well as capital supplied to the market maker.

## Access and remaining rollout details

Omni remains subject to jurisdictional restrictions after the funding. Variational's [restricted-persons policy](https://docs.variational.io/legal/restricted-persons) excludes United States persons and Canadian persons, among other restricted categories. Users represent on an ongoing basis that they are eligible to use the products. The release also warns that leveraged derivatives carry a high risk of loss.

The November funding release gives no date for completing the transition to continuous swaps trading or launching the trading API. Both remain roadmap items.
