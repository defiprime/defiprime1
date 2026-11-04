---
layout: blog
title: "Stripe opens stablecoin wallet payouts to US businesses"
url: /stripe-stablecoin-wallet-payouts.html
h1title: "Stripe opens stablecoin wallet payouts to US businesses"
pagetitle: "Stripe opens stablecoin wallet payouts to US businesses"
metadescription: "Stripe opens wallet payouts in more than 160 markets, with $USDC and $OUSD support, published fees and a New York exclusion."
category: blog
featured-image: /images/blog/stripe-stablecoin-wallet-payouts-ogp.png
intro: "Stripe now lets United States businesses send stablecoins from Treasury balances to external crypto wallets in more than 160 markets."
author: sawinyh
tags: ["Stablecoins", "Payments", "News"]
date: 2026-11-04T19:32:06+00:00
---

On November 4, 2026, [Stripe announced](https://x.com/StripeCrypto/status/2118027635230117889) that United States businesses can send stablecoin payouts to crypto wallets in more than 160 markets through Global Payouts. Businesses can send $OUSD or $USDC from balances in Stripe Treasury, with Stripe handling conversion when needed.

The [wallet payout documentation](https://docs.stripe.com/global-payouts/send-money/stablecoins.md) labels the feature public preview and excludes businesses located in New York. Those businesses can sign up for a notification. Stripe says payouts typically arrive within minutes, though network conditions can delay final receipt.

## Funding, networks and fees

A business funds the payout from a USD or $USDC balance in its financial account. If the funding currency differs from the stablecoin the recipient will receive, Stripe converts the funds before submitting the payout to the selected blockchain. Stripe charges the business in the currency of its balance.

The available networks depend on the destination token. Stripe lists $USDC payouts on Arbitrum, Avalanche C-Chain, Base, Ethereum, Optimism, Polygon, Solana, Stellar and Tempo. For $OUSD, it lists Base, Ethereum, Solana and Tempo. The documentation tells senders to confirm that the recipient’s wallet supports both the selected stablecoin and the selected network before sending.

Stripe’s [published pricing](https://stripe.com/pricing#global-payouts) lists a stablecoin wallet payout charge of $0.50 plus 0.5% of the amount. The Global Payouts section also lists a platform fee of 0.05% of monthly payout volume after an allowance. Stripe presents the platform fee separately from the stablecoin payout charge.

[Global Payouts requires Treasury](https://docs.stripe.com/global-payouts). Stripe tells businesses to check for Treasury in the Dashboard, activate their account or supply additional information where required, and fund the financial account before sending money. The wallet feature lets businesses send funds from those balances to recipients’ external wallets.

The Treasury-funded transfers are separate from the [Stripe and Plasma multi-currency card plans](/stripe-plasma-multi-currency-stablecoin-cards.html) defiprime covered previously. This announcement concerns payouts to recipients, with a documented wallet payout workflow available in public preview.

## Setting up recipients and sending funds

In the Dashboard, a sender creates a recipient by entering an email address and country, then supplies the required recipient information and crypto wallet details. Stripe allows the sender to reuse that information for future payouts, so repeat payments can use the existing recipient record.

Stripe’s [recipient creation guide](https://docs.stripe.com/global-payouts/recipient-creation) describes hosted forms for collecting payout details and identity information. Businesses can also collect and submit the information through their own interface. The business remains responsible for its interactions with recipients and for gathering the information needed to verify them. Stripe says it updates verification requirements as laws and regulations change. It tells businesses to review onboarding requirements regularly to avoid failures.

The recipient guide limits the Pay via email option to senders and recipients in the same country. That option does not support cross-border payouts. The guide also says Dashboard recipient creation supports bank accounts and crypto wallets, while compliance rules prevent manually entering a recipient’s debit card information.

The wallet documentation gives developers a choice between the Payout Intents API and the Outbound Payments API. Stripe recommends Payout Intents: the object covers review through sending and handles failed attempts on the same object. Setting `confirmation_method` to `manual` lets a business review a payout before Stripe sends it. An OutboundPayment is a single attempt; the integrator handles retries and rerouting.

Live API access requires a different key setup from a sandbox integration. Sandbox secret keys work with the APIs, but full-access live secret keys do not. Stripe requires a restricted API key for live requests. A business moving a working sandbox integration to live payouts must use that key setup to send real funds.

The recipient’s crypto-wallet capability must also be active before a payout. It cannot become active until the business provides the recipient’s name and address. Stripe checks capabilities asynchronously, so creating a recipient does not mean the recipient is immediately ready. Its documentation directs integrators to listen for the capability-status webhook.

## Submission and receipt are different states

Stripe distinguishes accepting a payout from submitting it on-chain. While an OutboundPayment is `processing`, Stripe holds the funds in the outbound pending balance. When it becomes `posted`, the funds have left the financial account and Stripe has submitted the payout on-chain. The recipient’s wallet or network can still delay availability at that point.

Failed and returned payouts have different accounting treatment. A `failed` payout stops before funds leave the financial account, and Stripe restores the available balance. A `returned` payout has posted but failed to reach the destination; Stripe returns those funds in a separate transaction. The wallet guide describes both states so an integration can distinguish a failed attempt from a later return.

The same guide explains how to handle webhook notifications. Its V2 events are thin events: the receiving system retrieves the related API resource to obtain the complete object. Stripe also instructs developers to verify webhook signatures to confirm that events came from Stripe. An integration uses the retrieved object together with the payout status to follow the transfer.

## Bank payouts have a separate access gate

Stripe documents another route for stablecoin balances: converting them into local currency and sending the money to an external bank account. That feature remains in private preview and requires an access request. The funds reach the destination bank account over a bank network. The newly announced wallet route sends stablecoins over a supported blockchain.

For bank payouts requiring currency conversion, Stripe shows an estimated amount in the recipient’s currency when the sender starts the payout. The final amount can change with the exchange rate when the payout completes. The documentation tells senders to review the payout details before sending, and says the conversion takes place as part of the payout.

The wallet documentation still directs New York businesses to sign up for notification of availability. It gives no opening date for those businesses.
