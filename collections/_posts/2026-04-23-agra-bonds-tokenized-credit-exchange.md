---
git-date:
layout: [blog]
title: "Agra Bonds: A CLOB for Tokenized Credit, and the Missing Secondary Market for RWAs"
permalink: agra-bonds-tokenized-credit-exchange
h1title: "Agra Bonds: A CLOB for Tokenized Credit"
pagetitle: "Agra Bonds: A CLOB for Tokenized Credit, and the Missing Secondary Market for RWAs"
metadescription: "Agra Bonds is a beta Ethereum orderbook for tokenized private credit. Here is how the rate-quoted CLOB works, what is actually live, and where it sits in the RWA landscape."
category: blog
featured-image: /images/blog/agra-bonds-tokenized-credit-exchange-ogp.png
intro: "Agra Bonds is a beta Ethereum orderbook for tokenized private credit. Here is how the rate-quoted CLOB works, what is actually live, and where it sits in the RWA landscape."
author: sawinyh
tags: ["Analysis", "RWAs"]
---

Tokenized private credit has a liquidity problem. An issuer like [Centrifuge](https://centrifuge.io/) mints a share token that represents a claim on a real fund paying real yield, and then the token sits. Holders are effectively locked until maturity, redemption windows are slow and gated, and the NAV on the dashboard is a reference price, not a market price. The whole point of putting these instruments on-chain was to make them tradable, and most of them are not.

Agra Bonds at [bonds.agra.gg](https://bonds.agra.gg/) is one of a handful of early attempts to fix that specific gap. It is a beta-stage, Ethereum-only orderbook that quotes tokenized credit in yield and discount-to-NAV terms, settles peer-to-peer on-chain, and lets holders exit positions that would otherwise be stuck until a scheduled redemption. The flagship market is ACRDX/USDC, the [Anemoy](https://anemoy.io/) tokenization of Apollo's diversified credit fund, and a smaller market for Pharos consumer credit (pALPHA) runs alongside it. A third market for aEthWETH opened last weekend to give depositors affected by the [KelpDAO rsETH exploit](/kelpdao-rseth-exploit) a way out while Aave's Ethereum pool was under utilization stress.

The product is small, unaudited in places, and operating in a corner of DeFi where almost nothing works end-to-end yet. It is also one of the more coherent attempts so far to build a fixed-income primitive that looks like a real credit desk rather than a yield aggregator. Here is what is actually live, how it works under the hood, and where it sits against the competition.

## What Agra Actually Is

Agra's pitch is narrow: a central limit orderbook for tokenized credit on Ethereum, with quoting in yield and NAV-discount terms instead of raw price. Makers post bids and asks denominated in basis points of discount or premium to the token's reference NAV, and the UI translates that into an effective yield based on the instrument's coupon and duration. Takers hit the book the same way they would on any CLOB, and settlement happens directly between the two wallets via a smart contract. There is no vault, no AMM pool, no shared liquidity reserve backing the trades.

That design choice matters. Tokenized bonds and credit shares move in a narrow band around NAV, typically a few percent in either direction, and that band carries real information about credit quality, duration, and liquidity preference. An AMM with a bonding curve prices that band badly. A CLOB that quotes in yield prices it the way the TradFi desks that originate these instruments already do. Agra is not trying to be a DEX for RWAs. It is trying to be a credit desk for the subset of RWAs that already look like bonds.

The mechanics on the user side are unsurprising. Connect a wallet, pass whatever KYC the instrument requires (the ACRDX share token enforces transfer restrictions at the contract level, so non-whitelisted wallets cannot receive it even if they clear the book), post a limit order or sweep the top of the book, settle. Positions are standard ERC-20 balances after settlement, which means they can be posted as collateral on any lending market that chooses to list them. That composability pitch is a big part of why issuers care about the platform existing: a liquid secondary market raises the ceiling on what downstream integrators are willing to do with the paper.

## What Is Live

As of late April 2026, three markets are running.

![Agra Bonds ACRDX/USDC orderbook, NAV chart, and trade panel](/images/blog/agra-bonds-ui.png)


**ACRDX/USDC** is the flagship. The underlying is Anemoy's tokenized wrapper of the Apollo Diversified Credit Fund, a senior private-credit fund managed through a BVI vehicle with KYC required for transfers. NAV sits at roughly $1.016. The coupon floats around 8.18%, and maturity is open-ended. The book typically shows bids in the −1% to −7% discount-to-NAV range, with larger capacity at deeper discounts. A buyer hitting the best bid is taking the 8.18% coupon plus whatever pull-to-NAV accrues if the position can eventually be redeemed at par, in exchange for accepting illiquidity and senior-private-credit default risk on a BVI vehicle.

**pALPHA** is Pharos Network's tokenized consumer credit, structured as a multi-tranche instrument with partial guarantees, onboarded through the same Centrifuge/Anemoy stack. Liquidity is thinner than ACRDX, and the discount band is wider, which is roughly what the credit profile would imply.

**aEthWETH/WETH** is the market Agra launched in the days after the KelpDAO exploit froze [Aave](/aave)'s rsETH markets and sent Ethereum WETH utilization sharply higher. aEthWETH is the Aave supply receipt for WETH, so a secondary market for it gives depositors a way to exit supply positions without waiting for utilization to normalize or for bad-debt accounting to settle. The capacities there are modest, and the use case is tactical rather than structural, but it is a reasonable demonstration of how quickly a rate-quoted CLOB can spin up a market for a distressed asset.

Public data on cumulative volume is thin, and Agra has not published a dashboard. The books on each market show live capacity in the low-to-mid six figures of USDC per level, which is typical for a beta RWA venue and well below what any serious private-credit desk would consider deep.

## Where the Trust Sits

Agra's stack has two contract layers, and they sit at very different levels of transparency. The asset you trade and the venue you trade it on are not the same trust problem.

The asset is inspectable. The ACRDX share token at `0x9477724Bb54AD5417de8Baff29e59DF3fB4DA74f` is a verified Solidity 0.8.28 ShareToken with token metadata naming Anemoy as the issuer. It is a standard Centrifuge-style RWA primitive: ERC-20 with EIP-2612 permits, a MakerDAO-style `wards` authorization pattern for mint/burn and config, transfer-restriction hooks that enforce KYC on-chain, and a vault mapping that links the share token to the underlying Centrifuge pool for NAV reference. The code is public, the pattern has been used by multiple issuers, and the risks can be evaluated against that pattern directly.

The tradeoff on the token side is that it is centralized by construction. Authorized operators can mint, burn, pause transfers via the hook, and reconfigure the vault pointer. That is the correct trust model for regulated private credit, not a red flag: you need the issuer to be able to enforce redemptions, blacklist sanctioned addresses, and pause if the underlying fund gates. A buyer of ACRDX is trusting Anemoy the issuer, and that trust boundary is explicit and priced into the instrument.

The exchange is not inspectable in the same way. Each Agra market lives behind an ERC-1967 proxy referenced in the UI as a `market` query parameter, and those proxies handle order placement, matching, and settlement against the underlying share token and USDC. Source code for the orderbook contracts is not verified on Etherscan as of this writing, no public audit reports have been posted, and there is no public GitHub repository for the matching logic. Settlement is on-chain and non-custodial, so funds move directly between maker and taker wallets, but the logic that routes them through the proxy is not something a user can currently read.

A buyer of ACRDX is extending trust to Anemoy, which is the normal, known price of tokenized private credit. A user of Agra is also extending trust to whoever wrote and upgrades the orderbook proxies, which is a second trust boundary that is not yet documented. That is not unusual for a beta venue, but it is the variable that has to close before the platform can be used at size. A subtly broken CLOB rarely shows up in the UI; it shows up in an edge case six months later.

## The Competitive Field

The space Agra is targeting is real, small, and contested. Secondary liquidity for tokenized credit has been the structural bottleneck on the entire RWA thesis for two years. Every issuer knows it, most buyers refuse to scale positions without it, and the venues trying to solve it are splitting the problem along different axes.

The closest direct competitor is [Figure Markets](https://figuremarkets.com/), which runs an on-chain limit-order book for tokenized credit on its own Provenance chain. Figure is much larger, much more institutional, and handles real volume in HELOCs and private credit, but it lives in a regulated, permissioned environment rather than on a general-purpose EVM and is effectively inaccessible to most DeFi users. NewEra Finance is the other close analog on the DeFi side, positioning itself as a multi-chain secondary market for RWAs including bonds and equities, but NewEra uses an AMM-style aggregator rather than a pure orderbook and targets a broader asset set. Bondi Finance runs a tokenization-plus-secondary stack focused on corporate bonds and Sukuk. [IXS](https://ixs.finance/) and [Swarm Markets](https://swarm.markets/) occupy adjacent regulated-DEX and OTC niches respectively.

The origination-first credit protocols are in a different business. [Maple](https://maple.finance/), Clearpool, Goldfinch, TrueFi, and Centrifuge itself all issue credit positions, but none of them run a meaningful secondary market for those positions. They expect holders to redeem, not trade. [Ondo](https://ondo.finance/) and BlackRock's BUIDL have resolved the liquidity question for tokenized Treasuries by routing secondary flow through standard DEXes, which works because Treasuries are homogeneous and NAV is essentially constant. That approach does not generalize to private credit, where every instrument has a different coupon, duration, and credit curve and where NAV is a moving target.

Pendle and Notional operate in the adjacent space of yield tokenization and fixed-rate trading, but they slice the yield off the principal rather than trading the bond itself. That is complementary to what Agra is building, not competitive with it.

What Agra has going for it is focus. It is one of the only DeFi-native venues running a yield-quoted CLOB specifically for Ethereum tokenized private credit, it is plugged directly into the Centrifuge issuer pipeline, and it has demonstrated the ability to spin up an opportunistic market (the aEthWETH book) inside a weekend. What it does not have yet is verified contract source, a published audit trail, or the kind of issuer breadth that would let a credit-focused allocator actually build a diversified book on the platform.

## The Risks Worth Tracking

Three risks dominate, and none of them are unique to Agra; they are the standard risks of any venue operating at this stage.

**Contract opacity.** The orderbook proxies are unverified and unaudited publicly. Settlement works today, and the UI-to-contract path appears clean, but nothing about the matching logic or the proxy upgrade controls is currently inspectable. A production-grade credit venue eventually publishes its source and its audits. Until that happens, position sizing on the venue should reflect that it is effectively a trust-the-frontend product at the exchange layer.

**Liquidity depth.** The books are shallow by institutional standards. Round-trip costs on anything larger than the top level of liquidity are material, and exits in a stress scenario, the exact use case the platform is pitching against, have not been tested. The aEthWETH market is the first live stress test, and it is small enough that it will not tell us much about how the venue behaves when the book needs to move real size.

**Underlying credit.** This is the risk that tends to get understated in DeFi coverage of RWAs. ACRDX is senior paper in a diversified fund, which is a reasonable credit profile, but it is private credit, it is BVI-domiciled, and the ~9–10% effective yield at current discounts is compensation for real default risk, not a free lunch. Anyone buying into the book at a discount is taking a view on Apollo's underwriting, not on Ethereum's security model. The platform can work exactly as advertised and a buyer can still lose money if the underlying fund runs into credit trouble.

There is no AGRA token, no points program, no yield farming layer on top. That is a feature, not an omission. The last thing a credit venue needs is a reflexive incentive structure layered on instruments whose returns are already bounded by the coupon.

## Why It Matters Anyway

The RWA category crossed $20 billion in tokenized assets earlier this year, and the overwhelming majority of that is Treasuries. Private credit is the obvious next tier by size and by yield, and it has been stuck on the origination-without-secondary problem for most of the cycle. A working rate-quoted CLOB for Ethereum credit would be a meaningful piece of the infrastructure that unlocks the next leg, because once holders can exit positions at a market-cleared discount, issuers can sell larger primary tranches, lenders can accept the tokens as collateral with tighter risk parameters, and the whole duration stack starts to resemble what TradFi already runs.

Agra is early, small, and has real gaps to close: verified contracts, public audits, a broader issuer set, and more issuer-funded inventory on the book. It is also one of the few venues attacking the right problem with the right primitive. The competitive field is thin enough that the incumbents (Figure on the institutional side, NewEra on the DeFi side) have not yet locked the category, and the issuer relationships Agra is building through the Centrifuge ecosystem are defensible.

The thing worth watching over the next two quarters is not the ACRDX book. It is whether Agra gets a second issuer category on the platform that is not routed through Centrifuge, whether the orderbook contracts get published and audited, and whether any downstream lender lists an Agra-traded token as collateral with underwriting that cites the on-chain market price rather than the NAV. The non-Centrifuge issuer is the most important of the three: as long as every asset on the book comes through one share-token pipeline, Agra is structurally a feature of Centrifuge rather than a standalone credit venue, and the "rate-quoted CLOB for tokenized credit" pitch is indistinguishable from something Centrifuge could run in-house. A second category (Superstate, Backed, Maple, or similar) is what turns two price points into the beginning of a yield curve. Those are the three milestones that would turn the platform from an interesting beta into actual RWA infrastructure. None of them are guaranteed. All of them are within the reachable path from where the product is today.

Treat the specific numbers above (NAVs, coupons, book depth, market addresses) as point-in-time snapshots from late April 2026. The live state is on [bonds.agra.gg](https://bonds.agra.gg/), and the interesting thing about a beta venue is that everything material can change inside a week.
