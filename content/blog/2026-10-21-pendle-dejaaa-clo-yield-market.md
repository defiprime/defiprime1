---
layout: blog
title: "Pendle opens a deJAAA market for AAA CLO yield"
url: /pendle-dejaaa-clo-yield-market.html
h1title: "Pendle opens a deJAAA market for AAA CLO yield"
pagetitle: "Pendle adds deJAAA principal and yield trading"
metadescription: "Pendle lists Centrifuge deJAAA on Base, separating principal and income from a note linked to the Janus Henderson Anemoy AAA CLO Fund."
category: blog
featured-image: /images/blog/pendle-dejaaa-clo-yield-market-ogp.png
intro: "Pendle adds principal and yield trading for Centrifuge’s deJAAA, with a November maturity and a USDC-denominated principal claim."
author: sawinyh
tags: ["News"]
date: 2026-10-21T10:23:08+00:00
---

Pendle announced a live market for Centrifuge's $deJAAA on October 21, 2026, with maturity on November 26, 2026. The market offers fixed-rate and floating-yield trades on a token linked to the Janus Henderson Anemoy AAA CLO Fund. Pendle's [announcement](https://x.com/pendle_fi/status/2112831332808315161) cited more than $30B in Janus Henderson's AAA CLO strategy. That figure covers the manager's strategy, not the deposits in this pool.

The [market is on Base](https://app.pendle.finance/trade/pools/0x6c23193128f7907a3570234a6f6f1c2932f1e84b/zap/in?chain=base). Its contract, `0x6c23193128f7907a3570234a6f6f1c2932f1e84b`, returned the name “PLP JAAA deRWA 26NOV2026” in a direct RPC reading at Base block 52894248. The reading confirms deployed code and the pool token's identity. This deployment check does not audit the contracts or verify the fund's offchain assets.

## The note behind the market

Centrifuge's [product page](https://app.centrifuge.io/pool/281474976710659) describes $deJAAA as a debt product linked to the tokenized fund. It names Open Market Factory Limited as the issuer and classifies the asset as tokenized notes. Pendle's description names Anemoy Capital SPC Limited as the issuer of the underlying fund, Janus Henderson Investors as its active manager, and Centrifuge as the tokenization provider. The note and the fund occupy different parts of the investment structure.

The fund holds AAA-rated tranches of collateralized loan obligations, backed by pools of senior secured corporate loans. Pendle's market description says the senior tranche receives payment first and absorbs losses last. Income is floating-rate and accumulates through an increasing net asset value instead of cash distributions. A holder receives that accrued income through the token's conversion into $USDC.

Centrifuge lists an accreting price mechanism and a minimum investment of 10,000 USD. Its eligibility field specifies non-US persons and entities. These are the published terms on the issuer's product interface, and the token's availability on a decentralized exchange does not remove them. The same page describes liquidity as daily through the vault, with trading available around the clock on DEXes.

Centrifuge identifies Chronicle as the oracle provider and Fordefi as wallet infrastructure. Its contract descriptions label the $USDC vault as both the investment and redemption contract and the token's price oracle. These components handle the operations beneath a holder's Pendle position, separate from the market that prices principal and yield.

## What principal and yield buyers receive

Pendle's [protocol documentation](https://docs.pendle.finance/pendle-v2/Introduction) describes how it splits a position. A yield-bearing token is wrapped into standardized yield, or SY, then split into principal tokens and yield tokens. PT represents the principal side; YT carries the income side. The new market applies that structure to the existing $deJAAA instrument. It does not issue a new portfolio of loans.

The market page denominates its principal claim in $USDC. It states that a PT represents 1 USDC on Centrifuge at maturity, while a YT receives the yield of 1 USDC on Centrifuge until maturity. The accreting note's conversion value changes as income accrues. The principal token has a specified maturity claim, giving a buyer a different position from holding the note itself.

According to Pendle's [yield mechanics guide](https://docs.pendle.finance/pendle-academy/optimizing-yields-with-pendle/optimizing-yields-with-pendle-key-takeaways), the fixed return comes from buying PT below its redemption value. The purchase discount becomes the holder's yield at maturity. A buyer can choose this maturity-dated principal position instead of continuing to hold the full floating-income exposure. The underlying credit still supplies the investment's cash flows.

An early sale uses the market price. Pendle's guide says supply and demand can make the realized return higher or lower than the fixed APY shown at entry, including a loss in extreme cases. A holder who sells a principal token before maturity takes the rate buyers will accept when the position is closed, instead of holding it through to its maturity claim.

The YT buyer takes the income exposure. Pendle describes profit as coming from a rise in the token's resale price or from collected yield exceeding the acquisition cost. In this market, that income originates in a floating-rate CLO strategy. The buyer's return depends on the price paid for the income and what accrues before the November maturity. Janus Henderson's overall strategy size is not a measure of that return.

Pendle's [token cheatsheet](https://docs.pendle.finance/pendle-academy/cheatsheet-for-the-impatient/pt-yt-lp-cheatsheet) says YT income is claimable in real time and the token's price falls to zero at maturity. The yield token gives its holder a finite income window, unlike an ongoing holding of the accreting note. The same documentation says a holder can sell YT at the prevailing market price without a lock or exit penalty.

The pool page also links its deposit and withdrawal routes to Centrifuge's vault. Pendle says its router chooses between native minting and DEX swaps for entry, and between native withdrawal and DEX swaps for exit. The interface shows a routed swap and a direct vault redemption as separate execution paths.

Liquidity provision adds another position. Pendle's documentation lists underlying yield, the PT component's fixed yield, swap fees, and $PENDLE incentives as sources of LP returns. The displayed LP return combines these revenue streams. It measures a different return from the underlying fund's income or the fixed return on a principal token.

## Existing distribution, new rate market

Centrifuge had already [introduced the transferable token to EVM trading venues](https://centrifuge.io/blog/centrifuge-brings-derwa-to-millions-on-evm). The Pendle listing adds a venue for separating and pricing its income. Pendle also distinguishes permissionless contract creation from inclusion in its official interface, where markets undergo a review process. Readers can check this listing through the public pool page and deployed contract, independently of the interview promoted alongside the announcement.

Pendle's announcement mentions using composable positions as collateral, but it identifies no lending market accepting this specific PT and publishes no collateral parameters for it. The live market matures on November 26, 2026.
