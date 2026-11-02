---
layout: blog
title: "Nvidia, Costco and Nike Object to OKXICE Stock Tokens"
url: /okxice-nvidia-costco-nike-issuer-objections.html
h1title: "Nvidia, Costco and Nike Object to OKXICE Stock Tokens"
pagetitle: "Nvidia, Costco and Nike Object to OKXICE Stock Tokens"
metadescription: "OKXICE's October 30 notice lists Nvidia, Costco, Nike and Micron among objectors. Timely objections block the affected third-party stock tokens on the venue."
category: blog
featured-image: /images/blog/okxice-nvidia-costco-nike-issuer-objections-ogp.png
intro: "OKXICE's October 30 public notice names Nvidia, Costco, Nike and Micron among issuers objecting to tokenized stock trading on the planned venue."
author: sawinyh
tags: ["News", "RWAs"]
date: 2026-11-02T16:32:12+00:00
---

On October 30, 2026, OKXICE named Nvidia, Costco, Nike and Micron among the companies that had submitted issuer objections to its tokenized securities venue. The [updated public notice](https://www.okx.com/cdn/assets/okfe/web3-activities/okxicetsv/notices/OKXICE_Tokenized_Securities_Venue_Public_Notice_26.10.30.pdf) also lists Palo Alto Networks, Reddit, Hewlett Packard Enterprise, IREN, USA Rare Earth and Bloom Energy.

A timely objection blocks the venue from making the affected third-party-tokenized stock available for trading under the SEC's exemption. The restriction covers the stocks proposed for trading on OKXICE. The venue's design pairs stock tokens with payment stablecoins in permissioned Uniswap v4 pools on XLayer.

The disclosure follows [the earlier issuer objections reported by defiprime](/okxice-nine-issuers-object-tokenized-stocks.html). Microsoft, Alphabet, Goldman Sachs, JPMorgan, Walmart, Coca-Cola and Eli Lilly also appear in the current list. The objection section names companies and their stock symbols; it does not reproduce their letters or explain their reasons.

## How an objection blocks a stock token

The mechanism comes from the [SEC's conditional exemption for tokenized securities venues](https://www.sec.gov/files/rules/exorders/2026/34-106402.pdf). Before offering a stock token created by an unaffiliated third party, a venue must notify the issuer of the underlying stock in writing. Trading cannot begin until at least 30 calendar days after the issuer receives that notice.

The SEC's [staff FAQ](https://www.sec.gov/rules-regulations/staff-guidance/trading-markets-frequently-asked-questions/frequently-asked-questions-innovation-exemption) explains the consequence of an objection: the venue must amend its public notice to disclose a timely objection and cannot make that tokenized stock available for trading. If the objection period expires without a timely objection, the venue can make the stock token available and must update its notice to remove the pending designation.

The order requires a revised public notice within five business days after receipt of a timely objection. The date on an updated list therefore records the disclosure, not necessarily the date each company sent its objection. The October notice supplies no individual submission dates beside the named issuers.

A separate notice period governs the venue's operations. Its public disclosure must appear at least 30 calendar days before operations commence. SEC staff says that disclosure should be published after operations and access standards are established and ready for production. The FAQ expresses staff views and has no independent legal force; the conditions come from the Commission's order.

## What OKXICE proposes to trade

OKXICE LLC is a Texas company owned equally by Intercontinental Exchange Holdings and OKC USA Holding. Its notice describes a market for both issuer-tokenized stock and stock tokenized by an unaffiliated third party. For third-party stock tokens, the tokenizer acts through an SEC-registered, FINRA-member broker-dealer. The broker-dealer holds underlying shares one-for-one against outstanding tokens.

Each token represents a security entitlement to one underlying share. The blockchain records ownership and transfers. The tokenizer then incorporates those records into its books and reconciles them. The notice identifies payment stablecoins such as $USDC and $USDG as the assets paired with tokenized stocks.

Minting follows the purchase and custody of the underlying stock. The tokenizer routes the purchase through its broker-dealer and issues tokens only after confirming acquisition and custody. Redemption runs through the tokenizer as well: it burns the tokens, then sells or delivers the corresponding shares, returning proceeds or shares under its redemption terms.

The venue's listing checks require equivalent shareholder rights, including dividends, voting rights and a share of residual assets on liquidation. Proxy materials and other issuer communications must reach holders without cost to either holders or issuers. OKXICE says it reviews legal and contractual representations supporting those rights.

To check the backing, OKXICE reviews the tokenizer's latest reserve attestation, issued or verified by an independent accounting firm. It also reviews written procedures for distributions, proxy voting and adjustments for corporate actions such as splits and mergers. If a stock token ceases to provide the required rights, the notice says OKXICE will stop making it available for trading.

## Public chain, restricted access

XLayer is a public, permissionless blockchain, but admission to these pools depends on OKXICE credentials. Users must pass identity, anti-money-laundering, sanctions and wallet screening, and obtain approval for a tokenizer account. OKXICE then issues a non-transferable soulbound token to the wallet, while the tokenizer adds that wallet to its approved list.

The venue's hook checks those credentials for trading and liquidity actions. Only OKXICE can create pools using its hook. Credentialed wallets can interact directly with the contracts or through custom integrations, but third-party smart contracts need separate whitelisting. The notice says the venue currently does not support aggregators, solvers or relayers.

Liquidity providers receive a receipt token with no governance rights. OKXICE has no governance token or on-chain voting mechanism. Administrative powers include upgrading contracts, pausing trading, changing the permissioning list and withdrawing a liquidity provider's liquidity. Multiple authorized personnel must approve administrative transactions. The risk disclosure says changes take effect without a timelock, so participants may receive no advance notice of an upgrade.

The ratio of assets in each pool determines prices for any eventual stock positions. Those prices can differ from prices in the underlying stock market. OKXICE warns that token prices may diverge from underlying shares, particularly outside the primary exchange's regular hours, when pool liquidity is low, or during halts and corporate actions.

The notice also says OKXICE is not SEC-registered for activities under the exemption, that the SEC has not passed on the merits or accuracy of its disclosures, and that the venue is outside Regulation NMS and the specified exchange and ATS fair-access requirements.

The [public landing page](https://www.okx.com/okxicetsv) still describes OKXICE TSV as coming and directs readers to the October 30 notice. The page gives no launch date, and the objection list does not disclose the individual issuers' reasons.
