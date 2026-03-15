---
git-date:
layout: [blog]
title: "yvUSD: Inside Yearn's Zero-Fee Stablecoin Vault"
permalink: yvusd-yearn-stablecoin-vault
h1title: "yvUSD: Inside Yearn's Zero-Fee Stablecoin Vault"
pagetitle: "yvUSD: Inside Yearn's Zero-Fee Stablecoin Vault"
metadescription: "Deep dive into Yearn Finance's yvUSD V3 vault: zero fees, nine active strategies, unlocked vs locked modes, where the yield comes from, and how the risks stack up."
category: blog
featured-image: /images/blog/yvusd-ogp.png
intro: "A deep dive into Yearn's yvUSD V3 vault: zero fees, nine active strategies, two deposit modes, and an honest look at where the yield comes from."
author: sawinyh
tags: ["DeFi Guides", "Yield Aggregators"]
---

Yearn Finance launched yvUSD on January 19, 2026. It's a V3 cross-chain, cross-asset stablecoin vault, not a simple USDC-only vault, with zero management fees, zero performance fees, and two deposit modes. At the time of writing it runs nine active yield strategies, though that number is dynamic and managed by the vault operator. If you've been watching the stablecoin yield space this year, those numbers alone probably caught your attention. Zero fees on a yield aggregator is unusual. Strategies spanning lending, fixed income, and points farming is ambitious. And the two-mode system (unlocked vs. locked) is a design choice I haven't seen done quite this cleanly before.

This article breaks down how the vault actually works, where the yield comes from, what the risks look like in practice, and how it stacks up against the alternatives. I've tried to write the kind of analysis I'd want to read before putting real money into this thing.

## What yvUSD is, mechanically

At the contract level, yvUSD is a Yearn V3 Allocator Vault. That means it's an ERC-4626 compliant smart contract that accepts USDC deposits on Ethereum mainnet, mints shares proportional to your deposit, and then deploys that capital across a portfolio of yield-generating strategies spanning multiple stablecoins and chains. Yearn's own [announcement](https://www.cryptointegrat.com/p/ethereum-news-march-13-2026) describes it as "a cross-chain, cross-asset vault for best in class stablecoin yield." The deposit token is USDC, but the vault's strategies convert into sUSDS, siUSD, and other stablecoin derivatives as part of normal operation.

ERC-4626 matters here because it's become the standard interface for tokenized vaults in DeFi. Any protocol that supports 4626 can plug into yvUSD without custom integration work. Your shares are yield-bearing ERC-20 tokens, which means they're transferable, composable, and can be used as collateral elsewhere if a lending market accepts them.

The V3 architecture is a big upgrade from Yearn's V2 system. In V2, strategies were locked to a single vault in a one-to-one relationship. In V3, strategies are themselves standalone ERC-4626 compliant contracts, Yearn calls them "Tokenized Strategies." Per [Yearn's V3 docs](https://docs.yearn.fi/developers/v3/overview): "strategies are now fully ERC-4626 compliant, stand-alone vaults" that "can now be connected to many different vaults simultaneously and can also be deposited into directly by an end user." This is a meaningful architectural change: strategies can serve multiple allocator vaults, and users can deposit into individual strategies directly if they want to bypass the allocator entirely.

The practical implication: yvUSD's current strategies are modular. They can be added, removed, or rebalanced without migrating the entire vault. The Debt Allocator contract handles capital distribution across strategies based on target allocations set by the vault manager, and an on-chain APR Oracle helps inform those allocation decisions.

**Vault specs as of March 13, 2026:**

- Asset: USDC (Ethereum mainnet, cross-chain via Circle's CCTP)
- TVL: $3.02M
- Fees: 0% management, 0% performance
- Risk score: 3/5 (Yearn's self-assessment)
- Contract: `0x696d02Db93291651ED510704c9b286841d506987` (per the [Yearn UI vault page](https://yearn.fi/vaults/1/0x696d02Db93291651ED510704c9b286841d506987); note that yvUSD may use multiple contracts across its allocator and strategy architecture, always verify the address you're interacting with on [yearn.fi](https://yearn.fi) directly)


## The unlocked/locked design

This is the architectural decision that distinguishes yvUSD from a standard Yearn vault. When you deposit, you choose between two modes.

![yvUSD Unlocked vs Locked Modes](/images/blog/yvusd-unlocked-locked-modes.png)

**Unlocked** gives you withdrawal access at any time, subject to the vault's liquidity buffer. At the time of writing, the displayed estimated APY is around 7.14%, but this number is a trailing estimate that fluctuates based on strategy performance, incentive programs, and capital allocation. The Yearn UI may show substantially different numbers depending on the calculation window (7-day, 30-day, inception). Don't treat any displayed APY as a fixed rate. The vault ensures it always has enough capital parked in short-duration, liquid strategies (sUSDS, basic Morpho lending) so that unlocked depositors can exit without delay.

**Locked** imposes a 14-day cooldown period after you signal your intent to withdraw, followed by a 5-day window during which you can actually pull your funds. In exchange, the vault can deploy your capital into longer-duration positions that pay more, things like Pendle principal tokens with fixed maturities, deeper leverage loops on Morpho, and cross-chain L2 plays.

The idea borrows from a concept that InfiniFi (one of the protocols integrated into the vault) has been developing: depositor-directed duration matching. Traditional banks take deposits and invest them into long-duration assets while hoping everyone doesn't withdraw at once. yvUSD instead lets depositors explicitly reveal their liquidity preferences, then builds the portfolio accordingly. Locked capital funds the higher-yield, longer-duration strategies. Unlocked capital stays in liquid backstops. The vault knows exactly how much of its capital has a 14-day minimum lockup, which means it can allocate with more precision than a vault that has to assume 100% of deposits might leave tomorrow.

It's a clean tradeoff, and worth thinking through carefully. If you're not sure you'll need the money in the next three weeks, locked mode is strictly better. If there's any chance you'll need fast access, stay unlocked and accept the lower rate.


## Active strategies: where the yield comes from

Everything is published on-chain, and the [DeBank bundle](https://debank.com/bundles/221066/portfolio) shows live positions in real time. The vault currently runs nine strategies (this count is dynamic and managed by the vault operator). Here's the approximate allocation as of March 13, 2026.

![yvUSD Strategy Allocation](/images/blog/yvusd-strategy-allocation.png)


### Morpho Yearn OG USDC Compounder (28% allocation, ~3.81% APY)

This is the vault's largest single position and its most conservative strategy. It deposits USDC into Morpho Blue's isolated lending markets, specifically into markets curated by Yearn's own risk team.

Morpho Blue, for those unfamiliar, is a permissionless lending primitive that launched as an evolution of Morpho's original peer-to-peer optimization layer. Each Morpho Blue market is an isolated pair (one collateral asset, one loan asset) with immutable parameters. Risk doesn't bleed between markets the way it can in pooled protocols like Aave. The tradeoff is that you need to pick your markets carefully, or delegate that decision to a curator.

The 3.81% APY comes from borrower interest. It's real yield in the most traditional DeFi sense: someone is paying to borrow USDC, and you're earning a share of that interest. Conservative, predictable, and the risk profile is well-understood after years of lending protocol history.


### USD3 Pendle PT Maxi (20% allocation, ~7.99% APY)

This is where the vault's yield starts to get interesting. The strategy buys Pendle Principal Tokens (PTs) denominated in USD3 at a discount to face value and holds them to maturity.

A quick primer on how Pendle PTs work. Pendle splits a yield-bearing asset into two tokens: a Principal Token (PT) that's redeemable 1:1 for the underlying at maturity, and a Yield Token (YT) that captures all the variable yield until that date. If you buy PT at a discount before maturity, you've effectively locked in a fixed yield, the spread between your purchase price and the redemption value.

So if PT-USD3 trades at $0.96 with a 6-month maturity, buying it and holding to expiration gives you roughly 8% annualized. No variable rate risk, no dependency on borrow demand staying high. The yield is encoded in the purchase price.

The risk here is duration. If the vault needs to exit this position before maturity, it has to sell the PT on the open market, potentially at a loss if rates have moved against it. This is one of the key reasons the locked/unlocked design exists. Locked capital can ride PTs to maturity. Unlocked capital stays out of these positions (or the vault maintains enough liquid buffer to cover unlocked withdrawals regardless).

Pendle has become a dominant venue for this kind of fixed-income DeFi. According to [CoinMarketCap's Pendle analysis](https://coinmarketcap.com/cmc-ai/pendle/price-prediction/), stablecoins now account for roughly 83% of Pendle's TVL. The protocol also [transitioned from vePENDLE to a liquid staking model (sPENDLE) on January 20, 2026](https://coinmarketcap.com/cmc-ai/pendle/what-is/), replacing multi-year lock-ups with a 14-day withdrawal period and directing up to 80% of protocol revenue to PENDLE buybacks for sPENDLE holders.


### InfiniFi sIUSD Morpho Looper (19% allocation, 0% base APY)

This is the most unusual position in the vault, and the one that confuses people when they look at the strategy list. It shows 0% APY. Why would the vault put 19% of its capital into something earning zero?

The answer is points farming.

InfiniFi is a DeFi protocol that replicates fractional reserve banking on-chain. Users deposit USDC, mint iUSD receipt tokens, then choose between liquid staking (siUSD) or locked positions (liUSD) with different yield profiles. Per [DefiLlama](https://defillama.com/protocol/infinifi), InfiniFi holds roughly $170M in TVL, and [Messari](https://messari.io/project/infinifi-usd) reports $175M. The protocol is heading toward a token generation event (TGE) expected in early-to-mid 2026.

The vault deposits into InfiniFi, receives siUSD, then loops that position through Morpho to amplify its exposure. The 0% base APY is accurate in that no interest is being paid right now. But InfiniFi Points are accruing on the position, with enhanced multipliers for the strategies involved. Pendle's siUSD pools are offering up to 4.5x point multipliers on YT positions.

When InfiniFi's TGE happens, Yearn will monetize the accumulated points, likely through their signature permissionless Dutch auction system or OTC deals, and funnel the proceeds back into the vault. Your price-per-share goes up, and the retroactive APY on this strategy could end up being substantial. Or it could be modest. Nobody knows what InfiniFi tokens will be worth at launch.

This is the speculative component of the vault, and you should be clear-eyed about it. About 19% of the vault's capital is sitting in a position that earns nothing today, betting on future token value. Yearn has historically been good at monetizing these positions (they've been doing it since the Curve wars era), but it's still a bet, not a guaranteed yield stream.


### USDC to sUSDS Depositor (10% allocation, ~3.82% APY)

This strategy converts USDC to USDS, Sky Protocol's stablecoin, and deposits it into the Sky Savings Rate module, receiving sUSDS in return. USDS is positioned as the successor to DAI within the [Sky ecosystem](https://sky.money/features) (formerly MakerDAO), with a 1:1 upgrade path from DAI to USDS. Both tokens still exist; DAI has not been retired or renamed, but USDS is where Sky Protocol is directing new development and integrations.

The Sky Savings Rate is funded by Sky Protocol's revenue, which comes from crypto collateralized loans, U.S. Treasury bill investments, and liquidity provisioning into SparkLend. As of March 2026, sUSDS yields around [4% APY](https://www.prnewswire.com/news-releases/sky-savings-rate-now-available-to-all-developers-building-on-privy-a-stripe-company-302706752.html). Sky Frontier Foundation's own press release from March 6, 2026 describes sUSDS as having "+$10 Billion in supply," making it the largest yield-generating stablecoin by market cap. (Note: this $10B figure refers to total sUSDS tokens in circulation, not to be confused with the larger DAI/USDS base stablecoin supply.)

For the vault, sUSDS serves a dual purpose. It generates reliable baseline yield (Sky Protocol's revenue model is diversified and has operated for years under its prior MakerDAO branding), and it's highly liquid with no withdrawal constraints. This is part of the vault's liquidity buffer, the safe money that ensures unlocked depositors can always exit.

The risk here is mostly stablecoin peg risk: USDS could theoretically depeg from the dollar, or the conversion path USDC to USDS could involve slippage. In practice, USDS has maintained its peg reliably through years of market stress as DAI, and the conversion path is well-established.


### syrupUSDC/USDC Morpho Looper (10% allocation, 0% base APY)

Similar to the InfiniFi strategy, this position earns 0% in direct interest but farms points from Maple Finance's syrupUSDC program. It's a leveraged lending position on Morpho that amplifies exposure to Maple's rewards program.

Maple has been rebuilding after its 2022 credit crisis, and syrupUSDC represents their new institutional lending product. The points here are a bet on Maple's token economics and the value of being early to their relaunched ecosystem.

Same logic as the InfiniFi position: no yield today, speculative upside tomorrow. Same honest assessment: it could pay off well, or it could amount to very little.


### PT siUSD March Morpho Looper (6% allocation, ~10.8% APY)

This is the highest-APY strategy in the vault. It buys Pendle PT-siUSD tokens (which mature March 26, 2026) and leverages the position through Morpho to amplify the fixed yield.

The base PT yield is attractive on its own, around 9% fixed according to InfiniFi's Pendle V2 pool data. The Morpho loop borrows against the PT position to buy more PTs, stacking the fixed yield. If the PT yield is 9% and you can borrow USDC at 4%, the spread gets amplified through leverage.

The risk here is compounded: you have PT duration risk, Morpho liquidation risk if collateral ratios move unfavorably, and the underlying InfiniFi counterparty risk, all stacked. At only 6% of the vault, this is sized as a satellite position rather than a core holding, which seems appropriate given the risk stack.


### Smaller allocations (remaining ~7%)

Three additional strategies round out the portfolio. The exact compositions shift as the vault rebalances, but they generally involve smaller Morpho lending positions and additional PT exposures across different maturities. They provide diversification within the strategy mix without materially changing the overall risk profile.


## Where the APY numbers actually come from

Here's the honest version of what to expect.

**Sustainable baseline (unlocked): roughly 6-8% APY, estimated.** This range is derived from the combination of Morpho lending (~3.8%), Pendle PT strategies (~8-10%), and sUSDS (~3.8%), blended across the portfolio. Even if every points program goes to zero, this baseline should hold because it's driven by real borrow demand, fixed-income instruments, and protocol revenue. It already beats Aave's 3-5% and Morpho direct lending's 4-8% after their respective fee structures. But this is an estimate based on current allocations. It is not a guaranteed rate, and it will shift as strategies are rebalanced and market conditions change.

**Points premium: highly variable.** The InfiniFi and syrupUSDC strategies (about 29% of the vault combined) are currently earning zero direct yield. Their eventual contribution depends entirely on token launch valuations and Yearn's monetization execution. In a good scenario, this could add several percentage points to the annualized return. In a disappointing scenario, it might add very little.

**The 54.4% 30-day APY on the vault page is misleading.** It includes temporary launch incentives and early points monetization events that won't recur. If you're making a deposit decision based on that number, recalibrate. Plan around 6-8% and treat anything above that as a bonus.


## How Yearn monetizes points (and why it matters that you don't have to)

This is one of the smartest parts of the design, and it's worth understanding.

![How Yearn Monetizes Points](/images/blog/yvusd-points-monetization.png)

When you deposit into yvUSD, all points and reward tokens accrue to the vault's contract address, not to your wallet. You never claim anything. You never pay gas to harvest. You never have to research which airdrop campaigns are running or track eligibility criteria.

When a points program converts to tokens (at TGE or during a liquidity event), Yearn's system handles monetization. They typically use one of two mechanisms: OTC deals with market makers who want early token access, or their permissionless Dutch auction system where tokens are sold on-chain in a declining-price auction until clearing.

The proceeds flow back into the vault as additional USDC. Your share of that USDC shows up as an increase in the vault's price-per-share (PPS). From your perspective, your yvUSD tokens are simply worth more when you redeem them.

The tradeoff is real, though. If InfiniFi's token launches and immediately does a 50x, you don't capture that upside, because Yearn sold the tokens at whatever price cleared the auction. You traded potential token moonshot exposure for guaranteed passivity. For most people holding stablecoins, that's the right tradeoff. But if you're the type who wants to hold and time individual airdrops, yvUSD isn't designed for you.


## Risk analysis

Yearn rates yvUSD at 3/5 on their internal risk scale. That's an honest number, not a conservative one. Here's what's driving it.

### Smart contract risk: medium-high

Multiple strategies (nine at the time of writing, subject to change) means a large set of smart contracts interacting with the vault. Each strategy interfaces with at least one external protocol (Morpho, Pendle, InfiniFi, Sky). The total smart contract surface area is large. Yearn's V3 codebase has been audited and has processed hundreds of millions in TVL across other vaults, but the specific strategies in yvUSD are newer and less battle-tested.

A bug in any single strategy could result in losses to the portion of capital deployed there. Yearn's architecture does provide some containment, since strategies can be revoked and capital recalled if issues are detected, but forced revocation during an exploit can still crystallize losses.

### Leverage risk: present

The Morpho looper strategies (InfiniFi looper, syrupUSDC looper, PT siUSD looper) use leverage. They borrow against their positions to amplify exposure. In normal markets, this amplifies yield. In stressed markets, it amplifies losses and can trigger liquidation.

Morpho's isolated market design means a liquidation in one market doesn't cascade into others, which is meaningfully better than pooled alternatives. But if a borrowed position hits its LLTV (Liquidation Loan-to-Value) threshold at oracle prices, the collateral gets sold. For looped positions, this can unwind rapidly.

### Duration risk: present (especially in locked mode)

Pendle PT strategies have fixed maturities. The USD3 Maxi position and the PT siUSD looper are both committed to specific expiry dates. If conditions change and the vault needs to exit early, it has to sell at market prices, which may be unfavorable.

The locked/unlocked design mitigates this significantly. Locked capital is deployed into duration-sensitive strategies with the explicit understanding that it won't be withdrawn for at least 14 days. Unlocked capital avoids these positions. But if a large amount of unlocked capital tries to exit simultaneously and the liquid buffer is insufficient, there could be withdrawal delays.

### Counterparty risk: moderate

The vault depends on InfiniFi, Sky Protocol, Pendle, and Morpho functioning correctly. Each of these is a separate protocol with its own governance, codebase, and risk profile.

InfiniFi, in particular, is the youngest and least proven of the group. It has roughly $170M TVL per [DefiLlama](https://defillama.com/protocol/infinifi) and a pre-TGE token, meaning its incentive structures are still evolving. Sky Protocol (the rebranded MakerDAO ecosystem) is at the opposite end of the spectrum, one of the most established DeFi protocols in existence.

### Bridge risk: low

Cross-chain activity uses Circle's CCTP (Cross-Chain Transfer Protocol), which burns and mints native USDC rather than relying on wrapped tokens or bridges with independent validator sets. CCTP is widely regarded as the safest cross-chain mechanism for stablecoins, since it leverages Circle's own attestation network. The risk isn't zero (Circle is a centralized entity), but it's meaningfully lower than most bridge alternatives.


## Competitive landscape

| | Aave V3 | Morpho direct | yvUSD (unlocked) | yvUSD (locked) |
|---|---|---|---|---|
| Expected APY | 3-5% | 4-8% | 6-8% sustainable | Higher (not disclosed) |
| Fees | Variable | Curator-dependent | 0% / 0% | 0% / 0% |
| Withdrawal | Instant | Instant | Instant (with buffer) | 14-day cooldown |
| Smart contract risk | Very low | Low-medium | Medium-high | Medium-high |
| Leverage exposure | None | None | Yes (partial) | Yes (more) |
| Effort required | None | Low | None | None |
| Points/airdrop exposure | None | Possible (via curator) | Yes (passive) | Yes (passive) |

**Aave** remains the obvious choice if you want the simplest, most proven option. Five years of operation, enormous TVL, instant withdrawals. The yield reflects that safety, you're paying for simplicity with lower returns. Currently around 3-5% on USDC after the protocol's fee cut.

**Morpho direct lending** (via curated MetaMorpho vaults) gives you 4-8% with more granular risk selection. You choose which vault, which curator, which risk profile. The recent Telegram integration and institutional partnerships suggest Morpho's distribution is expanding, which should sustain borrow demand. But you're trusting a curator's allocation decisions, and the newer isolated markets have a shorter track record.

**yvUSD** sits at the higher end of both yield and complexity. The 6-8% sustainable baseline comes from combining multiple yield sources that individually would be accessible but tedious to manage. The zero-fee structure means every basis point of yield goes to depositors, which is rare for an aggregator. Yearn's V2 vaults charged 2% management and 20% performance fees. The V3 yvUSD vault charges nothing.

The competitive question is whether the additional 2-4% yield over Aave justifies the additional risk surface. For someone sitting on stablecoins they don't need for three months, I think the answer is probably yes, especially in unlocked mode where you retain withdrawal flexibility. For someone who can't tolerate any smart contract risk beyond the most battle-tested protocols, Aave is still the right call.


## Projected returns on $100K

Assuming daily compounding:

| Timeframe | Conservative 7% APY | Boosted ~40% APY (temporary) |
|---|---|---|
| 1 month | ~$583 | ~$3,300 |
| 3 months | ~$1,750 | ~$10,000 |
| 6 months | ~$3,500 | ~$20,000 |
| 12 months | ~$7,000 | N/A (won't persist) |

The 7% column is your planning number. The boosted column is useful for understanding what the first few weeks or months might look like while incentive programs are active, but don't build a financial plan around it.


## Getting started

1. Navigate to [yearn.fi/v3/1/0x696d02Db93291651ED510704c9b286841d506987](https://yearn.fi/v3/1/0x696d02Db93291651ED510704c9b286841d506987)
2. Connect your wallet
3. Choose unlocked or locked mode
4. Deposit USDC and receive yvUSD shares
5. There is no step 5. No claiming, no harvesting, no rebalancing. Your PPS increases as the vault accrues yield.

To monitor positions: [DeBank transparency bundle](https://debank.com/bundles/221066/portfolio)


## What's next: yvBTC

Yearn has signaled that yvBTC is coming, following the same zero-fee, cross-chain, delta-neutral philosophy applied to Bitcoin. If yvUSD proves the model works for stablecoins, yvBTC would extend it to the most held crypto asset. Worth watching, though no timeline has been confirmed.


## Where I land

yvUSD is a well-designed product for a specific user: someone holding USDC who wants more than money-market rates, doesn't want to actively manage positions across five different protocols, and is comfortable with a 3/5 risk profile in exchange for 6-8% passive yield.

The zero-fee structure is the detail that moves it from "interesting" to "worth seriously considering." In most yield aggregators, fees eat 20% or more of your returns. Here, every basis point goes to depositors. That's a meaningful edge over time.

The risk is real. Multiple strategies, leverage in the mix, points bets on pre-TGE tokens, duration exposure in Pendle PTs. None of this is Aave-simple, and the vault page doesn't hide that (the 3/5 self-rating is refreshingly honest). But the risks are transparent, verifiable on-chain, and sized proportionally within the portfolio. The conservative core (Morpho lending + sUSDS) accounts for nearly 40% of the vault. The speculative tail (points farming) accounts for about 29%. The fixed-income middle (Pendle PTs) fills the rest.

If you're comfortable with that structure, deposit what you can afford to have illiquid for a couple of weeks in the worst case. Start with unlocked mode if you're cautious. And check the DeBank bundle periodically to verify the vault's positions match what's described here, because in DeFi, the ability to verify is the whole point.

*This article is for informational purposes only and does not constitute financial advice. Always conduct your own research and understand the risks before making any investment decisions.*
