---
layout: blog
title:  StakeWithUs
permalink: stakewithus
h1title: StakeWithUs staking-as-a-service provider
pagetitle: StakeWithUs - staking-as-a-service provider. StakeWithUs Review.
metadescription: Oliver, co-founder of StakeWith.Us talks about infrastructure and scalability built around adoption driven projects, staking-as-a-service providers and the future of DeFi.
category: blog
featured-image: /images/blog/stakewithus-og.png
quote: /images/blog/stakewithus-quote.png
intro: 'Oliver, co-founder of StakeWith.Us talks about infrastructure and scalability built around adoption driven projects, staking-as-a-service providers and the future of DeFi. '
author: Defiprime
---
Oliver, co-founder of StakeWith.Us talks about infrastructure and scalability built around adoption driven projects, staking-as-a-service providers and the future of DeFi.

### Hello! What's your background, and what are you working on?

Hi, I am Oliver Wee, CTO, and Co-Founder of [StakeWith.Us](https://stakewith.us/). I interned at JPMorgan Chase with the Production Management Team building tools for access control dashboard before moving on to be the Lead Software Engineer for RKR Capital's crypto trading arm.

StakeWith.Us is a [staking-as-a-service provider](/staking) building secure and highly reliable blockchain infrastructure to power the next generation of Proof of Stake blockchain protocols catered to all investors. We are currently live and validating for Loom Network, Cosmos Network, and Terra Money with a strong pipeline of validation projects onboarding by the end of 2019.

### What's StakeWithUs backstory?

We started in this space right around early 2017 as an investment firm focused exclusively on the blockchain space. Our core investment thesis focused on infrastructure and scalability built around adoption driven projects. We believe that it will come in 3 forms: Blockchain Agnostic Scalable Layer 2 solutions, Application Specific Blockchains that are interoperable and novel PoS blockchains.

Towards the end of 2018, as some of our portfolio projects delivered on their milestones, these networks started onboarding validators. As investors with a longer-term outlook in the space, we decided to build our own staking as a service provider with our own private funding.

The team we've built has deep expertise across financial markets, algorithmic cryptocurrency trading, cybersecurity, DevOps, and software development. As we continue to grow our team and scale-out our pipeline of validation projects, we continue to strive towards our vision of offering a service that allows for everyone to participate in securing decentralized networks.

![](/images/blog/StakeWithUs1.jpg)
_From left to right: Amit Karpe, Michael Ng, Oliver Wee (that's me!), Mervyn Chng and Do Ngoc Tan (Not in picture). Come StakeWith.Us :)_


### What went into building the StakeWithUs?

It took us three months of planning and R&D to launch our staking service right in the midst of the bear market. After weighing all the risks involved in staking, we decided to focus on growing and scaling our team, prioritizing security above all else. This does not mean we do not care about the availability of our validation setup, but that we will always choose the most secure option even if it means to have acceptable periods of downtime.

![](/images/blog/StakeWithUs2.png)

We have two servers located in two separate Tier 3 Datacenters hosting our validators in Singapore. We found the Yubi2HSM to be very useful in generating roles and set capabilities for validation, allowing us to multisig secrets and backups to be stored securely in well-protected bank vaults. We also deploy our sentries across multiple availability zones via multiple service providers.

We had previously [published an article summarizing our learnings](https://medium.com/stakewithus/our-validation-architecture-and-learnings-at-stakewith-us-1876470ec908) from launching StakeWith.Us, and in general, we find HashiCorp tools to be very useful.

Some of the improvements in our setup are:
1. Utilising Wireguard VPN to reduce latency between sentries and validators,
2. Using Consul for service discovery and health checks,
3. Terraform to manage multi-cloud infrastructure and
4. Implementing Nomad to assist with container management.

One technical limitation which we faced is with existing KMS solutions - It is not very flexible about key management policies. With our own custom Javascript KMS connector, we are able to implement our own rules and policies. Existing (open-source) KMS solutions also does not validate votes or proposals, which is also why we are building a KMS with distributed consensus that trades availability for strong consistency and hence double signing protection.

### What's your business model?

There are two business models in the staking-as-a-service industry. The most common being the fee-based delegation model as seen in the tendermint ecosystem, charging a fee ranging from 0-25% of delegators yield. This is pretty straightforward as separation of delegator and validator rewards have been seamlessly incorporated within the protocol for most projects that we are validating for.

Another revenue stream is to offer white label services to larger institutions like funds, exchanges, custodians who might be interested in engaging staking services for tokens that they or their clients/users own. These validators will be operated under our validation infrastructure and without technical hassles while retaining the branding of the institution.

Currently, the majority of our projects are on a commission-fee model. However, we are also providing white label services to larger token holders for various projects.

Our first validation project was [Loom Network](https://loomx.io/) (which we have been involved with since late 2017) which we started work on in late 2018 on their testnet. We launched on mainnet as the first validator in February 2019 and started opening up to delegations from the Loom community.

There are many professional staking-as-a-service providers in the market operating under similar setups, and we think that these best practices will eventually lead to tech commoditization. We try to contribute by sharing our own research on topics like [HSM Policies ](https://medium.com/loom-network/hsm-policies-and-the-importance-of-validator-security-ec8a4cc1b6f)and [lessons learnt from improving our architecture](https://medium.com/stakewithus/our-validation-architecture-and-learnings-at-stakewith-us-1876470ec908).

We believe that staking-as-a-service providers will differentiate through branding in their key target markets. Although there might be overlaps in the projects that professional staking services choose to validate for, we believe that differentiation will come from a project to project basis. This can come in the form of community contributions to the projects - hosting meetups, contributing code, voice in the governance process, providing resources (oracles, product nodes, etc.).


### What's your position on the regulatory landscape today?

We've recently seen a lot more scrutiny from regulators as digital assets gain adoption even by big technology companies like Facebook. We believe these discussions to give more clarity to the regulatory landscape will be very beneficial to the industry in the long run. With regards to Proof of stake, we are glad to see more involvement from various stakeholders working together to educate regulators and lawmakers about the benefit of Proof of Stake as well as to address regulatory uncertainty that could limit innovation.

For example, the recently established [Proof of Stake Alliance (POSA)](https://www.proofofstakealliance.org/) are representing PoS protocols interests to regulatory agencies by serving as a platform for the staking industry and a forum to create best practices. Other key areas of regulatory uncertainty, including the tax treatment of Proof of  Stake assets and security law matters.

For StakeWith.Us, we are blessed to be based in Singapore, where the government has been very forward-looking with regards to new technologies even [investing and supporting some of these blockchain focused startups alongside co-investors](https://e27.co/aiming-at-deep-tech-startups-sginnovate-partners-with-five-new-co-investors-20190427/) that have a proven track record.


### What are your goals for the future?

We believe that we are witnessing a shift in the blockchain industry from Proof of Work based networks to more cost-efficient and environmentally friendly Proof of Stake based networks. The lower energy and hardware costs makes the role of validating transactions more accessible to everyone than traditional Cryptocurrency mining.

Our core vision at StakeWith.Us is to enable everyone to participate in securing decentralized networks in a fuss-free and secure manner. We plan to accomplish this by focusing on our core infrastructure tooling and customized KMS solutions. Security is core to our business and will remain our primary focus as we onboard new projects in the pipeline. We also intend to build out more product features via an iterative process to cater to our user's needs.


### What are your future thoughts for the DeFi market?

Defi and the ideas behind Open Finance is probably one of the only use cases in the blockchain where we are witnessing real-world adoption with [$500MM USD locked in DeFi.](https://defipulse.com/)

We think staking derivatives, insurance-based products, and other financial schemes will emerge within the next 12 months. As long as there are ways to make these markets efficient, these products will thrive.  While the market is small right now, we believe that there is huge room for growth in the near future.


### Where can we go to learn more?

Feel free to engage us on our various social media channels:

- [Website](https://stakewith.us/)
- [Telegram Group](https://t.me/StakeWithUs)
- [Telegram Announcement Channel](https://t.me/stakewithusann)
- [Twitter](https://twitter.com/StakeWithUs)
- [Medium](https://medium.com/@StakeWithUs)
