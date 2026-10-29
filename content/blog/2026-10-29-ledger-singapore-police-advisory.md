---
layout: blog
title: "Singapore police warn of tampered Ledger wallets after losses"
url: /ledger-singapore-police-advisory.html
h1title: "Singapore police warn of tampered Ledger wallets after losses"
pagetitle: "Singapore police warn of tampered Ledger hardware wallets"
metadescription: "Singapore police report losses tied to tampered Ledger wallets. Ledger describes seed-stealing implants and tighter reseller rules."
category: blog
featured-image: /images/blog/ledger-singapore-police-advisory-ogp.png
intro: "Singapore police warned that tampered Ledger wallets sold through local retailers could expose recovery phrases and let attackers drain assets."
author: sawinyh
tags: ["News"]
date: 2026-10-29T19:29:13+00:00
---

Singapore police warned on October 28, 2026, that tampered Ledger hardware wallets purchased from retail stores in the country had been linked to at least two reported cases since September 10. The [police advisory](https://www.police.gov.sg/Media-Hub/News/2026/10/20261028_police_advisory_on_tampered_cryptocurrency_hardware_wallets) puts total losses at about $3.5 million, without explicitly identifying the currency.

Preliminary investigations found malicious hardware components capable of capturing recovery phrases or private keys. These could give unauthorized people access to wallets and allow them to transfer assets. Police said they were in contact with Ledger, which was reviewing the affected cases. Investigations remain ongoing.

The advisory tells users to stop entering recovery phrases or making further transactions on devices they suspect have been tampered with. Where keys may have been compromised, police recommend considering a transfer of remaining assets to a trusted wallet with a newly generated recovery phrase, using an uncompromised device.

## What the implant captures

Ledger described the mechanism in an [October 13 statement from its official account](https://x.com/Ledger/status/2109896739985453358). Its Donjon security team found an implant inside the enclosure that reads data shown on the device's screen. During setup, the device displays the 24-word recovery phrase. The implant's microcontroller decodes those words and transmits them over LTE through a provisioned eSIM.

“The implant is a separate component,” Ledger wrote. “It does not modify the Secure Element or the Ledger operating system, and it does not alter transactions or signatures.” Ledger's account describes the implant intercepting the recovery phrase on the display without changing those signing components.

In its [response last updated October 15](https://support.ledger.com/article/Ledger-s-Response-to-the-Hardware-Implant-Attack), Ledger said the attackers bought genuine devices, opened them, fitted hidden components and put them back into distribution through Southeast Asian resellers. It described an operation prepared over many months, with infrastructure for collecting seed phrases, draining wallets and laundering proceeds.

Ledger called it a localized attack on distribution after the devices had left its control. The company said its chip, operating system and servers were not compromised. These are Ledger's findings and its account of the attack; the later Singapore notice describes the police investigation as preliminary.

## What the earlier findings establish

The October 13 statement identified CryptoBilis, a Southeast Asian reseller, as the source of devices connected to all fund losses Ledger had confirmed in the incident disclosed on October 9. Ledger said it confirmed an unauthorized implant in one affected user's device on October 10. At the time of that statement, it had not verified a drain linked to a device purchased elsewhere.

CryptoBilis had stopped selling Ledger devices while the investigation continued, according to Ledger. The earlier statement also said Ledger had not confirmed the total number of affected users or total value lost. The Singapore police advisory gives a later, local case count and loss figure. It does not identify the retail stores involved or connect its cases by name to CryptoBilis.

A separate [Ledger statement on October 13](https://x.com/Ledger/status/2109984923343782374) said MediaMarkt Saturn had stopped selling Ledger devices in stores and online, with Ledger's agreement, after a customer in Germany reported an implant. That update reported no loss of funds, so the German report should not be counted as another confirmed drain alongside the Singapore cases.

Ledger's longer response said Donjon had dismantled the implant to identify how it worked. Teams also bought and opened devices from stores, including in Germany, and inspected warehouse samples. Ledger reported that every unit in those examinations was clean. In a separate screening of its own stock, the company likewise found no compromised units among the samples checked.

## Reseller handling rules changed

Ledger said it asked authorized resellers and distributors to suspend sales in Southeast Asia and Hong Kong. This precautionary suspension covered a broader area than the earlier CryptoBilis-specific announcement. The response gives no date for resuming those sales.

The company also reminded its authorized network that returned devices could never be resold in any form, even if they appeared new and unopened. According to Ledger, this rule was already in place. The response reiterated the existing ban on putting returned devices back into resale inventory.

New handling requirements took effect immediately in the October 15 response. Ledger products should no longer sit on shelves or displays. Retailers should keep stock in the back and hand it over at purchase. They should also promptly report customer accounts of unusual products. The requirements cover how the authorized network holds and delivers devices after distribution.

Ledger said it was working with law enforcement and the security community to trace funds and dismantle the attackers' infrastructure. The company was also developing additional product-level measures against this kind of attack, but gave no details of those measures in the response.

## Handling a suspected device

Ledger's instructions for CryptoBilis customers distinguish unused devices from wallets already set up. Buyers who have not initialized a device should leave it unset and contact support. Those who have should transfer assets promptly to a new device with a new recovery phrase. Ledger specifically warns against entering or restoring any recovery phrase on a device bought from CryptoBilis.

Ledger also gives instructions for preserving suspected devices. People who lost funds or hold a tampered device should contact official support and file a local police report. They should not send the device to anyone before speaking with support or law enforcement. People who lost funds should coordinate with law enforcement before opening it; Ledger warns that opening a device can damage it.

The police warning extends to recovery scams. Users should never give private keys or seed phrases to anyone claiming to represent a wallet provider, exchange or law enforcement agency. Police also warn against unsolicited wallet-verification or recovery offers. Ledger says it will never call users, message them directly or ask for their recovery phrase.

Singapore police have not named the affected stores in the advisory. Ledger's response promises a fuller technical disclosure when it can provide one, without giving a publication date.
