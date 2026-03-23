---
git-date:
layout: [blog]
title: "Three Token Fundraising Models Inspired by the SEC's March 17 Release"
permalink: token-fundraising-models-post-sec
h1title: "Three Token Fundraising Models Inspired by the SEC's March 17 Release"
pagetitle: "Three Token Fundraising Models Inspired by SEC Interpretive Release 33-11412"
metadescription: "The SEC's Interpretive Release 33-11412 cleared specific crypto activities. We explore three speculative fundraising models inspired by the new guidance and where the legal risk still lives."
category: blog
featured-image: /images/blog/token-fundraising-models-post-sec-ogp.png
intro: "The SEC's Interpretive Release 33-11412 cleared specific crypto activities. We explore three speculative fundraising models inspired by the new guidance and where the legal risk still lives."
author: sawinyh
tags: ["Analysis"]
---

On March 17, the SEC and CFTC jointly published [Interpretive Release No. 33-11412](/sec-defi-release-33-11412), a 68-page document that did something the crypto industry had been begging for since 2017: it drew actual lines. Not enforcement actions disguised as guidance. Not speeches that contradicted each other from one commissioner to the next. Lines.

The release classifies crypto assets into five categories and declares that specific, common crypto activities, staking, liquid staking derivatives, wrapping, and qualifying airdrops, "in the manner and under the circumstances described," fall outside securities law. It also introduces a "separation doctrine" that gives projects a potential off-ramp from investment-contract status once they decentralize. Chairman Paul Atkins said the quiet part loud: "Most crypto assets are not themselves securities."

We've read the release cover to cover. The legal analysis has been done to death by every law firm with a blockchain practice. What hasn't been explored yet is this: *what design space does this guidance open up, at least in theory?*

**An important caveat before we go further:** The release cleared specific activities as they commonly exist today. It did not pre-approve novel fundraising structures that chain those activities together in new ways. The three models below are thought experiments, not legal opinions. They use primitives the SEC described, but combine them into constructions the release never analyzed. Any team considering something like these would need its own legal counsel and a fact-specific analysis. We flag the legal risk for each model honestly, including where we think the arguments are weakest.

With that framing, here are three token-based fundraising and treasury designs that become *easier to reason about* after 33-11412, even if they aren't blessed by it. We ran economic simulations on each, and the numbers are interesting regardless of where the legal lines ultimately land.


## What Actually Changed (the 90-Second Version)

For readers who haven't waded through the release, here's what the SEC and CFTC actually said. Note: these apply to activities "in the manner and under the circumstances described" in the release, meaning existing common practices, not hypothetical new constructions:

**Native tokens of functional, decentralized networks are digital commodities.** Bitcoin, Ethereum, Solana, Cardano, Chainlink, and at least ten others are named explicitly. If no single person or group controls a network's operations, economics, or upgrades, the native token is probably a commodity under CFTC jurisdiction, not the SEC's.

**Staking is administrative, not a securities offering.** Self-staking, delegated staking, custodial staking, liquid staking, all of it. Rewards come from programmatic rules, not from a team's managerial efforts. Lido's stETH, Rocket Pool, Jito, and every other LSD protocol just got a regulatory shield.

**Liquid staking receipt tokens are not securities.** They're one-for-one receipts evidencing ownership. Trade them on DEXs, use them as collateral, bridge them, whatever. No registration needed.

**Wrapping is safe.** Deposit an asset, get a wrapped version. As long as it's one-for-one and redeemable, the wrapped token is not a security.

**Qualifying airdrops fail the Howey test.** No consideration from recipients means no "investment of money." Community drops, retroactive rewards, testnet airdrops, all clear.

**The separation doctrine describes a potential exit.** The release suggests that once promises are fulfilled, code is open-sourced, and the network genuinely decentralizes, the token may separate from any prior investment contract. But the conditions are fact-specific and require careful legal analysis, it's not a mechanical trigger you can just declare. As the Aurum Law analysis noted, you'll likely need a legal opinion benchmarked against your own prior representations.

That's what the release actually cleared. Below, we explore what *might* be buildable in its spirit, with full acknowledgment that these are extrapolations, not covered ground.


## Model 1: Liquid Genesis Staking Pools (LGSP)

![LGSP Model](/images/blog/token-model-lgsp.png)

*"Stake-to-Own the Network"*

This is probably the most immediately deployable model here. It could ship on Ethereum or Solana in weeks using existing audited staking contracts.

### How It Works

On day one, users stake blue-chip commodities (ETH, SOL, wrapped BTC, USDC) into a non-custodial pool. They immediately receive a liquid staking receipt token, the exact kind of instrument 33-11412 just cleared. The pooled capital becomes the protocol's bootstrap treasury and liquidity. In exchange, stakers earn two streams:

1. Normal yield from the underlying assets (standard LSD returns)
2. Pro-rata emissions of the protocol's native commodity token, minted programmatically as staking rewards, with no sale, no consideration

Once the network hits predefined decentralization milestones (node count, open-source code, live governance), the separation doctrine kicks in and the commodity token trades freely.

### The Economics

The "fundraise" is locked TVL, not sold equity. Protocol revenue from fees, MEV, or deployed yield gets split:

- 50% auto-compounded back into the staking pool, boosting LSD yield
- 30% used to buy back and redistribute native tokens through staking rewards only
- 20% to treasury for grants and operations

We ran a 12-month simulation starting from $10M TVL with a 5% LSD base yield, 20% annual token emission relative to TVL, 10% protocol revenue, and 2% monthly organic TVL growth. By month 12, the TVL reached roughly $13.3M. The circulating token supply hit about 116M tokens. Market cap landed around $2.5M with a token price near $0.02.

Early stakers capture upside while the protocol gets instant, sticky capital.

### The Legal Case and Its Limits

Of the three models, LGSP stays closest to what the release actually describes. Each individual component, staking, LSD issuance, programmatic rewards, is an activity the SEC addressed. The release says staking rewards are payments in exchange for services provided to the network, not profits from managerial efforts.

The open question is whether combining these primitives into a deliberate fundraising mechanism changes the analysis. A staking pool designed from day one to bootstrap a protocol's treasury looks different from Ethereum validators earning rewards on an established network. If users are staking primarily because they expect the new protocol's token to appreciate, a court might view that differently than the SEC's description of routine staking. The team's conduct matters enormously here: any marketing that frames staking as an investment opportunity could undermine the entire structure.


## Model 2: Commodity Pre-Participation Agreements (CPAs)

![CPA Model](/images/blog/token-model-cpa.png)

*The SAFT Killer*

SAFTs were an awkward compromise. They acknowledged the token might be a security at launch and tried to paper over the gap with a promise of future utility. CPAs skip the problem entirely.

### How It Works

Instead of selling tokens, the project issues irrevocable network participation rights as smart-contract NFTs or wrapped receipts. Contributors earn these rights by providing:

- Capital (staked into the protocol)
- Liquidity provision
- Work (running nodes, building integrations, community development)

These rights are wrapped commodities that automatically convert into the native token only after publicly verified decentralization milestones, exactly the trigger the separation doctrine describes.

Different contribution types get multipliers:

- Capital staker: 1x
- Node operator: 3x
- ZK-proof verified builder: 5x

Users can trade the wrapped rights on any DEX before conversion. They're treated as commodities the whole time.

### The Economics

There's no fixed cap or price. Allocation is dynamic based on actual contribution value. Vesting is milestone-based, not time-based, which means incentives align with genuine decentralization instead of calendar dates.

Total supply of 1B tokens might break down as:

- 40% reserved for CPA conversions
- 30% ongoing staking and airdrop rewards
- 20% protocol treasury, released only post-separation
- 10% liquidity bootstrapping

Early participants "pre-mine" their allocation through real work and capital while the project raises actual resources without ever selling a security.

The CPA model starts with a $5M initial contribution raise, giving it an immediate war chest. With a 50% ongoing treasury allocation and flat 10% emission cap, our simulation showed treasury staying above 29 months of runway through the first year. By month 12, TVL reached $13.5M, and token price sat around $0.46. Dilution over five years stayed at only about 40%, the best price performance of all three models.

### The Legal Case and Its Limits

The SAFT had a structural contradiction: you're selling something and simultaneously arguing it's not the thing you need registration to sell. CPAs attempt to sidestep this by never selling the token directly.

But here's where it gets uncomfortable: "participation rights" that convert into tokens post-milestones and trade on DEXs in the meantime look a lot like investment contracts. If people are buying these rights on a DEX because they expect the token conversion to be profitable, that's hard to distinguish from a securities offering regardless of the wrapping mechanism. The SEC's release cleared wrapping of existing non-security crypto assets on a one-for-one basis, not wrapping novel pre-token claims. A CPA right is not wETH. Calling it a "wrapped commodity" doesn't make it one if the underlying right hasn't been established as a commodity in the first place.

This model would need the strongest legal opinion of the three, and the outcome is genuinely uncertain.


## Model 3: Separation-Accelerated Revenue Rights (SARR)

![SARR Model](/images/blog/token-model-sarr.png)

*The Decentralization Bond*

This one is the most intellectually interesting because it turns the separation doctrine from a legal off-ramp into an economic primitive.

### How It Works

Early supporters (stakers, LPs, or contributors) receive wrapped revenue commodity rights, a claim on a percentage of all protocol fees, paid exclusively in the native commodity token.

The mechanism that makes this novel: the revenue share automatically decreases every time a decentralization milestone is hit and verified on-chain. The formula is simple:

> Revenue share at time t = Initial share x (0.75)^m

Where m = number of completed milestones. Start at 10% of fees going to early holders. After the first milestone, it drops to 7.5%. After the second, 5.6%. After the third, 4.2%.

This creates a direct economic incentive for the team to decentralize fast, because decentralization triggers the separation doctrine sooner and makes the underlying token trade freely, expanding the market and increasing volume-based revenue even as the per-unit share shrinks.

Holders can wrap and trade these rights on DEXs from day one.

### The Economics

The model creates a "decentralization bond" market. The price of rights rises as milestones approach because the revenue share is front-loaded. Protocol revenue stays inside the token ecosystem (no external stablecoin payouts). Post-full separation, rights convert 1:1 into the native token or expire.

In our simulation, SARR showed the strongest long-term treasury sustainability. By month 45, the project achieves positive treasury, with growing runway thereafter. By month 60 (five years), the treasury covers 6-7 months of operating expenses and is still growing. Dilution stayed around 49% over five years. The decay function means every milestone literally pays the dev team more, since less revenue flows to early holders and more stays in the treasury.

### Why SARR Is Interesting as a Design Primitive

It attempts to solve the biggest problem in crypto: aligning the founding team's financial interests with actual decentralization. Under the old regime, founders had every reason to maintain control, because that's where the value accrued. SARR inverts this. Centralization is expensive (high revenue share to early holders). Decentralization is profitable (lower share plus freely tradable commodity token).

### The Legal Case and Its Limits

Of the three models, SARR has the most obvious legal vulnerability. A claim on a percentage of protocol fees, paid in the native token, that decays over time, looks like a profit-sharing instrument under almost any reading of Howey. Calling it a "wrapped revenue commodity right" is creative labeling, but substance matters more than labels in securities law. The release cleared wrapping of existing non-security crypto assets. It did not address wrapping novel revenue claims.

The decay mechanism is economically elegant but doesn't solve the Howey problem. If anything, the milestone-gated structure reinforces that holders are depending on the team's managerial efforts to hit decentralization targets that increase the token's tradability. A skeptical regulator would have a strong argument here.


## Can These Models Actually Fund a Real Team?

This is the question that kills most novel tokenomics. Elegant mechanisms that can't pay ten engineers and an auditor are academic exercises.

We ran 60-month projections for all three models using these assumptions:

- Team of 10, fully loaded at $3M/year for Years 1-2, tapering to $2.5M in Year 3 and $2M in Years 4-5 as community contributors scale in
- $10M starting TVL
- 8% annualized protocol revenue capture (conservative for [Aave](/aave)/[Lido](https://lido.fi/)-class protocols)
- 2.5% monthly organic TVL growth
- Emission caps that taper over time (15% to 10% for LGSP, flat 10% for CPAs, 8% for SARR)
- Buyback logic: when runway exceeds 6 months, 50% of excess treasury buys back and burns tokens on a DEX

The honest answer: all three models are tight in Year 1. At $10M TVL, protocol revenue starts around $800K/year, well below the $3M dev budget. This isn't unique to these models. It's the reality of bootstrapped DeFi. Lido didn't become self-sustaining overnight either.

But by Year 4-5, TVL compounds to roughly $44M, generating around $3.5M/year in revenue. At that point, all three models become self-sustaining. CPAs get there fastest thanks to the $5M initial raise. SARR builds the most durable long-term treasury because the revenue decay function channels increasing fees to the project as it decentralizes.

The buyback mechanism matters here. When treasury exceeds 6 months of runway, excess capital buys and burns tokens. This creates a positive feedback loop: higher TVL produces more revenue, more revenue builds treasury, excess treasury supports price, higher price makes staking more attractive, which grows TVL further. It's the same flywheel [Maker](/makerdao) and Lido use, just built into the model from genesis.

For the bridge period (roughly months 1-18), projects using LGSP or SARR would pair with a small strategic round under the startup exemptions Chairman Atkins has proposed, or simply launch with enough initial staking deposits to generate adequate revenue. CPAs solve this natively with the initial contribution raise.


## What About the Caveats?

We'd be doing the reader a disservice if we didn't flag the structural risks, beyond the model-specific issues above.

**33-11412 is interpretive guidance, not statutory law.** It's the SEC's view of how existing law applies. It doesn't bind courts, and a future commission could revise it. That said, revising a jointly issued SEC/CFTC interpretation would be politically expensive and legally complex. This is about as durable as non-legislative guidance gets.

**Promissory language still triggers Howey.** If your whitepaper says "our team will work to increase token value," you've probably created an investment contract regardless of how clever your staking mechanism is. The models above only work if the team avoids profit promises and lets the protocol's programmatic design speak for itself.

**Centralized control is still the red line.** If a team retains operational, economic, or voting control, the asset may remain an investment contract. The separation doctrine rewards genuine decentralization, not cosmetic governance.

**Antifraud rules apply.** Misrepresentations, pump-and-dump schemes, and failure to deliver still trigger enforcement. AML, tax, and state-level regulations still apply. The SEC cleared specific activities, not all behavior.

**DeFi TVL sits around $95B as of March 2026, with $68B on Ethereum alone.** The market absorbed a significant correction in February (DeFi TVL dropped 12% in dollar terms), but ETH deposited in protocols actually increased by 2.7 million ETH during the downturn. Capital is rotating into yield-bearing positions. The regulatory clarity from 33-11412 should accelerate this, but "should" and "will" are different words.


## What Comes Next

The 33-11412 release is open for public comment. CFTC rulemaking on commodities oversight is still pending. Congressional market structure legislation is working through committees. There's a gap between the guidance we have and the statutory framework we'll eventually get.

But the gap is navigable now in ways it wasn't two weeks ago. Protocols can design around the five-category taxonomy instead of guessing. They can use staking, wrapping, and airdrops as fundraising primitives without wondering whether each one is a potential enforcement action. And they can build toward the separation doctrine as a defined milestone rather than a vague aspiration.

Every individual component in the models above, staking pools, LSD issuance, wrapped receipts, programmatic rewards, milestone-gated conversion, on-chain revenue sharing, exists in production today across multiple chains. What 33-11412 provides is clearer language around those individual primitives. What it does *not* provide is a blessing for novel combinations of those primitives into fundraising mechanisms the release never contemplated.

That's the honest gap. The release makes it easier to reason about these designs. It does not make them safe to ship without serious legal work. LGSP is closest to covered ground. CPAs and SARR are more creative but carry proportionally more legal risk, SARR especially.

The next few months will reveal whether founders treat the release as a starting point for careful legal engineering or as a green light for creative tokenomics. History suggests some will do the latter and regret it. The design space is genuinely more interesting after March 17. But "more interesting" and "legally cleared" are very different things.

---

*Disclaimer: This article is not legal advice and was not written or reviewed by attorneys. It represents our observations on what might theoretically be possible in the design space opened by Interpretive Release 33-11412. The models described are speculative thought experiments, not recommendations. The SEC's release cleared specific existing activities under specific conditions; it did not analyze or approve the constructions described here. Anyone considering building on these ideas should engage qualified legal counsel for a fact-specific analysis. The tokenomic simulations use illustrative assumptions and are not predictive. Nothing here constitutes financial or investment advice.*
