---
layout: blog
title: "Vault Street launches CARRY with a 12%+ net APY target"
url: /vault-street-launches-carry-rwa-vault.html
h1title: "Vault Street launches CARRY for leveraged RWA yield"
pagetitle: "Vault Street launches CARRY leveraged RWA vault"
metadescription: "Vault Street's CARRY vault targets 12%+ net APY with tokenized credit, cash-and-carry funds, delta-neutral trades and up to 4x leverage."
category: blog
featured-image: /images/blog/vault-street-launches-carry-rwa-vault-ogp.png
intro: "CARRY combines tokenized credit and market-neutral strategies in a managed vault with on-chain leverage and a dedicated redemption sleeve."
author: sawinyh
tags: ["News"]
date: 2026-10-08T15:19:05+00:00
---

On October 8 at 14:36 UTC, Vault Street [announced CARRY](https://x.com/Vault_St/status/2108204828774318346), its second vault, with a target of 12%+ net APY. The product combines leveraged exposure to tokenized real-world assets with delta-neutral strategies.

The target is not a fixed return. Vault Street described it as the result of portfolio construction, borrowing and hedged trading across several types of underlying exposure. The same announcement identified leverage, redemption timing and collateral management as parts of the product's operating model.

## What sits inside CARRY

Vault Street listed five current allocations. mGLOBAL is a Fasanara fund that invests in trade receivables and digital invoices. Prime is Figure's Democratized Prime home equity pool, minted by Hastra. mWIN is Midas' Wellington Income Opportunities product. USCC is a crypto cash-and-carry fund managed by Bitwise on Superstate's rails.

The fifth allocation is a set of proprietary delta-neutral strategies run by the Vault Street team. Those positions can use decentralized exchanges, perpetual platforms and centralized exchanges. Vault Street said the strategies start with gold and are intended to avoid directional price exposure. It plans to expand the set to other commodities and equities.

The manager said it reviews an asset's credit quality, liquidity, redemption terms and NAV reliability before adding it. That selection process matters because CARRY packages instruments with different settlement and redemption mechanics into one vault position. Investors do not hold and rebalance each component separately.

Vault Street describes its work as sourcing, underwriting, portfolio construction, leverage, liquidity management and continuous risk monitoring. The structure brings those functions together because each one can affect the others. An asset with an attractive stated return may still require a smaller allocation if its redemption window is long or its NAV is difficult to verify. The announcement presents the vault as the managed wrapper for those trade-offs.

This also changes what an allocator has to monitor. The return does not come from one borrower or one market. It comes from receivables, home equity, an income-opportunities product, cash-and-carry exposure and Vault Street's own hedged positions. The basket spreads exposure across several strategies, but each component has its own manager, liquidity path and valuation process. Vault Street's admission review is therefore only the first control. Ongoing portfolio and liquidity management determine how the combined position behaves after capital enters.

Vault Street's first vault, primeUSD, was built for conservative exposure to investment-grade assets. CARRY moves the platform toward a higher yield target by combining the RWA basket with leverage and hedged trading. The announcement did not provide the starting weight of each allocation.

## How leverage and liquidity work

A Dynamic Leverage Engine adjusts exposure using borrowing rates, available liquidity, collateral health and market depth. Vault Street said the system uses continuous on-chain monitoring and direct connections with asset issuers. It can connect to Morpho and Aave when those markets have liquidity for portfolio assets. The stated leverage ceiling is up to 4x.

Access to that leverage depends on available markets. Vault Street said the infrastructure can connect to Morpho and Aave wherever portfolio assets have liquidity. The vault therefore cannot treat the 4x ceiling as permanent capacity. Borrowing rates and market depth can change before the underlying RWA completes a redemption. The engine's job is to change exposure as those conditions move, while direct issuer connections give the manager another route for monitoring the assets.

That ceiling makes borrowing conditions part of the return and risk profile. A change in rates or market depth can alter how much exposure the engine can maintain. Collateral health also links the RWA portfolio to the liquidation mechanics of the connected lending market. Vault Street said the engine adjusts exposure using those inputs rather than holding one leverage level.

Redemption timing creates a separate constraint. Tokenized RWAs can redeem more slowly than on-chain capital expects, according to the announcement. CARRY therefore keeps a dedicated liquidity sleeve for express redemptions of up to 10% of NAV. Vault Street also described a pricing framework and an external stability buffer intended to keep daily NAV smooth.

For an allocator, the sleeve means a request within that capacity does not depend entirely on every underlying RWA completing its own redemption process first. The announcement does not promise that all withdrawals will settle through the sleeve, and it does not state the treatment of requests above 10% of NAV. Those terms are material when the underlying assets have different redemption windows.

## Controls and collateral use

Vault Street said MixBytes audited the vault and Hypernative monitors it continuously. Vault activity is restricted through narrowly scoped policies in MPC infrastructure supplied with Utila. Automated circuit breakers can reduce exposure or pause deployment when predefined risk thresholds are breached.

These controls address different parts of the operating stack. The audit covers the vault implementation, monitoring watches live activity, MPC policies limit permitted actions, and circuit breakers change deployment when a threshold is crossed. Vault Street did not publish the thresholds in the launch announcement.

CARRY positions can also serve as collateral. An investor can use the position to add leverage or refinance the exposure rather than redeeming it. Vault Street is targeting $2m of initial liquidity on Morpho for that use. The collateral option adds another borrowing layer on top of a vault that can already use leverage internally, so users need to account for both the vault's exposure and their own loan terms.

Vault Street said more vaults will follow as it adds venues and asset partners. For CARRY, the unresolved details are the initial portfolio weights, the circuit-breaker thresholds and the handling of redemptions beyond the 10% express-liquidity sleeve.
