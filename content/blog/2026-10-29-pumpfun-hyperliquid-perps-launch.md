---
layout: blog
title: "Pumpfun launches Hyperliquid perps with a separate trading fee"
url: /pumpfun-hyperliquid-perps-launch.html
h1title: "Pumpfun launches Hyperliquid perps with a separate trading fee"
pagetitle: "Pumpfun Hyperliquid perps: fees, margin and access"
metadescription: "Pumpfun adds Hyperliquid perpetuals with isolated margin, a 0.05% trading surcharge and separate bridge costs; US users are excluded."
category: blog
featured-image: /images/blog/pumpfun-hyperliquid-perps-launch-ogp.png
intro: "Pumpfun has opened Hyperliquid perpetuals in its app, with isolated margin and a fee schedule separate from its spot trading charges."
author: sawinyh
tags: ["News"]
date: 2026-10-29T03:26:01+00:00
---

On October 28, 2026, Pumpfun [announced that Hyperliquid perpetuals were live in its app](https://x.com/Pumpfun/status/2115447518591103261), bringing long and short exposure to crypto, stocks and commodities into the same interface. The launch adds leveraged trading from a Pumpfun wallet, with isolated margin and a separate surcharge on top of Hyperliquid's fees.

Pumpfun says the app offers [300+ Hyperliquid markets](https://x.com/Pumpfun/status/2115447524601352470). Users can also post callouts of their perps positions inside the app; the announcement says followers who tail those positions can generate Callout Rewards for the poster. The trading feature is live, but access depends on location: Pumpfun's terms explicitly exclude people in the United States and certain other jurisdictions.

## Trading from the Pumpfun wallet

The [launch specifications](https://x.com/Pumpfun/status/2115447529378918513) list leverage up to 40x on $BTC, 25x on $ETH, 20x on stocks such as Tesla and Nvidia, and 50x on the S&P 500. Pumpfun advertises these limits for the named markets; leverage limits vary across the app. Users can fund trades with $USDC or $SOL from a Pumpfun wallet. They can set take-profit and stop-loss orders when opening a position or add them afterward.

Pumpfun offers long and short positions with isolated margin. In [Hyperliquid's margin documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining), isolated collateral is constrained to the asset being traded. A liquidation in that asset leaves other isolated positions and cross-margin positions unaffected. Hyperliquid's cross-margin arrangement shares collateral across cross positions.

The same documentation allows traders to add or remove margin from an isolated position after opening it. Unrealized profit stays available as additional margin for the isolated position, whereas unrealized profit on cross-margin positions can support new positions. Hyperliquid checks leverage when a position opens. The trader is responsible for monitoring it afterward. The documentation lists reducing or closing a position and adding margin to an isolated position as ways to respond to losses.

## The advertised fee is not the whole cost

Pumpfun's [fee announcement](https://x.com/Pumpfun/status/2115447537356468447) states: “Fees on Pumpfun perps: 0.05% per trade, or 0.04% when using a referral code, plus Hyperliquid’s standard fee.” The [published fee schedule](https://pump.fun/docs/fees) describes Pumpfun's charge as a builder fee of up to 0.05% of order notional. It applies to orders that open, add to or close a position. The fee base is the notional value being traded, not just the collateral posted.

Users approve the builder fee by signature when first using the perps feature. Pumpfun says it appears as a separate line before an order is confirmed. Orders submitted through the Perpetuals Feature are exempt from Pumpfun's ordinary Platform Fee. The schedule keeps that spot-app charge separate from the surcharge applied to perps orders.

The launch post says “No bridging required.” The fee page nevertheless provides for transfers through a bridge made available in the app: Pumpfun can charge up to 0.25% on each transfer to or from Hyperliquid, in addition to the bridge operator's own fees. The page says those charges may be displayed together as a single bridge-fee figure. The announcement describes the funding experience in the app; the fee page still allows Pumpfun to charge for transferring collateral.

Hyperliquid's trading charges and one-time account activation fee remain separate third-party costs. Pumpfun says the activation fee is deducted from the first deposit. Its terms also allow it to amend its own fees by updating the fee page, effective upon publication or on a later date stated there, without advance notice.

Open positions also face funding payments. [Hyperliquid documents funding](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding) as peer-to-peer payments between the long and short sides, with no fee collected on those payments. Funding is paid every hour and added to or subtracted from contract holders' balances. Those payments continue to affect the cost of holding a position after the trader has paid the entry order's builder fee.

## Liquidation follows Hyperliquid, not the app display

Pumpfun's [terms](https://pump.fun/docs/terms-and-conditions) warn that all posted collateral can be lost rapidly and positions can be liquidated automatically without notice. They describe the prices, margin requirements and liquidation levels displayed in the app as indicative. Actual execution follows Hyperliquid's mechanisms, and Pumpfun says it neither operates nor controls that protocol.

[Hyperliquid's liquidation documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations) says liquidation uses a mark price combining external exchange prices with Hyperliquid's order-book state. During high volatility or on highly leveraged positions, that mark can differ significantly from the book price. A trader monitoring only the latest available trade price can be watching a different price from the one used for liquidation.

When equity falls below maintenance margin, Hyperliquid first attempts liquidation through market orders on the order book. Those orders can close positions fully or partly. If the executions restore the maintenance requirement, the trader keeps the remaining collateral. An isolated position that reaches backstop liquidation instead transfers its position and isolated margin to the liquidator. Cross-margin positions remain untouched, but the liquidated position's maintenance margin is not returned.

Eligibility for the perps feature is additional to eligibility for the rest of Pumpfun. The terms say a person allowed to use the general platform can still be barred from a restricted feature, and availability can change with the person's location or circumstances.

Pumpfun reserves the right to assess access using geolocation, IP addresses, device information, wallets and transaction signals. Its terms prohibit ineligible users from attempting to use the restricted feature and prohibit assisting another ineligible person to access it. The company says its determination of availability is final.

The fee page separately warns that displayed transaction charges may differ from those ultimately charged by smart contracts. For the Perpetuals Feature, Pumpfun identifies its trading services as the source that determines its applicable fees.

The launch announcement and fee schedule do not identify the bridge operator or specify the amount of Hyperliquid's first-deposit activation charge. Neither document provides a single all-in charge for funding and opening a position.
