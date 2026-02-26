---
git-date: 2022-02-10T11:40:51-07:00
layout: blog
title: "Application of IAD Principles to the DAO structure"
url: application-of-iad-principles-to-the-dao-structure
h1title: "Application of IAD Principles to the DAO structure"
pagetitle: "Application of IAD Principles to the DAO structure"
metadescription: "This article will explore some examples of how IAD principles can be realized in the context of DAO and the open questions we have so far"
category: blog
featured-image: /images/blog/iad-ogp.png
intro: "This article will explore some examples of how IAD principles can be realized in the context of DAO and the open questions we have so far"
author: Savelyev
tags: ["DeFi Guides", "For Builders", "DAO governed"]
---

![](/images/blog/application-of-iad-principles-to-the-dao-structure/image1.png)

The Institutional Analysis and Development (IAD) framework, designed by Ostrom, an American political scientist, who was the first woman to receive the Nobel Memorial Prize in Economic Sciences in 2009, and her colleagues from the Ostrom Workshop in 2005, facilitated the analysis of institution processes through which individual and collective choices occur. Their main focus was on institutional distributed structures that share common goods and resources, and on how these commons can be managed in a sustainable way, balancing individuals' use with the interest of a wider public.

The Decentralized Autonomous Organization (DAO) is still in the process of finding its best organizational structure and a flexible framework that would work for multiple entities and with the ability to customize accordingly. This article will explore some examples of how IAD principles can be realized in the context of DAO and the open questions we have so far.

The IAD framework states that eight following principles form the basis for every decentralized community that shares resources:

- Defined Boundaries
- Appropriate Rules
- Rule Making process
- Monitoring
- Sanctions
- Conflict resolution
- Self-governance
- Polycentricity

### Defined Boundaries

The first principle states that an organization should have clear boundaries to determine what is a part of the community and what isn’t. It comprises shared resources management, participant identification, core values and principles, communication channels, and project brand.

Without defining community boundaries, the use of a community holding sbecomes a free-for-all, leading to overuse and potential collapse due to the free-rider problem.

**_In the context of DAO, it leads us to an important question: Who is a part of DAO, who can decide the vision, strategy, and product scope?_**

![](/images/blog/application-of-iad-principles-to-the-dao-structure/image2.png)

Types of DAO participants can be separated into 2 categories which may overlap:

- Governance right owners - persons who have rights to govern and make decisions in the scope of DAO. They may or may not participate in DAO operations (free-riders).
- Contributors - participants who are actively involved in DAO operations. They may have governance rights or may not.

We assume that the target audience that leads a DAO towards development is Active DAO members who have voting and decision-making rights and actively participate in DAO operations. The growth of DAO directly depends on the quality of active DAO members.

Since contractors don’t affect DAO directly, we can put them outside the DAO boundaries.

Regarding the free-riders problem, every DAO is not interested in participating in governance or contribution. Essential solutions are a reward for participation or punishment for non-participation:

- Inflation of reputation economics. In the case of maintaining the same voting power, users should participate in DAO activities. Otherwise, their share will be inflated.
- Incentivization mechanics that stimulate token holders to participate in governance and decision-making.

Holographic voting provides an excellent example of a third way to overcome free-riders inactivity, replacing the absolute majority with a relative one.

### Appropriate Rules

There is no single unified approach on how to manage decentralized communities. That’s why rules should be adopted to specific DAO requirements. These rules include how the community manages its resources, makes decisions, and governs itself.

Furthermore, the community should have confidence in those rules and their implementation.

**_In the context of DAO, it means a defined governance template, voting, and funding mechanics, built on a trusted platform._**

The rules of decentralized organizations are primarily enforced by code rather than a nominal legal system. The core element is smart contracts, set in stone on the blockchain network and accepted by community members. Governors are the smart contract frameworks adopted for decentralized organizations.

![](/images/blog/application-of-iad-principles-to-the-dao-structure/image3.png)

### Rule-making processes

People are more likely to follow the rules if they are involved in writing and modifying them. This involves including stakeholders in the decision-making process – as it is the best way to ensure a broad community buy-in.

**_In the context of DAO, it may imply incentivization mechanics for participation in voting/governance, and the ability to hear the voice of minority stakeholders_**

Generally, rule-making occurs through governance (off-chain/on-chain). Participants create proposals to make changes in community or governance protocol. Based on the voting Mechanism, they vote for or against them and create new rules and amend existing ones.

Another angle on the rule-making process is the action-policy approach proposed by PolicyKit and the Metagov community.

The two main abstractions within PolicyKit are actions and policies.

An action is a one-time event that can occur within a community and is typically first proposed by a community member. In contrast, a policy is a declaration that must always be true and that governs some user capability.

For instance, a policy for joining a community might be: “To join the community, a user must be approved by at least one existing member of the community.”

To avoid the problem of underrepresentation of minor stakeholders, several approaches are applied by DAOs:

- Ability to delegate votes to other representatives to combine voting power. The Compound Governor allows the BAU to do it as BAU pleases. This is called Liquid Democracy.
- Limiting the voting power of whales and core teams to equalize voting power between them and minor stakeholders.
  - Examples of this can be shown on Gearbox DAO. It uses the approach “Reverse Voting Escrow Model”.
  - Another example is ElasticDAO. Elastic DAOs operate under a fair governance system limiting large wallets' influence. Members vote with their governance tokens up to the maximum voting power.
  - Pyramidic stacking mechanism in finance vote community. It utilizes a pyramidic stacking mechanism to normalize vote power across a voting population, ensuring that large token holders do not have an exceptionally out-weighted voice in the system.

### Monitoring

Effective monitoring by monitors who are part of or accountable to the appropriators. Once rules have been established, communities need to check that people are following them – in a manner that is still accountable to those in the community. Contributors need good information to ensure they are making the best decisions for the organization's future.

**_In the context of DAO, it can be applied as an approach of Radical Transparency, where all participants can view the whole DAO processes._**

Once there is no single center of authority, and every DAO member is involved in the decision-making process, it is essential to maintain transparency. This should be consistent in data flow and key DAO metrics.

It is essential to maintain equal access to crucial information. One of the proposed ways is to implement Radical Transparency. More specifically, transparency should be at least inside DAO. External transparency is not so important in this case.

The core of monitoring comes from the corporate world. These are clear goals, KPIs, and reporting along with responsible contributors. Typical activities that should occur periodically includes:

- Townhall meetings, where everyone can address questions
- Strategy sessions and annual goals meeting
- Goals & KPIs meeting
- Global OKRs
- DAO & Working Groups OKRs
- Periodic results meetings

### Sanctions

There is a scale of graduated sanctions for resource appropriators who violate community rules.

**_In the context of DAO, a community may implement a reputation system that penalizes wrongdoings with a loss of social credibility. Others may go for metrics based on experience_**

The outright banning of people who break the rules creates resentment rather than strengthening a community. Instead, graduated systems of warnings, fines, and reputational consequences are less disruptive to an organization and keep the punishments for wrongdoings proportional to the level of the offense.

The most typical way of sanctions is a reputation-based model like SourceCred. It is already working and widely spread among DAOs. The same approach is used in DXDao, where two tokens are presented - non-transferrable REP with no market value and marketable DXD. Reputation directly affects the user's voting power, thus preventing him from wrongdoing and decreasing his weight in the governance process.

### Conflict resolution

A community can include hundreds and thousands of people. Without a single center of authority, an expensive governance approach usually is not convenient to resolve internal conflicts and disputes, which are inevitable. Regarding external conflicts, the situation gets even more complicated. Thus mechanisms of conflict resolution should be cheap and of easy access.

**_In the context of DAO, a low-level dispute could be resolved with a random court of 5 ‘jurors’ chosen from among the community who are incentivized to provide a judicial ruling, e.g., the Metagov approach. As for external conflicts, there are smart-contract protected Decentralized Courts (Aragon, Kleros)._**

It is essential to provide easy and cheap ways to resolve conflicts. In most DAOs, it is working in a common way via discussion or voting on proposals. It may not be the most efficient way.

Another approach may be used based on Metagov/PolicyKit. Randomly select several juries that decide on a particular question to resolve a conflict. Also, a similar approach provides Digital Juries initiative – built on existing theoretical models of jury decision-making. They outlined a 5-stage model characterizing the space of design considerations in a digital jury process.

The solutions to solve external non-smart contract-based disputes are Aragon Court and Kleros protocols. They allow solving conflicts by randomly selected jurors, who stake tokens to participate. Although they were presented a while ago, the adoption rate is still relatively low (Kleros cases ~1100).

### Self-governance

The rights of a community to devise and govern its own institutions are recognized by external authorities. Without any kind of legal recognition, a community risks falling apart either through the exploitation of its resources by outside groups or due to an inability to escalate problems to higher-level authorities when internal sanctions are insufficient to settle a particular conflict.

**_In the context of DAO, recognition by other DAO or traditional legal entities and individuals, and ability to interact with them, e.g., Opolis, Open Collective. Another case uses a trusted 3rd party as a court to resolve problems_**.

Self-governance in the case of DAO includes at least the following directions:

- Ability to interact with other DAOs (partners, investors, etc.)
- Ability to interact with traditional organizations.
- Ability to hire and provide an appropriate level of services to its members (Opolis, Open Collective).

The strength of blockchain and crypto-related projects is the interoperability and ability to interact with other projects, even on technological background.

The ability to interact with traditional organizations is a bit tricky. Some jurisdictions are recognizing DAOs, but this question is still in its early state. As a workaround, DAOs register conventional forms of business like LLC to have a way to interact with established companies.

To interact with contractors and contributors, there are some projects like Opolis, which acts as a proxy for DAOs and provide with the ability to have standard corporate benefits like Benefits, Payroll, and Shared Services for independent workers like solopreneurs, sole-practitioners, independent contractors, gig workers, digital nomads, freelancers and the like.

### Nestedness / Subsidiarity / Polycentricity

![](/images/blog/application-of-iad-principles-to-the-dao-structure/image4.png)

Appropriation, provision, monitoring, enforcement, conflict resolution, and governance activities are organized in multiple layers of nested enterprises. Decision-making power should flow to the people most connected to being governed.

**_In the context of DAO, multiple layers of government, working groups, sub-DAOs, working domains, and different levels/tiers of participation._**

Once becoming more mature, DAOs face the need to implement a more rigid structure with nested layers of decision-making expanding jurisdiction to appropriate levels. Decision-making power should flow to the people most connected to being governed. The process can occur top-to-bottom when the core team initiates the creation of a department or bottom-up when most engaged community members initiate the process. Departments may include internal structure, governance, leadership, and treasury, but they usually have a flat structure.

All of this reveals the multiple centers of authority for different domains within the DAO.

It is essential that rules applied may be general and domain-specific.

- General overarching rules are intended to counteract tendencies towards monocentric; they include laws that provide institutional mechanisms for separation of powers, monitoring, conflict resolution, appeal, system entry, and exit.
- Domain-specific rules are tailored to the needs of particular domains, such as private production or public service provision, and often supply the mechanisms needed for a specific domain to effectively self-organize.

### Conclusion

The provided principles for the DAO are poised to encourage a wholesome experience in governance and management of the framework for both active participants, investors, and stakeholders across the board. Entirely in effect, the DAO’s framework will be safe, secure, and inviting for all.
