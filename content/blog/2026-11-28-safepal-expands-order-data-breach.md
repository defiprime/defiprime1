---
layout: blog
title: "SafePal expands breach disclosure to 37,542 earlier order records"
url: /safepal-expands-order-data-breach.html
h1title: "SafePal expands breach disclosure to 37,542 earlier order records"
pagetitle: "SafePal expands breach disclosure to 37,542 earlier order records"
metadescription: "SafePal adds earlier crypto-payment orders to its August breach disclosure and warns it cannot individually notify the newly identified customer group."
category: blog
featured-image: /images/blog/safepal-expands-order-data-breach-ogp.png
intro: "SafePal expanded its customer-data breach disclosure to earlier crypto-payment orders and warned that affected customers cannot be notified individually."
author: sawinyh
tags: ["News"]
date: 2026-11-28T04:21:52+00:00
---

On November 28, 2026, SafePal expanded its August customer-data breach disclosure to include 37,542 additional crypto-payment order records. The wallet maker says the newly identified records cover orders placed between September 6, 2022 and March 1, 2025. Customers who ordered in that period should consider their information potentially affected, even if they never received a breach notification.

The [updated incident report](https://www.safepal.com/blog/security-update) says SafePal cannot email those customers individually. It had already deleted the records needed to identify and contact them under its data policy and remediation work. The investigation widened after reports on November 25 of phishing emails targeting customers outside the order period originally disclosed.

SafePal says the earlier records belong to the same incident, not another breach. Wallet credentials were excluded from the exposed records, according to the company. Its warning concerns phishing messages that use genuine purchase details to persuade customers to disclose those credentials.

## Which orders and information were exposed

The additional dataset includes customer names, email addresses, countries, order IDs, products purchased and payment IDs. SafePal had stored crypto-payment and e-commerce records separately, but a shared payment ID could connect them. That connection brought the earlier orders into the investigation.

The company warns that the new record count is not a customer count. The 37,542 records include refunds, repeat orders and failed orders. SafePal has given no separate count of unique customers in this newly identified group. Adding these records to the original customer total would not establish how many people the incident affected.

Shipping addresses and phone numbers were excluded from the additional group, according to SafePal. The records also excluded payment-card and bank details, crypto-wallet payment addresses, recovery phrases and private keys. The exposed payment IDs could connect order records, but did not disclose the wallet addresses customers used to pay.

The original scope remains unchanged: orders placed between March 2, 2025 and April 11, 2026, involving approximately 39,798 customers. Those records contained a different set of fields, including shipping addresses and phone numbers alongside names, email addresses and purchase details. SafePal's statement that physical addresses were excluded applies to the newly identified group, not to everyone affected by the incident.

“We sincerely regret that this additional scope was not identified during our initial investigation,” SafePal wrote. It now tells earlier customers to treat their information as potentially affected without waiting for an individual notice.

## The authorization flaw and the cleanup failure

SafePal's original disclosure traced the access to an authorization flaw in an order-tracking plug-in. Under certain conditions, someone could use the flaw to access another customer's order information. The company says it fixed the issue when it discovered it and introduced additional security measures.

The [incident FAQ](https://www.safepal.com/scam-protection) sets out the earlier investigation timeline. SafePal first received a report consistent with the problem in early May. It initially treated the report as isolated, then escalated it into a formal security investigation. The company says interconnected e-commerce components, external integrations and third-party logistics partners left several possible explanations to investigate.

A separate configuration error affected a scheduled data-cleanup process, which stopped working correctly between September 2025 and April 2026. Older orders stayed in the system longer than intended. SafePal says this failure did not cause unauthorized access, but explains why the originally disclosed order range extended back to March 2025. The November expansion covers earlier records that the investigation connected through payment IDs.

SafePal says it shortened retention of sensitive order data to 90 days. Its FAQ describes a secured offline backup of specific affected records, kept solely for possible investigations. The latest blog update says the company had already deleted the customer records it would need to contact the newly identified earlier group. It does not explain which records from that group, if any, remain in the investigation backup.

On October 30, the company reported that Cure53 had completed an independent audit of its e-commerce system. The audit covered remediation and a broader review of order processing. SafePal says it found no security vulnerabilities. The November update repeats that finding, which SafePal reports in its incident notice.

## Phishing warnings and what customers should do

The expanded disclosure follows a November 12 warning about physical phishing letters sent to customers affected by the August incident. SafePal said the letters alleged firmware-security problems or made other false claims. They directed recipients to a phishing site through a QR code. The latest warning also tells customers to avoid unauthorized firmware-update instructions and communications that use real order details.

SafePal says customers should not need to move assets solely because their order information leaked. Its guidance separates exposure of purchase details from exposure of wallet secrets. Anyone who has entered a seed phrase or private key into a suspicious website, or shared it in response to a message, call or letter, should treat that wallet as compromised.

In that situation, the company tells users to create a new wallet with a trusted SafePal device or its official application, move remaining assets to the new wallet and contact official support. SafePal says genuine emails never ask for a seed phrase, private key or password. They also never demand urgent identity verification or a firmware upgrade through a link.

The company has engaged anti-phishing providers including Phishfort and says it is submitting takedown reports for impersonation sites. Customers can submit suspicious material through its scam-protection page. The FAQ also asks anyone reporting financial losses to contact the dedicated support channel. Those case details are intended to assist asset tracing and authorities where funds can be identified.

The FAQ expressly disclaims any commitment to compensation or admission of liability. SafePal has not supplied a unique-customer count for the expanded scope and says it cannot notify that group individually.
