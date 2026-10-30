---
layout: blog
title: "Aave Freezes Markets After Binance Security Breach"
url: /aave-freezes-markets-after-binance-breach.html
h1title: "Aave Freezes Markets After Binance Security Breach"
pagetitle: "Aave Freezes Markets After Binance Security Breach"
metadescription: "Aave halted new deposits and borrowing after the Binance incident. Withdrawals and repayments remain available, but borrowers cannot add collateral."
category: blog
featured-image: /images/blog/aave-freezes-markets-after-binance-breach-ogp.png
intro: "Aave froze new deposits and borrowing after the Binance incident while keeping withdrawals and repayments available."
author: sawinyh
tags: ["News", "Lending"]
date: 2026-10-30T03:23:42+00:00
---

Aave froze new deposits and borrowing across its DAO-operated V3 and V4 markets on October 29, 2026, after reports of a security incident affecting Binance-affiliated wallets. In its [initial statement](https://x.com/aave/status/2115937863162339637), Aave said its contracts were unaffected and positions remained overcollateralized. Withdrawals and repayments stayed available.

The restriction also blocks borrowers from adding collateral. The [incident response account on Aave's forum](https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954) says that, while reserves remain frozen, repaying debt is the available way to improve a position's health factor. Liquidations continue. Borrowers cannot rely on the usual alternative of depositing more collateral to protect a position during a price decline.

## What the freeze permits

No market was paused, according to the response account. A freeze stops new supply and borrowing, including transactions from the exploiter, while leaving existing users able to repay and withdraw. The same restrictions apply to ordinary depositors attempting to add funds to a frozen reserve.

Withdrawals depend on available liquidity. Aave's [withdrawal documentation](https://aave.com/help/supplying/withdraw-tokens) says suppliers can withdraw the underlying assets and accrued interest only when enough liquidity remains in the pool. Assets already borrowed are unavailable for withdrawal until liquidity returns. The interface asks users to check available liquidity before submitting the transaction.

Collateral places another constraint on withdrawals. The documentation says that supplied tokens supporting an active borrow position may require a partial repayment or additional collateral before withdrawal. The incident restriction removes the additional-collateral option for frozen reserves. A borrower seeking to withdraw pledged assets has to account for the remaining debt as well as the amount displayed under supplies.

Aave's [repayment documentation](https://aave.com/help/borrowing/repay-tokens) permits full or partial repayment through protocol contracts or a frontend. A confirmed repayment reduces debt and improves the health factor; fully repaying a borrow position releases its collateral for withdrawal or other uses. Repayment and withdrawal remain separate actions with their respective conditions.

The repayment workflow also requires the correct token authorization. For non-base tokens, the documentation says the Aave Pool may need approval to transfer tokens from the wallet. An approval can take the form of a transaction, which incurs a network fee, or a signature, which does not. Users select the borrowed token under the dashboard's borrowing section and confirm the repayment in their wallet.

Aave's [liquidation rules](https://aave.com/help/borrowing/liquidations) allow liquidation when a position's health factor falls below 1. The documentation allows up to 50% of total debt to be liquidated when the health factor is above 0.95 and both collateral and debt are worth at least $2,000 each. It allows up to 100% when the health factor is 0.95 or below, or either side of the position is worth less than $2,000.

The liquidator receives collateral equal to the repaid debt plus a liquidation bonus. Partial liquidations must leave at least $1,000 each in collateral and debt; otherwise, the position must be cleared fully under the documented dust rule. A borrower can still lose collateral to liquidation while new borrowing is frozen.

## Why responders froze markets broadly

The response account describes a joint war room involving Aave Labs, TokenLogic and Certora. Its rationale for freezing across markets was that the exploiter could swap stolen funds into any listed asset. Restricting only the originally stolen tokens would have left other assets available for new supply and borrowing.

Responders also considered how they would reverse the restrictions. According to the account, the guardian can reverse a freeze, whereas cutting supply and borrow caps would have required a governance vote and about five days to restore. The freeze gave responders a faster reversal path, without tying reopening to that governance timetable.

Aave Labs' engineering team helped prepare and simulate the freeze transactions before they were proposed to guardian multisigs for signing and execution. The response account describes a coordinated operation across networks.

Horizon was the exception. The account says its RWA market remained open because all its collateral is permissioned and could not be used by the exploiter. That is the market involved in the site's earlier coverage of [Chainlink's weekend RWA pricing with Aave Horizon](/chainlink-24-7-weekend-rwa-pricing.html). The response attributed the exemption to collateral access restrictions.

## Binance's investigation and the reopening conditions

Binance's [security incident update](https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7) described a preliminary investigation into a potentially compromised DevOps engineer's laptop. The exchange said that access may have allowed an attacker into a service container to submit unauthorized withdrawal transactions. Binance reported finding no evidence of a wallet private-key leak and said a technical postmortem would follow once the investigation and verification were complete.

The exchange temporarily suspended deposits and withdrawals during security checks, revoked the affected address authorization and engaged law enforcement and blockchain intelligence partners to trace and recover funds. Those exchange-level transfer restrictions are separate from Aave's reserve freeze, under which withdrawals remain permitted subject to liquidity and collateral requirements.

Binance said it would cover losses using its SAFU fund and company funds. It also committed to publishing an updated Proof of Reserves after remediation. The exchange described its explanation of how the breach occurred as an initial finding.

Aave's response account says responders are following the exploiter's wallet cluster on Ethereum, Arbitrum, Optimism and Avalanche, watching for interactions with Aave and monitoring the Chainlink feeds used by the protocol. It also identifies utilization as a reopening consideration: without new supply, large withdrawals can push utilization and borrow rates higher, while repayments bring them down.

The stated plan is a staged unfreeze coordinated with Aave Labs and other service providers. Markets are to remain frozen until the exploiter's funds stop moving and responders obtain more clarity on containment from Binance. The response account gives no fixed reopening date.
