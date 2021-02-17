---
git-date:
layout: [blog, blog-amp]
title:  "Mooniswap"
permalink: mooniswap
h1title: "Mooniswap"
pagetitle: "Mooniswap - New AMM exchange from 1inch team"
metadescription: "Anton told us the 1inch backstory from a hackathon project to a leading DeFi aggregator, and how's new Mooniswap AMM is different"
category: blog
featured-image: /images/blog/mooniswap-og.png
intro: "Anton told us the 1inch backstory from a hackathon project to a leading DeFi aggregator, and how's new Mooniswap AMM is different"
author: Defiprime
tags: ['Interview', 'DEXs', 'VC-founded', 'Liquidity Pools']
---
Anton told us the 1inch backstory from a hackathon project to a leading DeFi aggregator, and how's new Mooniswap AMM is different.

### Hello! What's your background, and what are you working on?

I'm Anton Bukov, co-founder and CTO of [1inch.exchange](https://1inch.exchange/#/r/0xEbDb626C95a25f4e304336b1adcAd0521a1Bdca1). I’m a software developer with more than 15 years experience in the field.

In December 2018, Sergej Kunz and I started to participate in [ETHGlobal](https://www.ethglobal.co/) and other blockchain hackathons around the world. Our first run was very successful for us! We won three sponsor prizes just by coding a dApp for SetProtocol, Kyber, and MakerDAO. By now we’ve attended more than 15 hackathons and implemented different ideas garnered from each of them. One of those ideas was 1inch, which came to life when we participated in the ETHNewYork 2019 hackathon.

Since then, the 1inch MVP has grown from a hackathon project into the leading DeFi aggregator with the best prices on the market. Simply put, 1inch discovers routes through various DEXs and liquidity pools, which allows the protocol to give better rates than any individual source.

This August, we also came up with [Mooniswap](https://mooniswap.exchange/#/swap?r=0xEbDb626C95a25f4e304336b1adcAd0521a1Bdca1) – a new AMM (automated market maker) where LP (liquidity provider) earnings are dramatically increased by slowing down price changes to prevent arbitrage traders from earning up to 100% of the swap slippages.

Besides 1inch and Mooniswap, I also serve as a core developer at NEAR. I built the [ETH-NEAR Rainbow Bridge](https://near.org/blog/eth-near-rainbow-bridge/) launched earlier this month. We’re excited to see the space grow along with our projects.

![](/images/blog/Mooniswap.png)

### What's the Mooniswap backstory?

A while ago we noticed a real problem of all leading AMMs: their liquidity providers do not earn on slippage.

When users swap tokens their exchange rate is formed by two parts: (1) fixed swap fee (e.g. 0.3% for Uniswap pools and/or an individual fee for each Balancer pool), and (2) price slippage due to volume swapped. The greater the size of the user’s swap, the worse the exchange rate. An unfortunate correlation!

Going back, the first part (i.e. swap fee) is earned by liquidity providers. However, the second part (i.e. slippage) is fully earned by arbitrage traders, who also share a significant part of the profits with miners by setting high gas prices to take advantage of transaction ordering in blocks. Most pools miss up to 100% of the possible LP income, whereas some of them miss 300%-500% of potential income.


![](/images/blog/mooniswap/image3.png)

![](/images/blog/mooniswap/image1.png)

**Mooniswap vs Uniswap**

![](/images/blog/mooniswap/image2.png)


### What went into building Mooniswap?


We started our investigation on the AMM arbitrage issue a few months ago. But once we came up with such an efficient solution, it took nearly two weeks to wrap everything up. This included writing smart contracts, preparing web UI, getting a security audit, and writing the whitepaper. We decided to start with a simple concept, i.e. 2-token pools of the same weight, to gauge how the DeFi community would like our idea.

Writing the smart contracts was the most inspiring part for me. We were able to verify if the idea was actually worth it or not. We verified different models in the process, like imbalanced deposits and withdrawals, multi-token, and custom-weighted pools.** **

It’s important to underline that we do not aim to compete with anyone, we aim to solve existing DeFi problems and improve the space. The 1inch team is mission-driven and works fast to achieve its mission. We built Mooniswap in 18 hours and launched it two weeks later. The team is thrilled to redistribute earnings to liquidity pools and protect traders from front-running.

Similarly, we built the 1inch DEX aggregator within two days at the ETHNewYork 2019 hackathon and the Chi Gastoken within the span of a week. We’re happy to see our users receive the best prices on the market because of our products. We’re also certainly looking forward to solving more problems and benefitting the overall space in as many ways as we can!

Ultimately, we prioritize safe and secure smart contracts. Thus Mooniswap has received three audits from some of the most prestigious auditors in the industry. If you’re interested, be sure to check out the Mooniswap audits from [Dapphub](https://dapp.org.uk/reports/mooniswap.html), [Scott Bigelow](https://mooniswap.exchange/docs/mooniswap-audit-report-2.pdf), and [Peppersec](https://mooniswap.exchange/docs/mooniswap-audit-report-3.pdf).


### What's the Mooniswap business model?

The Mooniswap business model is driven by the Referral Fee.

Mooniswap initially utilizes a 0.3% Swap Fee, which can be lowered all the way down to 0% in the future as a way to provide more competitive prices to the market. Moreover, Mooniswap introduces the Referral Fee to incentivise integrations with wallets and other services that increase trading volume and additional income for liquidity providers. The Referral Fee is only charged when the referral wallet is specified in transaction arguments.

The Referral Fee is fixed and is equal to 5% of income earned by liquidity providers on the trade. So the initial 0.3% Swap Fee will be split, with 0.015% going to referral and another 0.285% going to liquidity providers. Additional profits generated by virtual balances are also split in the same ratio, with 5% going to referral.

Notably, the Referral Fee does not introduce additional pressure on the price and rewards external actors who contribute to the protocol by providing trading volume. Apart from Swap Fee and Referral Fee, Mooniswap does not charge any additional protocol fees.

We largely prefer the Referral Fee over the swap fee. In order to guarantee liquidity provider earnings, Mooniswap does contain a swap fee of 0.3% (*this fee has been reduced 0.15% due to successful pool performance). The swap fee could go away as volumes increase.

Zooming out, the first customers of 1inch were myself and Sergej. It was exhausting and inefficient to manually check for the best trading prices on all the DEXes – e.g. Uniswap, Kyber, 0x – before placing a trade. We, like all crypto users, needed an elegant algorithm to search every DEX for the best trading price and instantly deliver an optimized trade. The solution came in 1inch: a decentralized exchange aggregator that sources liquidity from various exchanges and is capable of splitting a single trade transaction across multiple DEXes.

We believe there are no real competitors for 1inch, as our goal is not to compete but rather to contribute. We aim to unite traders and liquidity providers, facilitating transactions that are profitable for both sides. The core functionality of 1inch is to aggregate data from various decentralized exchanges and to combine the best prices from all bids with the necessary liquidity. In addition, we offer a fully on-chain open-source version of 1inch protocol that dozens of developers are already using in their projects to have easy access to all DeFi liquidity.


### What are your goals for the future?

We aim to continue to innovate and benefit the DeFi and Open Finance world in as many ways as we can. Look out for more 1inch community initiatives to come. We can’t wait to give the space more insights into we’ve deployed. And of course, can’t wait for the community’s feedback on what else we can build.

According to our estimates, by the end of 2020 1inch will account for up to 70% of the overall DEX market. Why? Largely, because 1inch is positive-sum and an efficiency improvement for users. It’s much easier for users to swap tokens via our platform than to check bids on all the different protocols and pools manually. And in 2021, 1inch will be ready to compete with centralized exchanges for users who swap assets a few times a day.


### What are your future thoughts for the DeFi market?

I believe that in the next 5-10 years the DeFi industry will grow massively. It’s already growing rapidly, but the advantages of peer-to-peer technologies can and will be more widely experienced.

Of course, in order for DEXes to dominate over CEXes, certain conditions have to be met in the future. DEXes and blockchain protocols have to perform 100 times faster than they do now. Users need to understand the core concept of the technology. User journeys have to shorten down and become friendlier for the beginners.

Also, the industry desperately needs more generally accepted security audit principles in order to prevent the next “DAO hack.” This way, the community and newcomers would feel more secure and willing to participate in the decentralized economy over the long term.

Taking into account current volumes and the speed of past development, we can safely conclude that the shift to DEX dominance is likely to accelerate in the middle of 2021. There is no doubt that DEXes will eventually win this competition due to superior technological advantages. A big question is whether the number of DEXes would continue to increase or if only a few dominant ones would come to reign. Time will certainly answer those questions very soon.


### Where can we go to learn more?

- Official Website: [https://1inch.exchange](https://1inch.exchange/#/r/0xEbDb626C95a25f4e304336b1adcAd0521a1Bdca1)
- Official Medium: [https://medium.com/@1inch.exchange](https://medium.com/@1inch.exchange)
- Official Twitter: [https://twitter.com/1inchExchange](https://twitter.com/1inchExchange)
- Official Discord: [https://discord.gg/Xyxv2Yz](https://discord.gg/Xyxv2Yz)
- Official Telegram: [https://t.me/OneInchExchange](https://t.me/OneInchExchange)
