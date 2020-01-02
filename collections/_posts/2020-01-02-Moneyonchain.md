---
git-date:
layout: blog
title:  Money On Chain
permalink: moneyonchain
h1title: "Money On Chain - a Stable Asset Platform"
pagetitle: "Money On Chain - a Stable Asset Platform"
metadescription: "Max, the co-founder of Money On Chain, shared the story of building a stable asset platform using RSK"
category: blog
featured-image: /images/blog/moneyonchain-og.png
quote: /images/blog/moneyonchain-quote.png
intro: "Max, the co-founder of Money On Chain, shared the story of building a stable asset platform using RSK"
author: Defiprime
---
Max, the co-founder of Money On Chain, shared the story of building a stable asset platform using RSK.

### Hello! What’s your background, and what are you working on?

My name is Max Carjuzaa, Co-founder of [Money On Chain](https://moneyonchain.com/). I have been programming since I was twelve years old, and I graduated with a degree in software systems. I’ve worked very close to technology, software, and finance all my life. My previous experience with crypto is mainly in payment systems and financial services.

I found out about Bitcoin in mid-2009 researching distributed applications. I got to know Bitcoin and what Bitcoin mining was at the time when you could only mine with your wallet. Back then, there were no mining pools, there were no exchanges, and bitcoins did not have a monetary value. At that time, I researched it from a technological point of view, and like most people who come to Bitcoin, what I thought at that time was that the blockchain was a great invention, but that bitcoins were “not backed” so I discarded it.

I rediscovered Bitcoin in late 2011 after it had reached its first $33 bubble and then dropped to $2 per BTC. I told myself, “These people are paying real money for these worthless digital tokens.” I began to investigate the reason why people were giving value to this. So I started to study a bit about the history of money, some schools of economic thought like the Austrian School.  Finally, I reached the “aha” moment with Bitcoin. From that moment on, I was fascinated with this technology and the possibilities that Bitcoin generates for humanity. In 2013, I began to give some talks at universities about this technology, and I started to spread the word in Argentina. In 2013, I also set up a small Bitcoin mining operation with some investors. With that company, we did quite well, but it was short-lived. We quickly realized that the Bitcoin mining industry was going to change, and that small mining operations were not going to be very profitable.

The real business was in designing, building, and selling technology to the miners, a market that was dominated by Bitmain for a few years.

Back in 2013, also with Alejandro Bokser, who is currently the CTO of Money On Chain, we developed an exchange. The reality is that that exchange never saw the light of day for two main reasons: at that time, it was impossible to open a bank account in Argentina for a Bitcoin exchange, and we felt that the technology was still very immature on security issues. I continued working as a consultant for a university and a telecommunications company on problems closely related to technology until I decided to build Money On Chain. Money on Chain was created to fit some undeniable Bitcoiners’ needs, like stability to trade and a way to earn an income on your Bitcoins without being exposed to counterparty risks.

Money On Chain is a stable asset platform that issues stable currencies backed with crypto. We understand that Bitcoin is great, but for many uses, it has the problem of volatility. We solved that problem by implementing smart contracts using [RSK](https://www.rsk.co/) technology.

Backed by Bitcoin, the protocol is comprised of four tokens that provide several use cases for Bitcoin holders, including leveraged Bitcoin operations. The first token is the Dollar on Chain (DOC). Users can quickly send and receive any amount of DOC - a token pegged to the value of the US Dollar. The second token is BitPRO (BPRO), and it is specifically designed for Bitcoin holders to earn passive income on their coins. BPRO holders have several streams of revenue: they receive a percentage of platform-collected fees, an interest rate, and a small leverage on the price of Bitcoin. The third token is the BTC2X, which is a token for traders wishing to go 2x long in the price of bitcoin. The Money On Chain (MoC Token) is a fourth token. It is designed to govern the decentralized autonomous organization (DAO), and can also be used to pay fees for the use of the platform at a lower rate than those to be paid with BTC.

{% youtube “https://youtu.be/SM7EyR3kXz8” %}
_Introduction to Money On Chain_

### What’s Money On Chain backstory?

The idea of creating Money On Chain came up of necessity. In 2015, I started thinking that what Bitcoin and the ecosystem needed to keep growing was a stablecoin with Bitcoin as collateral. I imagined a world where transactions were instant, cost-efficient, and free from the volatility of the current cryptocurrencies markets. Furthermore, I wanted international trade to be frictionless, so individuals and companies could use the Bitcoin blockchain without facing volatility risks. For that vision to happen, we need to bring stability to the Bitcoin world. We want the best of both worlds: decentralization, security, the immutability of Bitcoin, and the stability of traditional fiat.

Why are stablecoins needed? People and businesses are not used to thinking and trading in “Satoshis,” and we don’t foresee this changing soon. And there is a little chance that “hyperbitcoinization” is coming anytime soon. For the use of Bitcoin in everyday transactions, stablecoins are our best bet.

[The idea of a Stablecoin](https://medium.com/moneyonchain/argentinas-volatility-inspires-a-bitcoin-collateralized-stable-coin-fd411040d1f8) might not make much sense for someone living in the crypto world in “stable currency countries” such as Europe or the US. But since Money On Chain’s Founders are Argentinians, we have lived through hyperinflation in our childhood. Just last year, we “enjoyed” a 50% annual inflation in our local currency. So we tend to appreciate currency stability. We know that the USD also has a yearly depreciation, but for the average Argentinian, the USD is quite hard currency. We know that volatility and instability destroy economies. Stablecoins are a necessity for the crypto world to evolve.

The other thing that normally people tell us is: “If you want to hedge against volatility, you can exchange for dollars in an exchange, or for a Stablecoin backed by dollars in a bank account”. But when you and your family’s savings has been taken by different governments several times in your life, even savings in bank accounts in international and well-respected banks, you develop a tendency not to trust financial and government institutions. So, a software protocol for a Bitcoin Collateralized Stablecoin, back by Bitcoin, really makes a lot of sense to us.

When we first started thinking about all this, there was no way to do it. Today there are many stablecoins with Ethereum or fiat as collateral. But we believe that the volatility and the monetary characteristics of the collateral are essential. If we were going to make a stable currency in the crypto world, the stablecoin needed to preserve those characteristics of decentralization, and the collateral needs to have a clear monetary policy and be censorship-resistant.

Considering the characteristics that such stablecoin required, we waited for Roostock (now [RSK](https://www.rsk.co/)) to become a reality. [RSK was the only network](https://medium.com/moneyonchain/why-we-chose-rsk-601f972a5e30) that allowed us to generate smart contracts with Bitcoin as collateral.

### What went into building the Money On Chain?

When we started, our dream was to find a financial model that will allow us to solve the volatility problem of the price of Bitcoin in a decentralized way. That dream was there revolving within our heads for about a year until the first mathematical model that could solve the problem emerged. While the initial idea of a Bitcoin Collateralized stablecoin was older, the core team of Money on Chain was formed in January 2018. We worked to improve and evolve the model for another year. And once we had the mathematical model, we did the review with financial consultants, [we wrote a paper](https://moneyonchain.com/whitepaper/), and formal verification of the mathematics behind it. Then we made a prototype, and we built a simulator, we made a formal code verification and then we decided to implement it in the blockchain. The truth is that there was a lot of research work on this project until it became a reality.

We started testing the protocol in the RSK testnet in January 2019. After eleven months of simulations, testing, and two audits, we launched Money On Chain on the RSK [mainnet](https://moneyonchain.com/mainnet/) on 12th December 2019.

Currently, we’re finalizing audits on a Token Decentralized Exchange (TEX) that might be needed for bringing liquidity to the system in certain circumstances. Soon we will release the MOC token, which is needed for decentralized governance of the platform. And we are working on the next version of the platform that will bring new features and enhanced mechanisms.  

The cryptocurrency landscape has evolved tremendously while we’ve been building the protocol. When we started working on the Money On Chain project, MakerDao was not yet well known. We first heard of MakerDao from [Franco Amati](https://imtconferences.com/franco-amati/), a well-known bitcoiner in Latam (co-founder of the [NGO Bitcoin Argentina](https://www.bitcoinargentina.org/) and also of [Labitconf](https://www.labitconf.com/)), a good friend and project advisor. Franco told us about it a few months into developing Money on Chain. That is to say, the DeFi ecosystem did not exist just two years ago. When we told our friends in early 2018 that we were going to develop a decentralized Stablecoin using Bitcoin as collateral, using RSK smart contracts, even the most active Bitcoin supporters looked at us with a strange face. One of our advisors of the mathematical and financial model told us for many months that the problem was impossible to solve. Today, he is co-author of the white paper, and he has validated the financial model behind it.

Nowadays, DeFi is starting to gain traction and attention, with many ideas and projects developing every day, and bringing innovation into the crypto ecosystem.

During the last two years, we have been working together with the RSK team, which has helped us much. The advice of “Dieguito” Gutiérrez Zaldívar (CEO and co-founder of IOVLabs, the organization leading the development of RSK, RIF, and Taringa platforms), was precious for the project. And Dieguito leads an incredible team at IOV Labs that is helping us on many fronts, connecting us with their vast network of organizations and communities within multiple industries.

We also work with companies with extensive experience in smart contracts and security audits, such as [ATIX Labs](https://www.atixlabs.com/) and [Coinfabrick](https://www.coinfabrik.com/), which helped us accelerate the development of the project.

### What’s your business model?

[Our solution](https://moneyonchain.com/solution/) provides tokens for a wide range of individuals, depending on their risk appetite. The Dollar on Chain (DOC) is a stable token that will be pegged to the US dollar with a value of 1 USD  per DOC. This makes it ideal for individuals who are averse to the volatility risk of Bitcoin and seek stability in the volatile cryptocurrency environment.

The BitPro (BPRO) token is a token designed for Bitcoin holders. It absorbs the unwanted Bitcoin volatility from the DOC and sells it to the BTC2X. The BTC2X is a token for traders wishing to go 2x long in the price of bitcoin. The traders pay interest for those long positions, and that interest goes to the BitPro, the BitPro also earns a percentage of platform fees and receives a subsidy in the form of MOC token.

The Money On Chain (MoC Token) is a fourth token. It is designed to govern the decentralized autonomous organization (DAO), and can also be used to pay fees for the use of the platform at a lower rate than those to be paid with BTC. MoC holders will also be able to get a reward for staking and providing services to the platform. MoC token holders will vote on contract modifications and new features. On a basic level, the DAO decides whether or not to update the code of the smart contract. The platform will also offer a fifth service, the TEX (Token exchange). It will allow swapping any token in the RSK blockchain in a decentralized way.

![](/images/blog/moneyonchain1.png)

In a second phase, the project plans to implement the stablecoin collateralized by Bitcoin in products on the retail market and launch the Euro on Chain, the Real on Chain, the Peso Mexicano on Chain, etc., which will be linked to different fiat currencies, with collateral in Bitcoin.

There are many other exciting projects we are jointly collaborating with IOV Labs and other partners such as Coinfabrik. Our approach and strategy are not to compete against the crypto ecosystem, but to work with. We invest our resources in new ideas, but also existing projects that must be modified so that they can grow and/or last over time.

### What’s your position on the regulatory landscape today?

What is needed is regulatory clarity. Regulators must sit down to talk about this matter, decide what they are going to do about it, and do it. But it is also vital that regulators are informed that they work together with organizations, NGOs, and companies to reach decisions that are logical and that are useful to the whole world. Regulators should not be afraid of this industry, which can bring tremendous efficiencies to the economies of so many countries and which is a huge opportunity to improve the lives of billions of unbanked around the world.

### What are your goals for the future?

Our goal is clear, and we are building a stablecoin with no counterparty risk to bring real usage to Bitcoin and to change the lives of billions with financial tools. Imagine a self-employed Argentinean designer selling their work to a company in Europe or a programmer in India selling their work to someone in Chile. There is still a lot of work to do on the technological side. We are working with other projects to build the infrastructure to onboard millions; in the meantime, we are already working with some NGOs so they can use the DOC to improve the efficiency of their money flow.

We do not see roadblocks, save for regulatory, and we firmly believe that regulators will work successfully with the industry to release the power of this technology that can bring prosperity to so many people in the undeveloped world.

### What are your future thoughts for the DeFi market?

Bitcoin has grown exponentially since its inception. [We think Bitcoin could provide a more secure foundation upon which to build DeFi applications](https://medium.com/moneyonchain/everything-you-need-to-know-about-defi-on-bitcoin-8efffdba90b0). Projects today are exploring different sidechains to create Bitcoin-based smart contracts. They could enable asset-issuance, stateful smart-contracts, scaling, faster settlement finality, and higher privacy.
Liquid, an inter-exchange settlement network linking together cryptocurrency exchanges and institutions around the world, is an excellent example of DeFi on the Bitcoin blockchain, that enables faster Bitcoin transactions and the issuance of digital assets. Money On Chain has already developed a stable asset-backed by Bitcoin on RSK (a bitcoin sidechain). Now there are discussions of integrations between RSK, Blockstream’s Liquid, and the Lighting network, so assets are portable/tradable on the different networks.

### Where can we go to learn more?

- Website: [https://moneyonchain.com/](https://moneyonchain.com/)
- Twitter: [https://twitter.com/moneyonchainok](https://twitter.com/moneyonchainok)
- Telegram: [https://t.me/MoneyOnChainCommunity](https://t.me/MoneyOnChainCommunity)
- Youtube: [https://www.youtube.com/channel/UCrLzfY2gl9iIkawqMOJlODQ](https://www.youtube.com/channel/UCrLzfY2gl9iIkawqMOJlODQ)
- Medium: [https://medium.com/moneyonchain](https://medium.com/moneyonchain)
- Reddit: [https://www.reddit.com/r/MoneyOnChain/](https://www.reddit.com/r/MoneyOnChain/)
