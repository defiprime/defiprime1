---
layout: blog
title: "Firelight launches FXRP-backed cover for DeFi vaults"
url: /firelight-launches-fxrp-backed-defi-vault-cover.html
h1title: "Firelight launches FXRP-backed cover for DeFi vaults"
pagetitle: "Firelight launches staked FXRP vault cover"
metadescription: "Firelight has launched shared DeFi vault protection backed by staked FXRP, starting with two Sentora products and a $115 million cap in $XRP."
category: blog
featured-image: /images/blog/firelight-launches-fxrp-backed-defi-vault-cover-ogp.png
intro: "Firelight has launched shared DeFi vault protection backed by staked FXRP, starting with two Sentora vault products."
author: sawinyh
tags: ["News"]
date: 2026-10-07T06:20:11+00:00
---

On October 6, 2026, Flare [announced](https://flare.network/news/firelight-is-live-backed-by-staked-fxrp-on-flare) that Firelight Protocol was live with aggregate staked positions capped at $115 million in $XRP. The launch puts staked FXRP behind cover for Sentora's USD Protected Vault and Protected RWA Vaults. Sentinel Labs develops and maintains Firelight, while Sentora incubated it.

Firelight pools the capital for every covered vault in one Firelight Vault on Flare. Stakers deposit FXRP into that vault, and the pooled capital backs the full portfolio of coverage elected by participating operators. The capital sits outside the protocols it covers. Stakers receive emissions for supplying it, but their principal and compounded rewards can be slashed when a covered loss is approved.

The initial deployment embeds cover in two Sentora products. The USD Protected Vault allocates across dollar-denominated strategies on established DeFi protocols. The Protected RWA Vaults use strategies around real-world assets, including lending and leveraged looping in markets that accept those assets as collateral. Their underlying strategies continue to run as before. Firelight adds cover against defined protocol failures at the deposit level.

That structure removes a separate purchase step for depositors. A user entering a covered vault receives its protection under terms registered onchain. The user does not need to compare and buy an individual policy. The operator selects the coverage, while Firelight records its scope, parameters, price and capacity.

## What the cover can pay for

The [published launch details](https://flare.network/news/firelight-is-live-backed-by-staked-fxrp-on-flare) name smart contract exploits, oracle failures, governance exploits, bad debt, mechanism-driven depegs and redemption failures as covered event categories. An event still has to satisfy the terms set for the affected vault. Firelight describes the product as coverage rather than insurance.

A payout begins with identifying every eligible active position in the affected market. ZeroShadow, Firelight's designated security partner, then publishes an exploit report. A five-firm Risk Consortium independently checks the event, confirms the loss and publishes an onchain attestation. Its members are Hypernative, Native, Credora, Cyfrin and GFX Labs. The protocol cannot release a payout until the consortium authorizes the event against the published coverage criteria.

This creates a defined claims path, but it also puts a practical condition on protection. A vault label alone does not determine whether a loss qualifies. Users need the registered terms for that vault and the consortium's eventual attestation. Operators need to keep the advertised risk scope consistent with the parameters recorded onchain.

Veda and Upshift are integrating Firelight at their infrastructure layers. Operators building on either platform will be able to switch on protection for their own vaults while drawing on the same Firelight Vault. That shared pool is the mechanism Firelight is using to extend capacity beyond the first Sentora products.

For an operator, enabling the integration does not make every loss payable. The operator still needs to select cover with a stated scope, price and capacity. Its users remain subject to the event categories and criteria recorded for that vault. The shared-pool design also connects operator demand to available staker capital. Adding a vault consumes capacity from the same pool that supports existing products, rather than creating a ring-fenced reserve for the new strategy. That makes the registered capacity a practical constraint for both vault marketing and deposit limits.

For depositors, the relevant comparison is between the vault's published protection and its underlying strategy risk. Firelight can cover the named protocol failures, but the launch does not say that every investment loss or market move qualifies. The consortium's review and attestation determine whether a reported event meets the terms before capital can be released.

## How $XRP enters the protection pool

$XRP holders can supply the pool through Flare Smart Accounts. A holder connects a supported XRPL wallet and selects the mint-and-deposit flow. The wallet sends $XRP on XRPL with the instruction attached. Flare's Data Connector verifies the transaction, FAssets mints FXRP at a 1:1 representation on Flare, and the system deposits the FXRP into Firelight. The holder receives stXRP in a smart account controlled by the originating XRPL address.

The flow does not require the user to hold $FLR. Fees are charged in FXRP. Protocol emissions also stream in FXRP, including fees that operators pay in $USDC and that the system converts before adding them to a staker's position. Firelight says emissions follow protocol revenue, so the amount available to stakers rises as operators enable more cover.

The return comes with direct exposure to covered losses. The staked deposit has no Firelight cover of its own, and slashing applies to accrued rewards as well as principal. Depositing through a Flare Smart Account also adds contract exposure to the account, FAssets and Firelight layers. Firelight lists OpenZeppelin, Coinspect and 0xMacro as contract auditors and says it completed a public Immunefi bug bounty, but it also states that contract risk remains.

Withdrawals are not immediate. Stakers initiate an exit through the web application and wait through the unstaking period. As cover becomes active, that window increases to match the 30-day coverage periods. A completed withdrawal returns FXRP, which the holder can redeem to $XRP at the XRPL address that opened the position. For allocators, the exit delay and slashing exposure are part of the yield calculation rather than operational details.

## Capacity and the open question

Flare says capital backing onchain cover equals about 0.14% of nearly $100 billion in DeFi. Firelight starts with a $115 million cap in $XRP on aggregate staked positions. The cap limits the capital available to support the first portfolio, while the exact protection available to each vault depends on its registered capacity and terms.

The broader integrations could add more covered vaults without creating separate capital pools. That may improve capital use, but it also means the same staker pool can stand behind a wider portfolio of risks. The unresolved point is how Firelight will price and allocate capacity as Veda and Upshift operators join, especially when several covered vaults depend on the same protocol, oracle or collateral. Firelight has not published that portfolio-level concentration detail in the launch announcement.
