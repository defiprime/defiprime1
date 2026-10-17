---
layout: blog
title: "BIS Links Higher Deposit Rates to Slower Stablecoin Growth"
url: /bis-links-deposit-rates-to-slower-stablecoin-growth.html
h1title: "BIS Links Deposit Rates to Slower Stablecoin Growth"
pagetitle: "BIS Study Finds Bank Deposits Compete With Stablecoins"
metadescription: "A BIS study finds that higher U.S. deposit rates predict slower stablecoin growth, with a stronger response from $USDC than $USDT."
category: blog
featured-image: /images/blog/bis-links-deposit-rates-to-slower-stablecoin-growth-ogp.png
intro: "A BIS working paper finds that higher US deposit rates predict slower stablecoin growth, especially for $USDC."
author: sawinyh
tags: ["Stablecoins", "News"]
date: 2026-10-17T16:20:51+00:00
---

On October 13, with no UTC publication time listed, [BIS Working Paper 1382](https://www.bis.org/publications/working-paper-1382-are-stablecoins-and-bank-deposits-substitutes) reported that a one basis point increase in bank deposit rates predicted a roughly three percentage point reduction in stablecoin market capitalization growth over ten weeks. The estimate reduced average growth from 15% to about 12%.

The paper by Rashad Ahmed and Iñaki Aldasoro treats bank deposits and reserve-backed stablecoins as assets that can provide overlapping payment and liquidity services. Its result is evidence of partial substitution, not proof that stablecoin growth cuts total bank deposits or lending. Stablecoin issuers reinvest reserve assets, which can move deposits between institutions or depositor types rather than remove them from the banking system.

## What the study measured

The authors assembled 339 weekly observations from January 2019 through June 2025. Their stablecoin series covered aggregate reserve-backed market capitalization for $USDT, $USDC and other reserve-backed tokens. Algorithmic stablecoins were excluded. The sample began when stablecoin market capitalization stayed above $1 billion and ended when Haver Analytics suspended publication of the RateWatch deposit-rate data used by the study.

The key input was the weekly change in an average of six national deposit-rate series. Those series covered savings deposits and standard or preferred money market deposit accounts at several balance tiers. The model also controlled for the federal funds rate, the three-month Treasury bill rate, the ten-year Treasury yield, bitcoin prices, the VIX and the broad U.S. dollar index. Those controls were intended to separate deposit pricing from wider interest-rate, currency and crypto-market conditions.

Reserve-backed market capitalization rose from under $5 billion in 2019 to more than $220 billion by mid-2025. Across the full sample, average market capitalization was $95.42 billion, while the average deposit rate was 0.26%.

The authors used a kink in deposit-rate pass-through to address the possibility that causality runs in both directions. Banks changed deposit rates more aggressively once the federal funds rate moved above approximately 3%, while Treasury bill rates continued to track policy rates more linearly. The instrumental-variable specification set the threshold at 3.125%, the midpoint of a federal funds target range, and used a four-week lag to reflect slow bank repricing.

## The estimates and their limits

The ordinary least squares estimate found that a one basis point increase in deposit rates reduced ten-week stablecoin growth by roughly three percentage points. The instrumental-variable estimate was larger, reducing growth by roughly nine percentage points, from 15% to about 6%. The authors warn that these are reductions in growth rates rather than declines in the level of stablecoin supply. Growth can continue after deposit rates increase, only more slowly.

A placebo test found no statistically significant response in non-stablecoin cryptocurrency market capitalization. A separate test compared preferred money market deposit rates with savings rates. When preferred rates rose relative to savings rates, stablecoin market capitalization declined by roughly 0.7% after ten weeks. Both checks support the paper's interpretation that relative returns matter for money-like assets rather than for crypto assets in general.

The response differed by issuer. Under the ordinary least squares specification, the ten-week estimate was roughly negative 5% for $USDC and negative 2% for $USDT. The paper associates the stronger $USDC response with its greater use among U.S. institutional and DeFi users. It describes $USDT as more heavily used offshore and in developing economies, where U.S. bank deposit rates may be less relevant.

The authors also tested balances supplied to DeFi lending protocols while controlling for changes in DeFi yields. The median share supplied to lending was 12.8% for $USDC and 4.1% for $USDT over the available periods. After a one basis point deposit-rate increase, $USDC in lending protocols declined by roughly 3.4 percent over ten weeks, while $USDC outside those protocols declined by about 5.5 percent. $USDT in lending declined by about 6.1 percent, while the estimated response outside lending was negative 0.8 percent and statistically insignificant. The estimates for lending balances were imprecise, so the authors present this split as descriptive evidence.

Several constraints narrow the result. The first-stage F-statistic was 9.78, just below the conventional threshold of ten, which indicates some instrument weakness. Aggregate data cannot identify which holders moved funds or which banks and deposit categories were affected. The sample contains only one high-rate period, from 2022 through 2025. It also describes a market in which stablecoins generally paid holders no interest. Yield-bearing stablecoins and tokenized money-market funds could change the relationship.

The negative estimates survived several alternative specifications. The authors separately controlled for crypto trading volume, the Terra collapse, the FTX failure and the phaseout of $BUSD. They excluded the Silicon Valley Bank episode, which had caused an unrelated $USDC outflow, and added controls for DeFi yields. They also replaced non-maturity deposit rates with certificate-of-deposit rates, extended the projection horizon, added a time trend and varied the interest-rate threshold used by the instrument. These checks reduce the chance that one crypto shock or one modeling choice produced the main result, although they do not remove the limits of aggregate data and a single high-rate episode.

For stablecoin holders and DeFi operators, bank repricing belongs alongside crypto-native yields when assessing demand for dollar tokens. The study found a negative response even for balances already earning lending yield, but it did not show that bank deposits always dominate DeFi returns. For issuers and banks, the evidence points to deposit pricing as one influence on allocation between the two forms of money, while stopping short of a bank-funding estimate.

The paper leaves remuneration as the next open policy variable. Its final question is how the boundary between deposits and stablecoins changes if issuers are permitted to pay holders directly, because the observed relationship comes from a period when stablecoins largely offered no native interest.
