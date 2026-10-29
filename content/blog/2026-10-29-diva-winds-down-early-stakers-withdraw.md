---
layout: blog
title: "Diva winds down and tells early stakers to withdraw"
url: /diva-winds-down-early-stakers-withdraw.html
h1title: "Diva winds down and tells early stakers to withdraw"
pagetitle: "Diva shuts down before mainnet, directs Enzyme withdrawals"
metadescription: "Diva cancels mainnet and directs early stakers to withdraw through Enzyme. Its incentive terms tied DIVA distributions to a launch that will not happen."
category: blog
featured-image: /images/blog/diva-winds-down-early-stakers-withdraw-ogp.png
intro: "Diva Staking has abandoned its mainnet launch and told Early Staker Vault depositors to withdraw through Enzyme."
author: sawinyh
tags: ["News"]
date: 2026-10-29T00:22:44+00:00
---

On October 28, 2026, Diva Staking [announced that it would wind down](https://x.com/divastaking/status/2115475924753711538) without launching on mainnet. It directed people who had deposited in its Early Staker Vaults to withdraw through Enzyme. The team attributed the decision to exhausted funding and an inability to pay for further audits and continued operation.

The team told depositors: “You can withdraw your deposits from Enzyme. There is nothing left to wait for.” The statement gives no withdrawal deadline or date for closing the Enzyme interface. It reports no exploit of the pre-deposit vaults. The security concern it describes is whether the team could safely launch the unfinished staking operation.

Diva said its funds ran out in mid-2024 and three people had continued working without revenue or salaries. According to the team, its Hoodi deployment had run for four months without a failure, but no large backer had agreed to help it launch. The remaining team could not afford new audits or maintain a protocol of this complexity.

The team said AI had helped finish the software but was also making vulnerabilities easier to find. It chose to close rather than launch with a risk that earlier audits had missed something. The developers cited that risk as a reason for cancelling mainnet; they did not disclose a specific vulnerability or a loss in the Enzyme vaults.

## What early stakers can withdraw

The [Early Stakers documentation](https://docs.divastaking.com/early_stakers/) describes an independently run initiative approved by the Diva DAO, using Enzyme's asset-management contracts. Participants supplied $ETH or $stETH before Diva's launch. Under that design, the $ETH remained in hold mode, while the $stETH remained untouched and earned its existing staking rewards. Conversion into Diva's own $divETH was supposed to happen after mainnet went live.

The withdrawal instruction concerns those pre-launch Enzyme deposits. Diva has not announced a redemption process for a live Diva staking token. The conversion described in the documentation depended on the mainnet launch that the team has now cancelled. Its shutdown statement names no replacement token or another destination for the assets that early stakers deposited.

The original [DIP-02 terms](https://www.tally.xyz/gov/diva/proposal/45468458207916765916984557235161596151150976178275597160417224501662414206717) describe depositors receiving Enzyme vault shares representing their proportional ownership of the underlying assets. Those terms allow withdrawal at any time, subject to a default 24-hour lock-up in the vault settings. These are the initiative's published terms. The shutdown statement gives no updated account of individual vault settings or the status of a particular user's withdrawal.

DIP-02 says vault shares cannot be sent to another address or transferred to third parties. Only minting and redemption are enabled under those terms, so the documented exit is to redeem the vault position. A depositor cannot transfer the receipt token to someone else under that design. The team's withdrawal instruction names Enzyme without publishing a separate migration procedure.

The [Early Staker landing page](https://diva.enzyme.finance/) still invites users to deposit and secure a place in the queue. It describes holding deposits until Diva launches and claiming rewards afterward. The page retains those launch-dependent instructions even though Diva's newer statement says mainnet will not happen and tells depositors they have nothing left to wait for.

## The incentive terms depended on mainnet

DIP-02 separated the initial deposit queue from the reward accrual period. Early deposits established a first-come, first-served ranking that would determine reward rates. Actual $DIVA accrual was tied to the period immediately before launch, rather than every day a deposit remained in the vault. The original reward schedule made no promise of accrual throughout the wait for mainnet.

The terms defined the start retrospectively, as a 30-day lookback from the formal Mainnet Launch Date. To reach that date, the protocol had to undergo at least two audits, become fully operational and go live on mainnet. The date was to be publicly announced. The reported Hoodi deployment did not meet that definition, and Diva has now cancelled the mainnet event on which the schedule depended.

Reward eligibility also depended on asset conversion. Under the original terms, a participant redeeming before full conversion into $divETH would not qualify for $DIVA distributions. For redemptions after conversion but before the 183-day deadline, accrual would depend on full commitment days. The shutdown statement announces no alternative distribution for participants who waited through development and now withdraw their deposits.

DIP-02 describes an off-chain calculation for each address, with final distributions based on on-chain data gathered through the Enzyme API. Its formula combines the deposited amount, days within the defined accrual period and the reward rate for the applicable tranche. Time spent in the deposit queue alone was not the entire calculation. Diva's announcement supplies neither a final calculation nor a replacement claims process.

The original terms excluded US residents, citizens and entities from the incentive initiative, along with people or entities in blacklisted or sanctioned countries. DIP-02 proposed enforcing the restriction through a self-declaration signed with the depositor's wallet on the Enzyme interface, while stating that no KYC was enforced. Those eligibility conditions governed participation in the incentive program. The shutdown notice gives a general withdrawal instruction to Early Staker Vault depositors.

The documentation separately describes $DIVA as non-transferable and says transferability requires DAO approval. This is a governance condition in the published documentation, not a verified reading of the contract's current state. The shutdown statement establishes neither a market value for the expected rewards nor a current vault balance.

Diva has told depositors to exit through Enzyme, but it has not specified a withdrawal cutoff or explained whether the DAO will adopt new terms for the launch-dependent incentive allocation.
