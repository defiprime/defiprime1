---
layout: blog
title: "HyperDex Launches Spot and Perps Aggregator"
url: /hyperdex-launches-spot-and-perps-aggregator.html
h1title: "HyperDex launches spot and perps aggregator"
pagetitle: "HyperDex Launches Spot and Perps Aggregator"
metadescription: "HyperDex has launched a spot and perpetuals aggregator with non-custodial routing across 69 chains, 36 bridges and 39 exchanges."
category: blog
featured-image: /images/blog/hyperdex-launches-spot-and-perps-aggregator-ogp.png
intro: "HyperDex launched a spot and perpetuals aggregator that routes swaps and bridges while users sign transactions from their own addresses."
author: sawinyh
tags: ["News"]
date: 2026-10-13T09:21:00+00:00
---

HyperDex [introduced its spot and perpetuals aggregator](https://x.com/Hyperdex_app/status/2109809384750792820) at 00:52 UTC on October 13, 2026. The announcement did not report launch volume. The release puts spot routing, cross-chain transfers and a newly announced perpetuals aggregator under the HyperDex interface.

The launch announcement is brief about perpetuals. HyperDex names the product but does not identify the perpetual venues, supported contracts, collateral rules or liquidation mechanics in that post. Its published documentation describes the spot side in much more detail.

## What the spot aggregator routes

HyperDex describes itself as a marketplace for real-world assets. Its [overview](https://hyperdex.app/docs) lists stock tokens from Ondo, xStocks, Robinhood, Coinbase and bStocks. It also says the interface prices each swap and bridge across exchanges, bridges and intent solvers. Users sign from their own addresses, while transfers pass through audited routing contracts to the destination address they choose. HyperDex says it never holds user funds.

The team's earlier product description said the aggregator had integrated LI.FI, RIFT, Enso and Ravn. It also named Relay, Across, NEAR Intents and Chainflip among more than 70 venues. The same statement put the asset count above 19,000 tokens and included tokenized stocks, gold, treasuries and credit from Ondo, Backpack, Coinbase, Robinhood and eight other issuers. Those are team claims rather than a fixed inventory. The live route set can change as third-party venues add or remove liquidity.

That inventory broadens what the same routing screen has to compare. A quote may involve a conventional crypto token, a tokenized stock or another real-world asset issued by a separate company. HyperDex does not become the issuer or custodian when it displays the route. The issuer still determines how its token is backed, while the selected venues determine the available price and liquidity.

The interface treats a same-chain trade as a swap and a transfer between two chains as a bridge. A bridge route may swap on the way. HyperDex gives $ETH on Base to $USDC on Arc as one cross-chain example, and $USDC to $EURC on Arc as a same-chain example.

The [supported-chain list](https://hyperdex.app/docs) currently says routing covers 69 mainnets through 36 bridges and 39 exchanges. It includes EVM networks, Bitcoin, Solana, Sui and Zcash. HyperDex says that list updates live, so a new chain can appear without a separate application release. The count therefore describes the live documentation at launch, not a permanent limit.

## How a quoted route works

A user first selects the input token and chain, the output token and chain, and an amount. HyperDex then requests routes from every available venue and sorts them by best price or fastest completion. The documentation says quotes refresh every 20 seconds.

Each proposed route shows the minimum output, network fee, HyperDex fee and estimated completion time before the user signs. Some tokens require a one-time approval. The interface tracks approval, submission and arrival, with a transaction link for each step. HyperDex tells users to keep the browser tab open until the transfer arrives.

This sequence gives the user several checks before execution. The minimum received sets the protected output for the route. The fee fields separate HyperDex's charge from network and venue costs. Transaction links then let the user follow each submitted step rather than relying only on the application status. A token approval remains a separate on-chain permission when the selected asset requires one.

The displayed result is net of the route's stated costs. HyperDex charges a 0.50% fee on ordinary transfers and 0.75% on private swaps. Bridge or exchange fees come from the selected route, while network gas is paid in the source chain's gas token. On Arc, gas is paid in $USDC. The protocol takes its fee from the token being sent.

Those costs matter when comparing the best-price and fastest settings. A route can disappear because the prices and liquidity come from third-party protocols. HyperDex specifically warns that availability may drop outside US market hours. A saved route should not be treated as executable until a fresh quote returns.

## What changes for users

The immediate change is a single quoting surface for assets and routes that were previously exposed through separate issuers, exchanges, bridges and solvers. A user can compare the final output and estimated time without handing custody to HyperDex. The transaction still depends on the contracts and venues inside the selected route.

For same-chain swaps, HyperDex says settlement is atomic. If the price moves beyond the user's slippage limit, the transaction reverts. Cross-chain execution has a different failure mode. If the bridge completes but the destination swap fails, the user receives the bridged asset on the destination chain rather than the originally requested output token. Operators and automated users need to account for that intermediate asset in their monitoring and recovery logic.

The distinction changes what completion means. A reverted same-chain swap leaves the requested trade undone. A partially completed cross-chain route can leave value on the destination chain in a different asset. Users should check the destination address and transaction links before retrying, because the bridge portion may already have settled.

HyperDex says its routing contracts are audited, open source and covered by a bug bounty. The product is labeled beta. Its documentation warns that pages and transaction flows can change as integrations are added, while quotes and liquidity continue to depend on third parties.

The open question is the perpetuals side of the launch. HyperDex has not yet documented which perpetual markets it aggregates, how it compares margin requirements across venues, or what happens when a routed position reaches liquidation. Until those details are published, users can verify the spot route, minimum received and fees before signing, but cannot make the same assessment for perpetuals from the launch materials alone.
