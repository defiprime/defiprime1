---
layout: blog
title: "EQX Unveils Tokenized Equities on Hyperliquid"
url: /eqx-unveils-tokenized-equities-on-hyperliquid.html
h1title: "EQX unveils tokenized equities on Hyperliquid"
pagetitle: "EQX Details Share-Backed Equities for Hyperliquid"
metadescription: "EQX detailed 11 share-backed U.S. equity tokens for Hyperliquid, including custody, holder rights, fees and eligibility limits."
category: blog
featured-image: /images/blog/eqx-unveils-tokenized-equities-on-hyperliquid-ogp.png
intro: "EQX published the structure for 11 share-backed American equity tokens that it plans to open for round-the-clock trading on Hyperliquid."
author: sawinyh
tags: ["RWAs", "News"]
date: 2026-10-14T16:19:58+00:00
---

At 13:00 UTC on October 14, 2026, EQX Labs [introduced 11 tokenized U.S. equity markets](https://x.com/eqxlabs/status/2110355136329449686) that it plans to issue as HIP-1 tokens on HyperCore. The set covers $SPY, $QQQ, $AAPL, $AMZN, $GOOGL, $META, $MSFT, $NVDA, $TSLA, $MU and $SPCX. EQX says the markets will trade against $USDC on Hyperliquid's public spot order book, but its documentation states that trading is not live yet and gives no launch date.

The tokens are issued by EQX SPC Ltd., a British Virgin Islands segregated portfolio company. [Each token is legally an unsecured, limited-recourse participating debt instrument](https://docs.eqxlabs.io/how-eqx-works/what-you-hold), rather than the underlying share. Each ticker has a separate portfolio whose assets and obligations are kept apart from the other portfolios. The issuer is owned by the EQX STAR Trust, a Cayman purpose trust with independent governance, and EQX Labs provides technology services under an agreement with the issuer.

EQX says each token will be backed 1:1 by shares of the relevant company or fund. Those shares will sit in custody accounts held in the issuer's name at Alpaca Securities, Clear Street and StoneX Financial. The backing can include settled shares and shares in flight from an authorized participant, with delivery due by the next U.S. business day. EQX says its launch dashboard will separate settled and in-flight positions and publish the brokers' statements.

That split gives users two different backing states to monitor. Settled shares are already at a custodian. In-flight shares are still due from an authorized participant on the next U.S. business day. The broker statements and dashboard should therefore show whether reported backing has completed delivery or remains pending. The announcement does not describe a holder action for delayed delivery.

## How creation and holder rights work

Authorized participants will create tokens by delivering shares and redeem tokens for shares. EQX charges no issuer fee for creation or redemption. When a token trades above the backing value, an authorized participant can buy shares, create tokens and sell them. When it trades below backing value, the participant can buy tokens, redeem them and sell the shares. This mechanism can align prices while U.S. equity markets are open, when the underlying shares are available for arbitrage.

Other holders cannot redeem directly with the issuer. They buy and sell on Hyperliquid's order book. The trading venue, rather than the issuer, will therefore set the available liquidity. EQX says it adds no fee to holding or secondary trading, although traders still pay Hyperliquid's standard spot fee and an app may add its own charge. EQX instead receives a share of the trading fees that Hyperliquid pays to HIP-1 deployers. This separates the retail exit from the share-redemption process: a holder sells to another order-book participant, while an authorized participant handles conversion between tokens and shares.

The [holder documentation](https://docs.eqxlabs.io/how-eqx-works/what-you-hold) distinguishes the token from a brokerage share in several ways. EQX tokens are not covered by SIPC or deposit insurance. A holder has a limited-recourse debt claim against the issuer for one ticker's segregated portfolio, not equity in the company or fund. The token terms require redemption in shares rather than cash. That structure makes the quality and availability of the backing, the authorized participants and the issuer's compliance central to the product.

Dividends will initially buy more of the same shares after applicable withholding and broker costs. The shares-per-token ratio starts at 1.0 and increases as dividends are reinvested. EQX's comparison table specifies 30% U.S. withholding at the issuer. Stock splits will change the ratio. For other corporate actions, including mergers, EQX says it will announce the planned treatment in advance.

Token holders can submit voting instructions by signing with the wallet that holds the tokens. EQX says it will use reasonable endeavours to follow those instructions. The arrangement passes an instruction to the issuer, rather than making the token holder the registered shareholder.

## What changes for Hyperliquid users

The planned markets put equity exposure on HyperCore beside Hyperliquid's existing spot and derivatives markets. Orders will go directly to a public order book rather than through a broker. EQX says transfers and on-chain settlement complete in under a second. The markets are designed to operate 24/7/365, including when U.S. exchanges are closed. During those closed hours, authorized participants cannot perform the share-side leg of the arbitrage described by EQX, so the documentation does not establish that token prices will track shares continuously.

For DeFi operators, the tokens create prospective collateral and vault assets with equity-linked economics. EQX says public token IDs and backing data will let apps list, price or lend against the tokens without an EQX account, API key or issuer fee. HyperEVM use depends on a contract address being listed in the token registry. Protocols considering these assets will still need to account for off-hours price formation, the issuer claim, custody status and restrictions on who may hold them.

The eligibility restrictions are material. [EQX says the tokens are not offered](https://docs.eqxlabs.io/get-started) to U.S. persons, people in the United States, British Virgin Islands residents or persons there, or sanctioned persons. Eligible users need a wallet funded with $USDC on Hyperliquid, with no EQX account or identity check. The official token ID matters because anyone can copy a market name.

Trading remains the next unresolved milestone. EQX has published the issuer structure, the first 11 tickers and the intended mechanics, but it has not stated when the order books will open, which authorized participants will be active at launch or how much settled backing each market will begin with.
