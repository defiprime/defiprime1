---
layout: blog
title: "Pumpfun ends wallet sign-in, asks existing users to import keys"
url: /pumpfun-retires-wallet-login.html
h1title: "Pumpfun ends wallet sign-in, asks existing users to import keys"
pagetitle: "Pumpfun retires external wallet login on November 30"
metadescription: "Pumpfun ends external wallet sign-in on November 30. Its account migration asks for private-key imports, while a fresh-account option leaves history behind."
category: blog
featured-image: /images/blog/pumpfun-retires-wallet-login-ogp.png
intro: "Pumpfun will replace external wallet sign-in with email and social accounts, requiring a private-key import to retain an existing account through its migration flow."
author: sawinyh
tags: ["News"]
date: 2026-11-22T11:23:02+00:00
---

Pumpfun will retire external wallet sign-in on November 30, 2026, at 15:00 UTC. Its [migration notice](https://pump.fun/docs/wallet-login-changes) replaces sign-in through wallets such as Phantom, Solflare and Ledger with email, Google, Apple or GitHub accounts. Keeping an existing account through the recommended migration requires importing its wallet’s private key. Users can instead create a new account and wallet, leaving their history on the old address.

The Pump mobile app already uses the new login model, according to the notice. Users who retain their accounts keep their wallet addresses, positions, callouts, followers and usernames: “This is only about how you sign in.” The notice sets a deadline for changing how users log in, not for withdrawing funds, and trading continues.

## Keeping an account requires a key import

Pumpfun’s recommended route starts inside an existing signed-in account. The user opens “Link email & socials” on the profile card, which brings up a “Create account” window. They select the wallet they are already signed in as, then supply its private key. Under these instructions, retaining the account requires importing that key. Linking an email through a signature from the external wallet is not the migration process the notice describes.

Pumpfun says the key is encrypted in the browser and held end-to-end encrypted by its login provider, Privy. The wallet continues working for other uses, according to the notice. After adding an email, Google or Apple login, the user can sign in with that identity on both web and mobile. External wallet sign-in for the migrated address is then “switched off for good.”

The sequence in the account window determines which account the user gets. Selecting email or a social login before selecting the existing wallet starts a separate, empty account with a new wallet. Pumpfun says the window asks for confirmation before creating it. If a QR code appears, the wallet already has an account created in the mobile app. The notice directs those users to add their login in the app instead.

Users can also migrate through the app by importing the wallet there, then linking email or social accounts in Settings. They can subsequently use the same identity to sign in on the web. This route moves the import into the app; it still requires importing the wallet to preserve the account through the process Pumpfun describes.

Users who choose not to import can create a new email or social account, receive a new Pump wallet and transfer funds from the old wallet. Their history stays attached to the old address. Pumpfun directs Ledger, multisig and other users whose keys cannot be exported to this fresh-account option. The notice gives those users no route to migrate while keeping the same account.

## What Privy says happens to imported keys

Privy’s [wallet-import architecture](https://docs.privy.io/wallets/wallets/import-a-wallet/architecture) describes how a private key is encrypted for its trusted execution environment, or TEE. An initialization request retrieves a temporary public key from the Privy API. Before transmitting the wallet’s private key, the importing client encrypts it with Hybrid Public Key Encryption. Privy says only the TEE can decrypt the payload.

Inside the TEE, the payload is decrypted and the private key initializes a wallet. The temporary keypair used for the import is then destroyed to maintain forward secrecy. These steps describe Privy’s published architecture. They are not an independent audit of Pumpfun’s browser implementation. Pumpfun names Privy and describes browser encryption in its notice, but publishes no implementation-specific security assessment alongside the migration instructions.

Privy’s [export documentation](https://docs.privy.io/wallets/wallets/export) also describes how users can retrieve keys. Users normally authenticate directly to its API with their access token. Under that default, they can export keys even if an application has not implemented Privy’s export button. Whether a key can be exported depends on wallet ownership and authorization; having an account in the app alone is not enough.

Applications can configure joint authorization between a user and an application-controlled key. In that configuration, both parties must authorize an export. Privy also says a policy can disable export, and wallets without owners cannot be exported. These are options the provider makes available to applications. Pumpfun’s migration notice does not say which export policy or ownership configuration it uses for imported wallets.

## The migration guide conflicts with the terms

Pumpfun’s [Terms of Use](https://pump.fun/docs/terms-and-conditions), last updated November 16, 2026, tell users that “under no circumstances will we ask you to share your Wallet private keys, seed or recovery phrases, social-login or email credentials, one-time codes or similar.” The next sentence says: “You should never disclose these if asked.” The warning is unconditional. The migration guide asks users to supply a private key.

The guide limits that request to the account-creation window opened through “Link email & socials” inside a signed-in account on pump.fun. It says requests through direct messages, email, X or any other website are scams. The terms also assign responsibility for a generated wallet to Privy and the user. They describe Privy as unaffiliated with Pump and say Pump has no control over wallets or their private keys.

The terms require users to monitor their activity history and notify Pumpfun as soon as possible if they see suspicious wallet activity. They warn that a security breach can expose funds in the affected wallet and in associated wallets or accounts. Neither the terms nor the migration guide reports any loss of user funds caused by the login change.

## What happens after the cutoff

After November 30, an existing signed-in wallet session will show a screen asking the user to add a login. Pumpfun says the same migration choices will remain available and nothing will be deleted. The notice explicitly leaves the mobile app, API sessions and trading itself unaffected. The change applies to login for the website’s existing products, following its earlier [Hyperliquid perps launch](/pumpfun-hyperliquid-perps-launch.html). It announces no new trading venue.

Google sign-in is blocked inside wallet browsers, according to the guide, which directs users to sign in with email or open the site in Safari or Chrome. The notice gives a cutoff for web wallet login, but no date for reconciling its private-key import instructions with the contrary warning in the terms.
