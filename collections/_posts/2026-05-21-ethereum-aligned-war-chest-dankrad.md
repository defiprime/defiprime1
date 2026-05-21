---
git-date:
layout: [blog]
title: "Ethereum's Missing Fighter: Dankrad Feist's Case for a $1B War Chest"
permalink: ethereum-aligned-war-chest-dankrad
h1title: "Ethereum's Missing Fighter"
pagetitle: "Ethereum's Missing Fighter: Dankrad Feist's Case for a $1B War Chest"
metadescription: "Dankrad Feist argues Ethereum is losing because no organization is economically tied to ETH and willing to fight for it. A look at the proposal."
category: blog
featured-image: /images/blog/ethereum-aligned-war-chest-dankrad-ogp.png
intro: "Dankrad Feist argues Ethereum is losing because no organization is economically tied to ETH and willing to fight for it. A look at his proposal, the staking-revenue funding mechanic, and the case against."
author: sawinyh
tags: ["Analysis", "Governance"]
---

On May 21, 2026, Dankrad Feist posted a blunt diagnosis of [Ethereum](/ethereum)'s coordination problem. The argument: Ethereum is losing ground because no organization is both economically aligned with ETH's success and accountable for delivering it. The Ethereum Foundation funds research and writes grants, but it has no stake in ETH's price or usage. It behaves, in his framing, like a neutral grant-maker rather than a fighter. His fix is structural — the community should build, or evolve into, an organization that is economically tied to ETH and held accountable to it, seeded with a war chest of at least $1 billion.

Dankrad is not a fringe voice on this. He is one of Ethereum's better-known protocol researchers, associated with Danksharding and the data-availability scaling work, and he spent years full-time at the Foundation before [moving to a part-time advisor role in October 2025](/ethereum-foundation-departures-mandate) and joining Tempo, the Stripe and Paradigm-backed L1, as an L1 advisor. That biography matters here. The critique comes from inside the tent, from someone who has watched the Foundation's coordination machinery up close and concluded it is structurally unsuited to the job he thinks Ethereum now needs done.

This post is point-in-time as of May 21, 2026. The proposal is a tweet, not a published spec or an EIP, and the figures attached to it are Dankrad's own framing. The reply thread is summarized here as it was circulating, not audited line by line. Treat what follows as an analysis of an idea in its earliest, most contested form.

## The diagnosis: alignment without accountability

The Foundation's position is the starting point. By April 2026 its Arkham-tracked portfolio sat around $270 million across 14 addresses (ETH alongside the stablecoins it holds for operations). It completed a 70,000-ETH staking target early that month, and it has spent the past year converting ETH to stablecoins to fund operations. Those conversions are routine treasury management, framed that way in the EF's [own published policy](https://blog.ethereum.org/2025/06/04/ef-treasury-policy). But routine is the point. The EF is run as a non-profit steward, not as an entity whose mandate is to make ETH win.

The spending side has hard numbers behind it. The EF's most recent [published report](https://ethereum.foundation/report-2024.pdf) put 2023 expenditure at $134.9 million. The mid-2025 treasury policy then capped annual spending at 15% of reserves and committed to grinding that down toward a 5% long-run benchmark over five years, alongside a stated plan to narrow the Foundation's responsibilities. That is the part Dankrad's argument leans on hardest. The EF's own roadmap is to do less over time, on the assumption that the rest of the ecosystem absorbs whatever it sheds. The proposal is a bet that nothing in the current structure is built to absorb it.

Dankrad's claim is that the EF holds a vanishingly small slice of ETH, well under 0.1% of supply, and receives no direct flow of staking rewards or transaction fees. Its new staking program produces some yield, but at 70,000 ETH that is modest treasury management, not a revenue flywheel. The Foundation funds the protocol; it does not capture the protocol's upside. When ETH appreciates, the EF's runway gets longer, and that is roughly the extent of the feedback loop.

Compare that to how value actually accrues around Ethereum. L2 teams capture sequencer revenue and token upside. Venture funds capture equity. Validators capture issuance. The Foundation, the entity most associated with steering the protocol, captures the least. Dankrad's argument is that this is not a quirk — it is the reason core execution feels under-resourced relative to the size of the ecosystem it anchors.

Ethereum has always treated this as a feature. Public-goods funding is supposed to be unaligned; that is what makes it credibly neutral. The bet was that credible neutrality wins on a long enough timeline, and that no "general" is needed because the protocol coordinates itself. Dankrad is questioning whether that bet still holds in a market where competitors move faster precisely because their foundations and ecosystem orgs are willing to act like companies.

One caveat belongs up front. "Ethereum is losing" is Dankrad's read, not a settled fact. ETH still anchors the deepest on-chain liquidity and the settlement layer the most institutions actually trust, and usage has not collapsed. The under-execution case rests on a slower upgrade cadence and roadmap items pushed back fork after fork, not on users leaving. Whether that adds up to "losing" depends on which scoreboard you read: price and developer mindshare point one way, settlement volume and institutional adoption point another. The proposal is best judged as a response to a real but contested diagnosis.

## What he is actually proposing

The proposal is a minimum viable spec, sketched in a few lines. Four pieces:

1. **A credible war chest.** At least $1 billion to start. Dankrad calls that "very reasonable" for an ecosystem he pegs at roughly $255 billion in market cap. The ratio is the argument: a billion dollars is under half a percent of the network's value, and an ecosystem this large should be able to fund a serious execution arm without straining.
2. **A leader who wants to fight.** Competent and aggressive, in his words: someone whose job is to push, not to convene.
3. **Accountability to ETH itself.** A board whose members are incentivized for ETH's appreciation, plus a charter that enforces the alignment so it cannot quietly drift.
4. **Permanent, scalable funding.** A meaningful slice of staking revenue routed to the organization on an ongoing basis, with a governance process that can adjust the percentage over time.

The fourth point is the one that does the heavy lifting, and it is the one that turns this from a fundraising idea into a protocol-economics question. A one-time $1 billion raise is achievable today through philanthropy or a token sale. A permanent claim on staking revenue is something else entirely.

## What "fighting" would actually look like

The word "fighter" invites a marketing reading, and marketing is the least interesting version of the idea. The more substantive interpretation is an organization that owns execution across several fronts the current structure handles diffusely or not at all:

- **Shipping L1 improvements aggressively.** Funding and pushing gas-limit increases, execution-layer performance work, and state expiry on a cadence set by a roadmap owner rather than by rough consensus across client teams.
- **High-value business development.** Going after real-world assets, institutional DeFi, and payments directly, where Ethereum's credible neutrality is a genuine moat and where no one currently has the mandate to sell it.
- **Coordinating go-to-market across L2s.** The L2 ecosystem currently competes for the same users with no shared distribution strategy. An aligned org could impose coherence.
- **Regulatory defense at scale.** Lobbying and policy work funded as a line item, not as a volunteer effort.
- **Owning roadmap prioritization.** Dankrad concedes roadmap direction has improved recently. The structural complaint is that improvement still depends on the right people informally agreeing, not on an accountable owner.

The tension is obvious and Ethereum's own community surfaced it immediately. A powerful, well-funded org with a roadmap mandate is a capture target, a politics generator, and a step toward the "corporate chain" feel that Ethereum has spent a decade defining itself against. One reply to the original post framed it exactly that way. The counter is that the alternative, pure bottom-up coordination, has visibly slowed against faster-moving ecosystems, and that slowness is itself a risk to the thing the decentralization is meant to protect.

## The funding mechanic is the hard part

Routing staking revenue to an organization is the most novel and the most contentious element, because it touches the part of Ethereum that has historically been treated as untouchable monetary policy.

Ethereum issues new ETH to validators every epoch. With the staking ratio in the low-30s percent of supply and consensus-layer yield around 3% before MEV, annual issuance runs on the order of one to one-and-a-half million ETH, almost all of it flowing straight to validators. There is no protocol-level treasury; nothing skims that flow.

Before the question of how, it is worth being precise about how much, because the war-chest framing quietly conflates two different things. A tax on issuance is an annual flow. The $1 billion is a one-time stock. The tax never produces the stock in a single year. Taxing a million-plus ETH of yearly issuance raises, very roughly:

| Tax rate on issuance | ETH per year | Annual value, ETH at $2,000–$4,000 (illustrative) |
|---|---|---|
| 5% | ~57,000 | ~$115M–$230M |
| 10% | ~115,000 | ~$230M–$460M |
| 20% | ~230,000 | ~$460M–$920M |

Even an aggressive 20% skim almost never clears $1 billion in a single year. As an annual operating budget that is more than enough; it dwarfs the EF's ~$135 million of annual spending. As a one-time war chest it does not deliver. The $1 billion would have to be raised separately (a token sale, philanthropy, a BitMine-style seed), with the tax covering ongoing costs, or borrowed against the future stream. The $1 billion and the tax are two mechanisms, not one.

![Annual revenue from a staking-issuance tax, by tax rate and ETH price](/images/blog/ethereum-aligned-war-chest-dankrad-tax-revenue.png)

Read the other way, a permanent tax is worth far more than $1 billion. The present value of a perpetual stream is roughly its annual amount divided by a discount rate; at a 10% discount rate a 10% issuance tax capitalizes into the multiple billions. Run the logic backwards and the number gets small: to be worth $1 billion as an endowment, a permanent skim only needs to throw off on the order of $100 million a year, which is closer to a 2–4% tax on issuance than the 10–20% floated in discussion. The size of the tax was never the hard part.

![Capitalized value of a permanent issuance tax versus the $1B endowment target](/images/blog/ethereum-aligned-war-chest-dankrad-capitalized-value.png)

The hard part is everything around it. Skimming issuance is, mechanically, a pay cut to every validator it touches, at a time when the [staking issuance debate](/cut-ethereum-staking-issuance-debate) shows yields are already politically raw. There are three rough paths to impose it, none easy:

- **A protocol-level change.** An EIP plus a hard fork that mints a fixed share of issuance to a treasury address. Clean and durable, and the heaviest political lift Ethereum could attempt.
- **A governance vote**, if an on-chain mechanism existed to hold one. It does not, today.
- **A voluntary staking-pool tax.** Lido, Rocket Pool, and the exchanges agreeing to route a slice of rewards. This faces adverse selection: a taxed pool pays worse net yield than an untaxed one, so it only holds if the dominant pools move together.

A softer variant is to change the base. Taxing MEV and execution-layer tips rather than base issuance sidesteps the issuance curve the community is already fighting over, and MEV reads more like extracted surplus than a promised reward. The base is smaller and more volatile, but it avoids the "you are cutting my staking reward" framing.

The adjustable-percentage idea is the genuinely clever part. If the community can move the number up or down through a governance process, the organization stays accountable: underperform and its funding gets cut. That solves the "who watches the watchmen" problem in principle. It does not solve the bootstrapping problem of who runs that governance process on day one, and who has the legitimacy to route protocol issuance to an entity that does not yet exist. That chicken-and-egg is unresolved in the proposal as stated.

There is a sharper version of that problem. A protocol-level skim has to clear Ethereum's real governance path: an EIP, discussion on Ethereum Magicians, the All Core Devs calls, and sign-off from the client teams that write the code. That path has no formal vote. It runs on rough consensus, in a room where the EF and EF-funded researchers are heavily represented. The proposal effectively asks that process to bless an EIP whose founding premise is that the EF has under-executed and a rival should be funded to outdo it. The people best placed to wave it through are the ones it implicitly indicts. And client teams do not implement contested monetary changes that risk a chain split; rough consensus, with its strong status-quo bias, makes such a change easy to block. The body with the standing to approve the skim is dominated by the institution the proposal is built to route around.

The whole thing also lands in the middle of an argument Ethereum is already having. The community spent this spring debating whether to cut staking issuance outright to defend ETH's moneyness. Dankrad's proposal points elsewhere: leave issuance where it is, but skim a piece of it. The two interact directly. If a future fork halves issuance, the tax base halves with it, so a protocol historically reluctant to make any explicit monetary-policy decision now has two of them on the table, and they cannot be sized independently.

## The BitMine question

Replies to the original post kept surfacing the same name: [BitMine](/bitmine-vs-strategy-dat-flywheels). The public company has become a large ETH treasury holder, close to 5 million ETH (around 4% of supply) as of its late-April 2026 disclosure, and unlike a passive ETF it actively stakes through its own MAVAN validator network and builds infrastructure. To some repliers, that is already most of what Dankrad is describing: a well-capitalized entity economically tied to ETH.

Dankrad's own response was pragmatic. BitMine is more treasury than fighting organization today. Its mandate is to grow ETH-per-share, not to ship L1 improvements or coordinate go-to-market. But it could plausibly seed or catalyze the kind of entity he has in mind, and its Wall Street ties give it credibility that a from-scratch crypto org would lack.

That points toward a hybrid: a public-company treasury for capital and Wall Street credibility, a protocol revenue share for permanent funding, and an Ethereum-native governance layer for accountability. The pieces exist separately today. Nobody has tried to weld them into one entity, and the politics of doing so is the same problem the rest of this post keeps running into.

## The case against

The objections are not hard to find, and several of them are strong.

**It collides with the EF's own stated philosophy.** In March 2026 the Foundation published its [Mandate](/ethereum-foundation-departures-mandate), a document that explicitly warns against trading Ethereum's principles for financialization and institutional wins. Dankrad's proposal is, almost by construction, a financialization of Ethereum's coordination layer — an organization defined by its tie to ETH's price. The two visions are not obviously reconcilable. An aligned-org advocate would say the Mandate describes exactly the posture that is losing; a Mandate defender would say the proposal describes exactly the capture risk the document was written to prevent.

**Money may not be the binding constraint.** The proposal assumes Ethereum under-executes because no one is funded and incentivized to push hard enough. But L1 changes do not ship because someone wants them badly. They ship when the client teams (Geth, Nethermind, Reth, and the consensus clients) implement them and the rough-consensus process signs off. A structurally invasive consensus-layer change intersects with every client team's roadmap at once. A $1 billion war chest can fund engineering, hire business development, and pay for lobbying, but it cannot make multi-client coordination move faster. If the binding constraint is engineering coordination rather than money, the war chest is treating a symptom.

**A charter does not eliminate capture.** Incentivizing a board for ETH appreciation aligns it with price, which is not the same as aligning it with the protocol's long-run health. A price-linked board has a structural reason to favor changes that pump near-term over changes that harden security or preserve neutrality at the cost of growth. This is not a new worry in Ethereum. Vitalik Buterin's 2021 essay [Moving beyond coin voting governance](https://vitalik.eth.limo/general/2021/08/16/voting3.html) argues at length that tying governance to token wealth misfires, because the interests of large holders and the interests of the protocol come apart. A board paid to maximize ETH's price is a softer version of the same design, and it inherits the same gap between what the holder wants and what the network needs. It is also worth asking which precedent actually fits. The Linux Foundation, the usual reference point for a neutral coordinating body, is funded by corporate members and has no tie to any asset price. It coordinates a sprawling open-source ecosystem without the economic-alignment mechanism Dankrad treats as essential. That suggests the price linkage is the controversial half of the proposal, not the idea of a coordinating org itself.

**Coordination failure cuts both ways.** "The community should build this" assumes a community coherent enough to agree. The same fragmentation that makes Ethereum feel slow is what would make consensus on diverting staking revenue extraordinarily hard to reach. Getting agreement on this could be as difficult as any contentious hard fork — which is to say, it might simply not happen.

**The diagnosis may outrun the cure.** It is possible to accept that pure decentralization under-executes, and still doubt that a $1 billion org with a fighting leader is the answer rather than a new and larger failure mode.

It is telling that the replies ranged from "this is what BitMine is for" to "no thanks, sounds like VC centralization" to "we need this for Bitcoin too." The proposal does not have a constituency yet. It has a diagnosis that resonates and a cure that nobody has signed up for.

## Bottom line

Strip away the war-chest framing and Dankrad is making a narrow, serious claim: decentralized protocols still need a coherent, incentivized execution layer, and protocol decentralization alone does not produce one. Bitcoin has run for over a decade without such a layer, held together by culture and miner incentives. Solana moves faster in part because its foundation and ecosystem orgs behave more like companies. Ethereum's bet has been that credible neutrality wins on a long horizon. The proposal asks whether that is still enough without an aligned general and the money to back one.

The honest read splits in two. On the diagnosis, Dankrad is largely right. Ethereum has no body that is both resourced to execute and accountable for ETH's outcome, and the gap is real enough that something like his aligned organization is genuinely needed. On whether it gets built, the read is bleaker. Every mechanism the proposal depends on runs into a structural wall: a permanent staking skim needs a contentious hard fork, the EIP to authorize it has to clear a process the incumbent gatekeeps, and a price-linked board collides with both the EF Mandate and a decade of Ethereum thinking on wealth-weighted governance. None of those walls has an obvious way over it. Dankrad himself concedes the idea feels politically impossible today, and he is probably right that only a visible crisis or a clear loss of market share would forge the consensus he predicts. Absent that, the most likely outcome is that this does not get built: not soon, and quite possibly not at all.

Until then the value of the idea is as a diagnostic. The next time an Ethereum upgrade slips, or a competitor ships something Ethereum should have shipped first, the question to ask is not whose fault it was. It is whether anyone in the ecosystem had both the mandate and the incentive to make sure it did not happen — and, on Dankrad's reading, the answer is still no.
