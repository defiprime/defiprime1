---
git-date:
layout: [blog]
title: "EIP-8363: Ethereum's Plan to Burn Staking Rewards to Zero, and the Backlash"
permalink: ethereum-tapered-issuance-burn-eip-8363
h1title: "EIP-8363: Ethereum's Tapered Issuance Burn"
pagetitle: "EIP-8363: Ethereum's Plan to Burn Staking Rewards to Zero, and the Backlash"
metadescription: "EIP-8363 would burn validator rewards until Ethereum's net consensus yield hits zero at half the supply staked. The mechanism, the opposition, and what core devs did with it."
category: blog
featured-image: /images/blog/ethereum-tapered-issuance-burn-eip-8363-ogp.png
intro: "A draft EIP would burn a rising share of validator rewards until net consensus yield reaches zero at half the ETH supply staked. It landed two days before a fork deadline, drew organised opposition from Aave and ether.fi, and left the August 6 core devs call with a recommendation that its author consider withdrawing it."
author: sawinyh
tags: ["Analysis", "Yield"]
---

On August 4, 2026, a draft Ethereum Improvement Proposal appeared on GitHub proposing to burn a rising share of every validator's consensus rewards, scaling the burn up until net issuance yield hits zero once roughly half the ETH supply is staked. Two days later, the window closed for putting non-headliner EIPs in front of core devs for Hegotá, the network upgrade due to follow Glamsterdam. In between, the founders of two of the largest businesses built on staking yield mounted a public campaign against it.

Getting onto that list is called PFI, proposed for inclusion. It is the weakest of the stages an EIP passes through, and means only that an idea has been formally tabled for discussion, not that anyone has agreed to ship it. This one did not get there.

The proposal is [EIP-8363, Tapered Issuance Burn](https://github.com/ethereum/EIPs/pull/12081). Its authors are pintail, Jérôme de Tychey, dapplion, pa7x1, Ladislaus von Daniels, and Justin Drake. Several outlets filed it as a Justin Drake or Ethereum Foundation proposal; he is one of six authors, listed last, and the pull request comes from pintail. It is a Draft, it has not been accepted into any upgrade, and by the end of the [August 6 All Core Devs consensus call](https://ethereum-magicians.org/t/all-core-devs-consensus-acdc-184-august-6-2026/29209), the biweekly meeting where consensus-layer changes are argued out, the recorded next step for its presenting author was to consider withdrawing it from Hegotá consideration.

This piece reflects what was verifiable on the morning of August 7, 2026. The proposal text, the constants, the GitHub state, and the on-chain staking figures are checked directly and cited so you can re-check them. What is not settled is where the EIP goes from here, and any read on that is a guess.

## What the Proposal Actually Does

[Ethereum's](/ethereum) consensus layer pays validators from newly issued ETH. The amount issued each epoch is 64 × √D gwei, where D is the total active balance in gwei. Because issuance scales with the square root of the stake but is divided across all of it, yield falls as roughly 1/√f in the staking ratio f. It falls, but it never stops. At any staking ratio you care to name, the curve still leaves a positive yield of around 1.5%, and so an incentive to stake more.

EIP-8363 leaves that calculation untouched and adds a deduction on top. After rewards and penalties are applied each epoch, every validator is charged a fraction of the idealised reward for each duty it was assigned (attestation, block proposal, sync committee), and that ETH is destroyed rather than redirected anywhere. The burn fraction is:

```
b = (D / SATURATION_BALANCE) ^ 1.5
```

`SATURATION_BALANCE` is set to 60,250,000 ETH. Against a supply of about 121.93 million ETH, that is 49.4%, near enough to half. At that point b reaches 1, the deduction exactly cancels a performing validator's issuance, and net consensus yield is zero.

Two things about the design are easy to miss and matter a lot.

First, the deduction is sized on what perfect performance *by that validator* would have earned, not on what it actually earned. A validator that attests correctly nets exactly (1−b) times its reward, and the gap between doing a duty and skipping it stays exactly what it is today. That is deliberate: shrinking the reward curve itself would weaken every per-duty incentive while leaving MEV untouched, and the authors argue consensus rewards and penalties have to stay large relative to the external payoff from block-timing games and reorgs, or chain stability suffers.

There is a cost buried in that choice. Penalties stay at full magnitude while net earnings fall to (1−b) of the reward, so the time needed to earn back an outage grows by a factor of (1 + b/0.74)/(1−b). At today's staking ratio the EIP puts that at roughly 3.8 times what it is now. The ETH cost of downtime is unchanged; the number of days of net income it eats is not.

Second, the burned ETH goes nowhere. The rationale section is explicit that redirecting it, to other validators, to a treasury, to public goods, would leave total issuance unchanged and create a new claimant whose share could be lobbied over. That is a pointed contrast with the [Validator Redirected Revenue idea floated in June 2026](https://www.coindesk.com/tech/2026/06/22/ethereum-validators-asked-to-fund-projects-with-up-to-10-of-staking-rewards-under-new-proposal), which would have let validators signal 0 to 10% of rewards toward an ecosystem fund.

The 1.5 exponent looks arbitrary and isn't. The authors want the *absolute* deduction to grow linearly in the staking ratio so that net yield tapers to zero in a straight line. Since it is expressed as a fraction of a reward that itself falls as f^(−1/2), it picks up an extra half power. One consequence: total annual issuance under the tapered curve no longer rises with the staking ratio. It peaks at 2^(−7/3), about 19.8% of supply staked, and declines from there.

## The Numbers at Today's Staking Level

Ethereum currently has about 41.78 million ETH staked out of a 121.93 million ETH supply, or 34.3%, per [ultrasound.money](https://ultrasound.money/) on August 7. Running the EIP's own formulas against that base:

| ETH staked | % of supply | Burn fraction | Gross CL yield | Net CL yield |
|---|---|---|---|---|
| 41.78M (today) | 34.3% | 57.7% | 2.57% | 1.09% |
| 45M | 36.9% | 64.5% | 2.48% | 0.88% |
| 50M | 41.0% | 75.6% | 2.35% | 0.57% |
| 55M | 45.1% | 87.2% | 2.24% | 0.29% |
| 60.25M | 49.4% | 100% | 2.14% | 0.00% |

Execution-layer income (priority fees and MEV) is not touched, and this is the number that decides how much the burn actually bites. The EIP puts execution-layer rewards at no more than 78,300 ETH a year, roughly 0.20% on today's staked base, derived from about 72,600 ETH of MEV-Boost relay payments across 2.42 million blocks in the year to July 31, 2026. Live figures are lower still: ultrasound.money currently shows issuance at 2.575% APR against 0.052% from MEV and 0.049% from tips, which puts consensus issuance at roughly 96% of a validator's total return.

So the burn is not a haircut on one income stream among several. At today's staking ratio it would take all-in validator income from about 2.68% to about 1.19%, a cut of some 55%.

Arriving at once, that is enough to force stake out on activation, which the authors concede. They defuse it by temporarily doubling `BASE_REWARD_FACTOR` from 64 to 128 at activation and decaying it back over 123,300 epochs, about 18 months, in 65 integer steps of roughly 8.6 days each. Doubling lifts the tapered net-yield curve so it crosses today's curve at about 31% staked, close to where the network actually sits. Stakers start near what they earn now and slide down from there. Add the six months or more between a fork being scheduled and going live, and the authors argue participants get on the order of two years.

What the transition does *not* defer is the shape. From the first epoch after activation, the burn still hits 100% at 60.25M ETH whatever the base reward factor is. The off-switch is live on day one; only the level moves.

## Why Now, According to the Authors

The case for urgency rests on the entry queue. De Tychey [argued on the discussion thread](https://ethereum-magicians.org/t/eip-8363-tapered-issuance-burn/29263) that validator entry has been running at essentially the protocol's maximum churn, the fixed per-epoch cap on how much stake can activate, for a while, and that if entry stays saturated with few exits, more than 70 million ETH will be staked by January 1, 2028, north of 55% of supply.

His framing is that "do nothing" is not a neutral baseline. Acting now means the market settles below 50% on its own; acting after an overshoot means forcing stake back out. He also made the political argument plainly: every month of delay adds to the constituency earning fees on the status quo, and the previous issuance debates already showed how effectively that pressure stalls a proposal.

That is the strongest version of the case, and it doubles as an admission. The authors know the affected industry will fight, and they moved before it got bigger. Their opponents read the same fact as a reason the process was rushed.

## The Number Nobody Could Agree On

For its first two days the proposal was reported as EIP-8361 and EIP-8363 more or less interchangeably, which is why both numbers still show up in coverage. The explanation is mundane and slightly embarrassing. pintail self-assigned 8361 to get the pull request through CI, which is not how numbers are handed out; editors pointed out that only they and their associates allocate them, found 8361 already taken, and issued 8363 instead.

pintail [acknowledged it and asked](https://github.com/ethereum/EIPs/pull/12081) for the contributor guidance to explain the process, which it doesn't. Trivial in itself. It became a stick to beat the proposal with anyway, and de Tychey's own inclusion request still carries the wrong number in its title.

## The Opposition

Two founders drove most of the public reaction, and both have a business on the other side of it.

Stani Kulechov of [Aave](/aave) opened on August 4 with the substantive objection: unpredictable staking yield is an adoption cost, and a yield trending toward zero breaks ETH borrowing.

{% include tweet.html
  name="Stani Kulechov"
  handle="StaniKulechov"
  date="August 4, 2026"
  link="https://x.com/StaniKulechov/status/2084667208668467574"
  body="For DeFi, with moving to 0% reward, this essentially makes ETH borrowing strategies mostly unviable and killing ETH borrowing and yield use-cases for ETH (only reason to borrow ETH ironically would be to short it). The only way to get ETH yield would be to stake, lock into a time period (instead of instant withdrawals in DeFi) and also have hopium ETH doesn't reach 50% staked of supply. ... Ethereum should not be punished for its growth."
%}

That is not an abstract worry for him. The ETH looping trade on [lending markets](/decentralized-lending), borrow ETH, stake it or buy an LST, post that as collateral, borrow again, only works while the staking yield clears the borrow rate. Kulechov's point is that a yield which falls as the staking ratio rises does not just compress that spread, it makes it unforecastable, and the borrow side of his own book is what thins out first.

Kulechov also filed a detailed technical objection on Ethereum Magicians under the handle EthWarrior, which the forum profile confirms is him. It reproduces the proposal's own arithmetic and then pushes on who is left standing at the bottom of the curve:

> A zero-yield regime accelerates the capture it means to deter. It filters out everyone who stakes for economic return and leaves the field to entities that stake for structural, regulatory, or product reasons, which describes exactly the KYC'd, jurisdiction-bound, coercible operators the proposal fears.

His model puts a 32 ETH home validator with $500 a year in hardware and electricity and a 30% marginal tax rate on gross credited rewards, and finds the tax wedge does the damage well before the yield reaches zero. It is the sharpest objection on the thread, because it accepts the authors' goal and argues the mechanism works against it.

Mike Silagadze of ether.fi went at the process.

{% include tweet.html
  name="Mike Silagadze"
  handle="MikeSilagadze"
  date="August 4, 2026"
  link="https://x.com/MikeSilagadze/status/2084703078909907000"
  body="This is so disappointing on every level. EIP released with 48 hours notice for comments. Realistically 4 months before it goes live. For a major network economics change with far reaching implications for all of DeFi. ... This reinforces the Ethereum critics' position that the network is run by a small group of insiders with no regard for the actual users and builders on the chain. I can say that neither I nor any builder I know was asked for feedback on this before it went live. Any nation state or large institution looking at this will justifiably have a dramatic loss of confidence in the governance and stability of Ethereum."
%}

On the 48-hour framing, one correction is worth making: the EIP's own front matter carries a `created` date of 2026-07-14, three weeks before it was published, and the underlying research (pa7x1's issuance work, Anders Elowsson's offsets analysis, the material indexed at issuance.wtf) goes back years. What was compressed was the public review window before the PFI deadline, not the thinking. That is still a real complaint, and it is the one that landed hardest with core devs.

Silagadze also disputed the monetary premise directly, calling the claim that liquid staking tokens displace ETH as money "a cash-accounting level of understanding of the economy, as if only M1 counts as real money," and adding that the case for *increasing* ETH issuance is stronger than the case for cutting it.

By August 6 Kulechov was calling the proposal (using the discarded 8361 number, as most people still were) possibly "one of the most resisted Ethereum proposals ever, perhaps second only to ProgPoW," a reference to the mining-algorithm change that consumed Ethereum governance in 2019 and 2020 and was never shipped. He has been signing off with "Save ETH staking" ever since.

## The Blast Radius Priced In

Markets moved, though modestly and briefly. LDO fell from $0.3285 on August 4 to $0.2793 on August 5, a 15% drop, and was at $0.286 on August 7. ETHFI went $0.4028 to $0.3541 over the same two days, down 12%, and had recovered to $0.365. ETH itself barely registered it, sitting near $1,912 on August 7 (CoinGecko).

The scale of what sits on staking yield is easy to understate. Lido alone holds about $17.95 billion in TVL, over half of the $35.35 billion DefiLlama tracks across liquid staking on all chains, and the LST layer intermediates about a quarter of all staked ETH by Silagadze's count. Everything built on top of that (looping, LST collateral, the fixed-rate and yield-stripping markets that quote against [staking](/staking) yield as a reference rate) reprices if the reference rate becomes a function of the staking ratio rather than a floor.

This is the same fault line we covered when the [issuance-cut debate first broke into the open in April](/cut-ethereum-staking-issuance-debate), and it is the same one that runs under [DeFi's yield risk premium](/defi-yield-risk-premium): which property of ETH the protocol optimises for, and who eats the adjustment cost.

## The Vote That Proves Less Than It Looks

On August 5 the Ethereum Validators Association put EIP-8363 up for stake-weighted signalling on its hub. Numbers circulated fast. By 19:22 UTC on August 6 the association reported "a record $150 million dollars worth of ethereum:native" voted, with results at 99.92% no. By August 7, community posts were citing roughly 83,000 ETH voted and 99.77% against.

The association's own post breaks that $150 million down as ten no votes and two yes votes. Twelve entities in total. Stake-weighted signalling measures ETH rather than people, and 83,000 ETH is about 0.2% of the staked base. The direction is real and unsurprising: asking validators whether to cut validator income has a predictable answer. The magnitude is a rounding error dressed as a referendum, and every side of this argument should be careful about which of those two things they are citing.

On August 6, hours before the core devs call, ether.fi [stripped restaking out of weETH](https://www.coindesk.com/tech/2026/08/07/ethereum-staking-token-weeth-splits-from-restaking-as-rewards-debate-heats-up), making it a plain liquid staking token and moving restaking exposure to weETHs. Silagadze's comment on the change was "End of an era. Sad. I still think restaking will come back in one form or another, I think it was just a bit too early." Framed as a risk-separation product decision, it also lands as an unbundling of exactly the yield stack under debate.

## What Core Devs Actually Did

Most of the coverage of this proposal went out before the call and has not been updated since.

EIP-8363 was on the [ACDC #184 agenda](https://github.com/ethereum/pm/issues/2177) for 30 minutes on August 6, more than any other item in the Hegotá block. De Tychey presented it. Per the call's auto-generated summary posted to the Ethereum Magicians thread, participants raised the small-validator and centralisation concerns, Greg Koumoutsos argued it should be withdrawn for insufficient preparation time, and Oisin Kyne raised the effect on the Nakamoto coefficient. The recorded next steps for de Tychey were to "consider withdrawing the EIP 8363 (Tapered Issuance Burn) from consideration for Hegotá based on community feedback" and to answer every comment on the forum thread.

That summary is machine-generated and garbles several names, so treat the wording loosely; the recording and transcript are linked from the thread. The GitHub state is not ambiguous, though. The pull request collecting every EIP proposed for inclusion at ACDC 183 and 184 was updated after the call and lists nine additions, including Barnabé Monnot's Quick Slots and two BLS validator retirement EIPs. EIP-8363 is not among them. De Tychey's own PFI pull request is still open, unmerged, and still needs an author review.

It was presented, argued over, and left off the inclusion list, with a recommendation to its author to withdraw it. That is short of rejection, and PFI was never an inclusion decision anyway. But the proposal did not clear the first procedural bar it was aiming for, on the timetable its authors said mattered.

## What This Fight Is Really About

Strip out the founders and the vote counts and there are two claims that cannot both be the priority.

The authors' claim is that unbounded staking growth reads as success and behaves as a security problem. Past some level, more stake does not buy more security, it buys more concentration: an ever-larger share of the supply sits with custodians and ETF issuers rather than with its owners, which makes a fork against a dominant operator harder for the social layer to coordinate. Their sharpest version of this is the "too big to fail" case, where delegators stop pricing tail risk because they expect the biggest operator to be rescued, the discount makes it cheaper to stake with, and stake concentrates further. Dilution does the rest: it taxes anyone who does not stake, which pushes them to stake.

The opposing claim is that Ethereum's staking yield has quietly become the reference rate for on-chain finance, and you do not get to change a reference rate into a variable that moves with a participation ratio without repricing everything built on it. Institutions underwrite ETH on a forecastable cash flow. Lending markets quote against it. Solo stakers, who pay income tax on nominal yield and fixed costs regardless, are the least able to absorb the volatility.

Both sides are arguing about the same 2026 fact from opposite ends: ETH became a productive asset with a working credit market on top of it. To one camp that is the achievement to protect. To the other it is the mechanism eating the asset underneath.

What the last few days settled is narrower. A change of this size cannot be introduced two days before a deadline and expect a hearing on the merits, however long the underlying research has been running. The process objection swallowed the substance, and the substantive objections, Kulechov's zero-yield selection argument in particular, have not been resolved. If the taper comes back, it comes back with months of review, and the constituency defending the status quo will be larger than it was this week. Which is precisely what its authors were trying to get ahead of.
