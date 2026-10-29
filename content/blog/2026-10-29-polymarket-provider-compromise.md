---
layout: blog
title: "Polymarket promises reimbursement after third-party compromise"
url: /polymarket-provider-compromise.html
h1title: "Polymarket promises reimbursement after third-party compromise"
pagetitle: "Polymarket third-party compromise and reimbursement promise"
metadescription: "Polymarket says affected users will be made whole after a provider compromise. Hudson Rock reports wallet-draining code; aggregate losses remain unverified."
category: blog
featured-image: /images/blog/polymarket-provider-compromise-ogp.png
intro: "Polymarket confirmed a third-party compromise, promised to make affected users whole and marked the incident fixed after pausing trading and relayer actions."
author: sawinyh
tags: ["News"]
date: 2026-10-29T19:29:13+00:00
---

On October 29, 2026, Polymarket confirmed that a third-party provider serving its international platform had been compromised and promised to reimburse affected users. Its status account marked the incident fixed at 19:05 UTC, after the exchange entered cancel-only mode and paused relayer actions.

"Anyone who has been impacted will be made whole," [Polymarket said](https://x.com/PolymarketTrade/status/2115874609014726842). The operator said it had identified and fixed the issue and referred it to relevant law enforcement. It gave no loss total, affected-account count or reimbursement schedule.

Separately, [Hudson Rock published original research](https://www.infostealers.com/article/polymarket-breach-alert-wallet-draining-code-found-in-a-third-party-script/) describing wallet-draining code retrieved from a DebugBear script URL associated with Polymarket. The code was designed to reach an authenticated trading session, request signatures and redirect assets. Hudson Rock's findings come from static analysis, not a verified accounting of executed thefts.

## The halt and the recovery notice

At 18:06 UTC, [Polymarket's status account announced](https://x.com/Poly_Status/status/2115867993049620977) that the exchange was in cancel-only mode and had paused relayer actions while it investigated. The operator confirmed the compromise at 18:33 UTC. It described trading as temporarily halted while it worked to bring the platform back online.

The [19:05 UTC update](https://x.com/Poly_Status/status/2115882755460309266) said: "This is fixed." The [official status page](https://status.polymarket.com/) subsequently showed the predictions trading API as operational. The recovery notice gave no further details about which accounts had been affected or how Polymarket would deliver reimbursement.

Hudson Rock also found production-build metadata recording removal of the DebugBear RUM script, with an embedded build timestamp of 17:59:20 UTC. The researcher cautioned that this timestamp could not establish when the build was deployed or whether containment was complete. Its homepage snapshot did not cover previously opened tabs, cached responses or authenticated pages.

DebugBear's [installation documentation](https://www.debugbear.com/docs/rum/setup) describes an analytics snippet added to a site's page head or loaded through a tag manager. Polymarket did not name the compromised provider in its own incident statement. Hudson Rock connected the script to DebugBear through retrieval and inspection. The researcher did not establish a wider compromise affecting other DebugBear customers.

## Code aimed at the existing trading session

Hudson Rock said it independently downloaded the suspect file twice and received identical payloads. Its review found code that read browser local-storage entries containing authentication context, a deposit-wallet address and a map of trading API credentials. The code distinguished between account types and checked for account and credential data before continuing.

The sample searched through React component properties and hook state for a live trading client, according to the researcher. It looked for objects with order-creation and order-submission methods, then attempted to use the client and its signer. This gave the code a way to seek authority already available inside the authenticated application.

Hudson Rock did not identify a routine that sent the credential map, a password, a seed phrase or a private key to the sample's reporting endpoint. Its analysis describes code attempting to reuse the application's existing capabilities. Exposure depended on the signer and the actions it could authorize.

The code had different paths for moving assets. In the branch labelled for externally owned accounts, it built a batch transfer of position tokens to a configured recipient. The Magic or non-EOA branch attempted sell orders at progressively more aggressive prices, followed by transfers of available proceeds. These separate paths do not support a claim that every exposed account's holdings were sold.

For wallet actions, the sample constructed signed batch messages for Polygon and attempted to submit them through Polymarket's relayer. Hudson Rock also found conversion and swap routes, with a direct token-transfer fallback. The researcher identified these as intended execution paths in the retrieved code; it did not verify individual transactions executing them.

The sample also constructed reporting requests containing wallet addresses, IP and country information, account type, portfolio values, position summaries and transfer-result fields. Hudson Rock described this collection of account-related information separately from the code's attempts to move assets. It distinguished the reporting requests from exporting a private key.

## What the wallet documentation establishes

Polymarket's [API documentation](https://docs.polymarket.com/getting-started/api) separates authentication of a private request from authorization of an order. Order placement uses API credentials to authenticate the request and a wallet signature to authorize the order itself. The code Hudson Rock described sought both parts of that process by searching for a live trading client and its signer.

The [wallet documentation](https://docs.polymarket.com/trading/wallets-auth) describes a Deposit Wallet executing contract calls as an ordered batch. The signer authorizes the complete batch, and the relayer submits it gaslessly. Legacy Safe and Proxy Wallet flows use wallet-specific payloads. Hudson Rock's analysis describes untrusted code attempting to choose the actions submitted through this signed-batch mechanism.

Polymarket's [Session Keys documentation](https://docs.polymarket.com/trading/session-keys) describes a more restricted form of delegated authority. A separate signer can receive permission to trade for a Deposit Wallet without using the owner's key, but it cannot withdraw funds. The incident evidence does not establish that session keys were involved. Their documented restriction is separate from the broader signer access the sample sought.

Hudson Rock did not connect a wallet or execute the sample. It warned that a signature request could prompt the user, be rejected or depend on session-specific authorization rules. Some of the sample's success checks accepted pending relayer states. Those checks alone could not establish that a transaction had settled on the blockchain.

The researcher advises users to reject unexpected signing and approval requests and close potentially exposed tabs. It recommends checking recent orders, position movements and wallet transactions through a trusted route, and retaining timestamps and transaction hashes for anomalies. The guidance covers both trading activity and asset movements, the two types of action described in the code.

Polymarket's statements give no aggregate loss figure or reimbursement timetable, and this report has no independently pinned on-chain loss accounting. Hudson Rock's investigation leaves the initial compromise mechanism, first malicious delivery and affected-user count unresolved.
