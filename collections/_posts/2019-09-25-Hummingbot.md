---
git-date:
layout: blog
title:  Hummingbot
permalink: hummingbot
h1title: 'Hummingbot for Crypto Market Making'
pagetitle: 'Hummingbot - interview with co-founder Carlo Las Marias'
metadescription: "Hummingbot - interview with co-founder Carlo Las Marias. Carlo talks about switching career from Wall Street investment banker to open-source market making bot developer."
category: blog
featured-image: /images/blog/hummingbot-og.png
quote: /images/blog/hummingbot-quote.png
intro: "Carlo talks about switching career from Wall Street investment banker to open-source market making bot developer."
author: Defiprime
---
Carlo talks about switching career from Wall Street investment banker to open-source market making bot developer.

### Hello! What's your background, and what are you working on?

I'm Carlo, COO of [Hummingbot](https://hummingbot.io).  I started my career as an investment banker on Wall Street, ultimately spending 13 years in the industry.  I had roles in debt capital markets, liability management, and FX & rates structuring. I did a tour of the banks: Goldman Sachs, Deutsche Bank, UBS, and Credit Suisse, as well as the globe: New York, London, Singapore, and Hong Kong.  Eventually, I got disillusioned with banking, with increasing regulations, the never-ending chase for the next deal, and the realization that the exotic derivatives trades I was pushing on clients was more to benefit the bottom line of the bank, rather than providing value to the client.  It didn't give me the most fulfilling sense of the impact I'd be leaving on the world.

So I left investment banking in 2014, got the startup bug, and founded a big data, government software startup in Southeast Asia.  I have always been interested in technology, and I earned degrees in both finance and computer science.

I moved to Silicon Valley in early 2017, to throw myself into the center of tech.  I started attending some Bitcoin and crypto meetups.  It was a fascinating time, the optimism of "we can change the world," it's still early, and we're really onto something revolutionary.  For me, it also seemed like the perfect blend of background and interests in both finance and technology; 13 years of investment banking would not go to waste, after all.  So in July 2017, my co-founders and I started CoinAlpha, on the vision of using blockchain and cryptocurrency to revolutionize the world of finance; three DeFi products later, we created Hummingbot.

Hummingbot is an open-source software client that allows users to create and customize automated, algorithmic trading bots for making markets on both centralized and decentralized digital asset exchanges. By lowering these technical barriers and introducing new incentive mechanisms, Hummingbot enables anyone to act as a market maker for digital assets, a new model for liquidity provision that we call decentralized market making.​

![](/images/blog/hummingbot1.png)

Hummingbot was open-sourced in April 2019.  Since then, the Hummingbot discord community has over 1,100 members. There have been over 4,000 unique GitHub clones and Docker downloads, and the code has been forked on GitHub over 100 times.

There are two broad categories of users:
1. Users motivated by trading gains.  The vast majority of Hummingbot users are private individuals, though we are also aware of and working with crypto funds which are using it. These users use Hummingbot as a tool to automate their trading.
2. Users motivated by providing liquidity.  We are aware of some large, prominent token project/issuers who want to provide liquidity for their tokens as well as crypto exchanges (particularly new, smaller ones) that want to support their exchange's order books.

In July 2019, we start an experimental "liquidity bounty" program designed to reward users for using Hummingbot to trade and make markets for specific tokens or exchanges.  Our first such program was for Harmony Protocol in July 2019.  This program introduced a third category of user: members of the Harmony community that wanted to support the project.  In addition to supporting the project, these users, of course, were also capturing bounty rewards.

### What's Hummingbot backstory?

We founded CoinAlpha in July 2017.  Our team combines finance experience from Wall Street execs (Goldman Sachs, JPMorgan), tech startup founders, data science/machine learning engineering (Apple), and blockchain engineering (ConsenSys Academy global hackathon winner), and this was just a team of four.  We were one of the few well-rounded teams able to bridge the tech and finance worlds.

Initially, we launched a quantitative hedge fund and a blockchain-based fund protocol to administer this fund.  Being one of only a few quantitative hedge funds in the market, we naturally received inquiries from token projects/issuers in need of market-making for their tokens.

To give some background, crypto exchanges and token projects spend an estimated $3 billion annually on market making, in the form of rebates, fees, and cost of inventory.

Crypto industry stems from a supply and demand imbalance caused by a structural feature of crypto: anyone can create a token, and anyone can create an exchange where tokens are traded. Today, there are over 5,000 tokens and 300 exchanges, leading to over 35,000 unique markets (trading pairs) across a highly fragmented exchange landscape. These markets compete with one another based on liquidity, which measures how easily people can buy and sell something without losing money due to the bid-ask spread.

Despite a massive increase in the demand for liquidity, there hasn't been a corresponding increase in supply. Liquidity supplied by market makers, a job that requires an inventory of capital dedicated to a particular market, as well as trading software that can rapidly and automatically create and cancel orders in response to fast-moving markets.

Due to these financial and technical requirements, crypto market makers are typically quantitative hedge funds who charge hefty fees and may require millions worth of inventory. These costs can be prohibitive for even the most significant projects and exchanges, while the long tail of smaller projects and new exchanges can't afford them at all.

The need for liquidity was particularly evident in the DEX space.  Market making is already a complicated endeavor; throw in smart contracts and blockchain transactions, the complexity multiplies.  To some degree, the idea of Hummingbot fell into our lap; not many teams had the ability to take on this challenge, but this specifically was in our wheelhouse.  The initial validation: we received a grant as part of the 0x Ecosystem Accelerator Program.

Not long after that, in April 2019, we announced and open-sourced the first version of Hummingbot.  We were immediately inundated with requests from exchanges, crypto funds, DeFi protocols, crypto-traders, developers who wanted to work with Hummingbot.  A high level of interest continues today.  Clearly, we were onto something.

### What went into building Hummingbot?

Hummingbot was an evolution of the technology we had already started building from day 1, in 2017.  As part of the quant fund, we had built trading systems, engines, and integrations to crypto exchanges.  Administering the quant fund using smart contracts already got us engineering products that needed to interact with the Ethereum blockchain.  We had already started laying the foundation for what was to become Hummingbot.

As a company, we made a strategic decision to start working on Hummingbot full time in December 2018.  We released the first closed alpha version of the product in March 2019 and open-sourced the bot in April.  We were able to set up the infrastructure for and launch the first liquidity bounty program in July.

There are many factors that combine to make engineering Hummingbot challenging, mainly related to building for stability when all of the technology it has to interact with is still relatively nascent and unstable (i.e., buggy):
- Each exchange has its own set of APIs and its own idiosyncrasies.  For example, we had a case where an exchange would incorrectly return error messages even though transactions went through; building Hummingbot is to some degree an exercise in debugging the exchanges themselves.
- Blockchain transactions may fail, your orders on a DEX may have been jumped.
- High frequency of transactions: juggling lots of balls in the air, when you never know which one is going to blow up.
Throw in the fact that any error could result in the loss of money, i.e., repercussions for an error are severe.  Hummingbot engineering entails obsessive testing, error-handling, and designing for the unknown and unexpected.

![](/images/blog/hummingbot2.png)

Our challenge for onboarding new users is that Hummingbot is a very technical product.  The ideal setup is to run Hummingbot on a cloud server, using Linux and Docker.  Many of our initial users hadn't used any of these; most were running Windows; most had never used the command line.  The early users who were able to get Hummingbot up and running tended to be developers, folks who already had some degree of technical background.

What helped us overcome this is we were able to build a strong support team, provide comprehensive step-by-step documentation, and create tutorial videos.

Getting users to use these unfamiliar technologies is not a sustainable plan for growth.  Longer-term, we are planning to create a GUI and hosted service to give more users access.  However, in the near-term, we chose to prioritize Hummingbot's core: stability of the trading engine, exchange integrations, and strategies.  Another main priority for us has been in making the software developer-friendly.  Our longer-term vision is to have an active open-source community with many others customizing and contributing to the development of Hummingbot.

### What's your business model?

Our main business model is monetizing through liquidity bounties.  Our target customers are token issuers or crypto exchanges who are looking for an alternative to paying high-cost, professional market makers to provide liquidity for their tokens.  

When we administer liquidity bounties, we collect and analyze user data, run machine-learning-based algorithms to weed out any market manipulation (e.g., wash trading), provide end-user support, and help promote and market participation in the program.

Our first liquidity bounty program for Harmony showed us that with just a limited number of participants, we were able to provide liquidity comparable to professional market makers.

Fundamentally, our main competition is market makers.  After discussing with many token issuers and exchanges, some common gripes became clear: market makers are expensive, require millions in inventory, and operate as black boxes.  In contrast, a Hummingbot liquidity bounty program takes a data-driven approach - rewards are distributed based on tangible results provided by participants, participants use their inventory (not the issuer's), and costs and rewards are materially lower than what an issuer would pay a traditional market maker.

### What's your position on the regulatory landscape today?

Despite recent guidance from the SEC and FinCEN, many crypto-related activities still fall squarely into a gray area.  U.S.-based DeFi companies really have their hands tied; for everything we do, we're constantly consulting our lawyers and the advice we get is never clear.

There are so many other jurisdictions that are more progressive when it comes to crypto, such as Singapore, Estonia, and Malta.  We feel that the regulatory landscape in the U.S. is hampering innovation here and placing U.S. companies at a competitive disadvantage.

Case in point, while Facebook is all caught up in regulatory hearings, China is already planning to implement Facebook's Libra and adapt it for use with WeChat and Alipay.  I guess we'll see how it all plays out, but you get a real sense that the U.S. is going to be left in the dust.

### What are your goals for the future?

Our current focus is on continuing to build our community of developers and users.  As previously mentioned, to scale and improve the capabilities of Hummingbot, we want to encourage participation from the community.  To that end, we have spent a lot of time refactoring and documenting code, making it easier to use.  We have set up a Dev Forum for discussions, and we are starting Gitcoin bounty campaigns to reward code contributors.  We are collaborating with exchanges and DeFi protocols to announce new development bounties.

To drive user base growth, we are working on making Hummingbot easier to use through a GUI, and a future hosted service.  In addition, we are working with token issuers and exchanges and hope to announce several more liquidity bounty programs soon, to make additional rewards programs available for users.

Our long-term goal is to create a self-serve, liquidity market-place, where exchanges and token issuers can sign up for different liquidity campaigns and gain access to a community of Hummingbot market makers.

### What are your future thoughts for the DeFi market?

Having worked in Wall Street and structured finance, I am excited about the potential of DeFi to modernize the archaic practices in the financial industry. It's exciting to be involved in DeFi; there is such a sense of optimism, of the potential to bring about change and make an impact.  

Generally, the sentiment of working in blockchain and crypto is the feeling of being involved in a once in a lifetime/career opportunity to change the world and technology, comparable to the development of the internet in the late 90s/early 2000s.  When you have so many bright, talented, visionaries working together and creating new ideas, there is no doubt that something great will happen.

### Where can we go to learn more?

- [Website](https://hummingbot.io)
- [Litepaper](https://hummingbot.io/whitepaper/)
- [Blog](https://hummingbot.io/blog/)
- [Documentation](https://docs.hummingbot.io)
- [Discord community](https://discord.hummingbot.io)
- [Dev Forum](https://forum.hummingbot.io)
- [Twitter](https://twitter.com/hummingbot_io)
- [YouTube](https://youtube.com/c/hummingbotchannel)
