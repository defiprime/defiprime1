---
git-date:
layout: [blog]
title: "Token Vesting - The most extensive guide"
permalink: token-vesting-guide
h1title: "Token Vesting: Everything You Need to Know"
pagetitle: "Token Vesting: Everything You Need to Know"
metadescription: "Learn everything about token vesting in this comprehensive guide. Understand different vesting schedules, their benefits, and how they ensure long-term commitment and stability in blockchain projects. Perfect for investors, developers, and crypto enthusiasts."
category: blog
featured-image: /images/blog/og.png
intro: "Learn everything about token vesting in this comprehensive guide. Understand different vesting schedules, their benefits, and how they ensure long-term commitment and stability in blockchain projects. Perfect for investors, developers, and crypto enthusiasts."
author: sawinyh
tags: ["For Builders", "DeFi Guides"]
---


In the rapidly evolving world of blockchain and cryptocurrencies, token vesting has emerged as a crucial mechanism for ensuring the long-term success and stability of projects. Whether you’re an investor, developer, or enthusiast, understanding token vesting is essential for navigating the crypto landscape effectively.

**What is Token Vesting?**

Token vesting refers to the process by which cryptocurrency tokens are released over a predetermined schedule rather than being made available all at once. This mechanism is commonly used in blockchain projects to align the interests of team members, investors, and other stakeholders with the project's long-term goals.

**Key Components of Token Vesting**


1.	**Vesting Schedule:** This is the timeline for gradually releasing tokens. It outlines specific dates or milestones when portions of the tokens become accessible to the recipients.
2.	**Cliff Period:** A cliff is an initial period when no tokens are vested. After the cliff period ends, a lump sum of tokens may vest, followed by regular vesting intervals.
3.	**Linear Vesting:** Tokens are released evenly over the vesting period. For example, if 100 tokens vest over 10 months, 10 tokens become available each month after the cliff.
4.	**Token Lockup:** While similar to vesting, a lockup typically refers to a period during which tokens cannot be sold or transferred, even if they are fully vested.

**Purpose of Token Vesting**
-	**Aligning Incentives:** By releasing tokens over time, team members and early contributors are encouraged to remain committed to the project’s development and success.
-	**Preventing Market Dumping:** Gradual release of tokens helps prevent large sell-offs that could negatively impact the token’s market value.

**Controlled Token Release**
-	**Minimizing Price Volatility:** Vesting ensures that tokens enter the market gradually, avoiding the impact of large, sudden token sales that could devalue the token. This controlled release supports a more stable price over time, which benefits both the project and its investors.
-	**Building Investor Confidence:** A vesting schedule reassures investors that the project has a structured plan for token release, reducing the likelihood of extreme price drops. This stability is attractive to investors and helps build confidence in the project’s longevity.

**Mitigating “Pump and Dump” Risks**
-	**Discouraging Short-Term Speculation:** A structured vesting schedule can reduce the chance of “pump and dump” schemes, where early investors might drive up the price and then cash out, leaving others to bear the losses. Vesting makes it difficult for large holders to cash out quickly, promoting responsible trading and supporting sustainable growth.
-	**Building Trust:** Transparent vesting schedules enhance investor confidence by demonstrating a commitment to the project’s longevity.

**Long-Term Commitment**
-	**Founders and Team Members:** A vesting schedule helps ensure that those responsible for driving the project’s vision stay involved over the long haul. Instead of receiving all tokens upfront, they gain access to their tokens incrementally, creating a steady incentive to keep building and enhancing the project.
-	**Early Contributors and Advisors:** For those who may have provided valuable early-stage support, vesting schedules ensure they continue to support the project and contribute over time rather than disengaging once they receive their tokens.

**Enhancing Transparency**
-	**Clear Communication:** Publishing a detailed vesting schedule makes the token allocation process transparent. When investors and community members understand how and when tokens will be released, they are more likely to trust the project’s intentions.
-	**Setting Expectations:** By laying out a transparent vesting schedule, the project team can set realistic expectations for token distribution and reassure the community of their long-term commitment.

**How Token Vesting Works**

In practice, token vesting is often implemented through smart contracts on a blockchain platform. These self-executing contracts automate the release of tokens according to the predefined vesting schedule, ensuring fairness and transparency.

**Example Scenario**

Imagine a blockchain startup allocates 1 million tokens to its founding team with a 4-year vesting schedule and a 1-year cliff:
-	**Year 1:** No tokens are vested during the first year (cliff period).
-	**After Year 1:** At the end of the first year, 25% of the tokens (250,000 tokens) vest immediately.
-	**Years 2-4:** The remaining tokens vest monthly or quarterly over the next three years.

The easiest way to check if a token has a vesting schedule is by reviewing the project’s official documents and communications:

* **Whitepaper or Tokenomics Document**: Most projects outline token allocation details, including vesting schedules, in their whitepapers or separate tokenomics documents.
* **Official Announcements**: Project announcements on social media, Medium articles, or blogs often provide updates on token vesting and distribution schedules.
* **Community Channels**: Join the project’s community on platforms like Telegram or Discord. Teams frequently address questions about vesting schedules there, and you can also ask team members directly.

### Understanding Different Types of Token Vesting Schedules


Token vesting schedules are essential tools for aligning the interests of project teams, investors, and community members with a project’s long-term success. They determine how and when token holders can access their tokens, using varying structures to fit different project needs. Here, we’ll explore some popular types of token vesting schedules and how each one functions, from traditional unlocks to more complex exponential vesting.

![](/images/blog/vesting-schedule.jpg)

### **Linear Stream**

A **Linear Stream** vesting schedule releases tokens at a constant, even rate over time. With this type of vesting, token holders receive small, incremental portions of their allocation each second, creating a smooth and continuous stream of tokens.
* **Best For**: Projects that want a gradual, predictable release of tokens.
* **Example**: A team member’s 100,000 tokens vest over a year, with an even distribution every second.

### **Cliff Stream**

The **Cliff Stream** is similar to the Linear Stream but includes a *cliff period*—an initial waiting period before any tokens are released. After the cliff period ends, tokens begin vesting at a constant rate, similar to a Linear Stream.

* **Best For**: Teams wanting to ensure commitment before tokens start unlocking.
* **Example**: A team member’s tokens are locked for six months (the cliff period), after which tokens start vesting evenly every second over the remaining period.

### **Unlock In Steps**

The **Unlock In Steps** vesting schedule distributes tokens in fixed intervals or “steps” rather than continuously. At each interval, a set amount of tokens is unlocked, creating a more traditional vesting style that releases tokens in defined increments.

* **Best For**: Projects that prefer milestone-based vesting or require flexibility in token distribution.
* **Example**: A vesting schedule where 25% of tokens unlock every three months.

### **Monthly Unlocks**

A **Monthly Unlock** vesting schedule releases tokens once per month at a set amount. This schedule is similar to the “Unlock in Steps” method but specifically uses monthly intervals, making it predictable and easy to follow.

* **Best For**: Teams that want to align token releases with monthly reporting or progress evaluations.
* **Example**: 10,000 tokens unlock at the end of each month over a ten-month period.

### **Timelock**

**Timelock** vesting involves locking all tokens until a specific date, at which point they become available all at once. This method is used to secure tokens and prevent any access until a predetermined period ends.

* **Best For**: Projects aiming to prevent early token access, such as before a public launch or major milestone.
* **Example**: All tokens are locked for a year and released in full at the end of the lock-up period.

### **Backweighted**

A **Backweighted** vesting schedule releases tokens at an increasing rate over time. Token holders receive fewer tokens in the initial stages, with larger portions unlocking toward the end of the vesting period. This method can keep teams incentivized for longer-term contributions.

* **Best For**: Projects that want to reward long-term commitment, with larger rewards as more time passes.
* **Example**: In a four-year vesting period, smaller amounts are released initially, with the majority unlocking in the final year.

### **Unlock Linear**

In an **Unlock Linear** schedule, a portion of tokens is unlocked instantly, followed by a Linear Stream for the remaining tokens. This method allows token holders some immediate access while spreading the remaining tokens over time.

* **Best For**: Projects wanting to provide an initial token incentive while maintaining a steady, predictable release.
* **Example**: 20% of tokens unlock immediately, with the remaining 80% distributed evenly over the next two years.

### **Unlock Cliff**

With an **Unlock Cliff** schedule, a portion of tokens unlocks instantly, and the remainder follows a Cliff Stream. This approach combines an initial reward with a delayed stream, ensuring long-term involvement.

* **Best For**: Teams needing immediate partial access but aiming to incentivize longer-term commitment.
* **Example**: 10% of tokens unlock at once, with the rest locked for six months (cliff) and then gradually released.

### **Exponential**

An **Exponential** vesting schedule releases tokens on an exponential curve, meaning the vesting rate increases over time. This method provides minimal token access at the start, with a growing amount released as the schedule progresses.

* **Best For**: Projects looking to reward patient, long-term holders with increasing access over time.
* **Example**: Tokens are released slowly in the first half of the vesting period and accelerate significantly in the latter half.

### **Cliff Exponential**

The **Cliff Exponential** schedule combines a cliff period with an exponential release. No tokens are accessible during the cliff, after which tokens vest at an increasingly fast rate.
* **Best For**: Projects that want to delay initial access and reward patience with a faster release as time progresses.
* **Example**: Tokens are locked for six months (cliff), then released slowly at first, increasing in rate over the remaining vesting period.

### **Summary Table of Vesting Schedules**

<table>
  <tr>
   <td><strong>Vesting Schedule</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Best For</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Linear Stream</strong>
   </td>
   <td>Constant, continuous token release
   </td>
   <td>Gradual, predictable releases
   </td>
  </tr>
  <tr>
   <td><strong>Cliff Stream</strong>
   </td>
   <td>Linear release after an initial cliff period
   </td>
   <td>Ensuring long-term commitment before unlock
   </td>
  </tr>
  <tr>
   <td><strong>Unlock In Steps</strong>
   </td>
   <td>Tokens unlock in set intervals or milestones
   </td>
   <td>Milestone-based vesting
   </td>
  </tr>
  <tr>
   <td><strong>Monthly Unlocks</strong>
   </td>
   <td>Tokens unlock at monthly intervals
   </td>
   <td>Predictable monthly releases
   </td>
  </tr>
  <tr>
   <td><strong>Timelock</strong>
   </td>
   <td>All tokens locked until a specified date
   </td>
   <td>Projects requiring full lock-up before access
   </td>
  </tr>
  <tr>
   <td><strong>Backweighted</strong>
   </td>
   <td>Larger token unlocks towards the end of vesting
   </td>
   <td>Rewarding long-term commitment
   </td>
  </tr>
  <tr>
   <td><strong>Unlock Linear</strong>
   </td>
   <td>Partial unlock upfront, followed by a Linear Stream
   </td>
   <td>Immediate incentive with predictable stream
   </td>
  </tr>
  <tr>
   <td><strong>Unlock Cliff</strong>
   </td>
   <td>Partial unlock upfront, followed by a Cliff Stream
   </td>
   <td>Initial access, with long-term commitment incentive
   </td>
  </tr>
  <tr>
   <td><strong>Exponential</strong>
   </td>
   <td>Release accelerates over time
   </td>
   <td>Rewarding patient, long-term holders
   </td>
  </tr>
  <tr>
   <td><strong>Cliff Exponential</strong>
   </td>
   <td>Cliff period followed by an accelerating exponential release
   </td>
   <td>Delayed access with increasing rate over time
   </td>
  </tr>
</table>


### Token vesting vs. Token Lock-ups

The concepts of **vesting tokens** and **token lock-ups** are commonly used in cryptocurrency and blockchain projects to manage token distribution and ensure token value stability. While they may seem similar, they serve different purposes and function in distinct ways. Here's a breakdown of the differences:

A **token lock-up** is when certain tokens cannot be transferred or sold. Lock-ups are typically enforced at the beginning of a project to prevent large token holders from immediately selling off their tokens, which could crash the token's price.

* **Purpose**: Lock-ups are designed to prevent early investors, team members, or large holders from quickly liquidating their tokens, which could create significant selling pressure and negatively impact the token's market value.
* **Mechanism**: During the lock-up period, the tokens are completely restricted from being moved or sold. Once the lock-up period ends, the tokens become fully accessible to the holder, often all at once.
* **Example**: A project might lock up tokens held by the team and advisors for one year after the token launch, ensuring that they cannot sell any of their tokens during this period. Once the lock-up expires, they can use, sell, or transfer their tokens without restrictions.

### **Key Differences Between Vesting and Lock-Up**

<table>
  <tr>
   <td><strong>Aspect</strong>
   </td>
   <td><strong>Vesting Tokens</strong>
   </td>
   <td><strong>Token Lock-Up</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Token Access</strong>
   </td>
   <td>Gradual access over time (e.g., monthly or quarterly)
   </td>
   <td>No access until the lock-up period ends
   </td>
  </tr>
  <tr>
   <td><strong>Purpose</strong>
   </td>
   <td>Long-term commitment, aligning incentives with project
   </td>
   <td>Price stability by preventing early, large sell-offs
   </td>
  </tr>
  <tr>
   <td><strong>Flexibility</strong>
   </td>
   <td>Tokens become accessible in stages, per vesting schedule
   </td>
   <td>All tokens remain inaccessible until lock-up ends
   </td>
  </tr>
  <tr>
   <td><strong>Common Use Cases</strong>
   </td>
   <td>Team members, advisors, early contributors
   </td>
   <td>Early investors, team, pre-launch participants
   </td>
  </tr>
  <tr>
   <td><strong>Impact on Market</strong>
   </td>
   <td>Helps distribute selling pressure over time
   </td>
   <td>Prevents large, immediate selling pressure
   </td>
  </tr>
</table>


### Liquidity Locks  

**Liquidity locks** are a mechanism used by blockchain projects to secure and stabilize the liquidity of their tokens, especially in decentralized finance (DeFi) contexts. By "locking" liquidity, a project ensures that a certain amount of its tokens and funds remain in a liquidity pool for a set period, making it less likely for the token price to experience extreme volatility. This mechanism has become particularly important for building investor trust and preventing "rug pulls" (where developers remove liquidity from a pool, leaving investors unable to sell their tokens).

Here’s how liquidity locks work and why they matter:

### **What is a Liquidity Lock?**

A liquidity lock is a **commitment made by a project to keep its tokens paired with another asset (such as ETH or USDT) in a liquidity pool** on a decentralized exchange (DEX) like Uniswap, SushiSwap, or PancakeSwap for a defined period. The tokens in the liquidity pool are effectively locked, meaning they cannot be removed, transferred, or sold until the lock period ends.

This locked liquidity provides stability, as it ensures that there is enough token and asset supply in the pool to allow for trading without significant slippage or price impact.

### **How Liquidity Locks Work**

**Creation of Liquidity Pool**

- The project team creates a liquidity pool on a DEX by pairing their native token with a widely used asset like ETH, USDT, or BNB. They deposit both assets into the pool, providing liquidity that allows users to trade in and out of the token pair.

**Locking the Liquidity**

- Once the pool is created, the team locks the liquidity by sending the liquidity provider (LP) tokens to a **locking service** or **timelock smart contract**. These LP tokens represent ownership of the pool’s liquidity.
- Popular services that manage liquidity locks include [Unicrypt](https://uncx.network/), **TrustSwap**, and **DXSale**. These platforms allow the project to define a lock period and secure the LP tokens, preventing any access until the lock period expires.

**Locked Period**
- During the locked period, the team cannot withdraw or tamper with the locked funds. They are completely inaccessible until the set time elapses, offering peace of mind to investors.
- Typically, lock periods range from several months to years, depending on the project’s goals and timeline.

**Release of Liquidity**
- After the lock period ends, the LP tokens are released to the team. The team can then decide to either re-lock the liquidity, withdraw some funds, or use the tokens as they see fit.

### **Why Liquidity Locks Matter**

- **Investor Confidence**

A locked liquidity pool shows that the team is committed to the project and isn’t planning an exit scam. By locking liquidity, the project builds trust with investors, who can trade tokens confidently without fearing a "rug pull."

- **Price Stability**

Locked liquidity helps reduce volatility by ensuring that there is a stable pool of tokens available for trading. With ample liquidity, large trades have less price impact, making the token’s price more stable.

- **Prevention of Rug Pulls**

Without liquidity locks, developers could potentially remove liquidity, leaving little or no funds in the pool for investors to sell their tokens. Locking liquidity ensures that the liquidity remains available to support token trades during the locked period.

- **Marketing and Community Building**

Many projects use liquidity locks as a selling point, advertising their locked liquidity as a security feature to attract more investors. Transparency around locked liquidity can enhance community support and attract longer-term investors.


### **Key Considerations for Liquidity Locks**

- **Choosing the Lock Period**

A longer lock period is often seen as a stronger commitment to the project’s longevity. However, excessively long lock-ups may also limit the project’s flexibility, as the team won’t be able to access funds in case of unforeseen needs.

- **Third-Party Locking Services**

Using a reputable third-party service like Unicrypt or TrustSwap can add an extra layer of trust. These services are well-known and transparent about lock status, making it easy for investors to verify the lock.

- **Transparency and Communication**

Projects should communicate their lock-up details clearly and make the information easily accessible to investors. Projects often provide a public link to the locking service’s page, showing the lock duration, amount, and release date.

### **Example Scenario**

Imagine a new DeFi project creates a token and wants to build trust with its community. The team deposits $500,000 worth of their tokens and $500,000 worth of ETH into a Uniswap liquidity pool, creating a stable trading pair. They then send the LP tokens representing this liquidity to Unicrypt, locking it for one year. For the next 12 months, these tokens cannot be withdrawn or altered by anyone, including the project team. This setup gives investors confidence that the liquidity will remain stable, and the project team won’t remove it unexpectedly.


## On-Chain vs. Off-Chain Token Vesting: Understanding the Differences

There are two main methods for implementing token vesting: **on-chain vesting** and **off-chain vesting**. While both serve the same fundamental purpose of gradually releasing tokens to recipients over time, they differ significantly in their mechanisms, security, transparency, and flexibility. In this article, we’ll explore the differences between on-chain vesting and off-chain vesting (often conducted through custodial services) to help you understand which approach may be the best fit for a given project.

### **What is On-Chain Vesting?**

On-chain vesting involves the use of **smart contracts on a blockchain** to manage and automate the release of tokens according to a predefined schedule. Once deployed, the vesting smart contract is autonomous and operates transparently on the blockchain, eliminating the need for intermediaries.

#### **How On-Chain Vesting Works**

* **Smart Contract Setup:** The vesting schedule is embedded within a smart contract, specifying details like the total number of tokens, the vesting timeline, the cliff period (if any), and intervals for token release.
* **Automation and Execution:** Once the contract is live on the blockchain, it automatically releases tokens according to the specified schedule without requiring manual intervention.
* **Transparency and Immutability:** All transactions and vesting details are visible on the blockchain, making the process transparent to stakeholders. The terms of the vesting schedule are immutable, providing an extra layer of security and preventing unauthorized changes.


#### Popular onchain vesting service providers

**Sablier**

![](/images/blog/sablier1.jpg)

[Sablier](https://sablier.com/vesting/) is a pioneering token streaming protocol that enables real-time, continuous payments on the Ethereum blockchain and other EVM-compatible networks. Established in 2019, Sablier offers a user-friendly platform for creating and managing token vesting schedules, payroll, and airdrops.

-	**Key Features:**
  - **Security:** operating continuously for over five years with zero exploits.
  - **Real-Time Streaming:** Tokens are streamed to recipients every second, providing immediate access to vested amounts.
  - **Customizable Vesting Schedules:** Supports various vesting curves, including linear, exponential, and custom configurations.
  - **Cliff Periods:** Allows the inclusion of cliff periods before vesting commences.
  - **NFT Representation:** Each stream is represented as an NFT, offering flexibility in transferability and integration with other protocols.
  - **Available on most popular EVM L1/L2 chains:** Ethereum, Optimism, Arbitrum, Linea, Scroll, etc.

- **Use Cases:**
  - **Token Vesting:** Automates the distribution of tokens to team members, investors, and advisors over time.
  - **Airdrops:** Enables time-based token distributions to community members.
  - **Payroll:** Facilitates continuous salary payments in tokens.

Sablier’s open-source nature and extensive documentation make it accessible for developers and organizations seeking to implement on-chain token distribution solutions.  

**Superfluid**

![](/images/blog/superfluid1.jpg)

[Superfluid](https://superfluid.finance) is a protocol designed for real-time finance, allowing continuous money streams and on-chain subscriptions. It introduces the concept of “money streaming,” enabling tokens to flow between addresses every second without the need for recurring transactions.

-	**Key Features:**
  - **Continuous Streaming:** Facilitates per-second token transfers, ensuring recipients have immediate access to funds.
  - **Composability:** Streams can interact with other DeFi protocols, enabling use cases like automated yield farming.
  - **Full Liquidity:** Tokens remain in the sender’s wallet until streamed, allowing for liquidity management.
  - **Simple User Interface:** Offers a user-friendly dashboard for setting up and managing vesting schedules.

- **Use Cases:**
  - **Token Vesting:** Provides liquid and composable vesting solutions for projects.
  - **Salaries and Subscriptions:** Enables real-time salary payments and subscription models.
  - **DeFi Integrations:** Allows streaming tokens directly into DeFi protocols for staking or liquidity provision.

Superfluid’s innovative approach to continuous token flows offers flexibility and efficiency for various financial applications within the blockchain ecosystem.

**Streamflow**

![](/images/blog/streamflow1.jpg)

[Streamflow](https://streamflow.finance/) is a token distribution platform that focuses on simplifying the creation and management of vesting contracts and token streams. It aims to provide secure and efficient solutions for token vesting, payroll, and continuous payments.

- **Key Features:**
  - **User-Friendly Interface:** Offers an intuitive platform for setting up and monitoring vesting schedules.
  - **Security:** Emphasizes secure smart contract deployment and management.
  - **Flexibility:** Supports various token distribution models, including linear and milestone-based vesting.
  - **Analytics:** Provides insights and analytics on token distribution and vesting progress.
  - **Non-EVM chains supported:** Solana, Aptos, Sui

- **Use Cases:**
  - **Token Vesting:** Automates the release of tokens to stakeholders over time.
  - **Payroll:** Enables continuous payment streams for employees and contractors.
  - **Airdrops:** Facilitates time-based token distributions to community members.

Streamflow’s focus on security and ease of use makes it a viable option for projects seeking to implement on-chain token distribution mechanisms.

#### On-chain vesting: Service provider vs. In-house solution


### **Option 1: Using Smart Contract Vesting Provider**

Ready-to-go smart contract vesting providers—like Sablier, Superfluid, and Streamflow—offer pre-built platforms that manage token vesting with ease. These solutions are highly attractive for projects that need efficient, secure, and hassle-free vesting options.


#### **Pros of Using a Ready-to-Go Vesting Provider**

- **Speed and Convenience**
  * Pre-built solutions allow projects to set up vesting contracts quickly, often in a matter of minutes.
  * Project teams can avoid the complexities of smart contract development, letting them focus on other core aspects of the project.

- **Reduced Security Risks**
  * Leading vesting providers have been extensively tested and audited, minimizing vulnerabilities. Security audits are critical in blockchain, as bugs or exploits can lead to massive financial losses.
  * By using an audited provider, projects can trust that the vesting contract has passed rigorous security reviews, reducing the risk of loss due to exploits.
- **No Frontend Development Overhead**
  * Ready-made platforms often include a user-friendly frontend, saving teams from the time and costs associated with designing and developing an interface from scratch.
  * The platform’s frontend is also typically optimized for a seamless user experience, making it easy for recipients to view their token balance and vesting status.
- **Lower Upfront Costs**
  * Using a provider eliminates the need for hiring specialized smart contract developers and paying for security audits, which can be extremely costly.
  * Ready-made solutions usually have clear, predictable costs in the form of subscription fees or small transaction fees, making budgeting easier.
- **Support and Maintenance**
  * Providers typically offer ongoing maintenance, technical support, and upgrades, ensuring that the vesting contract remains secure and operational.
  * Any updates required for new blockchain standards or compatibility with other platforms are managed by the provider.

#### **Cons of Using a Ready-to-Go Vesting Provider**
- **Limited Customization**
  * Pre-built solutions may lack specific features or customization options that some projects require.
  * If the project needs highly customized vesting schedules or unique release mechanisms, a ready-to-go solution may be too rigid.
- **Dependency on Third-Party Providers**
  * Relying on an external provider means that the project’s vesting solution is tied to that provider’s availability and stability.
  * Any issues with the provider’s service, such as outages or business changes, could disrupt the project’s vesting operations.
- **Transaction Fees and Subscription Costs**
  * Some providers charge ongoing fees based on transaction volume or a flat subscription rate, which could add up over time, especially for large or highly active projects.

### **Option 2: Building a Custom Vesting Smart Contract In-House**

Creating a custom vesting smart contract offers complete control over the vesting mechanism, allowing teams to tailor it exactly to their needs. However, this approach also comes with significant time and resource demands.

#### **Pros of Building a Custom Vesting Solution**

- **Full Customization and Control**
  * Custom solutions can be designed to meet any specific requirements, including unique vesting schedules, complex conditions, and tailored functionalities.
  * Projects have full control over how tokens are distributed, which is especially valuable for unique projects or those with complex tokenomics.

- **No Ongoing Platform Dependency**
  * By developing an in-house solution, projects eliminate reliance on third-party providers, which can be beneficial for maintaining full ownership and flexibility.
  * An internal solution also allows the project to adapt or update the vesting contract without depending on external schedules or policies.

- **Potential for Future Flexibility**
  * Custom contracts can be designed to adapt to future project changes, giving teams the flexibility to add new features or modify the vesting schedule if needed.

#### **Cons of Building a Custom Vesting Solution**

- **High Cost of Smart Contract Security Audits**
  * Developing a custom smart contract means it must be rigorously audited by security experts to avoid costly vulnerabilities or exploits.
  * Smart contract audits are expensive, often costing tens of thousands of dollars depending on the complexity of the code. Audits may also need to be repeated if updates are made, leading to additional costs.

- **Frontend Development Overhead**
  * Custom solutions require a frontend for user interactions, adding development time and costs. The team will need frontend developers to build a dashboard or interface where users can check their vesting status.
  * Building an intuitive and secure interface is crucial, as users must have a straightforward way to monitor and manage their vesting tokens.

- **Engineering Time and Resource Demands**
  * Creating a smart contract from scratch is time-consuming and requires skilled blockchain developers, which are in high demand and can be costly to hire.
  * The project’s engineering team will need to spend valuable time developing, testing, and refining the custom vesting contract, taking focus away from other essential tasks, like building the project’s core functionalities.

- **Ongoing Maintenance and Updates**
  * A custom smart contract requires regular maintenance to address potential issues, security vulnerabilities, and compatibility updates.
  * Any bugs or required changes after deployment would fall on the project’s developers, requiring ongoing attention and resources for troubleshooting and improvements.

- **Increased Launch Timeline**
  * Building an in-house solution extends the time it takes to get the vesting solution ready. This delay can impact project timelines and reduce time-to-market, especially in fast-paced blockchain environments.

### **Comparing the Two Approaches**

<table>
  <tr>
   <td><strong>Aspect</strong>
   </td>
   <td><strong>Ready-to-Go Provider</strong>
   </td>
   <td><strong>Custom Solution</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Setup Time</strong>
   </td>
   <td>Fast, typically a few minutes to set up
   </td>
   <td>Extended development and audit time
   </td>
  </tr>
  <tr>
   <td><strong>Security</strong>
   </td>
   <td>Provider-audited contracts
   </td>
   <td>Requires costly security audits
   </td>
  </tr>
  <tr>
   <td><strong>Frontend Development</strong>
   </td>
   <td>Built-in, user-friendly interfaces
   </td>
   <td>Requires separate frontend development
   </td>
  </tr>
  <tr>
   <td><strong>Customization</strong>
   </td>
   <td>Limited
   </td>
   <td>Fully customizable
   </td>
  </tr>
  <tr>
   <td><strong>Upfront Costs</strong>
   </td>
   <td>Lower, predictable fees
   </td>
   <td>High, especially for audits
   </td>
  </tr>
  <tr>
   <td><strong>Maintenance & Support</strong>
   </td>
   <td>Provided by the vendor
   </td>
   <td>In-house team required
   </td>
  </tr>
  <tr>
   <td><strong>Dependency on Provider</strong>
   </td>
   <td>Yes
   </td>
   <td>No
   </td>
  </tr>
  <tr>
   <td><strong>Transaction Fees</strong>
   </td>
   <td>Typically charged by providers
   </td>
   <td>Minimal, but may incur gas fees
   </td>
  </tr>
</table>

### **Choosing the Right Option for Your Project**

The choice between a ready-to-go vesting provider and a custom-built smart contract depends on the project’s specific needs, timeline, and budget:

* **For Fast Setup and Lower Costs**: Ready-to-go providers are ideal for projects that need a quick, secure solution without heavy upfront investments. These are great for teams focused on delivering their main project features without diverting resources to custom development.
* **For Unique Vesting Needs and Full Control**: A custom-built smart contract is best suited for projects that require unique vesting schedules or functionalities unavailable in pre-built solutions. Projects with the resources and expertise to handle development, security, and ongoing maintenance might find a custom solution advantageous despite the higher costs.

### **What is Off-Chain Vesting?**

Off-chain vesting, on the other hand, typically involves **custodial services**—such as Anchorage, BitGo, or Coinbase Custody—that manage and hold tokens on behalf of the project. In this setup, the custodian manages the vesting schedule and releases tokens according to pre-agreed terms, but the vesting mechanics are not automated on the blockchain itself.


#### **How Off-Chain Vesting Works**

* **Custodial Agreements:** The project team or organization enters into an agreement with a trusted third-party custodian to manage the vesting. The custodian holds the tokens in a secure environment and manages their release based on the vesting schedule.
* **Manual Intervention:** The custodian manually or semi-manually initiates the token release based on the vesting terms, typically after verifying milestones, conditions, or other relevant criteria.
* **Off-Chain Management:** Since the vesting isn’t automated on the blockchain, the process relies on the custodian’s internal systems, security protocols, and reporting.


#### Popular Custodial Services

**Anchorage Digital**

Founded in 2017, Anchorage Digital is a comprehensive digital asset platform that provides a suite of services, including custody, staking, trading, and governance. Notably, it operates Anchorage Digital Bank, the first federally chartered cryptocurrency bank in the United States, approved by the Office of the Comptroller of the Currency (OCC) in 2021.
-	**Key Features:**
	-	**Regulatory Compliance:** As a federally chartered bank, Anchorage adheres to stringent regulatory standards, offering clients confidence in its operations.
	-	**Comprehensive Services:** Beyond custody, Anchorage provides staking, trading, and financing services, catering to a wide range of institutional needs.
  -	**Security Measures:** Utilizes biometric authentication and hardware security modules to safeguard digital assets.

**BitGo**

Established in 2013, BitGo is a digital asset trust company known for its multi-signature wallet services and institutional-grade security solutions. It offers custody, trading, and settlement services to institutional clients.
-	**Key Features:**
	-	**Multi-Signature Security:** Implements multi-signature technology, requiring multiple approvals for transactions, enhancing security.
	-	**Insurance Coverage:** Provides insurance policies to protect digital assets under custody.
	-	**Regulatory Compliance:** Operates as a qualified custodian, meeting regulatory requirements for institutional investors.

**Coinbase Custody**

Launched in 2018, Coinbase Custody is a division of Coinbase Global, Inc., offering secure and compliant custody solutions for institutional investors. It provides services such as staking, governance, and secure storage of digital assets.
-	**Key Features:**
	-	**Regulatory Compliance:** Operates as a New York State-chartered trust company, ensuring adherence to regulatory standards.
	-	**Comprehensive Insurance:** Offers insurance coverage for assets held in custody.
	-	**Integration with Coinbase Services:** Provides seamless integration with Coinbase’s trading and staking services.


### **Key Differences Between On-Chain and Off-Chain Vesting**

Here’s a closer look at how on-chain and off-chain vesting compare in terms of automation, security, transparency, flexibility, and more.

#### **1. Automation**

* **On-Chain Vesting:** Vesting schedules are fully automated through smart contracts. Once deployed, the smart contract executes token releases autonomously, according to the predefined schedule.
* **Off-Chain Vesting:** Off-chain vesting relies on manual or semi-automated intervention by the custodian. Token releases are initiated by the custodian based on the agreed schedule, but this process requires human oversight and approval.

#### **2. Security and Control**

* **On-Chain Vesting:** Security is enforced by the blockchain network and the smart contract itself. Since smart contracts are immutable once deployed, they are resistant to tampering or alteration. However, the security of on-chain vesting depends heavily on the quality and auditing of the smart contract code.
* **Off-Chain Vesting:** Security in off-chain vesting relies on the custodian’s infrastructure and security protocols. Leading custodians such as Anchorage, BitGo, and Coinbase Custody employ advanced security measures, including multi-signature wallets and insurance protections, to safeguard assets. However, trust is placed in the custodian to handle tokens responsibly.


#### **3. Transparency and Auditability**

* **On-Chain Vesting:** All vesting transactions are recorded on the blockchain and are publicly accessible, providing a high degree of transparency and auditability. Stakeholders can independently verify the vesting process by reviewing blockchain transactions.
* **Off-Chain Vesting:** Off-chain vesting lacks on-chain transparency since token release events are managed off the blockchain. Project teams and investors rely on the custodian’s reporting and documentation for updates on vesting status, which is typically provided through periodic reports or statements.

#### **4. Flexibility and Customization**

* **On-Chain Vesting:** Once a smart contract is deployed, it is typically immutable and difficult to alter. Any changes to the vesting schedule or terms would require a new smart contract. This lack of flexibility can be beneficial for security but may pose challenges if updates are needed.
* **Off-Chain Vesting:** Custodial vesting offers more flexibility. Terms can be adjusted by updating the custodial agreement, allowing for changes in the vesting schedule, milestones, or other parameters if needed. This adaptability can be helpful for projects requiring more control over token distribution.

#### **5. Regulatory Compliance and Legal Oversight**

* **On-Chain Vesting:** On-chain vesting is decentralized and lacks centralized oversight, which may complicate regulatory compliance in certain jurisdictions. Projects need to ensure compliance with securities and tax laws independently when using on-chain mechanisms.
* **Off-Chain Vesting:** Off-chain vesting through custodians often aligns better with regulatory standards. Many custodians operate in compliance with regulations in major jurisdictions, providing additional legal safeguards and reporting options that may be appealing to institutional investors.

#### **6. Cost and Complexity**

* **On-Chain Vesting:** Deploying and maintaining a smart contract for on-chain vesting can be costly, especially on high-demand blockchains where transaction fees are high. Additionally, smart contracts require skilled development and rigorous security audits to ensure they function correctly.
* **Off-Chain Vesting:** Custodial fees for off-chain vesting are typically less variable than on-chain gas fees, and custodians offer services to manage compliance, insurance, and reporting. However, projects must factor in custodial fees, which can vary based on the custodian and the assets under management.

### **Advantages and Disadvantages of Each Approach**

#### **On-Chain Vesting Pros and Cons**
* **Pros:**
    * High transparency and auditability.
    * Autonomous and tamper-proof once deployed.
    * Directly integrated with the blockchain ecosystem, fostering trust and reducing reliance on third parties.
* **Cons:**
    * Lack of flexibility; difficult to modify once deployed.
    * High development and auditing costs.
    * Potential challenges with regulatory compliance.


#### **Off-Chain Vesting Pros and Cons**

* **Pros:**
    * Greater flexibility in terms of adjusting vesting schedules.
    * Enhanced regulatory compliance and legal oversight.
    * Professional custodians offer insurance and reporting, increasing security and trust.
* **Cons:**
    * Less transparency, as vesting events are not directly visible on-chain.
    * Dependence on the custodian’s security and processes.
    * Potentially higher fees associated with custodial services.

### **Which Vesting Method is Right for Your Project?**

The choice between on-chain and off-chain vesting depends on the project’s needs, regulatory considerations, and the level of control desired.

* **On-Chain Vesting** is ideal for projects that prioritize transparency, trustless automation, and decentralization. It’s particularly well-suited for community-focused projects where stakeholders demand on-chain verification and autonomy.
* **Off-Chain Vesting** is suitable for projects needing more flexibility, regulatory compliance, or legal safeguards, particularly for projects aiming to attract institutional investors. Custodial services also provide insurance, regulatory reporting, and a trusted solution for handling large token holdings securely.

## Conclusion

Token vesting is a fundamental strategy in the blockchain space that aligns the interests of all parties involved—from founders and team members to investors and community supporters. By implementing thoughtful vesting schedules, projects can build trust, foster long-term commitment, and promote token stability, all of which are crucial for achieving sustainable growth.

As we’ve explored, there are various vesting structures available, each tailored to meet different project needs and goals. Whether it’s the steady flow of a linear vesting schedule, the delayed incentive of a cliff, or the gradually increasing release in an exponential schedule, the right vesting strategy can greatly impact a project’s success.

For projects looking to maximize impact, selecting the right vesting model is more than just a technical choice; it’s a reflection of their commitment to transparency, stability, and sustainable growth. With a well-designed vesting schedule, blockchain projects can not only strengthen their token’s value but also earn the confidence and support of their community, setting a solid foundation for the journey ahead.
