---
layout: blog
title: "Glamsterdam review puts up to 15,000 contracts in question"
url: /glamsterdam-november-contract-compatibility-review.html
h1title: "Glamsterdam review puts up to 15,000 contracts in question"
pagetitle: "Glamsterdam review puts up to 15,000 contracts in question"
metadescription: "Ethereum developers reviewed Glamsterdam compatibility findings on November 16. Fixed gas budgets and failure handlers need checks before the fork proceeds."
category: blog
featured-image: /images/blog/glamsterdam-november-contract-compatibility-review-ogp.png
intro: "Ethereum developers reviewed fresh Glamsterdam audit findings on November 16, with contract compatibility and possible specification changes still under discussion."
author: sawinyh
tags: ["Analysis", "Governance"]
date: 2026-11-17T13:26:26+00:00
---

On November 16, 2026, Ethereum core developers reviewed Glamsterdam compatibility findings at [All Core Devs Testing](https://ethereum-magicians.org/t/all-core-devs-testing-acdt-103-november-16-2026/30326). Ethereum Foundation developer Marius van der Wijden put the highest estimate of potentially affected contracts at up to 15,000. The discussion concerned EIP-8037 and EIP-8038, proposed changes to state-gas accounting and prices that can alter how deployed contracts behave without changing their code.

The new audit presentations follow the [earlier delay to the Hoodi fork](/glamsterdam-hoodi-delay-gas-failure-handlers.html). They separate several problems that need different fixes: hard-coded gas budgets that become insufficient, failure handlers that can finish when they previously reverted, and immutable systems that cannot accept a contract upgrade. The Foundation has left specification revisions open for the November 19 execution-layer meeting.

## What the audit numbers measure

In the [direct call transcript](https://forkcast.org/calls/acdt/103/), van der Wijden described the upper range as the highest estimates. He did not present a confirmed inventory of broken applications. The auditors reported findings, which count classes of affected contracts.

ChainSecurity's Tanguy reported 152 findings, including 76 also identified by the Foundation's internal search, bringing the combined search to 200 findings. He immediately explained the unit: a finding represents a class of affected contracts, not an individual contract. Repeated deployments of an affected implementation do not each increase that findings total. The audit tally cannot be read as a competing estimate of the total affected contract population.

Most ChainSecurity findings concerned the Foundation's invariants 4 and 7: assumptions about fixed gas budgets and reserves. Those failures came from higher gas costs, not primarily from the new reservoir or refill mechanism. ChainSecurity said most findings could be mitigated relatively easily, but some would require a contract upgrade or, for an immutable protocol, a full redeployment. Changing a setting and replacing an immutable system are different remediation tasks.

The search also had acknowledged blind spots. ChainSecurity named dormant execution paths, unverified code and private off-chain systems as reasons its coverage was incomplete. Comparing its results with the Foundation's investigation exposed findings it had missed. The auditor expected additional affected systems to be found, so absence from the presented findings does not establish compatibility.

ChainSecurity combined a search across protocol categories, deployment lists, verified source code and public software with a trace-based search of mainnet transactions. It compared old and proposed behavior through replays and constructed scenarios, then examined impact and who could control a mitigation. Those methods look for interacting execution paths as well as suspicious code in isolation.

Its investigation covered Ethereum mainnet, not layer-two networks. ChainSecurity also reported compatibility risks in Gloas, the consensus part of Glamsterdam: proof-layout changes could block staking operations, while relocated execution data could break indexers and oracles. It said it would coordinate reporting with the Foundation. Application review therefore extends beyond gas accounting to the data and proofs that supporting services consume.

The Foundation's Rahul reported at least 25 confirmed medium-severity issues in its application-team outreach. He withheld a larger untriaged count because it contained many false positives. That distinction keeps a search result separate from a confirmed finding, particularly when tools are scanning code for patterns that may never be reachable in actual use.

Before discussing the value in affected contracts, van der Wijden said in the transcript, "I don't have any reliable numbers on this". The call provided no verified balance sheet of funds that would become inaccessible, leaving the value at risk unquantified.

## Why a failed call can become a completed failure

[ChainSecurity's technical account](https://www.chainsecurity.com/blog/glamsterdam-gas/index.html) starts with contracts that catch a failed external call and continue. That can be useful for a batch operation or an optional extension. It becomes dangerous when continuing records a permanent failure or removes the ability to retry an otherwise valid operation.

An attacker can deliberately provide too little gas for the target call while leaving enough for the caller's failure handler. Contracts try to defend against that by checking a budget before the call, inspecting the remaining gas afterward, or relying on the failure handler itself running out of gas. Glamsterdam changes the assumptions behind those defenses.

Under the proposed accounting, state creation can draw from a separate reservoir. The reservoir travels with a call in full, while the normal forwarding restriction applies to execution gas. Solidity's `gasleft()` reports execution gas, not the reservoir. A small reported balance can therefore coexist with enough state gas to pay for a storage operation that records a failure.

If the target reverts or runs out of gas, its reservoir is restored to the value at call entry. The caller's failure handler can use that restored balance. Code that previously exhausted its gas before recording a permanent failure can now complete the write. The target operation still failed; what changed is whether the outer operation commits the failure response.

A separate path comes from clearing storage created earlier in the same transaction. Glamsterdam introduces an immediate state-gas refill. It first credits execution gas up to the outstanding state-creation charges that balance funded, then puts the remainder in the reservoir. ChainSecurity calculates that clearing a qualifying slot can restore up to 97,920 execution gas, subject to that cap. The restored gas can fund the continuation after a failed call.

There is also a nested-call case. An intermediary can create state, call another target, and propagate that target's failure using `REVERT`. Restoring the intermediary's state-gas accounting can return execution gas to its caller. ChainSecurity stresses that an explicit revert matters: if the intermediary itself runs out of gas or halts exceptionally, it returns no execution gas. Reviewers need to trace how failure propagates, not just inspect the final catch block.

Fixed-budget failures require a different check. A pre-call test can still guarantee delivery of a chosen gas amount, but the amount must cover every permitted execution path under the new schedule. ChainSecurity recommends assessing sufficiency without reservoir assistance and revalidating forwarding overhead. Merely preserving the old numeric limit preserves an assumption about cost that the repricing changes.

## Application developers challenged the failure semantics

Juicebox developer Jango described the issue through the protocol's payment and cash-out extensions. Applications can add behavior to payments, cash-outs and payout splits. Its try-catch handling lets execution continue when an extension is genuinely broken, rather than allowing that extension to stop the wider protocol.

His concern was that a caller could tune the gas limit to make the extension fail and trigger the catch block while the rest of the operation proceeds. The caller would then influence whether the composable behavior executes.

The Foundation's [invariants repository](https://github.com/ethereum/glamsterdam-gas-invariants) extends the review beyond on-chain failure handling. It flags off-chain components that assume particular receipt behavior, gas measured by subtracting `gasleft()` readings, and software that hard-codes gas limits. An audit confined to the deployed contract can miss assumptions in the software submitting or interpreting its transactions.

ChainSecurity recommends starting with calls that allow execution to continue after failure. Review the target's full execution path, including proxies, and everything the calling contract does before committing its failure response. Tests should force the subcall to fail and inspect whether the outer operation disables a retry, removes a claim or records an incorrect result. Comparing the old and proposed schedules requires the same relevant pre-state and explicit gas assumptions.

Where possible, its recommendation is to propagate call failures so the entire operation reverts. Where continuing is necessary, preserve a recovery path instead of making an irreversible decision from the remaining gas alone. Raising a threshold is not enough without checking the assumptions that made the threshold meaningful.

The Foundation asks affected teams to report privately to glamsterdam@ethereum.org. Useful reports identify the project and affected contracts, the broken assumption, what goes wrong, whether a setting change, upgrade or migration can fix it, and the expected timing. A reproducible test or transaction gives the reviewers something concrete to evaluate. The repository asks teams to use email rather than public issues so problems can be fixed before wider disclosure.

## The specification decision remains open

Van der Wijden acknowledged that public outreach and audit timelines slipped amid Foundation reorganizations and budget cuts. He called for engagement with application developers and security researchers before changes reach testnets. The compatibility assessment arrived after substantial implementation work.

Van der Wijden said proposed alternatives break other assumptions and would require fresh investigation. In the call's chat, researcher Ansgar Dietrichs cautioned against rushing to formalize permanent invariants, warning that premature commitments could prove wrong.

The [Foundation's published update](https://blog.ethereum.org/en/2026/11/06/glamsterdam-8037-8038) says revisions are being prototyped and reviewed, with their benefits and any newly broken assumptions to be presented to execution-layer developers. Hoodi remains delayed until the issues are resolved, while Hegota work continues in parallel. The November 19 discussion has no precommitted decision on the proposed changes.
