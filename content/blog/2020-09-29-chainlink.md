---
git-date: 2020-09-29T16:09:02-07:00
layout: blog
title:  "Chainlink"
url: chainlink
h1title: "Chainlink"
pagetitle: "Chainlink - Interview with Adelyn Zhou"
metadescription: "Adelyn Zhou shared Chainlink Network backstory and future goals, and how Chainlink going to build truly chain-agnostic oracles"
category: blog
featured-image: /images/blog/chainlink-og.png
intro: "Adelyn Zhou shared Chainlink Network backstory and future goals, and how Chainlink going to build truly chain-agnostic oracles"
author: Defiprime
tags: ['Interview', 'Infrastructure']
---
Adelyn Zhou shared Chainlink Network backstory, future goals, and how Chainlink going to build truly chain-agnostic oracles.

### Hello! What's your background, and what are you working on?

My name is Adelyn Zhou, and I’m the CMO of [Chainlink Labs](http://www.chainlinklabs.com) where I lead Chainlink marketing.

Throughout my career, I’ve taken emerging technologies and made them accessible and relevant to our everyday lives. Previously, I helped enterprises integrate machine learning to improve business results, co-authoring a best selling book on applications of artificial intelligence along the way. After entering the blockchain space, I’ve been striving to make Chainlink’s open-source oracle technology the leading solution powering Defi and the building towards the decentralized world.

At Chainlink, we build bridges between blockchains and the real world by solving [the oracle problem](https://blog.chain.link/oracles-the-key-to-unlocking-smart-contracts/). Developers can trust that a smart contract running on Ethereum will execute as written because its logic is secured by thousands of nodes. However, if a contract relies on an external data source -- say, [the price of gold](https://feeds.chain.link/xau-usd) -- it immediately introduces two obvious attack vectors: at the data origin layer and at the oracle layer. Chainlink allows for the decentralization of both data sources and oracle node providers, allowing for an externally connected smart contract to remain end-to-end secure.

Today, Chainlink’s oracles are live on Ethereum mainnet where they secure over $3 billion USD in value for lending protocols, synthetic asset platforms, [asset tokenization](/assets-tokenization) projects, and other leading teams in the DeFi space and beyond. Prior to Chainlink, smart contracts were largely limited to tokenization. By securely accessing real-world data, we believe smart contracts can truly begin to replace all other forms of digital agreements.

### What's the Chainlink backstory?

Chainlink’s co-founders, Sergey Nazarov and Steve Ellis, have been working on the oracle problem for over half a decade, well before it was on many developers’ radars. They realized very early into the first wave of smart contracts that without oracles, many of the most exciting use cases -- insurance, supply chain, derivatives, decentralized marketplaces -- either couldn’t function, or would have to remain trusted at some layer.

Chainlink’s growth and design also benefit from a long history of collaboration with the world’s leading academic and security research teams. For example, Ari Juels, the former Chief Scientist at RSA and the founder of Cornell’s IC3, is Chainlink Labs’ Chief Scientist leading our [research team](https://chainlinklabs.com) in pioneering the furthest reaches of the oracle frontier.


### What went into building the Chainlink network?

On June 1st, 2019, we launched our first oracle price feed live on Ethereum Mainnet. We decided to focus initially on price feeds based on user demand: price feeds are crucial for DeFi protocols like Synthetix and Aave, two users who went live and have been consuming our data for almost a year.

We’ve continued to expanded our oracle data offering in a variety of ways: we’ve added dozens of cryptocurrency pairs, multiple commodities feeds, stock index feeds, and FX pairs; we’ve onboarded dozens of new Chainlink Node Operators; we’ve set the standard for [data quality](https://blog.chain.link/the-importance-of-data-quality-for-defi/) by deploying some of the best and most reliable data providers in the space.

This work and the relationships we’ve built have allowed us to streamline our processes; now we can spin up a new price reference feed and bring on a project in a few days. On our [ETH/USD](https://feeds.chain.link/eth-usd) feed, for example, integration requires a single line of code: by connecting a contract to the Ethereum address in the upper left of the feed visualization, you can connect with the latest ETH/USD price. As of today we’re proud to say we have more than 40 live mainnet users -- by far the most in the DeFi space -- with more being announced every week.

This expansion has been mirrored by the explosive growth of the DeFi space in general. A key feature of Chainlink has always been ease of integration. We work to abstract away the difficulty of the oracle problem, allowing projects to focus on their core competencies and develop truly revolutionary products that they can bring to market with a high degree of security and reliability at the oracle layer. We believe that by continuing to expand the types of data readily available for smart contracts, we’ll help push not just adoption of our network but also that of DeFi as a whole.

### What are your goals for the future?

Moving forward, three of Chainlink’s key goals and technical objectives are to scale our oracle networks through an off-chain aggregation technique known as [threshold signatures](https://blog.chain.link/threshold-signatures-in-chainlink/), introduce [economic incentives](https://www.youtube.com/watch?v=A7u8XDkInqE) for node operators, our term for reputational staking, and to become truly chain-agnostic by integrating with a variety of smart contract platforms.

We also have big plans in the work for DECO, the privacy-preserving computation system we recently [acquired](https://www.coindesk.com/chainlink-blockchain-privacy-oracle) from Cornell University. As on-chain contracts and financial products grow more complex, they will need oracles that can accommodate unique needs, particularly access to data that needs to remain confidential. Our acquisition of DECO positions us to continue growing towards the future by allowing smart contracts to use sensitive data in on-chain transactions while keeping that data completely confidential.

We believe that any chain with smart contract functionality needs secure oracles to succeed, and we look forward to providing oracles across the entire blockchain space.

### What are your future thoughts for the DeFi market?

In a recent [interview](https://twitter.com/SergeyNazarov/status/1290432142992760832), Sergey discussed how deterministic smart contracts will become more attractive in a world where trusted, “brand-based” contracts have begun to fail. If we take this hypothetical to its extreme end -- a world where these trusted contracts have failed entirely -- DeFi becomes not just a parallel financial and legal system, but is instead the default standard.

DeFi removes middlemen, reduces transactional friction, and regulates itself, allowing for greater efficiency and access relative to legacy systems. Projecting the upper limits of the space is difficult because a “DeFi Standard” financial world could actually grow much larger than the legacy system due to these increases in efficiency. Compared with the current size of DeFi, that world might seem far away, but it’s what we should be building towards and preparing for. With tools like secure Chainlink oracles, DeFi’s rise and eventual domination is inevitable.


### Where can we go to learn more?

If you’re a developer and want to connect your smart contract to off-chain data and systems, visit the[ developer documentation](https://docs.chain.link/) and join the technical discussion on[ Discord](https://discordapp.com/invite/aSK4zew). If you want to schedule a call to discuss the integration more in-depth, reach out [here](https://chainlink.typeform.com/to/gEwrPO). For more information, check out the [Chainlink website](https://chain.link/) or follow us on [Twitter](https://twitter.com/chainlink) or[ Reddit](https://www.reddit.com/r/Chainlink/).
