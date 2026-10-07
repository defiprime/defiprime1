---
layout: blog
title: "Cardano launches programmable tokens on mainnet"
url: /cardano-launches-programmable-tokens-on-mainnet.html
h1title: "Cardano launches programmable tokens on mainnet"
pagetitle: "Cardano launches CIP-0113 programmable tokens"
metadescription: "Cardano has launched CIP-0113 programmable tokens, giving regulated asset issuers ledger-enforced transfer, freeze and seizure controls."
category: blog
featured-image: /images/blog/cardano-launches-programmable-tokens-on-mainnet-ogp.png
intro: "Cardano has launched CIP-0113 programmable tokens for regulated assets with transfer, freeze and seizure rules enforced by the network."
author: sawinyh
tags: ["News"]
date: 2026-10-07T04:21:53+00:00
---

At 03:00 UTC on October 7, 2026, the Cardano Foundation [announced](https://x.com/Cardano_CF/status/2107667227210367411) that its programmable token standard was live on mainnet. The launch carries the identifier CIP-0113 and no transaction amount. It gives issuers of regulated stablecoins and other assets a way to put compliance rules into native Cardano tokens without a hard fork.

The [launch page](https://cardano.org/programmable-tokens/) describes a framework for stablecoins, bonds, shares and other securities. An issuer can attach allow lists, deny lists, freezes, seizures or transfer restrictions to an asset. The ledger checks those conditions whenever the token is transferred, minted or burned. The rules travel with the asset instead of depending on a wallet, custodian or separate off-chain check.

That changes Cardano's prior native-token model. The [CIP specification](https://github.com/cardano-foundation/CIPs/blob/master/CIP-0113/README.md) says native tokens could move freely after minting because they lacked programmable transfer logic. That prevented an issuer from enforcing holder eligibility, blocking sanctioned addresses or recovering tokens when a legal order required it. CIP-0113 makes a successful script execution a condition for a change in ownership.

## How the controls work

Issuers assemble compliance rules as modules. Each module is an independent set of smart contracts that follows the validation interface defined by CIP-0113. An issuer can select an existing module or write a custom one, then configure the conditions under which its token may be minted, burned or transferred. Modules can be added or updated as requirements change without altering the core protocol.

The reference implementation is open source and written in Aiken. It uses Cardano's existing native tokens, stake credentials and withdraw-zero pattern, so deployment does not require a network upgrade. The system evaluates the selected rules once for each transaction rather than once for every holding involved. Cardano says this keeps execution costs predictable as transaction size grows.

Programmable tokens remain at a shared script address. Ownership changes when a token is transacted, but the token does not leave that address. Stake credentials determine who owns it and let the owner access it through a wallet. A compliance script runs when the asset moves and rejects a transaction if a required rule is not satisfied.

The design also separates the core validator from asset-specific policy. Anyone can build a module that satisfies the interface without modifying the validator. The standard builds on CIP-0143, while the Cardano Foundation rebuilt the implementation in Aiken and added in-place upgrades. Deployed compliance logic can therefore be replaced without reissuing the token.

## What changes for holders and DeFi protocols

Holder rights now depend on the module attached to the token. An allow-list module can restrict sending and receiving to addresses that passed identity and anti-money-laundering checks. A deny list can block transfers involving sanctioned addresses. Freeze and seize functions can halt transfers or recover tokens from designated addresses when an issuer applies a legal or regulatory requirement. Other modules can encode restrictions based on counterparty, geography or holding period.

Those powers matter when a programmable token enters a lending market. The CIP tells protocols to inspect the token's substandard before accepting it as collateral. A freeze-and-seize design may let a third party move tokens without the holder's consent, which can affect collateral that a borrower or protocol expects to control. Deposit and withdrawal transactions must also satisfy the token's transfer logic. A listing review therefore needs to cover both the issuer's current module and its upgrade rights.

Issuers gain a common framework instead of building enforcement separately into each wallet or service. Wallets, explorers and indexers still need to display the rules accurately so users can see which parties can block or move an asset. The launch page provides integration guides and names BendingAI, CardanoScan, Eternl, GeroWallet and BloxBean as partners or users.

A failed compliance check prevents the transaction from being accepted, regardless of which wallet or service submitted it. That makes a token's module part of its effective transfer policy. Users need to know whether the asset requires verified credentials, whether an address can be placed on a deny list, and whether an authorized party can freeze or seize a balance. Operators also need to track module updates because the framework lets an issuer change deployed compliance logic.

The upgrade design preserves two fixed components. The CIP says the base payment credential used by every smart wallet address cannot move within a deployment because changing it would relocate holder funds. An individual token's minting policy is also permanent. That permanence keeps the token's identity intact when the logic governing it is upgraded. A deployment that changes the base credential is treated as a different deployment with its own bootstrap transaction.

CIP-0113 does not prescribe one compliance package for every asset. The launch page says there is no single global rulebook for tokenized assets and no configuration suitable for every token. Issuers can therefore encode conditions for a specific instrument, market and jurisdiction on the common framework. For a holder or DeFi venue, that flexibility means the standard's name alone does not reveal the restrictions. The attached module and the issuer's authority determine what can happen to the asset.

The Foundation says No Witness Labs independently audited the standard, Anastasia Labs performed security checks, and the design received recognition under the Capital Markets and Technology Association framework. The page does not identify a regulated stablecoin, bond or fund already issued on mainnet with CIP-0113. The next test is whether an issuer deploys a production asset and publishes a module whose restrictions wallets and DeFi protocols can evaluate before accepting funds.
