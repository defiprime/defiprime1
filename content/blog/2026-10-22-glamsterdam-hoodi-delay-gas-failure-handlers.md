---
layout: blog
title: "Hoodi Glamsterdam fork delayed after gas-handling warning"
url: /glamsterdam-hoodi-delay-gas-failure-handlers.html
h1title: "Hoodi Glamsterdam fork delayed after gas-handling warning"
pagetitle: "Hoodi Glamsterdam delay: ChainSecurity flags gas-handling risks"
metadescription: "ChainSecurity reports 13 affected examples as Hoodi delays Glamsterdam. Gas refills can let contracts record permanent failures instead of reverting."
category: blog
featured-image: /images/blog/glamsterdam-hoodi-delay-gas-failure-handlers-ogp.png
intro: "ChainSecurity says gas-accounting changes can let existing contracts commit failures that previously reverted, prompting a delay to the Hoodi Glamsterdam fork."
author: sawinyh
tags: ["News", "Yield"]
date: 2026-10-22T17:22:41+00:00
---

On October 22, 2026, ChainSecurity said the Glamsterdam hard fork on Ethereum's Hoodi testnet had been delayed after its researchers identified security impacts in existing contracts. The firm said it had found 13 real-world examples and was conducting responsible disclosure with the affected projects. Its [announcement](https://x.com/chain_security/status/2113303061078671814) asked teams to check their contracts while the Ethereum Foundation assessed the extent of the impact.

The problem affects contracts that catch a failed external call and keep executing. Under the gas changes ChainSecurity examined, a failure handler can finish where it previously would have run out of gas and reverted. A caller can deliberately supply too little gas for an operation while leaving enough for the surrounding contract to record a permanent failure. An operation that should have remained retryable can then lose its recovery path.

ChainSecurity's [technical disclosure](https://www.chainsecurity.com/blog/glamsterdam-gas/?v=3) examines EIP-8037 and EIP-8038 using specifications reviewed on October 13. Its gas examples describe proposed execution behavior, not balances read from affected contracts. The announcement names neither the projects under disclosure nor their contract addresses.

## The failure handler gets another source of gas

Contracts defend against insufficient-gas griefing in several ways. Some check before an external call that they can forward a chosen gas budget. Others examine the gas left after a failed call and revert when too little remains. Others rely on the failure handler itself running out of gas. That rolls back the surrounding operation without an explicit check.

Checks after a call and handlers that rely on running out of gas depend on how much gas the call forwards, consumes and returns. Under EIP-150, a call can forward approximately 63/64 of its available gas. When the immediate target exhausts that allocation, the caller retains only a small share. A check can reject that remainder, or an expensive storage write can force the caller to revert.

The state-gas reservoir gives the caller another source of funding. ChainSecurity describes a separate pool that travels with calls in full, while the forwarding limit applies to execution gas. Solidity's `gasleft()` reports only the execution balance. A contract with a low reading can still have reservoir funding for state creation. If the target reverts or runs out of gas, its reservoir returns to its call-entry value and remains available to the caller.

In the report's example, around 15,000 execution gas can cover a cold fresh-slot write and a short continuation when the reservoir pays the state-creation charge. Under Osaka, the corresponding write costs 22,100 gas. A handler that previously could not record a failure may now commit it. Because the reservoir is forwarded in full, an outer wrapper can combine a funded reservoir with a limited execution budget.

## Clearing storage can refill the execution balance

A contract can also allocate a persistent storage slot, call another contract, catch a failure and clear that slot before continuing. Under Osaka, clearing storage allocated earlier in the transaction produces a refund subject to a cap. The refund settles at the end of the transaction, so it cannot pay for the next instruction.

Under the Glamsterdam rules examined in the disclosure, undoing state creation triggers an immediate refill. The refill first restores execution gas up to the outstanding state-creation charges paid from that balance. Any remainder enters the reservoir. Clearing a slot can restore up to 97,920 execution gas, enough to change whether the rest of the failure handler completes.

For this to happen, the slot must have been zero at the start of the transaction. The frame must have outstanding state-creation charges funded from execution gas, either from its own work or successful subcalls. It also needs enough execution gas to clear the slot: the `SSTORE` stipend check still requires more than 2,300 execution gas, regardless of reservoir funding.

A gas check performed after the clear can see a replenished balance even though the target ran out of gas. ChainSecurity says a check that rejects the failure before the clear is unaffected by that refill. Its review instructions ask teams to locate storage refills relative to checks, since the order determines whether the check sees the restored gas.

## An intermediary can return gas it already spent

Gas can also return through an intermediary. In ChainSecurity's example, a defending contract calls an intermediary, which creates state and calls a target. The target runs out of gas. The intermediary then propagates that failure with `REVERT`.

Under the reviewed changes, reverting restores the intermediary's state-gas accounting. It credits outstanding execution-funded state-creation charges back to the intermediary's execution balance. That restored gas can return to the defending contract and lift the remainder above a post-call check's threshold. It can also fund a failure handler that previously would have reverted.

The intermediary must retain enough gas to execute `REVERT`. If it runs out of gas itself or halts exceptionally, its resulting execution balance is consumed and no execution gas returns. Tests need to distinguish those paths, even when both ultimately report that a subcall failed.

## What contract teams need to review

Pre-call checks avoid inferring the cause of failure from returned gas, but their budgets need revalidation too. A check can guarantee delivery of the requested allocation even when that allocation no longer covers the target's work. ChainSecurity calls for bounds covering every permitted execution path under the new schedule, including cases where the reservoir cannot contribute. Forwarding overhead also needs rechecking.

The review starts with external calls that let execution continue after failure. Teams should trace the target's complete path, including proxies, and the caller's instructions before it commits a failure response. Tests should force a subcall failure and compare Osaka and Glamsterdam using the same relevant pre-state and explicit gas assumptions. The outcomes to inspect are disabled retries, removed claims and incorrect recorded results.

Where possible, ChainSecurity recommends propagating call failures so the entire operation reverts. Where execution must continue, it recommends preserving a recovery path instead of making an irreversible decision from remaining gas alone. Responsible disclosure continues with the affected projects unnamed. The firm's announcement gives no replacement date for the Hoodi fork.
