---
layout: blog
title: "Phylax brings Ethereum circuit breakers to Titan Builder"
url: /phylax-titan-ethereum-circuit-breakers.html
h1title: "Phylax brings Ethereum circuit breakers to Titan Builder"
pagetitle: "Phylax brings Ethereum circuit breakers to Titan Builder"
metadescription: "Phylax says Titan Builder now checks protocol-defined risk rules on Ethereum, with opt-in guards restricting protected calls to participating builders."
category: blog
featured-image: /images/blog/phylax-titan-ethereum-circuit-breakers-ogp.png
intro: "Phylax says its Ethereum expansion lets protocols register risk rules for Titan Builder to enforce during block construction, with onboarding still in closed beta."
author: sawinyh
tags: ["News"]
date: 2026-11-11T10:24:07+00:00
---

On November 10, 2026, Phylax brought its circuit breakers to Ethereum through Titan Builder, according to its [launch announcement](https://phylax.systems/blog/phylax-and-titan-bring-circuit-breakers-to-ethereum/). Protocols can define unacceptable risk outcomes for the builder to check during block construction. Titan excludes state changes that violate those rules before settlement.

Phylax describes Titan as Ethereum's leading builder, producing roughly 50% of blocks. That figure comes from the company; it was not independently measured for this article. Protocols opt in to the checks, which run through participating builders. The release explicitly says the checks do not run in every Ethereum block by default.

The Ethereum expansion follows an existing production service. Phylax says its Credible Layer has operated on Linea since January 2026 and names Derive and Lighter as production users. The Titan integration brings that runtime enforcement to Ethereum. New protocol and vault teams still enter through a closed beta, starting with a technical assessment.

## Rules checked before settlement

Applications specify the states they refuse to accept. During block construction, Phylax checks the prospective state change against those rules, and Titan excludes violations. The builder makes that decision before settlement, while it can still leave the offending state change out of the block.

The release illustrates the process with a vault withdrawal rule written in Solidity and registered against the vault's smart contract. The example caps the value leaving in one transaction at 50% of total assets under management. A vault team could choose that policy. The release does not announce it as a default withdrawal cap for every integrated application.

In this example, Titan runs each transaction touching the vault and checks the result against the registered rule. It leaves out an oversized withdrawal that fails the check. Phylax says the vault team then receives full traces of the attempted transaction, which it can use to investigate what happened and patch the issue.

The [product documentation](https://docs.phylax.systems/credible/credible-introduction) covers policies beyond withdrawal limits. Rules can constrain administrative changes, collateralization and oracle deviations, as well as relationships between balances or positions. Teams choose constraints that fit their protocol's normal operations. What the system protects depends on the policy the team registers for enforcement.

Phylax places circuit breakers alongside audits, formal verification, monitoring and incident response, each with a different job. Audits and formal verification help find problems before deployment. Monitoring and incident response help detect and contain problems in production. The release calls those measures essential and identifies attacks completed within a single block as the problem circuit breakers address. In the scenario it describes, post-block detection comes after the capital has already moved.

## Protected calls depend on participating builders

The proposed defense against routing around the checks sits in the protocol contract. A team marks a function, such as a withdrawal, as protected. The function can complete only in a block that a participating builder has marked as checked. Through another builder, the protected state change fails. The release describes this contract guard as the means of preventing an attacker from bypassing enforcement by choosing a different builder.

Titan is the first participating builder, according to Phylax, and the company says any builder can choose to run its enforcement system. The roughly 50% builder-share figure describes Titan's stated reach. Protection still depends on a protocol opting in and its protected calls reaching a checked block; the figure is not a claim that half of all Ethereum activity is protected or that applications receive automatic coverage.

Policy design also determines which legitimate transactions can proceed. The documentation gives an ownership-change rule as an example: a rule rejecting every ownership change would also reject a planned transfer to a new governance contract. Teams must account for legitimate exceptions when they specify harmful outcomes, including administrative operations they intend to carry out.

## Protocol teams retain the authority

Phylax describes circuit breakers as veto rights. A rule can prevent a transaction, but it cannot initiate or alter a state change. Its scope is limited to contracts the protocol controls. Registering a rule gives the application authority over its own state, not over transactions involving contracts outside that authority.

The protocol alone authorizes and approves its rules and decides when they become active, according to the release. It can change or remove them at any time. Phylax describes its platform as a convenience for managing assertions, the rules an application registers for enforcement. Teams can also use the Phylax smart contracts directly to modify their rules independently of the company, without going through its platform.

Integration begins with Phylax engineers working with the team to identify where enforcement could apply. They help write and test rules and establish what the integration requires. The documentation includes contract changes and transaction-routing changes within an agreed scope. Those changes are prepared for the protocol team's review before production activation.

Testing uses a replica of the protocol on a fork of Ethereum. Phylax says the process includes backtests, legitimate and violating transactions, investigation of false positives, and recovery rehearsals. The tests check whether the rules catch forbidden state changes and whether the protocol's intended operations can still execute under them.

The protocol team reviews the policies and evidence, approves changes and retains control of production signing. Phylax prepares and simulates activation transactions; the team's signers authorize and execute them. The documentation then calls for verification of live protection, followed by monitoring, incident response and policy changes under an operating plan agreed with the team.

This account relies on Phylax's release and documentation; no on-chain measurements were made for this article. Phylax describes production use and a live Ethereum expansion, but onboarding for new teams remains a closed beta.
