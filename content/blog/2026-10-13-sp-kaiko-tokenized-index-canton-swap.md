---
layout: blog
title: "S&P and Kaiko put a tokenized bond index into a Canton swap"
url: /sp-kaiko-tokenized-index-canton-swap.html
h1title: "S&P and Kaiko put a tokenized bond index into a Canton swap"
pagetitle: "S&P, Kaiko complete tokenized-index Canton swap"
metadescription: "DRW and Marex completed a Canton total return swap tied to a Kaiko-tokenized S&P iBoxx investment-grade bond index."
category: blog
featured-image: /images/blog/sp-kaiko-tokenized-index-canton-swap-ogp.png
intro: "S&P DJI, Kaiko, and Derivnex completed Canton's first OTC swap tied to a fully tokenized index, with DRW and Marex as counterparties."
author: sawinyh
tags: ["News", "RWAs"]
date: 2026-10-13T12:30:07+00:00
---

S&P Dow Jones Indices, Kaiko, and Derivnex [announced](https://www.prnewswire.com/news-releases/sp-dow-jones-indices-and-kaiko-enable-first-on-chain-otc-swap-referencing-a-tokenized-benchmark-executed-by-drw-and-marex-on-derivnex-302907001.html) at 08:00 ET on October 13, 2026 that DRW and Marex had completed the first OTC swap transaction on the Canton Network. The total return swap references the iBoxx USD Liquid Investment Grade Index, which Kaiko tokenized on Canton.

The parties describe the transaction as the first OTC derivative to reference a fully tokenized index on distributed ledger infrastructure. It connects an established bond benchmark to a live bilateral derivatives workflow rather than issuing a token that merely tracks an index for informational use.

## What moved onchain

The swap gives DRW and Marex exposure to the performance of the iBoxx index without requiring either counterparty to own the underlying bonds. The parties negotiated the contract privately, as is standard for an OTC swap. The onchain component changes how the trade and its supporting data are represented and managed after execution.

Derivnex represented the trade on Canton as a smart contract containing its transaction terms. That contract is designed to stay with the trade through its lifecycle. Both counterparties therefore use a synchronized record when they manage valuations and other lifecycle events.

This matters because a conventional bilateral swap can span separate trade-capture, valuation, communication, and reconciliation systems. Derivnex [describes its platform](https://derivnex.com/) as a post-trade engine for affirmations, valuations, cash-flow calculations, and payment coordination. The platform requires bilateral agreement before affirmations, valuations, and cash amounts advance to the next state.

The transaction did not put the bond portfolio itself on Canton. Kaiko tokenized the benchmark that defines the swap's reference performance. The token combines index data with access permissions and usage rules. Those controls are intended to let authorized participants consume the benchmark inside digital financial workflows while preserving S&P DJI's licensing and intellectual-property restrictions.

Kaiko also distributed signed official index values from S&P DJI. Derivnex uses those values to price the position through its lifecycle. The tokenized benchmark supplies the licensed reference data, while the signed values supply the inputs used for ongoing valuation.

## The operating model

Derivnex incorporates the Common Domain Model, which provides a standardized digital representation for derivatives transactions and lifecycle events. Canton supplies permissioned execution and privacy. The result is a shared contract state that the two counterparties can use without making the trade visible to every network participant.

The workflow begins with one set of trade terms in shared, permissioned state. Each counterparty reviews and affirms those terms. The same state then carries agreed valuations into exposure views and turns the agreed data into resets, coupons, fees, and payment amounts. Derivnex says payment coordination can include netting and stablecoin workflows where applicable. The announcement does not say that this particular swap used either feature.

That sequence separates the transaction from a simple record of a completed trade. The contract remains active as the parties value the position and process lifecycle events. Versioned bilateral approvals create an audit history for changes. Counterparty-level visibility restricts the trade data to authorized participants, while both sides work from the same record.

The split between the benchmark token and the swap contract is also operationally important. The benchmark token governs access to S&P DJI's index data. The Derivnex contract holds the bilateral transaction terms. Signed index values pass from the first layer into the second for valuation. This arrangement lets the benchmark owner maintain licensing controls without becoming the seller or sponsor of the derivative. It also lets DRW and Marex manage their contract without receiving an unrestricted copy of the index feed.

For operators, the immediate change is narrower than instant settlement. DRW and Marex gain one record for the terms and valuations that both sides can inspect and approve. That can reduce the scope for mismatched versions of a trade, although the announcement does not quantify any reduction in breaks, processing time, or operating cost.

Benchmark distribution also changes. S&P DJI can attach permissions and usage rules to the tokenized index instead of sending unrestricted benchmark data into a separate workflow. Kaiko can distribute signed values into the same environment where Derivnex manages the swap. The structure gives a benchmark owner an auditable route for controlling who can use its data in a financial contract.

The parties have not disclosed the swap's notional value, maturity, payment schedule, margin terms, or collateral. They also have not published a Canton transaction identifier that an outside reader can use to inspect the trade. Canton's permission model may limit public visibility in any case, but the missing identifiers mean the announcement remains the available record of execution.

The index is licensed for use by DRW and Marex Solutions. S&P DJI states that products tied to the index, including OTC swaps, are not sponsored or sold by S&P DJI and that the index provider does not assess whether investing in those products is advisable. That distinction keeps benchmark licensing separate from the bilateral credit and trading relationship.

## What comes next

The release says future functionality is expected to connect Derivnex-managed positions with digital cash and collateral on Canton. The intended workflow would let margin, collateral, and contractual payments move on the same infrastructure as the trade representation. That capability was not part of the transaction announced on October 13.

Until that integration exists, the completed swap demonstrates shared trade state, controlled benchmark delivery, and coordinated valuation. It does not establish atomic settlement of the derivative against onchain cash or collateral. The next test is whether Derivnex can connect those payment and collateral legs while preserving the bilateral privacy and licensing controls used for this trade.
