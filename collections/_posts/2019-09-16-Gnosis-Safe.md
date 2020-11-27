---
git-date:
layout: [blog, blog-amp]
title:  Gnosis Safe
permalink: gnosis-safe
h1title: 'Gnosis Safe: Smart contract-based multisig wallet'
pagetitle: 'Gnosis Safe - Multisig Ethereum Wallet'
metadescription: "Tobias from the Gnosis Team told us how to securely store funds on Ethereum, with multiple signatures to authenticate transactions and an extra layer of security, and about a future of DeFi."
category: blog
featured-image: /images/blog/gnosis-safe-og.png
quote: /images/blog/gnosis-safe-quote.png
intro: "Tobias from the Gnosis Team told us how to securely store funds on Ethereum, with multiple signatures to authenticate transactions and an extra layer of security, and about a future of DeFi."
author: Defiprime
tags: ['Interview', 'Asset Management']

---
Tobias from the Gnosis Team told us how to securely store funds on Ethereum, with multiple signatures to authenticate transactions and an extra layer of security, and about a future of DeFi.

### Hello! What's your background, and what are you working on?

My name is Tobias Schubotz, I am a product manager at [Gnosis](https://gnosis.io) on the team that builds the [Gnosis Safe](https://safe.gnosis.io).

I have a background in software engineering and have been following the development of blockchain/ Ethereum for a few years. I am fascinated by the possibility of reducing costs while accelerating the execution times of complex real-world business transactions that would otherwise take days or weeks and cost significantly more.

I joined Gnosis in early 2018 to help build the next generation of smart contract wallets to bridge the gap between technology and users’ needs and to make decentralized applications more accessible.

The Gnosis Safe is a smart contract wallet that allows users to store ether and ERC20 tokens securely and interact with the decentralized web. At its core, it is a multi-signature wallet. This means that users are required to confirm transactions with both their mobile app and the Gnosis Safe Authenticator (browser extension). We are working on adding additional authentication options in the near future.

Most decentralized wallets use externally owned accounts (EOAs) on Ethereum. EOAs are controlled entirely by a private key—it is the only thing that stands between the user and full control of the wallet. This means that if your private key is lost or compromised, your funds are no longer secure. The Gnosis Safe is different. Rather than using an EOA, the Safe operates entirely with smart contracts that define access control rights and enable more sophisticated security features.

The Gnosis Safe is live on Mainnet for [Android](https://play.google.com/store/apps/details?id=pm.gnosis.heimdall) and [iOS](https://apps.apple.com/app/gnosis-safe-smart-wallet/id1447390375). We are still working on the Gnosis Safe for Teams, targeted at groups of users managing crypto funds collectively.

![](/images/blog/gnosis-safe1.jpeg)

### What's the Gnosis Safe’s backstory?

In 2016 Gnosis developed a wallet in preparation for our token sale. We wanted to build something that allowed users to securely store funds on Ethereum and required multiple signatures to authenticate transactions for an added layer of security. These requirements drove the development of the [Gnosis MultiSig. ](https://github.com/gnosis/MultiSigWallet)This multi-signature wallet became the standard for collectively managing crypto funds with over 2,500 deployed instances (the top 25 accounts hold more than 1.4M ETH collectively).

Gnosis’ core focus is still prediction markets. Outcome tokens for prediction markets could potentially gain a lot of value meaning users will need a secure way to store them. Smart contract wallets, and more specifically multi-signature wallets, are the perfect way to manage these tokens.

As the ecosystem matured and gas costs became an important factor to consider when designing a dapp, the Gnosis MultiSig smart contract got redesigned from scratch considering the following requirements:

1. Reduced gas usage by leveraging off-chain signatures instead of on-chain confirmations
2. Upgradability via proxy contracts
3. The ability to add extensions to the base contracts via delegate calls.

More importantly, smart contract wallets allow for some unique features that we intend to leverage:
* Improved access control: Instead of 1 signature, the wallet can be configured in a way that multiple signatures are required to authorize a transaction. Furthermore, transfer limits could be configured to allow single owners to authorize transactions up to a certain amount. Most importantly, we will implement recovery methods beyond backing up recovery seed phrases.
* Allowing 3rd parties to submit transactions: This concept is commonly referred to as “meta transactions”. It allows “gas less” transactions, i.e. the wallet or dapp pay transaction fees in order to reduce friction during usage. Alternatively, users could pay transaction fees in ERC20 tokens, removing the need to always have ETH in their wallet.
* Simplified interaction with other contracts: Several dapps require users to sign numerous blockchain transactions in a row to perform a single business action. Smart contract wallets can batch these together, requiring the user to sign only 1 transaction thanks to the power of delegate calls.

### What went into building the Gnosis Safe?

We identified 2 main use cases and user groups:
1. Individuals wanting to store their funds
2. Groups of people that want to manage their funds collectively.
While there are a lot of similarities, some requirements differ between these groups.

The underlying set of [smart contracts](https://github.com/gnosis/safe-contracts/) is the same for both versions, but the interfaces that users interact with are different. Individual users usually don’t own more than 2 devices (mobile phone + computer) that can be leveraged for multi-factor authentication. Also, we opted for abstracting some of the underlying tech away in favor of streamlining some app flows. The main interface for them will be the mobile app. We employ [meta transactions](https://medium.com/@austin_48503/ethereum-meta-transactions-90ccf0859e84) so users can pay transaction fees with funds stored in their Gnosis Safe. That takes away the need of always having ether on a separate account.

A relay service ensures that transactions are submitted to the Ethereum blockchain. Our relay service accepts transaction payments in ETH and ERC20 tokens. This is especially important for user onboarding. Let’s assume a user was onboarded to Ethereum via the [Burner Wallet](https://xdai.io). When a user eventually transfers these funds from xDAI to Mainnet, they would only hold DAI. This would pose an issue if they were trying to execute transactions on Ethereum without ether. With the Gnosis Safe, this would not be a problem as users can pay transactions with a variety of ERC-20 tokens including DAI.

Teams managing funds collectively care more about flexibility when setting up their Gnosis Safe. This includes parameters such as threshold and owner structure. The main interface for them is a webapp. It integrates with any [WalletConnect](https://walletconnect.org) enabled wallet and MetaMask. We are currently discussing the best way of integrating DeFi solutions with the Gnosis Safe for Teams.

The biggest threat for smart contract wallets are vulnerabilities in the contract code. To mitigate this, we had [RuntimeVerification](https://runtimeverification.com/) perform a [formal verification](https://blog.gnosis.pm/formal-verification-a-journey-deep-into-the-gnosis-safe-smart-contracts-b00daf354a9c) of the Gnosis Safe base contracts. All future updates go through a [bug bounty program](https://blog.gnosis.pm/announcing-the-gnosis-safe-bug-bounty-10e147e719c4) and have been thoroughly audited by external auditors. Additionally, Gnosis moved a significant amount of funds into a [Safe contract](https://etherscan.io/address/0xafc2f2d803479a2af3a72022d54cc0901a0ec0d6), making it a honeypot for attacks. We will continue to move more and more company funds into the Safe to motivate others to do the same.

### What's your business model?

Ethereum is still missing fund management solutions that are both secure and usable. This is mainly due to the networks innate immutability. A transaction made on the Ethereum network cannot be altered in any way. This feature is valuable but different from most other software systems. Users have to be more careful with how they use their funds which hinders broader adoption.

This challenge was one of the main motivations when starting to build the Gnosis Safe. While we intend to keep it interoperable, we see it as the main gateway to using other Gnosis products such as prediction markets and exchanges. All these products will eventually be monetized.

### What are your goals for the future?

We are currently working on allowing alternative authentication factors for the Gnosis Safe. Instead of having to confirm all transactions via the Gnosis Safe Authenticator (browser extension), users will be able to connect their hardware wallets. We are starting with the [Status Keycard](https://keycard.status.im) and will add further hardware wallet support moving forward. The hardware wallets will connect directly to mobile phones with no need to validate transactions with a laptop. We are also working on releasing the Gnosis Safe for Teams on Mainnet in the near future so users can collectively store and manage funds.

Despite their potential, smart contract wallets have not achieved widespread adoption. We are working on leveraging this potential which will include integrations with other DeFi apps and asset insurance options to provide an added layer of security for users.

### What are your future thoughts for the DeFi market?

It seems like Ethereum has found its first validated use case with DeFi. There is a globally accessible liquidity pool that applications can tap into resulting in lower transaction costs than traditional finance applications. Additionally, the recent rise of stable coins removes the inherent volatility of crypto, which has been one one of its biggest friction points to date.

Also, the costs of switching between products is much lower. That is why we believe that open platforms will ultimately benefit the user. There is less of a lock in effect and more of a focus on user needs making it easier for them to choose the product that benefits them the most.

Ultimately, no one really knows where DeFi is going. Just looking back one year, the space has changed so much. I am really curious about what share of traditional finance applications DeFi will capture and what new use cases it will make possible moving forward.

### Where can we go to learn more?

Please follow us on Twitter [@gnosisSafe](https://twitter.com/gnosisSafe) to stay up to date and reach out via [Telegram](https://t.me/gnosisSafe) or [Gitter](https://gitter.im/gnosis/Safe) for direct support. You can also take a look at [our code](https://github.com/gnosis/?q=safe), all of which is open source.
- [Website](https://safe.gnosis.io)
- [Blog](https://blog.gnosis.pm/tagged/safe)
- [Dev docs](https://gnosis-safe.readthedocs.io/en/latest/)
