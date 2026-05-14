---
git-date:
layout: [blog]
title: "Papertrade's 1000x Perps on Hyperliquid: What HIP-3 Permits, and What I Couldn't See"
permalink: papertrade-hyperliquid-1000x-perps
h1title: "Papertrade's 1000x Perps: HIP-3 Mechanics and What's Still Hidden"
pagetitle: "Papertrade's 1000x Perps on Hyperliquid: What HIP-3 Permits, and What I Couldn't See"
metadescription: "Papertrade.xyz pitches 1000x leverage on Hyperliquid as a HIP-3 deployer. Here's what HIP-3 actually permits, the leverage math against Hyperliquid's documented engine, and the gap between marketing claims and verifiable product specs."
category: blog
featured-image: /images/blog/papertrade-hyperliquid-1000x-perps-ogp.png
intro: "Papertrade.xyz pitches 1000x leverage on Hyperliquid as a HIP-3 deployer. Here's what HIP-3 actually permits, the leverage math against Hyperliquid's documented engine, and the gap between marketing claims and verifiable product specs."
author: sawinyh
tags: ["Analysis"]
---

Hyperliquid spent 2024 and most of 2025 answering one question well: can a perpetual futures venue run fully on chain and still match a centralized exchange on execution? The answer was yes, with a custom L1, HyperBFT consensus, sub-second finality, and a CLOB that handled tens of billions of dollars in daily volume during peak weeks. By April 2026 the platform was clearing roughly $40 billion in weekly perp volume, holding around $9.5 billion of open interest, and capturing the majority of decentralized perp activity on most days.

What changed in October 2025 is that anyone with 500,000 HYPE staked could deploy their own perpetual futures market on top of that infrastructure. HIP-3, the builder-deployed perps standard, went live on mainnet on October 13, 2025. By April 2026 those builder-deployed markets accounted for over 35% of all Hyperliquid trading volume and peaked near $2.3 billion in open interest. The dominant deployer, trade.xyz, ran tokenized equities and commodities and accounted for roughly 90% of HIP-3 open interest at the time those figures were reported.

Papertrade.xyz is one of the smaller HIP-3 deployers. It puts a 1000x leverage offer on the front page and pitches itself as "the first fair-launched fully onchain perpetual exchange built on Hyperliquid." The marketing copy emphasizes "1000x leverage, 0 market impact, 100% user owned, fully onchain." A mobile app and full documentation are listed as coming soon. The team is not publicly named at the time of writing.

### What I could and couldn't see

This piece deserves an honest caveat up front. The papertrade.xyz marketing site, its X account, and the docs.papertrade.xyz subdomain all returned access errors or weren't indexed when I tried to load them directly for this article, so the marketing copy above is reconstructed from search-engine summaries rather than a first-hand read of the product. I have no on-chain confirmation of papertrade's HIP-3 deployer wallet, no asset list, no oracle list, no audit reports, no team identity, no documentation, and no per-deployer volume or TVL figures. What I can do is reason from public HIP-3 mechanics about what a deployer in this position can and cannot configure, and run the leverage math against Hyperliquid's documented liquidation engine. Those two things, together with the JELLYJELLY precedent from March 2025 and the trade.xyz trajectory since October, are what this piece is actually about. Take everything specific to papertrade as commentary on the marketing pitch and the structural envelope, not as analysis of a fully-disclosed product. If papertrade ships public documentation, much of this becomes verifiable rather than inferred.

## What Papertrade Is, Mechanically

Papertrade.xyz is a HIP-3 deployer. That means three concrete things.

First, somewhere on the books a wallet has 500,000 HYPE staked against the deployment, and that stake is subject to slashing by validator vote if the markets it runs are deemed to have caused "irregular inputs that cause invalid state transitions or prolonged downtime" (up to 100%), or lesser performance issues (up to 50% or 20% depending on severity). HYPE has traded around $39 in mid-May 2026, putting the deployer stake at roughly $20 million in current terms. It also takes a 7-day unstaking queue to remove, during which the stake remains slashable. That is the cost of misconduct, and it is meaningful — though not necessarily large relative to the bad-debt envelope an aggressive market can route into Hyperliquid's solvency stack.

Second, papertrade chose its own oracle, its own leverage caps, its own collateral asset, its own listed contracts, and (within HIP-3's permitted range) its own fees. What it did not choose is the matching engine, the orderbook infrastructure, the margin engine, or the solvency guarantees underneath. Those belong to Hyperliquid's validator set and are unified with the rest of HyperCore. HIP-3 deployers operate "essentially their own perpetual futures exchange built on top of HyperCore," in the framing the docs use: their own storefront, the same underlying plumbing.

Third, papertrade gets a fixed 50% of fees from its markets. Users pay 2x the base rate compared to validator-operated markets, the protocol takes the other half, and the deployer can also configure additional fee shares between 0 and 300% on top (0 to 100% if running in "growth mode" where taker fees can be cut roughly ninety percent). That is the economic engine for a deployer: the more volume the storefront generates, the more fee flow accrues, against a fixed staking cost.

What papertrade is selling on top of that infrastructure is leverage. Specifically, headline leverage that goes well above the 40x cap Hyperliquid imposes on its own validator-operated perps for crypto majors.

## What "Synthetic Perpetuals" Means Here

The "synthetic" framing in papertrade's marketing is doing meaningful work. Standard perpetual futures on Hyperliquid reference the underlying spot price of a listed asset (BTC, ETH, HYPE, the long tail of crypto names) and settle in USDC. HIP-3 deployers can pick any quote asset and any oracle-defined reference. Trade.xyz uses that to run perps on equities, indices, and commodities, where the spot price comes from oracle feeds pointing at off-chain venues rather than on-chain liquidity. That is what makes them "synthetic": there is no on-chain market for the underlying, just a contract that pays out the oracle's reading of one.

For papertrade specifically, the public marketing does not list which assets are on the menu (the docs aren't live yet) and the available signal is that it positions itself as a Hyperliquid-native perp exchange with extreme leverage. Whether the assets it lists are crypto perps, tokenized assets, or oracle-fed synthetics shapes the risk profile in different directions. Crypto perps reference deep CEX liquidity. Tokenized-asset perps reference oracle feeds that may close on weekends or experience reporting gaps. Pure synthetics with thin reference markets are where most of the historical oracle-manipulation incidents have happened.

Until the asset list is public it is fair to treat "synthetic perpetuals" as a positioning choice that makes the product feel modern, rather than as a description of a specific mechanism. The relevant fact for risk is which oracles feed which contracts, and that is information the live site does not yet expose.

## The 1000x Leverage Math (With Caveats)

Two big caveats before any number: Hyperliquid's documented margin formula is given with examples that cap at 40x for validator-operated markets, and HIP-3 deployers can configure their own leverage caps and (in some forms) their own risk parameters. So extrapolating the formula linearly to 1000x is a thought experiment about what the documented engine would imply, not a verified description of how papertrade actually has its markets parameterized. With that flagged:

Hyperliquid documents maintenance margin as half the initial margin at max leverage. At 40x leverage on BTC perps, the maintenance margin is 1.25%. At 3x leverage on a long-tail name, it's 16.7%. These are the thresholds at which an account is sent into liquidation via the orderbook. If equity falls below two-thirds of maintenance margin without a successful book fill, the liquidator vault (a component strategy of HLP, Hyperliquid's community liquidity pool) absorbs the position as a backstop. If that same formula extended linearly to 1000x, maintenance margin would be roughly 0.05% of notional and a five-basis-point adverse move would liquidate. In practice, no responsible venue would let the linear extrapolation hold, so the live papertrade configuration almost certainly imposes tighter constraints somewhere: position size caps, isolated margin only, stepped maintenance margin curves at extreme leverage, or different liquidation triggers. Without the docs, the linear-extrapolation number is a ceiling on how sloppy the math could get, not a description of how it actually does work.

The fee math is on firmer ground but still requires care. Hyperliquid's published base perp fees are 0.015% maker / 0.045% taker at the lowest staking and volume tier. HIP-3 markets pay 2x the standard rate, which gives roughly 3 / 9 basis points of notional at base, before any "growth mode" rebates a deployer might enable. At 1000x leverage, that 9-bp taker fee equals 90% of the trader's collateral on the entry alone. A round trip — entry plus exit, both as taker — runs about 180% of collateral, so the headline fees on a maxed-out position are bigger than the collateral backing it. A 1000x trader either uses far lower effective leverage than the headline number, runs in growth mode where taker fees are slashed by roughly 90% to about 0.5 bps, or accepts that every entry-and-exit is a structurally losing trade absent a sharp directional move that opens fast and closes faster than fees and funding accrue.

The other practical wrinkle: "0 market impact" and "0 slippage" are not properties of the math at 1000x. Hyperliquid's CLOB is among the deepest in DeFi for size, but a trader posting 100 USDC at 1000x is holding 100,000 USDC of notional. When that position is auto-liquidated, the position size is the leveraged size, not the collateral. Liquidating 100,000 USDC of notional through Hyperliquid's actual order book has whatever slippage profile that pair has at that size. The "0 slippage" claim, where it appears, is doing one of two things: either it refers to the experience of opening a position (where the CLOB is in fact very deep) or it is marketing language not anchored to an execution claim.

None of this is specific to papertrade. It is the structural reality of any high-leverage perp product. What is specific to the papertrade pitch is that 1000x sits at the extreme end even within crypto, where 100x has historically been the headline number on offshore venues and 40x is what mature on-chain venues permit on majors.

## The Two Reference Points

The HIP-3 surface so far has two useful reference points, each with its own complications.

Trade.xyz is the largest deployer by far. It uses HIP-3 to run tokenized stock, index, and commodity perps on Hyperliquid: S&P 500 and NASDAQ futures, pre-IPO contracts (Cerebras' CBRS being one example), and tokenized gold, silver, and oil. The product targets 24/7 access to traditional markets, which is a real and underserved demand, and per recent ecosystem reporting has hit 24-hour volumes in the multi-billion-dollar range with tens of thousands of unique daily traders. Trade.xyz's leverage caps are conservative compared to what's coming next in HIP-3 — the product sells access, not extremity. Calling trade.xyz the "responsible" template would be too strong though: tokenized equity perps are oracle-dependent on TradFi venues, can experience weekend reporting gaps, and the pre-IPO contracts in particular reference assets with no real spot liquidity. They are a different risk profile, not a smaller one.

The other reference is the JELLYJELLY incident from March 2025. The details matter, because the analogy to a 1000x perp product is weaker than it first looks. JELLY was a coordinated attack rather than a passive blow-up: an attacker opened a roughly $4.5 million short and two ~$2.5 million longs on a thinly-traded memecoin perp, then pumped the spot price by more than 400% in an hour on outside venues. The short was then made uneconomic to liquidate through the order book and inherited by HLP. Hyperliquid's validator set voted to delist JELLY perps within minutes, settled all positions at the opening price, and the Hyper Foundation made non-flagged users whole. The defense worked, in that bad debt was contained and users were compensated, but the resolution required active validator coordination and produced months of debate about how meaningfully different a "validator delist" emergency button is from a CEX. The lesson JELLY carries forward is narrow: a deployer who lists a perp on an asset with thin, manipulable spot liquidity is creating a configuration the validator set is willing to override. That is a real constraint on what an HIP-3 deployer can list. It is not, strictly, a leverage-level lesson.

For a more direct comparison on the 1000x dimension, the cleanest reference is [opt.fun](https://www.dlnews.com/articles/markets/hyperliquid-protocol-cranks-up-the-risk-with-1000x-leverage/), a separate Hyperliquid-ecosystem protocol that announced 1000x leverage options trading with one-minute expiry on Bitcoin and Pump.fun. Opt.fun's design has an important property the perp version does not: the user's loss is bounded by the option premium paid, because it is an option. A 1000x perp has no such bounding. The position can in principle go further underwater than the collateral if the liquidation cascade slips, with the residual landing on HLP and ultimately on Hyperliquid's protocol-level backstops.

## The Steel-Man for 1000x

Before treating 1000x as a failure mode, it is worth taking the design choice seriously on its own terms. A product called *papertrade* offering 1000x leverage could reasonably be positioned as a gambling-adjacent or entertainment product, where users post small dollar amounts ($5-50), accept the lottery framing explicitly, and the leverage is the point rather than a serious risk-management tool. Read that way, the fee math doesn't sting as much (a 90%-of-collateral entry fee on a $10 ticket is $9, comparable to a casino vig), the "0 slippage" claim makes more sense as marketing for tiny position sizes, and the comparison to opt.fun's options product becomes the right one. If papertrade is shipped and used at small-ticket size by a self-selecting audience, the blow-up problem stays inside individual user balances and the backstop layers are not stressed.

That framing is conjecture in the absence of asset lists, position caps, or any clear product positioning beyond a 1000x number on a marketing page. It is the version of the product where the structural critique above doesn't quite apply. The version where it does apply is the version with no position caps, listed against deep crypto-major liquidity, with serious-sounding marketing language. Which version is live is something the docs would settle.

## What HIP-3 Does Not Outsource

The most useful thing the HIP-3 documentation makes explicit is the split of responsibilities. The deployer is responsible for:

- Oracle selection and integrity. If the oracle gets manipulated, the deployer is on the hook (and, if validators rule the manipulation produced "irregular inputs," potentially slashed).
- Leverage caps, contract specifications, and listing curation. The deployer decides what users can do.
- Collateral asset choice. Picking a wonky collateral asset is non-slashable but real: it changes who eats the loss if the collateral itself depegs or fails.
- Market settlement and halt decisions. The deployer can halt trading via the `haltTrading` action and settle positions to mark price.

What the deployer cannot touch:

- The matching engine and orderbook. Those are HyperCore validator-operated.
- The margin engine and liquidation logic. The 1.25%-of-notional maintenance threshold scales with chosen max leverage, but the formula is unified.
- The backstop liquidator vault and the ADL fallback. Those belong to HLP and the validator set.
- Protocol solvency guarantees. These are Hyperliquid's, not the deployer's.

That distinction matters for the question "who pays if a papertrade market blows up." The first line of defense is the trader's own collateral. From there the loss-absorption stack is Hyperliquid's: the orderbook absorbing the liquidation, then the backstop liquidator vault funded by HLP, then auto-deleveraging (ADL) closing against opposite-side profitable positions, then in the worst case the kind of validator intervention JELLYJELLY produced. None of those downstream layers sit on papertrade's balance sheet. They sit on Hyperliquid's. The HIP-3 staking requirement is a 500,000 HYPE clawback for deployer misconduct, not an insurance fund sized to absorb a portfolio of 1000x-leveraged blowups.

This is the structurally important point about builder-deployed perps and high leverage: a deployer can offer leverage that consumes Hyperliquid's solvency stack as the backstop. The stake-to-slash threshold prices in the deployer's incentive to behave. It does not, in any direct way, price in the volume of bad debt their leverage choices can route into HLP.

## What Is Verifiable, and What Is Not

A clean separation, since this article rests on what could not be checked as much as on what could:

**From the documented Hyperliquid side, verifiable:** the 500,000 HYPE staking requirement, the 7-day slashable unstaking queue, the 2x HIP-3 fee multiplier, the 50% deployer fee share, Hyperliquid's published base perp fees of 0.015% / 0.045% maker / taker, the documented "half initial margin" maintenance formula at 3-40x, the backstop liquidator and HLP flow, and the JELLY validator-delist precedent.

**From the papertrade side, asserted by marketing but not independently verified:** the 1000x leverage cap, the "0 slippage" claim, the "fair launch" framing, and the claim of being a HIP-3 deployer in particular.

**Not currently public from any source I could reach:** the team identity, audit reports, asset list, oracle list, the actual maintenance margin formula papertrade uses, position size caps if any, growth-mode fee configuration, per-deployer TVL or trading volume, and the deployer wallet address (which would let on-chain stake verification happen). The papertrade docs subdomain returned 403 to my tooling; the marketing site says docs are coming soon.

The reasonable read is that papertrade is a small, recently-launched HIP-3 deployer leaning into extreme leverage as its differentiation. The structural critique in this piece applies to a particular version of that product. The docs would settle which version is live.

## The Broader HIP-3 Question

The more interesting question sits one layer above papertrade itself. HIP-3 was framed by its supporters as a way to bring 24/7 traditional-asset trading, exotic synthetics, prediction markets (under HIP-4), and bespoke crypto contracts onto a shared, high-performance settlement layer. The trade.xyz arc has largely delivered on that framing. Tokenized commodities and equities became a category, HIP-3 open interest peaked above $2 billion, and the deployer fee model has produced economically meaningful businesses on top of Hyperliquid.

The same surface that lets a builder list a Cerebras pre-IPO perp also lets a builder ship a 1000x crypto-perp. The protocol's defenses against the second case are staking economics (~$20M cost of misconduct at current HYPE prices), validator slashing for state corruption, validator delisting for manipulation precedent, and the structural reality that high-leverage products often self-limit through user blow-up rates. Those defenses do not prevent the product from being deployed. They constrain how much damage it can cause before the rest of the stack intervenes.

What's worth watching, in HLP's exposure data and in any future HIP-3 governance discussion, is whether the deployer-stake-to-bad-debt ratio is meaningfully calibrated for the leverage envelope deployers are now offering. The 500,000 HYPE requirement was set when HIP-3 launched and HIP-3 markets were a new category. It has not, to my knowledge, been re-examined in the context of 1000x products. Whether that conversation needs to happen depends on how much liquidation flow products like papertrade actually generate, which is the empirical question the next six months will answer.

For practitioners, the takeaway is narrower. Hyperliquid's CLOB remains a deep on-chain execution surface; HIP-3 is a real category; trade.xyz-class deployers are doing real work; and the same primitive that runs a 24/7 S&P 500 perp also runs a 1000x leverage product. The product label tells you which side of the primitive you are standing on. The product docs, when they ship, will tell you whether the structural critique above applies.

## Quick Reference

- HIP-3 went live on Hyperliquid mainnet on October 13, 2025. ([Hyperliquid Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals))
- Builder-deployed perps grew to roughly 35% of Hyperliquid volume and peaked near $2.3 billion in open interest by April 2026, with trade.xyz responsible for the large majority of that OI. ([TheBlock](https://www.theblock.co/post/393810/hyperliquid-hip-3-markets-1-43-billion-open-interest-24-7-trading-tokenized-equities-commodities), [CoinDesk](https://www.coindesk.com/markets/2026/03/10/hyperliquid-s-permissionless-market-smashes-usd1-2-billion-in-open-positions-as-oil-and-equity-futures-boom))
- Deployer staking requirement is 500,000 HYPE; unstaking takes 7 days during which stake remains slashable; deployers receive a fixed 50% fee share; user-side fees are 2x validator-operated markets at base rates. ([Hyperliquid Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals))
- Hyperliquid maintenance margin is half the initial margin at max leverage; backstop liquidation triggers at two-thirds of that. ([Hyperliquid Docs — Liquidations](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations))
- The JELLYJELLY incident (March 26, 2025) is the working precedent for what happens when thin-liquidity leverage meets the backstop liquidator. ([CoinDesk](https://www.coindesk.com/markets/2025/03/26/hyperliquid-delists-jellyjelly-after-vault-squeezed-in-usd13m-tussle), [Halborn post-mortem](https://www.halborn.com/blog/post/explained-the-hyperliquid-hack-march-2025))
- A separate Hyperliquid-ecosystem protocol, opt.fun, has marketed 1000x leverage on options (not perps) with 1-minute expiry on BTC and PUMP. ([DL News](https://www.dlnews.com/articles/markets/hyperliquid-protocol-cranks-up-the-risk-with-1000x-leverage/))

This piece is point-in-time as of mid-May 2026. HIP-3 is moving quickly; papertrade.xyz has not yet shipped accessible public documentation; specific volume and TVL figures will shift. Treat the Hyperliquid-side mechanics (staking, fees, liquidation flow) as verified from the docs and the papertrade-side specifics as inference from marketing copy and structural envelope, not as a description of a fully disclosed product.

For related defiprime coverage: [Hyperliquid vs. Aster](/hyperliquid-vs-aster) and the [Hyperliquid Chain ecosystem deep dive](/hyperliquid-chain-deep-dive). The product page for [Hyperliquid](/product/hyperliquid) sits in the [perps](/perps) collection.
