---
layout: blog
title: "Confiant finds iPhone ad attacks targeting wallet seed phrases"
url: /moldyroost-iphone-wallet-seed-phrase-attacks.html
h1title: "Confiant finds iPhone ad attacks targeting wallet seed phrases"
pagetitle: "MoldyRoost iPhone ads target crypto wallet seed phrases"
metadescription: "Confiant traces MoldyRoost ads to iPhone exploit kits targeting wallet apps, saved seed phrases and private data on vulnerable devices."
category: blog
featured-image: /images/blog/moldyroost-iphone-wallet-seed-phrase-attacks-ogp.png
intro: "Confiant disclosed an advertising operation that delivers iPhone exploits targeting wallet apps and saved recovery material."
author: sawinyh
tags: ["News"]
date: 2026-11-23T08:23:58+00:00
---

On November 20, 2026, Confiant disclosed MoldyRoost, a malicious advertising operation that delivers iPhone exploits built to steal cryptocurrency wallet seed phrases. Its researchers linked more than 480 ad domains to the operation and described payloads targeting MetaMask, Phantom and Trust Wallet, as well as recovery material saved elsewhere on the phone.

The [disclosure by researchers Roshan and Eliya Stein](https://blog.confiant.com/p/moldyroost-a-malvertising-machine) describes an attack that can begin before a wallet asks for a signature. “Just loading the landing page of a MoldyRoost ad on a vulnerable iPhone is enough to get infected.” The victim need not download a file or paste a command into a terminal. The exploit runs as the page loads.

Confiant tracked the ad domains from May 12 through November 17, across six sub-clusters and more than 47 countries. The researchers found that MoldyRoost distributes exploit kits through paid advertising. They say the operation did not write the underlying kits.

## An ad click reaches the wallet through the phone

The operation buys programmatic ads and sends visitors to attacker-controlled landing pages. A router checks the visitor's iOS version and selects an exploit kit. The distribution system includes advertising accounts, disguised landing pages and a backend that attributes stolen wallets to the channel that brought in the victim.

Confiant found more evidence in mid-November when a server exposed its source code. A commit built a separate payload for each sales channel so that, in the researchers' translation, “the backend can attribute by Host”. The channel is the operation's own campaign code, which it attaches to the stolen wallet in its records.

The landing pages conceal the attack from visitors outside the target group. Safari on iOS receives an exploit chain; some sub-clusters also target in-app browsers. Other visitors receive a functioning decoy site, a harmless page or an empty frame. Someone inspecting the advertisement on a desktop can see benign content while an eligible phone receives the payload.

One example in the report uses an Agoda-themed advertisement on a Hong Kong forum. The ad opens a clone of Agoda's local site, while an invisible frame loads a separate host and selects the exploit. An 18-second loading bar absorbs further taps before forwarding the visitor to the real Agoda site, giving the hidden attack time to run.

The selected exploit chain then crosses the phone's security boundaries. Confiant describes a Safari code-execution stage, escapes from the browser sandbox and a final kernel takeover. The attacker seeks control of the device that holds the wallet, without needing a transaction submitted through the wallet interface.

Coruna's implant hooks MetaMask, Phantom and Trust Wallet. It also searches Apple Memos for seed phrases and saved images for QR codes. The researchers describe a collection path that reaches beyond the wallet app to recovery information stored elsewhere on the phone in notes or photos.

DarkSword collects wallet data alongside messages from iMessage, WhatsApp and Telegram, keychain contents, saved Wi-Fi passwords, photo metadata and location history. Confiant says one of its backdoors can record the microphone and take screenshots. The kit also cleans up crash logs as it exits, making those logs less reliable as a record of its activity.

## Known exploit ranges and the limits of the evidence

The older Coruna family was documented in [Google Threat Intelligence Group's March 3 report](https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit). Google recovered five full exploit chains containing 23 exploits, targeting iOS 13.0 through 17.2.1. Its researchers described a framework that selects an appropriate chain for the device and software version.

Google traced the kit through several uses during 2025: a surveillance vendor's customer, attacks on Ukrainian users by a suspected Russian espionage group, and broad financially motivated campaigns operated from China. Confiant's new disclosure describes another way to distribute this class of exploit, using advertisements to bring visitors into the attack infrastructure.

DarkSword targets a different software range. Confiant identifies targets from iOS 18.4 through 18.7, while noting that the sample configuration examined by iVerify stopped at 18.6.2. The kit chains six vulnerabilities and is written entirely in JavaScript. According to Confiant, Apple had fixed all six bugs by iOS 26.3.

The report also identifies branches called SilkPath and GhostWave, but the recovered repository was incomplete. SilkPath's loader path was missing. GhostWave reuses DarkSword's loader, allows its server to choose the stage and includes a fallback referencing iOS 26.3 whose file was also absent. Those references alone do not demonstrate a working exploit against the referenced version.

Google's earlier Coruna advisory urges iPhone users to install the latest iOS version and recommends Lockdown Mode when an update is impossible. That advice comes from its examination of Coruna. In Confiant's separate findings, missing payload files leave the capabilities of the additional branches uncertain. Their names and version selectors are not a complete compatibility list for working attacks.

## Separate campaigns, unresolved operators

Confiant separates MoldyRoost from the November 16 Optimizely supply-chain attack. In that incident, hijacked scripts on the sites of 178 organizations skimmed payment cards, replaced cryptocurrency addresses and delivered iPhone exploits. The iPhone stage used Coruna and DarkSword, with a version router related to one seen in MoldyRoost.

The Optimizely incident reached visitors through hijacked scripts on existing websites; MoldyRoost uses purpose-built advertising campaigns and disguised landing pages. Confiant's report includes separate lists of advertising domains and payload infrastructure. The lists distinguish sites used to launch campaigns from hosts that serve exploit frames and collect data.

Confiant assesses that the six sub-clusters share one supply chain and delivery platform, but acknowledges that separate customers of the same kit could share some of those connections. Whether one crew controls all the sub-clusters or rents parts of the operation to affiliates remains unresolved.
