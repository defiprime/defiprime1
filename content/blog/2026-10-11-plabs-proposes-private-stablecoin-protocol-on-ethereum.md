---
layout: blog
title: "PLabs proposes private stablecoin protocol on Ethereum"
url: /plabs-proposes-private-stablecoin-protocol-on-ethereum.html
h1title: "PLabs proposes private stablecoin protocol on Ethereum"
pagetitle: "PLabs details private Ethereum stablecoin design"
metadescription: "PLabs proposed an Ethereum stablecoin design that separates unbacked inventory from 1:1 reserve-backed private notes and permits holder-led redemption."
category: blog
featured-image: /images/blog/plabs-proposes-private-stablecoin-protocol-on-ethereum-ogp.png
intro: "PLabs has proposed an Ethereum issuance protocol that would turn reserve deposits into private notes while keeping circulating claims backed 1:1."
author: sawinyh
tags: ["News", "Stablecoins"]
date: 2026-10-11T20:18:56+00:00
---

At 10:00 UTC on October 9, 2026, PLabs committed an [English technical paper](https://github.com/PLabs4/Private-StableCoin-On-Ethereum/blob/636c0e72bbc4e14cdc59d4b88bf9f563847e5c9f/private-stablecoin-on-ethereum-en.pdf) describing a private stablecoin issuance protocol for Ethereum. The proposed system separates unbacked protocol inventory from circulating private notes and requires a reserve deposit equal to each note that enters circulation. Its running example uses $USDC reserves and calls the resulting instance pUSDC.

The paper presents a design and does not report a deployed stablecoin. It describes two immutable contracts, ReserveVault and NotePool, plus zero-knowledge circuits and off-chain roles. Anyone could deploy a pair backed by a chosen reserve ERC-20. PLabs says the contracts would enforce reserve balance greater than or equal to circulating supply.

ReserveVault would custody the selected reserve asset and provide the public purchase and redemption entry points. NotePool would maintain the note commitment tree, spent-note nullifiers, and the compliance freeze root. PLabs recommends a commitment tree with depth 32. Once more than half of its leaves are used, the pool would enter an exit-only mode that rejects new activity while preserving redemption for every unspent note.

## Inventory becomes money only after payment

The accounting split is the paper's central mechanism. Protocol notes belong to a public protocol address and serve as inventory. Minting increases total supply and uncirculated inventory without moving $USDC. Those notes cannot be transferred or redeemed. A user note becomes circulating only through a purchase that deposits the same amount of reserve tokens in the same transaction.

The pool calculates circulating supply as total supply minus uncirculated inventory. A purchase decreases inventory by the amount sold while the ReserveVault pulls an equal amount of $USDC from the payer. The paper's target-output circuit binds that payment to the named private note, preventing the receiving commitment or amount from being substituted after authorization.

This separation lets an operator prepare inventory without creating a redeemable claim. The paper argues that excessive inventory minting does not threaten reserves because inventory cannot enter transfers. If the protocol's inventory spending key leaks, an attacker could disrupt sales by rewriting inventory ciphertexts, but could not convert those notes into circulating claims without depositing $USDC. PLabs recommends threshold signing for that key.

A buyer does not need to receive public $USDC before entering the private pool. The user gives a private payment address to an on-ramp. The ramp creates the output note, returns its plaintext to the user, and signs an EIP-712 authorization covering the payer, amount, commitment, nonce, and deadline. The operator then spends inventory, and a relayer submits the bundle. The Vault verifies the authorization, pulls $USDC, and calls the pool atomically.

At note level, each action spends one old note and creates one new note. Multiple actions can form a bundle. A public valueBalance records the difference between the face value spent and created. Purchases, redemptions, and transfers require that balance to be zero. Every signature covers the bundle's nullifiers, commitments, ciphertexts, valueBalance, recipient metadata, and executor. If the executor field names an address, only that address can submit the bundle.

The chain sees the payer, amount, output commitment, and nullifiers during a purchase. It does not see the user's private address or externally owned account. During a private transfer, the chain sees nullifiers, output commitments, and the relayer, while both addresses and amounts remain hidden. Redemption makes the recipient and amount public because reserve tokens leave the pool.

## Redemption does not require the operator

A note holder signs the redemption destination and amount into the bundle. The ReserveVault recomputes that digest before transferring reserves, so a relayer cannot replace the recipient or amount without invalidating verification. The holder or any relayer may call the public redemption entry point. The design requires no operator signature or submitter allow-list.

The contracts track slack as reserve balance minus circulating claims and accrued fees. Each valid entry point must leave that value unchanged and assert that it has not declined. A purchase is the only operation that increases circulating supply, and it deposits equal reserves atomically. Redemption remains available during an existing reserve shortfall as long as the transaction does not deepen it.

The operator does retain viewing keys for read-only audits. A compliance administrator can update a Merkle root representing frozen notes. Every spend must prove its note is absent from that set. A freeze leaves the note counted in circulating supply and does not let the administrator move reserves. A malformed root could halt all spending, which puts availability under the administrator's control even though reserve custody remains in the contracts.

Underlying reserve risk also remains. The paper states that the $USDC issuer could freeze the Vault address. Fiat delivery and inventory sales have no on-chain escrow, so users still trust their chosen ramp to deliver a note at purchase and fiat after an off-ramp redemption. Immutability removes an upgrade key, but any contract defect would require migration to a new pool.

## DeFi composition requires an atomic exit

Private notes are not ordinary ERC-20 balances, so existing public protocols cannot accept them directly. The paper proposes bundling redemption, a public action, and a return to privacy into one transaction. A non-reentrant coordinator would route the public leg through whitelisted adapters, bind execution to a signed plan, send leftovers only to a public address, and apply slippage limits.

PLabs also describes a private exchange prototype called PEX. Its current pair is P20 against sUSDC, where sUSDC is public $USDC shielded into a privacy pool. That prototype uses a non-custodial central limit order book and is separate from the proposed pUSDC issuance path. The paper presents it as a settlement model that could be adapted to trade a private stablecoin against a public asset in one transaction.

PLabs lists adapter allow-lists, freeze governance, and entry and exit specifications for other privacy pools as open questions.
