---
layout: blog
title: "Qubic resumes its network and opens weak-seed recovery claims"
url: /qubic-recovery-claims.html
h1title: "Qubic resumes its network and opens weak-seed recovery claims"
pagetitle: "Qubic recovery: wallet migration and fund claims"
metadescription: "Qubic says its network has resumed. Affected holders must migrate insecure wallets and prove ownership to reclaim funds through its recovery portal."
category: blog
featured-image: /images/blog/qubic-recovery-claims-ogp.png
intro: "Qubic says its network is operating again after a quorum-approved recovery, while weak-seed wallet holders face a separate ownership review to recover funds."
author: sawinyh
tags: ["News"]
date: 2026-10-21T06:22:34+00:00
---

At 18:14 UTC on October 20, 2026, Qubic [announced that its network was live again](https://x.com/_Qubic_/status/2112608369135804801), following a recovery approved by its Computor quorum. The team said the reclaim platform was open and the first funds had returned to verified owners. Its announcement did not provide an amount for those initial returns.

The [recovery thread](https://x.com/_Qubic_/status/2112608375129436524) says affected funds were moved into protected escrow while the network was halted. The quorum then approved the recovery and normal operation resumed. Holders must secure wallets that may still be vulnerable and provide proof of ownership to claim the assets held for recovery.

The team's claim portal still carries its halt-era description. The [portal's introduction](https://weak-seed-reclaim.qubic.org/) says the network is halted and funds are frozen. That conflicts with the subsequent announcement of resumed operation. The portal remains the team's named destination for claims, but its introductory description should not be read as confirmation of the current network state.

## Replace affected wallets before reusing them

Qubic's [wallet warning](https://x.com/_Qubic_/status/2112608383983661180) extends beyond holders who have already seen funds disappear. Anyone who created a wallet using the web wallet before version 4.26.4, released on October 19, is told to treat that wallet as insecure, even if its funds were untouched. The instruction is to update to that version or later, create a new wallet with a fresh seed, move funds as soon as possible and stop using the old wallet.

The claim portal adds a requirement for recovered funds: the destination must be a brand-new, secure identity generated in an updated wallet, not on an affected device or browser. Recovered assets are to go to that destination rather than back to the compromised identity. The portal explicitly tells applicants never to reuse the affected seed.

For a claim, the source must be the affected 60-character identity and appear on the published affected-address list. Claimants also need a signed message from that identity. The wallet signs the exact text supplied by the site; the process does not require pasting a seed into the portal.

A signature links the claim to a proposed destination. It cannot establish who owns the funds: the portal explains that weak seeds let an attacker generate the same valid signature as the legitimate owner. Core developers review separate evidence of ownership that the attacker would not possess.

## Ownership evidence determines the claim

The [claim instructions](https://weak-seed-reclaim.qubic.org/) rank an exchange withdrawal receipt showing a transfer to the affected source address as the strongest example of evidence, because the exchange's identity checks connect the withdrawal to its customer. An OTC deal confirmation referencing the address is another accepted example.

Other listed evidence includes a pre-incident funding trail from a source the claimant can demonstrate they control, or a signed message from a different, unaffected address that funded the compromised one. A personal or sworn statement can support a submission, but the portal explicitly labels it supporting material rather than proof.

The portal says one strong item of evidence is usually enough, while several weaker items can work if they corroborate one another. Filing early does not defeat a legitimate later claim. The site itself only collects and verifies submissions; decisions about recovery and their application rest with the Computor quorum. The claim form does not execute those decisions.

An optional identity check through Didit is available after filing. The portal says verification improves the prospect of fast approval and helps exclude impostors. Identity documents stay with Didit; Qubic says it receives a result rather than the documents themselves. Applicants are not required to complete this step.

The review process separates uncontested claims from those that need more scrutiny. A single, strongly evidenced, uncontested claim can take the fast route. Contested claims, those with weaker evidence and larger claims go to extended core-developer review. The portal does not specify a numerical threshold for the larger-claim category.

Approved claims are listed publicly with the address and amount for 7 days before payout. Unresolved competing claims remain frozen in escrow. Payout requires both an ownership check and a dispute period. Signing a message does not trigger an immediate withdrawal from escrow.

## Recovery depends on where the assets went

The portal distinguishes funds drained but still on Qubic from funds sent to MEXC. The former are returned from the recovery escrow account. The latter follow a separate, slower route through the exchange that depends on law-enforcement cooperation. The instructions give no completion date for that exchange route.

A weak identity whose funds were not drained is handled through release from an on-hold list after verification. Owned tokens and shares are to be returned to the new identity when its claim is approved. The application process also covers these undrained funds, alongside assets already taken by an attacker.

QEARN locks and specified smart-contract standings, excluding QX, remain in place and are due to return to the new identity in later batches. QX orders were cancelled during recovery so the assets committed to them could be secured. The portal tells affected users to file one claim despite these different asset treatments; it does not give dates for the later batches.

The [claim window runs until May 1, 2027](https://x.com/_Qubic_/status/2112608396709085343). Qubic warns that it will never initiate a direct message or ask for a seed, and identifies weak-seed-reclaim.qubic.org as the only official reclaim site. The team directs users needing help to Discord.

Qubic [says a full technical report will follow](https://x.com/_Qubic_/status/2112608402816090562). That report was still described as forthcoming in the recovery announcement; the published instructions do not supply an escrow address or a transaction record for the first returned funds.
