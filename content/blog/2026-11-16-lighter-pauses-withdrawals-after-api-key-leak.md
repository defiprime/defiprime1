---
layout: blog
title: "Lighter pauses withdrawals after trader API key leak"
url: /lighter-pauses-withdrawals-after-api-key-leak.html
h1title: "Lighter pauses withdrawals after trader API key leak"
pagetitle: "Lighter pauses withdrawals after trader API key leak"
metadescription: "Lighter suspended withdrawals and pool creation after a trader API key leak, enabled Guardian mode and targeted a same-day restart after contract upgrades."
category: blog
featured-image: /images/blog/lighter-pauses-withdrawals-after-api-key-leak-ogp.png
intro: "Lighter suspended withdrawals after a trader's API key leaked and said its Security Council would upgrade the contract to help recover funds."
author: sawinyh
tags: ["News"]
date: 2026-11-16T13:23:07+00:00
---

On November 16, Lighter [suspended all withdrawals and pool creation](https://x.com/Lighter_xyz/status/2122284181422284986) while investigating a security incident involving an external party. The team later attributed the incident to a leaked API key for a specific trader's account. Withdrawals remained paused while it prepared contract upgrades, with a target of reopening by the end of the day.

The initial disclosure described the scope cautiously: “We are actively investigating a security incident that appears to involve a single compromised external party.” Lighter said it had imposed the suspension as a precaution while investigating the circumstances and assessing the full impact. The notice gave neither the affected trader's name nor a loss amount.

In its [later statement](https://x.com/Lighter_xyz/status/2122311006604984497), Lighter said: “The Lighter protocol and smart contracts are unaffected.” It also said it had enabled Guardian mode on its smart contract. The operator described an account-level compromise alongside a platform-wide withdrawal restriction. Its statement announced no halt to trading.

## Recovery upgrade and withdrawal pause

Lighter said the next contract change would support recovery: “Our main priority is to recover funds involved in an additional withdrawal attempt by the attacker.” The Lighter Security Council would perform the upgrade. The disclosure included no code for the upgrade, no execution transaction and no amount for the funds involved in that additional attempt.

The team set a target for reopening: “Our current target is to complete the contract upgrades and resume withdrawals by the end of today.” Withdrawals were still paused in that update, and the statement reported no completed recovery. It also left pool creation unresolved, with neither an announcement that the function had resumed nor a time for reopening it.

The pool-creation freeze affects the venue's managed-capital product. Lighter's [public-pool documentation](https://docs.lighter.xyz/trading/public-pools) says whitelisted operators can establish pools, trade participants' funds and receive a share of profits. Each pool trades through a sub-account in the operator's account. The operator's fee comes from profits and is allocated when participants withdraw.

Depositors receive pool shares, which they redeem on withdrawal. Ordinary Public Pools have no lockup periods under the documented terms, but the incident notice temporarily suspended all withdrawals. Neither incident statement identified a particular public pool as the compromised account. The creation freeze therefore leaves open which pool, if any, was involved.

## What a leaked API key authorizes

Lighter's [API-key documentation](https://docs.lighter.xyz/developers/integration-guides/api-keys) separates account credentials from the wallet that owns the account. Each master account or sub-account has its own set of API keys. Every key has a separate key pair and nonce. Software uses those keys to trade and manage the account programmatically. Creating a key pair requires no access to the owner's wallet private key; associating it with a Lighter account requires the owner's authorization.

The destination determines the withdrawal permissions. “Secure withdrawals only need the API key because they can only go back to the L1 address that created the account.” For fast withdrawals and transfers to other owners' addresses, the same documentation requires a signature from the wallet's private key as well. Under those rules, an API key carries different authority from the owning wallet's signing key.

The incident statements left the transaction sequence unexplained. They attributed the compromise to a leaked API key but did not describe how that credential connected to the attempted withdrawal. Neither statement said the trader's wallet private key had leaked. The team's account thus identifies the credential it believes was compromised while leaving the route by which funds moved, and the checks applied along that route, undisclosed.

For services that only need account data, Lighter documents read-only tokens. These allow access to authentication-gated data but cannot sign transactions, place trades or request withdrawals. Lighter recommends using them instead of API keys for dashboards, tax tools and AI agents. They provide data access without trading authority. The incident update did not identify the service that held the leaked key.

## Ethereum settlement and emergency exits

Lighter was among the venues in defiprime's [guide to perpetual trading platforms](/perps-2025.html). Its current [technical architecture documentation](https://docs.lighter.xyz/about-lighter/technical-architecture-lighter-core) describes an exchange anchored to Ethereum. Smart contracts hold deposited assets and the canonical state root, which includes users' assets and positions, public pools and order books. Exchange operations execute deterministically from user-signed transactions. That execution produces a new state and a cryptographic proof.

State-update proposals are published to Ethereum with data blobs containing the transition details, including per-account changes. Users are meant to be able to reconstruct and verify their state from those data. Ethereum verifies the proofs before the contracts update the exchange state. The documentation establishes how settlement is designed to work; it supplies no independent verification of the team's claim that the contracts were unaffected in this incident.

Under the [normal withdrawal process](https://docs.lighter.xyz/developers/integration-guides/deposits-transfers-and-withdrawals), secure withdrawals finalize on Ethereum. Lighter usually claims the funds for the user. Its documentation also describes a `withdrawPendingBalance` call for a user who needs to claim a pending balance, as well as a separate route for submitting a secure withdrawal directly through the Ethereum messaging contract. The incident notices offered neither route as an exception to the withdrawal pause.

The architecture also specifies an Ethereum priority-request queue for withdrawals, public-pool exits and reduce-only immediate-or-cancel orders. If the sequencer fails to process those requests within the prescribed timeframe, the documented response is Escape Hatch mode. In that mode, the contract freezes. Users can then reconstruct their account state from Ethereum data and produce ownership proofs for withdrawal.

Lighter's incident update named Guardian mode, not Escape Hatch mode, and left unexplained how the activated precaution interacts with priority requests. The team had published no recovery procedure for users in that update; the Security Council upgrade and the reopening of withdrawals remained pending.
