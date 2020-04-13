---
git-date:
layout: blog
title:  "Why Decentralized Finance totally needs interest rate swaps"
permalink: defi-interest-rate-swaps
h1title: "From Zero to Hero on DeFi Rate Swap"
pagetitle: "Why DeFi totally needs interest rate swaps. Why interest rate swaps are so important?"
metadescription: "Why interest rate swaps are so important? Interest rate swaps are “an average” expectation of future variable rate and that swap rates can tell you about the “market” view"
category: blog
featured-image: /images/blog/swaprate/og.png
quote: /images/blog/swaprate/quote.png
intro: "This article explains why interest rate swaps are so important"
author: Belyakov
---
This article explains why interest rate swaps are so important, especially for Decentralizes Finance now.

### Swaps rates are the market expectation of the variable rate

Starting simple, what are “swap rates”? They are fixed rates that the market can offer to you now in exchange for future variable rates (also called floating rates). There are as many swap rates as dates to which you can lock up the contract. So, there can be a one-month, four-month, or 254-days rate present in the market. At [Swap Rate](https://swaprate.finance/), we introduce 12 rates for the next 12 months:

![](/images/blog/swaprate/1_aKhxElMhcPw7j3_Z5Arq3w.png)

Swap rates can instantly go up and down, depending on market expectations, liquidity, and many other things. That’s why our order books are run on meta-transactions (like 0x-protocol) and can afford hundreds of quotes per second. But first, let’s speak about swap rates as market expectations.

### Swap rates as market expectations

The curve on a chart above represents 12 rates that currently offered by the market in exchange for the variable rate. For example, the market offers me a 3% annualized interest if, in exchange, I pay a floating rate (that will be accumulated from now till the 1st of October). On the 1st of October, the variable rate will be known, and we will settle payments to each other.

What happened now if there is news (e.g., Joe Lubin announced in his twitter that he wants to put tons of DAI in DeFi starting in September). The swap rates starting from September will significantly decrease for a while. Market makers and users will withdraw their orders from Swap Rate and put new, less attractive orders back. Indeed, knowing that the deposit rate will drop in September, I am willing to pay a lower fixed rate in exchange for the variable, that is high for now, but will be very low starting in September.

That’s why the swap rates (so-called “swap curve”) represent the average market expectation of the effective APR rate for the specified period. If I don’t agree with these expectations, I can go and make money. In fact, I can [earn 10x leverage](https://medium.com/opium-network/how-to-make-10x-returns-on-compound-finance-9bf8914dbd21) if I am right.

## DeFi vs CeFi

Instead of talking about how vital interest swaps are for the traditional financial system, we will show you a chart. Interest rate swaps are the biggest market in the World:

![](/images/blog/swaprate/1_Hj8H25vinO14DaujVur3AQ.png)

### The market expectation in DeFi

Swap rates will represent market expectations and will change accordingly. It will also be a great indicator of what market thinks of a specific rate.

### Hedging rates in DeFi

The most apparent usage of swaps is locking the rate for deposits and loans. Indeed, it is a perfect match when I don’t like the risk, and I want to receive guaranteed interest on my deposit; at the same time, somebody wants to lock up his borrowing rate. We will run into a swap agreement, taking into account the typical difference between the deposit and borrowing rates.

### Arbitrage example

Why are swaps so cool for arbitrage? Because using them, you can easily hedge cash flow at different maturities from fixed income instruments.

Suppose you see a year bond that has a 10% yield. So you can invest today 100 USD and get 110 in one year. Suppose at the same time the market swap rate is 6%. You can make an arbitrage: you borrow 100 USD, lock the borrowing rate at 6% using the swap, and now buy a bond. In one year, you will receive 110 USD from the bond and pay 106 USD to the lender. You made a profit!
When more people start doing this trick, the bond price goes up, and the bond yield will go down.

## Liquidity

Liquidity is the key, and here we explain why there is natural demand from both demand and supply sides.

Every deposit-hedge corresponds to the loan-hedge. Indeed, as we explained earlier, both lenders and borrowers don’t like risks and uncertainty. It’s a natural need for swaps:

![](/images/blog/swaprate/1_uc_O9xEAtXxZ3-u9DWiD7g.png)

In this scheme, there is an explanation of how interest rate swaps make the DeFi ecosystem better and more reliable. They also open unlimited opportunities to build new products, using predictable and stable cash flows.
Interest rate swaps make the DeFi ecosystem better and more reliable. They also open unlimited opportunities to build new products, using predictable and stable cash flows.

Alice exchange variable future interest for fixed 3% and Bob pays fixed 5% for his loan. They both have swaps on Swap Rate, but because it is a non-custodial platform, there is a market maker who is counterparty for both of them. You can see from the scheme that the market-maker receives 5% and pays out 3%, earning 2% himself! But he also needs to pay a difference between lending and borrowing rates of AAVE. Fortunately, this difference is very stable and close to 1.8%, so the market-maker is earning 0.2% himself.

Everybody is happy: Alice can enjoy fixed-rate deposits. Bob can pay fixed interest for his loan, and the market-maker earns interest on the turnover.

If the market-maker increases the quoted spread that Alice receives 2.5% and Bob pays 5.5%, he will earn a 1.2% of turnover! He can also quote 3% for Alice and 6% for Bob and achieve the same result. Market-maker mathematics:

![](/images/blog/swaprate/1_rYlOirc3Rl24PJHwcFFM3A.png)

In fact, market-maker can earn from 0.2% till 5% of turnover depends on market conditions. Spreads between deposit and loan rates are statistically stable, so statistical arbitrage is possible:
![](/images/blog/swaprate/1_CGTcC7dQ7UA3lUIfPeY5AQ.png)

## Swap Rate

At [Swap Rate](https://swaprate.finance/), we have 12 order-books for every variable rate. Order-books carry meta-transactions with specific orders. Once two orders are matched, they immediately settled on the Ethereum blockchain. This mechanism allows to store and cancel orders instantly and free of charge. Depending on market conditions, one can send dozens of quotes per second or cancel orders when the market expectation changes. We achieve the speed of the centralized markets with the security of the blockchain.

The orders in each order book have various parameters but common maturity in the specific month. The settled swap will have a starting moment of the settlement and maturity of the first day of the corresponding month.

For example, I put a swap today for the 1st of June and desired to receive a fixed rate of 5%. My signed order (meta-transaction) will be instantly stored in the “June” order book until there is a matching order (that is willing to pay 5% fixed). If the matching order comes tomorrow (and I don’t cancel my order by that time), the settlement will occur, and that moment will be the swap start date. The variable rate will be accumulated between tomorrow and the 1st of June. On maturity, it will be exchanged for the quoted fixed rate according to the agreement.

![](/images/blog/swaprate/orderbook5.jpg)

### Arbitrage using Swap Rate

Suppose you find an asset that you can arbitrage with swaps. To make it real arbitrage, you would need to buy or sell an asset simultaneously with the swap position, speaking technically — in the same Ethereum transaction.
