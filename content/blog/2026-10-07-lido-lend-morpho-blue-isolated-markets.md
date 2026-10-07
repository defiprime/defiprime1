---
layout: blog
title: "Lido Contributors Unveil Lido Lend Based on Morpho Blue"
url: /lido-lend-morpho-blue-isolated-markets.html
h1title: "Lido Contributors Unveil Lido Lend Based on Morpho Blue"
pagetitle: "Lido Lend Targets Isolated, Screened Lending Markets"
metadescription: "Lido contributors unveiled Lido Lend, a planned lending market based on Morpho Blue with isolated markets, deposit screening and defined exit paths."
category: blog
featured-image: /images/blog/lido-lend-morpho-blue-isolated-markets-ogp.png
intro: "Lido contributors have unveiled Lido Lend, a planned lending market based on a modified fork of Morpho Blue."
author: sawinyh
tags: ["Lending", "News"]
date: 2026-10-07T16:18:28+00:00
---

Lido contributors [unveiled Lido Lend](https://research.lido.fi/t/unveiling-lido-lend-security-first-lending/11987) on October 7, 2026, describing a decentralized lending market under development on a modified fork of Morpho Blue. The forum post sets out the intended design, but leaves the technical specification, market parameters, audits and governance votes for later disclosures.

The proposed system would use isolated lending markets rather than a general pooled market. It is aimed at long-term, passive on-chain asset holders seeking rewards and at professional borrowers who need predictable rules for leveraged positions. Lido contributors say governance would sit with Lido DAO if token holders accept the protocol through a future vote.

No market is live under the proposal, and the post does not publish contract addresses or launch parameters. It says Lido Lend is coming this quarter. Before that, contributors plan to release technical specifications, market parameters and audit reports in the same forum thread, ahead of governance votes covering launch and DAO acceptance.

The scope also separates the announcement from Lido's existing products. The contributors describe Lido Earn and stVaults as current DeFi primitives, while Lido Lend remains under development. They propose that the lending system complement Lido Earn and the stETH flywheel. The unveiling therefore establishes a product direction and a governance path. It does not establish an approved DAO deployment.

## How the proposed markets would work

Each Lido Lend market would be isolated. The proposal says every market would have its own scope, giving lenders visibility into its rules while separating asset selection from other markets. This differs from a general-purpose pooled design, where several collateral types and borrowed assets can share liquidity and risk controls. Lido's post describes the product as a specialized system for conservative lenders and professional borrowers.

The asset policy would favor blue-chip assets and price-correlated pairs. The example in the proposal is a stETH and $ETH market. Contributors say that correlation is intended to temper volatility. The initial concept therefore centers on narrower pairs rather than permissionless support for a long list of collateral assets.

Lido contributors also propose deposit screening and filtering of hacked funds. The post presents those controls as a way to close major attack vectors and guard lenders against bad collateral. It does not identify the screening provider, explain how an address would be classified, or specify who could block a deposit. Those details matter because screening can change who can enter a market and how operators respond when a classification is disputed.

Exit design is another stated priority. The proposal calls for reliable exits during full utilization or a liquidity crunch. It also says markets should maintain high liquidity across market conditions. The announcement does not yet explain the mechanism that would supply an exit when all lendable assets are borrowed. That answer will determine whether the design relies on withdrawal queues, reserved liquidity, external liquidity or another method.

Borrowing is intended to support extended looping positions under clear rules. Contributors say those positions should remain possible to unwind during stressful conditions. The post gives no liquidation thresholds, loan-to-value limits, oracle design or interest-rate model. Without those parameters, users cannot yet compare the claimed predictability with existing Morpho Blue markets or estimate the cost of unwinding a loop.

## What changes for lenders and borrowers

For lenders, the proposal narrows the product's mandate. Lido Lend is being built for passive holders who want rewards without hidden risk exposure, according to its contributors. Its planned controls combine isolated markets, selected assets, deposit screening and explicit exit paths. Each control is described at the policy level. None can be evaluated against code or audit findings until the promised technical package is published.

For borrowers, the expected use case is concentrated. Lido contributors call the system purpose-built for looping on one side and conservative lending on the other. Correlated pairs such as stETH and $ETH can reduce price divergence between collateral and debt, but the proposal does not claim that such positions are free from liquidation, oracle or liquidity risk. Its stated goal is to make borrowing rules clear and predictable enough that extended loops can be unwound.

The proposal also puts a new product beside Lido Earn and stVaults. Contributors say Lido Lend would complement both products and the stETH flywheel. Lido's forum post cites more than $25B staked in stETH and six years of infrastructure work as reasons the contributors believe the organization can extend into lending. It also says Lido has had zero major security incidents since inception. These are claims in the proposal, not substitutes for the separate audits promised for Lido Lend.

## The decisions still ahead

The announcement is the start of a governance process rather than approval to launch. Contributors propose Lido DAO governance, pending acceptance by a vote. They also refer to relevant governance votes for both launch and protocol acceptance, which indicates that the DAO will receive more than the initial concept before making a decision.

The next release should answer the operational questions the unveiling leaves open. The promised specifications need to identify market creation powers, collateral selection, oracle sources, interest rates, liquidation rules and the exit mechanism. The market parameters should show how much discretion governance or other operators retain. Audit reports should identify the exact code reviewed and any unresolved findings.

Lido contributors say they will publish those materials over the next few weeks and that Lido Lend is coming this quarter. The next verifiable milestone is the technical post ahead of the governance votes. Until then, the proposal defines the intended users and safeguards, but not the contracts or parameters that would put user funds at risk.
