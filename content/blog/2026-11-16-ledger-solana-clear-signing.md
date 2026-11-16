---
layout: blog
title: "Ledger brings readable Solana swaps to its hardware signers"
url: /ledger-solana-clear-signing.html
h1title: "Ledger brings readable Solana swaps to its hardware signers"
pagetitle: "Ledger adds Solana Clear Signing for Jupiter and Kamino"
metadescription: "Ledger's Solana Clear Signing shows supported swap details before approval, but unknown instructions still trigger blind signing."
category: blog
featured-image: /images/blog/ledger-solana-clear-signing-ogp.png
intro: "Ledger has launched Solana Clear Signing for supported transactions, with Jupiter and Kamino among the first applications."
author: sawinyh
tags: ["News"]
date: 2026-11-16T14:24:32+00:00
---

On November 16, 2026, Ledger [announced that Clear Signing is live on Solana](https://x.com/Ledger/status/2122308449031618600), allowing users to read the assets they send and receive in a supported Jupiter swap before approving it. The company names Jupiter and Kamino as the first supported applications and says it built the feature with the Solana Foundation and Anza.

Ledger puts coverage at nine Solana apps and eighteen of the twenty-two core actions it tracks. Its [technical account of the implementation](https://www.ledger.com/blog-solana-clear-signing) says the engine is live in the Ledger Solana app, version 1.17.0 and above, and the Device Management Kit, its software toolkit for connecting wallets to signers.

Every instruction in a transaction needs a reviewed descriptor, the metadata that tells the device how to interpret it. If any instruction lacks one, Ledger says the whole transaction falls back to blind signing with a warning. Even a supported application can build a transaction that the signer cannot present as a fully readable review.

## Following the assets through a transaction

Solana applications can compose several programs inside the same transaction. Ledger gives the example of a Kamino deposit button that can trigger a Jupiter swap, a Kamino vault deposit and a farm stake. Showing each instruction separately leaves the user reviewing all those intermediate operations alongside the financial action they requested.

The new engine uses metadata that describes where value enters and leaves each instruction. It joins an output to the next input when they share an account and compatible tokens. It keeps the endpoints that describe what leaves the user's wallet and what arrives. The resulting review can show the swap with Jupiter's intent, combining the intermediate movements instead of presenting each one as an independent action.

The device needs exact matches to make those joins. Ledger says account identity, token identity and the instruction's input and output relationships must agree. An instruction stays visible if missing data or an unresolved account prevents the device from establishing a token, owner or amount. That leaves the user with a longer review when the device lacks the information needed to combine the steps.

Hiding a step from the display leaves it in the transaction being signed. Ledger writes: “Hiding is display only. The signed transaction is always the full instruction list, and an advanced view shows everything raw.” Users can inspect the underlying instructions through that advanced view even when the normal review combines them.

Ledger tested the design with an offline Python implementation before writing the device code. The test engine replays a corpus of real transactions and prints the screens the device would show. Ledger checks changes to the specification or a descriptor against that corpus, with regressions appearing in the reports. The tests are Ledger's own; they are not an independent audit of the implementation.

## The labels have a trust boundary

A developer can deploy a program and supply an interface description that makes it resemble a legitimate application. The readable metadata is itself a security dependency. Ledger's technical post says wallets must curate which programs they trust and review descriptors for misleading labels, hidden parameters and lookalike programs.

Ledger compiles its registry into compact binary descriptors and signs them with its hardware security module. The descriptors tell the device how to read the raw bytes for each instruction. The Device Management Kit selects those needed for a transaction and streams them to the signer. Before running the display engine and signing, the device checks that every instruction has a signed descriptor.

Some facts the device needs come from chain state, including token-account ownership and the contents of address lookup tables. A static program description cannot supply that context. A Ledger backend fetches and signs the information, tying it to a fresh challenge from the device to prevent replay. The review depends on the curated descriptions as well as the authenticated context delivered to the signer.

Clear Signing supplies readable intent and fields. Ledger's [Clear Signing guide](https://www.ledger.com/academy/topics/ledgersolutions/what-is-clear-signing) describes Transaction Check as a separate feature that analyzes transactions for potential threats and alerts the user before signing. The readable review and the threat check perform different jobs in the signing process.

Ledger's earlier [Singapore police advisory coverage](/ledger-singapore-police-advisory.html) concerned tampered hardware wallets. This release concerns the transaction review shown by a signer, a different part of the user's security checks.

## Compatibility still limits the review

The technical post names cases where program interfaces cannot supply the information the engine needs. DFlow's swap instruction puts source and destination token accounts, mints and routing information in a dynamic list whose meaning is determined at runtime. Ledger says the device can display slippage and a quoted output in that case, but cannot identify what is sent or received. Readable metadata cannot recover fields that the program interface leaves ambiguous.

Wallet integration has its own constraints. The [Ledger Wallet Provider documentation](https://developers.ledger.com/docs/ledger-wallet-provider/overview) describes an embedded connection flow with Clear Signing and Transaction Check. That browser SDK does not support mobile browsers because the required device-connection APIs are unavailable there. The restriction applies to this integration route; it does not establish the same restriction for every Ledger connection.

Ledger also uses two-step signing to give users time to review a Solana transaction before its blockhash expires. The device first records the approved transaction. The wallet then replaces the blockhash, and the device checks that nothing else changed before signing. An existing co-signature complicates the process because changing the blockhash breaks the other party's signature. Applications that verify the transaction after signing also need to accommodate that change to the blockhash.

Ledger says further work includes additional supported programs, interface changes that expose named accounts and unambiguous arguments, and a better answer to transaction expiry with the Solana Foundation. Its launch announcement names Jupiter and Kamino but does not enumerate the full set of supported apps or core actions.
