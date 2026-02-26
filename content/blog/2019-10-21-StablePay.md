---
git-date: 2019-10-21T11:06:05+00:00
layout: blog
title:  StablePay
url: stablepay
h1title: "StablePay: DeFi native payment system"
pagetitle: "StablePay"
metadescription: "Doug from the StablePay team talks about building DeFi enabled payment solution for content creators."
category: blog
featured-image: /images/blog/stablepay-og.png
quote: /images/blog/stablepay-quote.png
intro: "Doug from the StablePay team talks about building DeFi enabled payment solution for content creators."
author: Defiprime
tags: ['Interview']
---
Doug from the StablePay team talks about building DeFi enabled payment solution for content creators.

### Hello! What’s your background, and what are you working on?

My name is Doug Molina, I am a software engineer, and I am one of the creators of [StablePay](https://stablepay.io/). Before getting into the crypto/ blockchain space and landing finally on Ethereum development, I used to work in the financial and aerospace industry. Four years ago, I became interested in financial markets and Fintech, and that eventually led me to Bitcoin and Ethereum. I started attending the Ethereum hackathons to dive into the technology fully, and I was fortunate to win two prizes at eth Buenos Aires and eth San Francisco. One of those prizes was for the project that started StablePay.

StablePay is a decentralized platform that enables users to receive DAI or cDAI (Compound DAI) regardless of the source token transferred. Basically, Alice sends ETH or XYZ ERC20 token, and Bob gets DAI, cDAI, or any other token that Bob prefers.

We focus on users that want to receive donations or payments and want to avoid volatility or choose to receive their DAI transfers into a lending protocol like Compound to earn interest on their tokens, all this just by sharing a simple link or a profile that you can customize.

An example of what happens now for content creators is that they share their ethereum address but they do not control how they receive transfers or what tokens people send to them, with StablePay you get a higher level of control on the transfers you receive, without giving up the non-custodial and security aspects that make ethereum such an exciting technology.

![](/images/blog/stablepay/checkout.png)

### What’s StablePay backstory?

The StablePay core team is comprised of experienced software engineers most of us with financial backgrounds, we all come from different countries in Latin America, and currently, most of the team lives in Costa Rica. We had worked together for more than four years and decided to start programming in Ethereum two years ago. We won one of the main prizes in our first ever ETH hackathon in Buenos Aires 2018, and later that year, we attended the ETH San Francisco hackathon.

StablePay was one of the ideas we wanted to build for ETH San Francisco. Our inspiration came when we were thinking about all these tokens in Ethereum and how most of them are used for speculation, we thought that it would be cool to be able to use them to pay online for stuff. The problem was that merchants need to have the option to convert those tokens immediately to a stable coin to avoid volatility. During that time, DAI and DEXes were starting to get established, and the idea came together by joining all these pieces to solve what we thought was an interesting problem. We finished the code during the weekend in the event and validated that the solution was feasible and ended up winning a prize from MakerDao. A few weeks later, MakerDao contacted us to apply for a grant to finish building the project and take it to the mainnet.

Validation on the solution was very early during the build process, we created a simple website describing what we intended to do and started promoting it, a lot of people got interested, we started to get a few subscribers,  partnership calls and requests for integrations, etc. We got some early feedback that helped us with a lot of features, we later added integration for Compound and opened the design for future DeFi integrations, overall that got us to the version we launched recently as a version one.

### What went into building the StablePay?

Building this first version of StablePay overall has taken the better part of a year from conception to working code in testnets, including several integrations with different protocols like Uniswap, Kyber, Maker and Compound and recently concluding the audit process of our contracts to get to a release-ready version of the platform.

![](/images/blog/stablepay/architecture.png)

During the year, we were building StablePay the Ethereum ecosystem has found what we think is product-market fit in the DeFi movement, that impacted our initial design and idea. We had to change priorities and add both Uniswap and Compound that were not part of our initial scope. We were fortunate to have a very flexible design from the beginning that allowed us to integrate new protocols quickly.

![](/images/blog/stablepay/dashboard-detail.png)

Security has been a top concern for us since day one, and we designed into the platform several security best practices like upgradability, adjustable transfer limits, and pausable contracts. The design is non-custodial and tries to account as much as possible for several worst-case scenarios. The other advantage is that our contracts work like a gateway connecting all these protocols and never hold custody of user’s funds. In the event of transfer failure, the user’s tokens are never moved. We think this lowers the attack vector for the platform.

Onboarding users and improving user experience (UX) is an ongoing process for us, we use A/B testing and measure a lot UX aspects of the process to refine our user’s experience, initial feedback has been positive, and we are working on several more wallet integrations and feature improvements. The main technical limitations we are actively working on are adding meta transactions to pay with tokens instead of ether, lower gas costs as much as possible and add recurring donations/payments. Although we are a layer 1 protocol for payments, we think that the platform’s proposition is valuable today for DeFi and Ethereum users, and we are in a good position to make more improvements as Ethereum, and the overall ecosystem evolves.

Handling several protocols and integrations is not an easy task; we are very grateful for the openness and invaluable help we have gotten from all projects, specially MakerDao, Kyber, and Compound. The way the community helps you build cool things in Ethereum is something that keeps us motivated to continue and add value where we can to this ecosystem.

### What’s your business model?

We think that value capture for most dapps is still very much an open question in the ecosystem, and thus, we are exploring several business models in parallel. Right now, StablePay charges a small flat fee on each transfer that is swapped to cover operational costs, but we don’t collect fees on transfers from and to the same token (DAI to DAI, for example). We also have some integrations with partners for fiat off-ramps that earn referral fees. Finally, we can collect fees for executing swaps in our swapping providers like Kyber Network. We launched recently to mainnet and have started to actively onboard users. As we get feedback from them, we will continue to explore more options for business models.

Our target market for our initial version is mainly the content creators in the DeFi ecosystem, each day we see more and more great sources of content like newsletters and podcasts popping up that are just using ethereum addresses to get donations and cannot choose the token they receive those donations in or are not even able to charge in crypto for their content given the current options. We want to focus on building something useful for them first. We think our closest competitors in that segment are options like Coinbase Commerce, BitPay, or the incumbent payment options like Paypal, Stripe, and platforms like Patreon to some degree. We compete even with regular transfers on ethereum, where you can choose to do what we do manually, and it will take you two to three transactions to achieve the same result.

![](/images/blog/stablepay/widget-generator.png)

We think the biggest differentiators for us are the convenience and control you get on what you choose to do with your transfers. With StablePay you can supply to Compound every converted DAI you receive through the platform for example and with our upcoming features you will be able to configure more granular rules like send any transfer that is bigger than 20 DAI to Compound and the rest to your wallet or choose to supply your DAIs to the loan platform with the best interest at the moment. Imagine having that level of control with your bank account and current payment options that is the power of programmable money.

### What’s your position on the regulatory landscape today?

Our platform is open and non-custodial by design. User’s funds are never in our custody at any point in time, and our smart contracts handle all the heavy lifting. In our case, regulations are different from custodial service. As the ecosystem matures, we expect to see more guidelines and rules that will inform what is anticipated of blockchain-based platforms like StablePay.

### What are your goals for the future?

Our immediate goal is to get the feature set to a level where the platform is valuable to our target users. Our roadmap is flexible, but we know we want to add features like support for Multi Collateral DAI,  gasless transfers, recurring transfers from several sources like your CDP, Compound or your available tokens, and setting up different payment sources and options.

### What are your future thoughts for the DeFi market?

We think that cryptocurrencies are here to stay, there is no going back now that the cat is out of the bag, these open systems will drive a lot of innovation and bring to question a lot of our current paradigms. Living in Latin America, we understand first hand the power of open, censorship-resistant,  programmable money. This ecosystem will bring more and more users as the use cases and benefits become more apparent to mainstream users.

As StablePay our vision in DeFi is for users to subscribe to content creators with a set and forget type of system like we see in online services like Netflix, Amazon Prime, etc., in essence being able to use their tokens for accessing more services, regardless of how or where their tokens are held. Bringing these kinds of facilities to the DeFi ecosystem is our primary goal, and we believe it is the next step for activating a new and better type of economy.

### Where can we go to learn more?

Our website is the best source to get our latest news at [stabepay.io](https://stabepay.io), we also publish content on medium [here](https://medium.com/@stablepayio), and you can also follow us on twitter [@StablePay](https://twitter.com/StablePay).
