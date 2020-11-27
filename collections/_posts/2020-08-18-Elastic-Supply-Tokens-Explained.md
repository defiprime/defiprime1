---
git-date:
layout: [blog, blog-amp]
title:  "Elastic Supply Tokens Explained"
permalink: elastic
h1title: "Elastic Supply Tokens Explained"
pagetitle: "Elastic Supply Tokens Explained"
metadescription: "Elastic supply tokens are one of the newer and less-known of these blooming sectors, and yet the field’s gained traction upon a handful of price-elastic projects recently breaking into DeFi’s limelight"
category: blog
featured-image: /images/blog/elastic-og.png
intro: "In this post, we’ll break down how these assets work via rebases and walk through top example projects from today’s cryptoeconomy"
author: Peaster
tags: ['DeFi Guides']
---
Ethereum’s decentralized finance arena has many rising sectors, including non-custodial exchanges, stablecoins, tokenized bitcoin, and more.

Elastic supply tokens are one of the newer and less-known of these blooming sectors, and yet the field’s gained traction upon a handful of price-elastic projects recently breaking into DeFi’s limelight. In this post, we’ll break down how these assets work via rebases and walk through top example projects from today’s cryptoeconomy.  

## What’s a rebase?

A price-elastic token is one where the project’s total token supply is not fixed, but instead automatically adjusts on a routine basis.

These token supply adjustments, called “rebases,” take place per market demand and are done in such a way that users’ proportional holdings ultimately don’t change and thus aren’t diluted. Rebases are performed per a specific target price, with the idea being that a token’s nominal price will steadily be moved over time toward its target, e.g. $1 USD.

In this sense, price-elastic tokens are like cousins to stablecoins, in that both have price targets. Yet these token classes are fundamentally different. Stablecoins have semi-fixed, governable supplies and are designed to closely track their target prices at all times, while rebases make price-elastic tokens into synthetic commodities with fluctuating values and supplies that gradually stabilize.

Ultimately, rebases are designed to be tradable, and thus potentially profitable, events. However, the nature of rebases means that gains or losses can be compounded when investing in price-elastic tokens.

For example, let’s say you bought 100 XYZ, a hypothetical price-elastic token with a target price of $1, for $100. Then let’s say buy pressure pushed the price of XYZ up 20% to $1.20 and a rebase pushed the XYZ total supply up by 20%. This would leave the user with 120 XYZ and an acute portfolio price of $144. On the flip side, negative rebases (when the XYZ price is below its target) combined with a plunging XYZ market cap could lead to compounding losses.  

![](/images/blog/pic01.png)

## Tokens with elastic supply  

### AMPL

Dubbed an “adaptive money” project, [Ampleforth](https://defiprime.com/product/ampleforth) is designed as an uncollateralized, synthetic commodity that is aimed at providing returns that are uncorrelated with the rest of the cryptoeconomy. It’s the largest price-elastic token project to date.

Notably, Ampleforth relies on a Chainlink oracle price feed to determine the AMPL exchange rate. The target price of Ampleforth’s AMPL token is $1.009 in accordance with the U.S. dollar’s 2019 Consumer Price Index (CPI) rate, and the project’s rebases take place daily at 2am UTC.

Previously these rebases took place at 8pm UTC, but the schedule was updated last fall to be more accommodating to data providers. At the time, Ampleforth founder and CEO Evan Kuo explained:

“_Most data providers aggregate 24hr average prices from midnight-to-midnight. By aligning our operations to this same schedule, we increase the number of aggregators that can be utilized by our oracle system_.”

The project is a relatively new one, in that its [whitepaper](https://www.ampleforth.org/papers/) dates to May 2019 and the AMPL initial token offering launched on Bitfinex’s Tokenix platform that summer. The Ampleforth team raised just under $5 million in less than 15 seconds during the sale. Within two months of the offering, AMPL was listed on Uniswap and Bancor and slated for inclusion in Compound, and the project’s been on the rise ever since.

Along with the recent spike of activity around DeFi in general, Ampleforth has seen an uptick in activity lately thanks to kicking off its “Geyser” liquidity mining campaign this summer. One of the more interesting aspects of this offering is its duration. While some recent DeFi projects have run liquidity mining campaigns that were weeks-long, Ampleforth’s Geyser is structured to distribute rewards to participants for the next 10 years.

As for how AMPL is doing now, the token hit an all-time price high of $3.79 on July 11th, 2020, and the project’s since come back down to earth. At the time of this post’s writing, the AMPL price was $0.59 and the token had a $139 million market cap with a circulating supply of ~256 million AMPL.

![](/images/blog/Ampleforth.png)


### RMPL

A fork of Ampleforth, [RMPL](https://github.com/rmpldefiteam/rmpl) is a price-elastic token that employs randomized, not fixed, rebasing. These rebases take place within 48-hour windows but on average occur every 24 hours and track a $1 USD price target. Rebases begin when the RMPL price is above $1.05 or below $0.95. The randomization is meant to mitigate “market manipulation” related to the timing of rebases. This model stands in contrast to Ampleforth, whose rebases are explicitly meant to be arbitrage events.

The RMPL team, which is anonymous and has yet to release its whitepaper, conducted its pre-sale on August 2nd, 2020, and then listed RMPL on Uniswap on August 3rd. Currently, the project is working on releasing the RMPL Cradle, which is a mechanism that will incentivize RMPL liquidity provision on Uniswap via RMPL ecosystem pool rewards. At present, the RMPL price is $0.34 and the project’s circulating supply isn’t clear.


### YAM

![](/images/blog/YAM_Farmer.png)

Yam Finance introduced and launched its protocol and price-elastic [YAM token](https://medium.com/@yamfinance/yam-finance-d0ad577250c7) on August 11th, 2020. The conspicuously unaudited project was billed as an “experiment in fair farming, governance, and elasticity,” and its creators added:

“_We STRONGLY urge caution to anyone who chooses to engage with these contracts and think a proper professional audit would be highly advisable if this project gets any meaningful use_.”

The project did quickly recieve meaningful use as more than a few DeFi users promptly rallied around Yam’s design. Notably, the project was composed as a DeFi Frankenstein of sorts, with its code leaning on Ampleforth’s elastic supply, Synthetix’s staking system, and Compound’s governance module. Yet the Yam protocol was more than the sum of these parts, as the project was additionally designed to buy up yCRV tokens during positive rebases for Yam’s governable treasury.

With a price target of $1 USD, YAM rebases every 12 hours: once at 8pm UTC and once at 8am UTC. The token was distributed exclusively via yield farming to stakers who supplied assets to one of Yam’s supported staking pools. The initial pools were based around ETH/AMPL Uniswap V2 LP tokens, COMP, LEND, LINK, MKR, SNX, WETH, and YFI, and an additional YAM/yCRV Uniswap LP pool was later opened up.

Once live, Yam Finance rapidly ballooned in size as users rushed in to farm YAM. Within a day, the protocol brought in more than $600 million in total value locked (TVL) and the YAM price skyrocketed up to a peak of $167. Then things took a turn for the worse.

On August 12th, a [bug was discovered](https://medium.com/@yamfinance/yam-post-rescue-attempt-update-c9c90c05953f) in Yam’s rebasing system that would, if unchecked, allow way more YAM to be minted than was ever intended. In fact, so much YAM would be created that governance quorums, and thus governance in general, would be made impossible.

At this point, Yam’s builders quickly set up a delegation UI so that YAM holders could vote on a governance proposal to fix the rebase issue. However, the proposal failed and the ensuing rebase rendered Yam and its $750,000 yCRV treasury ungovernable.

To this end, the project’s first rendition was a failure as a yield and governance experiment. Interestingly, though, the original YAM will continue to rebase on Ethereum indefinitely as a price-elastic token, akin to AMPL.

Moreover, there are now migration plans in the works for a YAMv2 system. The Yam team set up a Gitcoin grant page to fund a protocol audit, and more than $115,000 has been donated to that effort to date.

The pivot would entail an initial migration contract being set up that would allow users to convert their YAM to YAMv2. Once the underlying protocol’s audits are completed, then users could migrate their YAMv2 to YAMv3 using another smart contract. If all goes well, then the protocol’s builders will advocate that users who delegated YAM to defend against the rebase bug should be made whole with YAM rewards and bonuses.


### REB

Another Ampleforth fork, [Rebased](https://rebased.fi/) is a new elastic supply project whose REB token was first launched for sale through Uniswap on August 14th, 2020.

With a price target of $1 USD, REB rebases every 12 hours, once at 9am CET and once at 9pm CET. Initially, the project started out with a total supply of 2.5 million REB and a circulating supply of 2 million REB. Now, there are more than 2.25 million of the tokens circulating in the cryptoeconomy.

The Rebased team has no whitepaper published yet and says they haven’t set aside any REB for the “team, advisors, partners, private investors, or any other centralized party.” Per the creators, Rebased’s raison d’etre is serving as a more immutable, inflation-resistant alternative to Ampleforth.

And while Rebased is still new, unproven, and largely unknown, the REB token managed to generate $250,000 of liquidity on Uniswap within its first week being live.


### BASED

Self-described as a “DeFi game of chicken,” BASED Protocol is a price-elastic token project that targets a price of $1 sUSD, i.e. Synthetix’s dollar-pegged stablecoin. The project is set to be ownerless, as its admin keys are scheduled to be burned so that its contracts can’t be altered in perpetuity.

BASED rebases take place every 24 hours and occur if the price of BASED differs from the sUSD price by 5%, whether the difference is up or down. For distribution, the project relied on two staking pools. The first, Pool 0, was a Curve $sUSDv2 LP pool that was slotted 25,000 BASED, with those rewards halved on a daily basis. The second, Pool 1, was another Curve $sUSDv2 LP pool, except this pool’s halving period was 72 hours and had 75,000 BASED for distribution. Notably, BASED was designed so that rebasing wouldn’t begin until 97% of all BASED tokens were claimed.

On August 12th, DeFi excitement saw BASED hit an all-time price high of $1,393. A snag was hit on August 13th, when a flaw in the design of Pool 1 allowed a user to freeze it. While all user funds were ultimately safe, the project’s builders redeployed a separate Pool 1 to make good on the mistake. On August 17th, a migration plan was revealed that would entail users moving into a new [BASEDv1.5 pool](https://twitter.com/BasedProtocol/status/1295471038759702528). At the time of this post’s writing, the BASED price was $370.


## Conclusion

Elastic supply tokens comprise a rising sector of DeFi that’s seeing rapid iteration lately. For some, these projects don’t provide meaningful or productive additions to the current landscape of digital money. For others, price-elastic projects are cryptonative innovations that pave the way to new kinds of finance.

Wherever you stand, it’s clear that price-elastic token projects are attracting a good bit of attention recently, which brings with it greed as well as bad actors. Just because these projects are hot doesn’t mean they’re all safe, regardless of the hype and how many other folks may be using them at the time. Bugs are an ever-present reality and threat in DeFi, so tread cautiously.

Ampleforth is hardly perfect, but it’s the most proven price-elastic token so far. To be safe, be particularly careful with newer and less-known projects. If you go chasing compounding gains, you might ended up with compounding losses … or worse, nothing.
