---
layout: blog
title: "Ethena Pay launches Earn+ with an 11x leveraged vault"
url: /ethena-pay-earn-plus-leveraged-vault.html
h1title: "Ethena Pay launches Earn+ with an 11x leveraged vault"
pagetitle: "Ethena Pay Earn+: 12% target APY through an 11x vault"
metadescription: "Ethena Pay's Earn+ targets up to 12% APY through an Upshift and Steakhouse vault on Avalanche, with 11x leverage and a $4.5 million initial cap."
category: blog
featured-image: /images/blog/ethena-pay-earn-plus-leveraged-vault-ogp.png
intro: "Ethena Pay added an optional leveraged vault to its app, moving participating users' balances into a third-party strategy rather than its regular rewards program."
author: sawinyh
tags: ["News"]
date: 2026-10-28T12:25:05+00:00
---

On October 28, 2026, Ethena Pay [launched Earn+](https://pay.ethena.fi/blog/earn-launch), an optional vault product targeting up to 12% APY through a strategy that aims for approximately 11x leverage. Upshift and Steakhouse manage the external vault, which Ethena Pay says uses Aave v4 on Avalanche. Initial capacity is $4.5 million across all users.

Money allocated to Earn+ leaves the user's regular USD Account. Ethena Pay provides the interface; its [Earn+ FAQ](https://pay.ethena.fi/faq#earn-plus) says the company neither manages nor guarantees the vault assets. Users must accept separate terms and risk disclosures before they participate. Once money moves into Earn+, it stops earning the app's Daily Boost.

## A borrowing loop behind the target rate

The launch document sets out the borrowing loop. The vault supplies $USDe as collateral to an Aave v4 Avalanche market, borrows $USDT, buys more $USDe and repeats the trade. The stated leverage target is approximately 11x. Ethena Pay says the $USDe oracle on that market is pegged to $USDT, as on Aave v3. These details come from the operator's description of the strategy. They have not been independently verified through contract readings.

Only Ethena Pay users can access Earn+. The announcement says someone without an app account will not be able to access the vault on chain, even though its strategy runs through external protocols. Ethena Pay describes the vault as capable of operating across chains and protocols from launch. Avalanche is the execution network it names for the initial strategy.

The advertised APY is a target. The FAQ says the displayed reward rate can change, including falling. After a user opts in and transfers money, rewards are added to the Earn+ balance daily. To make that transfer, the user selects an amount in the app and reviews it before confirming. Opening an account alone leaves money outside the vault.

Ethena Pay names both external operators in its [terms of use](https://pay.ethena.fi/terms). The Upshift agreement is with Fractal Network, Ltd. or an Upshift partner or affiliate. The Steakhouse agreement is with Carniceria Tropical Inc., a wholly owned subsidiary of Steakhouse Financial Ltd., or a partner or affiliate. According to the FAQ, those providers can change their terms independently of Ethena Pay.

## Deposit caps and the withdrawal queue

At launch, Standard users can allocate $20,000, Pro users $50,000 and VIP users $200,000. Each personal limit sits beneath the aggregate $4.5 million vault cap. Ethena Pay says it will increase capacity as caps fill and that users will be able to upgrade their membership tiers shortly. It gives neither a date nor a size for the next capacity increase.

If a deposit would exceed a limit, it is declined and the money stays in the user's USD Account. The FAQ says reaching a limit leaves money already in Earn+ unaffected. Users can still withdraw it, and they are not required to remove an existing allocation. The cap governs how much money they can add to the vault.

Ethena Pay charges no fee for adding money or withdrawing it. The product description says adding money is instant and withdrawal requests are processed and paid back into the USD Account within 24 hours. It describes no contractual lock-up. The FAQ, however, warns that withdrawals can take longer than usual, so the stated processing window does not assure immediate access to the balance.

During a delay, the app keeps the withdrawal marked as pending and notifies the user when the money arrives. The FAQ says users need not take action while processing continues. If the money still fails to arrive, it directs them to support. Under this published process, submitting a withdrawal request and receiving the money are separate steps.

## What changes from the ordinary balance rewards

The [ordinary rewards program](https://pay.ethena.fi/faq) combines the prevailing $USDe base rate with Daily Boost. This promotional addition brings eligible balances up to the account tier's total rate. The headline rate of up to 6% per year already includes the base rate. Users do not receive a further 6% on top of what $USDe earns.

Daily Boost has a tier-specific balance cap. Money above that cap continues earning the $USDe base rate but receives no Boost. The incentive accrues on the time-weighted average daily value of eligible balances. It is ordinarily paid in $USDe within 24 hours of the accrual day's close and requires at least one qualifying card transaction each calendar month. Ethena Pay describes the incentive as discretionary.

Earn+ has its own reward rate and external operators. Money allocated to it is ineligible for Daily Boost, so users cannot combine the two advertised rates on the same allocation. The FAQ calls USD Earn+ the USD-denominated version of this optional feature. Participating means transferring money out of the main account, rather than changing the reward setting on money held there.

## Loss exposure sits with the vault allocation

The risk disclosure says users could lose some or all of the money they move into Earn+. Smart-contract bugs, exploits, outages and failures in third-party infrastructure could reduce or lock up funds. Ethena Pay says the operators and underlying protocol are separate systems outside its control.

Earn+ is not a bank deposit. The disclosure says it has no FDIC, SIPC or other deposit-insurance or investor-protection coverage. Ethena Pay disclaims responsibility for the vault's performance and losses and gives no guarantee of rewards or principal value. Its policy of charging no fee for entry or exit provides no protection against those losses.

The launch announcement and linked FAQ do not identify the vault contract address, the specific Aave market address or the strategy's liquidation parameters. They also leave the timing and size of any expansion beyond the initial capacity unpublished.
