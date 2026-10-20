---
layout: blog
title: "Silhouette Opens HyperCore Perps RFQs With a $100k Quote Cap"
url: /silhouette-launches-hypercore-perps-rfq.html
h1title: "Silhouette opens HyperCore perps RFQs with a $100k quote cap"
pagetitle: "Silhouette Launches HyperCore Perps RFQs"
metadescription: "Silhouette launches BTC and HYPE perpetuals RFQs on HyperCore with a $100k quote cap, a 1.4 bps builder fee and positions held on Hyperliquid."
category: blog
featured-image: /images/blog/silhouette-launches-hypercore-perps-rfq-ogp.png
intro: "Silhouette has opened perpetuals RFQs on HyperCore, with accepted quotes executing on Hyperliquid and margin staying in each trader’s account."
author: sawinyh
tags: ["News"]
date: 2026-10-20T03:26:13+00:00
---

Silhouette opened its HyperCore perpetuals RFQ service on October 19, 2026, with $BTC and $HYPE markets and an initial cap of $100k per quote. The [launch announcement](https://x.com/silhouette_ex/status/2112178556994244815) says accepted trades print on Hyperliquid's order book. Margin and positions stay in the trader's own Hyperliquid account.

The service is public, with no waitlist or invitation requirement. In its [longer announcement](https://x.com/silhouette_ex/status/2112178263854354446), Silhouette says working a large order in slices exposes the trader's intent before execution is complete. Its RFQ asks competing makers to quote the full size before the trader chooses a price. The trade then uses Hyperliquid's existing book and margin system.

## A signed quote still goes through the book

The [perpetuals documentation](https://docs.silhouette.exchange/rfq/hypercore/perpetuals) describes a request in which the taker selects a market, side, size and price limit. Makers respond for the requested size. To accept a quote, the taker must sign an order at that price and size; a quote cannot win automatically. If nobody quotes, or the taker accepts none before the window closes, there is no trade.

Silhouette first places the winning maker's order on the book. It sends the taker's order only if the maker's order rests there. If the market has moved through the maker's price and the order is rejected, the process stops before Silhouette sends the taker's order. A stale quote can also fail. A maker that reprices requires a fresh acceptance, and cancellation ends once Silhouette starts placing the orders.

Silhouette sends the taker's order once, as signed. It cannot fill above the accepted size or execute at a worse price before fees. The taker's order never rests on the book. If better-priced liquidity sits ahead of the maker, the taker keeps the price improvement.

Full-size quotes do not guarantee full-size fills. Another trader can take the maker's order before the taker's order arrives. With no remaining liquidity at the agreed price or better, the request fails without a fill. If only part of the requested size is available, that part can execute and the request still displays as settled. Traders need to check the filled quantity to see how much exposure they added.

## Fees sit outside the signed price

Silhouette's [fee schedule](https://docs.silhouette.exchange/fees) lists a 1.4 bps builder fee for HyperCore perpetuals. Hyperliquid charges it to the taker's account on the fill. The maker's order carries no Silhouette builder fee. Hyperliquid's own taker fee applies separately at the trader's fee tier, and funding continues to accrue on the position.

The published example uses a fill of 100,000 USDC notional: the builder charge is 14 USDC, before Hyperliquid's own fee. If only 60,000 USDC fills, the builder charge is 8.40 USDC. Silhouette takes no additional spread on the perpetuals fill. The charge follows executed notional, including when execution covers less than the original request.

Neither the quote nor its price limit includes these fees. After fees, a buy can cost more per unit than the signed price, while a seller can receive less. Silhouette's HyperEVM spot trades settle directly with makers; the perps trades pass through the Hyperliquid book. The perps service leaves funds in the Hyperliquid account and collects its charge through Hyperliquid's builder mechanism.

Traders must approve the builder fee in their Hyperliquid account before using the service. If the rate rises above their existing allowance, they must approve it again. An approval below the required rate prevents Silhouette from sending the trade. Insufficient margin can separately cause Hyperliquid to reject the taker's order.

## Account permissions and closing exposure

The app requires a funded Hyperliquid account with $USDC margin, unified account mode and an approved signing key. The main wallet signs the setup actions: switching account mode, authorizing the key and approving the builder fee. After setup, the key signs orders when the trader accepts quotes, without a new main-wallet prompt. Those orders book to the main account. A key that stops working must be approved again from the main wallet.

The RFQ itself carries no leverage or margin-mode setting. Execution uses the settings already held for that market in the Hyperliquid account. The app shows leverage and margin mode on the request ticket, but those controls change the underlying account settings. The RFQ service has no separate margin account or independent position parameters.

Hyperliquid nets positions by market. To close a position, the app sends an ordinary order on the opposite side, and Silhouette does not cap that request at the size of the open position. A larger trade can close the existing position and open exposure in the opposite direction. The documentation tells traders to check their current size on Hyperliquid and keep the closing request at or below it.

API users can instead sign a reduce-only order. Hyperliquid checks that instruction against the position when execution occurs. The order can fill partially or not at all, but it can only shrink the position. The ordinary closing order submitted through the app lacks that protection.

## Check Hyperliquid after a failed request

The RFQ result reports the filled quantity and average price before fees. Silhouette returns neither a Hyperliquid order ID nor a transaction hash. Hyperliquid holds the fill record and position, and traders can check the fill in their Hyperliquid trade history.

A position may exist even when Silhouette cannot confirm execution. The documentation says an unconfirmed request is final and will not be updated later. It instructs traders to check their Hyperliquid position after any failed perpetuals request before trading the same market again.

The launch announcement names HIP-3 markets and higher quote caps as planned additions. It gives no date for either expansion.
