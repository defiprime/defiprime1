---
git-date:
layout: [blog]
title:  Band Protocol
permalink: bandprotocol
h1title: 'Band Protocol - interview with CEO and co-founder Soravis Srinawakoon'
pagetitle: 'Band Protocol - interview with CEO and co-founder Soravis Srinawakoon'
metadescription: "Soravis shared his thoughts on DeFi core values and told us how Band Protocol bring data available on-chain."
category: blog
featured-image: /images/blog/bandprotocol-og.png
quote: /images/blog/bandprotocol-quote.png
intro: "Soravis shared his thoughts on DeFi core values and told us how Band Protocol bring data available on-chain."
author: Defiprime
tags: ['Interview', 'VC-founded', 'Oracles']

---
Soravis shared his thoughts on DeFi core values and told us how Band Protocol bring data available on-chain.

### Hello! What's your background, and what are you working on?

Hello guys, happy to be here with DeFi Prime to answer some of the burning questions crypto community have about Band Protocol.

My name is Soravis, CEO of [Band Protocol](https://bandprotocol.com/) (not to be confused with another Sorawit our CTO, and no we are not brothers). Quick background about myself, I have a Bachelor's degree in Computer Science and a Master's degree in Management Science, both from Stanford University. I spent two years at Boston Consulting Group, advising many C-level executives on their business strategy, ranging from how to double company revenues in two years to how to penetrate a monopoly market with a new product.

So while I was at Stanford, I had a chance to study cryptography class, and I found its mathematics very fascinating. Coincidentally, around 2014-2015, MIT conducted Bitcoin airdrop, so my co-founders and I became very interested. We went down the rabbit's hole, since built one of the first crypto faucets with over 500,000 downloads, and started Band Protocol together a few years later.

At a high level, Band Protocol offers decentralized data oracle. Our protocol connects off-chain real-world data to smart contracts and decentralized applications. Current dApps have no easy way to gain access to real-world information, which is outside of the blockchain. Since data input essentially dictates the behavior of smart contracts, the data input has to be decentralized. Otherwise, it defeats the whole purpose of using a smart contract in the first place. It has been a critical flaw and big security loophole for many dApps.

![](/images/blog/bandprotocol1.jpg)

### What's Band Protocol backstory?

When we first started two years ago, we tinkered around smart contract potential quite a lot. We try to build everything from lottery app (I love PowerBall, and I couldn't play in Thailand) and gaming faucet to stablecoins. Every single time we came across the same problem - which is how to get real-world data to blockchain in a fully decentralized way. That has been a big, common issue for almost any dApps we want to create. Imagine trying to build decentralized Uber without location data. Hence, we pivot and focus on this problem since.

Our idea became much stronger when we observed an emerging trend in the crypto space, which is the current decentralized finance movement. Almost every single one of DeFi projects needs price oracle in some way. The two top DeFi projects [MakerDAO](https://makerdao.com) and [Compound](https://compound.finance) are spending vast amounts of resources trying to build their own oracle. Oracles are still one of their more centralized components, which again introduces a potential security risk.

To me, this does not make any sense. DeFi should be concentrating on their core offering, e.g., how to optimize interest rate and bring real-world users to the platform rather than the price oracle component. If every dApps have to build their own Ethereum every single time, we will never get to any mass adoption. We think there is a need for a standard protocol to handle oracle in the most decentralized way. Decentralized oracles will enable much more comprehensive use cases, and many more dApps can then be built.

We were raising funds in one of the worst bear markets in crypto history. Luckily, we came across Sequoia, and we were impressed by their long term focus. We extensively discussed the size of the problem, our team background, our long term vision, and we finally got our first cheque from them. This allows us to bootstrap for another year and finally get to the launch of Band Protocol.

### What went into building the Band Protocol?

It feels long and short at the same time. We spent almost two years of 9-9-6, going through nearly five or six iterations of our protocol, to get ourselves to where we are now. I'm proud of my team, both in terms of technical capability and their ability to persevere through ups and downs of the market. We are still in the early days, and the technology is very nascent, but we are excited to bring our solution to mainnet and eventually drive for mass adoption.

One thing we did well is behaving like real startups. We are very laser-focused on solving actual need and problem in the industry, while at the same time stay nimble and humble by taking in all the feedback. This feedback comes from our partners, crypto friends, and investors (especially from those that pass us! Always ask for their feedback). This feedback has been precious and has helped us gone through many iterations of our design.

Security is our number one priority. If there is a vulnerability in our protocol, this can potentially impact all dApps that are using us, which will be catastrophic. We have done extensive code audit and partnership with [Certik](https://certik.org/), leading formal verification company that does code audit for many top crypto projects and companies.

### What's your business model and go-to-market strategy?

We believe data oracle is a HUGE space. All dApps from all blockchains will require access to real-world data for any meaningful applications (e.g., all defi depends on the price of eth right now). Given that smart contracts are as secure as the data input, the market size will be as big as the money at stake. Otherwise, it will be cheaper to attack.

Our token economic model ensures that our tokens capture the value of our decentralized network. We are not a payment token, but instead follow a 'work token' model where data providers and token holders stake tokens in order to perform work - that is, providing data to the blockchain. dApps who query data need to pay small query fee, similar to API fee. These fees are accrued within the protocol and distribute back to data providers and token holders proportionate to their staked tokens.

![](/images/blog/bandprotocol4.jpg)

You can think of these tokens almost as paying dividends, not from thin air but actually, from the work token holders do to secure network (similar to miners in Bitcoin). So we can value our tokens using regular discounted cash flow model. If there are more data usages, there will be more revenues flowing through the protocol. Which ultimately feeds back to data providers and token holders who stake their token. We intend to stake most of our company's tokens portion to earn part of the fee as our revenues, to ensure its sustainability. So we don't just depend on the token's price.

Our go-to-market focuses on two things:

1. Layer 1 solution partner: As you know, all Layer 1 solutions are also driving for traction. We partner with them to build data layer on top and go to market with them since they have a lot of resources and existing developer community. This partnership allows us to scale very quickly instead of going one dApp by dApp.
2. Geographically speaking, most defi now is in U.S. Asia has been lacking behind, but we are catching up. There are so many projects that are coming out in China, Korea, India, etc. We use our investor's reach as well as our footprint to reach out to these new projects and help them build a better solution quickly.

It's worth mentioning that even though there are many oracles, dApps are likely to use multiple solutions as well given the criticality of data integrity. For example, it's doubtful that projects with over 500M collateralized loan will trust us or Chainlink alone - they will likely use multiple to cross-check data.

The industry is still relatively new and has the potential to grow with the smart contract and dApp adoption. I wouldn't say there are any dominant players in terms of adoption yet. All dApps we speak to are quite open to try new solutions. This industry is still early and provides a lot of room to grow, so we are not too worried about competition.

### What are the unique features that differentiate you from the competitors

There are a few important things that differentiate us from other solutions:
- Speed & Ease of integration: We bring data available on-chain, thus whenever a smart contract needs access to data, it can do so as a simple function call. Simple and require no block confirmation delay. Many current solutions are asynchronous and require multiple blockchain confirmation before they can process data.
- Economic Incentive: To provide data in Band Protocol, you need to stake tokens and your reputation as collateral. This is very crucial and very different from other solutions that may not have proper decentralized economic incentive at a protocol level. For example, current solutions have not implemented staking and there is no concrete plan from publicly available information. Furthermore, current solutions with smart contracts on the mainnet do not have a staking mechanism and dApps are required to choose data providers they trust themselves.
- Cost & Scalability: Since data is published on-chain. Multiple dApps can consume the same data without incurring more costs to data providers. As the system grows, we expect the price of individual queries to go down.


### What are your goals for the future?

Our long term vision is to become the go-to data oracle solution for all dApps. We need to onboard a good reputable set of data providers and dApps to start using our protocol.   Upcoming months and weeks actually will be crucial to us. Mainnet is around the corner; several products are being planned so people can utilize and understand how Band Protocol fits into the ecosystem.

The biggest challenge is bootstrapping both dApps and data providers - that's why we have tokens for the ecosystem that we are using to subsidize both sides. These will be used to stake for data providers as well as support initial query fees for the first dApps that we onboard.

### What are your future thoughts for the DeFi market?

We believe decentralized finance has the potential to create a new financial system that is truly global, open, and transparent. What we have seen so far, mostly over-collateralized loans is barely scratching the surface. Over-collateralized loans are quite small in traditional finance, and we think the bigger pies. The ones we are more bullish on, are bringing a more traditional financial product to blockchain and offering these solutions to the mass who previously has no easy access to good financial system. This will be truly game-changing.

#### Where can we go to learn more?

Official BAND communication channels:
- 🌏 [Website](https://bandprotocol.com)
- 📓 [Blog](https://medium.com/bandprotocol)
- 🔔 [Twitter](https://twitter.com/bandprotocol)
- 🌎 [Announcements](https://t.me/bandprotocolann)
- 🌎 [English Community](https://t.me/bandprotocol)
- 🇨🇳 [Chinese Community](https://t.me/bandprotocolCN)
- 🇰🇷 [Korean Community](https://t.me/bandprotocolKR)
- 🇻🇳 [Vietnamese Community](https://t.me/bandprotocolVN)
