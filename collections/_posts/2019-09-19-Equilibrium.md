---
git-date:
layout: blog
title:  Equilibrium
permalink: equilibrium
h1title: 'Equilibrium - framework for generating asset-backed EOSDT stablecoins'
pagetitle: 'Equilibrium - framework for generating asset-backed EOSDT stablecoins'
metadescription: 'Alex Melikhov shared his thoughts on stablecoins and DeFi and told us the backstory of building the first crypto-backed stablecoin based on the EOS blockchain.'
category: blog
featured-image: /images/blog/equilibrium-og.png
quote: /images/blog/equilibrium-quote.png
intro: 'Alex Melikhov shared his thoughts on stablecoins and DeFi and told us the backstory of building the first crypto-backed stablecoin based on the EOS blockchain.'
author: Defiprime
---
Alex Melikhov shared his thoughts on stablecoins and DeFi and told us the backstory of building the first crypto-backed stablecoin based on the EOS blockchain.

### Hello! What's your background, and what are you working on?

Hi, I'm Alex Melikhov, CEO and founder of [Equilibrium](http://eosdt.com/?utm_source=defiprime&utm_medium=referral&utm_campaign=defiprime_interview). Right now, we are developing an industry-leading DeFi framework. To tell you a bit about my background, I am an engineer in applied mathematics by training and a Fintech entrepreneur by a soul.

My friend told me about Bitcoin back in 2011, but I only took it seriously in 2014 when Ethereum's concept of smart contracts caught my eye. At the time I was building payment gateways, and the opportunities offered by decentralized smart contracts blew me away. Along with that, cryptocurrencies were gaining more widespread adoption, and the freedom of an emerging crypto financial system had become more obvious.

As such, I decided to pivot my focus from traditional banking systems to crypto. I then went on to co-found my first crypto business in 2015. Changelly has become one of the biggest instant crypto exchanges on the market.

### What is EOSDT?

EOSDT is the first decentralized stablecoin launched on the Equilibrium framework, based on the EOS blockchain and pegged to the US dollar. EOSDT enters circulation when users lock up their EOS holdings in a smart contract as collateral. One of EOSDT's key characteristics is its high-end collateral transparency. Stablecoin minting requires transparency, and we believe that real digital assets must be trackable within a smart contract. Therefore, every EOSDT transaction is registered on the blockchain and anyone, at any time, can inspect the underlying collateral pool in real-time.

![](/images/blog/equilibrium2.png)

The exciting relevance of these stablecoins is based on a wide range of use cases. It can be used as a tool for risk hedging as a part of various crypto trading strategies, from margin trading to [pyramiding](https://www.investopedia.com/terms/p/pyramiding.asp), and, excitingly, it has serious potential as a means of payment. One of the most popular scenarios to date is leveraging your EOS holdings. Recently, we have also added support for the REX market and are now seeing large EOS holders transfer their tokens from REX where they used to receive a passive income to EOSDT. With us, they have the same passive income as before, thanks to our REX revenue distribution mechanism for collateral holders.

I see much broader market opportunities for DeFi businesses willing to adopt such a powerful framework. We are designing the Equilibrium framework as an intuitive environment for creating advanced DeFi products that can make use of the out-of-the-box, liquid stablecoins, and other framework's modules. There are actually quite a few variants of stablecoin applications for DeFi services that create plenty of room for new business models. Without even exaggerating, it's a whole new industry that will be built on top of the current crypto market.

### What's EOSDT's backstory?

When we co-founded the Changelly exchange in 2016, stablecoins were just a pilot conception not visible enough on the market. 2017 revealed their fast-growing popularity with the giants like Tether, who rapidly occupied its large market share, proving the concept is promising and reliable. But until 2018, the stablecoin market was a market of USDT although we saw its massive potential for trading, leverage, and other exchange operations. I remember we lacked highly transactional and transparent stablecoins for that purposes. The market already had some other popular centralized stablecoins, but there was a lack of truly decentralized ones. I saw that some projects were ignoring the nature of stablecoins that required a transparent and robust collateral model, the absence of which causes a lack of faith in the system as a whole.
On the other hand, we saw a gap within the emerging EOS ecosystem for stablecoins that met these characteristics. Both the EOS currency and community are rapidly gaining market share by presenting new opportunities like the REX market and decentralized governance, along with demonstrating notable tech advantages in comparison to other blockchains. So, we ended up with EOS as the platform for EOSDT and started with EOS cryptocurrency as the first liquid digital asset to back the stablecoin.

I think that our fast growth was a strong signal that the concept was working. We launched in April 2019 as a fully functioning product, and now, with 4.8 million EOS in digital assets under collateralization, worth roughly $16 million USD, EOSDT is the fastest-growing stablecoin on the EOS mainnet and the biggest EOS-based DApp in terms of EOS balance today.

![](/images/blog/equilibrium1.jpg)

My team of software engineers and financial specialists have been focusing on decentralized finance applications for the past three years. Before this, we gained a lot of experience building a lending platform on Ethereum. Now we are developing on top of EOS, which we consider as a much more user-friendly and scalable blockchain.

Decentralized finance is one of the most promising industries in the crypto market, and the track records of existing stablecoins have already shown the public's demand for such products. Throughout 2019 the stablecoin market share tripled, and the daily trading volumes of USDT is now more than that of Bitcoin. We believe that the next step is to incentivise the community to start building DeFi products by leveraging the advantages of decentralized crypto-backed stablecoins within their dApps. This market has enormous potential.

### What went into building EOSDT?

We were the very first team to build a decentralized stablecoin framework on top of EOSIO, and we decided to forge ahead and release the full-scale product ourselves. As you probably know, there are a lot of hurdles in making a stablecoin project live, no matter what blockchain platform you use. According to the latest [Blockdata research](https://download.blockdata.tech/blockdata-stablecoin-report-blockchain-technology.pdf), since the start of 2017, 134 stablecoin projects have been announced and are still under development.

We have been designing the Equilibrium framework from October 2018 until March 2019 and have just launched it this April. The development stack was reasonably straightforward. It included C++ for smart contracts and a popular stack on the frontend side (React.js/Redux and TypeScript). There were some tasks implemented on the backend (.Net Core, Node.js, TypeScript, and PostgreSQL).

Our main product is a framework of smart contracts whose fundamental characteristics are safety-orientated. We were among the first to validate the approach of decentralized control of the smart contracts. Nonetheless, one of the most severe problems arising from smart contract design is the security audit. The debugging tools on the market for smart contracts are insufficient. For example, it would be great to have the ability to replay a test blockchain back to the state when the debugged transaction was executed and re-execute its code line-by-line again. That would make it easy to track down errors, implement necessary fixes, and protect all the similar transactions from new code errors. This is technically possible, but no tool exists today to facilitate this process.

In the absence of an adequate means of auto-testing and security analysis, it's common to see security audits performed manually. We used unit tests and comprehensive integration tests for these purposes and partnered with smart contract auditors. For example, we recently worked with [EOS42](https://eos42.io/), also known as "the guardians of the EOS blockchain," given their status as pioneers of EOS mainnet security. Worth mentioning that Equilibrium Lab, our R&D arm, also performs cybersecurity audits for EOS smart contracts with respect to our extensive dev experience.  

Partnerships are also an important part of the development process, given that we are building this community-driven project together with the community. So, for example, we worked with [EOS Authority](https://eosauthority.com/) who helped us to implement a seamless integration with REX, and now we are working with [LiquidApps](https://liquidapps.io/) on integrating their LiquidOracles service in order to diversify price feeds for our framework.

### What's your position on the regulatory landscape today?

The theme of regulation is one of the most important when it comes to building a successful stablecoin framework. Without regulatory certainty, public adoption and real-world implementation are simply impossible. Over the last year, we have spent a lot of time analyzing, from a legal perspective, the regulatory status in various jurisdictions for fiat-backed stablecoins. The universal conclusion was that it is a minefield of regulatory issues as these types of stablecoins are, in almost all cases, some kind of financial or regulated instrument, most notably an instrument that qualifies as "electronic money."

When we were building the Equilibrium framework, we wanted to build it with regulatory certainty. I think the best way to look at stablecoins is that they have an inherent utility — they're a volatility-neutral source of value. This is extremely important when it comes to cashing out of crypto positions, hedging activity, and day-to-day transactions via blockchain networks. They're just as crucial as the volatile crypto assets they trade against.

So, our main target was to validate this concept with regulators' expectations in mind. It took a lot of time going through all the technical aspects of the framework, to prepare all of the documentation, all interlinking concepts, and technology. We were delighted to get a good result - Equilibrium recently obtained a legal opinion in the US that sees both EOSDT & NUT as utilities that are unregulated in their nature.

### What are your goals for the future?

We have been building a development environment for decentralized stablecoins, synthetic assets, and DeFi products to thrive in all the while keeping an open-source approach. At the first stage, we have released a reliable stablecoin on top of our technology infrastructure, which allows for its locked assets to be financially productive. It definitely holds many advantages, including accelerated adoption by the community and rapid detection of bugs and vulnerabilities.

Because of this, the majority of our upcoming DeFi products will be open-source, and quite a few of them will be available for the developer community to advance these products. We will soon present the community with several wireframed, open-source product prototypes that anyone will be able to take ideas from and build on.

Additionally, we are launching a milestone grant program to support developers building DeFi products on top of the Equilibrium framework. Grant sizes will be up to $100,000 worth of our NUT (Native Utility Token, the framework's governance, and internal currency utility asset). They can apply for grants on our website.  

### Where can we go to learn more?

We have a very friendly [Telegram chat](http://t.me/equilibrium_eosdt_official?utm_source=defiprime&utm_medium=referral&utm_campaign=defiprime_interview) where you can get all your questions answered, as well as a [Medium blog](http://medium.com/equilibrium-eosdt?utm_source=defiprime&utm_medium=referral&utm_campaign=defiprime_interview) where you can find the latest news on Equilibrium and EOSDT. Finally, there's our website [eosdt.com](http://eosdt.com/?utm_source=defiprime&utm_medium=referral&utm_campaign=defiprime_interview) where you can generate your own EOSDT.
