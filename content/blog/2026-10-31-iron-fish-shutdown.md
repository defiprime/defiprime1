---
layout: blog
title: "Iron Fish ends network support after inflation bug"
url: /iron-fish-shutdown.html
h1title: "Iron Fish ends network support after inflation bug"
pagetitle: "Iron Fish ends support after inflation bug and bridge warning"
metadescription: "Iron Fish ends network support after a repeated-spend bug and warns on wrapped-token backing. Its patch offers no upgrade path for existing chains."
category: blog
featured-image: /images/blog/iron-fish-shutdown-ogp.png
intro: "Iron Fish is ending network support after an inflation bug, while its released patch leaves existing chains without a migration path."
author: sawinyh
tags: ["News"]
date: 2026-10-31T03:24:11+00:00
---

On October 30, Iron Fish [announced the end of all remaining network support](https://x.com/ironfishcrypto/status/2116278010802586090) after tracing abnormal wrapped-token activity to an inflation bug in its own blockchain. The project said an attacker repeatedly spent the same note, compounded the exploit and exited through the ChainPort bridge.

The disclosure follows an earlier warning about $wIRON on Base. Iron Fish had asked users to avoid buying the wrapped token or using the bridge while it investigated issuance that could no longer be assumed to have full backing. Its published patch leaves operators with another problem: it provides no upgrade path for the existing chain.

## From the bridge warning to the native-chain bug

In its [October 28 warning](https://x.com/ironfishcrypto/status/2115282030946824307), Iron Fish said: “Please avoid buying wIRON on Base or using the bridge until further notice. Full 1:1 backing cannot be assured.” The team had requested an urgent review from ChainPort after observing abnormal issuance on Base. It issued the backing warning before publicly identifying the flaw behind the wrapped-token activity.

The shutdown statement places the cause in Iron Fish itself. The team said it worked with ChainPort and reviewed the bridge operator's logs before reaching that conclusion. Its account identifies ChainPort as the attacker's exit route and locates the inflation bug in the native blockchain's Merkle tree implementation.

Iron Fish traced that implementation to a commit from early 2019. Its statement says the interaction between the tree and the calculation of a note's nullifier allowed a note to be spent more than once. The team acknowledged that auditors had reviewed the affected code: “This code path was within the scope of both our external and internal audits, but the bug wasn’t caught during review.”

The team said it committed the patch and a detailed postmortem before shutting down and archiving the repository. The announcement attributes the observed incident to the flaw. The technical document explains how the flaw works and what the proposed correction can support. Neither document gives holders a migration procedure for the existing network.

## How a spent note could appear unused

The [code-level postmortem](https://raw.githubusercontent.com/iron-fish/ironfish/c5c3c22bfc26dbf40a26c58ffee3181bef6cef5e/docs/merkle-note-position-alias-postmortem.md) describes a copied branch in the Merkle tree. At that branch, changing a position bit could still produce the same root. Someone controlling a note's spending authority could prove the inserted output at a position that had no separately funded output behind it.

The alternate position produced a different nullifier. The nullifier set then failed to recognize the transaction as another spend of the same note. Ordinary transaction value-balance checks also failed to correct the problem because the repeated input appeared under distinct nullifiers. Together, these failures allowed outputs with a combined value greater than the value the attacker originally held.

The attack required the note's contents and spending authority. The postmortem says this path could let an attacker spend their own nonzero-value note repeatedly; it did not permit arbitrary spending of another user's note. The flaw allowed inflation through repeated use of an owned input. The operator's incident account connects that inflation to the bridge activity.

The technical explanation has limits when applied to historical transactions. Valid proofs, real anchors and distinct public nullifiers would be consistent with the mechanism, but the note position is private. The postmortem says those observations alone cannot attribute a particular event or amount to the flaw. Historical attribution requires separate forensic evidence, so the code-level finding alone cannot establish the loss amount.

## Why the patch cannot repair the running chain

The [patch description](https://github.com/iron-fish/ironfish/pull/5762) says the corrected tree construction binds every inserted output to a real tree position. Identical commitments at separately funded positions remain legitimate. The defect was the unfunded position introduced by the copied branch; identical commitments in themselves were valid.

The spend circuit, proving parameters and transaction format remain unchanged. The circuit still does not constrain the private position to the public tree size, according to the patch description. The correction works through tree construction, which also changes the roots against which existing history would have to validate.

Mainnet and testnet histories were produced under the old rule. The postmortem says those histories are incompatible with the patch, and their historical genesis definitions were not migrated. A node running the corrected tree cannot simply switch rules at an arbitrary height and continue validating the existing chains. Installing the corrected implementation offers no documented recovery procedure for current balances.

The patch is suitable for a new chain with a newly generated genesis and coordinated network parameters. It includes no activation-height rule, dual-root verifier, legacy proof migration or historical accounting plan. Preserving an existing chain would require a separate consensus upgrade design and security review. The tests exercise the intended fresh-chain behavior. The postmortem explicitly says they are neither an independent cryptographic audit nor a way to make the old chains valid under changed roots.

## Support ends after maintenance mode

Iron Fish's [earlier maintenance-mode notice](https://ironfish.network/learn/blog/2026-04-20) had retained foundation-run supporting infrastructure, including bootstrap nodes, the block explorer and the website. The foundation described that infrastructure as noncritical to network operation and credited community participants with keeping the decentralized network running. Ending the remaining support withdraws the foundation's commitment to that infrastructure. The announcement does not establish that every independently operated node has stopped.

A pinned [Base contract reading](https://basescan.org/address/0x166e70941262ae7cbf9df5c8897a6242c546457d) at block 53143118 recorded a supply of 3,925,937.805213 wIRON and returned false for the paused flag. That snapshot records the wrapped contract's state at that block. It does not measure the native assets backing the token or the amount created through the exploit.

The shutdown statement gives no timetable for restoring assured wrapped-token backing, and the patch supplies no historical accounting plan. A supported migration for existing balances would require work outside the released fix.
