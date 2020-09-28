---
git-date:
layout: [blog, blog-amp]
title:  "Bonding Curve Offering Explained"
permalink: bonding-curve-explained
h1title: "Bonding Curve Offering Explained"
pagetitle: "Bonding Curve Offering Explained - Primer on Bonding Curve Token Sales"
metadescription: "In the context of DeFi, a bonding curve is a mathematical formula used to set a relationship between a token’s price and its supply"
category: blog
featured-image: /images/blog/bonding-curve-og.png
intro: "This year we’ve notably seen more DeFi projects turning to bonding curves to efficiently distribute their tokens to the ecosystem"
author: Peaster
tags: ['DeFi Guides']
---
In the context of DeFi, a bonding curve is a mathematical formula used to set a relationship between a token’s price and its supply. This year we’ve notably seen more DeFi projects turning to bonding curves to efficiently distribute their tokens to the ecosystem.

Launching a token in this way entails a team creating a bonding curve smart contract, which applies a custom-tailored formula to a smart contract with mint and burn functions. Once this contract is launched, users can buy or sell into the curve. Buying pushes the token price up along the curve, while selling pushes the token price down along the curve.

This distribution model, also known as a Bonding Curve Offering (BCO), provides numerous advantages beyond simply being automated and highly customizable. For one, BCOs (like ICOs) give early buyers an opportunity for considerable profit upside, a dynamic that can lead to cascading positive marketing effects over time. Additionally, BCOs offer instant markets for tokens and can be deployed via DAOs for effectively decentralized distributions.

## Bond Curve Offering Projects

### DXdao

Spun out as one of Gnosis’s umbrella projects, [DXdao](/product/dxdao) is a for-profit decentralized collective that collaborates on owning and operating DeFi products and protocols. For example, this year the collective launched Mesa.eth.link, a front-end UI for the Gnosis Protocol DEX, and Omen, a decentralized predictions marketplace, and the group continuously earns revenues from these ventures.

In May 2020, DXdao announced and launched a “continuous token offering via a bonded curve” for the collective’s native DXD token, which grant holders claims on future DXdao revenues. Using Alchemy, a resource management tool built atop DAOstack, the decentralized collective’s members had voted on the offering’s “configuration parameters, including pre-mint, curve slope, dividend split, and kickstarter threshold.”

For the sale, DXdao created a “linear and positive” curve for its bonding curve smart contract and designed it so that “$300,000 USD worth of ETH would be invested once 12,000 DXD was issued.” That 12,000 DXD represented slightly under 11% of the token’s total supply, and that allocation was reached in a matter of months. Since then, over 48,000 DXD have been issued through the BCO to date.

![](/images/blog/DXdao_eth.png)

Interestingly, in August discussions started picking up among DXdao stakeholders around the prospect of pausing or modifying the DXD minting contract’s bonding curve to improve “organic price discovery.” Those discussions remain ongoing right now.

### Hegic

In August, the upstart on-chain options trading project [Hegic](/product/hegic) [announced](https://medium.com/hegic/announcing-hegic-token-liquidity-mining-utilization-rewards-and-staking-d1dd6605f2cd) it was launching its native $HEGIC token via an initial bonding curve offering, or IBCO. The IBCO took place across three days, from September 9th to September 12th, and 25% of the +3 billion $HEGIC token supply (~753 million $HEGIC) was allocated to the sale.

![](/images/blog/EhvG_7eU8AAusQu.jpg)

In contrast to DXD’s bonding curve, $HEGIC’s bonding curve is hardcoded and “cannot be changed in the future.” Moreover, $HEGIC’s bonding curve contract also had a hardcoded initial $HEGIC token price of 0.0000069 ETH / HEGIC (~$0.0027) and a hardcoded final price of 0.007537 ETH / HEGIC (~$2.93). This means the token had a fully diluted market capitalization of ~$8.8 billion when the last one was purchased from the IBCO.

The Hegic bonding curve smart contract charges a 10% swap fee for users trading $HEGIC to ETH, with half of this fee being diverted to the Hegic Development Fund and $HEGIC “staking lots.” Another novelty of the $HEGIC IBCO was its anti-competitive structure, insofar as investors’ ETH was pooled and the settlement price was the same for all contributors. All of the ETH amassed during the offering will be used to bootstrap Hegic liquidity pools over the next year.

### Perpetual Protocol

In September 2020, decentralized perpetual contracts exchange Perpetual Protocol [launched distribution of its PERP token](https://medium.com/@perpetualprotocol/guide-to-perpetual-protocols-balancer-lbp-cf4fd160618f) through a Balancer Liquidity Bootstrapping Pool, or LBP.

This kind of private and specialized pool can be created according to any arbitrary logic, which gives projects superior flexibility when it comes to crafting a bonding curve and generating liquidity and distribution for a new token.

Accordingly, the Perpetual Protocol team specifically crafted their LBP curve to mitigate manipulation and speculation, the creators explained a few weeks ago:

>“The starting price will be very high to disincentivize front running and price speculation. We understand the desire to obtain PERP tokens to participate in governance and staking, but trying to rush into the pool will not have any benefits.”

As for specifics, Perpetual Protocol set aside 7.5 million PERP for its Balancer LBP, or 5% of the token’s 150 million total supply.

### Aavegotchi

Aavegotchi is a new DeFi-NFT meld from the minds behind the [Aave](/product/aave) lending and borrowing protocol. The play-to-earn project involves collectible NFT “Aavegotchi” creatures that are backed by Aave’s interest-bearing aTokens. Beyond that the innovative effort has no shortage of interesting additional dimensions, like governance, wearables, games, and more.

![](/images/blog/Aavegotchi_Token_Bonding_Curve.png)

Speaking of Aavegotchi governance, it’s managed by the new $GHST token, which was distributed on September 14th via a bonding curve smart contract. After the conclusion of a presale for 500,000 $GHST, the bonding curve was immediately opened. The IBCO is unlimited in size, has no time limit, and offers an opening price of 0.2 Dai per $GHST. Per Coingecko, the token’s price had already risen to +50 Dai each just a few hours after the IBCO launched.

## Conclusion

Bond curve offerings are a more flexible and customizable evolution of the initial coin offering phenomenon that seized the cryptoeconomy during the 2017 bull run. This evolution shows that DeFi teams are now approaching token distributions with more consideration and control, and this newfound empowerment will surely lead to more novel IBCO releases in the months and years ahead.
