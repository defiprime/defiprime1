---
git-date:
layout: blog
title:  ""
permalink: 
h1title: ""
pagetitle: ""
metadescription: ""
category: blog
featured-image: /images/blog/
intro: ""
author: Peaster
tags: ['']
---

# Ethereum Gas Explained

Ethereum is an open-source network designed to reliably power decentralized applications. A crucial element of the network is “gas,” which, if we understand Ethereum as a world computer, serves as the fuel for this computer’s applications and transactions. Accordingly, gas is one of the most salient UX aspects of Ethereum.


## What Is Ethereum Gas?

Gas is the fee a user pays to process a transaction on the Ethereum blockchain. Gas prices are denominated in “gwei,” which is a denomination of Ethereum’s native currency, ether (ETH). 1 gwei, also known as a nanoether, is equal to 0.000000001 ETH. 

When you pay gas to submit a transaction, you are paying for the computational energy needed to power the validation of that transaction on Ethereum. As the Ethereum 1.0 network is a proof-of-work system, this computation currently comes courtesy of “miners,” who use special hardware to compete for ordering and processing transaction-filled Ethereum blocks. In exchange for their service, miners can earn ETH block rewards and transaction fees via gas payments. 

Note: Ethereum 2.0 is starting in late 2020/early 2021, which will transition the blockchain into a proof-of-stake system. This shift will phase out mining in favor of staking, at which point stakers who deposit ETH will compete for block rewards and gas fees, not miners.

Additionally, different types of activities on Ethereum will have different gas costs. It’s cheaper to straightforwardly send ETH or an Ethereum-based ERC20 token from one wallet to another than to perform more complex interactions with smart contracts or to process a meta-transaction composed of many transactions. Simply put, gas costs rise in accordance with the complexity of on-chain activity. 


## Who Sets Ethereum Fees 

Two common misconceptions around Ethereum gas fees is that they’re either 1) set by developers, or 2) set by miners. Neither is true. 

Instead, Ethereum users send transactions with requested gas prices and then miners choose which transactions they want to mine into a block. In this sense, Ethereum gas prices are dynamic and the result of an equilibrium being reached between what users bid and what miners accept on a rolling basis. 

As such, it follows that the more transactions users are requesting at any given time, the more expensive gas prices will be as blockspace becomes increasingly scarce. In extension, transactions sent at higher gas prices will be processed faster than transactions sent at lower prices. 

Specifically, you can compute the cost of an Ethereum transaction fee at any time by multiplying the current gas price by the current Ethereum gas limit (i.e. gas price * gas limit = transaction cost). 


## What Is the Ethereum Gas Limit?

A key component of the Ethereum gas system is the Ethereum gas limit. In the context of transactions, the gas limit is the maximum amount of gas units you are willing to spend on a transaction. This ceiling is used to ensure transactions are executed, and since you won’t always pay the maximum amount, any unused ETH is returned to your wallet. 

For basic ETH transactions, a standard gas limit is 21,000. So for example, let’s consider a hypothetical generic transaction sent when the gas price is 100 gwei. We can compute this transaction’s cost by multiplying 21,000 (gas limit) x 100 (gas price) x 0.000000001 (gwei denomination), with the result being 0.0021 ETH. Relatedly, gas limits for ERC20 token transfers can range from 25,000 to as high as 500,000. 

Another important element to consider is how Ethereum has a network-wide gas limit for its blocks, too. This limit bounds the amount of transactions that can be included in a block. Miners have voted on raising this block size limit repeatedly over time to meet growing demand. For instance, in June 2020 miners voted to raise the limit from 10 million to 12.5 million. 


![](/images/blog/ethereum-gas-explained/image2.png)


## How to Set an Ethereum Transaction Fee

When transacting on Ethereum, you can optimize for price by sending transactions with low gas fees or optimize for time by sending transactions with high gas fees. 

Fortunately, popular wallets like Metamask let users easily choose between “Slow,” “Average,” and “Fast” gas fees at the point of transaction. The first two speeds make sense for casual users, whereas “Fast” is the only sensible option for decentralized exchange traders who need to execute the best prices possible as quickly as possible. 

Notably, Metamask and other wallets don’t always accurately estimate gas prices and transaction times, especially when network activity shifts quickly. If you’re ever in doubt, you can manually and correctly set your own gas fees using your wallet’s “Advanced” tab and updated prices from resources like [Gas Now](https://www.gasnow.org/). 

![](/images/blog/ethereum-gas-explained/image1.png)


## How to Cancel Stuck Ethereum Transaction 

In times of network congestion, it’s not uncommon to have an Ethereum transaction get stuck in the platform’s pending transactions pool. This happens when miners prioritize high-fee transactions and your transaction gets outpriced, effectively leaving your transaction stuck in a long queue. 

But no worries, it’s easy to cancel a stuck transaction. Once you do, you can retry the original transaction with a faster gas fee if you want. The process works like so: 


 
1. _Navigate to [Etherscan](https://etherscan.io/)_
2. _Paste your Tx Hash into the Etherscan search bar_
3. _On your transaction page, click the “Click to see more” button_
4. _Your nonce will appear; remember the number_
5. _Prepare a new 0 ETH transaction in your wallet_
6. _Go to the “Advanced” tab and input the same nonce as your stuck Tx (Note: you may have to activate the ability to customize your nonce in your wallet’s settings)_
7. _Send the new transaction with a “Fast” gas fee_
8. _Once this confirms, your original transaction will be unstuck_

Alternatively, there’s a new transaction cancellation dapp available at [cancel-ethereum-transactions.web.app](https://cancel-ethereum-transactions.web.app/). The user-friendly service automatically finds the pending transaction nonce in your wallet and then sends a transaction with the right configuration to quickly cancel it. 


## How to Save on Gas: GasTokens

Gas tokens are an innovation that lets users tokenize gas when gas prices are low. These tokens can then be spent when gas prices are high as a way to subsidize Ethereum transaction costs. 

To date, two ERC20 gas token projects have gained early traction: GasToken.io’s GST token and 1inch’s Chi (CHI) token.

GasToken was first on the scene to deploy a contract that could be used to tokenize gas. This system, which relies on the storage refund dynamic of Ethereum, lets you mint GST tokens by “saving data into the GasToken contract’s storage.” You can thereafter free up this data when gas prices are high by returning these tokens to the GasToken contract, which results in a gas refund. Moreover, in March 2020 the GasToken team rolled out the GST2, a new implementation that creates and deletes contracts to achieve gas savings. 

First unveiled at the “Hack Money” competition in May 2020, 1inch’s CHI is another rising gas token effort. Designed to provide savings and improvements on the GasToken model, CHI is notably meant to be used on the 1inch and Curve platforms, whereas GST can be used across all of Ethereum. GST tokens can be [minted](https://gastoken.io/) via Etherscan, while it’s possible to [mint CHI](https://medium.com/@1inch.exchange/everything-you-wanted-to-know-about-chi-gastoken-a1ba0ea55bf3) on both Etherscan and 1inch. 


## Conclusion

Gas is one of the fundamental elements of the Ethereum network. Over time, it seems likely that gas mechanics will be increasingly abstracted away from users. Until then, understanding how gas works and understanding how to approach configuring your own transactions is key for using Ethereum efficiently and effectively. 