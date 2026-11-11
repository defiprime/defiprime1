---
layout: blog
title: "Arcus covers $2,234,391 withdrawal exploit after subaccount bug"
url: /arcus-subaccount-bug-withdrawals.html
h1title: "Arcus covers $2,234,391 withdrawal exploit after subaccount bug"
pagetitle: "Arcus covers $2,234,391 withdrawal exploit after subaccount bug"
metadescription: "Arcus says a subaccount accounting bug enabled unauthorized withdrawals, with the treasury covering the shortfall and normal withdrawals restored."
category: blog
featured-image: /images/blog/arcus-subaccount-bug-withdrawals-ogp.png
intro: "Arcus says it covered an unauthorized withdrawal shortfall after a bug inflated one account's balance during transfers between subaccounts."
author: sawinyh
tags: ["News", "DEXs"]
date: 2026-11-11T03:22:14+00:00
---

On November 9, 2026, an accounting bug in Arcus let a newly created account withdraw 2,234,391 USDG against a balance it did not own, according to the exchange's [incident report](https://arcus.xyz/blog/arcus-incident-report-november-9-2026). Arcus says its company treasury covered the shortfall and normal trading and withdrawals have resumed.

The attacker used transfers between subaccounts belonging to the same wallet. Under conditions the report leaves unspecified, the exchange recorded a balance far larger than the account actually held. It then accepted withdrawal requests against that balance. Arcus says the incident involved a single account and left other users' balances, positions and orders unchanged.

The bridge's on-chain rate limit held back another $3M in requested withdrawals. Arcus says those requests were never paid out and were later reversed. The report accounts for the blocked amount separately from the funds that left the platform. Both the loss figure and the treasury reimbursement come from the operator; this article has not independently reconciled the transfers on-chain.

## The rate limit acted before the withdrawal pause

Arcus dates the first exploit activity to around 10:07 p.m. ET on November 9. Its timeline records the bridge rate limit capping payouts at 10:10 p.m., before monitoring flagged the withdrawals at 10:15 p.m. The team then began investigating. At 11:07 p.m., Arcus paused withdrawals across the platform and updated its status page.

Arcus deployed the fix at 11:37 p.m. and blocked the exploiter's addresses from trading, transferring and withdrawing at 11:43 p.m. The platform-wide pause, code fix and account restrictions were separate interventions, in that order.

Withdrawals reopened at 4:26 a.m. ET on November 10. Arcus reversed the exploiter's pending withdrawals at 5:02 a.m., and the company treasury covered the shortfall at 12:28 p.m. In the published sequence, withdrawals reopened before Arcus reversed the outstanding requests or recorded the treasury reimbursement.

The report's opening says the team detected and fixed the bug within one hour. Its detailed timeline puts deployment of the fix at 11:37 p.m., after the 10:15 p.m. monitoring alert. Arcus leaves that discrepancy unexplained. The listed times give the more specific account of when the team intervened.

Arcus says security partners reviewed the fix and related checks across the codebase. It also says it is continuing to improve systems for detecting and mitigating suspicious activity. The report gives no conditions that triggered the incorrect balance and includes no code change. Its root-cause explanation stops at subaccount accounting.

## Internal balances became external withdrawals

Arcus's [subaccount documentation](https://docs.arcus.xyz/concepts/subaccounts.md) describes an account as a wallet address paired with an account index. A wallet can have up to 10 subaccounts. Index 0 is the primary account; the remaining indexes let users separate strategies, books or risk. The feature and internal transfers are currently available through the API, not the web console.

Each index has its own collateral balance, rate-limit pools and volume credit for fee tiering. Positions, orders and free collateral are independent across indexes belonging to the same wallet. The documentation describes these per-subaccount rate limits separately from the bridge withdrawal limit that Arcus credits with holding back the additional withdrawal requests.

An internal transfer moves collateral between different indexes under the same master wallet address. The documented flow has no cross-wallet recipient. Authorization requires a self-signed EIP-712 typed-data signature under the Arcus Transfer domain instead of API-key authentication. That is the intended authorization path in the documentation. The incident report makes no claim that the attacker bypassed a signature check.

The transfer API is asynchronous. A response of 202 Accepted means the request has been validated and queued, with a pending status and a transfer identifier. Clients get the terminal result through the account-transfer updates endpoint or its WebSocket channel and match it to that identifier. If free collateral is insufficient, the documentation says the result should show a rejected transfer.

Internal transfers never settle on-chain, according to the documentation. Funds stay in custody as they move between indexes inside the exchange. In this incident, Arcus says an incorrect internal balance supported withdrawal requests that did reach the chain. The disclosed failure spans the exchange's account bookkeeping and its outward payment flow. The report leaves the exact failed check unidentified.

## What the architecture promises to verify

The [perpetuals architecture documentation](https://docs.arcus.xyz/concepts/exchange-architecture.md) describes an off-chain central limit order book, an appchain and an EVM public rootchain. Matching happens off-chain. The appchain anchors consensus and re-verifies exchange rules, while custody and final settlement sit on the public blockchain. These are the components of the perpetuals system; the documentation explicitly distinguishes spot trading's model.

Arcus describes the appchain validator set as permissioned. Its stated duties include checking acceptable state transitions and re-verifying signatures on orders, withdrawals and oracle prices. On the rootchain, the Bridge Vault holds funds, stores withdrawable balances and honors withdrawals published by the validator set. The incident report leaves unexplained how the incorrect balance passed through those components.

The architecture also includes an emergency-settlement escape hatch intended to prevent withdrawal censorship. That mechanism depends on data availability maintained by the appchain validators. Arcus's incident timeline records an operator pause and subsequent reopening. It reports no activation of the emergency exit.

For deposits, the [onboarding documentation](https://docs.arcus.xyz/concepts/onboarding.md) says funds enter through an in-app flow powered by Fun and settle as $USDG, the protocol's settlement stablecoin. Arcus identifies the same asset in the unauthorized withdrawals. According to its account of the remedy, the company treasury absorbed the shortfall, with no reported reduction in other users' balances.

Arcus says blockchain investigators are helping track the withdrawn funds and that it will coordinate with law enforcement as appropriate. The report gives no recovery total or timetable for a fuller technical disclosure.
