---
layout: blog
title: "JPM Coin adds Ethereum with vetted access and a bank-account off-ramp"
url: /jpm-coin-ethereum-deposit-token.html
h1title: "JPM Coin adds Ethereum with vetted access and a bank-account off-ramp"
pagetitle: "JPM Coin on Ethereum: contracts, access and redemption"
metadescription: "JPMorgan lists Ethereum alongside Base for JPM Coin. Its docs specify approved counterparties, BDA redemption and a Saturday funding interruption."
category: blog
featured-image: /images/blog/jpm-coin-ethereum-deposit-token-ogp.png
intro: "JPMorgan has added Ethereum to JPM Coin's supported networks, with participation limited to approved counterparties and dollar redemption through bank accounts."
author: sawinyh
tags: ["Payments", "News"]
date: 2026-10-19T18:22:45+00:00
---

JPMorgan has expanded JPM Coin to Ethereum, with its [product documentation](https://www.jpmorgan.com/kinexys/jpm-coin) now listing the network alongside Base. At Ethereum block 26,228,359, the contract linked by the bank was deployed and returned the name and symbol $JPMD, with a reported total supply of 0.00 tokens.

The bank describes JPM Coin as a dollar-denominated deposit token for institutional payments, collateral posting and settlement. Access remains restricted to vetted, approved counterparties. Ethereum is a public network, but JPMorgan controls participation in its token through the bank's compliance and risk-management framework.

## The contract the bank identifies

The issuance FAQ links directly to the [Ethereum contract](https://etherscan.io/address/0xb2906cced1b2c8330480414cefa1eb52bdbd73a3) at `0xb2906cCED1b2c8330480414CeFA1eb52bDBd73A3`. It also links the separate Base deployment and warns that tokens with the same or similar names at other addresses are not affiliated with JPMorgan. Clients can check the asset against the address in the bank's own documentation.

Our pinned-block RPC reading returned two decimals and a false paused flag. The reported supply is a snapshot of that Ethereum contract at the specified block.

JPMorgan classifies the product as a bank-issued deposit token, not a stablecoin. Its FAQ says dollar deposits in JPMorgan bank accounts back the token and funds remain inside the firm's regulated banking infrastructure. According to the bank, the product carries the credit risk profile of commercial bank money and uses a blockchain record for payments and settlement.

## Funding and redemption through bank accounts

Clients fund JPM Coin through a Blockchain Deposit Account, or BDA. The documented sequence starts with depositing dollars into that account, then converting them into deposit tokens. The [BDA documentation](https://www.jpmorgan.com/kinexys/blockchain-deposit-accounts) expressly allows clients to mint JPM Coin directly from the account. JPMorgan says the funds stay within its banking infrastructure throughout that process.

Redemption runs in the other direction: JPM Coin converts back into dollars in the client's BDA. The product page says redemption is available at any time, without a lock-up period. JPMorgan describes payment, settlement and reconciliation as a single on-chain action on a shared ledger. The bank says reconciliation happens automatically and settlement takes place in near real time.

The route between the blockchain account and a traditional bank account has a scheduled interruption. The disclosures specify a three-hour downtime from 3 to 6 p.m. EST every Saturday for moving funds between traditional Demand Deposit Accounts on legacy systems and BDAs. Network transfers operate 24/7/365, according to the documentation. The bank says an enhancement to the traditional-account interface is under development.

BDAs can initiate payments to or from traditional Demand Deposit Accounts either inside or outside JPMorgan's network. The bank documents this account-level connection as part of its funding infrastructure. Clients redeem the token into their BDA; the Saturday interruption applies to the separate movement of funds between that account and legacy accounts.

The BDA supports deposits in eight currencies: U.S. dollars, Hong Kong dollars, Singapore dollars, Chinese renminbi, Japanese yen, Australian dollars, euros and British pounds. JPM Coin's product page specifies availability in U.S. dollars only, while the broader account supports deposits in all eight currencies.

## Integration and permitted uses

The BDA integrates through an API, SWIFT or a user interface. JPMorgan gives indicative onboarding times of as little as two to three weeks for user-interface access and two to three months for full API connectivity. Those estimates appear in the BDA FAQ. JPM Coin's own FAQ says implementation timing depends on the client's infrastructure, operational requirements and regulatory environment.

The bank says it configures JPM Coin integration with each client's team through the BDA framework, connecting existing treasury and payment infrastructure to on-chain activity. Its account documentation lists encryption, access controls, ongoing monitoring and KYC/AML checks among the controls applied to accounts and transactions. The token FAQ separately promises near-real-time visibility into token activity, transaction status and settlement confirmation on the shared ledger.

Named institutional uses include cross-border payments, intraday liquidity transfers and posting collateral for securities transactions. JPMorgan also describes programmable payment execution: predefined instructions can trigger conditional releases, scheduled transfers or rule-based payments. Its examples include conditional payments and automated transfers linked to settlement, allowing a treasury team to automate those movements instead of initiating each one manually.

The BDA page treats advanced programmability as an optional enhancement to the core account, alongside on-chain foreign exchange. Its linked [Advanced Programmable Payments documentation](https://www.jpmorgan.com/kinexys/programmable-payments) describes a configurable rules engine that uses near-real-time data, external feeds and operational events. Clients set the conditions for moving money; receipt of an incoming payment is one documented trigger. The service also consolidates payment events and resulting actions into an auditable history that teams can review. These capabilities are part of the account's optional services.

The commercial terms remain subject to bank approval. The product disclosure says potential benefits are illustrative and outcomes are not guaranteed. Offerings remain subject to internal review, due diligence and required regulatory approvals. JPMorgan Chase Bank or its affiliates ultimately determine whether a client can use the service. Availability can differ by geography.

The page also distinguishes deposit-insurance status by where deposits are held. It identifies JPMorgan Chase Bank as an FDIC member but says deposits held in non-U.S. branches are not FDIC insured, and neither are non-deposit products. The documentation makes no universal insurance promise to participants using the public-chain token.

JPMorgan also reserves the right to withdraw its offering at any time. The disclosure says the webpage is not a commitment to extend or arrange credit, or to provide other products or services.

The public pages do not specify a JPM Coin fee schedule or a fixed onboarding deadline for all clients. They also give no completion date for the enhancement intended to address the Saturday interruption between legacy accounts and BDAs.
