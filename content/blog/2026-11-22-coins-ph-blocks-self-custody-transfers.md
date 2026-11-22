---
layout: blog
title: "Coins.ph blocks transfers to and from self-custody wallets"
url: /coins-ph-blocks-self-custody-transfers.html
h1title: "Coins.ph blocks transfers to and from self-custody wallets"
pagetitle: "Coins.ph blocks self-custody crypto transfers"
metadescription: "Coins.ph restricts external crypto transfers to regulated exchanges from November 19, with sender and recipient checks applying regardless of amount."
category: blog
featured-image: /images/blog/coins-ph-blocks-self-custody-transfers-ogp.png
intro: "Coins.ph now limits external crypto transfers to regulated exchanges and requires counterparty details regardless of the amount."
author: sawinyh
tags: ["News", "Payments"]
date: 2026-11-22T08:27:14+00:00
---

Coins.ph stopped supporting crypto transfers to and from self-custody wallets on November 19, 2026, under a policy that applies to all users. Its [updated Travel Rule notice](https://support.coins.ph/hc/en-us/articles/4403931971225-How-does-the-Travel-Rule-affect-crypto-transfers) limits external sends and receipts to accounts at other regulated exchanges and requires counterparty information regardless of the transfer amount.

Users can no longer transfer crypto directly between a Coins.ph account and a self-custody wallet. The notice states: "Self-custody wallets are no longer supported." According to the same page, the change does not affect users who keep their activity inside Coins.ph.

Coins.ph says the information requirements comply with the Bangko Sentral ng Pilipinas Travel Rule. It cites Circular 1108, series of 2021, and Memorandum M-2023-042 from December 2023. The memorandum calls for enhanced due diligence on unhosted-wallet transfers, not a blanket prohibition. Coins.ph has announced the restriction to regulated exchanges as its own policy.

## Verification comes before withdrawal or deposit credit

For an outgoing transfer, the user enters the withdrawal amount and wallet address, then fills in the recipient's details on the Travel Rule form. The user reviews and confirms the request before Coins.ph verifies the details and sends the funds.

The withdrawal form asks for the recipient's name and wallet address, the destination wallet type, the destination exchange platform and the purpose of the transaction. Coins.ph instructs users to enter an individual's full legal name or a company's registered name exactly as recorded on the other platform. Users must select the exchange that will actually receive the funds.

For incoming transfers, the customer acts after the crypto arrives. Coins.ph says it sends a push notification, email or SMS. The customer opens Pending Transactions through that notification or through View transactions on the dashboard's Incoming transaction card. They then select the deposit and tap Verify transaction. Coins.ph credits the deposit once it has verified the submitted sender details.

The deposit form asks for the sender's name, address and wallet address, the source wallet type, the source exchange platform and the transaction's purpose. The sender's address has its own field, separate from the wallet address. Coins.ph asks customers to update the app to its latest version to see the new forms.

Missing or incorrect information can delay a transaction or prevent Coins.ph from processing it. Deposits stay on hold until the sender's details are verified. Coins.ph says fictitious information, or names, platforms and addresses connected to illicit activity, will result in rejection. The checks also apply to small transfers: the notice sets no minimum amount for the information requirement.

The notice also explains who receives the information customers submit. Asked whether the recipient will see the customer's details, Coins.ph answers no. It says it shares the information only as regulation requires and handles it under its privacy policy.

## What the BSP memorandum actually requires

The [BSP memorandum cited by Coins.ph](https://www.bsp.gov.ph/Regulations/Issuances/2023/M-2023-042.pdf) describes peer-to-peer transactions and transfers to or from unhosted wallets as generally outside the central bank's regulatory perimeter. It nevertheless expects virtual asset service providers to exercise caution and perform enhanced due diligence when handling transfers involving those wallets.

To the extent possible, and regardless of amount, providers are expected to obtain, verify and retain originator information, obtain and retain beneficiary information such as the wallet address, and retain transaction data such as a transaction hash or reference number. The memorandum also calls for continuous due diligence on customers transacting with unhosted wallets.

The regulator specifies when an institution should stop a transfer. If minimum information is unavailable or incomplete, the institution should neither facilitate the transfer nor make the funds available to the beneficiary. The memorandum's unhosted-wallet section does not direct providers to reject every such wallet.

Small transfers still carry identification requirements under the BSP framework. For transfers not exceeding Php 50,000, the memorandum requires accurate and meaningful originator and beneficiary information to remain with the transfer or related message through the payment chain. It lists both parties' names and account numbers, or a unique reference number when account numbers are absent.

Non-custodial service providers must obtain, verify and retain sending-customer information under the memorandum. They must also obtain and retain beneficiary information when the beneficiary is someone else. For transactions consisting only of virtual-asset swaps, the memorandum says these providers are not expected to transmit the required Travel Rule information.

Cross-border counterparties without Travel Rule regimes have separate requirements. Before sending, an institution must assess whether its counterparty can receive the required information. If it cannot, the sending institution must still verify and retain originator information and obtain and retain beneficiary information. For receipts, the memorandum calls for assessing the sending institution and its host country. Periodic risk assessment informs whether the institution accepts the funds and makes them available.

## Saved addresses and API connections

Coins.ph points frequent senders to its [Wallet Address Whitelist](https://support.coins.ph/hc/en-us/articles/28510968832281-How-do-I-use-the-Wallet-Address-Whitelist-feature). The feature saves recipient or sender information, including a wallet address, recipient name, destination wallet or exchange, and transfer purpose. According to the Travel Rule notice, saved addresses allow recipient details to be filled in on the next transfer.

Enabling the whitelist adds a separate withdrawal restriction: funds can go only to addresses already in the Address Book. To add a new address, users must provide the necessary one-time passwords to authorize the saved details. Saved addresses remain subject to the regulated-exchange-only policy in the transfer notice.

The change also affects automated integrations. Coins.ph says its Wallet OpenAPI deposit and withdrawal endpoints changed on November 19, 2026. It directs API users to its documentation or customer support for details. The transfer notice gives no date for restoring support for self-custody wallets.
