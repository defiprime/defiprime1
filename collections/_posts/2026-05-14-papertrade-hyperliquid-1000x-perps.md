---
git-date:
layout: [blog]
title: "Papertrade's 1000x Perps and the Edge of HIP-3"
permalink: papertrade-hyperliquid-1000x-perps
h1title: "Papertrade's 1000x Perps and the Edge of HIP-3"
pagetitle: "Papertrade's 1000x Perps and the Edge of HIP-3"
metadescription: "Papertrade.xyz markets 1000x leverage on Hyperliquid via HIP-3. The leverage math against the documented liquidation engine, where this sits between trade.xyz and JELLY, and what HIP-3 has not yet priced in."
category: blog
featured-image: /images/blog/papertrade-hyperliquid-1000x-perps-ogp.png
intro: "Papertrade.xyz markets 1000x leverage on Hyperliquid via HIP-3. The leverage math against the documented liquidation engine, where this sits between trade.xyz and JELLY, and what HIP-3 has not yet priced in."
author: sawinyh
tags: ["Analysis"]
---

HIP-3 has been live on Hyperliquid mainnet for seven months and has already produced two distinct kinds of product. The big one, trade.xyz, runs tokenized stock, index, and commodity perps with conservative leverage caps and accounts for most of HIP-3's open interest; tokenized equity and commodity futures on Hyperliquid peaked above $2 billion in open interest in April 2026. The other shape is starting to surface around the edges. [Papertrade.xyz](https://papertrade.xyz/) markets itself as "the first fair-launched fully onchain perpetual exchange built on Hyperliquid" and puts a 1000x leverage offer on the front page. Documentation is "coming soon"; the team is not publicly named.

That second category is where HIP-3's design is now being stress-tested. Trade.xyz is what the standard pitched. Papertrade is what permissionless market deployment also makes possible.

Hyperliquid itself spent 2024 and most of 2025 being the cleanest on-chain answer to centralized perp execution. By April 2026 the platform was clearing roughly $40 billion in weekly perp volume, holding about $9.5 billion of open interest, and capturing the majority of decentralized perp activity on most days. Hyperliquid's own validator-operated markets cap leverage at 40x on majors. Papertrade's 1000x sits 25x above that.

## How a 1000x Builder Plugs Into Hyperliquid

HIP-3 lets anyone with 500,000 HYPE staked deploy a perpetual futures market on top of HyperCore. At HYPE near $39 in mid-May 2026, the stake is roughly $20 million. The unstaking queue is 7 days, during which the stake remains slashable. Validators can vote to slash up to 100% for "irregular inputs that cause invalid state transitions or prolonged downtime," and lesser amounts (50% or 20%) for performance issues.

What that $20 million buys is editorial control over a specific surface. A deployer picks the oracle, the leverage caps, the collateral asset, the listed contracts, and (within HIP-3's range) the fees. A deployer does not touch the matching engine, the order book, the margin engine, the backstop liquidator vault, or the protocol's solvency guarantees. Those are HyperCore's, run by Hyperliquid's validators and unified across all HIP-3 deployments.

The economic engine for a deployer is fee flow. HIP-3 markets charge 2x the standard Hyperliquid base rate (so 3 basis points maker / 9 basis points taker at the lowest tier, versus Hyperliquid's own 1.5 / 4.5 bps base) and the deployer takes a fixed 50% of that. There is also a "growth mode" config that can cut taker fees by roughly 90% to compete for early volume.

So the question for a 1000x product is whether the leverage envelope it offers is consistent with the rest of that plumbing.

## The 1000x Margin Math

Hyperliquid documents maintenance margin as half the initial margin at max leverage. At 40x leverage on BTC perps, maintenance margin is 1.25%. At 3x on a long-tail name, it's 16.7%. Below that threshold, accounts are liquidated against the order book. If equity falls below two-thirds of maintenance margin without a successful book fill, the position is absorbed by the backstop liquidator vault, a component strategy of HLP, Hyperliquid's community liquidity pool.

If you extend the formula to 1000x, maintenance margin is roughly 0.05% of notional. A five-basis-point adverse move liquidates; three basis points sends the position to the backstop. Five basis points on BTC is a normal-second amount of price drift on a normal day. Three is closer to bid-ask noise on the book.

No serious venue lets that math hold mechanically. Real 1000x products tend to defend the engine somewhere downstream: position size caps, isolated margin only, stepped maintenance curves at extreme leverage, or different liquidation triggers entirely. Without published docs it is impossible to say which constraints papertrade actually imposes. But the headline 1000x number is doing work whether the constraints are there or not. Either the trader gets the leverage and most of the structural problems below come with it, or the trader uses much lower effective leverage than the marketing implies and the 1000x is theatrical.

The fee math is the cleaner part of the picture. At HIP-3's 9-bp base taker fee, a 1000x position pays roughly 90% of its collateral on the entry alone. A round trip — entry plus exit, both as taker — runs about 180% of collateral. The headline fees on a maxed-out position are larger than the collateral backing it. The product is only economically coherent at 1000x in one of three configurations: growth-mode taker rebates that drop fees to fractional basis points, very small tickets where the user is paying for the lottery experience, or position caps that mean nobody ever runs the headline leverage in size. Each of those is a real product choice. None of them is "1000x leverage" the way the marketing reads it.

Slippage works the same way. A trader posting 100 USDC at 1000x is holding 100,000 USDC of notional. When auto-liquidated, the leveraged size goes through the order book, not the collateral. Hyperliquid's CLOB is genuinely deep, but it is not literally zero-impact at 100,000 USDC of notional on any pair where that size matters. "0 slippage" is either a claim about the experience of opening small positions or it is marketing language without an execution claim attached.

## Where This Sits, Between Trade.xyz and JELLY

The HIP-3 surface has two reference points for thinking about where papertrade lands.

Trade.xyz is what the HIP-3 pitch decks lead with. Tokenized S&P 500 and NASDAQ futures, pre-IPO contracts (Cerebras' CBRS being one example), tokenized gold, silver, and oil. The product targets 24/7 access to traditional markets, which is a real underserved demand, and per recent ecosystem reporting has hit 24-hour volumes in the multi-billion-dollar range with tens of thousands of daily traders. The leverage caps are conservative compared to what's now showing up at the edges. Tokenized equity perps are not risk-free — they are oracle-dependent on TradFi venues, can experience weekend reporting gaps, and the pre-IPO contracts reference assets with no real spot liquidity — but the risk profile is different in kind from a 1000x crypto-perp. Trade.xyz sells access. Papertrade sells extremity.

JELLYJELLY is the other reference, and the analogy is narrower than it first looks. In March 2025 a coordinated attacker opened roughly $4.5 million of short and ~$5 million of long positions on a thinly-traded memecoin perp, then pumped the underlying spot price by more than 400% in an hour on outside venues. The short was made uneconomic to liquidate through the book and inherited by HLP. Hyperliquid's validator set voted to delist JELLY perps within minutes, settled all positions at the opening price, and the Hyper Foundation made non-flagged users whole. The defense worked — bad debt was contained and users were compensated — but the resolution required active validator coordination and produced months of debate about how meaningfully a "validator delist" emergency button differs from a CEX. The lesson JELLY carries forward is specifically about listing perps on assets with thin, manipulable spot liquidity, not about leverage in general. It is a constraint on what deployers can list, not on how much leverage they can offer.

For a direct comparison on the 1000x dimension, [opt.fun](https://www.dlnews.com/articles/markets/hyperliquid-protocol-cranks-up-the-risk-with-1000x-leverage/) is the cleaner reference. Opt.fun is a separate Hyperliquid-ecosystem protocol that announced 1000x leverage options trading with one-minute expiry on BTC and PUMP. The opt.fun design has a property the perp version does not: user loss is bounded by the premium paid, because it is an option. A 1000x perp has no such bound. The position can in principle go further underwater than the collateral if a liquidation cascade slips, with the residual landing on HLP and ultimately on Hyperliquid's protocol-level backstops.

## What HIP-3 Does Not Outsource

The most useful thing the HIP-3 documentation makes explicit is the split of responsibilities. A deployer is responsible for:

- Oracle selection and integrity. If the oracle gets manipulated, the deployer is on the hook, and if validators rule the manipulation produced "irregular inputs," potentially slashed.
- Leverage caps, contract specifications, and listing curation.
- Collateral asset choice. Non-slashable but real: it changes who eats the loss if the collateral itself depegs or fails.
- Market settlement and halt decisions, via the `haltTrading` action.

A deployer does not touch:

- The matching engine and order book. HyperCore-operated.
- The margin engine and liquidation logic. The "half-of-initial" maintenance formula is unified.
- The backstop liquidator vault and the ADL fallback. Those belong to HLP and the validator set.
- Protocol solvency guarantees.

That distinction matters for the question of who pays when a high-leverage market blows up. First line of defense is the trader's own collateral. From there the loss-absorption stack is Hyperliquid's: the order book absorbs what it can, then the backstop liquidator vault funded by HLP, then auto-deleveraging (ADL) closing against opposite-side profitable positions, then in the worst case validator intervention of the JELLY variety. None of those downstream layers sit on the deployer's balance sheet. The 500,000 HYPE stake is a clawback for deployer misconduct. It is not an insurance fund sized to absorb a portfolio of 1000x-leveraged blowups.

This is the structural point about builder-deployed perps and high leverage: a deployer can offer leverage that consumes Hyperliquid's solvency stack as the backstop. The stake-to-slash threshold prices in the deployer's incentive to behave. It does not, directly, price in the volume of bad debt their leverage choices can route into HLP.

## The Design Space, Honestly

There is a version of papertrade where the structural critique above mostly does not apply: small-ticket gambling positioning, $5-50 user balances, position caps that prevent anyone from running the headline leverage in size, growth-mode fees that make tiny tickets economically coherent. That product is closer in spirit to opt.fun than to a real perp venue. The name *papertrade* — paper trading is practice trading, sometimes literally fake money — even gestures at it. If the live product is parameterized that way, blow-ups stay inside individual user balances and HLP is not stressed.

There is another version where the critique lands cleanly: no meaningful position caps, listed against deep crypto-major liquidity, full headline leverage available to anyone who shows up. That version routes the kind of liquidation flow into HLP that the JELLY governance precedent was about, with extra steps. Which version is live is what the docs would settle.

## What HIP-3 Still Has To Decide

The deployer-stake-to-leverage envelope is the thing HIP-3 has not yet been tested on at scale. The 500,000 HYPE requirement was set when HIP-3 launched, in a context where the expected deployer was something like trade.xyz. It maps to the cost of misconduct, not to the size of the bad-debt envelope a deployer's product choices can generate. As more deployers test how far the leverage envelope can be pushed, the empirical question is how much liquidation flow products at the extreme actually generate and whether HLP's exposure profile shifts as a result.

Hyperliquid has a working precedent for governance intervention in JELLY. It does not have a working precedent for pricing structural risk into deployer stakes ex ante. The first one is a fire alarm. The second is a building code. The next interesting HIP-3 story may be whether the building code shows up before another fire.

For the moment, the practitioner takeaway is narrower. Hyperliquid's CLOB is a deep on-chain execution surface. HIP-3 is a real category, and trade.xyz-class deployers are doing real work. The same primitive that runs a 24/7 S&P 500 perp also runs a 1000x leverage product. The product label tells you which side of that primitive you are standing on.

## Quick Reference

- HIP-3 went live on Hyperliquid mainnet on October 13, 2025. ([Hyperliquid Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals))
- Builder-deployed perps grew to roughly 35% of Hyperliquid volume and peaked near $2.3 billion in open interest by April 2026, with trade.xyz responsible for the large majority of that OI. ([TheBlock](https://www.theblock.co/post/393810/hyperliquid-hip-3-markets-1-43-billion-open-interest-24-7-trading-tokenized-equities-commodities), [CoinDesk](https://www.coindesk.com/markets/2026/03/10/hyperliquid-s-permissionless-market-smashes-usd1-2-billion-in-open-positions-as-oil-and-equity-futures-boom))
- Deployer staking requirement is 500,000 HYPE (~$20M at mid-May 2026 prices); unstaking takes 7 days during which stake remains slashable; deployers receive a fixed 50% fee share; HIP-3 user-side fees are 2x validator-operated markets (3 / 9 bps maker / taker at base). ([Hyperliquid Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals), [Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees))
- Hyperliquid maintenance margin is half the initial margin at max leverage; backstop liquidation triggers at two-thirds of that. ([Hyperliquid Docs — Liquidations](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations))
- The JELLYJELLY incident (March 26, 2025) is the working precedent for validator intervention against manipulated thin-liquidity perps. ([CoinDesk](https://www.coindesk.com/markets/2025/03/26/hyperliquid-delists-jellyjelly-after-vault-squeezed-in-usd13m-tussle), [Halborn post-mortem](https://www.halborn.com/blog/post/explained-the-hyperliquid-hack-march-2025))
- Opt.fun is the closest 1000x-leverage comparable in the ecosystem — options, not perps, with one-minute expiry on BTC and PUMP. ([DL News](https://www.dlnews.com/articles/markets/hyperliquid-protocol-cranks-up-the-risk-with-1000x-leverage/))

For related defiprime coverage: [Hyperliquid vs. Aster](/hyperliquid-vs-aster) and the [Hyperliquid Chain ecosystem deep dive](/hyperliquid-chain-deep-dive). The product page for [Hyperliquid](/product/hyperliquid) sits in the [perps](/perps) collection.
