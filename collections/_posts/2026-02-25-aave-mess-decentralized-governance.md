---
git-date:
layout: [blog]
title: "The Aave Mess: Who Actually Owns a Decentralized Protocol?"
permalink: aave-mess-decentralized-governance
h1title: "The Aave Mess: Who Actually Owns a Decentralized Protocol?"
pagetitle: "The Aave Mess: Who Actually Owns a Decentralized Protocol?"
metadescription: "Aave's governance crisis—swap fees, brand transfer, BGD's exit—exposes deeper questions about who really controls a decentralized protocol and whether DeFi governance is broken."
category: blog
featured-image: /images/blog/aave2025drama.png
intro: "Aave had a rough winter. What started as a fight over swap fees turned into a full-blown war between the people who built the protocol and the people who theoretically own it."
author: sawinyh
tags: ["DeFi Guides", "Governance", "DAO"]
---

[Aave](https://aave.com/) had a rough winter.

What started as a fight over swap fees—the kind of thing normal protocols would handle in a [forum thread](https://governance.aave.com/)—turned into something uglier. By February 2026, you had the founder voting against brand transfer proposals, key developers announcing their exit, and the [token](https://www.coingecko.com/en/coins/aave) down 40%. A full-blown war between the people who built the protocol and the people who theoretically own it.

I've read the two major write-ups on this saga. They both get parts of it right. They also both avoid saying what seems obvious: DeFi governance might be broken in ways nobody wants to admit.

## The Spark

December 2025. [Aave Labs](https://aave.com/) swaps out [ParaSwap](https://www.paraswap.io/) for [CoW Swap](https://cow.fi/) on their frontend. Routine maintenance, you'd think. Except the fees that used to go to the DAO treasury now went to Labs. Nobody asked. Nobody even mentioned it until delegates noticed.

[Marc Zeller](https://x.com/Marczeller) from [ACI](https://www.aavechan.com/) (Aave Chan Initiative) called it "unacceptable." Others called it theft. AAVE dropped 20%.

[Stani Kulechov](https://x.com/StaniKulechov) had a different read: the frontend isn't the protocol. Labs built the website, Labs maintains it, so Labs gets the revenue. The smart contracts and liquidity pools—that's the DAO's. The interface? Ours.

Reasonable legal distinction, or creative reinterpretation of "decentralization"? I genuinely don't know. But the implementation was awful. You can't take money without asking and then claim you support decentralized governance. Pick one.

## It Gets Worse

[BGD Labs](https://bgdlabs.com/) proposed [transferring brand assets](https://governance.aave.com/t/arfc-aave-brand-ips-transfer-to-aave-dao/20225) to DAO control. The aave.com domain. The Twitter account. Trademarks. If token holders own the protocol, they should own the brand.

Labs pushed the vote through over Christmas, when everyone was offline. It failed. Kulechov [voted against it](https://vote.onaave.com/).

I keep coming back to that timing. Maybe innocent. Maybe not. But if you look like you're gaming the process, you probably are. Governance runs on trust, and this looked bad.

## The Package Deal

February 2026: Labs drops the "[Aave Will Win Framework](https://governance.aave.com/t/aave-will-win-framework/21011)."

$42.5 million in stablecoins. 75,000 AAVE tokens. Call it $51 million total. In exchange, all frontend revenue goes to the DAO. V4 gets ratified as the future architecture. V3 gets deprecated eventually.

Sounds like a compromise until you notice the bundling. Like the revenue routing but hate the price tag? Too bad. Support V3 but want some frontend money? Can't have it. Vote yes to everything or no to everything.

This is how you manufacture consent. Tie things people want to things they don't. Then accuse anyone who votes no of opposing progress.

## The Sources Are Biased

The first document tries too hard to be balanced. Delegates are "financially aligned." Labs is "strategically aligned." This sounds even-handed until you realize financial alignment is measurable and strategic alignment is vibes.

Labs says V4 will be great. Maybe. "We're building the future" is not a falsifiable claim. It's a request for trust. And trust is what Labs burned with the fee redirect.

The second document leans toward the DAO position. It quotes [ACI's audit](https://governance.aave.com/t/aci-aave-labs-financial-audit-a-comprehensive-examination-of-resource-allocation-and-strategic-alignment/20964) at length—Labs has received \$86 million, produced questionable ROI, runs unprofitable products—without mentioning that ACI is a service provider whose business model depends on decentralized development. When ACI releases an audit right before a funding vote, that's competitive positioning, not neutral analysis.

Neither document addresses who actually holds AAVE tokens. No distribution data. No breakdown of voting patterns. "Token holder interests" gets invoked constantly, but nobody says whose interests.

## What Everyone Actually Wants

Aave Labs needs money. The VC market dried up. Self-funding from equity rounds isn't sustainable. The \$51 million isn't ambition—it's survival.

Labs also wants control. V4 ratification isn't just technical. It determines whose expertise stays relevant. If the future is V4, and Labs owns V4, then Labs is indispensable. BGD, whose expertise is V3, becomes obsolete.

Delegates want accountability. Fair. They also want power. Also fair. Some of them want contracts. Less fair to pretend otherwise.

When service providers lobby for decentralized development models that benefit their businesses, the idealism gets tangled with self-interest. That's fine—self-interest is normal—but don't dress it up as principle.

BGD Labs is [leaving in April 2026](https://bgdlabs.com/blog/bgd-is-leaving-aave). They cite the V4 pivot, governance tensions, adversarial behavior toward V3. The market believed them—AAVE dropped. Zeller called it the biggest talent loss in Aave history.

Is BGD's exit principled or strategic? Walking away from a captured process is noble. Creating leverage by threatening to leave is cynical. Probably both. That's uncomfortable but realistic.

## Who Gets the Swap Fees?

Labs says the frontend creates value independently. Delegates say the frontend only matters because Aave has billions in liquidity.

Both arguments have holes.

The frontend isn't nothing. Someone builds it. Someone maintains it. But aave.com doesn't have users because the interface is great. It has users because the protocol works. Strip away the liquidity, the website is worthless.

The real issue is simpler: Labs made the switch without asking. Even if the ownership claim holds, the unilateral action killed trust. You can't claim to support decentralization while acting like you don't need permission.

## The \$86 Million Question

[ACI's audit says](https://governance.aave.com/t/aave-labs-86-million-23-of-the-token-supply-and-this-is-their-track-record/24159) Labs has received \$86 million over the years. Labs says they built the protocol with 60% market share in DeFi lending.

The audit aggregates funding across different eras—2017 ICO, VC rounds, DAO payments, disputed fees—and presents one big number. This hides whether spending made sense at the time. Judging 2017 by 2026 standards isn't fair.

But the [Horizon](https://aave.com/horizon) RWA numbers are damning. \$216,000 revenue against millions in incentives. If that's typical Labs execution, why would more money help?

The harder problem: delegates can't evaluate technical roadmaps. They can measure past ROI but can't assess whether V4 is worth \$51 million. Labs has information advantages that make negotiation asymmetric.

## V4 vs. V3

Labs wants V4, plans to phase out V3. BGD says V3 is the "crown jewel" generating actual revenue. Betting on unproven architecture while neglecting the working system seems risky.

I don't know which is better. Neither do delegates. This is a technical question decided by politics. That seems bad.

BGD's exit makes it worse. The people best positioned to evaluate V3 just left. Maybe Labs wanted that—eliminate the competition, claim nobody can maintain the old system. Maybe BGD overstates their importance. Hard to tell.

## So Who's Right?

Neither side, fully.

The delegate position is more aligned with short-term token holder economics. Treasury preservation is measurable. Revenue routing is concrete. Funding discipline makes sense.

The Labs position might be better for long-term protocol success—if V4 works, if you trust Labs' execution, if centralized development beats governance coordination. Lot of ifs.

What tips me toward delegates: the trust problem. Labs took fees without asking. Labs timed votes to suppress participation. Labs bundles proposals to force consent. Even if the strategy is right, the behavior suggests they see the DAO as an obstacle, not a principal.

Trust is expensive to rebuild.

## What Both Accounts Miss

**Legal framework.** Are DAO votes binding? What jurisdiction applies? What enforcement exists? Without answers, "DAO authority" is wishful thinking.

**Token distribution.** Who holds AAVE? How concentrated? Who votes? "Token holder interests" is empty without data.

**Competitive context.** How do [Compound](https://compound.finance/) and [MakerDAO](https://makerdao.com/) handle this? Has anyone successfully moved from founder-led to DAO-led development?

**Technical assessment.** Is V4 actually better? What specific capabilities justify \$51 million? The debate is pure politics because nobody's evaluating the technology.

## The Real Problem

DeFi built sophisticated financial infrastructure and primitive governance infrastructure. Aave holds [billions in TVL](https://defillama.com/protocol/aave) and can't agree on who owns the swap fees.

The hybrid model—DAO votes on paper, founders run things in practice—worked during growth. It fails when there's money to divide. The fiction of decentralization collides with concentrated control.

Neither side offers clean answers. Delegates can't coordinate development. Labs can't be trusted to self-govern. The protocol needs both and can't reconcile them.

Maybe Aave figures this out. Maybe it forks. Maybe it fades. The outcome probably depends on whether anyone prioritizes institutional design over winning the current fight.
