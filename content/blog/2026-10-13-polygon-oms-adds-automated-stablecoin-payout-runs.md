---
layout: blog
title: "Polygon OMS adds automated stablecoin payout runs"
url: /polygon-oms-adds-automated-stablecoin-payout-runs.html
h1title: "Polygon OMS adds automated stablecoin payout runs"
pagetitle: "Polygon OMS adds automated stablecoin payout runs"
metadescription: "Polygon OMS now lets payment teams automate stablecoin payout runs under recipient, budget, expiry and revocation rules enforced by the wallet."
category: blog
featured-image: /images/blog/polygon-oms-adds-automated-stablecoin-payout-runs-ogp.png
intro: "Polygon Labs introduced automated stablecoin payout runs for Open Money Stack with recipient, budget and time controls enforced by wallet permissions onchain."
author: sawinyh
tags: ["Stablecoins", "Payments", "News"]
date: 2026-10-13T07:17:53+00:00
---

Polygon Labs [introduced automated stablecoin payout runs](https://polygon.technology/blog/automated-stablecoin-payout-runs) for Open Money Stack on October 12, 2026. A team approves the recipient scope, payment budget and run window once, then its product can request payments during that window without collecting a new signature for every transfer.

The launch announcement does not name a contract deployment, a launch time or a live payout amount. Polygon presents the feature as an OMS wallet workflow whose limits are recorded and checked onchain. That distinction matters for operators assessing what authority a payout service receives over treasury funds.

## How the payout rule works

A team first defines who can be paid, how much the program can spend and the dates during which the rule is active. Polygon says the product sends payout requests when the cycle opens. The wallet checks each request against the approved recipient scope, budget and time window before allowing it.

The permission is scoped more narrowly than control of the wallet. Polygon says teams define the contracts and methods that the permission may call, along with a maximum token amount and an expiry. The wallet records those terms in its onchain Sessions Module. Each request is checked there when it executes.

This separates request generation from authorization. A backend can submit the transfers needed for a payout cycle, but it cannot widen the recipient scope after approval. It also cannot increase the spending limit or extend the expiry. A request outside the approved terms is rejected at the wallet contract.

The contract and method restrictions add another boundary. The permission can be limited to the calls needed for the payout workflow instead of granting a service unrestricted access to every action the wallet supports. Recipient scope limits destinations, while the token maximum limits value. The expiry closes the permission after the approved period. Each setting covers a different failure mode, so reviewing only the total budget would miss part of the authorization.

A request still has to reach the wallet for evaluation. Polygon describes the product as the sender of payout requests and the wallet as the component that decides whether each request fits the rule. An unavailable backend could therefore delay a run even though it could not change the approved terms. The announcement does not specify retry behavior, request ordering or how partial runs are reconciled.

Teams can revoke an active rule. Polygon says turning it off stops the next payout request, which gives operations staff a way to halt future payments without waiting for the approved window to expire. The announcement does not describe whether revocation affects a request already executing or how quickly an operator interface reflects the onchain change.

The feature removes a signature from each individual transfer, not from initial authorization. The team still approves the payout rule before the run. Its product can then send requests during the approved period, subject to the checks stored with the wallet.

## What changes for payment operators

The immediate use case is a repeating payment cycle. Polygon lists marketplace seller settlements, contractor payments, creator revenue shares, customer rewards and partner commissions. In each case, an operations team can prepare the recipient and spending boundaries ahead of the run while keeping the workflow in its existing product interface.

For treasury operators, the main control is the upper bound on what the automation can do. The server running a payout cycle receives permission to request only approved actions. The wallet remains responsible for enforcing recipient, amount and expiry constraints. Compromise of the payout service should therefore leave the attacker constrained by the active rule, provided the permission was configured as Polygon describes and the wallet contracts behave as specified.

Configuration becomes part of the risk review. An overly broad recipient scope, token limit, contract list or expiry would still authorize a larger set of transfers. Teams need to inspect those terms before approval and test that an out-of-scope request is rejected. They also need an operational path to revoke the rule if a recipient list changes or the payout service is compromised.

The announcement says the active rule lives in the wallet rather than only in the service running the payout cycle. This means the backend cannot rewrite its authority after the team has approved it. The same design also makes the wallet configuration the record that security reviewers need to examine.

## Where the feature sits in OMS

Polygon positions the payout run inside a larger money flow. OMS can connect incoming local currency, stablecoin balances, payout controls, routing and settlement through one integration. The automated run governs the point where a product requests transfers from the held balance to approved recipients.

The release is about authorization and orchestration rather than a new stablecoin. Polygon says stablecoins provide the common rail, while OMS handles bringing money in, holding balances, applying payout terms and routing funds onward. Availability can still depend on jurisdiction, integration choices and the stablecoin or settlement path selected by the operator. Polygon's announcement says the examples are subject to applicable law and may not be available in every jurisdiction.

Polygon has not published a named customer, production volume or contract address for automated payout runs in the announcement. Those omissions limit independent verification of live usage. Operators can review the permission model and wallet configuration, but the post does not provide a deployment identifier that would let them trace a production run from the launch page alone.

The next verifiable milestone is a public deployment or customer transaction that exposes the wallet, permission configuration and execution path. Until then, the open question is how OMS implements these controls in production integrations and what monitoring operators receive when a request is rejected or a rule is revoked.
