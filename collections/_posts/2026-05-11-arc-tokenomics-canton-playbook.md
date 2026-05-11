---
git-date:
layout: [blog]
title: "Circle's ARC Tokenomics: The Numbers Circle Hasn't Published Yet"
permalink: arc-tokenomics-circle-whitepaper
h1title: "Circle's ARC Tokenomics: The Numbers Still Missing"
pagetitle: "Circle's ARC Tokenomics: The Numbers Circle Hasn't Published Yet"
metadescription: "Circle closed a $222M ARC presale at $3B FDV and published a whitepaper that leaves the dilution-determining parameters to a governance vote. Reading the document carefully."
category: blog
featured-image: /images/blog/arc-tokenomics-canton-playbook-ogp.png
intro: "Circle closed a $222M ARC presale at $3B FDV and published a whitepaper that leaves the dilution-determining parameters to a governance vote. Reading the document carefully."
author: sawinyh
tags: ["Analysis", "Stablecoins"]
---

Circle published the [ARC whitepaper](https://www.arc.network/blog/introducing-the-arc-token-whitepaper) on May 11, 2026 and disclosed that it had closed a $222M private presale of the ARC token at a $3B fully-diluted valuation. The round placed 740M tokens at $0.30 each, about 7.4% of the 10B initial supply. a16z crypto led at $75M, with participation from BlackRock, Apollo Funds, ICE, ARK Invest, Bullish, Haun Ventures, SBI Group, Janus Henderson, Standard Chartered Ventures, General Catalyst, Marshall Wace, and IDG Capital. Per [CoinDesk](https://www.coindesk.com/business/2026/05/11/circle-raises-usd222-million-for-arc-blockchain-token-sale-at-usd3-billion-valuation) and [The Block](https://www.theblock.co/post/400709/circle-raises-222m-in-arc-token-presale-at-3b-fdv-from-a16z-crypto-blackrock-and-others-q1-revenue-up-20), this is the first time a publicly listed company has run a token presale. Mainnet is targeted for summer 2026; the [public testnet has been live since October 2025](https://www.ledgerinsights.com/blackrock-ice-back-circles-arc-stablecoin-blockchain-in-222m-raise-3bn-valuation/).

Those facts hold up across primary and secondary sources. The token model under the headline does not, in the same way. The whitepaper specifies the two largest buckets of the supply (60% ecosystem, 25% Circle) and a high-level fee-and-burn architecture, and then leaves to a governance vote almost every parameter that determines whether ARC holders are diluted, paid, or burned out: the inflation rate, the decay curve, the validator/burn split, the breakdown of the remaining ~15% of supply, and the vesting schedule for the presale. The chain itself is currently Proof-of-Authority. [Proof-of-Stake is a future transition](https://unchainedcrypto.com/circle-ceo-reveals-arc-network-token-plans-and-proof-of-stake-roadmap/) the token is supposed to enable.

The cheapest assumption when a token model leaves its dilution parameters to a governance vote is that the parameters end up favoring whoever is voting. The rest of this piece is the case for that lean and the conditions that would change it. Numbers below come from the May 11, 2026 whitepaper materials, Circle's same-day [Q1 release](https://www.circle.com/pressroom/circle-reports-first-quarter-2026-results), and contemporaneous reporting. Where a parameter has not been disclosed, we flag it rather than estimate it.

## What the Public Materials Actually Specify

Three things are anchored.

| Bucket | Share | Stated purpose |
|---|---|---|
| Ecosystem | 60% | Developers, grants, network growth, contributors |
| Circle | 25% | Development, staking, validator operations, governance participation |
| Remaining | ~15% | Not broken out in the public materials we reviewed |

The 60% ecosystem share is the headline. Most L1 launches over the past three years have kept the team and investor slice between roughly a third and just over half of supply, and treated the "community" bucket as a residual, often back-loaded behind multi-year cliffs.

| Chain    | Mainnet      | Team   | Investors | Insiders subtotal | Community / Ecosystem |
|---|---|---|---|---|---|
| Aptos    | Oct 2022     | 19.0%  | 13.5%     | 32.5%             | 51.0%                 |
| Sui      | May 2023     | 20.0%  | 14.1%     | 34.1%             | ~26%                  |
| Celestia | Oct 2023     | 10.7%  | 35.6%     | 46.3%             | ~20% (public + drop)  |
| Berachain| Feb 2025     | 16.8%  | 34.3%     | 51.1%             | 48.9%                 |
| Monad    | Nov 2025     | 27.0%  | 19.7%     | 46.7%             | 49.3%                 |
| **Arc**  | **Summer 2026 (planned)** | **(in 25% Circle bucket)** | **7.4%**     | **7.4% / 32.4%\*** | **60%**               |

\*Arc's 25% Circle bucket is sui generis: issuer-held by a public-company sponsor, not VC or team equity in the traditional sense. If counted as team-equivalent, Arc's insiders subtotal becomes 32.4%, at the low end of the comparator range. If counted separately (the whitepaper does), Arc's insider float is 7.4%, the lowest in the set. Either way, the 60% ecosystem share is the highest of any chain in the table. Sources: [Aptos Foundation](https://aptosfoundation.org/currents/aptos-tokenomics-overview), [Sui docs](https://docs.sui.io/concepts/tokenomics), [Celestia docs](https://docs.celestia.org/learn/TIA/staking-governance-supply/), [Berachain docs](https://docs.berachain.com/learn/pol/tokens/tokenomics), [Monad Foundation](https://www.monad.xyz/announcements/mon-tokenomics-overview).

The headline ratio is unusual. Whether it inverts the usual pattern in practice depends on vesting schedules the whitepaper does not publish, and on whether the ecosystem bucket gets spent on real builder grants or absorbed into liquidity programs that primarily benefit market-maker counterparties.

The remaining ~15% is the bucket the public materials do not detail. Treat any breakdown of it (team, foundation, advisors, ecosystem reserve) as unconfirmed until Circle publishes one.

The institutional presale at $0.30 sets the floor. At 7.4% of supply it is small relative to the seed-and-Series-A allocations many recent L1s carried. The buyer list is also unusual: traditional asset managers (BlackRock, Apollo, Janus Henderson), exchange infrastructure (ICE, Bullish), regulated banks (Standard Chartered Ventures, SBI Group), and crypto-native funds (a16z crypto, Haun, ARK) in the same round. That mix cuts the most familiar L1 launch risk, which is a large early VC float dumping into thin secondary markets in year one, because most of these buyers are not running token-flip strategies. It is also a different posture than the post-33-11412 [token-launch templates](/token-fundraising-models-post-sec) that depend on public retail allocations.

What the buyer mix does not cut is the inverse risk. The whitepaper is explicit that the chain is currently Proof-of-Authority. ARC is positioned as the asset that supports a future transition to Proof-of-Stake. That gap matters because the bull case for the token rests on the network behaving like a credibly neutral public chain, and Proof-of-Authority is by definition not that.

## The Fee-and-Burn Architecture, with Parameters Missing

The economic model the whitepaper sketches has three moving parts, two of them described and one of them blank.

ARC issuance is supposed to fund validator and staker rewards under the planned Proof-of-Stake model, on top of fees. The whitepaper does not specify a starting inflation rate or a decay curve. Both are governance-tunable.

Network fees are paid in USDC (or other stablecoins) so applications have a predictable USD-denominated cost. At settlement, the protocol converts a portion of fee revenue into ARC, routes part to validator and staker compensation, and burns part. The whitepaper does not specify the burn-to-reward ratio. Governance can set it.

The stated equilibrium is inflation neutrality, where burns from real activity offset new issuance once usage matures. Whether that equilibrium is reachable depends on three numbers the whitepaper does not yet publish: the starting issuance rate, the decay curve, and the validator/burn split. All three are governance parameters. Any pro-forma model of ARC holder dilution today is therefore a model of assumptions, not of disclosed terms.

The structural observation that does not depend on the missing numbers is on the fee base. USDC-denominated gas is explicitly designed to keep per-transaction costs low for applications, and the chain is positioning into a price-sensitive market. To produce enough fee revenue to offset issuance and start contracting supply, the network needs higher-margin activity layered on top of basic transfers, which is its own bet (see below).

Reading the document as a whole, the gap between what is anchored and what is left open is wider than the headline tokenomics tables suggest.

| Specified in the public materials       | Deferred to governance / unpublished |
|---|---|
| 10B initial supply                      | Starting inflation rate              |
| 60% ecosystem, 25% Circle allocation    | Decay curve shape                    |
| 7.4% of supply sold in the presale at $0.30 | Validator/burn split of fee revenue  |
| USDC-as-gas, EVM-friendly               | Vesting schedule for the presale     |
| Sub-second finality, opt-in privacy     | Breakdown of the remaining ~15% bucket |
| Currently Proof-of-Authority            | PoS transition timeline              |
| Fee burn plus validator reward (concept)| Burn-to-reward ratio                 |
| Summer 2026 mainnet target              | Initial validator set composition    |

The right-hand column is where ARC's long-run price behavior actually lives.

## The Demand Side Is Harder Than the Mechanism

The token model assumes higher-margin activity layers on top of stablecoin transfers. Tokenized credit issuance, FX settlement, market-making rebates, and prediction-market clearing all clear the bar. Basic transfers do not. The harder problem is that none of those activities have to land on Arc. [Canton Network](/canton-vs-evm) attracted real institutional flows (the [$438B Represented stack on rwa.xyz](https://app.rwa.xyz/) is dominated by Canton's repo and money-market book, which we sized [here](/distributed-vs-represented-rwa-framework)) because it was the only network with shared atomic settlement and the privacy guarantees DTCC and major banks needed. Arc enters a category that already has working alternatives: [Solana](/solana) for payments throughput, the [larger Ethereum L2s](https://l2beat.com/) for general DeFi, and a growing set of purpose-built stablecoin chains. The 60% ecosystem allocation is sized to subsidize the first wave of apps. Whether the second wave shows up without subsidy is the demand bet, and the whitepaper does not address it.

## The Bear Case

Circle's framing is that Arc is a public chain for institutional finance, and that ARC is the coordination asset for that network. The structural facts, taken together, lean against that framing today.

Circle is a profitable, publicly listed stablecoin issuer. The Q1 2026 release on the same day as the whitepaper shows a business in expansion mode, with net income compressed by stock-based comp and Arc-specific investment.

| Metric                              | Q1 2026 | YoY change |
|---|---|---|
| USDC onchain transaction volume     | $21.5T  | +263%      |
| USDC in circulation                 | $77B    | point-in-time |
| Total revenue and reserve income    | $694M   | +20%       |
| Adjusted EBITDA                     | $151M   | +24%       |
| Net income (continuing operations)  | $55M    | -15%       |

Circle attributed part of the net income decline to "continued investment in the company's new Arc network" along with post-IPO stock-based compensation. The ARC presale and the Q1 results are two views of the same fact: Arc is being subsidized by the existing USDC franchise.

![Bar chart of USDC onchain transaction volume per quarter, Q2 2025 through Q1 2026: $5.9T, $9.6T, $11.9T, $21.5T. Q1 2026 is highlighted as the same day Circle published the ARC whitepaper. Sources: Circle quarterly earnings releases.](/images/blog/arc-tokenomics-circle-whitepaper-usdc-quarterly-volume.png)

USDC's volume curve is the franchise. ARC is a token issued on top of a chain whose distribution moat is that curve. Whether ARC the token captures a share of that economic surface is the parameter question; the surface itself is real and growing.

Five structural facts to hold against the bull case:

- The chain is Proof-of-Authority today. "Permissionless" is aspirational, not a property of the live network.
- 25% of supply belongs to Circle. Circle can run validator infrastructure, earn staking rewards, and participate in governance with that stack.
- The presale ran to institutions only at $0.30, with no confirmed retail allocation or airdrop. The first liquid market price will come from exchange listings, with no community-distribution floor underneath it.
- All of the dilution-determining parameters (issuance rate, decay curve, burn-to-reward split, vesting schedule) are governance-tunable, and governance is initially weighted toward the parties who hold the most ARC.
- Circle, per The Block and CoinDesk, is the first publicly listed company to run a token presale. The regulatory treatment of ARC in the hands of US retail buyers is unresolved at issuance, and the structure creates a parallel capital stack on top of a CRCL equity base in which several of the presale investors (a16z chief among them) already hold positions.

The steel-man on the other side is real but narrower. Circle has 25% skin in the game and a public-company reputational cost if the network fails. Proof-of-Stake and decentralization are on a published roadmap. The testnet has been processing transactions since October 2025 at sub-second finality and has attracted concrete institutional engagement (BlackRock, Visa, Goldman Sachs, Mastercard, BNY Mellon, State Street, HSBC, Deutsche Bank, Coinbase, Kraken, AWS, and others have participated, per reporting on the October 2025 testnet launch). Governance is open in principle and will become more economically meaningful as the validator set broadens.

The narrowness is that none of those counter-points are about ARC the token. They are about Arc the network. The token's value accrual is set by parameters Circle has not yet published, voted on by holders weighted toward Circle and its presale syndicate. Until those parameters land, "the token captures Arc's success" remains an assumption that the system has not yet been wired to deliver.

## What to Watch

Four falsifiable signals, in order of which one tells you the most.

The leading indicator is the first published economic parameter set. Until governance publishes a starting inflation rate, a decay schedule, and a burn-to-reward split, the long-run distribution between staker reward, builder grant, and burned supply is undefined. The first parameter vote is the moment Arc stops being a Circle product and starts being a network. It also gives the bear lean its first real test: a parameter set that genuinely favors holders outside the presale syndicate would falsify the cheap assumption.

Mainnet contents come next. Stablecoin-denominated fees, USDC-as-gas, sub-second finality, opt-in privacy, and EVM compatibility are all described in the public materials. Whether they ship at the targeted summer 2026 mainnet or arrive on a staged roadmap will tell you which parts of the design are load-bearing.

Validator decentralization is the third. Proof-of-Authority is not a steady state for a chain whose pitch is institutional public infrastructure. The line worth watching is how broad and how independent the validator set is when PoS goes live, and whether validators outside the presale buyer list operate economically meaningful stakes.

The fourth is whether USDC volume on Arc represents external pull or internal migration. Stablecoin volume moves between chains without producing real fee revenue on either, and a chain that captures Circle's own treasury operations gets a TVL boost without proving anything about third-party demand. The interesting line is third-party app activity denominated in USDC on Arc, not headline USDC float.

The mechanism Circle has sketched (builder-heavy allocation paired with fee-driven burns) is coherent, and the buyer alignment is cleaner than most 2026 L1 launches. What stays unresolved is the parameter set the whitepaper leaves blank, the consensus model the chain has not yet transitioned, and the demand the token mechanic assumes. Day-one tokenomics rarely tell you which way that resolves. The first published parameter set will.
