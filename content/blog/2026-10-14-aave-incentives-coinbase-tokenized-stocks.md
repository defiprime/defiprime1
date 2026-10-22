---
layout: blog
title: "Aave Starts USDC Incentives for Coinbase Tokenized Stocks"
url: /aave-incentives-coinbase-tokenized-stocks.html
h1title: "Aave starts USDC incentives for Coinbase tokenized stocks"
pagetitle: "Aave Adds USDC Rewards to Tokenized Stocks on Base"
metadescription: "Aave DAO approved variable USDC incentives for seven Coinbase tokenized stocks supplied to its isolated equities market on Base."
category: blog
featured-image: /images/blog/aave-incentives-coinbase-tokenized-stocks-ogp.png
intro: "Aave DAO has approved variable USDC rewards for seven Coinbase tokenized stocks supplied to its equities market on Base."
author: sawinyh
tags: ["News"]
date: 2026-10-14T07:20:06+00:00
---

Aave announced on October 13, 2026 that its DAO had approved incentives for the Coinbase Tokenized Stocks market on Base. The [published program terms](https://governance.aave.com/t/direct-to-aip-august-september-2026-funding-update/25597/4) say rewards began that day, are paid in $USDC through Merkl, and continue until the budget runs out. They do not state a campaign-specific budget.

The campaign covers supply positions in AAPLc, AMZNc, GOOGLc, METAc, MSFTc, NVDAc, and TSLAc. The rate is variable and not guaranteed. Aave can modify, pause, or end the program early, while rewards accrued before a change remain claimable for eligible users.

Access follows the issuer's jurisdictional restrictions. The terms exclude US persons and anyone located in the United States. They also exclude people in jurisdictions where Coinbase does not offer the tokens, comprehensively sanctioned jurisdictions, listed persons and addresses, and anyone whose participation would violate local law.

Claiming rewards amounts to a representation that the claimant is eligible, acquired the tokens under the issuer's terms, and complies with applicable law. The terms say rewards accrued by an ineligible person are not validly earned and may be withheld. This makes eligibility part of the claim process rather than a promise that every address supplying collateral will receive rewards.

The DAO approved the incentive budget through a broader funding update. TokenLogic said rewards are drawn only against live campaigns and that it will report incentive spending through its governance updates. The incentive post does not identify how much of the broader allowance is assigned to this campaign, so its end date cannot be calculated from the published terms.

## What the incentives pay for

The incentives sit on top of an isolated lending market rather than turning the stocks into borrowable assets. Aave's [Base market specification](https://governance.aave.com/t/arfc-deploy-aave-v4-on-base/25427/1) places the seven stocks in a dedicated Equities Hub. Users can post any combination as collateral and borrow $USDC. The equities themselves cannot be borrowed.

That separation matters to $USDC suppliers. Joining the hub explicitly opts them into lending against tokenized equity collateral, and the exposure does not extend to Aave's other Base markets. The hub also includes a supply-only tokenized $USDC spoke for vaults and aggregators.

Pooling lets one borrower use a combination of supported stocks in one position. Each asset keeps its own collateral factor, so the composition of the account determines borrowing capacity. A diversified basket does not receive a separate borrowing multiplier. The market's separation also means a problem with this collateral set does not automatically spread its exposure to lenders in other Aave markets.

Borrowing power varies by stock. The approved collateral factors are 78% for AAPLc, 73% for AMZNc, 76% for GOOGLc, 65% for METAc, 79% for MSFTc, 70% for NVDAc, and 65% for TSLAc. The market uses a 5.5% maximum liquidation bonus and a 10% liquidation fee. Its $USDC reserve has a 32 million add cap and a 21 million draw cap.

The token structure adds risks that do not exist for ordinary crypto collateral. LlamaRisk's [technical assessment](https://governance.aave.com/t/coinbase-b20-equities-on-base-assessments/25690/2) says each token is a certificate over shares held in segregated custody under a bare trust governed by Abu Dhabi Global Market law. Secondary-market buyers initially have economic exposure but no redemption right until they complete the issuer's vesting process. The program terms also say Coinbase, not Aave DAO, TokenLogic, or Aave Labs, issues the tokens.

The price feed includes an issuer multiplier as well as the underlying share price. The multiplier begins at 1.0 and changes for corporate actions. A reinvested dividend raises it after fees and withholding tax, while a stock split changes it by the split ratio. During a corporate action, the issuer pauses its registry flag, minting and redemption stop, and the feed holds its last value until the adjusted price is confirmed. Token transfers can continue during that window.

## The price feed stops when stocks stop trading

The market operates continuously, but its equity prices do not. Chainlink's tokenized equity feeds publish from Sunday evening through Friday evening in US Eastern time and hold their last value during weekends and market holidays. The feeds use a 0.5% deviation threshold and a 24-hour heartbeat while sessions are open.

A frozen feed means a position's reported collateral value does not move during a closure. Its health factor can still fall as interest accrues. When the feed resumes, news accumulated during the closure can appear in one price update and push a position below its liquidation threshold. LlamaRisk modeled the collateral factors around that gap, including a historical closure lasting 92 hours and 35 minutes and a 24% stressed debt rate.

Liquidators may also face a delay after taking collateral. The assessment says issuer redemption is available only to vested holders and settles during regular market hours. Base secondary liquidity can be thin, while an off-hours liquidator may need to hedge until the underlying market opens. The maximum liquidation bonus is designed around redemption, secondary-market sale, and perpetual-hedge routes.

For stock holders, the immediate change is a variable $USDC subsidy on collateral they could already use to borrow $USDC. The reward is not a contractual entitlement, and its rate can fall as participation grows. A supplier also remains exposed to the issuer, custody arrangement, price feed, smart contracts, and liquidation process.

For $USDC suppliers, the campaign may bring more collateral into the isolated hub, but it does not remove weekend repricing or liquidation-path risk. They have opted into that risk by supplying to this hub rather than another Aave market.

The next milestone is not dated. The campaign ends when its budget is exhausted unless Aave modifies, pauses, or stops it earlier. The figure to watch is whether borrowing demand remains after the variable subsidy changes or disappears.
