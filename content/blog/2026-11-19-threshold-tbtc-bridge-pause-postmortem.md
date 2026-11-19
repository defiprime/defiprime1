---
layout: blog
title: "Threshold discloses tBTC phantom-deposit bug behind bridge pause"
url: /threshold-tbtc-bridge-pause-postmortem.html
h1title: "Threshold discloses tBTC phantom-deposit bug behind bridge pause"
pagetitle: "Threshold discloses tBTC bridge pause postmortem"
metadescription: "Threshold explains the deposit-accounting bug behind its tBTC bridge pause, the Linux patching effort and higher gas requirements for relayers."
category: blog
featured-image: /images/blog/threshold-tbtc-bridge-pause-postmortem-ogp.png
intro: "Threshold's postmortem explains the bug behind its tBTC bridge pause and tells relayers to re-estimate gas limits after the fix."
author: sawinyh
tags: ["News"]
date: 2026-11-19T09:22:11+00:00
---

Threshold published a postmortem on November 18, 2026, explaining why its tBTC bridge stopped accepting deposits and redemptions and how a deposit-accounting flaw could have created unbacked $tBTC. The [report](https://www.threshold.network/blog/post-mortem-the-tbtc-bridge-pause) describes a precautionary pause that began on October 30 and an app reopening on November 10, after a bridge upgrade and node-operator patching.

Threshold says revealing a deposit now costs roughly 4,500 to 33,000 more gas, depending on the funding transaction's size. Relayers using fixed gas limits must re-estimate them. Malformed funding transactions now revert. The upgrade changed two bridge libraries while leaving storage layout, the ABI and events intact, according to the report.

## A wallet request arrived during a private bug investigation

An unknown address initiated a wallet-generation round at about 20:16 UTC on October 30, according to Threshold. Distributed key generation creates a signing wallet for bridge deposits. Anyone can start a round when the protocol's conditions are met, but the team had not initiated this one. Engineering received an alert about seven minutes later.

Researchers had already privately reported a deposit-accounting problem through the project's bug bounty program. The unexpected round led the team to consider whether an outsider was preparing to attack the reported issue. Threshold credits an OtterSec security researcher with first reporting the vulnerability through Immunefi.

Within about three hours, the team put the app into maintenance mode and issued a public notice, the report says. The Threshold Council multisig disabled Bitcoin proof submission, stopping minting, and blocked approval of the unexpected wallet-generation round. The app stopped accepting new deposits and redemptions. Threshold says a deposit crafted to exploit the accounting issue appeared the following morning.

According to the report, existing holders could still transfer and use $tBTC during the app pause, but could no longer convert between bitcoin and the token through the app. Proof submission remained disabled until November 7. The app reopened at about 03:00 UTC on November 10, after the Council had reauthorized proofs and the bridge fix was in place.

## The flaw could turn a wallet balance into a deposit

Threshold traces the flaw to the code that reads a Bitcoin funding transaction when a user reveals a deposit. The bridge needs to identify the deposit output and its amount. The old parser accepted an empty input list and trailing bytes, the report says. It did not require well-formed input and output lists that were consumed in full.

That let a carefully encoded transaction create a deposit record without a corresponding real deposit output, according to Threshold. The report calls this a phantom deposit and identifies `revealDepositWithExtraData` as one route used in the reported constructions. Recording the deposit was the first step. Whether it received credit depended on what happened when a wallet later swept funds.

The report says the sweep logic checked an input against deposit records before checking whether it was the wallet's own main UTXO, the Bitcoin output holding its balance. A phantom deposit registered at that output could cause the bridge to credit the wallet's entire balance as a deposit. Threshold says this would have minted $tBTC without new bitcoin backing it.

The same ordering could also make a wallet's sweep impossible to prove, freezing the wallet, according to the postmortem. A separate accounting gap allowed an output already claimed by a moving-funds transfer to be swept again as a deposit. Threshold says the upgrade addressed both failure modes.

Threshold attributes the crafted deposit's failure to produce excess credit to the proof pause. Deposit credit requires a sweep proof on Ethereum, and the Council had removed the only authorized proof submitter the night before. The alternative path, optimistic minting, credits deposits before a sweep but had already been paused since May. The report says the crafted deposit was processed only after the fix and credited at its real value, less fees.

## Operators also had to patch their servers

During the bridge investigation, node operators also faced a Linux kernel vulnerability affecting incoming TCP connections. Threshold says its nodes need internet connections to communicate with each other, exposing several operators' servers. Some Linux distributions lacked a fixed kernel for several days, complicating the restart.

According to the report, operators began stopping and patching nodes early on October 31. Where a fixed kernel was unavailable, the team asked operators to migrate to a distribution with a fix. Each node holds key shares, and a wallet needs more than half of its signer seats to sign. Signing could resume only after enough operators returned online.

The postmortem treats server patching and the deposit-accounting fix as separate problems handled during the same interruption. Threshold says the bridge upgrade went through the Council multisig and its timelock. It has not established that anyone exploited the kernel vulnerability against a node.

## Stricter reveals and a prospective fix

Threshold says the updated parser requires well-formed funding-transaction input and output lists, rejects an empty input list and requires the lists to be consumed exactly. Sweep processing now identifies the wallet's main UTXO before looking through deposit records. An output already claimed by a moving-funds transfer can no longer be swept as a deposit.

The patch prevents new phantom records but leaves existing records unchanged, according to Threshold, which describes the fix as prospective. The postmortem reports no unexplained bitcoin outflow or newly unbacked $tBTC in the team's review. These are Threshold's findings; the report is not an independent reconstruction of the bridge's Bitcoin and Ethereum histories.

The report also says Aave froze $tBTC on V3 Ethereum Core on October 31 and cites a reported Gauntlet market exclusion. Threshold says each partner decides when to lift its own measures, separately from the bridge reopening. Its reopening announcement does not confirm that those restrictions have been lifted.

Threshold has not established whether the unexpected wallet-generation round and the crafted deposit were connected, or whether anyone exploited the Linux vulnerability against a tBTC node.
