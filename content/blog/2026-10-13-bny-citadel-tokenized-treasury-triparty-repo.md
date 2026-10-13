---
layout: blog
title: "BNY and Citadel move a tokenized Treasury from settlement into repo"
url: /bny-citadel-tokenized-treasury-triparty-repo.html
h1title: "BNY and Citadel move a tokenized Treasury from settlement into repo"
pagetitle: "BNY, Citadel complete tokenized Treasury repo workflow"
metadescription: "Citadel Securities settled a tokenized 2-year Treasury on BNY's private ledger, then pledged it in an overnight triparty repo with BNY."
category: blog
featured-image: /images/blog/bny-citadel-tokenized-treasury-triparty-repo-ogp.png
intro: "Citadel Securities settled a tokenized 2-year Treasury on BNY's private ledger and then used it as collateral in an overnight triparty repo."
author: sawinyh
tags: ["News", "RWAs"]
date: 2026-10-13T21:19:39+00:00
---

At 20:51 UTC on October 13, 2026, BNY [announced](https://x.com/BNYglobal/status/2110111120841224418) that Citadel Securities had settled a tokenized 2-year U.S. Treasury note on BNY's private digital ledger and used it as collateral in an overnight triparty repo. BNY did not disclose the note's face value or the transaction time in its release.

The transaction was the first use of tokenized assets on a major triparty repo platform, according to [BNY's account](https://www.bny.com/corporate/global/en/about-us/newsroom/press-release/bny-completes-tokenized-us-treasury-triparty-repo-workflow-with-citadel-securities.html). It joined trade execution, settlement, and secured financing in one workflow. The sequence matters more than token issuance alone because the Treasury representation remained useful after settlement as collateral for cash financing.

## From Tradeweb purchase to overnight funding

Citadel Securities bought the 2-year Treasury note through BNY on Tradeweb. BNY then recorded a tokenized representation of that security on its private digital ledger. The representation settled within minutes rather than following the standard T+1 settlement cycle. The announcement does not say whether BNY minted the representation before or after Tradeweb execution, or which ledger controls determined when settlement became final. It does establish that BNY treated the digital record as settled before the financing step began.

Settlement made the representation available for another institutional use after record creation. BNY's stated sequence was purchase, ledger recording, settlement, and repo collateralization. Each stage stayed inside a workflow operated or connected by BNY.

After settlement, Citadel pledged the tokenized Treasury to BNY in an overnight triparty repo. BNY supplied cash against the collateral. The repo therefore tested whether the digitally represented security could pass from a purchase into a financing transaction without waiting for the conventional next-day settlement window.

BNY's release describes the bank as the operator of the private ledger and the provider of cash in the overnight repo. Citadel was the Treasury buyer and collateral provider. Tradeweb handled the initial purchase venue.

BNY framed the workflow as a test of collateral mobility rather than a new Treasury instrument. The underlying asset was a U.S. Treasury note. The digital ledger held a representation of it, and that representation moved through settlement and financing. BNY said the transaction showed that tokenized Treasuries can support institutional activity from execution and settlement through short-term funding.

The release does not identify a public chain, contract address, transaction hash, security CUSIP, or ledger block. That limits independent verification of the settlement path and collateral movement. Readers can verify the participants' statements, the sequence they described, and the announced settlement speed, but not the ledger state from a public explorer.

## What changes for collateral desks

The immediate operational change is the gap between a settlement measured in minutes and the standard T+1 cycle cited by BNY. A dealer that receives the digital representation can put it into a financing workflow sooner, subject to the ledger's permissions and the triparty platform's controls. In this transaction, Citadel moved directly from acquiring the note to borrowing cash against it overnight.

BNY's clearance and collateral head, Brian Ruane, said Treasury infrastructure must keep pace as market activity becomes more continuous. He described tokenized collateral as a way to reduce friction while retaining the market structure that participants already use. Citadel's digital assets operations lead, Dan Doherty, focused on moving high-quality collateral from settlement into financing more efficiently.

For operators, the relevant test is whether the workflow repeats across more securities, counterparties, and funding windows. A private ledger can shorten the internal path between recording ownership and recognizing eligible collateral, but access depends on the institutions and systems connected to it. The announcement does not say whether another custodian or triparty platform can recognize the same tokenized representation.

Cash is also still split across the digital and traditional sides of the transaction. BNY said it plans to add digital cash and tokenized deposit capabilities for onchain settlement and institutional financing. The completed repo used BNY cash financing, while the release did not say that the cash leg settled as a tokenized asset. That leaves the securities leg ahead of the cash leg in the announced workflow.

## The next operating-hours test

BNY expects to extend operating hours for its traditional settlement platforms covering Fed-eligible securities and U.S. triparty transactions. The bank said it aims to reach European and Asian trading hours next year. It expects those longer operating windows and tokenization to develop together as support for 24/7 markets.

The completed transaction does not establish that BNY's Treasury settlement or triparty repo platform now operates around the clock. BNY presented extended traditional hours as a future change and digital cash as planned functionality. For a desk comparing the new workflow with current operations, the demonstrated result is narrower: one tokenized Treasury representation settled in minutes and then served as collateral for overnight funding. Broader operating hours and a digital cash leg remain later steps.

That plan gives collateral desks two distinct changes to watch. Longer traditional platform hours would make existing settlement rails available across more of the global trading day. Digital cash and tokenized deposits would address the other side of a tokenized financing transaction, allowing cash settlement to move closer to the same programmable workflow as the security and collateral records.

The open question is interoperability. BNY has shown that a Treasury representation on its own private ledger can settle in minutes and enter its triparty repo process. The release does not explain how that representation would move to another custodian, dealer ledger, or repo platform, or what happens when a participant must leave BNY's connected workflow. BNY's next dated milestone is the planned expansion into European and Asian trading hours in 2027.
