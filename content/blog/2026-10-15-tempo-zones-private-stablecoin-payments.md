---
layout: blog
title: "Tempo Opens Private Stablecoin Zones With Deel Live in Production"
url: /tempo-zones-private-stablecoin-payments.html
h1title: "Tempo Opens Private Stablecoin Zones With Deel Live in Production"
pagetitle: "Tempo Zones Bring Private Stablecoin Payments to Deel"
metadescription: "Tempo made Zones generally available, letting enterprises hide internal stablecoin balances and payments while retaining compliance controls and liquidity."
category: blog
featured-image: /images/blog/tempo-zones-private-stablecoin-payments-ogp.png
intro: "Tempo has made its Zones privacy system generally available to enterprises, with Deel already using it for contractor stablecoin payments."
author: sawinyh
tags: ["News", "Stablecoins", "Payments"]
date: 2026-10-15T01:20:15+00:00
---

On October 14 at 13:18 UTC, Tempo announced that [Zones are generally available to enterprises](https://tempo.xyz/blog/privacy-is-live-on-tempo/), with Deel as the first production customer. The system keeps customer stablecoin balances and payments from public view while preserving operator visibility, policy controls, and access to applications on Tempo.

Deel is using its Zone to pay contractors without publicly revealing who received a payment or how much they received. Tempo says the deployment is live, rather than a pilot or planned integration.

## What a Zone exposes

A Zone divides payment data between the public chain and a private environment. A deposit into a Zone exposes the token, amount, and sender. The recipient remains private. A transfer inside the Zone exposes nothing publicly, while its sender, recipient, and amount remain private. Balances are also absent from the public view and visible only to the account holder and Zone operator.

The boundary becomes visible again when funds leave. A withdrawal exposes its amount and recipient, while keeping the sender private. An interaction with Tempo Earn or another DeFi product exposes the deposit, withdrawal, and amount. The identity that owns the resulting position remains private.

The table in Tempo's announcement gives each operation a different disclosure pattern. A payroll recipient can remain hidden when funds arrive inside a Zone, but the treasury deposit that funds the Zone is still public. Internal transfers conceal all three transaction fields from public observers. Withdrawal disclosure reverses part of that arrangement by showing the destination while concealing which private Zone account initiated it.

This makes the privacy claim narrower than hiding all activity associated with an enterprise. Public observers can still see assets and amounts crossing the Zone boundary. They cannot use the public record alone to assign an internal transfer or balance to a contractor. The operator and account holder retain information that the public chain omits. The announcement therefore promises confidentiality against public observers while preserving enterprise supervision of the private ledger.

This design does not make the operator blind. [Tempo says the Zone operator can inspect activity and pause transfers](https://tempo.xyz/blog/privacy-is-live-on-tempo/) to meet compliance requirements. Operators decide who can participate, which assets are allowed, and how incoming funds are screened. Stablecoin issuer policies carry into each Zone automatically.

The operator view gives businesses records for reconciliation, customer support, reporting, and audit. It also places access and intervention with the operator. Users receive privacy from the public chain, not from the enterprise running the Zone. That distinction matters for payroll and treasury teams assessing who can see payment records and who can stop a transfer.

## Private balances keep access to public products

Tempo presents Zones as a native network feature rather than a separate closed ledger. Private accounts can reach stablecoin swaps, foreign exchange, ramps, card programs, and yield. The announcement says every smart contract and protocol that works on Tempo also works with private balances in a Zone.

The privacy boundary changes when a user reaches those public products. A deposit to and withdrawal from Earn or DeFi are public, including the amount. Ownership of the position stays private. Operators therefore need to distinguish private internal transfers from public interactions at the Zone boundary when they explain the product to users.

Enterprises integrate with Tempo once, then select which flows are public or private. Privy and Bridge support Zones natively. Tempo says Privy's wallet infrastructure exposes the feature through familiar APIs, reducing the need for a business to assemble a separate privacy layer around each contractor wallet.

For a treasury team, the immediate operational change is the ability to keep payroll distribution and customer balances out of a public block explorer while still sending funds to network applications. For a user, the practical limit is equally clear: deposits, withdrawals, and selected DeFi actions still leave public records even when the account owner is concealed.

## Deel moves contractor wallets into a Zone

[Deel runs payroll for more than 40,000 businesses across 150 countries](https://tempo.xyz/blog/privacy-is-live-on-tempo/). It launched a stablecoin wallet on Tempo in June for contractors who want a dollar-backed balance that they can hold and earn on. Tempo and Privy then integrated a Zone with Privy's APIs for those wallets.

Deel's treasury deposit into the Zone remains visible. The individual contractor recipients, their payment amounts, and their holdings do not. Contractors see their own balances through Deel, while Deel retains the records needed for reconciliation and audit.

The setup preserves two separate views of the same payment system. Deel can use the operator record for payroll support and audits. Contractors can inspect their own balances in the Deel interface. An outside observer sees the treasury funding transaction but not its allocation among contractor accounts. Tempo does not say that the enterprise loses access to worker records, and the product's compliance controls depend on that retained access.

Thierry Edde, Deel's head of crypto, said salaries, balances, and payout histories should not sit on a public ledger. He described Zones as a way to preserve that privacy while allowing contractors to keep earnings stable, grow balances, and receive payments quickly. Dan Romero, Tempo's chief business officer, called privacy a native capability and said Deel is the first enterprise using it in production.

The announcement makes Zones available for enterprise payroll, contractor payouts, business payments, and stablecoin treasury activity. It does not name public pricing, capacity limits, or the process an account holder would use to challenge an operator pause. Those operating terms are the next details prospective users need before comparing a Zone with a public wallet or a conventional custodial account.
