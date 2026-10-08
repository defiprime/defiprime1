---
layout: blog
title: "Hashi sets October mainnet rollout with $500M committed"
url: /hashi-mainnet-launches-with-500m-committed.html
h1title: "Hashi sets October mainnet rollout with $500M committed"
pagetitle: "Hashi plans October mainnet launch with $500M committed"
metadescription: "Sui's Hashi plans an October mainnet rollout with over $500 million committed and two Anchorage Digital access routes for institutions."
category: blog
featured-image: /images/blog/hashi-mainnet-launches-with-500m-committed-ogp.png
intro: "Sui plans to move Hashi from testnet to mainnet by the end of October with more than $500 million committed by its launch coalition."
author: sawinyh
tags: ["News"]
date: 2026-10-08T05:21:29+00:00
---

At 01:00 UTC on October 8, 2026, Sui [announced](https://chainwire.org/2026/10/08/hashi-mainnet-to-launch-with-500m-in-capital-backing-adds-anchorage-digital-to-coalition/) an October mainnet rollout for Hashi, its native Bitcoin collateral system, with more than $500 million in capital commitments. The coalition supplying those commitments has more than 20 partners, and Anchorage Digital joined as a launch partner.

Hashi is intended to let holders use Bitcoin as collateral in Sui applications while the underlying asset remains on the Bitcoin network. The [product page](https://www.sui.io/hashi) describes it as a decentralized Bitcoin collateralization primitive that orchestrates native $BTC from smart contracts without relying on a centralized balance sheet.

## What goes live

The rollout is due to begin during October and proceed in phases. Sui said Hashi will start with capital behind lending, borrowing, credit, vaults and structured products. Named vault providers include Aftermath, Concrete and Fluid.

The launch coalition also includes BitGo, Bullish, Cumberland, FalconX and Ledger. Sui said the group has been building around Hashi since the project was unveiled. The commitment is capital designated for the launch, not a measure of deposits already live on mainnet. That distinction matters because the announcement does not state how much capital each provider committed, how quickly it will enter individual vaults or what portion will be available to borrowers on the first day.

Hashi separates Bitcoin custody from the lending logic running on Sui. A user sends native $BTC to a unique Hashi deposit address on the Bitcoin network. Each Sui address receives a personalized 2-of-2 multisignature address. Sui validators monitor Bitcoin confirmations, reach quorum and mint an equivalent representation on Sui. The user can then set loan-to-value parameters, connect price oracles and seek stablecoin liquidity through Sui smart contracts. Repayment starts the withdrawal process back to a Bitcoin address.

The sequence gives users several checkpoints before depositing. The Bitcoin address belongs to the Hashi flow, but validators still have to observe the deposit and create the Sui-side representation before it can enter a loan. The loan then depends on a specific contract, oracle and venue. A completed repayment still requires the signing process to release native Bitcoin. Users should therefore check how a venue handles delayed confirmations, oracle outages, liquidations and withdrawals. The announcement gives the architecture, but it does not publish operating targets for those paths.

The personalized 2-of-2 address also does not make every Hashi market equivalent. Vault providers can offer different collateral ratios, assets and strategies even when they use the same base system. A depositor evaluating Aftermath, Concrete or Fluid needs the terms of that particular vault rather than the coalition's aggregate capital commitment. A borrower needs the rate, liquidation threshold and available stablecoin liquidity for the same reason.

The system therefore exposes users to more than Bitcoin custody alone. Sui says Move contracts govern collateral parameters, loan-to-value ratios and liquidation logic. Price oracles update valuations, while collateral calls and liquidations execute under terms set by each venue. A borrower needs to examine those venue terms, the oracle design and the liquidation thresholds before treating the custody architecture as a complete risk assessment.

## Anchorage adds two access routes

Anchorage Digital plans to give institutional clients two ways into Hashi. The first uses Atlas, its settlement and tri-party collateral infrastructure. Sui positioned that route for organizations subject to qualified custody, compliance and operational requirements, including public companies with Bitcoin on their balance sheets and digital asset treasury companies that cannot directly use DeFi.

The second route uses Porto, Anchorage Digital's institutional self-custody wallet. Sui said Porto users can access lending, yield and real-world asset strategies directly. The stated audience includes venture funds, hedge funds, miners, market makers and liquidity providers. Anchorage also plans to supply stablecoin liquidity to Hashi, though the announcement does not name the stablecoin, the amount or the date that liquidity will arrive. The timing and distribution of that supply are not stated.

These routes change the operational choice for institutions. An Atlas client can keep a tri-party collateral workflow rather than moving straight into a self-custody setup. A Porto client can interact directly but assumes the wallet, contract and venue-level controls attached to that route. Neither option removes the lending risks created by oracle updates, collateral ratios and automated liquidation.

## How the collateral design works

Sui describes two main trust assumptions: the Sui validator set and the smart contract governing the loan. Funds move when one-third of validators produce a valid threshold Schnorr signature. A guardian layer performs another check before Bitcoin is released, and Sui presents it as protection against validator collusion or a wider compromise.

The product page sets out four stages from deposit to withdrawal. Bitcoin first moves to the user's Hashi-generated address. Validators then confirm the deposit and create the Sui-side representation. The user pledges that representation in a contract to obtain liquidity. Repayment permits release of native Bitcoin through the signing process.

Sui says returns are meant to come from interest spreads instead of token incentives. The available applications may include stablecoin borrowing, on-chain credit, automated vaults, structured products, real-world assets and Bitcoin-backed bonds. The announcement does not provide launch rates, maximum loan-to-value ratios, liquidation penalties or insurance terms. Those values will determine whether the initial products compensate depositors for contract, oracle, custody and liquidation risk.

Hashi remains labeled as testnet on Sui's product page at the time of the announcement. The next stated milestone is the phased mainnet rollout by the end of October. The unresolved point is how much of the committed capital becomes usable liquidity at launch, and under which vault and liquidation parameters.
