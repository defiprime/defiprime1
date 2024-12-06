---
git-date: 2020-08-03T18:53:35-07:00
layout: [blog]
title:  "What Are Perpetual Contracts for Bitcoin? dYdX Perpetual Futures Explained"
permalink: perpetual-dydx
h1title: "What Are Perpetual Contracts for Bitcoin? dYdX Perpetual Futures Explained"
pagetitle: "What Are Perpetual Contracts for Bitcoin? dYdX Perpetual Futures Explained"
metadescription: "What Are Perpetual Contracts for Bitcoin? dYdX Perpetual Futures Explained. A perpetual futures contract is a derivative product that mixes elements of futures contract trading and margin-based spot trading"
category: blog
featured-image: /images/blog/dydxperp/perpetual-dydx-og.png
quote: /images/blog/dydxperp/perpetual-dydx-quote.png
intro: "We are going in-depth on new dYdX Perpetual Futures platform in this article."
author: Defiprime
tags: ['DeFi Guides', 'dYdX']
---
A perpetual futures contract is a derivative product that mixes elements of futures contract trading and margin-based spot trading. We are going in-depth on new [dYdX Perpetual Futures](https://dydx.trade?ref=LastOrangeU5D) platform in this article.  


### What Are Perpetual Futures Contracts?

In contrast to regular futures, perpetual contracts don’t have an expiry. This means perpetuals remain active indefinitely if the positions don’t get margin liquidated. Perpetuals also typically trade closely to spot market prices, while traditional futures contracts can trade much higher or much lower than spot market prices. This is because perpetual contracts rely on a “funding rate” system that traditional futures don’t. Per this mechanism, perpetual traders with short positions have to pay perpetual traders with long positions if a contract’s price dips below the spot market price, and vice versa. The funding rate helps perpetual futures trade near spot market prices.


Notably, decentralized margin trading and lending platform dYdX was the first project to launch decentralized perpetual contract markets. dYdX kicked off its inaugural offering, a [BTC-USD Perpetual](https://integral.dydx.exchange/dydx-launches-btc-perpetual-contract-market/) contract, in April 2020.


### What Are Futures Contracts?

A futures contract is an exchange-traded derivative product that allows a buyer to buy or sell an asset at a predetermined price and date, no matter what the market price of the asset is at expiry.

The underlying assets can vary, but financial instruments and commodities are common subjects of these contracts. Mainstream futures exchanges offer a range of futures products, including commodity futures, currency futures, stock index futures, and beyond.


### Why Traders Use Futures Contracts?

Traders use futures contracts for speculation or for hedging risk.

A speculator can use a futures contract to bet on the direction of an asset’s price, and if that price movement plays out, the trader can buy the underlying asset at a profitable price. With regard to hedging risk, consider the hypothetical of a crypto ATM whose enterprise centers around bitcoin. Let’s say this owner thinks the bitcoin price is going to crash in the coming months, so they take up a short position using a bitcoin futures contract. If the bitcoin price does crash, this owner will be able to mitigate losses via the short.


### What Is Equity and Free Collateral?

On dYdX, equity is the trading capital a trader has at stake for perpetuals contracts. In the case of the BTC-USD Perpetual offering, the margin and settlement asset is the USDC stablecoin, so USDC is the equity type for this contract. The amount of equity a trader has available determines their margin level, which is found by dividing equity by the amount of margin used.

Just as dYdX’s spot markets trade separately from the platform’s perpetual markets, users must collateralize their perpetual accounts separately from their margin trading accounts. In addition, free collateral is the amount of collateral a perpetual trader can withdraw per their ongoing positions.


### What Is the Funding Rate?

The funding rate is the periodic rate paid between BTC-USD Perpetual long positions and short positions to keep the contract’s price tethered to the bitcoin price. On dYdX, these algorithmic rates are paid by the second and are updated hourly. These payments are dispensed in proportion to traders’ positions and are only paid among traders. If BTC-USD Perpetual contracts are trading above the spot market price of BTC, then long traders pay short traders; if these contracts are trading below the spot market price, short traders pay long traders.

![](/images/blog/dydxperp/image15.png)



### What Is Liquidation?

Traders whose accounts dip below dYdX’s required margin maintenance percentage are at risk of being liquidated. For the BTC-USD Perpetual, traders have an initial margin requirement of 10% and a margin maintenance requirement of 7.5%. Falling below the margin requirement can happen thanks to drastic price movements in the spot market. For example, a trader who takes out a BTC-USD Perpetual short position would face liquidation if the bitcoin price spiked up enough that they could no longer satisfy their margin requirement. dYdX liquidations are handled on-chain, meaning they are conducted transparently on Ethereum, and thus anyone can serve as a dYdX liquidator.


### What Are Mid-Market, Oracle, and Index Prices?

A mid market price, or mid-price, is the average between the highest buying price and the lowest selling price. At dYdX, any activities that use collateralization, like the BTC-USD Perpetual, rely on oracle/index prices and not the mid-price of dYdX’s spot order books.


Specifically, the BTC-USD Perpetual uses the MakerDAO BTCUSD Oracle V2, an oracle that reports in on-chain fashion bitcoin prices from the cryptocurrency exchanges of Binance, Bitfinex, Bitstamp, Bittrex, Coinbase Pro, Gemini, and Kraken. This on-chain index price is used as the mark price for dYdX liquidations. dYdX additionally uses a separate Index Price, which is also aggregated from multiple exchanges’ spot markets but is maintained off-chain for optimal performance.


### What Are Unrealized and Realized PnL?

PnL means the total profit or loss a trader would incur from ending their position. On dYdX, fees are included in the PnL, so the rate begins in the negative upon the opening of a position. Traders can view their current PnL by opening up their position dashboard. An unrealized PnL is the would-be profit/loss of a position that hasn’t been closed yet, whereas a realized PnL is the total profit/loss of a closed position.


# dYdX Perpetual Trading Guide


### How to Open a Perpetual Futures Trading Account on dYdX?

Since dYdX is a non-custodial exchange, it doesn’t make use of actual user accounts. Instead, traders simply connect their Ethereum wallets to the exchange to start trading. No email or Know Your Customer (KYC) information is required.

With that said, you will need to have a browser-compatible Ethereum wallet to use dYdX. [MetaMask](https://metamask.io/download.html) is one such excellent wallet, and it’s compatible with the Chrome browser as well as iOS and Android devices. We’ll use MetaMask as an example for the purposes of this post going forward, but dYdX also currently supports Coinbase Wallet, Ledger, and WalletConnect.

Once your wallet is ready, you can navigate to the dYdX exchange and move your mouse to the page’s top right corner where you will find a “Connect Wallet” button.

![](/images/blog/dydxperp/image8.png)



Click on that button, and you’ll be given a drop down menu of compatible wallets. We’ll select “MetaMask” here.

![](/images/blog/dydxperp/image3.png)


After clicking on your wallet of choice, your wallet tab will show “Connected” in green. Now you’re ready to deposit funds into this address for trading.

![](/images/blog/dydxperp/image2.png)

Before we get to explaining the depositing process, let’s walk through the signing process you’ll undertake before you can trade perpetuals on dYdX. Since dYdX is prohibited to U.S. users, you’ll be prompted with a “Terms of Service” pop-up once you click on the “Perpetuals” tab at the top of the exchange. You will have to click through four agreements to proceed. The first two agreements deal with confirming you’re not a U.S. citizen, while the last two are trading guidances.

![](/images/blog/dydxperp/image1.png)

Once you click through these agreements and login, your browser-compatible wallet will be prompted with a signature request to confirm the login. Sign the request, and then you’re ready to start trading once it’s processed.


![](/images/blog/dydxperp/image18.png)



### How to Transfer Funds?


You’ll need to have some ether (ETH) and USDC or USDT to trade BTC-USD Perpetual contracts on dYdX. The ETH will be used to pay for signing transactions on dYdX and for sending funds back to your exchange address later, while USDC will be your trading instrument. One of the easiest places to source these assets is large mainstream cryptocurrency exchanges that have fiat on-ramps, like Coinbase or Kraken. Once you’ve purchased and received the funds you want to trade on dYdX with, you send them to your aforementioned browser-compatible wallet.

Go to MetaMask (or your wallet of choice) and copy your trading wallet’s address. On MetaMask, you can do this simply by clicking on your address a single time.

![](/images/blog/dydxperp/image16.png)


At this point, you navigate to the exchange where you’ve purchased funds. We’ll use Coinbase for this example. Go into your USDC wallet and move your mouse to the right side of the page where you’ll find the “Send / Receive” widget. Type in how much USDC you’d like to transfer, and in the address line paste in the wallet address you copied earlier. Your screen will look something like this:


![](/images/blog/dydxperp/image12.png)


Click “Send.” If you’re using Coinbase, you’ll be asked one more time to confirm the send. If everything looks good, press “Send Now” and your funds will be on their way. Repeat this same transaction process with the ETH you’ve purchased until your dYdX trading address has both ETH and USDC in it. Then, it’s time to place orders.


### How to Place an Order?

Since dYdX’s margin trading accounts and perpetuals accounts must be collateralized separately, you’ll need to deposit the trading capital you want to put at stake into your perpetuals account first to make any orders. You do this by navigating to the upper left-hand corner of the exchange’s “Perpetuals” page where you’ll see the “Equity” and “Free Collateral” dashboard, which looks like so:

![](/images/blog/dydxperp/image17.png)


Here, click on the “Deposit” button, at which point you’ll be faced with this prompt:


![](/images/blog/dydxperp/image13.png)


You’ll have to enable your USDC for trading on dYdX, so here you’ll click “Enable USDC” to shoot off a small transaction. Once that goes through, you can start depositing funds into your perpetuals account. In the picture below, I can be seen depositing 50 USDC.

![](/images/blog/dydxperp/image14.png)


Once your funds arrive in your account, your Equity and Free Collateral dashboard should look something like this:

![](/images/blog/dydxperp/image20.png)


(Remember: there is a small fee to open a Perpetuals account, \
which is why this dashboard reads as ~48 USDC

instead of 50 USDC)

With your equity ready to go, you can start placing orders. Look directly below the Equity and Free Collateral dashboard to find the order menu, which appears like so:

![](/images/blog/dydxperp/image7.png)


The “Buy” menu is where you can take BTC-USD Perpetual long positions, and “Sell” is where you can take short positions.


### How to Go About Shorting Bitcoin?

Go to the “Sell” tab shown above and input the amount of BTC you’d like to take a short position out on. Since I wasn’t trading with much USDC, I chose to short 0.01 BTC as seen below.

![](/images/blog/dydxperp/image4.png)

Once your order goes through, you’ll be able to track your position’s performance through the large dashboard located on the lower right-hand side of the “Perpetuals” page. Immediately after I placed the position above, my dashboard looked like this:

![](/images/blog/dydxperp/image10.png)

This area of the page allows you to easily track your short position’s equity, realized and unrealized PnL, and beyond. Note in the picture above, the “8h Funding” section shows me being paid .0138% by long traders; this means the BTC-USD Perpetual contract price was trading above the spot market price of BTC at the time.


### How to Long Bitcoin with Leverage?

Longing BTC through the BTC-USD Perpetual market is generally similar to the process shown above, except we go through the “Buy” tab instead. Below, you can see what it looks like to long .01 BTC.

![](/images/blog/dydxperp/image9.png)

Once the order is successful, the main “Perpetuals” dashboard appears like this:

![](/images/blog/dydxperp/image21.png)

Again, notice in the “8h Funding” section I am paying shorters because I went long while the BTC-USD Perpetual contract price was trading above the spot market price of BTC. This funding rate changes as market conditions change.


### How to Close a Position?

To close a dYdX perpetuals position, navigate to the “Close Position” button in the “Perpetuals” page’s main dashboard. At this point, you’ll face the following prompt. You’ll choose the amount of your position you want to close out, and then click “Close Position” again.

![](/images/blog/dydxperp/image5.png)

Once this is done, you’ll soon see the relevant amount of USDC funds enter back into your “Equity” and “Free Collateral” tabs. You’re now ready to withdraw and cash out if you’d like.


### Moving Funds Back?

Once you’ve withdrawn your funds back into your browser-compatible wallet, you may want to send your assets back to your cryptocurrency exchange in order to cash out earnings (or what’s left from losses) into fiat. To do this, navigate to your wallet’s main screen and find the “Send” button. Click on it, and you’ll encounter this prompt:

![](/images/blog/dydxperp/image19.png)


Here, you’ll want to paste in the deposit address supplied to your account by your cryptocurrency exchange. On Coinbase, you can navigate to your USDC wallet and click on the “Receive” tab on the right-hand side of the page. You’ll be supplied with a QR code and a copyable address.

![](/images/blog/dydxperp/image11.png)

Once you have that address ready to paste, input it into the MetaMask “Add Recipient” bar. On the next screen, you’ll confirm how much USDC you want to send.

![](/images/blog/dydxperp/image6.png)


Click next, fire off the transaction, and your funds will arrive on your exchange shortly. At that point, you can cash out your assets to your bank account if you want.


### Advantages and Disadvantages

**Perpetual Markets Comparison**

There are a handful of notable centralized exchanges that offer BTC Perpetuals. Some of the most prominent of these exchanges are [BitMex](https://www.bitmex.com/app/perpetualContractsGuide), [Deribit](https://www.deribit.com/pages/docs/perpetual), and [FTX](https://ftx.com/trade/BTC-PERP). The perpetual offerings on these platforms have become increasingly popular in recent months, but these exchanges can’t match the transparency offered by dYdX’s on-chain activities. They also can’t match dYdX’s lack of KYC requirements, its non-custodial system, and its ability to let anyone be liquidators. Where the centralized exchanges have dYdX beat for now is volume and number of users, but that dynamic could reverse in the years ahead if decentralized apps continue to pick up steam.

#### dYdX Perpetual Futures Pros
*   no KYC of any kind
*   non-custodial; no account creation needed
*   dYdX Insurance Fund verifiable on-chain
*   deleveraging verifiable on-chain
*   1x to 10x margin offered on perpetual contracts
*   offers additional spot, margin, and borrowing services

#### dYdX Perpetual Futures Cons
*   not available to U.S. users
*   only BTC-USD contract currently offered
*   could use support for additional wallets
*   no BTC deposits available, only USD stablecoins


#### Where can we go to learn more about dYdX Perpetual?

- [Start trading on dYdX BTC Perpetual — get 10% off w/ DeFi Prime code](https://dydx.trade?ref=LastOrangeU5D)
