---
layout: blog
title: "Aegis deploys liquidation hedging contracts before live execution is ready"
url: /aegis-hedging-testnet-still-needs-live-execution.html
h1title: "Aegis deploys liquidation hedging contracts before live execution is ready"
pagetitle: "Aegis deploys liquidation hedging contracts on Elysium testnet"
metadescription: "Aegis has contracts on Elysium testnet, but its native price and order interfaces still have no code. Here is what users can verify."
category: blog
featured-image: /images/blog/aegis-hedging-testnet-still-needs-live-execution-ogp.png
intro: "Aegis has deployed its liquidation hedging stack on Elysium testnet while keeping execution in dry-run mode until the network exposes its native price and order interfaces."
author: sawinyh
tags: ["Analysis", "DeFi"]
date: 2026-10-17T06:19:35+00:00
---

On October 15, 2026, [Aegis introduced](https://x.com/aegis_hedge/status/2110779116500726076) a non-custodial risk-management layer for Elysium. The repository identifies the network as Elysium testnet, Chain ID 99801. At block 10,421,030, the deployed Aegis vault held 9,155 bytes of runtime code. The native price and order addresses that the final design expects, 0x0801 and 0x0802, each held 0 bytes.

That split defines the launch. The contracts and adapters exist on testnet, but the protocol cannot yet run the native hedge path described in its pitch. Aegis currently depends on relayed data and an offchain dispatcher. Its own readiness plan says the keeper must remain in dry-run mode while the native interfaces are unavailable or unverified.

## What the hedge is supposed to do

Aegis is designed for borrowers who want to keep spot collateral instead of having a lending protocol sell it after a health threshold breaks. The [repository describes](https://github.com/youngcrypton/Aegis/blob/main/README.md#executive-overview) a sentinel that watches a collateralized position and opens a short perpetual position on HyperCore when the position approaches liquidation. The short is intended to offset the collateral's falling dollar value.

The exit is tied to a rebound rather than a fixed holding period. The sentinel tracks the lowest observed price while the short is open. Once the market rises by the user's trailing tolerance, the system buys back the short. The repository says the resulting trading profit is credited to the vault to improve its health factor. This leaves the spot collateral in the vault, although the borrower still carries execution, funding, basis, oracle, and smart-contract risk.

A delegated session key is the control surface for automated trading. The [verification dossier](https://github.com/youngcrypton/Aegis/blob/main/docs/FACT_CHECK_AND_VERIFICATION_DOSSIER.md#claim-1-strict-non-custodial-bounds-invariant-inv-1) says the key can execute trade-only short hedges and has no token transfer, withdrawal, or approval path. The vault also exposes a manual override that clears the caller's session key and emits a revocation event. Those limits matter because the keeper needs authority to react without waiting for the borrower, but it should not gain general custody of the collateral.

The proposed fee path separates hedge proceeds from protocol revenue. The repository says 90% of net trading proceeds would stabilize vault debt and a 10% performance fee would go to the fee collector. Inside the collector, the implementation divides each fee into two shares: one half for the proposed buyback path and the remainder for sentinel yield. If fee collection fails during an unwind, the vault records a fee debt instead of reverting the safety action.

Those mechanics are code and testnet design claims. They are not evidence that the hedge has protected a live borrower during market stress.

## What is actually deployed

The current [deployment manifest](https://github.com/youngcrypton/Aegis/blob/main/deployments.json) points to vault 0xC064495DE20EfeEBB6a4B1dE57ffb48ED8f5dA29, oracle adapter 0x8829386b87F6CFbf64A3f75916BC96bAb0B12991, writer adapter 0xBAD4C895DBcA78F10764D73274dC1f314c80237e, fee collector 0xCA9D24c4B5025dA065d1AEf92808aB1698f267ae, and sentinel registry 0x6C64188e1D677Eb85E4aD71836650310281f0893.

A pinned RPC reading at 06:17:12 UTC on October 17 found runtime code at all five addresses. The [vault](https://elysium.kinetiq.xyz/testnet-explorer/address/0xC064495DE20EfeEBB6a4B1dE57ffb48ED8f5dA29) had 9,155 bytes, the fee collector had 4,240 bytes, the oracle adapter had 2,092 bytes, the registry had 4,223 bytes, and the writer adapter had 1,045 bytes at block 10,421,030. Canonical testnet $USDC and wrapped $HYPE addresses named in the manifest also had runtime code at that block.

The reading establishes that the current manifest points to contracts with code. It leaves the match between source and bytecode, constructor arguments, ownership data, external dependencies, and transaction history unverified.

The more important result sits at the expected native interfaces. Address 0x0801 had no runtime code at block 10,421,030. Address 0x0802 also had no runtime code. Aegis's [technical dossier says](https://github.com/youngcrypton/Aegis/blob/main/docs/FACT_CHECK_AND_VERIFICATION_DOSSIER.md#fact-check-a-are-precompiles-0x0801-and-0x0802-live-on-elysium-testnet-today) the first address returns empty bytes and the second reverts on the current network.

The missing code prevents the final path from working as presented. The price adapter cannot read native HyperCore market data through 0x0801, and an EVM call cannot dispatch a trade through 0x0802. The protocol therefore uses a relayed oracle adapter and an agent dispatch adapter in its current testnet mode. The [dual-mode document](https://github.com/youngcrypton/Aegis/blob/main/gitbook/chapter-2-architecture/dual-mode-framework.md#1-the-two-execution-modes) describes the dispatcher as emitting EVM events for sentinels, while the proposed post-hardfork mode would make a synchronous cross-domain call to HyperCore.

This distinction changes the trust model. A native precompile would place pricing and order submission inside the network's execution environment. The current route depends on relayed prices and offchain keeper infrastructure. The readiness plan requires the keeper to stay at DRY_RUN=true until the interfaces are verified, so the present deployment is a test harness for the mechanism rather than a production liquidation backstop.

## Where protection can fail

Liquidation protection has a narrow timing requirement. A useful hedge must receive a current price, calculate the required short, obtain authorization, reach an orderbook, and fill before the lending position crosses its liquidation threshold. The current Aegis route has an offchain component at both the data and dispatch boundaries. Its relayed oracle enforces staleness checks, while the dispatch adapter emits an event for a sentinel instead of placing the order through a native network interface.

That architecture gives testers observable contract events, but it does not give borrowers synchronous settlement. A keeper can be unavailable after the event is emitted. A relayed price can pass its configured check and still differ from the price available on the execution venue. An order can arrive after collateral has already been liquidated, or fill only in part. The project itself says market liquidity, execution latency, price gaps, borrowing rates, slippage, and venue availability can prevent a hedge from avoiding liquidation.

A short perpetual also moves risk instead of removing it. The borrower retains the spot collateral and gains an offsetting derivative position. That derivative needs margin, available orderbook liquidity, and a reliable close. If the rebound exit does not execute, the short remains open against the collateral. If the market rebounds quickly, losses on the short can offset the recovered value of the spot position until the unwind completes. The mechanism therefore depends on both entry and exit execution.

The manual override is useful when a borrower wants to revoke the delegated key. It does not complete a pending hedge or close an existing position by itself. The deferred-fee rule solves a different problem: a failed fee transfer should not block an unwind. It leaves fee debt for later collection, so operators need a way to expose that debt and prevent it from being lost during contract replacement or account migration.

Dry-run mode avoids presenting these untested paths as live protection. It also means a successful interface simulation cannot be read as evidence of a successful hedge. The production test has to join the full sequence: a live market input, an authorized order, a confirmed fill, a tracked low, and a confirmed unwind. Each step should be linked to the same vault and visible in transaction or order records.

## The controls that still need work

The session-key restrictions reduce one category of risk, but ownership remains concentrated. The [readiness plan](https://github.com/youngcrypton/Aegis/blob/main/docs/audits/AEGIS_TESTNET_TO_MAINNET_READINESS_PLAN.md#32-key-architectural-takeaways) says ownership of the vault, fee collector, and registry is assigned to a single developer EOA. It calls for a production multisignature safe and an onchain timelock before mainnet. The same plan says the yield distribution target currently points to the deployer EOA and needs an audited distributor contract.

Token bindings create another deployment constraint. The fee collector and registry use immutable token addresses. The plan says mainnet contracts cannot be deployed safely until canonical $USDC and $AEGIS contracts exist and have been verified on Elysium mainnet. A wrong immutable address would require replacement contracts rather than an administrative update.

The project also needs to reconcile its public documentation with the active manifest. The fact-check dossier lists an older set of vault and adapter addresses than deployments.json. That does not by itself show a fault, since testnet contracts are often replaced. It does mean users should start with the current manifest, verify its commit and deployment transactions, and avoid assuming that evidence collected for an earlier address still applies.

The deferred-fee path deserves separate review. Recording unpaid fees instead of reverting can keep an unwind from failing, but it creates an obligation that must be measured and collected later. The code's behavior under partial fills, stale prices, unavailable orderbooks, and repeated keeper failures will matter more than the happy-path simulation. The current readiness document explicitly separates simulated stress tests from production execution.

## What users can verify next

For now, prospective testers can confirm the Elysium chain, inspect the five deployed contracts, and check that 0x0801 and 0x0802 remain empty at a chosen block. They can also inspect the vault's session-key revocation and deferred-fee code in the repository. None of those checks requires depositing assets.

The next meaningful milestone is native execution. Elysium must expose and document the interfaces, after which Aegis must show verified contract upgrades, live price reads, and successful trade dispatches against the intended orderbook. The keeper then needs to leave dry-run mode under a disclosed operational policy. Until those steps are observable, Aegis remains a testnet architecture for liquidation hedging. It does not yet replace liquidation.
