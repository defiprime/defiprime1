---
layout: blog
title: "Link brings USDC-funded agent spending to Instinct"
url: /link-balance-instinct-usdc-agent-spending.html
h1title: "Link brings USDC-funded agent spending to Instinct"
pagetitle: "Link balance brings USDC-funded agent spending to Instinct"
metadescription: "Link balance lets eligible US Instinct users fund AI purchases with USDC and skip approval within per-purchase limits. New York is not yet included."
category: blog
featured-image: /images/blog/link-balance-instinct-usdc-agent-spending-ogp.png
intro: "Link has opened USDC-funded balances for eligible US Instinct users, allowing agents to make purchases within a user-set limit without repeated approval."
author: sawinyh
tags: ["Stablecoins", "News"]
date: 2026-10-27T08:25:16+00:00
---

On October 26, 2026, Link [began rolling out funded balances](https://x.com/link/status/2114799287645393098) that let eligible US Instinct users authorize AI purchases without approving every checkout. The balance holds $USDC. Users choose how much money to add and set the maximum amount an agent can spend per purchase without asking again.

Instinct [confirmed the feature was live](https://x.com/instinct/status/2114799582760861732), built with Stripe and Link. Its announcement described a US rollout starting that day, with New York coming later. Users start from Instinct by asking the agent to set up the balance. The announcement directs them to a feature they can use, with no waitlist to join.

## A purchase limit, not a cumulative allowance

Link's [setup guide](https://support.link.com/questions/set-up-a-balance-for-agent-wallet-purchases) lays out the authorization process. The user follows a setup link and accepts the terms, then completes identity verification, chooses a purchase limit and adds funds. Purchases above that limit still require approval. The threshold applies separately to each purchase, rather than setting a cumulative budget for all the orders an agent places.

The existing [agent-wallet workflow](https://support.link.com/questions/link-agent-wallet-faq) asks the user to approve each proposed spending amount with biometric authentication, such as a passkey, FaceID or Touch ID. After approval, the agent receives a one-time card for checkout. The payment method first receives an authorization for the requested amount, then the final purchase cost when the agent completes the transaction. Completed transactions appear in Link Activity.

With a funded balance, the agent can use the skip-approvals option for purchases within the threshold. Users can change that threshold by asking the agent for an update link. Setting it to $0 prevents the agent from skipping approval. The same balance can also pay for purchases that still require approval, so users can draw on those funds for both approved and unattended orders.

Users remain responsible if the agent buys a different product from the one originally shown, according to Link's agent-wallet FAQ. The spending permission covers the amount; it cannot ensure that the agent selects the intended item. The FAQ directs users with wrong-item complaints to the agent platform. Users can also pursue a return with the merchant that sold them the product.

## Card funding, stablecoin balances

The setup page identifies the asset behind the balance as $USDC. Users do not need to convert it before making purchases through the agent. Receipts refer to $USDC even when the user started by adding money from a card. The feature uses a stablecoin balance to fund payments through Link's existing checkout service.

Users can add funds with supported credit and debit cards. American Express, Discover and Capital One cards are excluded. A saved payment method can appear grayed out if it is ineligible. Link tells users whose funding attempts fail to try again or choose another card. Money added to the balance appears in the account's Activity section.

The setup-link troubleshooting instructions also specify that the amount being added must be $150 or less and denominated in USD. If both conditions are satisfied but the link still fails, users should request a fresh setup link from their agent. This restriction applies to the amount being added through that link. The documentation does not describe it as a lifetime spending allowance for the agent.

US onboarding requires successful Social Security number verification. Setup initially asks for a date of birth and the last four digits of the SSN. If that check fails, the user must provide all nine digits. If verification fails again, Link support must arrange another attempt. The guide offers no alternative verification method. The broader [balance FAQ](https://support.link.com/questions/link-balance-faq) requires account holders to be at least 18 and says Link may request age documentation.

## Custody and the exit route

Link's setup guide describes both custodial and non-custodial balances. In the custodial version, Bridge, a Stripe company, holds assets on the user's behalf and manages the private keys. Users retain ownership and give withdrawal instructions through their Link account. Bridge handles key management under this arrangement; the shopping agent does not hold the keys.

For the non-custodial version, Link and wallet provider Privy supply access to an on-chain wallet controlled by the user. The displayed balance reflects the assets in that wallet. Users can give Link permission to transact within approved limits. The guide says users can export self-custodial wallet keys at any time and warns them to keep the keys confidential. Losing login or recovery access can permanently cut off access to funds.

The balance FAQ permits withdrawals after identity verification, with no holding period. Users can send funds to a bank account or an external crypto wallet. A bank withdrawal converts $USDC to local currency at the current exchange rate; a wallet withdrawal retains the asset without conversion. Users must check the destination network and address. Link warns that transfers to a wrong address or unsupported network may be permanently lost. Once a withdrawal request has been created, it cannot be canceled.

## Checkout access still has limits

Link says agents can shop most websites, but merchants may block automated purchases with CAPTCHAs or bot detection. Restrictions also apply to some categories of goods and services. When an agent purchase fails at a particular merchant, the FAQ suggests trying another retailer or completing checkout without the agent.

Users can disconnect an agent through Connected Apps in Link. Disconnection stops it requesting new cards and expires existing spending requests and generated virtual cards. Lowering the balance's skip-approval threshold changes when the user must approve a purchase. Disconnecting the agent ends its connection to the payment account.

The standard agent wallet supports accounts originally created in the US and Canada. The new balance announcement covers eligible US Instinct users. Instinct has not given an opening date for New York. The setup guide describes both custody arrangements without identifying which applies to every account in this rollout.
