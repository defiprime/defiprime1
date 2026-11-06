---
layout: blog
title: "Coinbase Adds PAX Gold Collateral for USDC Loans"
url: /coinbase-paxg-gold-backed-usdc-loans.html
h1title: "Coinbase Adds PAX Gold Collateral for USDC Loans"
pagetitle: "Coinbase Adds PAX Gold Collateral for USDC Loans"
metadescription: "Coinbase opens USDC borrowing against PAX Gold through Morpho on Base, with variable rates and liquidation risk for eligible US customers outside New York."
category: blog
featured-image: /images/blog/coinbase-paxg-gold-backed-usdc-loans-ogp.png
intro: "Coinbase has opened borrowing against tokenized gold for eligible customers in the United States, with Morpho handling the loans on Base."
author: sawinyh
tags: ["Lending", "News"]
date: 2026-11-06T16:26:19+00:00
---

On November 6, 2026, Coinbase [opened $USDC borrowing against PAX Gold](https://x.com/coinbase/status/2118727681886105975), bringing tokenized gold into its Morpho-powered lending interface on Base. Holders can pledge $PAXG to borrow stablecoins without selling their gold position. They take on variable-rate debt and risk having their collateral liquidated.

Coinbase's [legal reply to the announcement](https://x.com/coinbase/status/2118730034105991551) limits the launch to eligible United States customers outside New York. Availability and terms depend on jurisdiction, eligibility and market conditions. The announcement names Morpho and Base but gives no starting interest rate, collateral address, market identifier or liquidation threshold.

## What the borrower signs up for

Coinbase provides the interface to Morpho, according to its [DeFi Borrow introduction](https://help.coinbase.com/en/coinbase/trading-and-funding/loan/loan-intro). Its general variable-rate loan documentation describes loans with no set term, minimum payment or due date. Borrowers can repay partly or fully at any time. The gold launch specifies variable rates. The broader help center also describes fixed-rate options, but does not confirm their availability for gold loans.

The public collateral list names Bitcoin, Ethereum, Solana and several other assets. It does not yet name $PAXG. Availability is established by the official launch posts, while the general help pages describe the borrowing interface and its risks. Those pages have yet to publish the gold-specific limits a borrower would need to check.

The [setup instructions](https://help.coinbase.com/en/coinbase/trading-and-funding/loan/loan-setup) direct borrowers to review the processing fee, risk disclosure and total loan before confirming. The app displays the rate and borrowing limit for the selected collateral. Borrowers can check the offered terms in that preview before committing. Once the transaction processes, the proceeds enter the customer's $USDC balance.

Coinbase's [fee documentation](https://help.coinbase.com/en/coinbase/trading-and-funding/loan/fee) says it adds a processing fee to principal each time a customer borrows, including when they increase an existing loan. A platform fee may also apply. Interest accrues on the processing fee as part of the loan balance, so the recorded debt can differ from the amount the borrower receives.

Coinbase's [onchain integration terms](https://www.coinbase.com/legal/onchain-integration/terms-of-service) restrict how borrowers can spend the proceeds. They prohibit using these loans to purchase digital assets through its website, APIs, mobile app or other Coinbase websites. The same terms say that, unless explicitly stated otherwise, neither the contracting Coinbase entity nor another Coinbase Group member is the lender. Access requires a self-custodial Smart Wallet.

## Liquidation depends on the selected market

Coinbase's [collateral guide](https://help.coinbase.com/en/coinbase/trading-and-funding/loan/collateral) says Morpho locks collateral when a loan opens and returns it automatically after full repayment of debt, fees and accrued interest. Coinbase continues to include locked collateral in the customer's displayed total balance without deducting the debt. That displayed balance is not the account's value net of its loan.

The [loan-health documentation](https://help.coinbase.com/en/coinbase/trading-and-funding/loan/loan-health) measures loan-to-value against the collateral's current market value and includes unpaid interest in the debt. A falling gold-token price can push the ratio upward. Accruing interest or further borrowing can also raise it while collateral value stays unchanged. Repaying debt or adding collateral can bring the position further below its liquidation threshold.

Coinbase says liquidation loan-to-value varies by collateral asset. It directs customers to the loan management page for the threshold that applies to their position. The gold launch posts give no such figure. A Bitcoin threshold published on another Coinbase borrowing page describes the terms for that asset; it cannot supply the missing threshold for a $PAXG-backed loan.

The general loan-protection feature can automatically add collateral when a position reaches a trigger. Coinbase says borrowers must enable it for each loan and re-enable it after use. If available funds are insufficient, the top-up may execute only partly or fail altogether. Market volatility and technical issues can also prevent execution, so enabling the feature does not guarantee protection from liquidation.

Morpho's [variable-rate market documentation](https://docs.morpho.org/learn/concepts/blue/) describes isolated pools that pair a collateral asset with a loan asset. Each pool's parameters are fixed at creation, including its liquidation threshold, price oracle and interest-rate model. Defiprime previously covered this structure in [Lido Lend's use of Morpho Blue](/lido-lend-morpho-blue-isolated-markets.html). The market page exposes the oracle and rate-model addresses for inspection.

Once a position exceeds its liquidation threshold, Morpho allows anyone to repay part of the debt in exchange for discounted collateral. Its [borrowing guide](https://help.morpho.org/en/articles/12166187-borrow-product-variable-rate-markets-morpho-blue) warns that a manipulated oracle can cause liquidation or bad debt. That oracle supplies the posted asset's value against the debt asset. The token's physical gold backing does not establish the reliability of the price feed used to value it.

Morpho's variable-rate model adjusts borrowing costs independently for each market according to utilization, the ratio of borrowed assets to supplied assets. Its guide says collateral is not rehypothecated by default. It earns no supply APY because the protocol does not lend it to other borrowers. A borrower posting collateral therefore receives no lending interest on those assets.

## What backs the gold token

[Paxos describes $PAXG](https://www.paxos.com/pax-gold) as ownership of physical gold in its custody. Each token is backed by one fine troy ounce stored in London LBMA vaults, and its value follows the underlying metal's market value. Borrowers remain exposed to gold prices while their loan also carries the lending market's interest costs, oracle risk and liquidation terms.

Paxos offers a gold-allocation lookup that shows the bar serial number, weight and vault information. The issuer specifies that the tool covers holdings in onchain Ethereum and Solana wallets, excluding custodial exchanges and wallets. Its redemption routes include dollars and, for institutional customers, unallocated Loco London gold. Paxos provides those issuer services separately from Coinbase's borrowing interface.

Paxos currently charges no gold storage fee, according to its [fee schedule](https://support.paxos.com/articles/2899561282-pax-gold-fees). Its creation and redemption charges apply to conversions through a Paxos account, including conversions involving dollars, gold bars or unallocated gold. Purchases and sales outside the Paxos wallet are exempt from those charges. The issuer's fees are separate from the processing fees and interest a customer pays to borrow against the token.

Neither Coinbase launch post identifies the Base collateral contract or Morpho market used for the gold loans. The posts also leave the $PAXG-specific liquidation threshold and offered borrowing rate undisclosed; Coinbase's help center directs borrowers to their loan overview for the applicable terms.
