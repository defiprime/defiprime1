---
git-date:
layout: [blog]
title:  Comparing Insurance Like Solutions in DeFi
permalink: comparing-insurance-like-solutions-in-defi
h1title: "Comparing Insurance Like Solutions in DeFi"
pagetitle: "Comparing Insurance Like Solutions in DeFi"
metadescription: "Hugh Karp compared various insurance like solutions existing right now in DeFi space"
category: blog
featured-image: /images/blog/comparing-insurance-og.png
quote: /images/blog/comparing-insurance-quote.png
intro: "Hugh Karp compared various insurance like solutions existing right now in DeFi space"
author: karp
tags: ['DeFi Guides', 'Insurance']
---
I regularly get questions like, could you use a prediction market for insurance instead? Or how does a financial derivative compare to what you’re doing at [Nexus Mutual](https://nexusmutual.io/)?

The truth is, each of these products have benefits and disadvantages and are useful in their own right, often for different purposes. So let’s dive right in with a high level comparison table.

>Please note I’m the Founder of Nexus Mutual so even though I’ve tried to take a neutral view throughout this post I’m sure it will inevitably contain some bias.

![](/images/blog/insurance-image2.png)

## Capital Pool and Liquidity

The main difference with insurance-like protocols is the common capital pool. This allows sharing of risk across different covers and crucially allows the pool to be under-collateralised (hold less than 100% of the sum of all potential claim payouts). In fact, this is actually the fundamental reason insurance companies exist, they can cover many multiples of risk with much lower capital.

The common pool structure more efficiently covers risk than either a prediction market or [financial derivative](https://drive.google.com/file/d/1YsrGBUpZoPvFLtcwkEYkxNhogWCU772D/view) that covers a similar event because each market or option needs to be able to pay-out by itself and therefore requires full collateralisation.

Additionally, the pool approach can more easily bootstrap liquidity across a variety of risks. Instead of requiring liquid two-sided markets for each risk, one side of the market is taken by the pool. The pool provides liquidity to all risks at once with the main restriction being limits on the size of each risk (relative to the size of the pool).

## Flexibility

Prediction markets and financial derivatives are much quicker to develop new products, or take on new risks, as long as they fit within the platform criteria. Prediction markets are infinitely flexible and this is one of their major selling points, with the ability to deploy new products in minutes.

Derivatives are also very quick to market, provided the risk fits within the general criteria and constraints of the platform (eg must fit the notion of a financial option that has a strike price etc). Insurance products are much slower, requiring heavy research work on pricing and underwriting to ensure the pool is confident in taking the new risk.

The type of risk that can be covered ie, the flexibility of risk coverage is something else to consider. With prediction markets and - to a slightly lesser degree - insurance pools you’re only limited by your imagination. With financial derivatives there are more restrictions as you need to swap one financial asset for another at a future point in time and are therefore limited by what financial assets exist.

## Oracles

Oracles are another item worth discussing. With Nexus there is a voting approach so it is somewhat similar to [Augur](https://www.augur.net/) at a very high level. However, other insurance like approaches, eg [Etherisc](https://etherisc.com/), use an external oracle as a data feed to determine claim payouts.

The main interesting point of comparison here is not external data feed vs voting, which is a large discussion in its own right, but actually the financial derivative approach which doesn’t have an oracle. If the buyer of the option wants to exercise their right to buy/sell at the pre-agreed price, then they simply do so. This is actually a really neat advantage over the oracle approach.

## Pricing

If we focus on extreme events, or “deep out of the money” events, then the insurance pool approach has significant advantages over either the prediction market approach or derivatives. Say there is a very small likelihood of an event, 1% per year. If you wanted to take the other side of this bet the maximum you could earn would be 1% on your capital as you have to lock up the full potential claim value. Capital costs become a severe limiting factor for deep out of the money events if full collateralisation is required. This is the primary use case for the insurance pool approach and is where it’s benefit of under-collateralisation comes to the fore.

Complimenting this are “at the money risks”, or ones where there is a reasonable likelihood that a payoff occurs. Here capital costs become much less significant relative to risk cost and the flexibility (and other benefits) of prediction markets and derivatives clearly win out. If you’re looking to hedge risks to smooth returns or cap your downside in volatile markets, prediction markets and derivatives are your friend.

## Summary

Each approach works better in particular situations, the key is understanding which approach applies best to the problem you’re trying to solve. If you break down the risk into two components you can better understand what action to take:
- likelihood of it occurring, and
- the consequence assuming the event occurs.

![](/images/blog/insurance-image1.png)
_Classify your risk to understand the best way of managing it._

In general, prediction markets and derivatives are at their best dealing with risks in the “Manage” category. Higher likelihood of occurrence with low to medium financial consequence. Insurance pool like solutions work best for rare or more extreme events that have high financial consequences.
