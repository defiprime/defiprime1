---
layout: blog
title: "ArcaTrader adds Hyperliquid perpetuals to its CFD platform"
url: /arcatrader-adds-hyperliquid-perpetuals.html
h1title: "ArcaTrader adds Hyperliquid perpetuals to its CFD platform"
pagetitle: "ArcaTrader adds Hyperliquid perpetuals to its CFD platform"
metadescription: "ArcaTrader adds Hyperliquid perpetuals for brokers and prop firms, with shared risk tools, broker-set fees and withdrawal approval queues."
category: blog
featured-image: /images/blog/arcatrader-adds-hyperliquid-perpetuals-ogp.png
intro: "ArcaTrader has added Hyperliquid perpetuals to its existing CFD platform, giving brokers and prop firms a shared terminal and back office for both markets."
author: sawinyh
tags: ["News"]
date: 2026-11-19T05:22:57+00:00
---

On November 17, 2026, ArcaTrader [announced its entry into perpetuals](https://x.com/arcatradecom/status/2122670746816192882), adding Hyperliquid-based trading to a platform previously used for contracts for difference. Its public product pages describe the web trader as live. Brokers and proprietary trading firms can offer perpetuals and CFDs through the same terminal and back office.

The firms preparing to use it have yet to launch. The announcement says "10+ new Perpetuals prop firms about to launch," a count of prospective deployments rather than evidence of existing perpetuals volume. ArcaTrader's [company page](https://www.arcatrade.com/about) dates the perpetuals launch to November 2026 and says the underlying CFD platform has operated for more than two years across multiple brands.

FDCTech built ArcaTrader. The company page identifies FDCTech as a United States public company listed on the OTC market and attributes more than 10,000 existing traders to the platform. That count belongs to the established CFD business. The announcement gives no separate count of active perpetuals traders.

## Hyperliquid settlement inside a broker terminal

ArcaTrader's [market description](https://www.arcatrade.com/) says perpetuals settle on-chain through Hyperliquid and trade around the clock. CFDs on forex, metals, energy and indices retain their market hours. Traders switch between these markets inside the same terminal, but each keeps its own settlement arrangements and trading schedule.

The perpetuals offering has no expiry and uses hourly funding. ArcaTrader lists adjustable leverage, isolated or cross margin, reduce-only orders and one-click execution among the available features. These specifications come from the operator's published product descriptions. They have not been checked against a deployed contract or tested through execution in a broker account.

The [perpetuals product page](https://www.arcatrade.com/perpetuals) describes how risk-based sizing works in the order panel. A trader selects the percentage of account balance to risk, and the platform calculates the lot size. Traders can still set the lot size manually. Market, limit and stop orders support both methods, with the sizing choice built into the order workflow.

Traders can enter take-profit and stop-loss instructions by price, dollar amount or percentage. The order panel also displays leverage and margin. Before submission, it shows the fee and liquidation price attached to the order, allowing the trader to inspect both the stated cost and the liquidation threshold.

The account-health panel shows the current margin level, the margin-call and liquidation levels, and the distance to a margin call. A live margin-level bar displays the account's margin position inside the web trader. ArcaTrader's published description gives no single margin-call threshold that applies to every firm's customers.

## The broker still configures the account

The [broker product page](https://www.arcatrade.com/brokers) describes controls that firms set by trade group and symbol. These include required stop losses, spread limits and price-spike filtering. Firms can also configure routing by trade group, keeping flow in-house or sending it to an external liquidity provider. The page lists these platform-wide capabilities alongside the Hyperliquid integration without specifying which routing choices apply to particular perpetuals markets.

The firm sets fees through the back office. It can configure percentage and per-lot transaction charges with minimums, as well as interest settings and swap and rollover schedules. These revenue controls apply across the platform; ArcaTrader has not published a uniform tariff for Hyperliquid trades. Account-level charges are described by the fee shown in the order panel and the firm's own terms.

Deposits and withdrawals pass through approval queues in a payments desk. The broker-facing software therefore retains a fund-movement approval process alongside the advertised access to on-chain perpetuals. ArcaTrader's public pages describe settlement through Hyperliquid, but leave the customer-by-customer wallet custody model unspecified. They also identify no new ArcaTrader settlement contract.

The platform provides more than 20 operational reports with Excel and PDF export. Listed categories cover profit and loss, commission, revenue, turnover and mark-to-market. Staff can also access margin warnings, reconciliation and audit reports. A separate live dashboard shows exposure by symbol and trade group, with widgets that the firm's staff can arrange.

## Prop challenges and deployment limits

The [prop-firm version](https://www.arcatrade.com/prop-firms) has a challenge engine for evaluations and funded accounts. Firms set profit targets, daily and overall drawdown, active days, starting balances and evaluation phases. The same engine supports challenges for perpetuals and CFDs, so firms can configure evaluations for both products through a common set of settings.

As a challenge's status changes, the platform automatically sends pass, next-stage and fail emails. Those messages are part of its built-in evaluation workflow. The launch announcement names none of the prospective perpetuals prop firms and publishes none of their individual challenge conditions. The available configuration settings describe the software, not the account agreement a particular firm will offer.

Firms can deploy a white-label platform under their own names, colours and custom web addresses. Other firms are not listed inside their platform. ArcaTrader offers hosting on its own servers or the customer's servers. For firms connecting the trading platform to an existing operation, its published interfaces include FIX, WebSockets and a web services API.

The [integration page](https://www.arcatrade.com/integrations) describes a separate setup discussion for each interface. FIX connectivity is scoped around the customer's liquidity and trading requirements. For WebSockets, customers must define the data they need and confirm which messages their configuration supports. The web services API connects business software, with account and back-office workflows agreed with the ArcaTrader team.

ArcaTrader advertises a fully branded launch in 7 days. Its setup process covers choosing connections, configuring branding and hosting, and setting account controls and routing for each trade group. Firms must discuss the scope and timing of custom integrations separately. The advertised launch interval covers platform setup, with no published timetable that applies to every custom connection.

The web trader is live, according to ArcaTrader, while native iOS and Android apps remain planned. Its coming-soon list also includes market depth with a buy/sell imbalance bar, shareable profit-and-loss cards and richer trader statistics. ArcaTrader gives no release dates for those features.
