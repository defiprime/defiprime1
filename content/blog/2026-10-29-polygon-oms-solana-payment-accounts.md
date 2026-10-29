---
layout: blog
title: "Polygon OMS adds Solana accounts and fiat payment flows"
url: /polygon-oms-solana-payment-accounts.html
h1title: "Polygon OMS adds Solana accounts and fiat payment flows"
pagetitle: "Polygon OMS adds Solana accounts and fiat payment flows"
metadescription: "Polygon OMS adds Solana wallets, virtual accounts and fiat payouts, linking stablecoin balances to bank money and cross-chain routing."
category: blog
featured-image: /images/blog/polygon-oms-solana-payment-accounts-ogp.png
intro: "Polygon has extended Open Money Stack to Solana, adding embedded accounts and fiat payment flows around its cross-chain routing service."
author: sawinyh
tags: ["Stablecoins", "Payments", "News"]
date: 2026-10-29T13:33:17+00:00
---

On October 29, 2026, Polygon [announced Solana support for Open Money Stack](https://polygon.technology/blog/polygon-oms-supports-solana), extending its payments infrastructure to bank payins, customer accounts, embedded wallets and fiat payouts around Solana balances. Polygon says those functions are live now, alongside routing between Solana, TRON and EVM chains.

The release covers the money flow around a Solana application: accepting a deposit, identifying its owner, holding funds, moving them to another asset or chain, and paying them out. Solana can remain the application's settlement layer. Polygon supplies the surrounding banking, wallet and routing services. Applications can use them without first moving their balances onto Polygon.

## From bank money to a Solana account

Customers can enter through bank transfers, cards, cash or crypto. Polygon says the fiat on- and off-ramp infrastructure is backed by money transmitter licenses across 48 US states and supports conversion between dollars and stablecoins on Solana. The licenses describe the ramp infrastructure's regulatory footprint; availability of individual payment methods still depends on the jurisdiction.

Virtual accounts identify the owner of incoming bank money. Each customer or business receives an account into which transfers can arrive, allowing the operator to identify whose money it has received. The virtual account handles bank intake. After conversion, the funds sit in a Solana account, separate from the account used to receive the bank transfer.

Polygon offers custodial or embedded wallets for those balances. Its embedded wallets now support Solana through the same API used for EVM wallets. An application can create and manage customer accounts through that interface, keeping the wallet and chain operations behind its own product screens. The announcement also lists programmable controls over when and where money moves as available now.

The routing component supports $USDC, $USDT, $PYUSD, $SOL and wrapped $SOL. Polygon gives an example: an application can receive $USDC from an Ethereum wallet and settle in $SOL for a Solana user, or run the flow in reverse. The source asset, source chain and asset delivered to the recipient can differ within the payment flow.

At the other end, customers can convert Solana stablecoins into fiat dollars and receive money through a bank account, card or cash collection at a store. Polygon says that off-ramp stays inside the business's product experience. A customer receiving a stablecoin payment can choose a fiat exit or keep the balance in a wallet.

## Routing uses existing liquidity infrastructure

Polygon's [separate explanation of Solana routing](https://polygon.technology/blog/move-money-between-solana-and-polygon-ethereum-base-more-evm-chains-with-polygon-oms) identifies Trails as the cross-chain component of OMS. It describes routes between Solana and more than 20 EVM chains in either direction. Named destinations include Polygon, Ethereum, Base, Arbitrum, Optimism and Avalanche. The page links to a live swap application and an interactive demo where developers can inspect the transaction experience.

The [Trails documentation](https://docs.trails.build/intro) explains what sits beneath that interface. Trails aggregates a user's wallet balances across chains and sources liquidity from existing infrastructure, including bridges, fillers and solvers. Its routing service sends flow to those systems. An application can remove the bridge-selection screen, but the underlying bridge or liquidity provider remains in the execution path when the chosen route requires it.

An application begins by defining an intent: the transaction it wants to complete, its destination chain and the token involved. Trails checks whether the transaction can succeed with assets already held on the current chain. If it can, the documented path is a direct call. Otherwise, Trails presents the user's aggregated balances so the user can select a funding route.

The wallet confirmation deposits the requested amount into what Trails calls an intent address. Trails then handles the required swaps, bridges and execution. Developers can also supply calldata for an arbitrary smart-contract function at the destination. The documented mechanism can orchestrate that transaction as well as handle transfers of the same asset between wallets.

Trails also documents [alternative gas payments](https://docs.trails.build/architecture/alt-fee-tokens) for permit-compatible tokens. Where that mechanism is available, the widget offers fee-token choices alongside native gas. The user signs an off-chain permit, and the relayer deducts the fee from the selected token balance without a separate on-chain approval transaction. This permit mechanism applies to compatible tokens; the documentation does not describe it as a general method for handling Solana gas.

Polygon's routing disclosure retains the infrastructure risks. Cross-chain functionality can depend on blockchain networks, smart contracts and third-party bridges outside Polygon's control. The same disclosure says licensed partners may carry out regulated money services, including fiat ramps. A route can involve a provider handling the fiat payment and separate infrastructure executing the on-chain transaction.

## Components can be adopted separately

Solana businesses can use the entire stack or select individual components while retaining their existing wallet, compliance provider, ledger or settlement rail. An operator can add routing or account infrastructure without replacing every provider in its payments system. Polygon offers the stack to fintechs, payment applications, marketplaces and other platforms building on Solana.

Its creator-payment example starts with a fan paying by dollar debit card. OMS converts the payment into a stablecoin on Solana and routes it across borders; the creator receives crypto or cashes out to a bank account. The announcement presents this as an illustrative workflow, not a named customer's production transaction. It combines a card-funded payment with the recipient's choice of bank or crypto delivery.

Polygon's broader [OMS product page](https://polygon.technology/open-money-stack) qualifies the stack's rollout. Its FAQ says many components are live while more components, including a single API for easy integration, are forthcoming. The Solana announcement says the listed payment functions are live now. Polygon has not reconciled the two descriptions on those pages, leaving the scope of the unified integration interface unclear.
