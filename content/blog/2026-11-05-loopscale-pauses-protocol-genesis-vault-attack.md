---
layout: blog
title: "Loopscale Pauses Protocol After Genesis Vault Attack"
url: /loopscale-pauses-protocol-genesis-vault-attack.html
h1title: "Loopscale Pauses Protocol After Genesis Vault Attack"
pagetitle: "Loopscale Pauses Protocol After Genesis Vault Attack"
metadescription: "Loopscale paused activity after attacks on its Genesis vaults. The team says deposits are intact, but repayment functionality was still awaiting restoration."
category: blog
featured-image: /images/blog/loopscale-pauses-protocol-genesis-vault-attack-ogp.png
intro: "Loopscale paused protocol activity after a campaign targeting its Genesis vaults and said repayments were awaiting restoration."
author: sawinyh
tags: ["News"]
date: 2026-11-05T15:31:40+00:00
---

On November 5, 2026, Loopscale [said it had paused protocol activity](https://x.com/Loopscale/status/2118285556123611378) after a sustained attack campaign escalated against its $SOL and $USDC Genesis Vaults. The Solana lending protocol said the affected vaults had been made whole and user deposits had incurred no loss. Repayment functionality was still awaiting restoration when it issued the statement.

The team said malicious requests had targeted its protocol APIs over the preceding week before its security systems detected a significant escalation. It attributed the campaign to a sophisticated actor. The disclosure names the targeted vaults but gives no transaction-level account of how the activity affected them. It also leaves out the amount requiring reimbursement and the source of the funds used to make the vaults whole.

"Affected vaults have been made whole and no user deposits have incurred a loss," Loopscale said. The assurance comes from the operator; an independently verified balance reconciliation is still missing.

## Repayments remain the operational priority

Loopscale said normal operations would resume once it had established the campaign's complete scope and implemented further security hardening. It separately said it would re-enable the protocol interface shortly. The team was working to restore repayment functionality as soon as possible to mitigate unforeseen liquidations, but gave no firm reopening time.

The interface and repayments had separate restoration plans, with neither confirmed available to borrowers at the time of the disclosure. The statement also leaves the treatment of existing loans during the interruption unresolved. That includes whether borrowers will receive any accommodation on positions whose scheduled terms expire while normal operations are paused.

The repayment interruption affects a normal method of reducing liquidation exposure. Loopscale's [loan-management documentation](https://docs.loopscale.com/using-loopscale/borrow/health-and-liquidations.md) says partial early repayments reduce outstanding debt and improve loan health. Full repayment closes the loan and returns the collateral to the borrower. Early repayments include interest accrued up to that point. These mechanics describe normal operation; repayment functionality remained paused when Loopscale issued its notice.

Borrowers can also improve loan health by adding collateral under the documented rules. Loopscale's notice gives no function-by-function account of availability during the pause, leaving it unclear whether borrowers could still use that option. Confirmation of which actions have resumed requires a subsequent operational notice. The ordinary product documentation describes how those actions work, without establishing their availability during the interruption.

## How the lending terms create exposure

Loopscale's [borrowing documentation](https://docs.loopscale.com/using-loopscale/borrow/overview.md) describes isolated, fixed-rate lending markets that match borrowers directly with lenders. A borrower locks eligible collateral and selects an offer based on amount, duration and interest rate. These overcollateralized loans require active management when collateral prices fall: the borrowing rate stays fixed, while the value of the collateral supporting the debt can change.

Loan health depends on current loan-to-value and a lender-set liquidation threshold specific to the collateral asset. The debt value used in that calculation includes principal and the total interest that will accrue over the full term. Under the documented rules, a position becomes eligible for liquidation when its current loan-to-value exceeds the threshold. Loopscale announced no replacement calculation or revised collateral thresholds in its incident statement.

Loans can also reach liquidation through failed refinancing. The [risk disclosures](https://docs.loopscale.com/resources/risks-and-security.md) explain that refinancing pays off an existing loan with an order from the books. Insufficient order-book liquidity, chain congestion or technical failure can prevent that refinancing from going through. If it fails and the loan passes its grace period, the documentation says the loan will be liquidated. The incident statement does not identify any of these disclosed failure modes as having occurred during the pause.

During liquidation, the documented process first attempts a partial sale of collateral sufficient to bring the loan back below its maximum loan-to-value. If the remaining collateral cannot restore a healthy position, the protocol sells the minimum amount needed to repay the lender fully. Any collateral remaining after fees returns to the borrower. Loopscale reported no completed liquidations arising from the pause in its statement.

Oracle inputs are another source of premature liquidation or bad debt identified in the risk disclosures. A loan's connected oracle is established in the initial order, and the team determines the connected oracles used across Loopscale loans. Manipulated or incorrect inputs can falsely increase or decrease asset values. The documentation tells users to assess oracle safety, liveness, centralized control, precision and update frequency when evaluating exposure. The November disclosure identifies malicious API traffic without attributing the campaign to an oracle failure, so its mechanism remains unresolved.

## Genesis vaults and the Formation parent

Loopscale's [archived Genesis risk framework](https://docs.loopscale.com/partners/archived/genesis-risk-framework.md) describes the Genesis Vaults as managed lending vaults designed and curated by its core team. The archive identifies the products named in the incident notice. It is not a current on-chain reading of the vaults' allocations or risk parameters.

The framework describes credit risk as isolated by vault. Under its default-handling model, the difference between loan principal and recovered collateral value reduces the affected vault's net asset value. Depositors absorb those losses proportionally, and withdrawals pause during resolution. Loopscale says the vaults targeted in this incident were made whole, but has not explained whether it invoked the archived default process or how it settled any shortfall.

Before the incident, [Orca and Loopscale merged as Formation](/orca-loopscale-merge-as-formation.html), a transaction Defiprime previously covered. Loopscale's [Formation documentation](https://docs.loopscale.com/resources/formation.md) says both brands continue as products under the combined company. Its merger FAQ says the transaction left Loopscale's programs, upgrade authority, multisig setup and risk controls unchanged.

The incident notice names Loopscale's Genesis Vaults, with no Orca product identified as affected and no basis given for extending the scope to other Formation services. Loopscale says it is engaged with federal law enforcement and security professionals and will share material updates. It has not published a firm repayment-restoration time or the transaction-level reconciliation behind its assurance that the affected vaults were made whole.
