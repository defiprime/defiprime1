---
git-date:
layout: blog
title:  "Comparison betwen Flashloan providers: Aave vs dYdX vs Uniswap"
permalink: flahloans-comparison
h1title: "Comparison betwen Flashloan providers: Aave vs dYdX vs Uniswap"
pagetitle: "Comparison betwen Flashloan providers: Aave vs dYdX vs Uniswap"
metadescription: "If you follow DeFi, you probably have heard of Flashloans. With Flashloans, you can borrow massive amounts of money on the Blockchain without any collateral"
category: blog
featured-image: /images/blog/flahloans-og.png
quote: /images/blog/flahloans-quote.png
intro: "In this article, we are going to go over their pros and cons"
author: Klepatch
---
If you follow DeFi, you probably have heard of Flashloans. With Flashloans, you can borrow massive amounts of money on the Blockchain without any collateral.

You can use this money for:
- Doing arbitrage strategies
- Executing liquidations
- Swapping collaterals
- And probably a lot of other creative use cases!

When people think “Flashloans,” they think Aave, the company that originally came up with the concept of Flashloans. But there are also other DeFi protocols that provide the flashloans.

In this article, we are going to go over their pros and cons, since you need to know them if you want to create profitable Flashloans.

Before you continue, do not be shy to sign up for my [free training for mastering flashloan](https://eattheblocks.com/flash). And if you want to watch the video version of this article, [click here](https://youtu.be/x145fp11zj0).

## Aave Flashloans
[Aave](https://Aave.com/) is a lending protocol. You can borrow and lend tokens on their platforms. In early 2020, they came up with the idea of Flashloans, and ultimately they became mostly known for flashloans, even if that’s not their main product.

The [first REAL Flashloan](https://twitter.com/CamiRusso/status/1218640871048056832) ever made on the Ethereum Blockchain was actually created with an Aave Flashloan. So Aave has a special place in the Flashloan ecosystem.

On the pros side:
- Wide choice of tokens
- Can borrow ETH directly, instead of WETH
- And it’s quite easy to integrate, as they have good documentation and even a [Truffle box](https://github.com/Aave/flashloan-box) (i.e., a template you can use to create your own flash-loan quickly)

On the cons side:
- They charge a 0.09 pct fee for each Flashloan

And we’ll see later how these pros and cons compared to other flashloan providers.

## dYdX Flashloans
[dYdX ](https://dYdX.exchange/)is a decentralized exchange for advanced traders. It has some advanced features like margin trading and synthetic assets that can track the performance of other assets, like Bitcoin.  dYdX also provides flashloans, but it’s a bit of a hidden feature, and not many people know about it.

First, we need to understand how dYdX works. In the smart contracts of most decentralized exchanges, they have different entry points or functions in their Solidity code for the various actions you can take.

For example, there is a function for:
- Depositing tokens
- Another function to withdraw tokens
- Another function to buy, tokens, etc., etc.…

This poses a problem because traders have to send several transactions to make just one trade, which costs more money in transaction fees.

It’s possible to solve this problem with what we call meta-transactions. With meta-transactions, you can do several transactions in a single transaction.

dYdX has built-in meta-transaction capabilities. With dYdX, there is just one entry point to interact with its smart contracts. So no matter which operation you want to do, buy, sell, deposit tokens, you always call the same Solidity function.

When you call this function, you will define a set of actions you want to take. For example, you can package together three steps:
1. Deposit tokens
2. Trade
3. Withdraw tokens

And with that, you complete the whole process in one single Ethereum transaction. One interesting detail is that balances are only checked at the end of a transaction after completion of all the actions. A consequence is that you can withdraw as many tokens as you want, regardless of your actual balance on the exchange.

Another interesting detail is that there is a general action named the “call” action. With this action, you can execute the function of any smart contract on the Ethereum blockchain, outside of dYdX.

So here is how you would build a flashloan on dYdX. You will need to combine three actions in a single transaction:
- First, with the withdraw action, you can withdraw a lot of tokens, more than what you have in your balance.
- Then, with the call action, you can execute an arbitrage on the Ethereum Blockchain, by calling for any DeFi protocol you want: Uniswap, Kyber, etc.
- Finally, with the deposit action, you reimburse the tokens you borrowed, and you are done, the flashloan is completed

On the pros side:
- dYdX has no fee. That’s really huge!
- You can use the flashloan money for arbitrages on dYdX itself

On the cons side:
- Limited choice of tokens
- You cannot borrow ETH directly. Instead, you get WETH (Wrapped Ether), which is less convenient to manipulate
- Complex to integrate, with their system of actions, and they don’t have proper documentation for their hidden flashloan system

Okay, so now you understand dYdX a bit better, that was a bit complex, and for the next flash loan provider we are going to see, Uniswap, it’s going to be simpler.

## Uniswap Flashloans
[Uniswap](https://uniswap.org/) is one of the most popular decentralized exchange in DeFi. Uniswap recently upgraded to Uniswap V2, and as part of the update comes to a new feature called Flashswap. Flashswap is essentially Uniswap’s term for flashloan.

On Uniswap, when you want to buy tokens on their platform:
- First, you send the tokens used for your payment.
- Then you call a function called swap(), which will send you the tokens that you just purchased

The important thing is that you can “forget” to send your payment tokens, and first receive the tokens you purchased before paying. Once you have received these tokens, you can use them in whatever way you want. For example, you can use them to do some arbitrage on Uniswap itself or at any other DeFi protocol.

And after your arbitrage, you have to send the payment tokens to Uniswap finally. And if you don’t, of course, the whole transaction fails.

On the pros side:
- Wide choice of tokens
- Can borrow ETH directly, instead of WETH
- You can use Uniswap flashloan to trade on the Uniswap itself
- The choice of asset available for flash loans is huge, as you can tap one of the many Uniswap pairs

On the cons side:
- There is a 0.3pct fee for each flashloan with Uniswap. Just to be clear, this is not an extra cost just for the use of flashloan. This is the regular fee you pay for every trade on Uniswap.

## Which flashloan to pick?

If you want to borrow ETH, DAI, or USDC, I would go with dYdX because it’s the only Flashloan provider that does not charge a fee.

If you want to access more currencies, I would go with Aave.

And if you want to access more currencies, I would use Uniswap.

Now what you now all of this, the next step is to create your own profitable Flashloan.

---
And to learn how to do this, register for my free training on flashloan [on my website EatTheBlocks](https://eattheblocks.com/flash).

I will see you there!
