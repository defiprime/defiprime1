---
git-date:
layout: blog
title:  "Uniswap Explained"
permalink: Uniswap-explained
h1title: "Uniswap Explained"
pagetitle: "Uniswap Explained"
metadescription: "Uniswap Explained"
category: blog
featured-image: /images/blog/post.png
intro: "Uniswap Explained"
author: Peaster
tags: ['DeFi Guides']
---

### What is Uniswap? How Uniswap works?

Written in the Vyper smart contract language, [Uniswap](https://app.uniswap.org/#/swap) is an open-source automated liquidity protocol on Ethereum that allows for easy trading and listing of ERC20 tokens. Built around the values of decentralization, censorship-resistance, security, and permissionless utility, Uniswap has become Ethereum’s most popular automated market maker (AMM) exchange since Uniswap’s V1 launch in November 2018.

The Uniswap protocol powers a decentralized marketplace of trading pairs, with each of its pairs composed of reserves of two tokens on an equivalent, 1:1 basis. All pairs are managed by separate Uniswap contracts. This model allows anyone to become liquidity providers (LPs) for a given pair, like ETH/USDC, if they provide the appropriate reserves to the pair’s pooled assets. For instance, using the above example one might supply 1 ETH and 400 USDC if the ETH price is $400, or 2 ETH and 800 USDC, and so forth.

Accordingly, Uniswap LPs are granted pro-rata style LP shares for their services. Notably, these tokenized shares can be redeemed for their underlying assets whenever. Yet since the Uniswap protocol charges a 0.30% fee to all trades and returns these charges to liquidity pools without new LP shares being created, returns are shared proportionally among pools’ liquidity providers. As such, the protocol offers a simple and effective marketplace for ERC20 token trades as well as a cryptonative earning venue for LPs.

While Uniswap V1 will live on for as long as Ethereum does, the upgraded and opt-in Uniswap V2 contracts launched on mainnet in May 2020. The new system offers a [range of key optimizations](https://uniswap.org/blog/uniswap-v2/), including ERC20/ERC20 token pairs, price oracles, flash swaps, and more. At the time of this post’s writing, Uniswap V2 was facilitating nearly $200 million dollars’ worth of total liquidity and over $60 million in 24-hour volume. Moreover, the protocol’s builders are already in the process of preparing [Uniswap V3](https://twitter.com/haydenzadams/status/1290408898898341888).


### Automated Market Maker vs. Order book DEXes

In Ethereum’s decentralized finance sector, two genres of decentralized exchanges, or DEXes, have dominated to date: order book-based DEXes and AMM-based DEXes.

Order book DEXes rely on buy and sell orders around a given token. Buy orders are called bids, and sell orders are called asks. To this end, these exchanges list bid orders and ask orders across every price point, with the “top of the book” marking whatever the lowest ask and the highest bid prices are at a particular time. The cons of order-book marketplaces, though, is that they don’t work well for illiquid markets, and they can be particularly prone to market manipulation and front-running. Some examples of this kind of DEX include 0x, IDEX, and Ethfinex.

On the flip side, AMM-based DEXes like Uniswap rely on what’s called “algorithmic agents,” or “money robots,” rather than order books. Key to this DEX model is liquidity pools, in which users supply assets that a finely-tuned algorithm uses to make markets. Every AMM has its own customized algorithm with its own pros and cons. Ultimately, the algorithm’s unique formula is used to determine prices for users rather than a list of bid orders and ask orders.  



### How are prices determined?

There are multiple genres of AMM-based DEXes, but Uniswap is specifically what’s known as a “Constant Product Market Maker,” or CPMM. This simply means that Uniswap, like other CPMMs, relies on the equation x*y=k to create a price spectrum for token pairs per the available liquidity of these pairs.

For example, if Uniswap had an EXAMPLECOIN/ETH pair, the EXAMPLECOIN (X) supply would decrease if the ETH (Y) supply increased, with the opposite being equally true, so as to preserve the constant of K, i.e the pool’s price of EXAMPLECOIN. “When plotted, the result is a hyperbola where liquidity is always available, but at increasingly higher prices that approach infinity at both ends,” the Chainlink team has [aptly explained](https://blog.chain.link/challenges-in-defi-how-to-bring-more-capital-and-less-risk-to-automated-market-maker-dexs/) before.


### How can I add a token to Uniswap?

Anyone or any project can permissionlessly list a token on Uniswap for trading. Here’s how the process works.

First, navigate to the [Uniswap exchange](https://app.uniswap.org/#/swap). You’ll arrive at a page that looks like this:

![](/images/blog/uniswap/uniswap/image8.png)

Next, click on the “Select a token” button. You’ll arrive at the following prompt:

![](/images/blog/uniswap/uniswap/image3.png)

In the “Search name or paste address” box, paste in the contract address of the ERC-20 token you’d like to list.

For the purposes of this example, _defiprime_ has minted 1 million B52 test tokens and sent my wmpeaster.eth address 100,000 of the tokens to show how a Uniswap listing works. The B52 smart contract can be found at the address [0xc47828014f40322fc24d9c2340ef29d754d67cf4](https://etherscan.io/token/0xc47828014f40322fc24d9c2340ef29d754d67cf4), so we’ll paste this address into the aforementioned “paste address” box. Once that’s done, Uniswap instantly finds my 100,000 B52 tokens:

![](/images/blog/uniswap/uniswap/image6.png)

Moving along, you’ll want to click on the token you’ve just selected, which in our case is the B52 listed below my ETH. Once I do that, I come to this warning screen:

![](/images/blog/uniswap/uniswap/image5.png)

Uniswap includes this warning here because the protocol’s listing process is permissionless, meaning both good and bad actors can readily list tokens through it. To caution against potentially malicious projects, Uniswap stresses that first and foremost users have to take the initiative to avoid scammers. For our example, B52 is just a test token and we know it’s safe, so we click “I understand” here. Now, we arrive back at the main Uniswap trading interface, at the top of which are the “Swap” and “Pool” buttons. Click on “Pool,” and you’ll see this screen:

![](/images/blog/uniswap/uniswap/image12.png)

Press the “Add Liquidity” button, and if prompted, paste in your token contract address again and select your token in the dropdown menu, and you’ll come to a page that looks like this:

![](/images/blog/uniswap/uniswap/image10.png)

Since I’m the first liquidity provider for the ETH/B52 pair, whatever ratio of ETH-to-B52 tokens I add to the pool will determine the B52 token’s price. For example, if I add 0.1 ETH and 100,000 B52 to the pair’s pool, the initial B52 price will be 0.000001 ETH, or roughly $0.0004 USD at current ETH prices. If I add 0.2 ETH and 100,000 B52, the initial B52 price will be 0.000002 ETH/$0.0008, and so forth.

Note: this Uniswap price dynamic is important to consider when gauging newly listed tokens on the protocol. Projects can list only a fraction of a token’s total supply on Uniswap if they want to, meaning the ensuing price actions wouldn’t accurately represent these projects’ wider valuation realities out of the gate. For example, I could list 10 B52 tokens against 2 whole ETH on Uniswap, but the ensuing market activity would be a poor stand-in for how valuable the hypothetical B52 project really is.

Once we have the token ratio set that we’re looking for, we’ll want to approve Uniswap to handle our B52 tokens. I’ll select to fund this test pool with 0.1 ETH and 50,000 B52 tokens as a demonstration and then click the “Approve B52” button. At this point, you’ll have to send a transaction, so you’ll press “Confirm” as prompted:

![](/images/blog/uniswap/uniswap/image13.png)


Now, you’ll wait for that approval transaction to go through. Once it does, Uniswap will activate a “Supply” button on its UI, and you’ll press that.

![](/images/blog/uniswap/uniswap/image9.png)


A final confirmation prompt will pop up that looks like this:

![](/images/blog/uniswap/uniswap/image2.png)

When you’re ready press on the “Create Pool & Supply” button, submit the transaction (but mind the gas fee if you’re pinching gwei), and wait for it to go through. Once it does, your liquidity pool will be created, which results in your token being listed on Uniswap.

Hereafter, you can go to Uniswap’s “Pool” tab to view your liquidity provider (LP) dashboard, which looks like so:

![](/images/blog/uniswap/uniswap/image1.png)


### How does Uniswap pool work?

Liquidity pools, like Uniswap is now renowned for, are a cryptonative utility and a cryptonative earning opportunity.

Simply speaking, Uniswap’s liquidity pools are composed of pools of tokens, with each pool being secured by its own dedicated smart contract. With Ethereum as the foundational infrastructure, users can trade through these pools permissionlessly, 24/7, and without account creation requirements.

The incentive for LPs to provide liquidity is the ability to earn a cut of a given Uniswap pool’s fees, as powered by their provided liquidity. For more on precisely how these pools work, check out defiprime’s longer guide on the subject [here](https://defiprime.com/uniswap-liquidity-pools).  

### How do I add liquidity to Uniswap?


Okay, so how about adding liquidity to an already existing Uniswap pool? The process is similar to the listing sequence we discussed above.

First, navigate to the pool you’re interested in. Go to the Uniswap “Pool” tab, click on it, and then click on the ensuing “Add Liquidity” button. You’ll be prompted to submit a transaction according to your desired token allotments, and once that transaction confirms, your liquidity will be added to the pool. For my example, I sent some B52 to my writer.gimmethe.eth alt so I could add liquidity from a second address. In the picture below, you can see me submitting 3,000 B52 and 0.0068468 ETH to the B52/ETH Uniswap pool.

![](/images/blog/uniswap/uniswap/image7.png)

### How do I remove liquidity from Uniswap?

Withdrawing liquidity from Uniswap is just as easy as adding liquidity is. Go to the Uniswap “Pool” tab, and look at the bottom of the widget for the “Remove” button. Your page will look like this:

![](/images/blog/uniswap/uniswap/image4.png)

Click on “Remove,” and you’ll arrive at a liquidity removal dashboard where you can choose to remove 25%, 50%, 75%, 100%, or a more specific amount of your liquidity. Approve the transaction, submit your removal request transaction, and your assets will be returned to your wallet once the transaction confirms.


### Uniswap how to check liquidity for token

If you’d like to see an expanded information dashboard on a particular Uniswap liquidity pool, go to the uniswap.info website and paste in the token address of the token you’re looking for. When I submit the B52 contract address and click on the ensuing popup, I arrive at a page like this:

![](/images/blog/uniswap/uniswap/image11.png)


The pair dashboard will show you metrics like total liquidity, 24-hour volume, 24-hour fees, as well as all transactions involved with the selected pool.


### Uniswap risks

Uniswap’s design is simple, elegant, and self-contained, meaning the protocol doesn’t have a wide attack surface. However, Uniswap isn’t totally free from risk, either. Namely, Uniswap bears the technical risk that comes with any smart contract-based project, i.e. contracts being attacked or otherwise obstructed.

That said, Uniswap doesn’t appear extensively exposed to technical risk, as the project has been repeatedly audited and the protocol has proven itself in the wild for some time now.

Notably, there was a reentrancy attack vector in Uniswap V1, wherein an attacker could use “hooks” in the ERC-777 token standard to drain liquidity pools based on this type of token. Support for ERC-777 tokens have been added to Uniswap V2, so this sort of attack is no longer possible.


### Uniswap FAQ

- **Q: Why is my Uniswap trade stuck/failing?**

**A**: If you’re Uniswap trade transaction gets stuck indefinitely or fails, chances are you didn’t pay enough gas, i.e. ETH, to successfully process the transaction. You can use your wallet to cancel the transaction and start over, or you can attempt to speed up your initial transaction using something like the [MetaMask wallet’s “Speed Up”](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction) functionality.

-  **Q: Why does my transaction cost X?**

**A**: Every Ethereum transaction needs a payment of ether (ETH), called “gas” or a “gas payment,” to be completed. Ethereum gas prices fluctuate daily in line with demand. If many folks are trying to use Ethereum all at once, then gas prices will be higher. If activity is low, then gas prices will be lower. Your Uniswap transaction cost is the sum in ETH it takes to process your trade or liquidity provision/removal. For up to date stats on current Ethereum gas prices, check out [ethgasstation.info](https://ethgasstation.info/) or [etherscan.io/chart/gasprice](https://etherscan.io/chart/gasprice).
