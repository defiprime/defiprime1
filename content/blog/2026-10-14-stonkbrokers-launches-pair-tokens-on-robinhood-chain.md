---
layout: blog
title: "StonkBrokers launches auto-compounding Pair Tokens on Robinhood Chain"
url: /stonkbrokers-launches-pair-tokens-on-robinhood-chain.html
h1title: "StonkBrokers launches Pair Tokens on Robinhood Chain"
pagetitle: "StonkBrokers launches Pair Tokens on Robinhood Chain"
metadescription: "StonkBrokers launched fungible Uniswap v4 LP positions that compound fees, support one-sided entry and charge a fee on compounding."
category: blog
featured-image: /images/blog/stonkbrokers-launches-pair-tokens-on-robinhood-chain-ogp.png
intro: "StonkBrokers launched Pair Tokens on Robinhood Chain, turning full-range Uniswap v4 liquidity positions into fungible assets with automatic fee compounding."
author: sawinyh
tags: ["News"]
date: 2026-10-14T08:19:46+00:00
---

StonkBrokers [announced Pair Tokens](https://x.com/ClutchMarkets/status/2110062378025144450) on October 13 as part of a package of official Uniswap v4 hooks built with Hookr. The product turns two deposited assets into one ERC-20 representing a full-range liquidity position on Robinhood Chain.

The live [Pair Tokens interface](https://stonkbrokers.io/pair-tokens) lets users mint with both underlying tokens or enter with one token through a zap. Holders can transfer or trade the resulting ERC-20, then burn it for both assets or zap out to one. The documentation says there is no lockup and no administrative path to the liquidity.

## How the position works

Each Pair Token is a proportional claim on a full-range Uniswap v4 pool. StonkBrokers gives $SPY and $NVDA as an example: the two assets become $SPYNVDA, a fungible token backed by that pair's liquidity position. Other examples shown in the interface include $ETHSPCX, $GMETSLA and $USOGLD.

Swaps through a Pair Token pool pay a 1% fee. The product compounds accumulated fees into the underlying position whenever a user deposits, zaps or redeems. Anyone can also call the compound function, according to the [launch statement](https://x.com/ClutchMarkets/status/2110066562573140292). Compounding carries a 10% charge on the LP fees generated, with that charge used for $STONKBROKER buybacks. Minting and redemption have no protocol fee.

The resulting token remains a standard ERC-20. A holder can send it to another address, keep it in a wallet or use it on a venue that supports the asset. StonkBrokers also says Pair Tokens can themselves be supplied as liquidity or paired with a launchpad. That structure gives other applications a fungible token to integrate instead of requiring them to manage a position NFT.

StonkBrokers contrasts the product with a Uniswap v2 LP token. A v2 receipt represents liquidity in a pool with fixed rules. Pair Tokens wrap v4 positions whose hooks can execute logic on swaps and liquidity changes. The team's documentation lists dynamic fees, custom swap logic, automated compounding, token buybacks and incentive rules as possible pool-level functions.

The specific rules depend on how a pair was created. The documentation says factory pairs currently trade through a hookless 1% pool. Programmable rules apply to pairs launched through Hookr with the StonkFeeHook. Those rules can include a decaying snipe tax, an allowlist for adding liquidity and fee routing to Clock In, $STONKBROKER buybacks or a partner.

The interface's comparison with Uniswap v2 makes the boundaries explicit. Both receipts are plain ERC-20 tokens. A v2 position requires both assets for entry, while a Pair Token can zap one asset in or out with price guards. A v2 pool has one fixed fee and no programmable fee routing. The Pair Token hook can tax, route or gate transactions. Launcher pairs can also use a decaying snipe tax and an LP allowlist. These controls sit in the pool hook rather than in the Pair Token contract.

## What changes for liquidity providers

The main operational change is that LP fees do not wait in the reserves until the holder exits. A deposit, zap or redemption folds the fees back into the position. Each asset pair has one canonical Pair Token address, so wallets and applications can identify the same fungible receipt for later mints.

That canonical address also separates the token from the route used to acquire it. A user can mint, receive or buy the same ERC-20 and later redeem it through the Pair Token interface. Integrators can track a conventional token balance rather than a separate NFT position for each holder. The underlying exposure still consists of the two pool assets, and the full-range position remains active across the pool's entire price curve.

One-sided zaps remove the need to arrive with both assets in the pool ratio. StonkBrokers says those zaps include price guards. On exit, a holder can redeem the pair or request one asset. This reduces the number of transactions a user must arrange outside the product, although the swap inside a zap still changes the user's execution exposure.

The economic risk remains that of a liquidity position. As the relative prices of the two assets move, the position's composition shifts. The product page says fees may offset that effect over time but do not guarantee it. Automatic compounding increases the token quantities behind each share; it does not guarantee a higher value in a user's chosen unit of account.

The fee path also matters. Pool swaps charge 1%, while the compounding action takes 10% of the LP fees being reinvested. Holders therefore receive the remaining compounded fees after the stated charge. Programmable launcher pairs may route additional slices under their hook configuration, so users need to inspect the rules for the specific pair rather than treating every Pair Token as identical.

## Deployment status and the next check

The product interface lists a factory at `0x282c4815F30abc1D0A8eB810c7309140d35a5B38` and displays canonical addresses for stock-token pairs. The launch announcement says Pair Tokens are available for any pair on Robinhood Chain through the StonkBrokers website.

Hookr's [official StonkBrokers hooks page](https://hookr.fun/stonkbrokers) adds an important qualification. It lists six official hook surfaces and says the Pair Token Hook deployment is on hold. The same page says the planned Hookr version leads with $WETHNVDA and is intended to open $WETHNVDA markets against $HOOKR and $STONKBROKER. It also says Hookr earns part of the fee taken at each compound on preset pools.

Users can access factory Pair Tokens now, but the status of the separately programmable Hookr deployment remains the open question. The next verifiable milestone is a live Pair Token Hook contract and pools on Hookr, replacing the current on-hold notice with contract addresses and executable markets.
