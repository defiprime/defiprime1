---
layout: blog
title: "DTCC Sets $30T Tokenization Scope Across Canton and Besu"
url: /dtcc-tokenization-service-launch-scope.html
h1title: "DTCC Sets $30T Tokenization Scope Across Canton and Besu"
pagetitle: "DTCC Tokenization Service Opens With 25 Securities"
metadescription: "DTCC's tokenization service starts with 25 securities, about $30T of eligible assets, and transfers on Canton and a private Besu network."
category: blog
featured-image: /images/blog/dtcc-tokenization-service-launch-scope-ogp.png
intro: "DTCC has defined the launch scope for tokenized DTC-held securities, including eligible assets, networks, controls, conversion hours, and its next integrations."
author: sawinyh
tags: ["News"]
date: 2026-10-17T07:18:54+00:00
---

DTCC's Tokenization Service is entering its October 2026 launch with [25 securities and about $30T of assets available to tokenize](https://communications.dtcc.com/rs/669-QIL-921/images/DTCC%20Tokenization%20Service%20At-a-Glance.pdf). Tokens will be backed 1:1 by securities held at The Depository Trust Company, and registered wallets will be able to transfer them within the same chain around the clock.

The first networks are Canton and DTCC's private Hyperledger Besu network. The launch gives DTC participants a controlled route between book-entry securities and blockchain representations while DTC remains the official record keeper. Canton is the public-network option, while Besu is operated as DTCC's private network. Both were used for digital conversions in the July production exercise, so the initial service carries those tested network choices into launch.

## What launches

The initial list covers select Russell 1000 equities, exchange-traded funds, and U.S. Treasury bills, notes, and bonds. DTCC says the equity list starts with select large-cap names. The ETF and Treasury sets will also begin with a limited selection before expanding.

Canton uses the CIP-56 token standard for the service. DTCC's private Besu network uses ERC-20. [Stellar with SEP-41 and Circle's Arc with ERC-20 are anticipated in 2027](https://communications.dtcc.com/rs/669-QIL-921/images/DTCC%20Tokenization%20Service%20At-a-Glance.pdf), along with other layer-one and layer-two networks chosen according to client and market demand.

Participants will submit conversion orders through a user interface or API. The conversion window runs from 2 a.m. to 6 p.m. ET on business days, with DTCC targeting processing in 15 minutes or less. Transfers between registered wallets can continue 24/7 after conversion, provided both wallets are on the same blockchain. DTCC's materials do not describe cross-chain transfers at launch.

This schedule separates conversion from transfer. A firm cannot submit a conversion at any hour just because the token can move at any hour. The 24/7 feature applies to peer-to-peer transfers between registered wallets after the security is in tokenized form. Entry into and exit from that form remain tied to the business-day order window and DTCC's processing target.

The tokens retain the same CUSIP as the book-entry securities. DTCC says they carry the same rights and investor protections. [DTC-issued tokens are also designed to preserve the same legal rights and economic interest as the underlying securities](https://www.dtcc.com/products-and-services/digital-assets/tokenization), including corporate-action processing across tokenized, traditional, or mixed holdings.

DTC will keep the official books and records. Token controls include transfer restrictions at launch. DTCC's product page also lists mint, burn, pause, and clawback functions, while ComposerX LedgerScan provides near real-time ownership tracking across the traditional and blockchain ledgers.

Those controls define the limits of token possession. A wallet can hold and transfer the representation, but DTC still maintains the authoritative record. Mint and burn functions govern movement between traditional and tokenized form. Pause, clawback, and transfer restrictions give the service compliance and operational controls that ordinary permissionless tokens may not have. LedgerScan is intended to show ownership across both ledgers without replacing DTC's records.

Treasury distributions and maturities will be serviced on-chain, but payments will go in fiat to participants' traditional accounts. The arrangement leaves the cash leg outside the blockchain workflow for those events.

## What changes for market participants

A DTC participant can convert an eligible position during the business-day window, move the token to another registered wallet at any hour, and later return it to book-entry form through the service. The same-CUSIP design is intended to keep one security identifier across both representations. DTCC describes this as a common liquidity pool spanning traditional and blockchain systems.

That structure matters for custody and operations. Firms can retain existing DTC custody, settlement, and servicing processes while adding approved blockchain wallets. They must also account for the service's controls. DTC can pause or claw back tokens, and transfer restrictions remain part of the asset. Operators therefore need wallet registration, compliance checks, and ledger reconciliation in addition to ordinary securities workflows.

The launch follows a production exercise on July 15, 2026. [More than 30 firms participated](https://www.dtcc.com/press-releases/2026/dtcc-turns-tokenization-into-reality), and conversions occurred on Canton and DTCC's private Besu network. DTCC said the exercise covered collateral pledges, securities lending, Treasury repo delivery-versus-payment, equity delivery-versus-payment, equity delivery-versus-delivery, equity token transfers, and central counterparty margin workflows.

The production exercise covered a broader workflow set than simple wallet transfers. The list included financing, settlement, securities lending, and margin operations. That range shows how DTCC expects one tokenized position to move through several institutional uses while remaining tied to a DTC-held security. It also explains the emphasis on the same CUSIP, ownership tracking, and controls across the tokenized and book-entry forms.

That exercise also showed where the first practical demand may come from. A participant holding an eligible Treasury or equity can move the token between approved wallets outside the conversion window. Collateral and settlement workflows still depend on counterparties, wallet support, compliance controls, and the availability of a suitable cash leg. The service provides the asset rail, while each transaction still needs those surrounding arrangements.

## The next service boundaries

DTCC's roadmap for 2027 and beyond includes more eligible Russell 1000 securities, ETFs, and Treasuries. It also lists expanded equity and ETF corporate actions, a consolidated stock record across book-entry and on-chain positions, settlement and collateral functions, on-chain netting, and digital cash. Single sign-on and maker-checker controls are planned as well.

The roadmap is indicative and subject to regulatory, participant, and market considerations. DTCC says it will prioritize the work during 2027 with participant and industry input. The immediate open question is which 25 securities participants can tokenize at launch. DTCC's public materials describe the asset classes and selection approach but do not publish the full list.
