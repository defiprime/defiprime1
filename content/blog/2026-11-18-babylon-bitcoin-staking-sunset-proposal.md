---
layout: blog
title: "Babylon proposal would end Bitcoin staking and cut inflation"
url: /babylon-bitcoin-staking-sunset-proposal.html
h1title: "Babylon proposal would end Bitcoin staking and cut inflation"
pagetitle: "Babylon proposes Bitcoin staking sunset and lower inflation"
metadescription: "Fisher Yu proposes ending Babylon Bitcoin staking by year-end, preserving existing unstaking rules and reducing $BABY inflation from 5.5% to 2%."
category: blog
featured-image: /images/blog/babylon-bitcoin-staking-sunset-proposal-ogp.png
intro: "Babylon’s proposed Bitcoin staking sunset would remove staking rewards and finality while keeping existing withdrawal rules as development shifts to vaults."
author: sawinyh
tags: ["Analysis"]
date: 2026-11-18T16:28:50+00:00
---

On November 17, 2026, Fisher Yu proposed [ending Babylon Bitcoin staking by year-end](https://forum.babylon.foundation/t/on-sunsetting-bitcoin-staking/790). The forum proposal would set Bitcoin staking and co-staking rewards to zero, disable staking finality and stop new registrations. Existing stakers would keep the ability to unstake under the protocol’s existing rules.

Yu also proposes reducing $BABY inflation from 5.5% to 2%. The post asks the community to consider the change. It gives no execution block, and there is no completed vote authorizing the shutdown. The proposed year-end target would end the staking service; depositors would retain the right to withdraw after that date.

Yu says Babylon’s Trustless Bitcoin Vaults, or TBV, need more engineering and security work than the staking protocol and require the team’s full attention. His proposal would move Babylon’s development effort toward using native Bitcoin in lending and other applications. The Aave integration is the immediate destination for that work.

## What would stop, and what would remain

The proposal treats reward payments, network functions and withdrawals separately. Bitcoin staking rewards would stop, along with the additional co-staking rewards for participants who also stake $BABY. Babylon would close new staking registrations. Existing positions would keep their withdrawal rights under the rules already attached to them, including after the proposed sunset.

Disabling staking finality would remove the security service those deposits support. Babylon’s [finality-provider documentation](https://docs.babylonlabs.io/operators/finality_providers/) describes providers as supplying finality votes on top of CometBFT, the network’s consensus mechanism. They receive commissions from Bitcoin staking delegations in exchange. Yu proposes removing that finality function. He does not propose shutting down CometBFT or say that the whole Babylon Genesis chain would cease operating.

The finality-provider documentation also sets out the existing service’s slashing mechanism. A provider that double-signs loses voting power, exposes its private key and cannot regain voting power. The exposed key can then sign slashing transactions for the provider’s delegations. The documentation describes how the staking design works; it reports no slashing event connected with the sunset proposal.

Unstaking has its own Bitcoin-side process. Babylon’s [earlier unbonding parameter proposal](https://forum.babylon.foundation/t/reduce-btc-stake-unbonding-delay-from-1008-to-301-bitcoin-blocks/661) explains that the delay runs from posting an unbonding transaction on Bitcoin to being able to withdraw the coins. The delay keeps stake slashable until Babylon Genesis has been checkpointed on Bitcoin, preventing an attacker from escaping after finalizing conflicting blocks.

That governance document proposed reducing the delay from 1008 to 301 Bitcoin blocks. It explicitly limited the updated parameters to new stake transactions. The relative timelock makes the unbonding output unspendable, except through the slashing path, until the lock expires. A holder can then spend the output to an address of their choice. Each holder needs to check the delay attached to their individual stake. The sunset post offers no replacement timelock or accelerated withdrawal procedure.

Yu leaves participation in TBV applications to the holder after unstaking. The post describes no automatic migration of an existing staking position into a borrowing position. Nor does it require holders to transfer the Bitcoin they withdraw into a vault.

## Co-staking loses its reward purpose

The [earlier co-staking tokenomics proposal](https://forum.babylon.foundation/t/inflation-reduction-and-the-introduction-of-co-staking/718) sets out the incentives the sunset would remove. It proposed a 5.5% inflation schedule with 1% going to Bitcoin stakers, 2% to $BABY stakers and an additional 2.35% to Bitcoin stakers who also stake $BABY. These percentages describe proposed allocations of token issuance. They are not a depositor’s annual return.

Under that design, every 20,000 $BABY staked made one bitcoin of an existing Bitcoin stake eligible for co-staking rewards. The Babylon address associated with the Bitcoin stake identified the participant receiving the rewards. The proposal’s stated aim was to encourage the same participants to support both validation and finality provision, with the additional rewards tied to their combined position.

Yu’s new proposal would end that additional reward alongside ordinary Bitcoin staking rewards. It gives 5.5% as the inflation level from which the reduction would begin. The earlier tokenomics document had called for reviewing the allocation when the vault protocol became ready. The sunset proposal takes up that planned review, though neither document supplies a pinned reading of the chain’s currently executed parameters.

Yu proposes token buybacks as a separate source of token demand. His sunset post points to the Aave integration’s revenue-sharing arrangement between Aave DAO and Babylon Foundation, with a portion allocated to $AAVE and $BABY purchases. Babylon’s integration announcement expressly says those terms guarantee neither revenue nor token purchases or returns. The proposal to end issuance-funded staking rewards establishes no replacement yield for existing stakers.

## The proposed destination is still staged

Babylon says Aave DAO approved the native Bitcoin collateral ARFC on November 9, 2026, with 100% of votes in favor. Its [announcement of the result](https://babylonlabs.io/blog/arfc-passed-to-enable-native-bitcoin-btc-collateral-on-aave-v4-through-babylon) names an AIP as the next step, the final governance stage before mainnet deployment. The ARFC approval supports the configuration and integration. Deployment still requires final approval and launch readiness.

Yu’s newer sunset post expects a permissioned private mainnet in late November, followed by a gradual opening to permissionless participation in early 2027. The integration announcement separately targets late 2026, subject to confirmation. It says the initial restricted phase would limit both participants and volume. The proposed replacement for staking is not yet an unrestricted service that existing staking users can enter.

Work on the vaults predates the shutdown discussion. Defiprime previously covered [HashKey Cloud’s plans to use Babylon vaults for native Bitcoin lending](/hashkey-cloud-to-integrate-babylon-bitcoin-vaults.html). Yu now proposes retiring the staking mechanism so the team can prioritize the vault integration, which would give holders a different use for their native Bitcoin.

The [Aave integration proposal](https://governance.aave.com/t/arfc-onboard-native-btc-as-collateral-to-aave-v4-via-babylon-trustless-bitcoin-vaults/25845) describes how the vaults would work. Bitcoin would be locked in a Taproot script on Bitcoin. Redemption would require a valid zero-knowledge proof of an event on the host chain, such as loan repayment. An eligible challenger could contest an invalid claim during a fraud-proof window. A depositor could operate their own vault provider to challenge claims.

Aave would account for the collateral on Ethereum. Because Aave accepts ERC-20 collateral, the integration would represent native Bitcoin collateral through a transfer-restricted accounting token. The proposal says users could not trade that token, transfer it between users or hold it outside the integration. The restricted representation would let a Bitcoin deposit support a borrowing position while the underlying coins remained on Bitcoin.

## Different operators, liquidation paths and controls

Yu suggests that existing finality providers could continue serving holders as vault providers. The Aave proposal defines a vault provider as an operator appointed by the depositor to set up and redeem the vault and challenge fraudulent claims. Application vault keepers would have separate claim and challenge rights. In the Aave integration, they would claim liquidated vaults and act as arbitrageurs. Providers making the transition would move from signing finality votes to managing vault operations and challenges.

Liquidation would require infrastructure beyond the native Bitcoin lock. The integration’s swap mechanism would let a permissionless liquidator exchange an acquired vault for wrapped Bitcoin, initially $WBTC, at the oracle rate less a discount. An Aave liquidity hub would supply the wrapped asset and record it as interest-bearing debt against the escrowed vault. Permissioned arbitrageurs would repay the principal and accrued interest before redeeming the underlying Bitcoin.

The redemption delay is the reason for separating those transactions. The Aave proposal restricts native redemption to actors pre-committed in the vault’s script and says it takes multiple days through the challenge window. Liquidators would receive wrapped Bitcoin immediately. Arbitrageurs would complete the slower Bitcoin-side redemption, leaving the liquidation process dependent on wrapped-asset liquidity even though the collateral itself remained native Bitcoin.

The proposal splits governance controls between the lending and vault systems. Aave DAO would set collateral and borrowing assets, caps, interest-rate strategy, liquidation parameters and oracle configuration. It could freeze individual assets to stop new supply and borrowing, or pause them to stop all activity for that asset. Babylon governance representatives would manage the vault protocol’s configuration and operator sets.

The vault protocol would also distinguish between a freeze and an emergency pause. According to the Aave proposal, freezing TBV would block new vault creation and borrowing while keeping exits available. Pausing would stop exits as well. Governance actions would execute through a public timelock with advance on-chain notice. Babylon’s own announcement warns that borrowing introduces liquidation risk and that protocol or network failures can cause losses or delay access to collateral.

The sunset post gives no execution block, implementation release or voting schedule for ending staking, while the vault rollout remains conditional on final governance approval and launch readiness. The sunset proposal has no published transition schedule connecting each existing stake’s withdrawal process to eligibility for the restricted vault launch.
