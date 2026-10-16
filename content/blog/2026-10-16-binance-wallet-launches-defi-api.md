---
layout: blog
title: "Binance Wallet launches DeFi API across 10 EVM chains"
url: /binance-wallet-launches-defi-api.html
h1title: "Binance Wallet opens a DeFi transaction API"
pagetitle: "Binance Wallet launches DeFi API for 10 EVM chains"
metadescription: "Binance Wallet's DeFi API queries positions and builds unsigned deposit, redeem, liquidity and claim transactions across 10 EVM chains."
category: blog
featured-image: /images/blog/binance-wallet-launches-defi-api-ogp.png
intro: "Binance Wallet released a DeFi API on October 16 that queries positions and builds unsigned protocol transactions across 10 EVM chains."
author: sawinyh
tags: ["News", "Infrastructure", "For Builders"]
date: 2026-10-16T11:19:48+00:00
---

Binance Wallet released a DeFi API on October 16, 2026, after marking its documentation as modified on October 15. [The API documentation](https://web3.binance.com/en/dev-docs/products/defi-api/introduction) covers position queries, protocol and investment discovery, and transaction construction across 10 EVM chains. Binance said Solana support is planned but did not give a release date.

The service builds unsigned calldata for deposits, redemptions, liquidity changes, and reward claims. It does not hold a user's private key. A wallet still signs and broadcasts the resulting transaction, leaving execution and key custody outside the API.

## What the API exposes

The data endpoints let an application query DeFi positions for one or more wallet addresses. They also list supported protocols, return protocol details, list investment products, and return details for a selected product. Binance places those routes under `/api/v1/defi/data/*` and uses POST requests for each operation.

Position responses organize data by queried address, protocol, pool, position collection, and individual position. The top level includes the total value across all queried addresses. Lower levels separate each address's value, protocol totals, pool identifiers, collection totals, and token roles such as supply, borrow, reward, and farming reward. That structure lets a wallet show an aggregate view while retaining the components needed for a protocol or pool breakdown.

The transaction endpoints cover deposit, redeem, liquidity addition, liquidity removal, and claims. There is also a calculation route for paired token amounts before adding liquidity. Each build response returns an ordered list. When an ERC-20 approval is required, the approval item comes first and the main protocol action follows.

Applications can set `simulate=true` on the five transaction-build endpoints. The resulting preview can include projected balance changes, estimated gas, and a change in lending health factor before broadcast. Binance's documented flow is build, sign, broadcast, and poll. The API handles the build step, while the connected wallet handles signing.

## Chains and protocol coverage

[The supported-chain list](https://web3.binance.com/en/dev-docs/products/defi-api/supported-chains) names BSC, Ethereum, Base, Arbitrum One, Polygon, Optimism, Avalanche C-Chain, Robinhood, Katana, and ARC. Each chain has a Binance chain identifier, and native assets use the address `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee` in API responses.

Transaction and investment support is narrower than position coverage. The transaction list includes lending and yield protocols such as Venus, Aave, Morpho, Spark, Fluid, Ethena, Lido, Maple, and Rocket Pool. It also includes liquidity protocols such as Uniswap, PancakeSwap, and QuickSwap on specified chains. Available actions differ by protocol and chain. Some integrations expose deposit and redeem, while others also expose claims or liquidity actions.

Position queries cover additional protocols that cannot necessarily be used as transaction entry points. Binance labels those results display-only when they fall outside the transaction and investment list. Their `investmentIds` may be empty, and an application must check an identifier through the investment list or detail endpoint before using it in a transaction-build call. A build can fail even when a position response includes an identifier if the investment endpoint returns no match.

The protocol list endpoint is the authoritative live source for supported protocols and actions. Binance says the published tables describe the release scope, while server-side support can change. Developers therefore need to query the list rather than hard-code the documentation table as a permanent set.

The separation affects interface design. A wallet can show a position because the position endpoint recognizes its protocol, yet still be unable to build a deposit or redeem transaction for it. The application has to check the investment endpoints before presenting an action. It also has to use the target chain identifier because the same protocol identifier can span several chains while exposing different actions on each one. A static allowlist copied from the launch documentation can become wrong as Binance changes server-side coverage.

## Limits and integration risks

The service has independent rate limits by IP address, API key, user, and endpoint. The documentation gives limits of 1200 requests per 60 seconds for an IP address, 1200 requests per 60 seconds for an API key, 6000 requests per 60 seconds for a user, and a default of 5 requests per second for an endpoint. The gateway returns HTTP 429 with business code 42900 and a `Retry-After` header when a limit is exceeded.

Data formatting also requires care. APY arrives as integer basis points and as a preformatted display string. TVL, position values, and token amounts arrive as decimal strings. Timestamps use Unix time in seconds. An application that treats these values as ordinary floating-point numbers could change precision or display a value differently from the source.

Rate handling is part of the integration contract rather than a single global ceiling. IP addresses, API keys, users, and individual endpoints each have their own limit. A client can hit one dimension while remaining below the others. Binance tells clients to use the `Retry-After` value after an HTTP 429 response. Repeating a request immediately would ignore the documented backoff signal and can keep that call path unavailable.

Redeems can introduce a protocol-specific delay. Binance says some supported protocols impose a waiting period before redeemed funds can be claimed. The redeem builder returns `redeemDelayDays` as a minimum and maximum day pair, with an empty pair indicating an instant redemption. A wallet needs to show that value before the user signs rather than assuming every redeem completes immediately.

For users, the API does not make Binance the signer or custodian for these protocol transactions. The connected wallet remains responsible for reviewing, signing, and broadcasting the calldata. For developers, the practical risk sits in treating discovery data as executable support. Position visibility, investment availability, and transaction actions are separate scopes.

Binance's [launch post](https://x.com/BinanceWallet/status/2111006211596501292) says Solana support is coming. The documentation currently lists only the 10 EVM networks and says more chains and protocols will be added in future releases. The open question is when Solana enters the documented release scope and which data and transaction endpoints it will support.
