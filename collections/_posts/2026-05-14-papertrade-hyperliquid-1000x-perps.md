---
git-date:
layout: [blog]
title: "Papertrade's 1000x Perps on Hyperliquid: What HIP-3 Lets You Build, and What 1000x Leverage Actually Means"
permalink: papertrade-hyperliquid-1000x-perps
h1title: "Papertrade's 1000x Perps and What HIP-3 Actually Permits"
pagetitle: "Papertrade's 1000x Perps on Hyperliquid: What HIP-3 Lets You Build, and What 1000x Leverage Actually Means"
metadescription: "Papertrade.xyz pitches 1000x leverage synthetic perpetuals on Hyperliquid. Here's how HIP-3 actually works, what's the deployer's responsibility, and the margin math that decides who survives."
category: blog
featured-image: /images/blog/papertrade-hyperliquid-1000x-perps-ogp.png
intro: "Papertrade.xyz pitches 1000x leverage synthetic perpetuals on Hyperliquid. Here's how HIP-3 actually works, what's the deployer's responsibility, and the margin math that decides who survives."
author: sawinyh
tags: ["Analysis", "Yield"]
---

Hyperliquid spent 2024 and most of 2025 being the cleanest answer to the question "can a perpetual futures venue run fully on chain and still match a centralized exchange on execution?" The answer was yes, with a custom L1, HyperBFT consensus, sub-second finality, and a CLOB that handled tens of billions of dollars in daily volume during peak weeks. By April 2026 the platform was clearing roughly $40 billion in weekly perp volume, holding around $9.5 billion of open interest, and capturing the majority of decentralized perp activity on most days.

What changed in October 2025 is that anyone with 500,000 HYPE staked could deploy their own perpetual futures market on top of that infrastructure. HIP-3, the builder-deployed perps standard, went live on mainnet on October 13, 2025. By April 2026 those builder-deployed markets accounted for over 35% of all Hyperliquid trading volume and topped $2 billion in open interest at peak. The dominant deployer, trade.xyz, ran tokenized equities and commodities and accounted for roughly 90% of HIP-3 open interest at the time those figures were reported.

Papertrade.xyz is the part of the HIP-3 surface that the dominant deployer is not. It is a builder-deployed perp market that puts a 1000x leverage offer on the front page and pitches itself as "the first fair-launched fully onchain perpetual exchange built on Hyperliquid." The marketing copy emphasizes "1000x leverage, 0 market impact, 100% user owned, fully onchain." The product is live; the team is not publicly named at the time of writing; a mobile app and full documentation are listed as coming soon.

This piece is not a review of papertrade.xyz as an investment opportunity. The goal is to do three things accurately: explain what HIP-3 actually lets a deployer like papertrade do (and not do), work through the margin math on 1000x leverage as it lands inside Hyperliquid's liquidation engine, and place the product in the context of the other things HIP-3 has so far produced. Specific numbers are point-in-time as of mid-May 2026 and will move.

## What Papertrade Is, Mechanically

Papertrade.xyz is a HIP-3 deployer. That means three concrete things.

First, somewhere on the books a wallet has 500,000 HYPE staked against the deployment, and that stake is subject to slashing by validator vote if the markets it runs are deemed to have caused "irregular inputs that cause invalid state transitions or prolonged downtime" (up to 100%), or lesser performance issues (up to 50% or 20% depending on severity). At HYPE's recent prices that stake is a non-trivial amount of capital pledged against the deployer behaving. It also takes a 7-day unstaking queue to remove, during which it remains slashable.

Second, papertrade chose its own oracle, its own leverage caps, its own collateral asset, its own listed contracts, and (within HIP-3's permitted range) its own fees. What it did not choose is the matching engine, the orderbook infrastructure, the margin engine, or the solvency guarantees underneath. Those belong to Hyperliquid's validator set and are unified with the rest of HyperCore. HIP-3 deployers operate "essentially their own perpetual futures exchange built on top of HyperCore," in the framing the docs use: their own storefront, the same underlying plumbing.

Third, papertrade gets a fixed 50% of fees from its markets. Users pay 2x the base rate compared to validator-operated markets, the protocol takes the other half, and the deployer can also configure additional fee shares between 0 and 300% on top (0 to 100% if running in "growth mode" where taker fees can be cut roughly ninety percent). That is the economic engine for a deployer: the more volume the storefront generates, the more fee flow accrues, against a fixed staking cost.

What papertrade is selling on top of that infrastructure is leverage. Specifically, headline leverage that goes higher than anything Hyperliquid offers natively.

## What "Synthetic Perpetuals" Means Here

The "synthetic" framing in papertrade's marketing is doing meaningful work. Standard perpetual futures on Hyperliquid reference the underlying spot price of a listed asset (BTC, ETH, HYPE, the long tail of crypto names) and settle in USDC. HIP-3 deployers can pick any quote asset and any oracle-defined reference. Trade.xyz uses that to run perps on equities, indices, and commodities, where the spot price comes from oracle feeds pointing at off-chain venues rather than on-chain liquidity. That is what makes them "synthetic": there is no on-chain market for the underlying, just a contract that pays out the oracle's reading of one.

For papertrade specifically, the public marketing does not list which assets are on the menu (the docs aren't live yet) and the available signal is that it positions itself as a Hyperliquid-native perp exchange with extreme leverage. Whether the assets it lists are crypto perps, tokenized assets, or oracle-fed synthetics shapes the risk profile in different directions. Crypto perps reference deep CEX liquidity. Tokenized-asset perps reference oracle feeds that may close on weekends or experience reporting gaps. Pure synthetics with thin reference markets are where most of the historical oracle-manipulation incidents have happened.

Until the asset list is public it is fair to treat "synthetic perpetuals" as a positioning choice that makes the product feel modern, rather than as a description of a specific mechanism. The relevant fact for risk is which oracles feed which contracts, and that is information the live site does not yet expose.

## The 1000x Leverage Math

Hyperliquid's documented liquidation engine works the same way for HIP-3 markets as for validator-operated markets, because the margin engine is unified. The maintenance margin is half the initial margin at max leverage. At 40x leverage on BTC perps, the maintenance margin is 1.25%. At 3x leverage on a long-tail name, it's 16.7%. These are the thresholds at which the account is sent into liquidation via the orderbook. If equity falls below two-thirds of maintenance margin without a successful book fill, the liquidator vault (a component strategy of HLP, Hyperliquid's community liquidity pool) absorbs the position as a backstop.

If you apply the same formula to 1000x, and HIP-3 deployers do inherit the unified margin engine even though the documented examples cap at 40x, the maintenance margin works out to roughly 0.05%. That is the live constraint: at 1000x leverage, an adverse move of about five basis points moves the account into liquidation, and a move of about three basis points (two-thirds of that) sends the position to the backstop liquidator. Five basis points on BTC is the kind of price wobble that lands inside a single minute of normal market activity. Three basis points is closer to bid-ask noise on the book at any given moment. Whether papertrade configures its specific markets to use the documented formula or some custom version is not visible without the docs that the project has labeled as coming soon.

That math has two consequences worth being clear about.

The first is that "0 market impact" and "0 slippage" do not survive the trip from marketing copy to execution. Hyperliquid's liquidation flow uses a mark price that combines external CEX prices with the local book state. When a 1000x position is auto-liquidated, the position size is the leveraged position size, not the collateral. A trader who posts 100 USDC at 1000x is holding a 100,000 USDC notional contract. Liquidating that notional through Hyperliquid's actual order book has the same slippage profile any 100,000 USDC market order would have on that pair. The "0 slippage" claim, where it appears, is doing one of two things: either it refers to the experience of opening a position, where Hyperliquid's CLOB is genuinely one of the deepest in DeFi, or it is marketing language not anchored to a specific execution claim. The math of forced liquidation cuts through it either way.

The second is that at 1000x, the trader is not really "trading." They are running a high-frequency binary lottery in which the breakeven hurdle is fees plus a few basis points of price drift, and the loss event is total. Hyperliquid's HIP-3 base fees on builder-deployed markets are 2x the standard rate, which puts them in roughly the 6 / 18 basis-points-of-notional range on maker / taker before any growth-mode adjustments. Per dollar of *collateral*, 18 bps of notional at 1000x equals 180%. The round-trip fee on a maxed-out position is bigger than the collateral backing it. In practice this means a 1000x trader either uses much lower effective leverage than the headline number, or accepts that every entry-and-exit is a structurally losing trade absent a sharp directional move that opens fast and closes faster than fee accrual. Funding rates compound the problem on either side. Most high-leverage perp products converge on a similar steady state: a small number of accounts win large amounts, the average lifetime per account is short, and the venue's economics are driven by entry-and-blow-up frequency rather than directional trading skill.

None of this is unique to papertrade. It is the structural reality of any high-leverage perp product. What is specific to the papertrade pitch is that 1000x sits at the extreme end even within crypto, where 100x has historically been the headline number and 40x is what mature venues actually permit on majors.

## Two Precedents That Matter

The HIP-3 surface so far has two reference points worth comparing papertrade against.

Trade.xyz is the responsible deployer template. It has used HIP-3 to launch tokenized stock, index, and commodity perps on Hyperliquid, including S&P 500 and NASDAQ futures, pre-IPO contracts (Cerebras' CBRS being one example), and tokenized gold, silver, and oil. The product mix points at the most underserved corner of crypto-derivative demand: 24/7 access to traditional markets, rather than higher leverage on assets that already have leverage. The result is a deployer that, per recent ecosystem reporting, has hit 24-hour volumes in the multi-billion-dollar range with tens of thousands of unique daily traders, and accounts for the bulk of HIP-3 open interest. Trade.xyz's leverage caps are conservative by HIP-3 standards; the product sells access, not extremity. That is the version of HIP-3 the Hyperliquid documentation and pitch decks tend to emphasize.

The other reference point is the JELLYJELLY incident from March 2025. Several newly-created addresses opened a $4.5 million short and two ~$2.5 million long positions on a memecoin perp, then pumped the underlying spot price by more than 400% in an hour. The short position became uneconomic to liquidate through the book and was inherited by HLP. The validator set convened, voted to delist JELLY perps, and settled all positions at the opening price. The Hyper Foundation made non-flagged users whole. Technically the defense worked: bad debt was contained, HLP losses were absorbed by the foundation, and users were compensated. But the resolution required active validator coordination, and it produced months of debate about whether a venue with a "validator delist" emergency button is meaningfully different from a CEX. The lesson HIP-3 deployers carry forward from JELLYJELLY is that thin underlying liquidity plus high leverage is exactly the configuration that forces governance interventions, and the validator set has shown it is willing to use them.

Papertrade is structurally closer to the JELLY configuration than to the trade.xyz configuration: extreme leverage on what is likely to be a mix of crypto-native assets, marketed for the kind of position sizes where the backstop liquidator and HLP would be the counterparties of last resort. Calling that out is descriptive, not a forecast that anything blows up. It locates the product on the HIP-3 design space.

There is also one outside reference: [opt.fun](https://www.dlnews.com/articles/markets/hyperliquid-protocol-cranks-up-the-risk-with-1000x-leverage/), a separate Hyperliquid-ecosystem protocol that announced 1000x leverage options trading with one-minute expiry on Bitcoin and Pump.fun. Opt.fun's framing is closer to honest: an options product, with explicit one-minute time decay, where the premium is the entire risk and the leverage is on the premium. That product is structured so that the user's loss is bounded by what they paid. A 1000x perp does not have that bounding. The position can in principle go further underwater than the collateral if the liquidation cascade slips, with the residual landing on HLP and ultimately on Hyperliquid's protocol-level backstops.

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

Specific claims that the public surface area of papertrade lets a third party verify right now:

- It positions itself as a HIP-3 deployer (consistent with the marketing language about being "fully onchain" and "on Hyperliquid"). On-chain confirmation that the wallet behind papertrade has the required 500,000 HYPE staked is the kind of thing the project will be expected to surface in the documentation it has marked as coming soon.
- The 1000x leverage number is in the marketing copy. Whether all listed assets get that cap, or just some, is not visible without docs.
- The "0 market impact" claim is doing marketing-language work; the underlying execution surface is Hyperliquid's CLOB, which is genuinely deep but is not literally zero-impact for any position size that matters.
- The "first fair-launched fully onchain perp exchange on Hyperliquid" claim is unfalsifiable in practice; HIP-3 deployers have not produced a shared definition of "fair launch."

Claims that cannot currently be verified from public sources, as of mid-May 2026:

- The team. No publicly named founders surface in search.
- Audits. No audit reports surface in search.
- Live TVL, deposits, and trading volume specific to papertrade's markets. Hyperliquid surfaces HIP-3 OI in aggregate; per-deployer breakdowns require either trade.xyz-style PR disclosure or direct chain analysis.
- The asset list and the oracles backing each contract.
- Whether a fundraise occurred. The closest things to papertrade-named funding events in search are unrelated companies (paper.xyz, the NFT payments processor, and Trade[XYZ], the HIP-3 tokenized-stocks deployer).

The reasonable read is that papertrade is a small, recently-launched HIP-3 deployer running on top of Hyperliquid's plumbing, leaning into extreme leverage as its differentiation. Whether it accrues a real user base or stays a footnote inside the HIP-3 expansion will be visible in HLP's exposure data and in HIP-3 volume breakdowns over the coming months.

## The Broader HIP-3 Question

The interesting story is not really papertrade itself. It is what the existence of papertrade tells us about HIP-3.

HIP-3 was pitched and largely received as "the iPhone moment for permissionless perp creation," a way to bring 24/7 traditional-asset trading, exotic synthetics, prediction markets (under HIP-4), and bespoke crypto contracts onto a shared, high-performance settlement layer. The trade.xyz arc has validated that pitch. Tokenized commodities and equities have become a category, HIP-3 open interest now sits in the $2 billion range at peak, and the deployer fee model has produced economically meaningful businesses on top of Hyperliquid.

What papertrade demonstrates is that the same surface that lets a builder list a Cerebras pre-IPO perp also lets a builder ship a 1000x crypto-perp. The protocol's defense against that is partially staking economics (cost of misconduct), partially validator slashing (cost of state corruption), and partially the structural reality that high-leverage perps tend to attract a self-selecting user base whose blowup rate keeps the product's volume from compounding too far. None of those defenses prevent the product from existing. They constrain how much damage it can cause before validators step in.

The thing to watch is whether HLP's exposure profile changes as more deployers test how far the leverage envelope can be pushed. HLP is the actual backstop for everything HIP-3 routes into it. The community-owned vault that absorbs Hyperliquid's bad debt also absorbs the bad debt that any HIP-3 deployer creates. If 1000x products like papertrade route enough liquidation flow into the vault, the next conversation Hyperliquid has to have is whether the deployer's slashable stake should be sized to the leverage offered, not just to the cost of running an irregular market. That is a governance question rather than a contract question, and the precedent for that conversation already exists. The validator set used it on JELLY.

For practitioners, the immediate takeaway is narrower. Hyperliquid's CLOB is still the best execution surface in DeFi. HIP-3 is a real category and trade.xyz-style deployers are doing real work. And the same primitives that let trade.xyz run a 24/7 S&P 500 perp let papertrade run a 1000x leverage one. The product label tells you which side of that primitive you are standing on.

## Quick Reference

- HIP-3 went live on Hyperliquid mainnet on October 13, 2025. ([Hyperliquid Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals))
- Builder-deployed perps grew to roughly 35% of Hyperliquid volume and topped $2 billion in open interest at peak by April 2026, with trade.xyz responsible for the large majority of that OI. ([TheBlock](https://www.theblock.co/post/393810/hyperliquid-hip-3-markets-1-43-billion-open-interest-24-7-trading-tokenized-equities-commodities), [CoinDesk](https://www.coindesk.com/markets/2026/03/10/hyperliquid-s-permissionless-market-smashes-usd1-2-billion-in-open-positions-as-oil-and-equity-futures-boom))
- Deployer staking requirement is 500,000 HYPE; unstaking takes 7 days during which stake remains slashable; deployers receive a fixed 50% fee share; user-side fees are 2x validator-operated markets at base rates. ([Hyperliquid Docs](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals))
- Hyperliquid maintenance margin is half the initial margin at max leverage; backstop liquidation triggers at two-thirds of that. ([Hyperliquid Docs — Liquidations](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations))
- The JELLYJELLY incident (March 26, 2025) is the working precedent for what happens when thin-liquidity leverage meets the backstop liquidator. ([CoinDesk](https://www.coindesk.com/markets/2025/03/26/hyperliquid-delists-jellyjelly-after-vault-squeezed-in-usd13m-tussle), [Halborn post-mortem](https://www.halborn.com/blog/post/explained-the-hyperliquid-hack-march-2025))
- A separate Hyperliquid-ecosystem protocol, opt.fun, has marketed 1000x leverage on options (not perps) with 1-minute expiry on BTC and PUMP. ([DL News](https://www.dlnews.com/articles/markets/hyperliquid-protocol-cranks-up-the-risk-with-1000x-leverage/))

This piece is point-in-time as of mid-May 2026. HIP-3 is moving quickly; papertrade.xyz has not yet shipped public documentation; specific volume and TVL figures will shift. Treat the leverage math as the load-bearing claim. Treat the per-deployer traction figures as snapshots.

For related defiprime coverage: [Hyperliquid vs. Aster](/hyperliquid-vs-aster), the deeper [Hyperliquid Chain ecosystem](/hyperliquid-chain-deep-dive), and the asset-primitive gap analysis from [on-chain forex](/onchain-forex-asset-primitive-gap) and [on-chain interest rate swaps](/onchain-interest-rate-swaps-yield-stripping). The product page for [Hyperliquid](/product/hyperliquid) sits in the [perps](/perps) collection.
