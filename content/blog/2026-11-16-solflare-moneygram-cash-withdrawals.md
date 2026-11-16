---
layout: blog
title: "Solflare adds MoneyGram cash withdrawals for $USDC"
url: /solflare-moneygram-cash-withdrawals.html
h1title: "Solflare adds MoneyGram cash withdrawals for $USDC"
pagetitle: "Solflare adds MoneyGram cash withdrawals for $USDC"
metadescription: "Solflare users can cash out $USDC through MoneyGram in supported markets, with an introductory fee waiver through December 31, 2026."
category: blog
featured-image: /images/blog/solflare-moneygram-cash-withdrawals-ogp.png
intro: "Solflare has added MoneyGram cash withdrawals for eligible users holding $USDC on Solana."
author: sawinyh
tags: ["News", "Infrastructure"]
date: 2026-11-16T20:20:07+00:00
---

On November 16, 2026, MoneyGram [announced that Solflare had integrated its Ramps service](https://www.prnewswire.com/news-releases/solflare-and-moneygram-ramps-offer-crypto-to-cash-in-170-countries-and-territories-302940133.html), letting eligible wallet users withdraw $USDC on Solana as local cash at participating locations in more than 170 countries and territories. The service is live in supported markets.

Solflare users pay $0 in cash-out fees through December 31, 2026, subject to MoneyGram's terms and eligibility requirements. The withdrawal starts inside the wallet. Users select Withdraw from the portfolio, choose MoneyGram and enter the amount of $USDC to convert. MoneyGram then guides them through the transfer and cash collection.

## From wallet authorization to cash pickup

MoneyGram's [non-custodial Solana integration guide](https://xramps.moneygram.com/ops/developer/guides/react-native-solana) describes how cash-out works. The wallet opens MoneyGram's widget inside a mobile WebView. When the customer commits to the transaction, the widget sends a signing request to the wallet. The wallet signs and broadcasts the stablecoin transfer on Solana, and the widget issues a reference number for collection.

The recipient presents that reference number at the MoneyGram agent. The guide tells wallet developers to save it immediately and display it prominently in transaction history. Customers can also reopen an existing transaction in view mode. To do that, the wallet passes the transaction identifier and creates a session with the same wallet address used to start the transfer.

MoneyGram handles identity verification, compliance, stablecoin settlement and fiat payout. Its [product documentation](https://xramps.moneygram.com/) says partners must complete business verification and contract setup before going live. The user authorizes the on-chain transfer from their wallet. MoneyGram processes the cash payout through its retail network, subject to its compliance checks.

The wider Ramps service supports $USDC on Solana and Stellar through its widget and API keys. Solflare's announcement covers cash withdrawals on Solana. MoneyGram also documents a separate cash-in flow: a customer selects a location, completes identity checks and receives a counter confirmation code. After depositing cash, the customer receives stablecoins in a wallet. The Solflare release announces only cash-out.

Coverage differs by direction. MoneyGram lists cash-in availability across more than 25 countries and cash-out across more than 170 countries and territories. Access varies by market and wallet integration. Even in a supported country, the customer must be eligible and use a participating location. The announcement does not say that every retail agent can process Solflare withdrawals.

## The fee waiver and network costs

The cash-out fee promotion is separate from the Solana transaction fee. MoneyGram's developer guide says transferring stablecoins requires a small amount of $SOL for network costs. Wallet developers can check that the customer has enough of the native asset or arrange for the wallet operator to sponsor the fee. Solflare's release does not specify which approach it uses.

The widget's standard balance request checks only $USDC, according to the guide. A customer can have enough stablecoins to withdraw but lack the native asset needed to broadcast the transfer. The signing operation can then fail after the customer has completed identity verification and accepted the disclosures. The widget may not show the reason for the failure.

In MoneyGram's documented sponsorship design, the fee payer and transfer signer are separate. The operator's backend holds a funded keypair and signs for the network fee. The customer's wallet still signs the transfer instruction. This lets a customer transact without personally holding $SOL, though Solflare has not confirmed that it uses the sponsorship option.

Geographic restrictions apply independently of the promotion. MoneyGram's product page excludes crypto services in Alaska, Louisiana and Hawaii. It also says MoneyGram holds money-transmitter licensing across all 50 states, the District of Columbia and United States territories, and is registered with FinCEN. The listed crypto-service exclusions still apply despite that licensing coverage.

## What the integration requires

The developer documentation requires standard SPL $USDC for the Solana flow and excludes the token-extensions variant. MoneyGram uses its own signing-message format rather than the Solana Pay QR or deep-link specification. Wallet developers must meet these requirements when integrating Ramps; Solflare customers do not have to implement them to make a withdrawal.

MoneyGram controls production access. It must allowlist a partner's app domain or bundle identifier before the credentials will work. Partners must keep the secret API key on their server and out of the mobile application. MoneyGram supplies separate credentials for sandbox and production access. The public integration guide covers the non-custodial mobile flow.

Sandbox withdrawals produce reference numbers for testing, but retail locations cannot redeem them for cash. Production reference numbers are redeemable. The guide also states that the sandbox uses no real money, so completing a test withdrawal does not establish that an integration can make a cash payout.

Session tokens expire after 1 hour. The guide warns that a customer who returns to an old, open widget can encounter a silent failure. Developers must request a fresh session when mounting the widget instead of caching credentials across app sessions. MoneyGram provides no refresh endpoint; the application has to create a new session.

MoneyGram's security checklist tells partners to keep session tokens out of crash reports and enforce product amount limits on the server. The widget checks balances only on the client side. These are requirements in the provider's integration documentation, not findings about defects in Solflare's deployed wallet.

Customers can handle eligible refunds inside the widget. According to MoneyGram's guide, the returned $USDC goes to the original Solana wallet address. The transaction-history view shows pickup instructions and a status timeline. Reopening that view requires the API transaction identifier, which differs from the reference number used at the cash counter. Developers are instructed to store both identifiers.

Alongside the launch, MoneyGram reports 113% year-over-year volume growth for Ramps. The release does not give the underlying volume. The figure measures growth in MoneyGram's wider service, not activity from Solflare's newly announced withdrawal option.

The announcement leaves Solflare-specific withdrawal limits, the conversion-rate schedule and the post-promotion cash-out fee unpublished. The fee waiver ends December 31, 2026.
