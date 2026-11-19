---
layout: blog
title: "HSBC opens RedCoin-funded tokenised money fund access"
url: /hsbc-redcoin-tokenised-money-fund.html
h1title: "HSBC opens RedCoin-funded tokenised money fund access"
pagetitle: "HSBC opens RedCoin-funded tokenised money fund access"
metadescription: "HSBC offers tokenised money fund access from HKD100 through its app, with Ethereum records, approved wallets and off-chain settlement finality."
category: blog
featured-image: /images/blog/hsbc-redcoin-tokenised-money-fund-ogp.png
intro: "HSBC customers can use RedCoin to buy tokenised money fund units through its banking app, while ownership and settlement remain subject to fund administration."
author: sawinyh
tags: ["Stablecoins", "News"]
date: 2026-11-19T08:28:58+00:00
---

On November 19, 2026, HSBC opened RedCoin-funded access to a tokenised class of HSBC Global Money Funds, Hong Kong Dollar. Its [live product guide](https://www.hsbc.com.hk/investments/products/mutual-funds/guide-to-tokenised-funds/) offers entry from HKD100 through the HSBC HK App, with RedCoin required for subscription and settlement.

The fund uses Ethereum as its initial public blockchain, according to its issuer's terms. Only approved wallets can transact in its tokens. Distributors hold them for investors, and the registrar's off-chain register remains the official ownership record. Secondary trading is unavailable.

Winnie Ng Wing-yee, HSBC Hong Kong's head of wealth and premier solutions, told the [South China Morning Post](https://www.scmp.com/business/banking-finance/article/3375028/hsbc-expands-redcoin-use-wealth-management-tokenised-fund-launch): “By bringing HSBC RedCoin together with tokenised investments, we are creating new ways for our wealth customers to access innovative investment opportunities with a lower entry threshold and a more efficient experience,” the newspaper reported. The investment opening follows [RedCoin's earlier PayMe launch](/hsbc-redcoin-payme-hkd-stablecoin-launch.html).

## What customers buy

The [product key facts statement](https://www.assetmanagement.hsbc.com.hk/api/v1/download/document/hk0001359691/hk/en/product%20key%20facts) describes a money market fund seeking capital preservation, daily liquidity and a return comparable to normal money market rates in its base currency. Capital preservation is an objective, not a guarantee. A fund unit is not a bank deposit. The manager has no obligation to redeem it at its offering value.

The fund must invest at least 70% of net asset value in Hong Kong dollar-denominated short-term deposits and high-quality money market instruments. Eligible issuers include governments, quasi-governments, international organizations, financial institutions and other corporations. The investment policy includes treasury bills, bills of exchange, commercial paper, certificates of deposit and interbank deposits.

The portfolio has maturity limits. Instruments generally cannot have more than 397 days remaining to maturity, with a two-year limit for government and other public securities. Weighted average maturity cannot exceed 60 days, and weighted average life cannot exceed 120 days. The fund will not use derivatives for any purpose.

Tokenised units generally have the same rights as non-tokenised units, subject to exceptions in the explanatory memorandum.

## Public blockchain, controlled ownership

The Hongkong and Shanghai Banking Corporation is the tokenisation agent. Its terms identify Ethereum as the primary blockchain initially. They allow other public blockchains in future if the manager and agent consider their security resilience and distributed ledger technology comparable. This infrastructure description comes from the issuer; the deployed contracts have not been independently verified here.

The agent uses whitelisting to restrict transactions to registered digital wallets. Smart contracts enforce its policies and procedures, blocking transactions between unknown persons or unknown wallets even though Ethereum itself is permissionless. The manager currently has no intention of allowing peer-to-peer transfers or trading of the tokenised units on secondary markets.

Eligible distributors hold the relevant wallets through their appointed token custodians as nominees for end-investors. The token holder is an intermediary acting for the customer. The fund records transactions on-chain, but cash settlement for subscriptions and settlement finality remain off-chain. The registrar maintains the official register of unitholders.

HSBC's app guide describes payment, order confirmation and unit issuance as happening together in a single transaction. The fund keeps separate legal and operational records alongside that app workflow. Its terms determine which record establishes ownership and when settlement is final.

The agent can also correct errors or unauthorized transactions. After consulting the trustee and manager, it can append correct transaction history to the blockchain. Earlier transactions remain in the chain's history. For lost or stolen tokens, the terms provide for immobilising and burning them, then reissuing equivalent tokens to the relevant investors.

The manager controls the response to a blockchain fork. It has sole discretion to choose which resulting network continues to support the tokenised units and which is discontinued. It must consult the tokenisation agent and, when the off-chain register is affected, the trustee. It must also act in investors' best interests.

The manager, agent and distributors keep investor identifying information separately, out of public view. The facts statement warns that a leak of this data could allow someone to determine an investor's identity and investment history in the fund.

The issuer also warns that tokenisation contracts may contain coding errors capable of causing token losses, unauthorized operations or system failures. Contract upgrades can introduce vulnerabilities or interrupt service temporarily. Dependencies on external contracts or protocols add security risks, and token standards may have limitations that affect token operations.

## Dealing windows, fees and withdrawal risks

Subscriptions and redemptions generally receive the next-determined price by reference to net asset value after a distributor receives a request in good order by 11:00 a.m. Hong Kong time. Distributors may impose earlier cutoffs. Net asset value is calculated, and tokenised unit prices are published, on each dealing day.

Daily liquidity remains subject to the fund's liquidity controls. Selling assets may take time or require a discount, particularly when many market participants seek to liquidate investments. The fund can use pricing adjustments and temporarily suspend redemptions. Investors cannot treat its daily-liquidity objective as an unconditional promise of immediate withdrawal.

Blockchain delays can also hold up proceeds. When transactions cannot be recorded, on-chain and off-chain records may diverge, affecting subscriptions and redemptions. The facts statement warns that investors may receive either units or redemption proceeds late. A distributor's lost or stolen private key can expose investors to misappropriation or prevent access to the associated tokens.

The tokenisation agent currently charges a maintenance fee of up to US$1000 per month per tokenised class. The expense applies at class level; it is not a stated monthly charge per investor. Unitholders must receive at least one month's notice before transaction or processing fees are introduced or agent fees increase, with regulatory approval where required.

The tokenised units also bear network and transaction fees for maintaining, minting and burning tokens. Separately, HSBC's [RedCoin page](https://www.hsbc.com.hk/stablecoins/) lists no current fee for buying, selling or holding the stablecoin, while warning that charges can change. Fund unit expenses still apply under those RedCoin terms.

The documents reviewed do not identify the fund's token contract address, leaving its deployed code and supply unverified here. HSBC says RedCoin's first independent reserve attestation is expected after Q4 2026; the promised report will cover reserve assets' market value and composition.
