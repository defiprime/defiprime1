---
layout: blog
title: "Samsung Wallet Adds USDC Transfers on Solana and Sui"
url: /samsung-wallet-adds-usdc-on-solana-and-sui.html
h1title: "Samsung Wallet Adds USDC Transfers on Solana and Sui"
pagetitle: "Samsung Wallet Plans USDC Transfers on Solana and Sui"
metadescription: "Samsung Wallet will add USDC transfers for U.S. Galaxy users through Solana and Sui, with the initial rollout scheduled for late October."
category: blog
featured-image: /images/blog/samsung-wallet-adds-usdc-on-solana-and-sui-ogp.png
intro: "Samsung Wallet will add USDC transfers for American Galaxy users through Solana and Sui, with Coinbase supporting the product."
author: sawinyh
tags: ["News"]
date: 2026-10-08T03:19:43+00:00
---

At 00:39 UTC on October 8, 2026, the [Solana Foundation announced](https://x.com/solana/status/2107994265104339166) that Samsung Wallet users in the United States will be able to send $USDC across borders on Solana beginning in the last week of October. The planned feature will be available across 82 million U.S. Galaxy devices at launch. A [separate Sui Foundation announcement](https://www.sui.io/blog/samsung-collaborates-with-sui-to-bring-usdc-to-samsung-wallet-on-82-million-u-s-galaxy-devices) confirms that Samsung Wallet will also support $USDC on Sui.

The two network announcements describe one Samsung Wallet rollout with multiple blockchain rails. Solana says Samsung Wallet and Samsung Pay will support stablecoins on Solana. Sui says users will be able to hold and send $USDC over Sui. Coinbase separately said $USDC will be the first supported stablecoin and that the feature is powered by Coinbase. None of the three announcements names another stablecoin available at launch.

## How the transfer flow works

The [Solana product announcement](https://solana.com/news/samsung-wallet) places the transfer flow inside Samsung Wallet rather than in a separate crypto application. A user starts from the same interface used for payment cards, boarding passes and IDs. Solana runs behind the interface, while integrated fiat on-ramps and off-ramps convert money to and from local currency.

That structure gives users two distinct layers to consider. Samsung Wallet is the product interface. Solana or Sui provides the network used to move $USDC. The user does not have to leave Samsung Wallet to initiate the transfer, but the announcements do not specify how Samsung will select a network when both are available or whether the sender can choose one.

The Sui implementation removes a separate blockchain requirement. Sui says its gasless stablecoin transfers let users send $USDC without holding $SUI and without paying a network fee. The network-level transfer cost is $0.00. Samsung Wallet will support $USDC at launch, while the $SUI token itself will not be supported.

Sui's payment path combines infrastructure introduced in separate releases. Native $USDC went live on Sui in 2024, followed by Circle's Cross-Chain Transfer Protocol integration. Gasless stablecoin transfers reached Sui mainnet in May 2026. Samsung Wallet is therefore using an existing native asset and an existing sponsored-transaction mechanism rather than introducing a wrapped version of $USDC or requiring the sender to acquire the network token first. The announcement does not say whether Samsung will expose Cross-Chain Transfer Protocol functions in the wallet.

Solana does not make the same zero-fee promise in its announcement. Its release says the wallet has integrated conversion to and from local currency, but it does not publish transfer charges, conversion spreads, destination coverage or settlement limits. Those terms will determine the delivered cost of a remittance even when the blockchain layer is hidden from the sender.

Coinbase's [official statement](https://x.com/coinbase/status/2107988576042422383) describes the Samsung Wallet feature as powered by Coinbase and identifies $USDC as the first supported stablecoin. The statement does not explain which account, custody or compliance functions Coinbase will provide. The Solana and Sui releases also do not describe who controls private keys inside Samsung Wallet. Users therefore have no published basis yet for comparing the product's custody model with a self-custodial wallet or an exchange account.

## What changes for users and payment operators

The immediate change is distribution. Samsung says the function will sit in an application already present on Galaxy devices, and Solana puts launch availability across 82 million U.S. devices. That figure measures devices with access to the rollout, not funded accounts or completed transfers. The announcements provide no enrollment target, expected balance or transaction-volume forecast.

The networks bring different operational claims. Solana says its network has processed more than $5.25 trillion in stablecoin volume during 2026, while stablecoin supply on Solana is up nearly 20% year over year. Sui says it has processed more than $1 trillion in stablecoin transfer volume since August 2025. Those figures describe prior network activity. They do not measure Samsung Wallet usage.

For senders, the important change is the removal of several visible crypto steps. The transfer begins in Samsung Wallet, conversion is integrated, and the network runs behind the interface. On Sui, the sender does not need to obtain $SUI for gas. This reduces the number of assets and applications needed to initiate a transfer, although identity checks, funding methods and recipient eligibility are not described in the network announcements.

For payment operators, the launch creates a consumer distribution channel for $USDC without requiring a separate wallet download. It also creates integration questions. A receiving wallet or service will need to know which network carried the payment, which destinations Samsung supports and how conversion is priced. The announcements do not publish an API, recipient specification or merchant acceptance flow.

The stated use case is cross-border money movement. Sui cites more than 1.3 billion people participating in remittances worldwide and a Visa survey in which 41% of U.S. remittance users said they were likely to use stablecoins for international transfers. These are market-context figures rather than projected Samsung adoption. The rollout will provide a direct test of whether familiar wallet placement changes actual stablecoin usage.

## What remains open

Both network releases say the service will start in the United States and expand to additional markets. Solana makes that expansion subject to local regulatory requirements. Neither announcement gives a country list or a date for the first expansion.

The next dated milestone is the last week of October 2026, when the U.S. rollout is scheduled to begin. Before then, users and payment providers still need Samsung's fee schedule, eligibility rules, custody terms, supported destinations, transfer limits and network-selection process. Those details will show whether the product offers one consistent transfer service across Solana and Sui or separate routes with different costs and recipient requirements.
