---
layout: blog
title: "BitGo launches Bitcoin staking with Stacks in qualified custody"
url: /bitgo-bitcoin-staking-stacks-custody.html
h1title: "BitGo launches Bitcoin staking with Stacks in qualified custody"
pagetitle: "BitGo Bitcoin staking: Stacks bonds, custody and risks"
metadescription: "BitGo opens Stacks Bitcoin staking to whitelisted institutions, with paired $STX, six-month bonds and variable bitcoin rewards."
category: blog
featured-image: /images/blog/bitgo-bitcoin-staking-stacks-custody-ogp.png
intro: "BitGo has opened Bitcoin staking through Stacks to eligible institutions while keeping principal in qualified custody and requiring a paired $STX lock."
author: sawinyh
tags: ["News"]
date: 2026-11-04T07:35:44+00:00
---

On November 3, 2026, BitGo announced Bitcoin staking through Stacks for whitelisted institutional clients of BitGo Bank & Trust. The integration pays rewards in bitcoin and keeps the principal on the Bitcoin network in qualified custody. Participation requires a paired $STX position worth 5% of the staked bitcoin's value.

BitGo's [launch announcement](https://www.bitgo.com/resources/blog/bitgo-adds-bitcoin-staking-through-stacks/) describes a live service limited to institutional partners managed by Stacks Labs. Clients stake from their existing BitGo accounts. The service is separate from BitGo's [Gokubu consumer card](/bitgo-gokubu-card-collateral-rewards.html), which the company introduced through BitGo Labs.

The integration uses PoX-5, the bootstrap phase of Stacks' Proof-of-Transfer mechanism. Bitcoin stays with the custodian. The paired $STX is locked on Stacks, and the position must be registered with the protocol before it qualifies for rewards. BitGo then claims those rewards on the client's behalf.

## A bitcoin payout with a second asset at risk

Stacks' [announcement of the BitGo integration](https://www.stacks.co/blog/bitgo-announces-bitcoin-staking-with-stacks-for-institutional-clients-in-qualified-custody) puts the bond term at about six months. Standard Bitcoin script timelocks the bitcoin. The paired $STX allocates staking capacity and secures the position's claim on rewards. Clients receive bitcoin payouts but remain exposed to the market value of the paired $STX throughout the lock.

The [institutional product documentation](https://www.stacks.co/institutional-bitcoin-staking) describes weekly bitcoin distributions over the bonding period. According to Stacks, a target yield is set before each period opens and applies for the full term. The realized rate can vary with the timing of miner reward distributions. BitGo separately warns that rewards depend on protocol activity and conditions and are not guaranteed.

Stacks miners supply the rewards by spending bitcoin to compete for $STX block rewards and transaction fees. Active protocol bonds receive the target yield first. Excess miner revenue is then shared between participants staking only $STX and a reserve fund. The reward payments come from this miner expenditure, without lending out the client's bitcoin to collect interest.

Stacks says the underlying miner-funded mechanism has distributed more than 4,200 BTC since January 2021. That cumulative figure covers the mechanism's history. It does not measure rewards earned through the newly announced BitGo integration or the amount of bitcoin committed by BitGo clients.

During PoX-5, the reserve accumulates funds without making payouts. Stacks describes this as accrual-only mode, with reserve drawdowns beginning under PoX-6. The reserve's role in supporting bond rewards depends on which phase is running: participants in the current bootstrap cannot assume the fund already makes the payouts described for its proposed successor.

The protocol includes no slashing. BitGo still lists smart-contract, protocol and network risk, alongside $STX price risk and restricted access to bitcoin, as potential causes of delay or loss. Qualified custody leaves those protocol exposures in place. Third parties develop and maintain Stacks, according to BitGo, which neither operates nor controls the protocol.

## Custody remains, liquidity changes

BitGo says the staking design leaves bitcoin unwrapped, unbridged and unloaned. The qualified custodian holds the timelocked principal under the client's existing custody arrangement for the staking period. Eligible institutions can participate from that arrangement without moving their bitcoin to another chain or onboarding a replacement custodian.

Access to the principal changes during the lock. Stacks' general product documentation describes an optional early exit: participants can release bitcoin before the period ends if they forfeit the remaining yield. The paired $STX stays locked for the full term, leaving that asset committed until maturity even after the bitcoin has been released.

BitGo's own disclosure uses more restrictive wording: staked bitcoin generally cannot be accessed until the bonding period ends. Its announcement does not say whether clients can use the general Stacks early-exit option through the BitGo integration or how they would request it. Availability of that withdrawal facility in a BitGo account remains unconfirmed.

Clients can route rewards to an address different from the staking address. This keeps principal and rewards in separate balances from the moment payments arrive. BitGo presents the option as useful for exchange-traded fund and exchange-traded product issuers that need separate principal and reward accounting. Fund issuers should consult their own advisers on regulatory, tax and accounting treatment, the company says.

BitGo's disclosure also states the limits of qualified custody: digital assets are not deposits and are not FDIC insured. The company does not guarantee protocol performance, rewards or the value of the assets. Clients must meet the eligibility requirements, and access remains subject to their applicable agreements.

## Whitelisted bonds before open auctions

The public onboarding instructions require both a bitcoin wallet and a $STX wallet. After an entity clears review, the Stacks Endowment approves its addresses for the bonding period. Each period has fixed capacity, allocated to approved participants before it opens. Institutions requesting access apply for that allocation; entry into a bond remains restricted.

Stacks' [phase-specific documentation](https://www.stacks.co/blog/bitcoin-staking-pox-5-pox-6) says a new bonding period opens about monthly, with overlapping six-month terms. During PoX-5, the Endowment sets capacity and target yield. The pairing ratio stays at 5% throughout the bootstrap. These are the administrative settings for the staking product now available through BitGo.

PoX-6 would replace the current allocation process with permissionless auctions run by a decentralized signer set. Bidders would state the yield they accept, and bids would clear on yield. The whitelist would end. Anchor participants and pools would use the same open allocation process, with the auction's exact rules written into a Stacks Improvement Proposal and decided by a vote.

The transition requires a holder vote and a hard fork. Engineers are to draft the proposal once bootstrap results support an auction design and the necessary signer, wallet and custody tooling is ready. Stacks has set no activation date, and the auction's bid format, clearing rules and minimums remain undecided.
