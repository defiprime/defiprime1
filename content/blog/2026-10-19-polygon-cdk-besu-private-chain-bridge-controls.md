---
layout: blog
title: "Polygon adds Besu to CDK with separate bridge and validator controls"
url: /polygon-cdk-besu-private-chain-bridge-controls.html
h1title: "Polygon adds Besu to CDK with separate bridge and validator controls"
pagetitle: "Polygon CDK Besu: private chains and bridge controls"
metadescription: "Polygon's CDK Besu launch connects private ledgers to Agglayer. Its proofs limit bridge withdrawals, while validators retain control over chain execution."
category: blog
featured-image: /images/blog/polygon-cdk-besu-private-chain-bridge-controls-ogp.png
intro: "Polygon added a production-ready Besu configuration to CDK, with public instructions for connecting private institutional chains to Agglayer."
author: sawinyh
tags: ["Payments", "News"]
date: 2026-10-19T17:22:20+00:00
---

Polygon [added Besu as a supported CDK configuration](https://polygon.technology/blog/introducing-cdk-besu) on October 19, 2026, giving banks and other institutions a documented deployment path for private chains connected to Agglayer. Polygon says the configuration is ready for production on Ethereum mainnet, with testnet and devnet setups available for evaluation.

The release pairs the standard Besu client and QBFT consensus with Agglayer's bridge infrastructure. An institution or consortium runs the validators and decides which accounts can transact. Transaction data stays inside that private infrastructure. The bridge connection is included from genesis, instead of being added after the network starts operating.

Polygon's public documentation sets out the limits of the bridge's security. The pessimistic proof limits what a connected chain can withdraw from the shared bridge. Internal transactions still depend on the chain's own validators, and their data is not posted to Ethereum.

## What the bridge proves

The [CDK Besu overview](https://docs.polygon.technology/chain-development/cdk/cdk-besu/overview) describes a sovereign-mode deployment using the `AggchainECDSAMultisig` consensus contract. It supports settlement on Sepolia or Ethereum mainnet and includes an optional consortium configuration. The runbook creates a new chain with both the bridge and Global Exit Root contracts already in its genesis.

The proof checks that a chain cannot withdraw more than it deposited. Polygon presents that accounting limit as protection for other connected chains when a member chain fails or is compromised. A compromised chain can still lose its own deposits. The documentation explicitly says the pessimistic proof does not prove the chain's internal state transitions.

That leaves execution under the private ledger's controls. Besu validators maintain the chain's state, while account permissioning determines who can use it. Polygon points institutions that require every state transition to be proven toward its CDK configuration on op-reth, which supports full zero-knowledge execution proofs. The Besu path uses pessimistic proofs only.

Settlement continues after the chain produces a block. Agglayer requests a pessimistic proof generated on the Succinct Prover Network. Once that proof is verified, the certificate settles on Ethereum. The bridge service then picks up the settled transfer and the asset is claimed on the destination chain. A local block and a completed cross-chain claim are separate stages of this process.

A dedicated RPC node serves the connection so the validators can stay off the public network. Polygon's deployment instructions direct aggkit, the bridge service and users to that node. Operators must include their hostnames in its host allowlist. The public documentation covers the machinery that handles settlement and the network access configuration operators need to run it.

## Consortium approvals remain explicit

The consortium option separates block production from certificate approval. Each member operates its own QBFT validator and retains its validator key. Changes to membership go through a validator vote. Polygon recommends four or more validators for testnet and mainnet; a single-validator devnet stops if that validator fails.

Certificate approval uses a separate signer set. The `AggchainECDSAMultisig` contract requires M of N registered signers to approve each certificate. One member runs the proposing aggsender. Other members run aggsender validators that check the certificate against their own view of the chain before approving it. This consortium authorization process applies alongside the bridge's proof requirements.

The order of addresses in the signer list also determines whether certificates can be sent. The first address in the consensus contract's signer list must be the aggsender address. Otherwise, the aggsender refuses to send certificates. Operators must satisfy that requirement as well as the shared approval threshold.

Account permissioning must also cover the services that keep the connection working. When an operator enables an account allowlist, the instructions require adding the aggoracle and ClaimTxManager addresses before starting aggkit and the bridge service. Every validator and RPC node must use the same allowlist. The institution must configure its user admission policy at the infrastructure level, beyond front-end access.

## Deployment has compatibility and key requirements

The documentation calls for aggkit 0.9 or later. Earlier versions recompute block hashes in a way that never matches a QBFT block hash, preventing aggkit from building a certificate. The [prerequisites runbook](https://github.com/0xPolygon/cdk-besu/blob/main/00-prerequisites.md) explains that the mismatch causes the bridge syncer to drop blocks carrying bridge events.

Finality settings need a Besu-specific configuration too. QBFT finalizes each block when it is produced, but Besu does not serve the `safe` and `finalized` block tags used in other execution setups. The instructions require every aggkit block-finality setting to use `LatestBlock`. These are deployment requirements published with the release, not findings from an independent test of a running chain.

The prerequisites also distinguish devnet examples from production key handling. Although example commands pass private keys directly on the command line, the runbook instructs testnet and mainnet operators to use a keystore or hardware wallet instead. It warns against putting private keys in shared terminals or committing environment files that contain them.

Polygon singles out the deployer, admin and Aggchain manager keys as especially sensitive, calling compromise of any of them unrecoverable. Validator node keys also authorize block signing. The deployment guide assigns responsibility for custody of these keys to the operator, alongside the protection provided by the bridge proof.

The software uses the standard Besu client. Polygon says operators have no proprietary client to adopt, no fork to maintain and no revenue share owed on network activity. Its [rollup-creation instructions](https://github.com/0xPolygon/cdk-besu/blob/main/01-rollup-creation.md) begin with the Agglayer integration process, which produces the `combined.json` artifact required for the later genesis steps.

Existing Besu networks follow a different route. The documentation directs chains with their own history to Agglayer Outpost and says that path is outside this new-chain runbook. Polygon asks existing operators to contact its team about connecting their networks; the published CDK Besu procedure covers starting a new one.
