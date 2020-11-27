---
git-date:
layout: [blog, blog-amp]
title:  "Lien Protocol"
permalink: lien
h1title: "Lien Protocol - Stablecoin Without Governance"
pagetitle: "Lien Protocol - Stablecoin Without Governance"
metadescription: "The Lien Protocol team talks about their new stablecoin system, which doesn’t require over-collateralization or governance"
category: blog
featured-image: /images/blog/lien-og.png
quote: /images/blog/lien-quote.png
intro: "The Lien Protocol team talks about their new stablecoin system, which doesn’t require over-collateralization or governance"
author: Defiprime
tags: ['Interview', 'Derivatives']

---
The Lien Protocol team talks about their new stablecoin system, which doesn’t require over-collateralization or governance.

_Disclosure: This article was sponsored by Lien Protocol._


### Hello! What's your background, and what are you working on?

Our name is [Lien](https://lien.finance/). Our core members include people who previously worked at crypto-related companies as engineers, traders, researchers, and strategists. Our team also includes former bankers, analysts, and quants. Everybody on our team believes in crypto as a technology and its philosophy, which we think will change the world and how we all approach identity.

Lien is a Protocol that can mint a crypto-backed stablecoin without over-collateralization and governance. Instead of requiring users to pledge excess collateral to produce stablecoins, the Lien Protocol enables users to mint two types of derivative tokens, which are called SBT and LBT, from ETH. Both these tokens have a strike price and a maturity date, and they allow holders to receive certain amounts of ETH according to the ETH/USD price at the maturity date.

An equivalent quantity of SBT and LBT (i.e. at a ratio of 1:1) are minted from the ETH that is pledged. SBT stands for “Solid Bond Token.” As its name suggests, it is rather stable compared to LBT, which stands for “Liquid Bond Token.” SBT is defined as a token that is redeemable upon maturity in ETH equivalent to kUSD, as long as the price of ETH upon maturity is above kUSD. kUSD represents the strike price. If the price of ETH is below the strike price, the holder of SBT receives the amount of ETH that was pledged when the SBT was minted. On the other hand, the amount of ETH that could be redeemed by the holder of LBT is leveraged. Since LBT holders receive the remaining ETH after SBT holders redeem their ETH according to the strike price, the higher the ETH price is on the maturity date, the more ETH that LBT holders receive.

For example, let’s assume you pledge 1 ETH and generate 1SBT and 1LBT with a strike price of 100 USD/ETH when the price of ETH is 200 USD/ETH. If the price of ETH on the maturity date is 400 USD/ETH, the SBT holder receives ETH equivalent to 100 USD, which is 0.25 ETH, and the LBT holder receives 0.75 ETH. On the other hand, if the price of ETH on the maturity date is 100 USD/ETH, the SBT holder still receives ETH equivalent to 100 USD, which is 1 ETH, and the LBT holder receives nothing. While the value of SBT is stable, LBT acts as a call option since the amount of ETH the LBT holder receives increases as the price of ETH increases. By bifurcating ETH into a stable-valued token and a call option token, the Lien Protocol eliminates the need for over-collateralization.

![](/images/blog/Frame 1.png)

As was explained above, the value of SBT is stable as long as the strike price is adequately set by considering the current price and volatility. By utilizing this feature of SBT, the Lien Protocol is able to mint stablecoins from SBT. By putting SBTs with varied maturity dates and appropriate strike prices into a contract, the value of the stablecoins are kept stable. We believe this mechanism is an improvement to other protocols that require frequent intervention of governance schemes to maintain stability fees or require users to pledge excess collateral to ensure that the protocol is kept stable.

With the Lien Protocol, users can gain access to a “real” stablecoin that is censorship-resistant, purely backed by ETH, and whose value is clearly defined by financial theory.

### What's the Lien Protocol backstory?

As many of our team members used to design derivative products in the traditional financial industry, we have been pursuing a product that has better capital efficiency in the DeFi world.

Out of coincidence or pure luck, an idea struck us in early 2020. After brushing up that idea through hours of discussion, we finally came up with our current model. We validated the feasibility of our idea through back-testing and simulations using historical data going back three years. We wrote about this extensively in our third whitepaper if you’re interested in learning more.

### What went into building the Lien Protocol?

According to our current plan, we will be able to release the [Lien Protocol](https://lien.finance/) to mainnet towards the end of August. An initial round of code audit was conducted by Consensys Diligence and we have already received feedback. We are in the process of diligently addressing the feedback from the initial audit and preparing for the second round of code audit. We will be ready to release to mainnet once we finish addressing any findings from the second code audit.

While we were building the Lien Protocol, a lot of DeFi products were released -- one after another it seemed. We strongly believe that our protocol will be among those that will benefit the market most. In addition to the protocol itself, we developed a DEX platform so that users can trade assets generated using the Lien Protocol without worrying about liquidity. Existing DEX platforms require LPs to provide liquidity in advance, which is disadvantageous to the LPs. We designed our DEX platform to mitigate front-running and cater to LPs. We would like users to trade assets minted from Lien using this DEX platform, which we call Lien FairSwap.

![](/images/blog/1_ntGOr9GWGrSgLIYL1PApng.png)

Though we still need to increase users and LPs who exchange assets on our platform, we are confident the Lien Protocol will benefit users in the long run.

### What's your business model?

Our intention is to generate enough funds to maintain the Lien Platform through the issuance of Lien tokens. The Lien token is a utility token that the holders can use to receive discounts on the transaction fees that are required when transacting on the Lien Platform. The Lien Protocol charges a fee when users mint iDOL, our stablecoin, and when users exchange assets using Lien FairSwap. Fees are collected in ETH or iDOL and are then distributed to holders of the Lien token as discounts/rebates at the end of each month. Early users can purchase Lien tokens using Lien FairSwap.

As the Lien Protocol provides a versatile service, the competitors are different for each area. In terms of the crypto-backed stablecoin iDOL, MakerDAO is undoubtedly a competitor. However, the approach that Lien takes is completely different from the one of MakerDAO. MakerDAO accepts USDC and WBTC, which exposes MakerDAO to the credit risk and security risk of issuers. Lien only accepts ETH as a collateral and the stablecoin minted by the Lien Protocol is purely backed by ETH derivatives. Since over-collateralization is not required, users can efficiently create positions.   

The Lien Protocol can be considered a protocol to create options, too. The SBT has the same cash flow as selling a European put option, and the LBT has the same payoff as buying a European call option. In this sense, Opyn may be a competitor, though we don’t consider them a direct competitor as they take a much different approach to their system. Opyn chose not to use an oracle, while Lien requires one in providing its services.

### What’s your position on the regulatory landscape today?

Though regulation of “crypto assets” is gradually being applied to various regions around the world, a regulatory framework that addresses the openness and complexity of DeFi has yet to be conceived, let alone established. Honestly speaking, we believe the DeFi movement which started with Bitcoin is unstoppable, and what is important is to think of how we are going to coexist with such technology and freedom.

We call this “financial imagination” among our team. Our hope is that the regulation that is created in this brave new world will benefit society. We have performed our own analysis and study on how the Lien Protocol would fit under current regulatory frameworks, though we do not mention it here as the regulations differ from region to region.  

### What are your goals for the future?

Our ultimate goal is helping to lead the world into the future by providing people options to be freed from overbearing governance systems. To achieve that, we set our product goal as creating a stablecoin that could be widely used in the world. We’ve brought ideas from traditional finance to the DeFi world to create a new financial system that can only be done in DeFi. [Lien Protocol](https://lien.finance/) is just a tiny step towards that goal.

### What are your future thoughts for the DeFi market?

The future of cryptocurrencies and DeFi is definitely bright. We believe DeFi has pushed the crypto world into the next stage as it starts to open up the possibility of everything working automatically. Because the on-ramps and off-ramps into and out of the crypto world are still controlled by regulators, transfer of assets sometimes do not occur according to the users’ intention. However, in DeFi once users request a contract to do things, it will automatically be enforced.

Just like buying candy or chocolate at a store, this sector lets you easily access financial products such as loans, insurance, derivatives, and investments. This will accelerate and expand the crypto economy just like how financial products did in the traditional economy through credit-creating functions. This will change peoples’ lives by providing them with freedom to choose where to store their value, like in assets other than fiat or securities which exist in the world today.

Though there is a possibility that these new assets might bring chaos to the world in one form or another, it is unstoppable, and we cannot wait to see what the future holds. It is our belief that the attractiveness of cryptocurrencies and DeFi will gradually grow on people and spread as the core infrastructure of the future. Gradually but surely, they will keep creating a positive impact on our lives.

#### Where can we go to learn more?

- [Website](https://lien.finance/index.html)
- [Whitepapers](https://lien.finance/White_paper.html)
- [Twitter](https://twitter.com/lienfinance)
- [Github](https://github.com/lien-finance)
- [Blogs](https://medium.com/lien-finance)
