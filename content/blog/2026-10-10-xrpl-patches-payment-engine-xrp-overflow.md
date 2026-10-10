---
layout: blog
title: "XRPL patches payment engine bug that could mint spendable $XRP"
url: /xrpl-patches-payment-engine-xrp-overflow.html
h1title: "XRPL patches payment engine bug that could mint spendable $XRP"
pagetitle: "XRPL fixes critical $XRP payment engine overflow"
metadescription: "XRPL fixed a payment engine overflow that could mint spendable $XRP and disclosed why the patch bypassed its normal amendment process."
category: blog
featured-image: /images/blog/xrpl-patches-payment-engine-xrp-overflow-ogp.png
intro: "XRPL fixed a payment engine overflow that could let a crafted payment mint spendable $XRP while charging the buyer only a few hundred drops plus a fee."
author: sawinyh
tags: ["News"]
date: 2026-10-10T05:19:04+00:00
---

XRPL released xrpld 3.4.1 on September 25, 2026, with a fix for a payment engine overflow that could let a crafted payment mint spendable $XRP while charging the buyer only a few hundred drops plus a fee. The [public vulnerability disclosure](https://xrpl.org/blog/2026/vulnerabilitydisclosurereport-bug-20261009), published October 9, says RippleX reproduced the attack and found no evidence that it had been used on a public network.

The finding was reported through the XRPL bug bounty program on September 22. The initial report rated it Major. RippleX reproduced the mint on a standalone server and in its unit tests, confirmed that the new $XRP could be spent in a later payment, and raised the severity to critical.

## How the payment created new $XRP

The vulnerable path ran through XRPL's built-in order book. An attacker could create a few hundred accounts and use each account to offer a tiny amount of another token for a very large amount of $XRP. A separate account could then send one payment that consumed all those offers. Each offer remained valid when considered by itself.

The payment engine calculated what the buyer owed by adding the amounts across every offer taken in one pass. That calculation used ordinary 64-bit integer addition without an overflow check. Once the sum passed the integer's maximum, it wrapped to a small value. The engine still credited every offer owner with the full requested amount, but it charged the buyer only the wrapped total. The difference became newly created $XRP.

The [disclosure explains](https://xrpl.org/blog/2026/vulnerabilitydisclosurereport-bug-20261009) that all accounts in the construction could belong to the same attacker. The starting cost was a few hundred $XRP for account and offer reserves, most of which would be returned after the objects were removed, plus ordinary transaction fees. The attack required hundreds of deliberately mispriced offers and a payment designed to consume them together. Normal payments and trades could not reach the overflow because the total $XRP supply sits far below the point at which the arithmetic wraps.

A ledger invariant was supposed to reject any transaction that created $XRP. It failed here because it totaled balance changes with the same type of 64-bit counter. That counter wrapped in the same way, making the transaction appear to have burned only its fee. A second check limited the balance held by one account, but distributing the minted assets across hundreds of accounts kept each balance below that threshold.

The bug had been present since the current payment engine was written in 2015. The no-new-$XRP invariant arrived two years later with the same unchecked arithmetic. The report says a normal payment never approaches the overflow boundary, which left the path dormant until a researcher built the required offers.

## What changed in xrpld 3.4.1

Starting with xrpld 3.4.1, the payment engine checks for overflow while summing offer amounts. A sum that would overflow now fails cleanly, producing a normal path-dry or partial-payment result without minting anything. Developers added the same check where the engine combines results from multiple payment paths.

The invariant now uses a wider counter that cannot wrap around in the same way. The team also hardened several other places that total balances across many accounts, although the disclosure says real transactions could not currently reach those paths. For server operators, the immediate requirement is concrete: the report says all operators must run xrpld 3.4.1 or newer to remain in sync.

XRPL normally changes transaction processing through amendments. A new rule ships disabled, then activates only after more than 80 percent of trusted validators support it for two weeks. The network did not use that route for this fix. Each server applied the new payment rule as soon as its operator installed xrpld 3.4.1. The disclosure calls this the first deliberate direct transaction-processing change since the amendment system began more than ten years ago.

The team chose the direct release because publishing an inactive amendment would expose the bug while leaving it usable during the upgrade, voting, and activation periods. The exploit was cheap, required no privileged access, and could create assets that would be difficult to unwind. On release day, more than 80 percent of validators on the default Unique Node List were already running the patched version, even though the fix's source code had not yet been published.

That rollout created a short consensus risk. Patched servers would reject an exploit transaction while older servers would accept it. If someone had attempted the exploit during the mixed-version window, unpatched servers could have fallen out of sync, or the network could have halted over the next ledger. The team judged a halt preferable to validating a transaction that created an incorrect ledger state. Normal transactions did not enter the affected path.

## What operators and users can verify

The disclosure says no exploitation was found on public networks. It also says the attack could not occur accidentally, since it needed hundreds of offers at prices no ordinary trader would use and one purpose-built payment. Those statements narrow the user risk, but they do not replace an operator's version check. Any server below xrpld 3.4.1 lacks the overflow rejection and the wider invariant counter described in the fix.

The report also separates this issue from a Batch transaction wrapper vulnerability fixed in the same release. The payment overflow fix took effect immediately with the software upgrade. The Batch fix depended on the fixBatchV1_2 amendment, which activated on Mainnet on October 9. Older servers are now amendment blocked, giving operators a second reason to update.

XRPL plans to add a re-verification step to its release process. Every security finding marked fixed, whether it came from an audit, bug bounty, attackathon, or AI-assisted red team, will be retested against the release candidate. The finding will close only after that candidate passes a test reproducing the original issue. The open operational question is whether this repeatable test process finds other arithmetic paths that share assumptions with the payment engine before a crafted transaction reaches them.
