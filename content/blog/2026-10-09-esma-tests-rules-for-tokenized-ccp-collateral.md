---
layout: blog
title: "ESMA tests rules for tokenized CCP collateral"
url: /esma-tests-rules-for-tokenized-ccp-collateral.html
h1title: "ESMA tests rules for tokenized CCP collateral"
pagetitle: "ESMA opens tokenized CCP collateral review"
metadescription: "ESMA is examining whether tokenized securities and cash can serve as CCP collateral without weakening legal certainty, liquidity or resilience."
category: blog
featured-image: /images/blog/esma-tests-rules-for-tokenized-ccp-collateral-ogp.png
intro: "ESMA has opened a call for evidence on how EU clearing houses could accept tokenized collateral while preserving existing safeguards."
author: sawinyh
tags: ["Regulation", "News"]
date: 2026-10-09T14:21:56+00:00
---

On October 9, 2026, the European Securities and Markets Authority [opened a call for evidence](https://www.esma.europa.eu/sites/default/files/2026-10/ESMA91-1505572268-4934_-_Call_for_evidence_tokenisation.pdf) under reference ESMA91-1505572268-4934 on tokenized collateral at central counterparties. ESMA will accept comments through January 15, 2027, then assess the feedback in the first quarter of 2027 before deciding whether to act.

The review asks whether tokenized securities and tokenized forms of cash can be used safely and effectively by EU CCPs. It does not propose adding new categories of eligible collateral. ESMA is instead testing whether tokenization changes how an otherwise eligible asset is moved, managed, protected and converted into funds during a member default.

The intended respondents include CCPs, clearing members and their clients. ESMA also addresses central securities depositories, custodians, triparty agents, tokenization providers, legal experts and firms building digital financial infrastructure. That scope reflects the number of systems and legal relationships between a token and cash that a clearing house can use.

## The two operating models

ESMA groups current designs into digital twins and assets issued natively on a distributed ledger, while allowing that a system may combine both. A digital twin represents an asset still recorded in conventional infrastructure. The token may mirror rights held elsewhere, represent an individual claim on a custodial pool, or help mobilize the asset without becoming the authoritative ownership record.

That model creates a reconciliation question. Operators must know whether the ledger, a custodian's books or another record prevails when records disagree. In a default, the token layer may identify and pre-position collateral, but a sale or repo can still depend on the custodian or securities depository. Reconciliation, confirmation and messaging can add steps before the CCP gets usable liquidity.

A native model puts issuance, ownership and transfer on the ledger. Posting, monitoring and updating collateral positions can occur in the same environment. Access to value then depends on the ledger, its controls, connected settlement mechanisms and available liquidity. Technical control of a token or private key does not by itself establish legal ownership because property, securities and insolvency rules still determine the right that a CCP can enforce.

For both models, ESMA says tokenization should not lower the standards applied under EMIR. Collateral still needs legal enforceability, settlement certainty, prudent valuation, liquidity and operational resilience. The regulator wants evidence on whether existing EU rules can produce those outcomes when ownership records and operational control are split across conventional and ledger-based systems.

Client protection cannot stop at wallet separation. A workable design must attribute assets to each participant in a legally recognized way, prevent unauthorized use or double use, and preserve those controls through default or insolvency. It must also support the transfer of positions and collateral to a backup clearing member within the available window. ESMA warns that a holder without enforceable proprietary rights could instead rank as an unsecured creditor.

Settlement needs a legal endpoint as well as a technical one. CCPs must know when a collateral transfer becomes definitive and cannot be reversed later in an insolvency proceeding. Without that point of finality, an exposure treated as extinguished could return after the event, disrupting margin calculations, liquidity plans and the default process.

## Liquidity is measured at default

The paper separates the economics of an asset from the route used to realize it. A tokenized government bond starts with the credit and market risk of the conventional bond. Its collateral treatment can still change if selling, repoing or redeeming the token takes longer, relies on one platform, or introduces conversion and cyber risks.

Tokenized cash presents a related problem. ESMA lists tokenized central bank money, stablecoins, e-money tokens and tokenized deposits as possible settlement assets. Some may not qualify as cash under regulatory or supervisory frameworks. Stablecoins can deviate from par, while other instruments may depend on an issuer's credit, redemption terms, conversion systems or intermediaries. A CCP therefore needs to know whether the instrument legally discharges the obligation and whether it can obtain the required currency within the default-management window.

Automation can also compress that window. Faster settlement and conditional transfers may reduce routine friction, but they can increase intraday liquidity needs by giving members less time to find eligible assets. Common triggers could cause many firms to move collateral at once during stress, increasing demand for the same assets and adding procyclical pressure. Those effects can feed into eligibility decisions and haircut calibration.

## What operators need to prove

ESMA's operational tests extend beyond whether a ledger stays online. A digital twin can fail through a coding or reconciliation error even when the underlying security remains safe in custody. A native asset can become unavailable through failures in node operations, permissions, smart contracts or key management. Interfaces to custodians, settlement links and tokenized cash arrangements can become critical dependencies as well.

The paper asks for technical and process testing before CCPs rely on these arrangements broadly. Its scenarios include platform outages, compromised private keys, failed reconciliation, smart contract malfunctions, governance intervention and stressed conversion into usable liquidity. Firms also need fallback arrangements and evidence that a critical provider can be replaced. Reliance by several CCPs on the same platform, cloud service, wallet system or developer could turn a vendor failure into a market-wide bottleneck.

Interoperability is the remaining constraint. ESMA argues that an eligible asset should not become captive to one venue or collateral platform merely because it has been tokenized. Closed systems can limit mobility, reduce substitutability and weaken the liquidity case for the asset precisely when a CCP needs to use it.

For clearing members and infrastructure providers, a useful response must therefore trace the full path from legal ownership to cash in a default. It must identify the controlling record, settlement point, conversion route, failure dependencies and tested fallback. ESMA will use the submissions received by January 15 to decide in the first quarter of 2027 whether current rules are sufficient or need clarification.
