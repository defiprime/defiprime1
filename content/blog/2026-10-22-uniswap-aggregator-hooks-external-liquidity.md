---
layout: blog
title: "Uniswap launches Aggregator Hooks for external liquidity"
url: /uniswap-aggregator-hooks-external-liquidity.html
h1title: "Uniswap launches Aggregator Hooks for external liquidity"
pagetitle: "Uniswap Aggregator Hooks go live across three chains"
metadescription: "Uniswap adds external liquidity routing on Ethereum, Base and Robinhood Chain through v4 hooks, with automatic app access and protocol fees."
category: blog
featured-image: /images/blog/uniswap-aggregator-hooks-external-liquidity-ogp.png
intro: "Uniswap has enabled external liquidity routing through v4 hooks in its web app and API on Ethereum, Base and Robinhood Chain."
author: sawinyh
tags: ["News"]
date: 2026-10-22T14:35:25+00:00
---

On October 22, 2026, Uniswap [launched Aggregator Hooks](https://blog.uniswap.org/aggregator-hooks-are-now-live) in its web app and API on Ethereum mainnet, Base and Robinhood Chain. The hooks expose external liquidity as Uniswap v4 pools, letting the router reach outside venues through the same pool interface it uses for Uniswap liquidity.

Uniswap says seven sources are available at launch, covering more than 90% of DEX activity on those chains. The announcement does not name the seven sources or give a measurement period for that coverage claim. Uniswap says it will add more chains and sources, but gives no schedule for either.

## External liquidity enters the route

The web app includes external sources automatically, without requiring users to select an outside venue. According to the announcement, the router pulls fresh quotes from connected sources every block and builds a route across Uniswap pools and external liquidity. The whole swap settles in a single transaction. This integration requires no new approvals.

Swaps through the wrapped sources pay protocol fees that contribute to $UNI burn, Uniswap says. Liquidity supplied elsewhere can therefore generate fees for the protocol when a swap reaches it through these hooks. The release gives no fee rate, expected fee revenue or projected burn amount with which to quantify that expansion at launch.

The [public implementation](https://github.com/Uniswap/v4-hooks-public/blob/main/src/aggregator-hooks/BaseAggregatorHook.sol) shows how the base hook connects to an external pool. It rejects liquidity additions with `LiquidityNotAllowed`, delegates swaps to the external source and settles the resulting amounts through the v4 PoolManager. In this implementation, the wrapper connects execution to existing liquidity; it accepts no new deposits. Liquidity providers evaluating these pools need to inspect the underlying venue where the swap executes.

The same base contract adjusts quotes for protocol fees. For an exact-input swap, it subtracts the calculated fee from the quoted output. For an exact-output swap, it adds the fee to the required input. It returns the unadjusted amount if the protocol fee is unset, or if the fee destination remains unset after polling. These conditions come from the source code. The deployed fee configuration on each launch chain has not been verified here.

## The adapters preserve external pool behavior

Uniswap's [Aggregator Hooks repository](https://github.com/Uniswap/v4-hooks-public/tree/main/src/aggregator-hooks) documents how adapters connect to different venues. Curve uses one hook per underlying pool. A Curve pool containing eight tokens can appear as 28 v4 pools, all sharing one hook address. Routers can check for repeated hook addresses to recognize when separate trading pairs draw on the same reserves.

The repository explains why that check affects routing: a Curve swap changes other directions involving a touched token. The shared hook address lets the router identify that dependency across the separate v4 pool representations. The documented Curve implementations cover both classic StableSwap and StableSwap-NG pools.

Fluid also uses one hook per pool. Its documented implementations include pools with collateral and debt reserves, a lightweight DEX implementation and concentrated liquidity. The repository still labels the concentrated-liquidity implementation's mainnet launch as pending. The implementation inventory describes the adapters in the repository; it has not been verified as the list of sources enabled for this release.

The v2-compatible adapter uses a singleton. One deployment serves multiple v4 pools, with an immutable factory resolving each external pair. Routing depends only on the currency pair. The fee and tick-spacing fields in the v4 pool key do not select the external pair, and the adapter gets its quotes from onchain reserves.

The v3-compatible and Slipstream adapters also use singletons. Their pool lookups differ: the v3 adapter resolves an external pool through its factory, tokens and fee tier, while Slipstream uses tick spacing in place of the fee tier. Both use a chain-deployed compatible Quoter for documented quotes. Each adapter retains the external venue's rules for selecting a pool.

A separate adapter connects directly to MakerDAO's LitePSM for fixed-fee conversion between a gem token and $USDS. It resolves the gem token at construction instead of hardcoding $USDC. On each call, it reads the conversion fees, which governance can change. The adapter permits only one canonical v4 pool per gem/$USDS pair and addresses the PSM directly, without a factory lookup. The repository documents this design but does not confirm LitePSM as an announced launch source.

The repository also describes an address-prefix identification system for routing programs to recognize protocols and repeated pool interactions. It warns that a random hook address can produce a false positive. Routers can use the prefix as a hint, but it cannot prove which implementation controls an address.

## API settings still determine route eligibility

Uniswap's [API routing guide](https://developers.uniswap.org/docs/trading/swapping-api/amm-vs-uniswapx-routing) separates AMM routing from UniswapX intent execution. AMM routes use onchain pools and can split a swap across paths or take multiple hops. UniswapX relies on competing solvers that can use their own inventory and routing strategies. The solver submits the order fill.

API integrations using `BEST_PRICE` search for the most efficient route under the request's inputs. The `FASTEST` setting prioritizes quote response speed and excludes UniswapX; it concerns quote delivery, not settlement complexity. Under `BEST_PRICE`, leaving `protocols` unset lets the API consider both AMM and UniswapX paths. Restricting the field to v2, v3 or v4 limits selection to AMM routes.

Solver availability can further limit those choices. When UniswapX is unavailable, the API can fall back to AMM routing if the request permits it. Chain-specific size thresholds and solver participation can prevent an intent quote. Uniswap also warns that API quotes can differ from the web app because request fields differ. Changes in market conditions can make a fresh best-price search differ from an earlier quote.

The repository's UniswapX aggregator implementation fills a supplied signed order. It has no persistent pool to consult. Original Dutch orders require a full fill, and ordinary routing-quote calls are unsupported because the order arrives with the swap. This implementation opts out of protocol-fee classification, unlike the fee-paying external routes described in the launch announcement. The announcement does not identify it as a launch source, and the repository alone cannot establish that it is enabled.

That order-driven implementation uses a separate base, which forwards per-swap `hookData` directly from calldata into execution. Most documented adapters ignore this data because their external pool is fixed at initialization. The order-driven adapter instead requires the signed order with each swap.

Uniswap has not named the deployed hook contract addresses. Without a deployment list, the source code cannot establish which implementations and fee settings are active on each launch chain.
