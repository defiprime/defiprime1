---
layout: blog
title: "OmenX raises $2M and launches 30-second Bitcoin predictions"
url: /omenx-seed-round-bitcoin-predictions.html
h1title: "OmenX raises $2M and launches 30-second Bitcoin predictions"
pagetitle: "OmenX raises $2M for Base-native prediction markets"
metadescription: "OmenX raised $2M led by Informed Ventures and launched timed Bitcoin predictions. Its product rules detail index checks, entry fees and settlement pauses."
category: blog
featured-image: /images/blog/omenx-seed-round-bitcoin-predictions-ogp.png
intro: "OmenX announced a $2M seed round led by Informed Ventures alongside a live Bitcoin prediction product with individually timed calls."
author: sawinyh
tags: ["News"]
date: 2026-11-23T13:24:52+00:00
---

On November 18, 2026, OmenX announced a $2M seed round led by Informed Ventures and launched on-demand, 30-second Bitcoin predictions. The platform said in its [funding announcement](https://x.com/OmenX_Official/status/2123079008414052362) that it had been built natively on Base from the outset.

The [company-commissioned release](https://cointelegraph.com/press-releases/omenx-announces-2-million-in-funding-from-informed-ventures-and-launches-on-demand-30-second-bitcoin-predictions) describes a product in which each trade starts its own prediction window. In its example, a position opens at 10:00:12 and ends at 10:00:42. Traders get the full interval from their own entry, rather than entering a shared round with some of its time already gone.

OmenX's existing intraday offering has prediction horizons from 30 seconds to 24 hours, depending on the market, according to the release. It also has directional markets tied to more than 100 global assets, including equities, futures, ETFs and indices, alongside sports and esports. Leverage is available on supported event markets. The announcement describes it as an existing platform feature.

## The index decides the outcome

The live [Bitcoin prediction page and its rules](https://www.omenx.com/arcade) set out what happens to each stake. Traders choose whether Bitcoin will finish higher or lower over their call's interval. Once accepted, a call runs for the full 30 seconds and cannot be undone. A losing call forfeits the stake.

OmenX settles calls using its Bitcoin index. The rules describe the index as the median of exchange mid-prices from Binance and Coinbase, expressed in $USDT terms. Binance supplies its Bitcoin market against $USDT. Coinbase supplies its dollar Bitcoin market, converted using the live $USDT-dollar rate. Each exchange's mid-price comes from its best bid and ask.

For an index snapshot to be valid, both sources must be fresh, neither order book can be crossed, and each spread must be at most 2 bps. The sources must also agree within 5 bps. If any check fails, the index is invalid for that second and new calls stop. Existing calls continue toward settlement. The displayed chart can update more frequently, but the rules specify that opening, closing and settlement all use the index.

The opening value is the first valid index after the server accepts the stake. The closing value comes from the index at the 30-second mark. OmenX says it waits up to 2 seconds for late data but never substitutes a price from after the closing mark. A call's entry reference is the accepted call's index snapshot, which can differ from the chart price the trader saw before tapping.

Up wins when the closing value is higher than the opening value; Down wins when it is lower. Equal opening and closing values void the call. A missing valid opening or closing value also voids it. In those cases, the trader gets the stake and fees back. The published settlement rules specify these refunds as well as the data-quality checks that can halt new entries.

## Fixed quotes, entry fees and profit deductions

OmenX prices Up and Down with a model based on recent index moves. Under the rules, each displayed probability price stays between 40 and 60 cents, and the two sides sum to $1.00. A call fills at the quote shown to the trader, fixing its payout when accepted. If the price moves too far before acceptance, the platform refuses the call instead of filling it at another price.

The release calls this zero slippage. Under the documented execution rule, that can mean a rejected call and another submission by the trader. The model supplies the price used to calculate the payout. The opening and closing index values determine which direction wins.

OmenX charges an entry fee of 0.4% of the stake. On a winning call, it divides the stake remaining after that fee by the quoted probability, rounds down to the cent and deducts 5% of the profit. The payout display on the page includes the returned stake. The amount labelled as the prospective win is therefore not all profit.

The published example starts with $50.00 on Up at 53.0 cents. The $0.20 entry fee leaves $49.80, producing a payout of $93.96 before the profit deduction. OmenX then deducts $2.20 from the $43.96 profit. That leaves $41.76 in profit and $91.76 returned, including the stake. These amounts come from the product's own example, not from an estimate using a current quote.

The table limits entry frequency to 2 calls per second. New calls pause if the index is invalid, Bitcoin moves more than 10 bps in a second, OmenX reaches its daily loss limit or the table's risk capacity is full. Calls already open continue toward settlement during a pause. The rules say the chart displays the reason for the interruption.

Each call records its acceptance time, opening and closing values, quote, fee and payout. The Settled tab shows opening and closing values for calls in the current session; calls also appear in Portfolio. A session ends after 30 minutes without a call. For disputes, the instructions tell traders to contact support@omenx.com and provide the time of the call.

## The funding supports an existing market offering

Other OmenX products follow different settlement schedules. Its [homepage](https://www.omenx.com/) describes daily stock predictions as a question about whether a stock closes above its previous trading day's close. Those rounds settle at the closing bell. Winning shares pay $1 and losing shares pay $0. The new Bitcoin product uses the individually timed opening and closing references set out in its rules.

The release lists football leagues, basketball, American football, ice hockey, baseball and UFC among the platform's sports coverage. Across its asset markets, the contract asks whether a price will be higher or lower at the end of a specified period. Users take that position without buying the underlying asset or choosing an exact closing price.

OmenX compares that decision with constructing an options position, where the trader must consider strikes, implied volatility and time decay. Its founder describes the product in terms of choosing a contract and timeframe that suit the trader's view, whether the subject is Bitcoin, a stock or a sporting event.

The funding release says OmenX plans to expand traditional and crypto asset coverage while developing trading across supported markets. It gives no timetable for those additions. The Bitcoin rules name a daily loss limit as a reason to stop new calls but do not disclose its amount.
