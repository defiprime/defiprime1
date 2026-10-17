---
layout: blog
title: "CoreWeave, Broadcom and Seven Others Object to OKXICE Stock Tokens"
url: /okxice-nine-issuers-object-tokenized-stocks.html
h1title: "CoreWeave, Broadcom and Seven Others Object to OKXICE Stock Tokens"
pagetitle: "CoreWeave, Broadcom and Seven Others Object to OKXICE Stock Tokens"
metadescription: "OKXICE lists nine issuers objecting to tokenized stock trading, including CoreWeave and Broadcom, as its notice details permissioned pools on XLayer."
category: blog
featured-image: /images/blog/okxice-nine-issuers-object-tokenized-stocks-ogp.png
intro: "OKXICE disclosed objections from nine issuers to tokenized stock trading on its proposed XLayer venue."
author: sawinyh
tags: ["News", "RWAs"]
date: 2026-10-17T20:21:59+00:00
---

In its October 15, 2026 [public notice](https://www.okx.com/cdn/assets/files/2610/F085D8D65135AB9C.pdf), OKXICE disclosed objections from nine companies to trading tokenized versions of their shares on its planned venue. CoreWeave, Broadcom and Verizon appear alongside Cerebras Systems, AppLovin, Applied Digital, Rocket Lab, Applied Optoelectronics and UnitedHealth Group.

The venue would run permissioned Uniswap v4 pools on XLayer. Its operator, OKXICE LLC, is a Texas company owned equally by Intercontinental Exchange Holdings and OKC USA Holding. It intends to serve retail investors, institutions, market makers and liquidity providers.

## The objection applies to the venue

Nasdaq's [issuer FAQ](https://www.nasdaq.com/docs/listings/faq-sec-innovation-exemption) describes how the SEC's innovation exemption handles stock tokenized by an unaffiliated third party. An issuer has 30 calendar days after receiving notice to evaluate the proposal and submit an objection directly to the venue. A timely objection prevents that venue from making the tokenized stock available under the exemption. If the issuer does not object, the venue may proceed subject to the exemption's conditions.

The opt-out covers the particular venue that sent the notice. An issuer cannot use it to submit a blanket objection covering every venue that might trade a tokenized version of its stock. Other venues have separate notice processes, regardless of how the issuer responds to OKXICE.

Nasdaq has stated its own position as an issuer in the FAQ: it intends to opt out of tokenized securities venues. That statement is separate from OKXICE's list of nine objecting companies. Nasdaq is not on that list.

## What a participant would hold

OKXICE's [disclosure](https://www.okx.com/cdn/assets/files/2610/F085D8D65135AB9C.pdf) describes tokens issued by a third party unaffiliated with the underlying company. Each token represents a security entitlement to one underlying share. The tokenizer acts through a broker-dealer registered with the SEC and belonging to FINRA. The stock is held on a one-for-one basis against the tokens outstanding.

To mint tokens, the tokenizer first routes an order for the underlying stock through its broker-dealer. It confirms acquisition and custody before issuing the corresponding tokens. Redemption reverses that process: the tokenizer receives and burns the tokens, and the underlying shares are sold or delivered. The return of shares or proceeds follows the tokenizer's redemption terms.

Before making a stock available, OKXICE says it verifies that token holders receive the rights of the equivalent traditional share class, including dividends, voting and a share of residual assets on liquidation. It checks the tokenizer's most recent reserve attestation, which must be issued or verified by an independent accounting firm. It also reviews written procedures for passing through distributions and votes.

That review covers stock splits and mergers as well. The tokenizer must have procedures for corporate actions that change a holder's interest in the issuer. OKXICE reviews the backing, redemption and shareholder rights separately from its process for obtaining notice of an issuer's objection.

## Access and pricing inside the pools

The proposed pools pair a tokenized stock with $USDC, $USDG or $USDT. OKXICE does not operate an order book, take custody of participants' assets, extend credit or conduct primary securities offerings. A participant's wallet must hold the venue's valid soulbound token to trade or provide liquidity.

Participants obtain that non-transferable token by clearing identity, anti-money-laundering, sanctions and wallet screening. They must also receive approval for an account with the tokenizer, which adds the wallet to its approved list for the relevant stock. Only OKXICE can create pools using its permissioning hook.

Approved wallets can interact directly with the contracts or through a custom integration, without using the venue's interface. Third-party smart contracts need their own whitelisting. OKXICE says it does not currently support aggregators, solvers or relayers, which limits the external applications that can route trades into the pools.

Pool prices follow the Uniswap v4 constant-product mechanism. A purchase raises the pool price; a sale lowers it. The OKXICE hook leaves that pricing formula unchanged. Liquidity providers can choose a price range, and their liquidity is used for trading only while the pool price stays within that range.

The notice warns that token prices may diverge from the underlying shares, particularly outside regular exchange hours, in thin liquidity, or around trading halts and corporate actions. A large order can move the pool price substantially or fail. These warnings are the venue's own risk disclosures.

Each executed trade settles atomically on XLayer. Both assets transfer in the same blockchain transaction, with no clearing agency, central counterparty, netting or partial fill. If the transaction fails, neither asset transfers and participants' holdings remain unchanged.

The fee schedule separates the venue's service charge from pool and network fees. Every participant pays the same service-fee rate, with no individual negotiation. Each pool's fee rate is set when the pool is created. That fee accrues to liquidity providers in proportion to their liquidity, while network fees go to the supporting blockchain. The notice refers participants to the published schedule for the service and pool rates.

## Operator powers and halted pools

OKXICE can upgrade contracts, pause trading, change permissioning, create pools and withdraw a liquidity provider's position. Administrative transactions require approval by multiple authorized personnel, according to the notice. There is no timelock on changes, so participants may receive no advance notice of an upgrade.

Affected pools execute no trades during a stoppage. Liquidity providers can still deposit and withdraw assets to reposition before trading resumes. If OKXICE permanently stops offering a stock, it says it will use an administrative contract to return the remaining pool liquidity directly to providers' self-custodial wallets.

The notice lists the nine companies' objections without explaining their reasons. It does not attribute their decisions to the venue's pricing, access rules or contract controls.
