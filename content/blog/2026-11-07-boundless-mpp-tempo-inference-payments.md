---
layout: blog
title: "Boundless Opens Tempo Wallet Payments for AI Inference"
url: /boundless-mpp-tempo-inference-payments.html
h1title: "Boundless Opens Tempo Wallet Payments for AI Inference"
pagetitle: "Boundless Opens MPP Payments for AI Inference on Tempo"
metadescription: "Boundless launches wallet-paid AI inference on Tempo with MPP, session deposits, usage billing and refunds, without an account or API key."
category: blog
featured-image: /images/blog/boundless-mpp-tempo-inference-payments-ogp.png
intro: "Boundless now accepts wallet-funded MPP payments on Tempo for AI inference, with usage-based charges and refunds of unused session deposits."
author: sawinyh
tags: ["News", "Stablecoins", "Payments"]
date: 2026-11-07T05:26:39+00:00
---

On November 6, 2026, Boundless [opened wallet-paid inference over MPP](https://x.com/BoundlessHQ/status/2118803721723449464), letting agents buy model responses with assets on Tempo mainnet without a Boundless account or API key. The service accepts $MACH, $USDC.e and $OUSD, takes a session deposit, and charges for the tokens each request actually consumes.

Wallet payments sit alongside Boundless's existing prepaid API service. Boundless calls itself the first inference provider on Tempo to accept MPP directly. Its public product page and implementation documentation describe a live service, with terms for payment handling and refunds, supported clients and request restrictions. Access is account-free, but new wallets face sanctions screening when they first open a session.

## A deposit pays for requests

MPP is the machine-payments standard co-authored by Stripe and Tempo. In [Boundless's implementation](https://inference.boundless.network/docs/mpp), an unpaid inference request receives an HTTP 402 Payment Required response carrying a payment challenge. The client then opens a payment channel with a small deposit and signs a voucher for each request.

The endpoint supports both OpenAI Chat Completions and Responses. Model discovery and the setup guide are free to read, so an operator can check the available models and their quoted prices without paying for an inference call. An ordinary OpenAI client, however, stops at the payment challenge, according to the documentation. The client must also support the payment exchange: opening the session and signing requests.

The [product FAQ](https://boundless.network/mpp) describes $MACH as Tempo's onchain credit for payments and identifies $USDC.e and $OUSD as the accepted stablecoins. Boundless counts each accepted asset at dollar parity. A session opens in the asset used to pay, and any refund returns in that same asset. Dollar parity here is the provider's billing treatment of the tokens; their issuers' redemption promises have not been independently verified for this reporting.

A wallet funded with $MACH also needs a small $USDC.e balance. According to the documentation, $MACH's transfer policy limits transfers to approved addresses, which prevents its use for Tempo gas. Opening a channel and topping it up both incur network fees in $USDC.e. Boundless puts those fees at a fraction of a cent. It recommends keeping deposits small because the endpoint moves real money on mainnet.

## Actual usage follows a larger initial hold

Before running inference, the service reserves the request's worst-case cost. For that reservation, it counts every byte of the request body as an input token and adds the output limit. The final bill uses the tokens the model actually consumed, with cached input charged at the cache rate. A request the model fails to answer is refunded. Because the reservation happens before final billing, a request with a small eventual bill can still need a larger available session balance to run.

Nanocode's documented default deposit is one token, with $USDC.e as the default currency on Tempo mainnet. Operators can change the deposit, but the configuration expresses it in base units with six decimals. Currency selection is explicit. A separate setting can pin the network to mainnet instead of taking the chain from the endpoint's challenge. Together, these settings determine which asset the wallet pays with and how much of it is locked when the session opens.

The time it takes to recover unused funds depends on how the session closes. According to the docs, Nanocode cooperatively closes on exit and returns the unused deposit immediately. It also has a keep-session option for later runs. Closing through the Tempo wallet submits an on-chain close request instead. If spending remains unsettled, Boundless says its endpoint responds with its own close in about two to four minutes, settles the spending and refunds the balance. With nothing unsettled, withdrawal follows a 900-second grace period.

## The payment route changes, the rate card stays

Boundless advertises sixteen open models over MPP at the same per-token prices as its API. Its [published rate card](https://inference.boundless.network/docs/pricing) lists DeepSeek V4 Flash at $0.04 per million input tokens, $0.02 for cached input and $0.21 for output. The cached rate applies when a request reuses a prefix already held by the gateway. There is no advertised MPP discount on inference; the launch changes how agents fund calls at those rates.

The existing team on-demand plan uses prepaid credits, a shared team balance and per-key budgets, with no subscription fee. Boundless already has an account-free trial, though that route still issues a temporary API key. The [quickstart](https://inference.boundless.network/docs/quickstart) limits the trial to $0.01 of credit, expiring after 24 hours, with no top-up or extension. Wallet-funded sessions let agents continue paying for inference without moving from the trial into a Boundless account.

Concurrent agents can share a wallet and keep separate payment channels. Boundless says it built and tested the integration with Nanocode, the open-source agent SDK from Paradigm's Georgios Konstantopoulos. Nanocode assigns concurrent runs separate sessions unless a named session is selected. Its spending display shows what each model cost, giving the operator a per-agent channel record instead of putting every run against one shared API key.

## Client and request limits remain

The documentation names Nanocode as the supported client and warns that its prebuilt release does not yet include the Tempo gateway option. The documented installation requires a build from source with a Rust toolchain. Funding a wallet is therefore only part of the setup: the client still has to implement the payment exchange.

Boundless rejects several familiar API features before taking payment. These include requests for multiple results through the relevant sampling settings, previous-response references, conversation state, and stored prompts or items. It also refuses images and files supplied through remote URLs; the documented alternative is to supply the data inline. Workloads that need features outside MPP's coverage must use an API key and prepaid credits.

Boundless's announcement, FAQ and payment documentation provide no MPP usage totals or independent settlement audit. The availability and operating terms are the provider's statements; this reporting did not fund a wallet, open a session or test a refund.
