---
layout: blog
title: "HINC Goes Live as Collateral on Aave Horizon"
url: /hinc-live-aave-horizon.html
h1title: "HINC goes live as collateral on Aave Horizon"
pagetitle: "HINC Adds High-Yield Credit Collateral to Aave Horizon"
metadescription: "Eligible HINC holders can borrow stablecoins on Aave Horizon while retaining exposure to a permissioned high-yield credit fund."
category: blog
featured-image: /images/blog/hinc-live-aave-horizon-ogp.png
intro: "Securitize says eligible HINC holders can now borrow stablecoins on Aave Horizon against their tokenized high-yield credit investment."
author: sawinyh
tags: ["News", "RWAs", "Lending"]
date: 2026-11-24T14:37:25+00:00
---

On November 24, 2026, Securitize [announced that the Neuberger Securitize High Income Tokenized Fund is live as collateral on Aave Horizon](https://securitize.io/learn/blog/hinc-launches-on-aave-horizon). Eligible HINC holders can borrow $USDC, $GHO and $RLUSD against their investment without first redeeming their fund shares.

HINC brings high-yield corporate bonds and collateralized loan obligation tranches into a collateral market that Securitize describes as largely concentrated in tokenized Treasuries, money market funds and higher-rated credit. Neuberger Berman Investment Advisers is the fund's sub-adviser. Securitize Capital is its investment adviser. Holders who borrow against HINC keep their exposure to the credit portfolio and take on the risk of liquidation.

## The fund behind the collateral

The [HINC product page](https://securitize.io/hinc) sets a minimum investment of $100,000. The strategy puts most assets into high-yield bonds, with the remainder in CLOs, bank loans and other high-yielding fixed-income instruments. The fund itself uses no leverage. A holder who borrows against its shares on Horizon takes on that borrowing separately from the fund.

HINC is domiciled in the British Virgin Islands and offered through exemptions from securities registration. The launch disclosure limits offerings to eligible investors, through official offering documents and where permitted by law. Its permissioned token can move only among eligible investors who have completed onboarding. Transfers may be restricted or frozen to comply with the law and the offering documents.

Securitize's onboarding instructions require identity verification, an investment profile and an accreditation application. Investors then select the fund, enter an amount and sign subscription documents. They can fund the investment by wire transfer or ACH and choose between self-custody and holding it in a Securitize account. These admission requirements apply to the tokenized investment.

The issuer's earlier proposal describes a direct fund structure. Investors own shares in HINC itself, without a feeder or master-feeder arrangement. The proposal describes the token as non-rebasing, with income reinvested and no distributions expected. Under that design, income accrues through the share's net asset value rather than scheduled cash distributions to the holder.

The product page lists a management fee of 0.50% and a total expense ratio of 0.60%. The expense cap includes management fees. The manager waives or reimburses operating expenses above the cap, though the governing documents allow the cap to be modified or terminated. Securitize's launch disclosure also states that its adviser and affiliates earn fees connected to HINC. They benefit when fund assets grow, including through use on Horizon.

The model portfolio on the product page is expressly illustrative and does not represent actual holdings. Its gross yield excludes fund fees, trading costs, defaults, realized losses and taxes. It is neither a distribution yield nor a guarantee of future income. A holder comparing borrowing costs with fund income cannot treat the illustration as an assured return on the investment.

## Borrowing access and redemption timing

The fund's redemption terms allow requests on business days and target T+1 settlement for the associated liquidations. Actual settlement may take T+2, T+3 or longer, depending on liquidity in the underlying investments. The terms guarantee no particular timing. An eligible holder can borrow stablecoins against the investment without waiting for that redemption process, subject to Horizon liquidity and borrowing conditions.

The product page places transfers to other whitelisted holders one day after issuance. Its risk disclosure says no secondary market exists for the fund's shares, although the adviser intends to develop one. It cautions investors to treat the investment as having limited liquidity. Holders can pledge their tokens on Horizon while remaining subject to restrictions on selling or transferring the underlying investment.

The public page gives conflicting cutoff times. Its detailed redemption footnote lists 2:00 p.m. ET, while the separate tokenized-access section gives 2:30 p.m. ET for daily subscription and redemption requests. An investor arranging an exit needs confirmation of the applicable offering terms to resolve the conflict between the two summaries. Both sections describe a settlement target, not a guaranteed payment deadline.

The launch disclosure lists credit default, below-investment-grade debt, interest rates, CLOs, liquidity and valuation among the fund's risks. Borrowing on Horizon adds smart-contract, oracle, stablecoin, cybersecurity, operational and regulatory exposure. Securitize explicitly warns that borrowing can lead to liquidation and loss of collateral. Neither Securitize nor HINC guarantees Horizon's liquidity or uninterrupted availability.

## What the earlier proposal explains

Securitize's [August 18 onboarding proposal](https://governance.aave.com/t/arfc-onboard-hinc-neuberger-securitize-high-income-tokenized-fund-to-aave-horizon/25500) targeted Horizon on Ethereum and described HINC as supply-only collateral. It identified the shares as permissioned, ERC-20-compatible DSTokens issued under Securitize's DS Protocol. Securitize Transfer Agent maintains the securityholder register. According to the issuer, VanEck's tokenized Treasury fund on Horizon already used the same issuance infrastructure.

Under the proposed recordkeeping model, pledged tokens remain within each investor's legal holdings. They are marked as encumbered collateral and appear in the investor portal's total securities. The transfer agent reconciles balances and encumbrances through protocol APIs and subgraphs. The earlier proposal describes this as the issuer's intended accounting arrangement; the launch release supplies no new technical specification for it.

Permissioned ownership also limits who can liquidate collateral. The proposal required a liquidator to complete business verification, be onboarded to HINC and have stablecoin capacity committed before activation. A liquidator must be eligible to receive the collateral. The issuer separately warned that liquidators are independent parties whose capacity and participation may vary. Successful liquidation is not guaranteed.

The same proposal identified another route to bad debt. A transfer-agent freeze or seizure could leave collateral temporarily unavailable for liquidation while debt keeps accruing. Securitize asked for the final approval to state explicitly who bears that debt. The issuer raised this as a condition in the earlier proposal, but the launch release does not spell out the resulting allocation.

Horizon has also been expanding how it prices other collateral, including the [weekend pricing for tokenized equities announced in October](/chainlink-24-7-weekend-rwa-pricing.html). That announcement concerned equities. The HINC launch release does not specify its production oracle address or pricing configuration. It also leaves the HINC token contract address, collateral factor, liquidation threshold and liquidator roster unpublished.
