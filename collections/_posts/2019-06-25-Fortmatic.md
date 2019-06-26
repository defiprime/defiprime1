---
layout: blog
title:  "Fortmatic"
permalink: fortmatic
h1title: Interview with Fortmatic co-founder Sean Li
pagetitle: Interview with Fortmatic co-founder Sean Li. Fortmatic Review.
metadescription: Fortmatic co-founder, Sean Li talks about building an SDK that enables users across the globe to interact with dApps using just their phone number.
category: blog
featured-image: /images/blog/fortmatic-og.png
quote: /images/blog/fortmatic-quote.png
intro: Fortmatic co-founder, Sean Li talks about building an SDK that enables users across the globe to interact with dApps using just their phone number.
author: Defiprime
---
Fortmatic co-founder, Sean Li talks about building an SDK that enables users across the globe to interact with dApps using just their phone number.

## Hello! What's your background, and what are you working on?

Hi! I’m Sean Li, co-founder, and CEO of [Fortmatic](https://fortmatic.com/). During my years of study at the University of Waterloo, I became fascinated by the topics of HCI, security, and distributed systems - which led to me developing a knack for making sophisticated technology more comprehensible.

After I graduated, I started a company called Kitematic with my classmates, which made Docker containers accessible to developers on Mac and Windows when it was predominantly Linux. Shortly we were acquired by Docker and during my years there, I was extremely fortunate to work closely with the founder and the amazing staff engineering team to deliver the next embodiment of Kitematic, Docker Desktop, which became the de facto-way for developers to interact with Docker on the desktop, and acquired over millions of monthly active users. I experienced the rapid scaling of a startup from around 50 people to over hundreds, as well as navigating the ups and downs of a complex yet vibrant open source ecosystem.

From this experience, I naturally gravitated towards _another_ complex yet vibrant [open source ecosystem - Ethereum](/ethereum), and the broader blockchain ecosystem in general. I was blown away by its implication on finance, economy, politics, as well as technology - interweaving centuries of knowledge on money and humanity. I was bewildered and decided that I _have_ to be involved - I left Docker and started building and experimenting with a few dApp projects.

It was too early - at the time, there weren’t much mature infrastructure and tooling to rely on. The only gateway available for users to interact with the Ethereum blockchain was [MetaMask](https://metamask.io). Despite it striking a note with the early crypto community and became ubiquitous across dApps, I feel trade-offs need to be made regarding key management and usability - an obvious pain point that needs to be addressed for mainstream users to interact with the blockchain.

I aspire to build a solution that strikes the right balance by adopting a pragmatic mindset and work closely with our customers & partners. Therefore, with the help of my co-founders Arthur and Jaemin, we started [Fortmatic](https://fortmatic.com/), building an SDK that enables users across the globe to interact with dApps using just their phone number, without requiring any extra installation, by abstracting away many blockchain-specific facets around key management for users such as the recovery seed phrase.

![](/images/blog/fortmatic1.png)

To date, some well-known integrations with the Fortmatic SDK include dApps like [TokenSets](/tokensets), Cent, Radar Relay, Zerion, and Fulcrum - with Fortmatic enabling over 65% new interactions from users on mobile web browsers!

![](images/blog/fortmatic2.gif)

## What's Fortmatic backstory?

The source of conviction to found Fortmatic came from the extreme pains felt as dApp developers ourselves early in the ecosystem, and a solution like Fortmatic was something we wish we had back then. We validated our idea by prototyping an initial solution with our key management model and shared them with developers and advisors we knew, the response was very positive, so we went ahead and raised venture capital from top firms in the valley to quickly bring this to market.

I’m very proud of the team we’ve built at Fortmatic. I contribute my past experience building well-crafted products that touches by millions of developers, and being part of the wild ride of a rapidly growing startup from validation to growth. My co-founder Arthur brings in his infrastructure prowess from Yelp, shipping critical data platforms for partners that requires availability, privacy, and security.

My co-founder Jaemin brings in his expertise working at Uber business payment platform and fraud prevention. We’ve formed a solid core, and almost a year later, we’ve grown to a team of over ten people, with experience working at top companies such as Docker, Google, Amazon, Apple, Yelp, Uber, and Accenture.

## What went into building the Fortmatic?

If a dApp already works with MetaMask, it’ll only take a couple lines of code to integrate Fortmatic by swapping web3 providers. The simplicity around our developer on-boarding and user experience is a product of the team's tremendous amount of hard work. Iterating with and supporting developers, building great product experiences and key management infrastructure together are already ambitious endeavors, let alone also having to make sure Fortmatic works with every common web3/ethers.js method, versions, and browsers.

Despite the challenges, the passion and dedication of the team were able to get us from zero to our initial mainnet launch in 6 months, when we had our first public debut at Ethereum Denver conference going out of stealth.

![](/images/blog/fortmatic3.png)

The cryptocurrency/blockchain landscape has drastically changed as we were building our product - from fanatic optimism to nuclear winter. Generally, the maturation phase after the mania around pure speculation on price had died down has been perceived as beneficial to the overall ecosystem. The increase in rationality and risk aversion led to companies becoming more realistic, pragmatic, and focusing on delivering tangible value to customers and users to fuel growth, which had empowered the business Fortmatic is in - to help our dApp customers grow and reach more users.

As our approach is getting validated by iterating with our partners and customers, we progressively upgrade our technology and infrastructure. We started Fortmatic by leveraging what we knew to build an HSM backed secure enclave on AWS which we do all of user key management in, providing account recoverability and enough security assurance for storing relatively smaller amounts of assets (what users will be comfortable with storing on MetaMask).

After on-boarding a few notable integrations, we started to invest more heavily in improving our approach, working with multiple security agencies continuously running blackbox and whitebox penetration testing programs, and have recently passed our SOC 2 Type 1 security audit, which is also acquired by industry leaders like Gemini and Coinbase, as well as becoming insured against cybercrimes.

On top of all of this, we can’t get to where we are without our early partners. They’ve been like family, believed in us and in bringing the best possible UX to blockchain. They are patient with us and continuously helping and supporting us with invaluable advice and feedback on making Fortmatic even more successful.

## What's your business model?

We’re in the business of helping dApps reach more users and encourage more engagement - bringing users from different mediums (including desktop & mobile web browsers), different demographics, and different levels of familiarity with blockchain into the Ethereum dApp ecosystem.

At the moment we are not charging partners and developers for using Fortmatic but instead focused on growth, working with them to perfect our product before locking down a reasonable pricing model for both ourselves and our partners and developers as we provide even more value-add within our platform.

## What are your goals for the future?

We’ll be doubling down on growth, and working with our partners and developer community to provide the best possible web3 authentication experience. We have many exciting projects in the works too - to name a few: 2FA authenticator integration (address SIM porting concerns for higher stake users), fiat-onramp, gas subsidy, and L2 integrations. We’ll also soon be open sourcing our Javascript SDK and sharing more content and updates about security at Fortmatic!

## What are your future thoughts for the DeFi market?

We are _thrilled_ by the developments around DeFi. Since earlier this year, DeFi has amassed an incredible amount of momentum and the maturation of many financial primitives, such as borrowing, lending, exchanging, sets, and more. These have been the fundamental building blocks that the more complex tradition financial systems are built on - except now, any developer can create a financial products by composing these primitives and have the digital assets accessible globally to anyone in the world!

All of this is also possible without middlemen, in a fully transparent and auditable manner, compared to everything happening behind closed doors with an extremely high barrier of entry. This is a huge deal and disrupts moats around finance, which is an inevitable evolution for a more efficient, open, and versatile financial system.

## Where can we go to learn more?

- [Website](https://fortmatic.com/)
- [Developers Documentation](https://developers.fortmatic.com/docs)
- [Twitter](https://twitter.com/fortmatic)
- [Medium](https://medium.com/fortmatic)
- [Discord](https://discord.gg/JqrDbRB)
