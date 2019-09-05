---
layout: blog
title:  DeFi Accounting
permalink: defi-accounting
h1title: 'DeFi Accounting Series: Crypto Lending & Borrowing Platforms'
pagetitle:  'DeFi Accounting Series: Crypto Lending & Borrowing Platforms'
metadescription: 'In this article, we’ll look at some of the most popular crypto to crypto financing platforms in detail and discuss the bookkeeping entries and tax ramifications from the lender side and borrower side.'
category: blog
featured-image: /images/blog/defiaccounting-og.png
quote: /images/blog/defiaccounting-quote.png
intro: 'In this article, we’ll look at some of the most popular crypto to crypto financing platforms in detail and discuss the bookkeeping entries and tax ramifications from the lender side and borrower side.'
author: knab
---
<div style="text-align: right">
<p>DeFi Accounting Series:
<br>
<a href="/dao-accounting">Part 1: Decentralized Autonomous Organization Accounting</a>
<br>
<a href="/defi-accounting">Part 2: Crypto Lending & Borrowing Platforms</a></p>
</div>
The notion of HODLing is rooted in the idea that assets should be held onto because chances are the price of the assets will increase. We know thought that cryptocurrency prices don’t always go up because of inherent value.

Lending and borrowing cryptocurrencies gives HODL a whole new meaning. The Compound Finance [whitepaper](https://compound.finance/documents/Compound.Whitepaper.pdf) describes HODLing as providing “negative yield.” The network fees and risk associated with holding onto an asset mean that unless there are price increases, the value of the asset actually decreases over time. DeFi platforms allow lenders to lock cryptocurrency and watch the interest accrue. Borrowing also offers ways to hedge risk and potentially make money off your cryptocurrency holdings.

In this article, we’ll look at some of the most popular crypto to crypto financing platforms in detail and discuss the bookkeeping entries and tax ramifications from the lender side and borrower side.

>Disclaimer: This is not accounting advice, just an intellectual exercise about how one can think about how to book these types of transactions.

## Lending/Borrowing Platform Overview

![](/images/blog/defiaccountingimage1.png)
_Figures from [defipulse.com](https://defipulse.com/) on August 5, 2019._

## EOSRex

The EOSRex is different from the rest of the platforms analyzed not only because it is built on a protocol that’s not Ethereum but because it has an overall mission as a lending platform: to enable users to lend/borrow EOS to be able to stake on the network. It does not create any assets but instead issues a claim to the EOS locked in its protocol in the form of REX. REX are not tradeable outside of the platform.

### Lender

- #### Bookkeeping Entries.

Since the lender still has domain over their funds and can maintain their voting rights when lending to EOS REX, the transaction could just be considered an internal transfer. It would stay on the assets side of the balance sheet. It’s not possible right now to lend for longer than 30 days so it would even be considered a current asset. All that would be booked are fees associated with moving funds under expenses. The user is then designated a REX token to represent their lent funds. This token is not tradeable nor transferrable, so we would not classify it as an additional asset. Any interest gained from the EOS lockup would be booked as income, and its cost basis would need to be marked as of the time of receipt.

- #### Tax Implications.

If the transfer of EOS from the user wallet to the REX is booked as an internal transfer, there would not be a taxable event triggered. There would be income taxes associated with the interest received from lending.

### Borrower

- #### Bookkeeping Entries.

Borrowing EOS would need to be booked as a loan liability with a corresponding entry to increase crypto-assets. Interest payments are expensed as fees.

- #### Tax Implications.

Capital gains/losses should be calculated for interest payments.

## Compound Finance

### Lending

The more that I have researched this platform, the more alike I think it is to MakerDAO from a bookkeeping perspective. Compound takes an interesting approach to lending and borrowing as a platform. The act of lending to Compound actually creates a whole new asset that needs to be taken into account. When a user deposits crypto into Compound, they receive a corresponding cToken that accumulates interest during the lending period. For example, if I deposit ETH into Compound, I receive cETH back. Compound calculates the exchange rate of cETH by starting at “0.020000 — and increases at a rate equal to the compounding market interest rate. For example, after one year, the exchange rate might equal 0.021591. Each user has the same cToken exchange rate; there’s nothing unique to your wallet that you have to worry about.” These cTokens are tradeable on secondary markets. When a cToken is transferred, the claim to the underlying asset is transferred.” Check out their website for more information.  

When I first read this, I thought, “more derivatives!” I have a general wariness about some of the creative asset creations in crypto because they are a tad like a house of cards: if one underlying asset suffers a liquidity crunch, it affects all of the assets on top of it. But I digress - that’s a conversation for another article. Since cTokens are a new kind of asset, I wondered if there was a secondary trading market for them. The answer is “sort-of” right now. Here is a representation of the liquidity of on-chain some cToken transfers courtesy of [Will Price](https://twitter.com/willprice221) from [FRST](https://www.frst.com/):

![](/images/blog/defiaccountingimage2.png)

If I were in the business of predicting the future, I would imagine that scenario will change, and cTokens will be more widely traded (especially with the super recent creation of rDAI). From a savings perspective, why would I accumulate DAI? It’s got a negative yield. If I were wanting a relatively stable form of crypto that accumulated interest, I would rather be creating or buying, cDAI.

- #### Bookkeeping Entries.

The real question here is about custody. Compound says they are a non-custodial platform in that lender funds are sitting in smart contracts that their company cannot touch. Given this guidance, we need to make entries that somehow reflect you’re locking up an asset, then receiving a new, different, interest-bearing asset in return, then unlocking that locked asset and cashing in the interest-bearing asset. Some might argue that a cToken should not be treated as a separate asset. I do not agree with this because a) it is structurally different from the underlying asset, and b) it is tradeable on a (small) secondary market. So we will also move forward with the assumption the cTokens are separate assets from their underlying asset.

As with certain types of DAO transactions, the need to convert everything to USD for the sake of uniform bookkeeping and readable financial statements means that we are not truly capturing what is going on in the transaction. But let’s give it a shot:

![](/images/blog/defiaccountingimage3.png)

Booking the receipt of the value of cTokens is difficult because it has tax implications. We technically need to mark the value of the cToken at the time of receipt, but its “true” value really isn’t realized until it is either redeemed at Compound or traded away to a different counterparty. In my mind, it is sort of like a buy option but without a strike price or date. In the absence of clear guidance, it is up to the lender to determine the fair market value of the cToken at the time of receipt. The difference in the amount of underlying collateral sent and received upon redemption of the cToken is interest income.

- #### Tax Implications.

This is a fairly complex transaction to figure out tax calculations for. There is interest income that would need to be reported. Additionally, there are potentially two assets that capital gains/loss must be calculated for. There would need to be a capital gain/loss of the actual assets lent to the platform. Additionally, one might want to consider that cTokens in themselves would trigger a taxable event - especially if they are not redeemed on Compound but are instead sold to a different counterparty. Matching the fair value of the cTokens at the time of receipt to the value at the time of redemption would minimize the capital gain potential.

### Borrower

- #### Bookkeeping Entries.

This would look very similar to the bookkeeping entries for MakerDAO CDPs. There must be entries for the loan liability, receipts of funds, interest payments, and collateral. The collateral is where things get weird.

![](/images/blog/defiaccountingimage4.png)

- #### Tax Implications.

Capital gains/losses would be calculated on the collateral.

## dYdX, Dharma & Nuo

dYdX platform is unique from the others in that it offers more robust functionality. It allows margin trading, portfolio management, as well as lending and borrowing features. We will just focus on the accounting for the loan business line. Dharma and Nuo offer peer-to-peer matches of lending and borrowing.

### Lender

- #### Bookkeeping Entries.

dYdX looks like it is a custodial platform to me but markets itself as a decentralized exchange (DEX). We will continue under the assumption that their loan platform is decentralized enough where you can classify funds lent as under the user’s ownership.

![](/images/blog/defiaccountingimage5.png)

One interesting thing about dYdX is that interest is deposited continuously into the user’s wallet according to a floating rate. This is great in the sense that you are earning crypto quickly, but impractical from a fair market value calculation. Figuring out the value of income earned would be super complicated; it is as if you were attempting to calculate fair value at the time of each deposit. The important thing here is to figure out a strategy for recognizing interest income - specifically: at what time do you want to be recognizing the income and what methodology do you use to consistently convert it to USD.

- #### Tax Implications.

Income taxes would be calculated on interest income. Since in this example, we are considering this an internal wallet transaction, there would not need to be a capital gain/loss for transfer of funds.

### Borrower

- #### Bookkeeping Entries.

If dYdX is considered a DEX, meaning that a user can access their funds at anytime, can we really book borrowing from them as a loan? A loan suggests that there is a counterparty associated with the transaction, not just you loaning funds to yourself. I would say that because there is interest involved here that gets paid to their protocol, it would be appropriate to book it as a loan.

![](/images/blog/defiaccountingimage6.png)

- #### Tax Implications.

Capital gains/losses would be calculated on the collateral.

## Conclusion

Maybe more than any other category of project, cryptocurrency lending and borrowing platforms have ushered in the era of DeFi. While each platform facilitates transactions differently, the real benefit of each is that for the first time, it offers a kind of savings rate for locking up crypto, as well as a new way of creating liquidity.

#### DeFi Accounting Series

<a href="/dao-accounting">Part 1: Decentralized Autonomous Organization Accounting</a>

<a href="/defi-accounting">Part 2: Crypto Lending & Borrowing Platforms</a>

---
Thanks to [Marissa Iannarone](https://medium.com/@mari.iannarone) and [Will Price](https://towardsdatascience.com/@will_price) for their reviews of this article.
