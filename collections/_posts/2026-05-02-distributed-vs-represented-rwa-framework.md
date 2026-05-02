---
git-date:
layout: [blog]
title: "Distributed vs. Represented: A Cleaner RWA Lens, and a Harder Path to $100B"
permalink: distributed-vs-represented-rwa-framework
h1title: "Distributed vs. Represented: A Cleaner RWA Lens"
pagetitle: "Distributed vs. Represented: A Cleaner RWA Lens, and a Harder Path to $100B"
metadescription: "rwa.xyz split tokenized assets into Distributed (~$30B) and Represented (~$438B). The lens is cleaner, but the $100B-by-year-end forecast does not survive the math."
category: blog
featured-image: /images/blog/distributed-vs-represented-rwa-framework-ogp.png
intro: "rwa.xyz split tokenized assets into Distributed (~$30B) and Represented (~$438B). The lens is cleaner, but the $100B-by-year-end forecast does not survive the math."
author: sawinyh
tags: ["Analysis", "RWAs"]
---

For most of the last two years, the headline number for "real-world assets on-chain" lumped everything into a single total. A tokenized Treasury sitting in a wallet and trading on Curve counted the same as a private-credit interest locked inside an issuer's permissioned platform. The underlying data had categories; the headline did not. The total looked impressive, the comparisons across reports were inconsistent, and the debates about whether tokenization was working ran on definitions that nobody actually shared.

In November 2025, rwa.xyz rewrote that frame. The dashboard now splits tokenized assets into two categories based on two practical questions: can the token leave the issuer's platform, and can it move peer-to-peer between wallets. Assets that pass both tests are Distributed. Assets that fail one or both are Represented. The default view on the site is Distributed, sitting at roughly $30 to $31 billion as of early May 2026. Toggle to Represented and the number jumps past $438 billion, mostly held inside permissioned institutional rails.

The lens is the most useful thing to happen to RWA data in two years. The narrative built on top of it is the part worth pushing on. Through early 2026, $100 billion in Distributed value by year-end has been the consensus forecast from sources like Bitfinex and Centrifuge's COO. Run the math against the dashboard's actual growth rate and that target requires something close to a 3.3x move in eight months, which is not what current trajectory delivers. The framework is good. The forecasts riding the framework are softer than they look.

## What the Framework Actually Says

The taxonomy is deliberately narrow. The point of the exercise was to stop having philosophical arguments about what counts as "on-chain." Instead of debating wrappers, custody arrangements, or chain choice, the framework reduces the question to two on-chain attributes that anyone can verify by reading the contract.

**Distributed assets** can be moved to wallets outside the issuing platform, and they can be transferred between wallets. The blockchain is acting as a distribution layer: capital formation is global, settlement is 24/7, and downstream protocols can plug in. Whitelist or eligibility controls on transfer do not disqualify a token from this bucket as long as cleared wallets can actually move the asset peer-to-peer. The promise here is the original tokenization promise, scaled down to what is technically true today: composability, secondary markets, and capital efficiency that depend on the asset being mobile.

**Represented assets** cannot leave the issuing platform, or cannot move peer-to-peer once they are out, or both. The blockchain is acting as a recordkeeping and reconciliation layer rather than a distribution layer. The institutional value is real, just different. Settlement is faster, books reconcile cleaner, and operational overhead drops. Holders cannot do anything with the asset on-chain that they could not do off-chain through the same issuer.

rwa.xyz is explicit that classifications evolve. The example the team uses is Figure Technologies' tokenized HELOCs, which originated as Represented (locked inside Figure's marketplace) and are now migrating toward Distributed as Figure integrates with [Solana](/solana) DeFi. The expectation is that most Represented categories will eventually flip, the speed depending on regulatory clarity and product redesign rather than on technology.

## What the Headline Numbers Hide

The most jarring effect of the new lens is that "total RWA" looks smaller. Distributed value at ~$30B is roughly an order of magnitude below the ~$438B Represented total. A casual reader looking at the headline before and after the reclassification might conclude the market shrank. It did not. What shrank is the share of the total that meets a strict on-chain mobility test.

The split also reveals what the old aggregate was hiding. The Canton Network alone accounts for something on the order of $380B in tokenized institutional value, dominated by repo, money-market, and bond collateral flows between large counterparties on a permissioned chain. Those positions are real, useful, and structurally important to TradFi rails, but they are not assets that can move into a [DeFi yield strategy](/defi-yield-risk-premium), get posted as collateral on [Aave](/aave), or trade on a public DEX. Counting them in a number compared against ~$30B of mobile, transferable on-chain assets was a category error, and the new dashboard at least separates the two.

Where this gets interesting is the asset-class breakdown. As of early May 2026:

- **Tokenized Treasuries** sit around $15B total, split between Distributed (BlackRock's BUIDL on public chains, Ondo's USDY and OUSG, Superstate, Franklin Templeton's BENJI) and Represented (institutional money-market wrappers that stay on issuer platforms). This is the category furthest along on the Distributed side. Treasuries are homogeneous, the secondary market is solved through standard DEXes, and NAV is essentially constant.
- **Private credit** shows roughly $5B Distributed against $18 to $19B in the broader category, with most of the gap sitting in Represented vehicles. The names typically associated with Distributed private credit include Apollo's ACRED, Maple's syrupUSDC and syrupUSDT line, and the Centrifuge issuer set, though individual bucket assignment can change as issuers tighten or loosen transfer logic. The Represented slice is dominated by Figure's HELOC stack and large institutional credit platforms.
- **Tokenized stocks** clock about $1.2B in Distributed value, growing fast off a small base and concentrated in the cohort of issuers that came online after the U.S. stablecoin and securities-tokenization rules clarified through 2025.
- **Real estate** is around $448M total, almost entirely Distributed, almost entirely small.
- **Private equity** is a small dollar number and the fastest mover in percentage terms, up north of 160% over the trailing 30 days. That growth rate sounds dramatic, and it is, but it sits on a base small enough that one or two new tokenized fund vehicles drive most of the move. It is a signal that the category is opening, not that it is scaling.

Two patterns matter here. First, the categories that are big in dollars (private credit, repo) are heavy on Represented. Second, the categories that are growing fastest in percentage terms (private equity, stocks) are heavy on Distributed but tiny in absolute size.

The Distributed total is up roughly 5% over the last 30 days. Holding that monthly rate constant for a full year compounds to about 1.8x, which gets the category to roughly $54B. The same math against the eight months left in 2026 lands closer to $44B. The $100B-by-year-end forecast requires something close to 3.3x in eight months. That is not extrapolation, it is a step change, and it has to come from a discrete event: Figure's HELOC book flipping fully into Distributed, a major institutional issuer launching public-chain wrappers that pass the mobility test at scale, or a regulatory move that unlocks part of the Represented stack. The 5% monthly rate itself is also extrapolated, which is worth flagging: a single large issuance in the trailing 30 days can flatter the rate, and growth this small in absolute dollars is not a stable trend line yet.

## Transferable Is Not Tradable

The framework tells you whether a token can move, not whether anyone is moving it. Distributed is a technical attribute of the contract. Liquidity is a market attribute, and on most Distributed RWAs it is still thin.

The Treasuries category is the exception. BUIDL flows into composability vehicles like Securitize's sBUIDL and feeds part of the collateral basket behind Ethena's USDtb, [Ondo](https://ondo.finance/)'s USDY and OUSG clear through standard DEX pairs, and the spread between primary issuance and secondary venues is tight. Treasuries also benefit from being homogeneous: every $1 of BUIDL is fungible with every other $1, and a buyer's reservation price is essentially the risk-free rate plus a small wrapper premium. Pricing is easy, so liquidity follows.

Private credit is where the framework's limits are most visible. A tokenized fund interest can be Distributed in the rwa.xyz sense (mobile to outside wallets, transferable peer-to-peer) and still trade by appointment. The Centrifuge issuer pipeline, one of the larger Distributed private-credit conduits, has been live for years, and most of its share tokens sit in holder wallets between redemption windows rather than circulating. The closest thing to a real secondary venue for this category is [Agra Bonds](/agra-bonds-tokenized-credit-exchange), an early Ethereum CLOB for tokenized credit, and even there the books are thin enough that any institutional position has to be exited in pieces.

Equities are even earlier. The newer tokenized stock issuers can technically move tokens between wallets, but the secondary venues are immature, the primary issuance is small, and the regulatory perimeter for who can hold a tokenized U.S. equity outside the U.S. is not fully resolved. So the tokens clear the Distributed test on-chain while still sitting in a legal grey zone for some holders and trading in books that are too thin to absorb size. The framework classifies these as Distributed, and that classification does not promise anything about whether the holder can exit at scale.

The same gap shows up in commodities. PAXG and the larger tokenized-gold issuers have real DEX volume and stable pegs, but most of the long tail of Distributed metal tokens is dormant in practice. We mapped the venue-by-venue picture in [the tokenized metals guide](/tokenized-metals-onchain-2026). The category looks healthier on the rwa.xyz dashboard in aggregate than the on-chain transfer activity outside the top issuers would suggest.

## Why Things Stay Represented

The default explanation for why an asset is Represented is "regulation," and that is the right answer most of the time, but it is not the only one. rwa.xyz does not break Represented assets out by reason; the bucket is binary. Reading across the category, though, three distinct reasons keep showing up, and they have very different migration profiles.

The first is regulatory perimeter. Tokenized U.S. securities sold to non-U.S. holders, or tokenized fund interests with KYC requirements that the issuer cannot enforce post-transfer, generally have to live behind a transfer hook that prevents peer-to-peer movement entirely or restricts it to whitelisted addresses tightly enough that the asset functions as platform-bound. Figure's HELOCs were the canonical example, with the loan-level disclosures, state-by-state lending licenses, and consumer-protection rules requiring the issuer to keep the asset inside its own marketplace until the legal architecture caught up. The migration toward Distributed only became possible after Figure built the supporting compliance machinery to enforce equivalent controls on a public chain.

The second is product design. Some institutional products are Represented by intent rather than by regulatory necessity. The Canton repo network is the cleanest case: the entire point of running tokenized repos on a permissioned chain is that the participants want a closed system with shared atomic settlement, not a publicly-tradable instrument. There is no Distributed version of that product because the buyers do not want one.

The third is operational. Many earlier tokenization efforts shipped without the contract-level transfer logic, on-chain registry support, or off-chain reconciliation needed to let the asset leave the issuer's platform safely. Those products are Represented because the team has not yet built the rails to make them Distributed, not because they have a structural reason to stay locked. Those are the cases most likely to flip in the next two years.

The rwa.xyz team's migration thesis (Represented becomes Distributed over time) is broadly correct, but the speed depends on which bucket each Represented asset is actually in. Regulatory-driven assets flip when rules change, which is slow and uneven. Design-driven ones do not flip at all, and probably should not. Operations-driven ones flip whenever the issuer puts engineering hours into the problem, which is usually fast once the decision is made.

## Where the Framework Stops Short

The two-bucket split solves the worst measurement problem in RWAs. It leaves a few smaller ones in place. The Distributed total is a useful denominator, but treated on its own it is a proxy for "real on-chain progress" only by accident.

Liquidity is the obvious one. A token can be Distributed and have zero secondary volume, and the dashboard will not tell you which is which. Regulatory fit is similar: a tokenized U.S. equity sold to a non-U.S. retail wallet can clear both attribute tests and still be in a grey zone legally. Custody concentration is invisible too. A Distributed asset can be held almost entirely by the issuer and a handful of insider wallets, with the float available to outsiders functionally zero. Cross-chain fragmentation adds another wrinkle: the same asset issued on multiple chains can show up across Distributed totals while still being illiquid on each chain individually because the order books are not consolidated.

These are limits of any binary classification, not failures of the framework. The two-attribute split is the right level of abstraction for a public data product, and analysts are expected to layer their own filters on top. The mistake the framework is trying to prevent is using the headline Distributed number as a one-shot answer to "is tokenization working."

There is also the question of how the rwa.xyz total compares with what other trackers report. DefiLlama's RWA category aggregates protocol-level TVL using its own inclusion rules; the totals do not match rwa.xyz on either Distributed or Represented because the methodologies are different. Chainalysis tends to publish flow-based numbers rather than outstanding stock. The Distributed/Represented split makes the rwa.xyz slice more legible than it used to be, but rwa.xyz is one tracker among several, not the authoritative denominator. Any single "total tokenized RWA" figure in a 2026 report should still come with the lens that produced it, and the rwa.xyz lens is curated with the issuers themselves, which is worth keeping in mind when reading the bucket assignments.

## What to Watch

Two signals over the next few quarters will tell us whether the discrete events the $100B forecast actually depends on are happening.

The first is private credit migration with real secondary volume behind it. The single highest-leverage move available is for the largest Represented private credit platforms (Figure being the cleanest example) to complete the transition to Distributed. Even a partial flip on the Figure HELOC book alone would meaningfully change the Distributed total without any new origination. The piece worth watching is not the contract-level migration but whether the migrated assets actually clear volume on venues like [Agra](/agra-bonds-tokenized-credit-exchange) on the credit side and [emerging tokenized-stock venues](/exchanges) on the equities side. Migration without trading just relabels Represented as Distributed-but-dormant.

The second is Treasury composability. The Distributed Treasury stack is roughly $15B and growing on the wrapper side, but the share of that stack that is actually integrated into [lending markets](/decentralized-lending), [yield strategies](/defi-yield-risk-premium), and [tranched credit products](/tranched-credit-markets) is still small. If [BUIDL](https://www.blackrock.com/) and Ondo become standard collateral across two or three more major lending venues over the next two quarters, the Distributed-to-utilized ratio improves materially and the category starts to look like real infrastructure rather than a parking lot.

"Distributed vs. Represented" is now standard vocabulary in serious RWA discussions, and the framework itself is unlikely to change much from here. The work left is on the analysts using it. The Distributed total is a much sharper denominator than the old aggregate, but the dashboard answers a narrow question: what can move. The harder questions, especially what is actually moving and where it actually clears, sit on top of that and stay with the reader.

The numbers above (~$30B Distributed, ~$438B Represented, asset-class breakdowns, growth rates) are point-in-time snapshots from early May 2026 sourced from the [rwa.xyz dashboard](https://app.rwa.xyz/). The Represented total in particular moves quickly as the Canton repo book reprices and as institutional issuance comes on and off chain. The interesting thing about a framework that classifies a moving target is that the categories change faster than reports about them get written.
