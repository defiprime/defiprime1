---
git-date:
layout: [blog]
title: "Cutting Ethereum's Staking Issuance: Existential Threat to DeFi, or Fix for ETH's Original Sin?"
permalink: cut-ethereum-staking-issuance-debate
h1title: "The Ethereum Staking Issuance Debate"
pagetitle: "Cutting Ethereum's Staking Issuance: Existential Threat to DeFi, or Fix for ETH's Original Sin?"
metadescription: "Should Ethereum cut staking rewards to defend ETH's moneyness, or keep them to protect LST-fueled DeFi? A look at the curve, the camps, and what a hard fork could change."
category: blog
featured-image: /images/blog/cut-ethereum-staking-issuance-debate-ogp.png
intro: "Should Ethereum cut staking rewards to defend ETH's moneyness, or keep them to protect LST-fueled DeFi? A look at the curve, the camps, and what a hard fork could change."
author: sawinyh
tags: ["Analysis", "Yield"]
---

On April 28, 2026, Dima Gusakov, a tech lead at Lido's community staking team, posted a tweet that read like a four-line obituary for [Ethereum](/ethereum):

> If we cut Ethereum staking issuance, we will likely kill LSTs. Without LSTs, DeFi will shrink to the size of a penny. Without DeFi, Ethereum will lose its main value proposition. Without its value proposition, Ethereum will die.

It hit 55,000 views in a day, and Crypto Twitter has not stopped arguing about it since. The post was dramatic enough to cut through the noise, but the underlying debate is older and more technical than the framing suggests. It is also genuinely consequential. Ethereum's consensus-layer reward curve has not been touched since the Beacon Chain launched in 2020. The community is now openly asking whether that should change in a future hard fork.

This is, structurally, a fight about which property of Ethereum matters more: short-term DeFi composability anchored by liquid staking tokens, or long-term ETH moneyness anchored by scarcity. Both sides claim their answer is what keeps Ethereum alive over the next decade. The figures and quotes below are point-in-time as of late April 2026 and will move as upgrade discussions progress.

## What "Cutting Issuance" Actually Means

Ethereum's PoS reward curve was specified before the Merge with one explicit assumption: only 20–30% of the ETH supply would ever be staked. That target shaped the math. The protocol issues new ETH every epoch (~6.4 minutes) according to a formula whose key building block is the per-validator base reward:

```
base_reward = (effective_balance × BASE_REWARD_FACTOR)
              ÷ (BASE_REWARDS_PER_EPOCH × √(total_active_balance))
```

Three things matter in that expression. `effective_balance` is capped at 32 ETH per validator. `BASE_REWARDS_PER_EPOCH` is a fixed denominator constant in the spec. `BASE_REWARD_FACTOR` is the tunable scalar, set to 64 at genesis and never changed since. The square-root denominator is what makes the curve self-correcting: as more ETH stakes, the per-validator yield falls. Total annual issuance grows roughly with √s, while the yield each staker sees scales as 1/√s.

At very low staking ratios the curve pays out aggressively, which is what bootstrapped validator participation in the first place. At the 20–25% range the original designers were aiming for, nominal issuance yield sits around 4–5%. Past 30%, the yield has already compressed to roughly 3% before MEV and execution-layer tips. As of late April 2026 the staking ratio is in the low-30s percent of the ETH supply, which means the network is sitting beyond the equilibrium the curve was specified for, and the marginal economics for new validators keep getting tighter.

"Cutting issuance" is shorthand for changing this curve. There are two distinct versions of that change:

1. **Scalar adjustment.** Lower `BASE_REWARD_FACTOR` from 64 to something smaller (32 has been floated as a clean halving, 40–48 as a moderate cut). One-line change in the consensus preset. Keeps the same √-shaped curve, just shifts it downward. Easy governance, predictable outcome.
2. **Curve reshape.** Replace the √ denominator with something that drops off faster at high staking ratios. Ethereum researcher Anders Elowsson has published proposals along the lines of `c / (√D × (1 + kD))` that compress yields more aggressively once staking exceeds the original target. The functional form is more complex but the policy is more durable: it caps over-staking on its own instead of relying on future scalar tweaks.

Either path requires a hard fork. Both were seriously discussed in the run-up to Pectra (which activated on Ethereum mainnet in 2025) but were left out. Pectra shipped EIP-7251 (validator consolidation, max effective balance up to 2,048 ETH) and other items, and explicitly deferred the issuance question. Discussion has now shifted to a future fork, with Glamsterdam and its successors as the realistic windows.

## Why The Debate Is Loud Now

The Beacon Chain's design assumption broke quietly. Staking participation rose past 20% in 2023, past 25% in 2024, and into the 30%+ range over 2025–2026, helped enormously by liquid staking tokens that let stakers keep using their ETH inside DeFi. Lido alone holds roughly $20.5B of ETH on its protocol per DefiLlama (the largest LST by a wide margin), with ether.fi restaking ($5B+), Binance Staked ETH, Rocket Pool, Coinbase's cbETH, mETH and others making up the rest of the LST and CEX-staking landscape.

That supply structure produced a feedback loop the curve was never designed for. LSTs strip the only practical cost of staking, illiquidity, which means the marginal staker keeps showing up well past the point where the curve was supposed to make staking unattractive. The protocol responds by lowering yields, but each yield decrement is offset by composability gains as LSTs get plumbed deeper into [lending](/decentralized-lending), restaking, and stablecoin collateral. Equilibrium keeps moving up.

Several things changed in the last year that turned a slow-burn researcher concern into a public fight:

- **Yield is now genuinely low.** Sub-3% nominal issuance with MEV adding a thin variable on top. Solo-staker economics are tight, and the yield gap between staking and on-chain dollar yield has narrowed enough that some validators are weighing alternatives.
- **LST and LRT incidents stacked up.** Restaking fragility, curated-vault liquidity crunches on Morpho, and high-profile depegs (the Resolv USR exploit in March, the [KelpDAO rsETH incident](/kelpdao-rseth-exploit) in April) have made systemic-risk arguments concrete rather than theoretical.
- **A future fork has to touch the curve anyway.** Faster slot times and other consensus changes proposed for Glamsterdam force adjustments to the per-epoch reward math. If you are already opening that surface, the question of whether to also rebalance the long-run curve is unavoidable.
- **A senior LST voice put the existential framing in writing.** Gusakov's tweet was not the first time a Lido figure pushed back on issuance reduction, but it was the most quotable, and it drew the line in a way that made researchers respond at length. Jerome de Tychey's reply, illustrated with pre-LST DeFi TVL data, has been the most-shared rebuttal.

## The Anti-Cut Camp

The anti-cut argument, pushed hardest by LST operators and DeFi power users, is straightforward: liquid staking tokens are now the load-bearing collateral asset of on-chain finance. Lower yields mean less staking, which means less LST supply, which means less collateral available to lending markets, restaking, and the curated yield vaults that have become a meaningful share of DeFi TVL.

Stripped to its strongest form, the case has four pieces:

1. **LSTs are the dominant DeFi collateral.** stETH and its peers underpin lending markets on [Aave](/aave) and Morpho, restaking on EigenLayer, and a wide range of leveraged-yield strategies. A material share of DeFi activity is loops on top of LSTs.
2. **Liquid staking changed DeFi's growth curve.** DeFi existed before LSTs, but its post-2022 expansion was meaningfully driven by the unlock of staked ETH as productive collateral. Reversing that incentive could compress activity.
3. **Security is already strong.** Ethereum is the most-staked PoS chain in absolute terms. Any cut that reduces the staked share is a perceived security regression, even if the absolute number stays comfortably over the threshold for credible finality.
4. **Timing.** L2 scaling, institutional adoption, and competition from new L1s mean any change that hits the user-facing yield is more likely to drive capital out than recycle it inside Ethereum.

The anti-cut framing is most credible when LST operators frame it as product risk, a concrete near-term consequence, rather than as a question about Ethereum's survival. Where it gets weaker is the leap from "LST TVL drops" to "DeFi shrinks to the size of a penny." Pre-LST DeFi was not a penny. It was a multi-billion-dollar ecosystem that ran without staked-ETH derivatives. The argument is on stronger ground describing a pricey transition than a terminal one.

## The Pro-Cut Camp

The pro-cut side is led by protocol researchers, ETH-as-money advocates, and core-dev-adjacent voices who treat the current curve as a design overshoot. Their case is longer-horizon and structural:

1. **ETH's moneyness is being eroded.** When the staking yield meaningfully exceeds risk-adjusted DeFi yield on native ETH, the rational holder stakes (directly or via an LST) instead of lending. That hollows out the pool of unstaked ETH available as pristine collateral and makes ETH less useful as money. Lower issuance reverses the trade-off.
2. **DeFi predates LST dominance.** The chart Jerome de Tychey circulated this week is the central exhibit: DeFi grew and matured before liquid staking became its main collateral source. If LST supply contracts, the unstaked ETH that exits LSTs has to go somewhere, and a meaningful share would rotate into native lending and stablecoin collateral.
3. **The original design was the right one.** The 20–30% target was not a back-of-envelope number. It came from an analysis of validator economics, security thresholds, and asset utility that researchers still defend. The current 32%+ is the curve overshooting because LSTs eliminated the friction the curve was built around.
4. **Systemic risk compounds with staking ratio.** As the staked share grows, slashing becomes a less credible deterrent in absolute terms (the residual unstaked supply is smaller relative to penalties). LST and LRT rehypothecation imports smart-contract and governance risk into what is supposed to be the protocol's clean security layer. Recent depeg and curated-vault episodes are early warnings, not edge cases.
5. **Lower issuance is monetarily stimulative for ETH.** Holding everything else constant, a permanent cut to inflation strengthens the asset's monetary premium. That higher monetary premium in turn supports the dollar value of the validator set — the security budget does not necessarily shrink with the issuance rate.

The pro-cut case is strongest when it treats the issuance curve as a piece of monetary policy that can be tuned, and weakest when it underestimates how disruptive even a moderate cut would be for current LST and curated-vault P&L. Solo-staker economics are already tough at 3%. A cut without a parallel improvement to MEV smoothing or proposer-builder economics would make the small-scale validator picture worse before it gets better.

## What A Cut Would Mechanically Do

Both camps agree on the direction of the first-order effect; they disagree on the second-order chain. A scalar cut from `BASE_REWARD_FACTOR = 64` to 32 would, holding the staking ratio constant, halve the consensus-layer issuance yield. At a ~32% staking ratio that takes the nominal CL yield from ~3% to ~1.5%, with MEV layered on top.

In practice the staking ratio would not stay constant. The curve compresses yield as staking grows; the same logic in reverse means a yield cut should reduce the staked share over time as marginal validators exit. The disagreement is about how much exits, how fast, and where the freed ETH goes. Anti-cut voices model the freed ETH as net flight: out of staking, out of LSTs, and largely out of DeFi. Pro-cut voices model it as rotation: out of LSTs, into lending, native ETH stablecoin collateral, and other on-chain uses where ETH is currently undersupplied because the staking-yield bid keeps it locked.

A curve reshape, the Elowsson-style tempered formulas, is more aggressive on the tail and less aggressive at the originally-targeted 20–25% range. The political case for that path is that it preserves attractive solo-staker yields if the staking ratio comes back inside the original band, while still ensuring the system can never re-overshoot in the same way. The cost is implementation complexity and a more complicated debate about the parameter `k`.

## Where This Sits On The Roadmap

Nothing changes immediately. Ethereum's social process for consensus-level changes runs through All Core Devs, Ethereum Magicians, and the standard EIP track. Pectra deferred the issuance question. Glamsterdam is the next realistic window where curve-modifying EIPs could land, and even then, only if researchers, client teams, and the broader community converge on a specific proposal.

The fact that the conversation is now public and high-profile is itself a signal. When LST operators, researchers, and core-dev-adjacent voices are arguing in the open about the right shape of `BASE_REWARD_FACTOR` and curve denominators, the issue has moved from "abstract concern" into the live decision queue. That does not guarantee a change, but it raises the probability that the next major fork includes some form of issuance adjustment — even if the form ends up being modest.

For builders and capital allocators the practical implications are forward-looking. Strategies that depend on a particular LST yield level over multi-year horizons are now exposed to a non-trivial protocol-policy risk. Vault curators and structured-yield products built on top of stETH and friends should be modeling at least a downside scenario where consensus-layer issuance is cut by a third or more in a future fork. That is consistent with how mature markets handle policy uncertainty: stress-test the path, do not assume the curve is frozen forever.

## Bottom Line

The Lido tweet that lit this fuse made a genuine claim: that LSTs are existential to Ethereum, and cutting issuance would unwind them. The counter-claim is that the existing curve is itself a slow-moving threat to ETH's value proposition, and that the longer the protocol waits to bring staking back inside its design band, the more painful the eventual rebalancing becomes.

Both views can be partly right. The curve is overshooting its design target; LSTs are also load-bearing for current DeFi composability. The hard problem is choosing how much of the LST and curated-vault economy you are willing to compress in order to defend ETH's moneyness, and on what timeline. That is a monetary-policy decision in a protocol that has been historically reluctant to make explicit monetary-policy decisions, and it is the reason the debate now reads as existential to people on both sides.

A change is not happening this quarter. The question is whether the next major fork makes the call, and if so, whether it picks a clean scalar cut or a structurally different curve. Either answer rewrites the long-run economics of staking, LSTs, and the [yield premium](/defi-yield-risk-premium) that the rest of on-chain finance prices off of.
