---
layout: blog
title: "Ethena removes $sUSDe cooldown as risk triggers await detail"
url: /ethena-susde-zero-cooldown.html
h1title: "Ethena removes $sUSDe cooldown as risk triggers await detail"
pagetitle: "Ethena removes $sUSDe cooldown as risk triggers await detail"
metadescription: "Ethena removes the $sUSDe exit delay while its risk committee keeps reward vesting and prepares exact triggers for reinstating a cooldown."
category: blog
featured-image: /images/blog/ethena-susde-zero-cooldown-ogp.png
intro: "Ethena has removed the $sUSDe unstaking delay after risk committee approval, with exact reinstatement thresholds still pending."
author: sawinyh
tags: ["Analysis"]
date: 2026-11-26T11:29:26+00:00
---

On November 26, 2026, Ethena [removed the one-day cooldown for unstaking $sUSDe](https://x.com/ethena/status/2125891305691873746), following approval from its risk committee. The operator also advertised zero mint fees. Holders can now exit the staking product without the waiting period, while rewards continue to vest over eight hours.

The committee based its approval on a liquidity snapshot and two conditions. In its [November update to the cooldown proposal](https://gov.ethenafoundation.com/t/proposal-adopt-a-dynamic-cooldown-period-for-susde-unstaking/759/5), it reported about $1.25B in Tier 1 liquidity against about $1.14B of outstanding $sUSDe as of November 23. It supported removing the delay on the condition that reward vesting stayed intact and a trigger for reinstating a cooldown was defined. The committee left the exact trigger levels for a follow-up.

## The approval goes beyond the existing model

Ethena's dynamic framework had a one-day minimum because its fastest liquidity category was modelled on one-day settlement. Immediate unstaking falls outside that calibration. The committee acknowledged the gap: “zero sits one step beyond its current calibration.” It supported the change based on current coverage and declining staking demand. It had not completed a zero-cooldown simulation.

The November snapshot put one-day settlement assets at roughly 1.1x outstanding $sUSDe. The committee separately reported one-day buffer coverage of 4.15x and three-day buffer coverage of 1.94x, both above its 1.5x minimum. The buffer ratios compare liquidity with redemption benchmarks. The 1.1x figure compares liquidity with the outstanding staking product. Each measures the same pool of backing assets against a different demand on it.

The Reserve Fund stood at 1.44x its analytical target, according to the same update. Staking supply had also been declining as holders moved into $USDe. The committee's case for immediate exits rested on available liquidity and reserve capacity, with a smaller staking balance to service. All of these figures describe the committee's November 23 snapshot. They are not measurements of the backing portfolio when Ethena announced the change.

The proposed reinstatement conditions cover both growth in staking supply and deterioration in liquidity coverage. One example is staking supply growing beyond Tier 1 liquidity. Another is three-day buffer coverage falling to an early-warning level set comfortably above the existing minimum. The update gives these as examples and promises exact levels later. It specifies neither an automatic execution mechanism nor a finalized trigger table.

## Why the cooldown became dynamic

The [original March proposal](https://gov.ethenafoundation.com/t/proposal-adopt-a-dynamic-cooldown-period-for-susde-unstaking/759/1) sought to replace the seven-day delay used since launch with one-, three-, five- or seven-day periods tied to the composition of backing assets. At the time, Ethena reported perpetual futures at 11% of backing and liquid stablecoins at 89%. Those allocations explained the March proposal; they are historical figures, not a current portfolio breakdown.

[Blockworks Advisory's framework](https://gov.ethenafoundation.com/t/proposal-adopt-a-dynamic-cooldown-period-for-susde-unstaking/759/2) grouped liquid backing by settlement speed and compared it with historical tail redemptions. Its p99 benchmarks were 4.1% of $USDe supply over one day, 9.2% over three days and 12.0% over seven days. The framework required available liquidity to cover 1.5 times the relevant benchmark as a safety cushion. Changes in the asset mix or redemption pressure could then change the cooldown.

Classifying a token required checking how it could be converted into spendable stablecoins. The committee challenged an earlier treatment that counted the full $USDtb balance as Tier 1. The revised framework counted only its 1% Anchorage instant cash buffer in that category. It assigned the remaining 99% to Tier 2 because replenishing through BUIDL depended on banking hours. The asset was redeemable, but the full balance could not be treated as immediately available liquidity.

The committee also requested a queue-pressure module that would use actual unstaking activity alongside the liquidity coverage calculations. It asked for explicit one-day monitoring and estimates of how long a shortened cooldown could survive sustained outflows. The policy would account for unstaking requests already arriving as well as the stock of assets available to meet them.

Earlier simulations showed how shortening a queue could concentrate withdrawals. Large request batches matured earlier and sometimes fell before days with low inflows. That produced spikes that would not have appeared under the longer delay. The simulations measured the timing of cash demand under a framework whose shortest settlement interval still allowed a day. Removing the waiting period requires a fresh calibration.

The original queue rule divided a day's unstaking requests by their 14-day rolling average. If that ratio exceeded 2.0x while three-day coverage fell below 1.5x, the recommendation increased by one day. A separate hard escalation applied when at least two consecutive days exceeded the historical p95 daily-outflow level. In that case, the cooldown recommendation moved straight to three days regardless of coverage. These rules belonged to the existing framework. They were not the still-unpublished thresholds for reversing the zero-cooldown change.

The coverage horizons count different assets. One-day coverage uses Tier 1 alone, while three-day coverage includes Tier 2 as well. A large second bucket can put three-day coverage above one-day coverage despite the longer redemption horizon. Blockworks identified the one-day ratio's position relative to the safety floor as the signal to monitor. Its ranking against the other coverage lines was not the test.

The report also examined an atomic swap route for external $USDtb holders: use it to mint $USDe, then redeem that $USDe for $USDC or $USDT. Onboarded mint and redeem participants could use the route without an Anchorage account. For $USDtb already inside the backing portfolio, however, the same operation would be circular. It would exchange claims within the backing and provide no additional net liquidity to the portfolio.

The stress-endurance simulation applied repeated daily drains to Tier 1 from each historical starting date. It tested normal, elevated and severe outflows at 4.1%, 6.15% and 8.2% of supply per day, counting the days until coverage fell below the safety floor. The simulated horizon stopped at 365 days. This tested how long liquidity could withstand continuing demand. A coverage snapshot measures the assets available at one observation point.

## Reward vesting remains the anti-sandwich protection

The committee's first condition preserves the eight-hour linear vesting of rewards. It said the protection is hardcoded and unaffected by the cooldown change. With immediate exits, vesting becomes the principal defense against a holder depositing just before a reward distribution and withdrawing immediately afterward to capture rewards at other stakers' expense.

Ethena's [staking documentation](https://docs.ethena.fi/technical-design/staking-usde) describes rewards entering the contract every eight hours and vesting linearly over the same interval. A holder who stakes and unstakes in consecutive blocks receives a share of the increase that vested between those blocks. The holder cannot capture a share of an entire payment becoming available at once. That reward-release schedule stays in place after the exit delay is removed.

The contract accounts for deposits and rewards through staking shares. A depositor transfers $USDe into the contract and receives $sUSDe. Subsequent reward transfers add underlying assets. On exit, the contract burns the staking token for a proportionate amount of $USDe, based on outstanding shares and the underlying assets it holds. The payout includes deposited principal and the holder's share of rewards.

The vault implements ERC4626 and exposes deposit and redemption functions, including variants with slippage thresholds and permit signatures. Users can interact directly with the contract or through Ethena's interface, according to the documentation. The cooldown change applies to this existing staking product. It is separate from the leveraged vault described in [Ethena Pay's earlier Earn+ launch](/ethena-pay-earn-plus-leveraged-vault.html).

Immediate unstaking leaves the source of rewards unchanged. Ethena's documentation says distributions come from protocol revenue, including staking income and funding and basis spreads on hedging positions. Distributions may stop when negative funding and basis income offset staking income, with the reserve fund supporting underlying backing. Although the announcement describes a savings rate, the cited staking terms make no fixed payout commitment.

The same documentation excludes acquisition by people with habitual residence or a registered office in the European Union or European Economic Area. Ethena's announcement of faster exits makes no change to that eligibility language. Zero mint fees are also an operator claim. The staking-token reading below checks neither mint pricing nor access permissions.

## What the contract reading establishes

Ethena's [canonical address list](https://docs.ethena.fi/technical-design/key-addresses) identifies the Ethereum staking contract and $sUSDe token at the same address. A pinned reading of [that contract](https://etherscan.io/address/0x9d39a5de30e57443bff2a8307a4256c8797a3497) at Ethereum block 26499019 returned deployed code, the name Staked USDe, 18 decimals and 900,002,943.229967 outstanding shares. That supply is a share count. The committee's dollar-denominated comparison is dated November 23, so the two readings differ in both units and observation date.

The pinned reading identifies the deployed token and its supply. It did not read the cooldown parameter, reconstruct the change transaction or verify the off-chain liquidity inventory behind the committee's ratios. Ethena's announcement is the source for the removal of the delay. The governance record supplies the committee's reasons for supporting it. The evidence set contains no independently verified execution block for the parameter change.

The staking documentation still describes the launch-era delayed exit: requested underlying moves to the silo contract and becomes withdrawable after the cooldown expires. That section covers the earlier workflow. Neither the announcement nor the committee update explains what happens to requests already waiting in the silo after the change. Holders with queued requests cannot assume those requests have cleared solely because Ethena announced zero-delay unstaking.

The committee still has to publish exact reinstatement thresholds and rerun its framework with a zero-cooldown state. Its linked approval leaves both items pending.
