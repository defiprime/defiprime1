---
layout: blog
title: "Zerohash launches AUTH with configurable transfer checks"
url: /zerohash-auth-account-linking-transfer-controls.html
h1title: "Zerohash launches AUTH with configurable transfer checks"
pagetitle: "Zerohash AUTH launch: account linking and transfer checks"
metadescription: "Zerohash launches AUTH for linked-account crypto transfers. Its documentation separates address-free transfers from identity checks and deposit availability."
category: blog
featured-image: /images/blog/zerohash-auth-account-linking-transfer-controls-ogp.png
intro: "Zerohash launched AUTH for linked-account crypto transfers, with optional identity checks that can hold funds after they arrive on-chain."
author: sawinyh
tags: ["DeFi", "News"]
date: 2026-10-19T15:24:47+00:00
---

On October 19, 2026, Zerohash [announced AUTH](https://www.manilatimes.net/2026/10/19/tmt-newswire/globenewswire/zerohash-launches-auth-to-simplify-onchain-movements/2448792), an account-linking product for moving crypto, stablecoins and tokenized securities without copying wallet addresses or choosing a blockchain. The company says it offers 600+ connections across custodial accounts and self-custody wallets.

The product's public documentation separates that transfer interface from account-ownership checks. Platforms can use a connectivity-only version or enable identity matching. In the documented processing configuration, assets can arrive on-chain but remain locked until the sending account's name passes a check against the receiving customer's record.

## A launch after an earlier beta

AUTH already appeared in Zerohash's [August 3, 2026 release notes](https://docs.zerohash.com/changelog/auth-beta). That release made it available in beta for the Account Funding SDK, both as an addition for existing customers and for new integrations. The October announcement describes a broader launch. Account linking was already available through that earlier beta release.

Zerohash describes the connected accounts as representing approximately 250 million users across 190+ countries. Those are reach figures for the connection network, not a count of people using AUTH. The release names Robinhood, Gemini, Coinbase, MetaMask and Phantom among the supported connections.

The [network directory](https://docs.zerohash.com/docs/auth-network) still labels Coinbase, Kraken, Binance, Robinhood, Gemini and Crypto.com custodial integrations as beta. Separately, the launch disclosure says that names and logos in the application should not imply an official association or endorsement.

The [product overview](https://docs.zerohash.com/docs/auth) describes a standalone option for deposits and withdrawals involving crypto and stablecoins. AUTH can also be bundled with Zerohash's Move products: payouts, payins and account funding. Each platform chooses the assets, accounts and transfer types it enables, so the available routes depend on the application offering the service.

## Lite and Validate handle ownership differently

Auth Lite provides connectivity without matching the end user's account to the external account being connected. Zerohash describes it as suited to low-risk or closed-loop environments where ownership verification is not required. Auth Validate instead compares the KYC customer record with the external account and adds identity verification to the transfer flow.

Selected platform partners can combine Lite and Validate to accommodate more complex integrations and their chosen level of risk mitigation.

Authentication is required in both versions. The [integration guide](https://docs.zerohash.com/docs/auth-standalone) says users must enter their credentials regardless of whether a platform uses Lite or Validate; account matching is specific to Validate. The opening screen also presents the product terms, privacy policy and regulatory disclosures, and captures explicit consent before the linking flow.

Within [Validate](https://docs.zerohash.com/docs/auth-validate), Zerohash documents a daily reporting option and a processing-time check. The daily report identifies discrepancies between sending and receiving accounts using information exchanged through the TRUST network. Compliance teams can act on flagged participants, including locking or disabling them through the participant API.

The processing option changes when funds become available. In the documented flow, a user initiates an exchange withdrawal over $3,000. After the asset reaches the user's Zerohash wallet address, it remains in Processing while Zerohash waits for sender information and performs the name match. On-chain arrival precedes permission to use the funds.

The default comparison uses first and last names and a Jaro-Winkler similarity score. Zerohash recommends a threshold of 0.75, but allows organizations to change it according to their risk tolerance. Each platform sets the matching threshold that Zerohash will apply when checking a transfer.

A successful match leads to conversion into fiat in this documented account-funding flow. A failed match prevents conversion and moves the funds to a recovery-quarantine account label. The customer can then initiate a withdrawal to a wallet address of their choice. Zerohash sends status webhooks to the platform and can send customer emails when enabled.

Validate also permits platforms to block deposits initiated outside AUTH from being credited. The documentation gives the example of a user finding a deposit address on a block explorer and sending another transfer from a self-custody account. A platform can reject that credit even though the address is public; the Recovery SDK provides a route to retrieve the funds.

## Integration and settlement conditions

Connecting a new organization starts with Connect's onboarding process. The integration guide directs businesses to a representative for KYB requirements and assigns an organization identifier for subsequent API calls. Businesses must complete onboarding to integrate AUTH into their platforms. Wallet holders do not download it as an independent consumer app.

Organizations can set minimum and maximum transfer amounts denominated in fiat. They can also impose a daily volume cap per user. Connect enforces the individual transaction limits, while the daily cap covers activity within a 24-hour period. These settings sit alongside the platform's selection of permitted assets and transfer methods.

The technical flow begins with a backend request to create a Connect session. The returned token initializes the embedded AUTH SDK in the platform's frontend. For deposits, the guide instructs the platform to credit the customer's balance after on-chain confirmation and the Auth Completed webhook, tying the internal balance update to the reported settlement state.

The same guide describes failures caused by the connected account's systems or by the underlying blockchain being down. In those cases, it says the source account will be recredited and the user should retry. Zerohash's launch description of near-instant movement is subject to these documented processing and failure paths.

The launch disclosure identifies Connect Ltd., a Bermuda affiliate of Zerohash, as the entity securing AUTH and requires users to accept its terms. It also warns that services may be unavailable in some jurisdictions, including New York, and that Zerohash accounts have no FDIC or SIPC protection. The announcement gives no date for removing the beta labels that remain on the custodial integrations in the public network directory.
