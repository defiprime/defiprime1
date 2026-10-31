---
layout: blog
title: "Recall Foundation winds down with November withdrawal deadline"
url: /recall-foundation-wind-down.html
h1title: "Recall Foundation winds down with November withdrawal deadline"
pagetitle: "Recall Foundation winds down with November withdrawal deadline"
metadescription: "Recall Foundation ends staking rewards and sets November 30 for app withdrawals, with no token redemption and an estimated future burn."
category: blog
featured-image: /images/blog/recall-foundation-wind-down-ogp.png
intro: "Recall Foundation is winding down with no holder redemption, a November 30 app withdrawal deadline and a direct-contract exit for later lockups."
author: sawinyh
tags: ["News"]
date: 2026-10-31T03:24:11+00:00
---

The Recall Foundation announced on October 30, 2026 that it will wind down, stop staking rewards and end support for $RECALL. Its [notice to holders](https://x.com/recallnet/status/2116234988601704457) sets November 30 as the deadline to unstake and withdraw through the app. Stakes whose lockups end later can still be withdrawn through the contract.

Token holders will receive no treasury distribution. The Foundation proposes burning the tokens it controls, but gives conflicting dates: a calendar entry says Foundation tokens were burned on October 30, while the detailed burn section places execution immediately before liquidation in Q1 2027. The notice describes the wind-down plan without independently confirming a completed burn.

The board made its decision independently of Recall Labs, which the notice describes as a separate corporate entity. The shutdown covers the Foundation and its wholly owned subsidiary, Atlas Networks Limited. The announcement does not say that Recall Labs is winding down.

## Stakers must initiate their own withdrawals

“Staked RECALL belongs to you and is not part of the burn,” the Foundation wrote. Nothing is automatically unstaked. Holders must initiate both the unstake and the withdrawal. The route depends on when their original lockup expires.

The Foundation says it has reduced the unstaking cooldown from 30 days to zero for requests made from October 30 onward. Existing requests retain their original withdrawal date. The original stake lockup also stays in place: holders must wait for it to end before unstaking. These are the operator's stated withdrawal conditions. The contract reading below did not independently check the cooldown parameter.

The calendar says app.recall.network will become read only on November 30. Elsewhere, the notice says access to Foundation-hosted applications will cease after 30 days. Its FAQ directs holders to unstake and withdraw in the app by November 30, and to use the contract if their lockup ends later. The notice gives no precise interface cutoff beyond that wording. Holders cannot assume app access will continue beyond the stated withdrawal window.

For direct withdrawals, the Foundation identifies the [staking proxy on Base](https://basescan.org/address/0x37ee1fe41231b631d62658372b457235b9b884e0). Its instructions are to connect the wallet holding the stake, open “Write as Proxy,” call `unstake(tokenId)` once the lockup ends, then call `withdraw(tokenId)`. Both transactions require Base $ETH for gas, and both calls use the original position identifier.

A historical RPC reading at Base block 53,297,682, timestamped October 30 at 18:25:11 UTC, confirmed deployed code at that address and returned `paused: false`. The snapshot precedes the announcement. It shows that the specified contract was deployed and reported itself unpaused at that block. It does not verify any holder's balance, lockup expiry or ability to complete a withdrawal today.

New competitions and staking rewards stop on October 30, according to the Foundation's calendar. Running competitions end, with earned rewards distributed through the app. The statement gives no separate deadline for claiming those competition rewards beyond its application wind-down schedule.

## Proposed burn depends on assets returning to the Foundation

The Foundation estimates its proposed burn at 358,562,442 RECALL, or 35.86% of total supply. It says this would leave an estimated 641,437,558 RECALL, with none held by the Foundation. These supply figures are the issuer's estimates and have not been independently verified.

The largest listed components are locked ecosystem reserves of 175.9M RECALL and locked Foundation treasury tokens of 57.8M RECALL. Foundation-controlled wallets outside those locked allocations account for another 79.7M RECALL. The proposal includes locked tokens under Foundation control, while expressly excluding individual users' staked tokens.

The remaining categories are 6.7M RECALL from a liquidity pool, 1.5M RECALL in unvested vendor, adviser and Foundation employee tokens, and 37.0M RECALL in market-maker loans and outstanding options. The Foundation says the pool amount is subject to supply fluctuations and assumes all options expire out of the money. The forecast total depends on those conditions; the amount ready for disposal is not fixed.

The stated destination is the null address ending in `dEaD`. The Foundation says holders can track transfers there and expects the burn immediately before liquidation of the Cayman Foundation in Q1 2027. Its calendar also describes all remaining tokens being burned by final liquidation. Neither that schedule nor the conflicting October 30 entry supplies transaction evidence of how much has already moved.

## Creditors receive funds, holders receive no redemption

“There is no buyback, redemption mechanism, or pro-rata distribution of treasury assets to token holders,” the Foundation wrote. It reports approximately $3,700,000 in $USDC, $USDT and fiat assets as of October 30, with $3,450,000 allocated to creditors and vendors, $200,000 to wind-down costs and $50,000 reserved for claims and contingencies until liquidation ends.

The estimated remaining balance is $0. The cost allocation covers legal work, liquidation, security, engineering, insurance and team transition. The Foundation calls these figures unaudited estimates that may change. They include fiat holdings and reflect the Foundation's account of its finances. The balances have not been independently reconciled on-chain.

The Foundation says continued protocol development is commercially unviable after reviewing adoption, operating costs and growth projections. It says a hack or security incident did not cause the decision. Software development, administrative support and liquidity support will cease, although the Foundation describes the Base token contract as immutable. Exchanges independently decide whether trading and listings continue. The Foundation says it expects delistings.

Atlas Networks Limited is expected to enter voluntary liquidation under British Virgin Islands law in December 2026. The Foundation expects to enter voluntary liquidation under Cayman Islands law in January 2027, with final completion estimated for Q1 2027. Applicable statutory and regulatory requirements take precedence over the announcement.

Official notices are restricted to the publication, @recallnet and the official Discord server. The Foundation says there will be no new token, airdrop or migration and that it will not send direct messages or ask for seed phrases. It has not reconciled the October 30 burn entry with its future execution schedule.
