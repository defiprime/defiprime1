---
git-date:
layout: [blog, blog-amp]
title:  "Partially Collateralized Options with Opyn"
permalink: partially-collateralized-options-with-opyn
h1title: "Partially Collateralized Options with Opyn"
pagetitle: "Partially Collateralized Options with Opyn"
metadescription: ""
category: blog
featured-image: /images/blog/
intro: ""
author: Prospere
tags: ['Interview']
---

### What are Options?

Options are derivatives contracts that give the buyer the right, but not the obligation, to either buy or sell a fixed amount of an underlying asset at a fixed price on or before a certain date, commonly referred to as the expiry date. In DeFi, underlying assets can include any ERC-20 assets, such as: WETH, WBTC, UNI, YFI, SNX, among others. 

People use options for a variety of reasons. The primary reasons include yield / income generation, speculation, and hedging. For the purpose of this article, we’ll focus on generating yield through selling options and explain how DeFi traders can take advantage of the capital efficiency benefits of partially collateralized options. In short, partial collateralization allows options to be collateralized with less than their max loss (&lt;1 asset for call, &lt;strike for puts), enabling users to sell more options with the same amount of capital. 


### Background

To date, one of the biggest limitations of options in decentralized finance was that users were required to fully collateralize options trades. In traditional finance, margin required for options only represents a small fraction of the total value of the contract, making options a highly leveraged trading vehicle. Trading on margin is also why traditional financial markets have been more capital efficient than DeFi but today marks the dawn of a new era!

In other words, partially collateralized options represent a large contract value that can be controlled with a relatively small amount of capital. This aspect of options trading results in greater profits and losses than fully-collateralized options, providing traders, and ultimately markets, with better leverage and capital efficiency.


### Opyn Partial Collateralization Overview

Users can now choose if they want to fully collateralize or partially collateralize a minted option.

If a user chooses to partially collateralize their trade:
* For calls, less than 1 underlying asset can be posted as collateral
* For puts, less than strike can be posted as collateral

With partial collateralization, excess capital is now free to either standby risk free or be deployed in another trade.

#### Benefits of Partial Collateralization

* Enhanced leverage for short options
* Sell MORE options to generate HIGHER yield
* Commit less capital, allowing more portfolio flexibility

#### Risks Associated with Partial Collateralization

* Greater downside leverage
* Under-collateralized positions will lead to forced liquidations
* Possible to lose 100% of original investment prior to expiration


### Margin Design

Margin is calculated using only a spot price, a shock to spot parameter, a conservative assumption on vol/premium, and time to expiry to give a worst case bound on the option premium.

Full details [here](https://medium.com/opyn/partially-collateralized-options-now-in-defi-b9d223eb3f4d).


### Liquidation Mechanism

Sellers must maintain a minimum amount of collateral in their vault to secure the options they have sold. If a seller fails to do so, their vault may be liquidated and their collateral will be seized and auctioned off to repay their debts. The liquidation mechanism is a reverse dutch auction that is triggered via a Chainlink pricer with a specific timestamp.

The reverse dutch auction serves as the price discovery mechanism for Opyn liquidations.The reverse dutch auction starts at a low price and then the price increases over time — liquidators will execute the trade when it is profitable.

Full details [here](https://medium.com/opyn/partially-collateralized-options-now-in-defi-b9d223eb3f4d).


### Opyn Partial Collateralization Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/4Rvy-XOcg3Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

\
Link: [https://youtu.be/4Rvy-XOcg3Y](https://youtu.be/4Rvy-XOcg3Y) 


### Partial Collateralization Examples (*numbers made up for ease of understanding)

#### Collateralization Ratio 100%

* **Option:** 2400 call
* **Option Expiration:** &lt; 1 week
* **Current ETH Price:** $1815
* **Collat Ratio:** 100%
* **Spot change:** N/A
* **Liquidation Price:** Infinity

Alexis has 1 ETH and wants to sell call options to earn yield. She wants to fully collateralize her position to avoid any possibility of being liquidated. Alexis can either leave the partial collateralization toggled off or select a collateralization ratio of 100%. By fully collateralizing her short position, Alexis can only sell 1 call option, but she won’t be liquidated.

* **Trade Date:** July 3
* **Option Expiration Date:** July 9
* **Amount of Calls Sold:** 1

On July 4, the price of ETH rises to $1900 \
On July 5, the price of ETH rises to $2000 \
On July 7, the price of ETH rises to $2075 \
On July 9, the settlement price of ETH is $2050

Since the price of ETH stayed below $2,400 on the expiration date, Alexis’ option expires worthless and Alexis can redeem the premium + her full collateral.


#### Collateralization Ratio 50%

* **Option:** 2400 call
* **Option Expiration:** &lt; 1 week
* **Current ETH Price:** $1815
* **Collat Ratio:** 50%
* **Spot change:** 20%
* **Liquidation Price:** $2178

Aparna has 1 ETH and wants to sell call options to earn yield. She wants to partially collateralize her position so she can sell more than one call option and earn more premium. Aparna toggles the partial collateralization button on, and selects a collateralization ratio of 50%. By partially collateralizing her short position with a 50% collateralization ratio, Aparna can sell 2 call options, but she has the possibility of being liquidated if the price of ETH moves to her liquidation price of $2178.

* **Trade Date:** July 3
* **Option Expiration Date:** July 9
* **Amount of Calls Sold:** 2

On July 4, the price of ETH rises to $1900 \
On July 5, the price of ETH rises to $2000 \
On July 7, the price of ETH rises to $2075 \
On July 9, the settlement price of ETH is $2050

Since the price of ETH stayed below the liquidation price of $2178 before the expiration date, Aparna’s options expire worthless and Aparna can redeem the premium + her full collateral.


#### Collateralization Ratio 33.3% 

* **Option:** 2400 call
* **Option Expiration:** &lt; 1 week
* **Current ETH Price:** $1815
* **Collat Ratio:** 33.3%
* **Spot change:** 12.5%
* **Liquidation Price:** $2041

Zubin has 1 ETH and wants to sell call options to earn yield. He wants to partially collateralize his position so he can sell more than one call option and earn more premium. Zubin toggles the partial collateralization button on, and selects a collateralization ratio of 33.3%. By partially collateralizing his short position with a 33.3% collateralization ratio, Zubin can sell 3 call options, but he has the possibility of being liquidated if the price of ETH moves to his liquidation price ($2041).

It’s important to note that as the collateralization ratio decreases, so does the spot change % until liquidation. In other words, a lower collateralization ratio means a smaller change in the price of the underlying asset can increase the risk of the position being liquidated. That’s why the liquidation price is lower for Zubin’s options than it is for Aparna’s partially collateralized options.

* **Trade Date:** July 3
* **Option Expiration Date:** July 9
* **Amount of Calls Sold:** 2

On July 4, the price of ETH rises to $1900 \
On July 5, the price of ETH rises to $2000 \
On July 7, the price of ETH rises to $2075 \
On July 9, the settlement price of ETH is $2050

As you can see, the price of ETH moves close to Zubin’s liquidation price of $2041 on July 5th, and then moves above Zubin’s liquidation price on July 7th. Let’s look at two scenarios, 1) Zubin adjusts collateral to avoid being liquidated, and 2) Zubin does NOT add collateral to his vault before the reverse dutch auction starts the liquidation process.

#### Scenario 1: Zubin adjusts collateral to avoid being liquidated

On July 5, the price of ETH rose to $2000, close to Zubin’s liquidation price of $2041. To avoid the possibility of being liquidated at $2041, Zubin goes to his [Dashboard](https://v2.opyn.co/#/dashboard), selects his short position, and then adds collateral to his short position vault. By adding collateral, Zubin increases his collateralization ratio, increases the spot change % until liquidation, and increases the liquidation price of his position. Zubin’s new collateralization ratio is 50% and his new liquidation price is $2178.

Since the price of ETH stayed below Zubin’s new liquidation price of $2,178 before the expiration date, Zubin’s options expire worthless and he can redeem his premium + his full collateral.

#### Scenario 2: Zubin does NOT add collateral to his vault before ETH increases past his original liquidation price of $2400, causing the reverse dutch auction to start the liquidation process

On July 7, the price of ETH moved above Zubin’s liquidation price of $2041, causing the reverse dutch auction to start.

The reverse dutch auction serves as the price discovery mechanism for Opyn liquidations.The reverse dutch auction starts bidding for Zubin’s collateral at a low price and then the price increases over time — liquidators will execute the trade when it is profitable.

#### Zubin’s Liquidation Example (numbers made up for ease of understanding):

​​Zubin sold 3 call options, and the margin required for each option was ~$266 (33.3% collateralization ratio on $2400 call = ~$799 total), but each option is worth $200, so $799 margin is required total to cover options worth $600 total. However, let’s say only $700 of collateral is in the vault, so the vault is in the liquidation zone.​​The system seizes the vault and tries to buy the options that were minted from the vault by offering some of the collateral in the vault in exchange for those options.​​

The reverse dutch auction will first bid a very small amount of collateral for the 3 options, say $6, or $2 each. No one will execute this trade.

​​Then, a few blocks later, Opyn’s bid will be $100. No one will execute this trade. This process will be done continuously on a per block basis. ​​Quite a while later, opyn will raise its bid to $550. At this point, a liquidator might execute this trade, if not, someone will definitely a few blocks later when Opyn raises its bid to $600, assuming gas is less than $100.

#### Reasons to Avoid &lt; 40% Change in Spot

It’s recommended that you do not input a spot change % less than 40%. This will cause your vault health to start in the warning or dangerous zone, which could lead to your options position being liquidated from small moves in the price of the underlying asset.

Adjusting your collateral also costs gas, so significantly under-collateralizing your position to start could become expensive over time.