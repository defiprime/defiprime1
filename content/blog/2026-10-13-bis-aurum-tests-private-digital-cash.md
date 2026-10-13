---
layout: blog
title: "BIS Aurum prototype tests private digital cash with ZK proofs"
url: /bis-aurum-tests-private-digital-cash.html
h1title: "BIS Aurum prototype tests private digital cash with ZK proofs"
pagetitle: "BIS Aurum tests privacy-preserving digital cash"
metadescription: "BIS Project Aurum Phase 2 uses evolving pseudonyms, ZK proofs and partitioned ledgers to keep payment details private while preserving bank controls."
category: blog
featured-image: /images/blog/bis-aurum-tests-private-digital-cash-ogp.png
intro: "BIS Project Aurum Phase 2 combines evolving pseudonyms, zero-knowledge proofs and partitioned ledgers in a privacy-preserving digital cash prototype."
author: sawinyh
tags: ["News"]
date: 2026-10-13T11:20:41+00:00
---

On October 13, 2026, the Bank for International Settlements published [Project Aurum Phase 2](https://www.bis.org/publications/project-aurum-phase-2-exploring-privacy-enhancing-technologies-digital-cash), a prototype for privacy-preserving digital cash. The publication gives no release time, transaction identifier or live transfer amount because Aurum is an exploratory system rather than a production payment network.

The prototype asks whether routine payments can avoid exposing unnecessary personal information while regulated institutions retain tools for anti-money laundering, counter-terrorist financing, fraud prevention and legally required intervention. BIS says the stack is not production ready. Its purpose is to show which privacy choices can be enforced by technology instead of depending only on institutional promises.

## How Aurum separates identity from payment data

Aurum keeps the two-tier structure of its first phase. The wholesale layer includes the central bank, commercial banks and validators on distributed ledger infrastructure. The retail layer is a non-DLT e-wallet network where digital cash is represented as unspent transaction output tokens. The central bank can issue and settle money without automatically receiving retail transaction details.

The system separates data twice. Wholesale and retail ledgers are distinct, so the central bank cannot access the retail ledger. Each bank also maintains a separate ledger. A bank retains the legal identity of the customer it onboarded, while the validator, counterparty bank and central bank do not receive that customer base.

After KYC, a user's bank issues a BBS+ credential on the user's certified public key. The credential lets the wallet create multiple evolving pseudonyms without revealing the public key. Each pseudonym remains verifiable as belonging to a KYC-checked account, while merchants cannot use a stable account identifier to join payments into a spending profile.

Pseudonyms alone do not hide enough. A centralized processor could still correlate transactions through amounts and timing. Aurum therefore uses zero-knowledge proofs to validate payments while restricting visibility of payment details, including amounts. Coins remain separate in the wallet, and legal finality occurs at payment. The design makes each payment an independent event rather than an update to a visible account history.

Selective disclosure adds a configurable compliance path. A payer scans the payee's QR code, chooses an account and enters an amount. The default reveals no personal information unless a compliance rule requires it. Users may disclose selected information voluntarily, while a bank can require masked payer details when a payment meets its configured threshold.

The [technical report](https://www.bis.org/publications/project-aurum-phase-2-exploring-privacy-enhancing-technologies-digital-cash.pdf) also describes controlled anonymous wallets. A dedicated intermediary could enforce one wallet per legal identifier and device without retaining the identity in the payment system. Banks can impose wallet and spending limits. At the highest privacy setting, payer and payee exchange only pseudonyms and cannot attribute them to real identities.

## Controls stay with regulated intermediaries

Aurum does not make every coin untouchable. A bank can lock one coin, a subset of coins or an entire wallet. If a suspicious transfer reaches a user, the bank can freeze the received coins while leaving unrelated value available. A separate decree transaction lets a bank transfer a coin without the owner's key in an exceptional case such as court-ordered confiscation. BIS says that function would require strong administrative controls against abuse.

Onboarding is also modular. The report lists options ranging from no identity checks with issuance and transaction limits to comprehensive checks that store personal data. Intermediate models can bind a wallet to a phone, accept a limited-use eligibility proof, use a non-linkable token from an identity provider or validate an ID while retaining only a privacy-preserving unique identifier. The common objective is to enforce one user and one wallet without exposing personal information more broadly.

For payment operators, that structure moves compliance decisions to explicit controls. A bank must set disclosure thresholds, wallet limits, onboarding rules and the conditions for coin or wallet locks. The architecture does not give the central bank a full retail ledger by default. It leaves customer identification and lawful tracing with the bank that performed onboarding.

For users, stronger privacy changes recovery. A KYC-linked pseudonym can still be resolved by the issuing bank when lawfully required. A fully anonymous wallet has no identity link, so funds cannot be recovered if access credentials are lost. BIS compares that result with losing physical cash or a cryptocurrency private key.

## Performance sets the deployment boundary

The prototype's pseudonym is around 2 KB before compression and 1.5 KB after compression. It fits in one QR code. BIS found that a 12 MP phone camera should scan it under suitable conditions, while an older 5 MP camera may struggle in low light. Reducing that payload remains part of the accessibility work.

Proof generation is the main processing cost. On the test setup, one input coin required 2.86 seconds and 20 input coins required 29 seconds. GPU acceleration reduced those results to 0.4 seconds and 1.76 seconds respectively. The implementation currently caps a transaction at 20 input coins because proof time and key size grow with the number of inputs.

A batch option lets a user merge many small coins without generating the full arithmetic-circuit proof. It improves performance but reveals the input coins to the validator. The validator can link those coins one step back to the transactions that created them, although evolving pseudonyms and proofs prevent tracing beyond that layer. Users can instead consolidate through regular transactions when avoiding that link matters more than speed.

Programmability has a similar limit. Conditions can be attached to individual coins, either in plaintext or encrypted and checked with proofs, but Aurum does not provide a general-purpose virtual machine. Automated payments may also require temporary delegation to a bank because each coin normally needs the user's signature. That introduces intermediary risk into a design intended to behave more like cash.

BIS does not set a production launch or another dated milestone. The open work is whether proof generation, QR payloads, recovery and access portability can be improved without giving one operator a reconstructable payment history or weakening the compliance controls the prototype preserves.
