---
layout: blog
title: "Across takes frontend and API offline after domain takeover"
url: /across-domain-takeover.html
h1title: "Across takes frontend and API offline after domain takeover"
pagetitle: "Across domain takeover: frontend offline, approvals at risk"
metadescription: "Across reports a domain takeover and keeps its frontend and API offline, warning affected users to revoke approvals and check signed permits."
category: blog
featured-image: /images/blog/across-domain-takeover-ogp.png
intro: "Across took its frontend and API offline after a domain takeover exposed visitors to malicious approvals, and published instructions for affected wallets."
author: sawinyh
tags: ["News"]
date: 2026-11-11T00:25:17+00:00
---

On November 10, 2026, Across said an attacker took control of its domain at approximately 18:45 UTC through a social engineering attack on Namecheap, its domain registrar. Across kept its frontend and API offline while it worked to secure the domain. Its recovery guide warns that approvals signed on the malicious site can still expose tokens in affected wallets after the site has been removed.

In its [incident disclosure](https://x.com/AcrossProtocol/status/2120278803318489362), Across said it was alerted within 15 minutes and immediately worked to shut the site down. SEAL911 marked the domain as a phishing site with major wallets. Cloudflare marked it as at risk and later pulled its DNS records.

By the time Across published the disclosure, it said the domain was fully down and the phishing site unavailable. Some visitors may have been affected before Cloudflare fully blocked the malicious site. The account of social engineering at Namecheap came from Across, the affected operator, whose investigation was still pending.

## Who Across says was affected

Across's [initial warning](https://x.com/AcrossProtocol/status/2120231513459433747) told users: "Do NOT visit the app, connect your wallet, or sign any transaction or approval there until further notice." Its later statement separated visitors during the attack from people who had used the frontend before it. Across said earlier frontend users, API users and users of third-party integrations were unaffected.

The [recovery guide linked by Across](https://docs.google.com/document/d/1IW3_cSr9fANfxHSXgVnzQ89Bitqv00Xbk-8bhx3L3kM) addresses anyone who visited the site on November 10 and connected a wallet, approved a token, signed a message or permit, or sent a transaction. Its checklist covers wallets with no visible loss as well as those that have already lost funds. It includes signatures that an attacker may not yet have submitted.

According to the guide, the malicious site requested approvals and permits that let attacker-controlled contracts move tokens from users' wallets. Some permissions remained open. The guide warns: "Until you revoke them, the attacker can take any more of those tokens that arrive in your wallet."

Across also [promised reimbursement](https://x.com/AcrossProtocol/status/2120278805084295328): "All affected users will be made whole." It asked affected users to contact its account by direct message. The guide asks people who lost funds to provide their wallet address and transaction hashes. The reimbursement statement gives no payment date or claims timetable.

## Check spenders across networks

The guide tells users to type revoke.cash into their browser themselves and avoid revocation links received in direct messages, replies or emails. It warns that scammers copy the site. Users can paste a wallet address into Search Accounts to inspect its permissions without connecting the wallet. Submitting a revocation requires a wallet connection.

Across instructs users to begin with the network where they used the frontend, then inspect Ethereum, Base, Arbitrum, Ink, $BNB Chain and any other network where they hold funds. Its recovery instructions extend beyond the network used during the attack: users are told to repeat the spender checks and revocations across their networks.

To review approvals, the guide tells users to enter the addresses it identifies in the Search by Spender field. They can also sort by Last Updated to inspect permissions granted on November 10. Across instructs users to revoke approvals for matching spenders without waiting for the attacker to use those permissions.

Some victims signed a permit instead of approving the attacker directly, the guide says. This gives the attacker an allowance inside Permit2, which needs a separate check. On revoke.cash, these allowances appear as their own rows with the actual spender and an expiry note under the amount. Users can find them through the spender search.

A row naming Permit2 itself shows the token's approval to the Permit2 contract. The guide distinguishes this from the allowance granted to an individual spender inside Permit2. Revoking the token approval to Permit2 also cuts off an attacker allowance for that token, it says. The user will then need a fresh approval the next time they use an app that requires it.

Each matching revocation must be confirmed in the wallet as an on-chain transaction. The guide tells users to retain enough of the network's gas token to submit it: $ETH on Ethereum, Base, Arbitrum and Ink, and $BNB on $BNB Chain. After revoking, users are told to reload and confirm that matching rows have disappeared or show an allowance of 0 on every network reviewed.

## Unused permits remain a separate exposure

A signed permit that the attacker has not submitted will not appear on revoke.cash, the guide warns. It recommends that anyone who signed anything on the compromised site that day revoke visible permissions and move remaining assets to a new wallet. Even with a clean list of visible approvals, an unsubmitted signature can leave the wallet exposed.

Revoking a permission prevents future theft; it does not recover assets already taken. The guide also distinguishes approvals from plain transfers. If a visitor sent $ETH or another coin directly to the attacker, there is no approval to revoke for that transfer. For users unable to revoke immediately, it recommends moving affected tokens out of the wallet, since an open approval can drain tokens held there.

Across's guide warns that the team will never send the first direct message, request a seed phrase or private key, or ask someone to validate or sync a wallet on a website. Affected users are asked to initiate contact themselves and supply transaction details.

In the domain disclosure, Across said Namecheap had been unresponsive and that it could not yet secure the domain sufficiently to restore service. It committed to keeping both the frontend and API down until it could secure them. Across promised a postmortem explaining how the takeover happened; the disclosure gives no restoration deadline.
