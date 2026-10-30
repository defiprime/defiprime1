---
layout: blog
title: "OnePay opens stablecoin deposits with own-wallet restrictions"
url: /onepay-stablecoin-deposits-own-wallet-rules.html
h1title: "OnePay opens stablecoin deposits with own-wallet restrictions"
pagetitle: "OnePay stablecoin deposits: wallet rules and settlement risk"
metadescription: "OnePay opens USDC deposits for select US customers. Terms require a wallet users own and control, pass through depeg losses and allow early-credit reversals."
category: blog
featured-image: /images/blog/onepay-stablecoin-deposits-own-wallet-rules-ogp.png
intro: "OnePay's new stablecoin off-ramp converts funds into checking dollars, with strict sender-ownership rules and conditional early credits."
author: sawinyh
tags: ["Stablecoins", "Payments", "News"]
date: 2026-10-30T21:24:11+00:00
---

On October 30, 2026, OnePay [opened stablecoin deposits](https://www.onepay.com/newsroom/announcing-stablecoin-deposits) to select U.S. customers, allowing them to fund OnePay Checking with $USDC across 12 blockchains. The launch includes Tempo, Base, Solana and Ethereum, with no conversion fees at launch.

Incoming stablecoins become a dollar checking balance. The public customer agreement limits transfers to wallets the customer owns and controls. It also assigns depeg losses to the customer and allows an early dollar credit to be reversed if settlement fails.

## A checking off-ramp with a sender restriction

Users find “Deposit stablecoins” under Cash Control in the OnePay app. Bridge, Stripe's stablecoin orchestration platform, creates and secures the deposit addresses. It receives the assets, runs compliance checks and converts them into dollars. OnePay then credits the checking balance.

[Stripe's official statement](https://x.com/StripeCrypto/status/2116242702207799544) confirms the rollout, chain count and launch pricing. The announcement says deposits usually appear within moments. Conversion still requires blockchain confirmations under the terms, and the number of confirmations depends on the network. Bridge can also impose reviews, holds or compliance checks that delay access to the money.

The [Stablecoin Account Customer Agreement](https://www.onepay.com/legal/stablecoin-account-agreement), effective October 5, 2026, sets the operating rules. Customers must already be registered OnePay users with a deposit account in good standing, and they must pass Bridge's verification checks. Access also depends on whether Bridge is authorized to provide services in the customer's U.S. jurisdiction. The app is for personal, non-commercial and non-professional use. Each customer may maintain only one Stablecoin Account.

The agreement states the sender restriction directly: “You are not using the OnePay Stablecoin Program to receive stablecoins from any third party.” Customers must be the sole beneficial owners of the stablecoins they send and use the program for their own benefit. They must also own and control the sending blockchain address.

Both launch statements describe sending from an external wallet or exchange. The agreement puts a narrower condition on the sending address: OnePay or Bridge may refuse or reverse a transfer if it determines that the customer does not own and control that address. An exchange withdrawal has no blanket exemption from that requirement. Under these terms, a payer cannot send stablecoins directly to someone else's OnePay deposit address.

The app has the current supported-asset and network list. OnePay or Bridge can change it with or without notice. An unsupported asset, the wrong network or an incorrect address can permanently lose the funds. The agreement says none of OneProgress, its affiliate, the sponsor bank or Bridge provides recovery services for those mistakes.

## Conversion proceeds, not a promised dollar peg

OneProgress Assets LLC is the legal counterparty on the OnePay side. Bridge provides the Stablecoin Account and conversion services. OneProgress says it never receives, holds or takes title to the stablecoins. The customer authorizes Bridge to take title upon receipt and hold the assets in transit. Once the stablecoins reach Bridge, OneProgress cannot recall them.

Bridge uses the prevailing market rate at the time of conversion. The agreement allows intermediate settlement steps, including a temporary conversion into a different stablecoin before conversion into dollars. Customers neither hold nor receive that intermediate asset. Only the resulting dollars reach the destination account. The program does not allow cryptocurrency purchases through these Bridge services.

If the stablecoin depegs, the customer receives fewer dollars. OneProgress guarantees no particular dollar amount for a quantity of stablecoins, and the customer bears the difference between face value and actual conversion proceeds. That lower conversion value also determines the amount of any early credit. A weakened stablecoin carries no promise of redemption at par.

OnePay's no-conversion-fee offer applies at launch. Under the agreement, OneProgress charges no service fee but can introduce fees with notice. Customers still pay blockchain network fees. The standing risk disclosure also says Bridge's conversion rate may include a spread or fee. The launch offer is therefore not a permanent guarantee covering every cost of the transfer and conversion.

## Early dollar access can be reversed

After Bridge confirms conversion, the sponsor bank may make the proceeds available before Bridge delivers the corresponding dollars to its settlement account. The agreement calls this an Early Deposit. It carries no interest, finance charge or credit fee, and the agreement expressly describes it as neither a loan nor an extension of credit. The bank has discretion over whether to make those funds available. That availability can be suspended without notice, subject to applicable law.

Bridge delivers the underlying conversion proceeds at the end of the same business day or according to its settlement schedule. OneProgress then reconciles the prefunded position. If Bridge fails to settle, claws back a transaction or unwinds it after a compliance review, the corresponding early credit can be reversed. A customer can face that settlement reversal separately from a depeg loss already reflected in the conversion amount.

Corrections can leave the checking account with a negative balance, and the customer remains liable for it. Stablecoins and funds in transit at Bridge are not FDIC- or SIPC-insured. According to the agreement, FDIC coverage applies only after the credit is made available in the destination account at the sponsor bank, subject to applicable limits and requirements.

Customers should report missing credits, materially incorrect amounts or unauthorized deposits through OnePay support in the app. Which agreement governs a dispute depends on where it arose. Deposit-account credit disputes follow the deposit account agreement. Disputes over Bridge's receipt, custody, conversion rate or clawbacks follow the Bridge agreement. Disabling the program revokes continuing authorizations, but transactions already initiated remain subject to their reversals or corrections.

OnePay has announced access for select U.S. customers without a general-availability date. The complete current asset and network list remains in the app.
