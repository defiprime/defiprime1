---
layout: blog
title: "Aero merger opens token migration and replaces weekly voting"
url: /aero-merger-migration-rewards.html
h1title: "Aero merger opens token migration and replaces weekly voting"
pagetitle: "Aero merger: token migration, LP rewards and lock changes"
metadescription: "Aerodrome and Velodrome combine as Aero. Migration changes token contracts, liquidity rewards and locked positions, with separate timing for final-epoch voters."
category: blog
featured-image: /images/blog/aero-merger-migration-rewards-ogp.png
intro: "Aerodrome and Velodrome launch Aero across seven networks, requiring holders and liquidity providers to migrate to keep earning its token rewards."
author: sawinyh
tags: ["News"]
date: 2026-10-22T00:22:31+00:00
---

At 00:00 UTC on October 22, 2026, Aerodrome and Velodrome's merger into Aero reaches its scheduled launch, replacing their separate token-reward systems with a shared exchange across seven networks. Aero's [launch announcement](https://aero.xyz/articles/aero-launches-today/) allocates 94.5% of the upgraded supply to the Aerodrome community and 5.5% to Velodrome holders.

The supported networks are Base, Ethereum mainnet, Optimism mainnet, Arc, Ink, Robinhood Chain and Arbitrum. The operator directs holders to the existing Aerodrome and Velodrome sites for upgrades and liquidity migration. Staking, allocation and new pools are available through the Aero app.

Under the [upgrade hub's instructions](https://aero.xyz/aero-upgrade/), legacy emissions end at launch. Holders must upgrade their tokens manually to keep earning the new exchange's token rewards. Liquid $AERO and $VELO convert into new $AERO, while locked veAERO and veVELO positions become sAERO. None of these holdings convert automatically.

## Conversion changes tokens and position IDs

Aerodrome tokens convert one for one. The hub estimates that each Velodrome token converts into approximately 0.044 new $AERO. The precise rate reflects supply at launch and Velodrome's allocation. Liquid and locked holdings receive the same conversion treatment. According to the launch announcement, the entire upgraded supply goes to existing holders, without a venture allocation or token sale.

Velodrome's migration crosses networks. Old $VELO starts on Optimism mainnet, while upgraded $AERO arrives on Base. Holders of bridged xVELO must return it to Optimism mainnet before upgrading. Aerodrome upgrades require network fees in $ETH on Base; Velodrome upgrades require $ETH on Optimism mainnet. Multisig and contract-wallet users must confirm a receiving address that supports Base.

New liquid tokens become transferable when the upgrade completes. Each centralized exchange controls the migration process and timetable for balances it holds in custody. Aero has coordinated with exchanges on the upgrade, but customers must follow their exchange's instructions for those balances.

Only the wallet that owns a veNFT can upgrade it. Positions held in vaults, lending markets or other contracts must return to their owner, or the protocol holding them must perform the upgrade. The hub gives a specific sequence: claim rewards and rebases, reset votes, then upgrade. Anything left unclaimed cannot be recovered afterward.

The upgrade retires the old veNFT and issues a new sAERO position. Integrations that track positions by NFT ID must map the replacement. Remaining lock time carries over, rounded up to the next full week. Permanent locks become positions at maximum stake duration. Holders can combine positions at launch, but they cannot split them.

The hub schedules migration for final-epoch voters at 01:00 UTC on October 22, an hour after launch. That interval allows final protocol operations to finish before those holders claim and upgrade. Liquid tokens and veNFTs that did not vote in the final epoch can upgrade from launch.

## Liquidity needs its own migration

The portals support moving deposits into Aero pools, though some old pools lack a comparable destination at launch. Those deposits require manual withdrawal. Users can create new pools through the liquidity interface. Upgrading a token does not also move the liquidity position containing it; liquidity providers must migrate their deposits separately.

Aero tells users of the old automated liquidity management solution to withdraw their deposits and manage positions manually because automated rebalancing is winding down. The checklist also instructs Velodrome users to unstake emission-earning deposits outside Optimism mainnet and Ink as gauges shut down. Deposits on Lisk should be withdrawn before October 31.

Liquidity providers in pools paired with $VELO must withdraw their positions and upgrade the token. The upgraded asset settles on Base, so they must then bridge it back to Optimism mainnet before depositing into an upgraded pool, even when they intend to keep providing liquidity on Optimism mainnet.

The old front ends remain available for upgrades after launch, while their gauges are deactivated and emissions cease. Velodrome says it will continue to support trading and liquidity deposits on Celo, Fraxtal, Soneium and Unichain without its token economy.

## Allocation replaces the weekly vote

Aero's launch document describes a continuous allocation system. Holders of sAERO direct rewards to pools and receive a proportional share of the revenue those pools produce while their allocation is active. When a liquidity provider chooses $AERO rewards, the position's trading fees become exchange revenue for those allocators. Liquidity providers can instead choose to earn fees.

The launch hub sets a 47-hour cooldown between allocation changes, subject to change with notice. That replaces the 48-hour minimum contemplated in the earlier [economic design article](https://aero.xyz/articles/aero-economic-case/). The launch instructions give the timing operators should use when changing allocations.

Autopilot automates allocation and can compound or convert earned revenue. Its first allocation is scheduled for 16:00 UTC on October 22. Deposits enter a queue and begin earning rewards with the next allocation, according to the hub. Autopilot follows the same cooldown as other sAERO positions.

The launch announcement says pool rewards are calculated in dollars. Each pool's rewards can be capped against a multiplier of projected revenue, with recalibration more frequently than weekly. Rewards withheld by a cap are never minted. For liquidity providers who choose fees, Slipstream V3 introduces dynamic fees that rise during fast markets and MEV recapture on supported layer-two networks.

Aero says Sherlock and ChainSecurity audited its contracts across five engagements, followed by a three-week public contest. A Sherlock bounty opens on launch day. These are the operator's statements about its audits; this article does not independently verify deployed contract state.

The hub sets no migration deadline, but warns that legacy front ends may close later. Conversion is irreversible. Aero has given no date for those interface shutdowns.
