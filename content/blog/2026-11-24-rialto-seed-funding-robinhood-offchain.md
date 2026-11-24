---
layout: blog
title: "Rialto announces $5M seed round co-led by Robinhood and Offchain"
url: /rialto-seed-funding-robinhood-offchain.html
h1title: "Rialto announces $5M seed round co-led by Robinhood and Offchain"
pagetitle: "Rialto announces $5M seed round co-led by Robinhood and Offchain"
metadescription: "Rialto disclosed a $5M seed round for its onchain trading app and Swap API, with Robinhood Chain its priority and API access also live on Arbitrum."
category: blog
featured-image: /images/blog/rialto-seed-funding-robinhood-offchain-ogp.png
intro: "Rialto disclosed a $5M seed round backing an operating onchain spot exchange and Swap API, with Robinhood Chain remaining its priority."
author: sawinyh
tags: ["News"]
date: 2026-11-24T17:26:17+00:00
---

On November 24, 2026, Rialto [announced a $5M seed round](https://x.com/rialto_xyz/status/2125276960729260329) co-led by Robinhood and Offchain for its onchain trading business. The company runs a spot trading app and a Swap API that gives wallets and other applications access to its routing and liquidity.

Rialto co-founder Can [told The Block](https://www.theblock.co/news/deals/2026-11-24-robinhood-onchain-trading-platform-rialto-funding-446030) that fundraising began in October 2025 and the round closed in early 2026. The co-leads were its only investors. He described it as Rialto's first funding round, structured as equity with token warrants. Rialto did not disclose the valuation.

In a [follow-up statement](https://x.com/rialto_xyz/status/2125276962285367653), Rialto said the partnership began over a year ago. It involved working with Robinhood Crypto and Offchain on how crypto and Stock Tokens trade on Robinhood Chain. Can told The Block that the app and Swap API launched publicly in July 2026 and have processed more than $600 million in spot trading volume. The volume figure comes from the co-founder and has not been independently reconstructed onchain.

## The exchange and the routing business

Rialto's [documentation](https://docs.rialto.xyz/) describes an onchain spot exchange covering crypto, equities, ETFs and commodities. Users trade from their own wallets, and trades settle onchain. The documentation says Rialto never takes custody of their funds. Stock-token and crypto trades use the same routing system, which compares supported liquidity sources for each order.

Those sources include propAMMs, whose market makers use their own pricing logic and inventory to quote trades instead of relying on a passive constant-product pool. Can told The Block: “Our PropAMM-driven approach puts market-making and inventory management directly onchain, so professional market makers can quote competitive prices.”

The documentation says propAMMs compete with conventional DEX pools on each quote. Rialto samples candidate sources against current chain state for the requested trade size, ranks routes by output after gas costs and settles the selected route. Its [Swap API explanation](https://blog.rialto.xyz/blog/rialto-swap-api) says a single order can use more than one source when doing so improves the result. Rialto compares only the sources it supports.

Can said a recent upgrade reduced average quote response times from 250 milliseconds to 20 milliseconds. He described the API as competing with aggregators on liquidity and speed on Robinhood Chain, while the app competes with centralized platforms on performance and fees. The documents reviewed contain no independent latency benchmark for those performance claims.

The app earns a 5-basis-point trading fee, Can said. He did not disclose revenue. Robinhood Chain remains the priority, though he said the Swap API is also live on Arbitrum. His stated goal is to make Rialto a trading destination on Robinhood Chain and a core aggregator for Arbitrum.

## What integrators receive and still have to handle

Rialto's API returns the route and executable transaction. Its product explanation names solvers and liquidators among potential users, while leaving order fulfilment and liquidation logic to the integrating system. An application can request the buy or sell its workflow needs without implementing Rialto's liquidity routing itself. Market makers supply liquidity by exposing onchain quoting and settlement functions.

The [quote endpoint](https://docs.rialto.xyz/developers/requesting-a-quote) requires an API key with quote access. For an exact-input swap, its response includes expected output, route legs, platform fees, an estimated network fee and an executable transaction. Requests identify assets by canonical token addresses. The endpoint rejects token symbols because they are not unique, so a wallet integration must use the address returned by token discovery.

Integrators handle balance and allowance checks, user authorization and transaction confirmation. Rialto's product guide tells developers to keep API keys on the backend and validate requests before forwarding them. The application must take the returned transaction through its own execution flow and present the trade clearly to the user.

The [execution documentation](https://docs.rialto.xyz/developers/executing-a-quote) distinguishes Permit2 settlement from allowance settlement. The returned settlement field determines how the application must handle the transaction, even if the requester supplied a preference. The docs warn developers against editing the route, fee fields, witness or transaction data beyond inserting the required Permit2 signature. Changing the route or witness can cause the signed quote to fail.

With Permit2, the user signs a transfer bound to the particular swap. The signed conditions include the recipient, buy token, minimum output, deadline, quote identifier and hash of the route actions. The user must still complete an outstanding token approval when the quote flags it. The documentation describes the signature as authorizing a single exact transfer.

Rialto also offers a [gasless relay flow](https://docs.rialto.xyz/developers/gasless-relayer). The user signs the Permit2 witness, then Rialto submits the transaction and its relayer pays network gas. In the direct flow, the user's wallet submits the returned transaction. Applications can use either path and must handle authorization according to the settlement mode they receive.

Gasless execution has narrower eligibility than direct submission. Rialto's relay documentation limits it to ERC20 sells; native $ETH sales require the taker's own transaction. A request must explicitly opt into Rialto's relay. Choosing Permit2 alone does not authorize the service to broadcast. The permit owner must also match the taker, and any outstanding Permit2 allowance remains a prerequisite.

Integrators must select the chain explicitly as well. According to the quote documentation, Rialto serves a request without a chain identifier as Robinhood Chain. The same default applies even though the API supports Arbitrum, so an integration must specify the chain when requesting a quote.

Changes in liquidity can affect a quote before execution. Rialto says it validates routes against live chain state before quoting them. Integrators can also simulate the returned transaction themselves to check that the route still fills and meets the minimum output. A failed simulation calls for a fresh quote, as does a delay before execution.

Can did not answer The Block's question about a future token or another financing, despite the round's inclusion of token warrants. On network expansion, he said: “We have no other chains to announce.”
