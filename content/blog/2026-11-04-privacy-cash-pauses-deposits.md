---
layout: blog
title: "Privacy Cash pauses deposits to strengthen wallet screening"
url: /privacy-cash-pauses-deposits.html
h1title: "Privacy Cash pauses deposits to strengthen wallet screening"
pagetitle: "Privacy Cash pauses deposits, says withdrawals remain open"
metadescription: "Privacy Cash paused deposits after citing the Binance hack and plans stronger wallet screening; the operator says withdrawals remain available."
category: blog
featured-image: /images/blog/privacy-cash-pauses-deposits-ogp.png
intro: "Privacy Cash has temporarily paused deposits to strengthen wallet screening, while saying existing users can still withdraw."
author: sawinyh
tags: ["News"]
date: 2026-11-04T17:27:33+00:00
---

On November 4, 2026, Privacy Cash [announced a temporary pause on deposits](https://x.com/theprivacycash/status/2118013653966364974), citing what it called the recent Binance hack. The operator said withdrawals would remain available while it strengthened its wallet screening system. Withdrawal availability has not been independently tested for this report.

Privacy Cash said it wanted to prevent criminal use of the product. “When we started Privacy Cash, our goal was to make privacy tools for everyday people, not to enable crime,” it wrote. “In light of the recent Binance hack, we want to make sure bad actors can’t use our product.” The post gave no incident amount and identified no transaction involving funds that had entered Privacy Cash.

## Deposits already pass through wallet screening

Privacy Cash's [documentation](https://privacycash.mintlify.app/) describes a protocol for private transfers and swaps. It lists Solana, Ethereum, Base and Robinhood Chain among the supported networks. The protocol uses zero-knowledge proofs, an append-only Merkle tree and a relayer system to break the on-chain link between deposits and withdrawals, according to the docs. The announcement covers Privacy Cash deposits generally. It gives no chain-by-chain account of how the pause has been implemented.

The documented deposit process already includes wallet screening. “Your signed deposit transaction is sent to a relayer, which screens your wallet address through CipherOwl,” the documentation says. “If your address is flagged as malicious, the deposit is rejected.” Privacy Cash described the work during the pause as strengthening this existing system. CipherOwl is also named in the service terms that predate the announcement.

The [service terms](https://docs.google.com/document/d/1gPXLC2a7ehT_T2bYOeZt0v2OCpyk4CYrGYhCuDOgXcw/export?format=txt) explain what users consent to when they use those relayers. The provisions cover wallet address screening and risk assessment, possible denial of service when CipherOwl flags a wallet, and compliance checks intended to maintain a clean liquidity pool. These checks govern access to the service: a wallet can be screened when it deposits even though the privacy mechanism aims to obscure the link between that deposit and its eventual withdrawal.

The terms prohibit money laundering, terrorist financing, sanctions evasion and circumvention of legal restrictions. They also prohibit processing criminal proceeds and mixing funds derived from theft or fraud. The terms carry a last-updated date of October 29, 2025, preceding the deposit pause. These restrictions on permitted use were already in place when Privacy Cash announced that it would strengthen screening.

Privacy Cash reserves the right to terminate or suspend access at any time, without notice. The listed grounds include a terms violation, a CipherOwl flag, a requirement imposed by law or regulatory authorities, and discontinuation of the service. In this case, the announcement cites screening work and the Binance hack. It identifies no legal demand behind the pause and does not say that a regulator ordered it.

## What the docs say about withdrawing

The documentation describes a client-generated zero-knowledge proof that binds the withdrawal instructions. “A zero-knowledge proof generated on the client ensures that the relayer cannot modify the recipient address, amount, or other parameters,” it says. “Any tampering will cause the on-chain transaction to fail.” That protection is described by the project in its documentation; the deployed contracts have not been freshly verified for this report during the pause.

The docs give a more Solana-specific account of how balances are recorded. Each deposit and withdrawal creates an encrypted UTXO that is submitted to the Solana program on-chain. Those encrypted UTXOs are then indexed off-chain. According to the documentation, only the user who holds the encryption key can decrypt the UTXOs and spend the balance.

The client derives that encryption key deterministically when the user signs a fixed message. Privacy Cash says only the user can access the key unless it is leaked, intentionally or unintentionally. The documentation specifically names phishing as a way the key can leak and warns: “Don’t blindly sign messages on phishing sites!” This warning covers exposure of the user's encryption key, a separate risk from the wallet screening checks applied to deposits.

For withdrawal destinations, the docs recommend first using a clean, new noncustodial wallet. They name Phantom, Solflare, Backpack, Coinbase Wallet, Rabby and Metamask as examples. Users can then send funds from that wallet to centralized applications. The documentation gives a processing reason for this advice: centralized exchanges and Revolut may require manual handling that takes days or longer. Those potential delays occur at the receiving service, beyond Privacy Cash's own statement that withdrawals remain available.

## Privacy limits and outstanding details

Privacy Cash's documentation also warns about limits to transaction privacy. An observer may infer a connection when a unique amount is deposited and the same amount is withdrawn shortly afterward. The docs specifically describe examining on-chain activity through SolScan or other explorers. The project's claim that its mechanism breaks the direct link between deposits and withdrawals comes with this warning: amounts and timing can still allow an observer to infer a connection.

The terms reserve a further right: “Privacy Cash reserves the right to log the transactions metadata.” That sentence specifies neither the metadata fields that would be retained nor a retention period. The provision appears in the existing service terms alongside consent to wallet screening. It addresses transaction metadata separately from the documentation's account of encrypted UTXOs and the keys used to read and spend those balance records.

The same terms warn that software and smart-contract risks can cause partial or complete loss of deposited capital despite audits and best practices. “No audit or security measure can guarantee complete safety,” they say. “Bugs, exploits, or unforeseen technical issues may occur at any time.” These are standing risk disclosures in the service terms. The pause announcement does not report an exploit of Privacy Cash's contracts.

Privacy Cash has promised updates on resuming deposits but has provided no reopening date. It has also not specified which changes to its screening system must be completed before deposits resume.
