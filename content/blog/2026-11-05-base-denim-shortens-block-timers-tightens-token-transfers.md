---
layout: blog
title: "Base Denim shortens block timers and tightens token transfers"
url: /base-denim-shortens-block-timers-tightens-token-transfers.html
h1title: "Base Denim shortens block timers and tightens token transfers"
pagetitle: "Base Denim shortens block timers and tightens token transfers"
metadescription: "Base activated Denim with faster blocks and stricter B20 transfer checks, shortening block-based delays while transaction inclusion delays remain unresolved."
category: blog
featured-image: /images/blog/base-denim-shortens-block-timers-tightens-token-transfers-ogp.png
intro: "Base activated Denim, shortening block-count durations and extending B20 executor checks to direct transfers while reporting transaction inclusion delays."
author: sawinyh
tags: ["News"]
date: 2026-11-05T20:25:01+00:00
---

Base said its Denim upgrade went live on mainnet on November 5, 2026, replacing Flashblocks with native 200ms blocks and tightening transfer checks for B20 tokens. The [activation announcement](https://x.com/buildonbase/status/2118433231842513404) identifies a timing change for protocol teams to inspect: contracts that measure delays in blocks now run those delays in one tenth of the intended wall-clock time.

Before Denim, Base produced a canonical block every two seconds. Flashblocks streamed incremental pending-state updates while that block was being built. Denim replaces those previews with five complete canonical blocks per second. Base says the protocol validates a full timestamp exactly 200ms after the parent, with no skipped slots.

Transaction inclusion still comes before Ethereum settlement. Base says a block becomes safe when its batch is posted to Ethereum and final when Ethereum finalizes that batch. Applications that display inclusion in a native block need to keep those stages distinct when reporting settlement to users.

## Block-based delays need inspection

The [native-block documentation](https://docs.base.org/upgrades/denim/200ms-blocks) says `block.number` advances ten times faster in wall-clock time, while `block.timestamp` continues to advance in whole seconds. The affected code includes timelocks, cooldowns and exit delays expressed as `block.number - start >= N`. A contract that keeps the same block count reaches that condition sooner in elapsed time.

The announcement also lists vesting, emission and difficulty schedules measured in blocks, per-block rate limits, and deadlines expressed as `expirationBlock = block.number + N`. Each needs its own check. A cap that resets with each new block now resets more frequently, while a block-based deadline arrives sooner. Teams reviewing withdrawal delays also need to inspect these schedules, limits and deadlines.

Governance contracts face the same change when voting delay and voting period use blocks, including `ERC20Votes` with its default block-number clock. The documentation says voting windows shrink ten times while stored checkpoints stay correct. The historical voting records remain valid, but the upgrade reduces the time available for a new vote under the same block-count parameters.

Base's migration instructions contradict each other. The announcement says, “Where a block count is governance-tunable, multiply it by ten.” The specification instead says, “Where a block count is governance-tunable, plan to divide it by ten at activation.” Both describe faster block production, yet they prescribe opposite adjustments. Teams should check their contract's timing logic and resolve that inconsistency before submitting a parameter change. Copying the specification's division instruction leaves the contradiction unresolved.

Both sources recommend replacing block-count durations with `block.timestamp` comparisons where redeployment or upgrades are possible. The specification says immutable block-count constants cannot be retuned. It calls for assessing their impact and planning a migration before activation, and directs teams to test changed behavior on Vibenet, which already produces 200ms blocks. The published guidance leaves continued operation of immutable contracts still in use after activation to a contract-specific assessment.

The oracle guidance separates price calculation from historical coverage. The documentation says Uniswap V3-style time-weighted average prices remain correct because their accumulators are second-weighted. It also warns that fixed observation cardinality covers roughly half as much wall-clock history. Long `observe()` lookbacks can therefore revert with `OLD` sooner, even when the accumulated prices remain correct. Teams need to check both the prices and the history available to those calls.

## Applications move off Flashblocks

Base says it has stopped producing Flashblocks streams, and the `pending` block tag no longer returns preconfirmed state. Applications using `eth_subscribe("newFlashblocks")` must move to `eth_subscribe("newHeads")`; `pendingLogs` subscriptions move to `logs`. Clients using `newFlashblockTransactions` need to subscribe to new heads and fetch each block's transactions.

The new millisecond fields are conditional. Clients derive `timestampMs` from authenticated BaseTime metadata; they cannot estimate it from the whole-second timestamp. Responses omit the field when the historical block body or metadata has been pruned or is unavailable. Mined transaction objects gain an optional `blockTimestampMs` field. Indexers reading historical records must handle records with no millisecond metadata.

The [operator notice](https://base-l2.statuspage.io/incidents/js0n0438q6l4) instructed mainnet node operators to upgrade to `base/base v1.5.1` before activation. Operators upgrading from an older release must remove `--enable-experimental-validity-transactions` from the `base-reth-node` command if present. Leaving the flag in place causes the node to fail to start. Operators need to address that startup requirement separately from the subscription changes application clients must make.

## B20 checks reach direct transfers

Denim also changes who can initiate transfers of restricted B20 tokens. Base says `TRANSFER_EXECUTOR_POLICY` previously applied only to `transferFrom` calls made by someone other than the holder. A holder calling `transfer` directly could bypass the executor allowlist, even when the issuer intended an approved party such as a transfer agent to initiate every transfer.

The policy now checks `msg.sender` on every transfer path, matching the sender and receiver policy checks. Tokens launched with an executor policy automatically inherit the behavior. A holder's direct transfer can now fail an executor check that the same call previously bypassed. Tokens that never set an executor policy keep the always-allow default, so this check does not change their transfer behavior.

Denim also adds a way to compose policies. Cobalt allowed issuers to combine policies with AND and OR; Denim adds NOT through a reserved bit that inverts a policy ID. This reverses the authorization result while keeping membership on the underlying policy, without copying it. An issuer can use the same address list for inclusion in one scope and exclusion in another without maintaining duplicate membership lists.

Recipient validation changes too. A transfer, mint or seizure addressed to the token's own address now reverts with `InvalidReceiver`. Base says a B20 token is a precompile without a holder key. Balances previously sent there were stuck unless the issuer seized them back. An issuer can still recover an earlier balance through `seizeWithMemo`, but only if it opted into seizure functionality. Self-sends, transfers to other B20 tokens, approvals and burns are unaffected.

Defiprime previously covered [Base packaging stablecoin yield and crypto-backed loans for apps](/base-packages-stablecoin-earn-and-crypto-loans.html). Denim's documentation covers the infrastructure beneath applications. Neither the announcement nor the material reviewed here identifies an application-specific loss or provides independently verified contract-state readings.

Base's status notice says Denim successfully activated and reports an investigation into periodic transaction inclusion delays causing a higher-than-expected rate of empty blocks. The cited update leaves those delays unresolved.
