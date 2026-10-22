---
layout: blog
title: "Base packages stablecoin yield and crypto-backed loans for apps"
url: /base-packages-stablecoin-earn-and-crypto-loans.html
h1title: "Base packages stablecoin yield and crypto-backed loans for apps"
pagetitle: "Base launches Earn & Borrow for app developers"
metadescription: "Base Earn & Borrow lets apps offer variable stablecoin yield and crypto-backed loans through third-party lending markets on Base."
category: blog
featured-image: /images/blog/base-packages-stablecoin-earn-and-crypto-loans-ogp.png
intro: "Base has introduced an integration stack that lets platforms put stablecoin yield and crypto-backed borrowing inside their own apps."
author: sawinyh
tags: ["News"]
date: 2026-10-14T06:21:48+00:00
---

On October 13, 2026, [Base introduced Earn & Borrow](https://x.com/base/status/2110054191419027932), an integration stack for platforms that want to offer stablecoin yield and loans against customers' crypto. The product page puts the launch against more than $3B supplied across tracked Base lending protocols and a 4.45% average yield for USD stablecoins before incentives. Base says those market figures use 28-day average balances as of October 1.

Earn & Borrow is infrastructure for other businesses rather than a single vault run by Base. [The product page](https://www.base.org/earn-borrow) says platforms use Base infrastructure and third-party lending markets to serve eligible customers. Each integrating platform chooses its wallet and custody model. The underlying deposits, loans, repayments and liquidations are recorded onchain.

## How the earn side works

A customer starts by depositing a supported stablecoin in an app. Base names $USDC as one example and says supported assets vary by market. The deposit then earns a variable rate from borrowers across lending markets on Base. A customer can withdraw and stop earning when liquidity and the protocol's terms allow it.

The source of yield is lending demand, not a fixed rate from Base. Optional vaults supply deposits to lending markets, while borrowers pay interest on overcollateralized loans. Base describes that interest as the main source of yield. Deposits can also go directly to a lending protocol instead of passing through a vault.

The stack separates several decisions that an app may otherwise have to assemble itself. A wallet holds customer assets and signs transactions. The integrating platform selects that wallet and its custody model. An independent curator chooses the markets used by a vault and sets the vault's risk limits. Base supplies the network where the resulting activity is recorded.

Base lists Morpho and Aave as examples of lending protocols in the stack. It also says those names are examples rather than endorsements and discloses commercial relationships with both protocols. [Aave separately confirmed](https://x.com/aave/status/2110099293671440563) that it is available through Earn & Borrow. The Aave statement says businesses building on Base can use the stack to offer stablecoin yield and loans powered by Aave. Base's page does not say that every named market or vault is available to every app or customer.

## What the borrowing side changes

The borrowing flow lets a customer request a loan against crypto already held in an integrating app. The customer receives $USDC, while the collateral moves onchain and backs the loan. Base says the product has no repayment schedule or deadline. The customer can repay and recover the collateral, subject to the terms set by the product and protocol.

For an app operator, that creates a second use for assets already held on the platform. Base says a business may earn from eligible stablecoin balances or charge fees on loans against customer assets. The operator does not get to treat the lending layer as a black box, however. Its choice of wallet, custody model, protocol and any curator determines how customer funds reach the market and which risk limits apply.

For a depositor, the app interface does not remove protocol exposure. Base says lending and borrowing through third-party protocols can involve smart contract failure, oracle errors, liquidation, stablecoin depegs and loss of funds. Rates, fees, withdrawals, loan terms, liquidation rules, eligibility and availability can vary by protocol, curator, platform and jurisdiction. None is guaranteed by the launch page.

Liquidity is a direct constraint on the earn side. Base says customers can withdraw subject to available liquidity and protocol terms. A platform therefore needs to show which market or vault holds a deposit, who curates it, how the variable rate is formed and what happens when many users seek liquidity at once. The branded app remains the customer's front end, while the lending market governs the financial outcome.

The same separation affects how an advertised rate should be read. Base reports an average across tracked markets and says customer deposits earn a variable rate. It does not promise that an integrated app will deliver the reported 4.45% average, because the selected market, vault, curator and available liquidity can differ. A platform may also send deposits directly to a protocol. Users therefore need the product-specific route, not just the Base network name, to understand where yield comes from and which withdrawal terms apply.

Borrowers face a parallel dependency. The stack can put the request and repayment flow inside an app, but the collateral still moves onchain and the loan remains governed by protocol terms. The absence of a repayment schedule does not remove liquidation risk. Base explicitly includes liquidation and oracle errors among the risks of third-party lending. An operator that offers the borrowing flow needs to expose the collateral terms that determine when the protocol can liquidate a position.

## What is live and what is still open

Base says its tracked lending markets had more than 200,000 lenders and more than 115,000 borrowers alongside the supplied-balance figure. Those figures describe the wider set of tracked Base protocols, not deposits made through the new stack. They show the markets into which Earn & Borrow can route users, but they are not adoption figures for Earn & Borrow itself.

Aave's confirmation identifies one protocol available through the stack. Base also presents Morpho as an example and says vaults are operated by independent curators. Base and Coinbase do not curate, manage or guarantee any vault. That distinction matters because an app can use Base's packaging while its customers remain exposed to decisions made elsewhere.

The next useful disclosure will come from the platforms that integrate the stack. Their launch terms will determine the supported collateral, selected markets, curator, custody model, fees, withdrawal conditions and jurisdictions. Until those details arrive, Earn & Borrow defines an integration path, while each app still determines the product its users actually receive.
