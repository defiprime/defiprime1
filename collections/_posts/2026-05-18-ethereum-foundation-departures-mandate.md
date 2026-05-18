---
git-date:
layout: [blog]
title: "The Ethereum Foundation's Spring 2026 Reshuffle: Departures, the Mandate, and the Glamsterdam Window"
permalink: ethereum-foundation-departures-mandate
h1title: "The EF's Spring 2026 Reshuffle"
pagetitle: "The Ethereum Foundation's Spring 2026 Reshuffle: Departures, the Mandate, and the Glamsterdam Window"
metadescription: "Five senior Ethereum Foundation exits, a March Mandate that triggered sign-or-leave reports, and a scoped-down Glamsterdam fork. What's verified, what isn't, and what's actually at stake."
category: blog
featured-image: /images/blog/ethereum-foundation-departures-mandate-ogp.png
intro: "Five senior Ethereum Foundation exits, a March Mandate that triggered sign-or-leave reports, and a scoped-down Glamsterdam fork. What's verified, what isn't, and what's actually at stake."
author: sawinyh
tags: ["Analysis", "Governance"]
---

Between mid-February and mid-May 2026, five senior contributors stepped back from full-time roles at the [Ethereum](/ethereum) Foundation. A sixth, Alex Stokes, started an open-ended sabbatical in the same window. A seventh, Dankrad Feist, had moved to a part-time advisor role the previous October. The EF, the non-profit that funds protocol research and employs a meaningful share of L1 core contributors, also released a 38-page Mandate in March that re-anchored its self-described role in cypherpunk principles. By mid-May the X-thread version of the story was settled: ideological purge, brain drain at the worst possible moment.

The published record is messier than that. This post is point-in-time as of May 18, 2026. Some departures are still in their wind-down windows, the Glamsterdam fork is mid-devnet, and several of the most-cited claims on X are not currently in any primary EF document. Treat the figures and quoted reasons below as the cleanest version of the public record on this date, not as final.

## What actually happened

**Tomasz Stańczak (co-Executive Director).** Announced his step-down on [February 13, 2026 via the EF blog](https://blog.ethereum.org/2026/02/13/leadership-update), roughly 11 months after he took the role alongside Hsiao-Wei Wang in March 2025. The two had replaced Aya Miyaguchi, who [moved to a President role in February 2025](https://www.coindesk.com/tech/2025/02/25/ethereum-foundation-s-aya-miyaguchi-leaving-executive-director-role). Bastian Aue, previously the EF's chief of staff, was named interim co-ED. Tomasz was the first person to hold the title; there is no historical baseline for co-ED tenure, but 11 months is short by any peer-organization standard.

**Dankrad Feist (researcher).** Announced on October 17, 2025. He left full-time to join Tempo, the Stripe and Paradigm-backed L1, as an L1 advisor, while staying on as an EF advisor in parallel. A partial departure, not a clean break, but it was the first time a senior researcher publicly framed a VC-backed competing chain as the destination.

**Josh Stark (board co-steward, ~7 years).** Announced his exit on X on April 16, 2026, with end of April as his wrap-up date. Stark joined the EF in 2019, was named a board co-steward in the 2025 reorg, and was co-chair of the Trillion Dollar Security initiative. His own framing: he made the decision in early March, has "no plans for the future, other than taking a long break to reset and spending time with family." The Block carried [the announcement](https://www.theblock.co/post/397777/ethereum-foundation-exec-josh-stark-is-stepping-down).

**Trent Van Epps (Protocol Guild contributor, ~5 years).** Same day, April 16, 2026, with his last EF day on April 10. He stays inside the Ethereum ecosystem via [Protocol Guild](https://protocol-guild.readthedocs.io/), the independent funding mechanism for L1 contributors that he helped organize. According to multiple outlets covering the announcement, he publicly described EF leadership's association with the Milady NFT collection as "baffling and sad" — that line got more screenshot circulation than any other quote from this cluster.

**Barnabé Monnot, Tim Beiko, Alex Stokes (Protocol cluster, May 2026).** Announced in the EF's [Protocol Cluster Updates, May 2026](https://blog.ethereum.org/2026/05/11/protocol-update-may-26). Monnot and Beiko are moving out of the cluster; Stokes is taking a sabbatical. Three new co-leads stepped in: Will Corcoran (zkVM proving, post-quantum consensus, the Fast Confirmation Rule), Kev Wedderburn (zkEVM team), and Fredrik (Protocol Security and the Trillion Dollar Security project Stark co-stewarded). The EF blog did not publish departure rationales for any of the three.

Five full-time exits between February and mid-May, four of them (Stark, Van Epps, Monnot, Beiko) clustered inside roughly four weeks. That is a high concentration against base rates for an organization this size. It is also not, on its own, a collapse.

## The Mandate, and the alignment requirement

On [March 13, 2026 the EF published "The Promise of Ethereum: Introducing the EF Mandate"](https://blog.ethereum.org/2026/03/13/ef-mandate). The companion PDF reads as part constitution, part manifesto. The blog post itself establishes the core principle, **CROPS**: that "Ethereum must, above all, remain censorship resistant, open source, private, and secure." The Mandate frames the EF's role as steward rather than driver of adoption, and includes language warning the Foundation against trading those principles away for financialization or institutional wins.

Two specific items from the Mandate became the most-cited artifacts on X. Both deserve careful attribution because the verbatim language is harder to verify than the secondary coverage suggests:

- A passage often summarized as the **"Source Seppuku License"** — paraphrased in coverage roughly as "may the Foundation fall on its own sword if it fails to uphold its solemn promise to Ethereum." This appears as an illustration inside the document. The Source Seppuku License itself is a pre-existing satirical license from internet subculture; the EF appears to have adopted and quoted it rather than authoring it.
- A passage paraphrased in secondary coverage as the **"walkaway test"** and Ethereum as **"sanctuary technology"** — the idea that the protocol should function if the Foundation and its current developers vanished tomorrow. Neither phrase is in the public-facing blog post. They appear in the longer PDF and in secondary write-ups.

The second-order story that lit the fuse: [Cryptopolitan reported](https://cryptonews.net/news/ethereum/32610280/) that "all members of the Ethereum Foundation were asked to sign the Mandate document or be fired effective immediately." That claim went unconfirmed by EF communications. It did not appear in any on-the-record departure statement. It also did not get a clean denial. The first major exits landed four to five weeks after the Mandate was published, which is what made the sign-or-leave framing sticky.

What can be said cleanly:

- No departing contributor has publicly cited the Mandate as a reason. Stated reasons cover family time, sabbatical, product-centric roles, and (in Van Epps' case) discomfort with specific cultural choices.
- A formal sign-or-leave requirement is in published press, not just X. It is not in any EF blog post.
- A reshuffle and a Mandate dropping in the same six-week window may share an upstream cause — the 2025 reorg posture — without the Mandate triggering any individual exit.

The published record supports the question, "did the Mandate accelerate the departures." It does not currently support a clean answer in either direction.

## The Protocol cluster, in plain terms

The personnel change with the most direct upgrade-work impact is the Protocol cluster reshuffle. The new co-lead structure, per the EF's May post:

- Will Corcoran leads zkVM proving, post-quantum consensus, and the Fast Confirmation Rule.
- Kev Wedderburn leads the zkEVM team.
- Fredrik leads Protocol Security, including the Trillion Dollar Security project.

That is a reframing as much as a personnel change. The previous cluster narrative leaned on shipping-track labels ("Scaling," "UX," "Hardening") that mapped to user-facing improvements. The new framing leans on cryptographic infrastructure and security as first-class tracks, with UX-flavored work pushed out a fork.

## Where Glamsterdam stands

A widely held assumption is that Ethereum is shedding senior contributors right before the Glamsterdam fork has to ship. The fork itself has moved.

The current Glamsterdam scope, per the EF's May 2026 update and follow-on coverage:

- **EIP-7732 (ePBS)**: enshrined proposer-builder separation. Bakes the MEV market role, where specialized builders construct blocks for validators, into the protocol itself instead of leaving it to off-chain relays.
- **EIP-7928 (Block-level Access Lists)**: parallelization groundwork for execution.
- **EIP-8037 gas repricing**, with a 200M gas-limit target as the headline scaling step.
- Multi-client devnet testing is live as of May 2026; mainnet realistically Q3 2026.

What is **not** in Glamsterdam, despite frequent assumption otherwise:

- FOCIL (Fork-Choice Enforced Inclusion Lists, the censorship-resistance mechanism that lets multiple validators force transactions into blocks) — pushed to Hegotá, the upgrade after Glamsterdam.
- Native account abstraction — also pushed to Hegotá.

That deferral matters because the Glamsterdam scope is now heavier on protocol economics and throughput, lighter on the consumer-experience improvements that account abstraction and inclusion lists were going to deliver. New cluster leads are being judged on a scoped-down fork at the same time as the most-quoted user-facing items have been pushed back.

The personnel-to-execution link is the part of the story to watch. ePBS is a structurally invasive change to how blocks get produced; it intersects with active consensus-client roadmaps. If the new Protocol cluster co-leads have to absorb that integration work while still ramping into their tracks, the realistic outcome is timeline slip rather than fork failure. Glamsterdam moving to Q4 or early 2027 would not surprise anyone close to the work.

## The treasury picture, with a denominator

Separate from the personnel and Mandate story, the EF spent late 2025 and early 2026 publicly converting ETH to stablecoins to fund operations. The verifiable events:

- **July 2025:** 10,000 ETH sold to SharpLink Gaming via OTC.
- **September 2025:** announced plan to convert 10,000 ETH (~$43.6M at the time) to stablecoins.
- **October 2025:** 1,000 ETH converted via OTC for ~$4.5M.
- **2025:** further OTC sales to [BitMine](/bitmine-vs-strategy-dat-flywheels), with separate reports of 5,000 ETH and 10,000 ETH transactions.
- **April 2026:** 5,000 ETH (~$10–11M) converted via a CoWSwap TWAP execution.

For scale: the EF's Arkham-tracked portfolio sat at roughly $270M across 14 addresses in April 2026, against annual operating expenses around $100M and a previously announced 70,000-ETH staking target the Foundation [completed in early April 2026](https://www.coindesk.com/markets/2026/04/03/ethereum-foundation-stakes-another-usd93-million-ether-reaching-its-70-000-eth-target). Total stablecoin conversions visible above are well under $100M across nine months. The published [June 2025 treasury policy](https://blog.ethereum.org/2025/06/04/ef-treasury-policy) framed these as routine operational funding, not directional calls on ETH.

That ratio matters. The story that the EF is dumping ETH on weak hands while preaching purity does not survive contact with the actual flow sizes. Treasury operations and personnel transitions can move in parallel without either causing the other; reading too much into the timing here is the largest single risk in the broader narrative.

## What's actually at stake

Three things worth separating:

1. **Execution risk on Glamsterdam.** New cluster leads, narrower scope, devnet-stage. The realistic downside is timeline slip on ePBS and the 200M gas-limit target, not the fork failing outright. Q3 2026 is the current target; Q4 or early 2027 would be the visible signal that the reshuffle cost shipping velocity.
2. **Cultural and recruiting risk.** The Mandate signals a posture. If that posture is incompatible with the adoption-focused engineering talent the EF needs for Hegotá's UX work, the second-order cost is recruiting friction. That story plays out over quarters.
3. **The competing-narrative risk.** Competing chains and L2 ecosystems are recruiting Ethereum-aligned contributors aggressively and framing themselves as the place where shipping-focused work happens. The Tempo move with Dankrad is one data point. This sits adjacent to the ongoing [Ethereum staking issuance debate](/cut-ethereum-staking-issuance-debate) and the broader question of whether Ethereum's posture is being tuned for the institutional adoption wave the [CLARITY Act](/clarity-act-anchorage-wysocki) is widely expected to unlock.

None of these is a crisis. They are questions that will look obviously decided in retrospect twelve months out, in either direction, and that are unsettled today.

The signals to watch over the next two quarters are concrete. Does Glamsterdam ship close to the Q3 timeline. Does Hegotá keep account abstraction and FOCIL on track or do they slip further. Do the new Protocol cluster co-leads hold tenure long enough to push their tracks into mainnet. Does the next round of senior protocol hires come from inside the Ethereum ecosystem or from outside it. Those answers will settle the larger question more reliably than any current narrative will.
