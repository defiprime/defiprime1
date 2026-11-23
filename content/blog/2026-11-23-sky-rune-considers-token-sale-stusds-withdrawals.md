---
layout: blog
title: "Sky cofounder considers $SKY sale as stUSDS withdrawals stall"
url: /sky-rune-considers-token-sale-stusds-withdrawals.html
h1title: "Sky cofounder considers $SKY sale as stUSDS withdrawals stall"
pagetitle: "Sky cofounder considers $SKY sale as stUSDS withdrawals stall"
metadescription: "Rune Christensen is exploring an institutional $SKY sale to repay borrowing as stUSDS depositors face unavailable withdrawals and debate a recovery plan."
category: blog
featured-image: /images/blog/sky-rune-considers-token-sale-stusds-withdrawals-ogp.png
intro: "Sky cofounder Rune Christensen is exploring an institutional sale of $SKY to repay borrowing as stUSDS withdrawals remain unavailable, according to his statement."
author: sawinyh
tags: ["News", "Stablecoins"]
date: 2026-11-23T18:23:13+00:00
---

On November 23, Sky cofounder Rune Christensen said he was exploring a sale of $SKY to institutional investors to repay his borrowing. He acknowledged that his positions had contributed to unavailable stUSDS withdrawals. His [statement](https://x.com/RuneKek/status/2124860307998732354) names no buyer, agreed price or completion date for the possible sale.

"This is on me," Christensen wrote. He said he had borrowed without properly considering "what happens if rates spike" and apologized to depositors. He pointed to a broader proposal from governance participants and promised updates at least every 48 hours, including when there was no new development. He gave no deadline for restoring withdrawals.

The affected stUSDS depositors supply capital for borrowing against staked $SKY. The protocol's documentation describes their deposits as insurance funds and warns that borrowers can consume all available withdrawal liquidity. The value represented by a depositor's shares and the amount available for immediate redemption are calculated separately.

## What depositors can redeem

Sky's [stUSDS implementation documentation](https://raw.githubusercontent.com/sky-ecosystem/stusds/master/README.md) says the system segregates the risk capital backing staked-$SKY loans. Depositors bear stake-engine bad debt and governance risk alongside their exposure to the asset they supplied. Their funds back the borrowing mechanism.

The system calculates withdrawable funds by subtracting existing stake-engine debt and $USDS in auctions from the pool's total value. It disregards the liquidation penalty in the auction calculation. A depositor can therefore hold stUSDS shares representing more value than they can immediately withdraw. Existing debt continues to restrict withdrawals until the accounting changes.

The [official chainlog](https://chainlog.skyeco.com/api/mainnet/active.json) lists separate addresses for the stUSDS proxy and its implementation. At Ethereum block 26,479,570, a pinned reading of the [proxy contract](https://etherscan.io/address/0x99cd4ec3f88a45940936f469e4bb72a2a701eeb9) returned a supply of 145,466,817.508955 stUSDS shares. That checks the deployed token and its share supply. It does not measure available $USDS liquidity or verify Christensen's individual loan balances.

Governance-appointed operators configure supply and borrowing rates through the Rate Setter, subject to security restrictions. The component also controls the supply cap and maximum debt ceiling within limits set by governance. Participants discussing how to restore liquidity can propose changes to those parameters.

Governance has more extensive powers over deposited funds, too. The documented `cut` function was designed to slash $USDS when the stake engine recognizes bad debt, but authorized governance can call it directly. Depositors can bear an allocated loss as well as a wait to withdraw. The documentation establishes those powers; it provides no evidence of a new slashing operation in this incident.

Third-party integrations receive a specific warning in the documentation: an inability to redeem instantly, or slashing from bad debt, can cause devaluation in other markets. Depositors may sell a share on a secondary market instead of redeeming it through the protocol. The warning describes the design's risks, and the pinned share-supply reading gives no price at which that secondary-market exit could execute.

The implementation also differs from the debt-ceiling Instant Access Module used elsewhere in the system. Deposit and withdrawal code can change the borrowing ceiling up to the permitted maximum without that module's pacing. The documentation warns that debt can expand quickly under this design. Depositors also bear the risk of an oracle reporting an excessively high collateral price.

The Rate Setter has no separate pacing mechanism for changes to its cap and debt-ceiling settings. It relies on maximum values and rate-adjustment steps. The documentation expects operators' off-chain algorithms to account for manipulation attempts and suggests averaged historical utilization and variance in sampling as possible approaches. Those protections depend on operator behavior; the token's share accounting does not guarantee them.

Another documented risk is a race to withdraw before losses are allocated. Depositors who anticipate bad debt or a governance slash may take the available funds first. The documentation warns that this can produce large changes in deposits and prevent losses from being shared more broadly. It describes a potential failure mode, without establishing that particular withdrawals caused the current shortage.

## A proposed rate cut meets repayment conditions

In a [Sky governance forum discussion](https://forum.skyeco.com/t/proposed-stusds-liquidity-and-protection-plan/28465), participant misher proposed fixing the rate at 10%. The author argued that an excessively high interest burden could make repayment less likely. Depositors, misher said, needed confidence that they would recover their principal more than they needed a higher advertised return. The rate cut remains a participant's proposal, not an enacted change.

The plan would also reduce the minimum loan from $30k to $10k to make repayment easier for smaller borrowers and disable further borrowing against $SKY. These changes would address the existing loan structure and new demand for liquidity. The proposed rate adjustment would change what borrowers owe over time.

Misher proposed using monthly Step 2 capital for market purchases of stUSDS until its quoted peg reached 0.98 or higher. The plan presents the purchases as an exit for depositors who need to sell quickly, while allowing Sky to acquire claims at a discount. The discussion leaves both the purchase mechanism and the interpretation of the target open. It supplies no executed transactions.

Forum participant ares supported disabling new borrowing and making market purchases, but opposed cutting rates without repayment obligations. Ares proposed a 20% rate conditional on repayment, with a missed scheduled payment returning the borrower to 50%. These are competing terms proposed in the forum, not rates verified from a live rate-setting transaction.

Under the counterproposal, every borrower in the named stake-engine collateral type would have to follow a weekly or monthly repayment schedule. Ares offered 12 months as an example. Staking rewards from borrowing positions would automatically go toward repayment until the debt was cleared, adding an enforcement requirement to the proposed rate relief.

Ares also asked that repayments reach depositors pro rata or through a queue, instead of going to whichever transaction claimed the available liquidity first. The counterproposal called for public tracking of each large borrower's progress. These conditions would govern how repayments reach depositors as liquidity returns.

Misher replied that the original plan relied on parameter changes and existing code. Individual repayment schedules or penalties enforced on-chain could require additional development and audits, the author said. Misher raised concerns about how long that work would take and the risk of smart-contract bugs. The proposals differ in their implementation requirements as well as their interest rates.

Christensen has not identified an institutional buyer or a completed sale. The forum discussion contains competing repayment conditions but no executed governance transaction establishing a withdrawal-restoration date.
