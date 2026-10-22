---
layout: blog
title: "Blur to close frontend and stop new Blend loans"
url: /blur-to-close-frontend-and-stop-new-blend-loans.html
h1title: "Blur to close frontend and stop new Blend loans"
pagetitle: "Blur sets November 12 shutdown for frontend and new Blend loans"
metadescription: "Blur will retire its frontend and stop matching new Blend loans on November 12, while its marketplace contracts and $BLUR fee switch remain active."
category: blog
featured-image: /images/blog/blur-to-close-frontend-and-stop-new-blend-loans-ogp.png
intro: "Blur will retire its web frontend and stop matching new Blend loans on November 12, leaving its marketplace protocol onchain and promising a separate withdrawal tool."
author: sawinyh
tags: ["DeFi", "News"]
date: 2026-10-12T21:21:03+00:00
---

On October 12, 2026, Blur [said it will deprecate the Blur frontend](https://x.com/blur_io/status/2109735810857861203) on November 12, 2026. The marketplace protocol will remain operational onchain, and $BLUR holders will retain control of its fee switch.

The same deadline applies to Blend's loan-matching service. Blur [said Blend will stop matching new loans](https://x.com/blur_io/status/2109735871377289375) on November 12. Borrowers have until then to repay their loans or allow them to default. After the cutoff, Blur plans to provide a frontend tool that helps users withdraw assets from Blend.

The announcement separates the interfaces from the contracts. Blur is retiring the website used to reach its marketplace, while the marketplace protocol itself stays live. Blend's change is narrower in wording but more direct for borrowers: new loan matching stops, existing borrowers face a repay-or-default decision, and asset withdrawal moves to a tool that Blur has not yet released.

## What the Blend cutoff changes

Blend was designed as a peer-to-peer perpetual lending protocol for arbitrary collateral, including NFTs. Its [published design](https://www.paradigm.xyz/writing/blend) has no oracle dependency and no fixed expiry. A borrowing position can remain open until liquidation, while lenders set loan terms through market offers rather than a protocol price feed.

The lack of an oracle changes where risk decisions sit. Blend does not ask a shared price feed to decide when an NFT position should be liquidated or what rate a borrower should pay. Each lender chooses the interest rate and loan-to-value ratio it will accept. The protocol then tests whether another lender will refinance the debt when the current lender wants to leave.

The design also avoids scheduled maturity dates. Blend says a position rolls automatically for as long as some lender remains willing to finance the amount against the collateral. Users need an onchain transaction when a rate changes or when either side exits. This cuts routine rollover transactions, but continued financing still depends on lender availability.

In the normal flow, a lender signs an offchain offer specifying the principal, interest rate and collateral collection. A borrower accepts a compatible offer onchain, places the NFT in a vault with a lien, and receives the principal. Blend matches each loan individually instead of pooling lenders' funds.

The perpetual structure does not guarantee that a borrower can keep a position forever. Loans continue only while a lender is willing to finance the debt against the collateral. Interest accrues continuously, and the contract calculates repayment when an interaction requires it. Borrowers can repay at any time. They can also replace a loan atomically by taking a new loan against the same collateral and using the new principal to close the old debt.

Lenders have two exit paths in the design. A lender can submit a compatible offer from another lender and transfer the position without an auction. Otherwise, the lender can trigger a refinancing auction in which the offered interest rate rises until a new lender accepts. The replacement lender pays the old lender the full repayment amount and takes over the loan at the auction's rate.

If no lender accepts before the auction reaches its defined maximum rate, the protocol treats the position as non-viable and liquidates the borrower. The existing lender can then claim the collateral. Blend therefore uses the availability of refinancing, rather than an oracle's estimate of the NFT's value, to determine whether debt can continue.

Stopping new matching removes the path Blur currently provides for originating loans after November 12. The announcement does not explain whether any refinancing functionality will remain available through other interfaces or direct contract calls. It tells current borrowers to repay or allow default before the deadline, which makes the status of each open loan the immediate operational question for users.

## What remains onchain

Blur said the marketplace protocol will continue running after the frontend disappears. Traders or developers may still be able to interact with those contracts through other software, but Blur did not name a replacement marketplace interface in the announcement. The team also said $BLUR will continue to control the protocol's fee switch.

That governance role is consistent with the original Blend design. The paper says Blur's implementation gives $BLUR governance control over selected protocol parameters after a 180-day waiting period. Those parameters include borrower and lender fees, the maximum interest rate reached before liquidation, and the formula used to raise the offered rate during a refinancing auction. The protocol does not ask governance to value collateral or set loan-to-value ratios.

The announced withdrawal tool is different from keeping the full Blend loan interface open. Blur described it only as a way to help users withdraw assets after the deadline. No separate release date accompanied that promise. It did not provide the tool's URL, contract scope, release time or instructions for borrowers whose loans enter refinancing near the cutoff.

For marketplace users, the key distinction is that contract availability does not preserve Blur's own web access. For Blend users, the practical deadline concerns debt rather than the token fee switch. Borrowers need to review open positions before November 12 and choose between repayment and the default path described by Blur. Lenders need to account for the end of new matching through the official interface and for the absence of published details about post-cutoff refinancing.

The next dated milestone is November 12, 2026. Blur still needs to specify when its withdrawal tool will appear and whether users will have any supported route for refinancing or managing active Blend loans after matching stops.
