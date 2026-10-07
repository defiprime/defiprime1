---
layout: blog
title: "HashKey Cloud plans native Bitcoin lending through Babylon vaults"
url: /hashkey-cloud-to-integrate-babylon-bitcoin-vaults.html
h1title: "HashKey Cloud plans native Bitcoin lending through Babylon vaults"
pagetitle: "HashKey Cloud to integrate Babylon Bitcoin vaults"
metadescription: "HashKey Cloud plans to offer institutional clients native Bitcoin-backed borrowing through Babylon vaults and Aave v4."
category: blog
featured-image: /images/blog/hashkey-cloud-to-integrate-babylon-bitcoin-vaults-ogp.png
intro: "HashKey Cloud plans to connect institutional Bitcoin collateral to Aave v4 through Babylon's Trustless Bitcoin Vaults."
author: sawinyh
tags: ["News"]
date: 2026-10-07T22:21:03+00:00
---

At 14:35 UTC on October 7, 2026, Babylon [announced](https://x.com/babylonlabs_io/status/2107842354962919815) that HashKey Cloud would integrate its Trustless Bitcoin Vaults, or TBV, for institutional clients using Aave v4. The companies have not set a public launch date. Their [joint announcement](https://babylonlabs.io/blog/hashkey-cloud-to-integrate-babylon-trustless-bitcoin-vaults) says further timing and partnership details will arrive in the coming months.

The planned service would let a HashKey client borrow against Bitcoin that remains on the Bitcoin network. Babylon says the design avoids wrapping the asset, sending it through a bridge or placing it with a centralized intermediary. Aave v4 supplies the lending market, while HashKey Cloud provides the institutional access and operational role described by the partners.

HashKey clients would be able to borrow stablecoins and other supported assets against that collateral. The announcement also says clients could deploy borrowed stablecoins into yield strategies. It does not name the strategies, borrowing limits, collateral parameters, fees or jurisdictions that HashKey will support.

## How the collateral path works

Babylon's [technical overview](https://babylonlabs.io/blog/bitcoin-borrowing-repriced) describes a five-stage process. A depositor first locks native Bitcoin in a dedicated unspent transaction output on the Bitcoin network. Participants construct and pre-sign a transaction graph while the deposit receives confirmations. That graph fixes the permitted paths by which the Bitcoin can later be spent.

After setup, a self-custodial BTCVault is activated on Ethereum. Aave v4 can then recognize the locked Bitcoin as collateral. The borrower takes a supported asset from Aave at a market-based variable rate. Babylon's product page lists $USDC, $USDT and $WBTC as examples of assets that may be borrowed, though the HashKey announcement does not say which assets its service will expose.

Closing the position requires repayment of the outstanding debt and accrued interest before the user requests a withdrawal. The same overview says a position is liquidated only after it falls below the liquidation threshold and that partial liquidation is supported. The HashKey release does not provide the threshold or other market parameters, so clients cannot yet calculate a position's liquidation buffer from the announcement.

A withdrawal then enters a challenge process on Bitcoin. If no valid challenge is raised, the Bitcoin returns to the address nominated by the user. Babylon says an Ethereum event authorizes redemption, a zero-knowledge proof demonstrates that the event occurred, and the challenge mechanism determines whether the claim may proceed. The process is designed to avoid approval from a custodian, wrapped-asset issuer or signer committee.

This architecture separates the location of the collateral from the location of the loan. The Bitcoin remains locked in a Bitcoin UTXO, while Ethereum and Aave account for the collateral and debt position. It also means the borrower depends on the vault transaction graph, proof system, oracle and Aave market operating as intended.

## What changes for HashKey clients

HashKey Cloud already provides staking and yield infrastructure under HashKey Holding Limited. The company says it has provided node validation services since 2018 across public chains and Layer 2 networks. The integration adds a proposed borrowing route to that institutional infrastructure.

Fisher Yu, a Babylon co-founder, said HashKey Cloud would take a "core operational role in TBV" and bring native Bitcoin credit to institutional clients in Asia. He also said the self-custodial design lets regulated institutions retain title to their Bitcoin while using it as collateral. Leo Li, CEO of HashKey OnChain, described the goal as turning native Bitcoin into an asset that can be borrowed against and then deploying the proceeds.

For a client, the practical change is the ability to seek stablecoin liquidity without first selling Bitcoin or converting it into a wrapped representation. That removes an issuer and redemption process from the route. It does not remove lending risk. Babylon's own disclosure says users remain exposed to smart-contract and implementation risk, price-oracle risk, and the risk profile of the lending application they choose.

The cost is also not limited to Aave's variable borrowing rate. Babylon says users may pay protocol, Vault Provider and network fees. Its product page displays estimated native Bitcoin borrowing rates between 3% and 5%, alongside estimates between 0% and 5% for on-chain borrowing and between 9% and 16% for centralized borrowing. The page warns that rates and fees are variable and may change. Those ranges are product-page estimates, not terms promised to HashKey clients.

## The integration is not live yet

Native Bitcoin-backed borrowing through TBV is available on a public Aave v4 testnet with test assets. The HashKey announcement describes a future integration and gives no production deployment date. It also leaves open which entity will act as Vault Provider, how HashKey will handle access controls, which Aave market will hold the debt, and what collateral and liquidation settings will apply.

Those missing terms matter to institutions comparing this route with custody-based loans or wrapped Bitcoin in existing lending markets. Self-custody changes one category of counterparty exposure, but the position still depends on code, proofs, market liquidity, oracle inputs and liquidation execution. Borrowers also need the complete fee schedule to compare the advertised structure with another loan.

A prospective borrower will need several parameters before using the service: the supported debt assets, the variable rate for each asset, the liquidation threshold, oracle design, Vault Provider fees and network costs. The published flow also makes repayment operationally important because a full withdrawal requires the outstanding debt and accrued interest to be repaid. If collateral crosses the liquidation threshold first, the system supports a partial liquidation instead.

The next stated milestone is the release of integration timing and partnership details in the coming months. Until then, the verifiable state is a planned HashKey service built around a live public testnet, not a production borrowing market for HashKey clients.
