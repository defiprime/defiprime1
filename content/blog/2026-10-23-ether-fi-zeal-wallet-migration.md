---
layout: blog
title: "Ether.fi opens Zeal migration as wallet and card services wind down"
url: /ether-fi-zeal-wallet-migration.html
h1title: "Ether.fi opens Zeal migration as wallet and card services wind down"
pagetitle: "Ether.fi opens Zeal wallet migration"
metadescription: "Zeal users can opt into ether.fi as card services end December 20. Unsupported assets convert with fees; existing Safe access needs attention."
category: blog
featured-image: /images/blog/ether-fi-zeal-wallet-migration-ogp.png
intro: "Ether.fi has acquired selected Zeal assets and opened an optional migration as Zeal winds down its wallet and card services."
author: sawinyh
tags: ["News"]
date: 2026-10-23T16:26:26+00:00
---

On October 23, 2026, [ether.fi announced its acquisition of Zeal](https://x.com/ether_fi/status/2113647301046788374) and opened an in-app route for Zeal users to move to its account and card product. Zeal says the deal covers selected assets, not user accounts, keys or funds, as its wallet winds down.

The move is optional. In its [own announcement](https://x.com/zealwallet/status/2113649405048082914), Zeal said: “You choose what to move, and nothing moves automatically.” Its [follow-up statement](https://x.com/zealwallet/status/2113649407702773889) describes ether.fi as a self-custodial Visa option for users whose Zeal wallet and Gnosis Pay card services are ending.

[Gnosis Pay’s migration guide](https://help.gnosispay.com/articles/9340240615-which-apps-you-can-move-to) says Zeal’s card services will be wound up by December 20, 2026. The guide also describes other ways to keep a Gnosis Pay account. Zeal users can choose those routes instead of moving to ether.fi.

## What moves to ether.fi

The [live migration page](https://www.ether.fi/zeal) sets out four steps. Users start from the Zeal home screen and supply an email address. Entering the emailed six-digit code creates an ether.fi account. Zeal then moves the selected balance and assets into the new account. The final step is identity verification with ether.fi, followed by setting up the card.

Supported assets move across unchanged. Unsupported assets are converted during the move, incurring network fees and potentially losing some value in the conversion. The page invites users to bring their whole balance, but warns that conversion can reduce its value. It supplies neither a conversion quote nor an asset-by-asset migration table.

Opening the account creates a separate legal relationship with ether.fi. The migration page says ether.fi and Zeal remain separate companies. Users of the new account come under ether.fi’s terms and privacy policy. Eligibility, availability, fees, limits and restrictions apply; crypto assets can lose value and returns from earning products are not guaranteed. Identity verification is required before all features become available.

## Keeping access to the existing Safe

Before Zeal users lose access to the old interface, Gnosis Pay’s guide tells them to add another wallet they control as a second owner of their Safe. It gives MetaMask and Rabby as examples. It says this lets them sign into the Gnosis Pay web app with that wallet and manage the account, including withdrawals. Without it, transactions still require signatures inside Zeal.

The same guide warns users taking its partner-migration route to withdraw assets from Zeal’s earn product back to their balance first. Assets left in earn will not be picked up. It specifically says Rebind’s migration tool moves assets on Gnosis and Base automatically. Those instructions describe the Gnosis Pay partner route; ether.fi’s migration page does not give equivalent detail about handling existing earn positions.

For EUR cardholders, Gnosis Pay recommends Rebind. Its guide says the account, IBAN and card carry over without new identity checks, with the existing card unchanged at that stage. Users choosing ether.fi’s published flow create a new account and complete verification before setting up the card.

Gnosis Pay describes its partner transition as a staged process. Some partner apps initially import the existing card and Safe setup. Later, when the partner programme goes live, users accept new terms and receive a partner card, with advance notice. Where the partner supports importing the existing card, users keep it for the initial move, with the replacement card coming later in the transition.

## Spending balances or borrowing against them

Ether.fi’s [Direct Pay documentation](https://etherfi.gitbook.io/etherfi/products/cash/direct-pay) lists $USDC, $USDT, $EURC and $frxUSD as spendable stablecoins. It also lists Liquid USD, Liquid RWA, Liquid Reserve and Liquid EUR vault balances. Card payments can draw directly from those vault balances without a prior withdrawal.

The Set Spend Priority control selects which balance pays first. If that balance cannot cover a purchase, the card uses another balance that can. The documentation lists these assets for spending in the destination product. It does not list every asset supported by the Zeal migration.

Users who borrow also take on lending and collateral risk. According to [ether.fi’s Borrow guide](https://help.ether.fi/en/articles/764754-how-borrow-works), eligible assets are supplied to a dedicated onchain lending market managed by ether.fi, earning variable rates determined by supply and demand. Eligible assets act as collateral automatically, and each has its own loan-to-value limit. Both the assets in the portfolio and their total value determine how much a user can borrow.

Loans must remain overcollateralized. Reaching the liquidation threshold shown in the app triggers the automatic liquidation of some collateral to restore the position. Limits on new borrowing cannot prevent market movements from pushing a position toward that threshold. Borrow can be switched off in settings once no borrowed amount remains outstanding, leaving the card operating in Direct Pay.

The [terms of use](https://www.ether.fi/legal/terms-of-use) separate protocol lending from the card issuer. They describe overcollateralized credit through decentralized borrowing protocols, with borrowing eligibility and limits set by protocol parameters. The issuer supplies the card used to access that credit; it does not originate the protocol loan.

## Cashback has separate conditions

Ether.fi’s Zeal page advertises 3% cashback on eligible purchases up to the applicable monthly limit. The acquisition announcement advertises up to 4%. The migration page does not explain what would qualify a migrating user for the higher advertised rate.

The [cashback programme terms](https://etherfi.gitbook.io/etherfi/legal/ether.fi-legal/ether.fi-cash-cashback-rewards-program-u.s.-and-international) exclude ATM withdrawals, peer-to-peer payments, tax payments, currency exchange services, gift cards and other cash equivalents. They also permit reversal of rewards after a refund, cancellation or chargeback, including by debiting the account, reducing future rewards or reducing the refund by the original reward’s dollar value.

The migration page has not published an asset-by-asset conversion schedule or explained how existing Zeal earn positions are treated in its own flow. Gnosis Pay’s stated December 20 deadline covers Zeal card services; ether.fi’s page gives no separate closing date for its migration offer.
