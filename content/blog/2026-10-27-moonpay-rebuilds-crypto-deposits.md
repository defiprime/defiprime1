---
layout: blog
title: "MoonPay rebuilds Crypto Deposits with fiat and exchange funding"
url: /moonpay-rebuilds-crypto-deposits.html
h1title: "MoonPay rebuilds Crypto Deposits with fiat and exchange funding"
pagetitle: "MoonPay rebuilds Crypto Deposits with fiat and exchange funding"
metadescription: "MoonPay combines fiat, wallet and exchange funding in Crypto Deposits. Its docs specify route checks, embedded-onramp approvals and settlement webhooks."
category: blog
featured-image: /images/blog/moonpay-rebuilds-crypto-deposits-ogp.png
intro: "MoonPay has rebuilt Crypto Deposits around fiat and crypto funding, with merchant-selected payout tokens and customer-specific route checks."
author: sawinyh
tags: ["News"]
date: 2026-10-27T16:23:05+00:00
---

On October 27, 2026, MoonPay [released a rebuilt Crypto Deposits product](https://www.moonpay.com/newsroom/crypto-deposits) that combines fiat funding, cross-chain transfers and connections to more than 600 wallets and centralized exchanges. The company says it is available now to partners and their users. Merchants choose the token they receive; MoonPay handles routing, conversion and delivery.

The original product launched in February to let users fund applications with crypto they already held. The upgrade adds funding options, including purchases made inside a partner's app. MoonPay's public implementation documentation sets out what merchants need to integrate it: a configured recipient currency, customer-specific deposit addresses, route checks and backend confirmation of settled deposits.

## What the funding flow supports

MoonPay names Bitcoin and stablecoins among the supported assets. Its announcement also says the product supports all tokens on chains including Solana, Ethereum, Arbitrum, Polygon, Base, $BNB Smart Chain, Robinhood Chain, HyperEVM and Hypercore. Users can connect an existing DeFi wallet or transfer directly from centralized exchanges, including Coinbase and Binance.

Fiat funding supports Apple Pay, Google Pay, credit and debit cards, Revolut Pay, bank transfers and local payment methods. MoonPay describes the headless onramp as operating inside the partner's app without redirects. Merchants seeking fiat settlement can also integrate MoonPay Enterprise, which the release identifies as a separate integration.

The [product page](https://www.moonpay.com/business/deposits) gives a narrower description of crypto coverage: 13 tokens across 10 blockchains. It also states that the webpage is not intended for EEA or New York users. Developers must check whether a particular deposit can reach the merchant's chosen payout currency at the implementation level, beyond the coverage described in the announcement and product page.

The [deposit documentation](https://dev.commerce.moonpay.com/docs/deposits) directs developers to query Get Deposit Currencies for available assets and networks. Deposited funds are then bridged and swapped into the recipient currency. The Get Deposit Customer response supplies a `swapRoutes` array describing paths into that currency, with an `available` flag and a `minAmountUsd` threshold for each route. Developers are told to remove unavailable routes from their currency picker and display or enforce the relevant minimum.

## What an integration actually needs

A merchant starts by creating a deposit through the dashboard or Create Deposit endpoint. The resulting `depositId` identifies the configuration. The merchant names it, chooses the recipient blockchain and currency, and enables the funding methods it wants to offer. Email notifications can report successful deposits.

The documented methods include manual transfers, wallet connections, exchange connections, Add Money and bank transfers. Manual transfer displays a QR code and address. Connecting a wallet lets the interface read its balance and initiate a transfer without copying an address; connecting an exchange lets the user transfer from an exchange balance.

Add Money requires API keys from MoonPay Ramps or Onramper under the integration settings. Bank Transfer creates a virtual account for the user, with support for rails such as SEPA and ACH where available. The documentation makes bank-transfer availability dependent on the user's region.

Each customer also needs a Deposit Customer record. The API requires a unique `customerId` and a `recipientWallet`, with optional metadata in `additionalJson`. It generates associated deposit addresses across SVM, EVM and Bitcoin networks. Developers must store the returned customer token to reuse the same customer's address for later transactions. The documentation provides separate endpoints to retrieve or update that record.

Developers can serve addresses through their own interface or embed MoonPay's deposit widget. The headless path retrieves the customer's `depositWallets` array. Recording wallet activity, either through the customer token or specified public keys, increases balance polling so incoming payments are detected more quickly. The widget route includes a React package and a demo where developers can paste a customer token to test display configurations.

MoonPay Ramps must approve the application's domains before Add Money can run in inline or button mode; additional business verification may be required. The documentation allows new-tab mode without that domain whitelisting. Merchants can also disable the cash-payment option. Funding without redirects, as described in the release, depends on how the merchant configures the embedded flow and whether it receives the required approval.

## Settlement, review and custody

MoonPay's instructions call for webhooks to confirm deposits on the backend. Developers can configure them in dashboard settings or through the deposit-webhook endpoint. The `DEPOSIT_TX_*` events confirm settled deposits. The documented integration handles settlement through these events, separately from the user's funding action on the frontend.

Other webhook events describe deposits that need different treatment. `DEPOSIT_BELOW_MINIMUM` tells the application that funds arrived below the sweep minimum so it can request a top-up. `DEPOSIT_UNDER_REVIEW` reports funds held for additional review. `DEPOSIT_WALLET_ROTATED` tells the application to replace a stored deposit address when the customer's wallet is replaced. Applications maintaining their own address records need that rotation update as well as the original customer token.

The release's legal disclaimer describes Crypto Deposits as a transfer service to a non-custodial wallet provided by a third-party platform. Helio Fintech Limited says it neither operates nor controls that wallet and does not hold, access or control user assets. The product page similarly says MoonPay does not accept deposits or act as custodian in connection with the feature.

Transfers through the product are not deposits with Helio, MoonPay or its affiliates. The disclaimer excludes FDIC deposit insurance, SIPC protection and other deposit-protection schemes, and warns that crypto assets can lose their value. The word “Deposits” in the product name describes the funding action, not an insured balance held by MoonPay.

MoonPay's announcement and product page still describe asset coverage differently. The documentation leaves the usable route and minimum amount to the customer-specific API response; those values must be checked against the merchant's selected payout currency.
