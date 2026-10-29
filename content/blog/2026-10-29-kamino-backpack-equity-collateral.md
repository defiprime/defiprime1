---
layout: blog
title: "Kamino opens Backpack equity collateral market"
url: /kamino-backpack-equity-collateral.html
h1title: "Kamino opens Backpack equity collateral market"
pagetitle: "Kamino opens Backpack equity collateral market"
metadescription: "Kamino adds Backpack tokenized equities as collateral for USDC loans, with Allez Labs risk settings and an oracle that holds prices during market closures."
category: blog
featured-image: /images/blog/kamino-backpack-equity-collateral-ogp.png
intro: "Kamino opened an isolated Backpack equity market for eligible borrowers, with redemption routed through Backpack accounts."
author: sawinyh
tags: ["News"]
date: 2026-10-29T03:26:01+00:00
---

On October 28, 2026, Kamino opened the Backpack Market on Solana, letting eligible holders borrow $USDC against Backpack Securities tokenized equities. The [launch announcement](https://kamino.com/blog/kamino-integrates-backpack-securities-tokenized-equities) describes tokens backed 1:1 by underlying shares, with redemption through an eligible Backpack account.

Borrowers can initially pledge tokenized Micron ($MU), SK Hynix ($SKHY), SpaceX ($SPCX) and SanDisk ($SNDK), according to Kamino's [launch thread](https://x.com/kamino/status/2115467810541609016). Allez Labs sets the risk parameters for these assets. Borrowers keep their exposure to the shares while borrowing against them, and the tokens they deposit as collateral remain subject to liquidation.

Kamino says around $50 million in tokenized equities had been supplied to its lending protocol as of October 2026. That figure covers equity collateral across Kamino, not deposits in the new Backpack Market. Backpack joins the protocol's existing tokenized-equity business, but the release gives no separate balance for the market at launch.

## Lending stays open when the price feed stops

The Backpack Market has its own reserves and risk settings. Kamino describes it as isolated: bad debt or liquidity shortfalls in other Kamino markets do not pass through to it. Each listed equity has separate loan-to-value, liquidation and borrow-cap parameters based on its liquidity and oracle coverage. The announcement does not give the numerical settings for any of the individual collateral assets.

Users can deposit, borrow, repay and withdraw around the clock, Kamino says. Equity price updates follow U.S. trading sessions, however. During market closures, including weekends and U.S. market holidays, the oracle holds the last published price until trading resumes. Lending operations stay open through those closures, with the collateral price feed waiting for the underlying market to reopen.

Kamino's [disclaimer](https://x.com/kamino/status/2115467476603433108) warns that tokenized-equity borrowers face liquidation risk even when the underlying share markets are closed. It also identifies oracle and smart-contract risk in isolated markets. The oracle's use of the last published price during a closure gives borrowers no assurance that their loans will be protected from liquidation while share trading is closed.

The market manager is responsible for lending settings. Kamino says it neither manages nor guarantees third-party managers' parameters or risk decisions, and explicitly includes Allez Labs in that disclaimer. Kamino supplies the lending infrastructure. Backpack's securities arm issues the collateral tokens; Kamino says it does not issue, sell, custody or redeem those instruments.

## Backing and redemption take different routes

Backpack describes the underlying holdings in the release as security entitlements under New York UCC Article 8. RQD Clearing, LLC and Atomic Vault Securities, LLC clear and custody them. According to Backpack, both firms are SEC-registered and members of FINRA and SIPC, and customer securities are kept separate from the company's creditor claims. Those representations concern the holdings backing the tokens.

To redeem tokens, a holder deposits them into an eligible Backpack account. Backpack says eligible account holders can redeem 1:1 for the corresponding share, subject to its terms. Dividends are reinvested into additional tokenized shares and credited to the holder's wallet. For splits and other corporate actions, the release describes a multiplier on the token mint rather than a separate manual claim.

The protections for the underlying securities stop short of covering the lending position. Kamino says they do not cover tokens deposited on its protocol, smart-contract risk or liquidation losses. Backpack's [issuer risk disclosure](https://drive.google.com/file/d/1Bw7oNVFsrqu8SE41-xAIJfPJnhdNnNms/view), linked from its securities terms, separately says the tokens have no public compensation-scheme or private insurance coverage. The issuer provides no insurance for token losses.

That disclosure names Trek Nexus Markets Ltd, a company incorporated in the British Virgin Islands, as the token issuer. It also sets conditions for obtaining rights directly from the issuer. Before exercising beneficiary rights, an on-chain token holder must appear in the company's internal beneficiary register and satisfy its know-your-customer and transaction-screening requirements. Those conditions apply to redemption, distributions and instructions. Possessing tokens in a wallet alone is insufficient to exercise those rights.

## What the issuer terms require off-exchange

A recipient who withdraws tokens from Backpack Exchange into a self-hosted or third-party wallet becomes the on-chain holder for blockchain transfer purposes, the disclosure says. That transfer does not automatically confer beneficiary status with the issuer. In the ordinary course, the issuer recognizes Trek Forge Ltd, an exchange affiliate, or its designated nominee or custodian as the beneficiary entitled to request redemption and receive the proceeds.

The same document describes a contingency process for exercising beneficiary rights directly. Possible triggers include insolvency, delisting or a prolonged suspension of Backpack Exchange. After a trigger, the holder must pass compliance checks and meet evidentiary requirements, and the issuer must update its internal register. The disclosure warns that a contingency may never occur. Ordinary redemption under the launch terms still requires a deposit into an eligible Backpack account; a Solana wallet holder has no unconditional direct claim.

Eligibility restrictions apply before holders can bring a position to the lending market. The issuer disclosure says tokens may not be offered or sold to U.S. citizens, residents or entities. It also excludes jurisdictions where holding or transfer is prohibited or requires registration. Kamino describes access for eligible holders rather than unrestricted access to the underlying equities.

The issuer makes no commitment to maintain a secondary market or ensure token liquidity or value. Its disclosure says trading venues may be limited or absent, and liquidity can fall substantially or disappear. Users also bear the risk of using third-party platforms, wallets and exchanges. The issuer disclaims responsibility for operational, regulatory, technological or fraud losses through those services.

Kamino expects additional tokenized equities as Backpack expands its supported assets. The launch announcement names no further collateral tokens or listing dates.
