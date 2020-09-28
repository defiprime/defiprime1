---
git-date:
layout: [blog, blog-amp]
title:  DAO Accounting
permalink: dao-accounting
h1title: DAO Accounting. DeFi Accounting Series
pagetitle: DAO Accounting - DeFi Accounting Series
metadescription: DAO Accounting - DeFi Accounting Series. We’ll analyze various DeFi products from a US GAAP accounting perspective and end with a rumination on what they mean for the Ethereum economy as a whole.
category: blog
featured-image: /images/blog/dao-og.png
quote: /images/blog/dao-quote.png
intro: 'We’ll analyze various DeFi products from a US GAAP accounting perspective and end with a rumination on what they mean for the Ethereum economy as a whole.'
author: knab
tags: ['DeFi Guides', 'DeFi Accounting']
---
<div style="text-align: right">
<p>DeFi Accounting Series:
<br>
<a href="/dao-accounting">Part 1: Decentralized Autonomous Organization Accounting</a>
<br>
<a href="/defi-accounting">Part 2: Crypto Lending & Borrowing Platforms</a></p>
</div>
The prominence of decentralized finance products has ushered in a wave of capital and new users to the Ethereum ecosystem.

These experiments have also been great learning opportunities to think about finance and an economy at a more fundamental level. While there has been much discussion about the mechanics of particular products and projections of their outcomes, I thought it would be worthwhile to discuss what should happen once these transactions have actually taken place.

In this series, we’ll analyze various DeFi products from a US GAAP accounting perspective and end with a rumination on what they mean for the Ethereum economy as a whole.

## Decentralized Autonomous Organization Accounting

This article will go over:

*   What’s a DAO?
*   Historical context
*   Overview of current DAO environment
*   Accounting treatments

### What’s a DAO?

The best definition of a DAO that I have found comes from the [Amentum blog](https://medium.com/blockchannel/the-year-of-the-dao-comeback-1de1b1a36113):

“An organization that runs autonomously, in a decentralized manner, that functions without the need for centralized parties to make decisions for the organization to grow, to be profitable, or *physically* exist to serve its overall purpose. A DAO can be an on-chain contract or a series of on-chain contracts that interoperate to complete some greater organizational function.”

Some define DAOs more broadly. For example, some would argue that Bitcoin itself is a DAO. To learn more about this perspective, check out [this article](https://hackernoon.com/the-state-of-the-daos-b7cba318460b). For the purposes of this piece, we will adhere to the Amentum definition.


### History: “The DAO”

“The DAO” was a project in 2016 that resulted in the hard fork of Ethereum from which ETC and ETH were born. This project started up during an exciting time in the Ethereum community - prices were rising as was Ethereum’s notoriety. The concept was to create a kind of decentralized venture capital fund. Members would contribute ETH, then vote on projects they thought were worthy of funding. Tons of money poured into “The DAO.” This project was ultimately unsuccessful but did lay the intellectual and coding framework for the DAO environment that exists today. For more detailed background on The DAO, check out [this article](https://medium.com/swlh/the-story-of-the-dao-its-history-and-consequences-71e6a8a551ee).

Immediately after the dissolution of The DAO, general DAO activity died down. The Securities and Exchange Commission released a [statement](https://www.sec.gov/news/press-release/2017-131) indicating that the project would have been subject to securities regulations. In the years since the DAO hack, U.S. regulatory guidelines have become a bit clearer, and smart contract code repositories have gone through more vetting and hardening. It has laid the groundwork for the resurgence of DAOs.


### DAO Landscape

Some have dubbed 2019 the year of the DAO. There have been a proliferation of DAO projects that have come about, maybe the most notable being the MolochDAO, which was launched at ETHDenver in February. DAOs have a variety of different purposes and structures. Here’s an overview of some of the most popular DAO projects around currently:

![](/images/blog/dao-image2.png)
Figures estimated as of August 5, 2019

### Accounting Implications

At the danger of sounding like a broken record, there are currently no specific guidelines for how contributions to and receipts from a DAO should be treated from an accounting perspective. All we can do is take the rules we know and attempt to apply them as best we can. I’ve created from arbitrary categorizations of DAOs that we’ll analyze from a bookkeeping and tax viewpoints. We’ll also look at each DAO from the perspective of what I’ve termed the “Pledger,” or the people/businesses sending assets to the DAO, and from the perspective of the “Receiver,” or those that given assets from the DAO.

_Disclaimer: This is not accounting advice, just an intellectual exercise about how one can think about solving these issues._


### Financial Products Focused DAOs (MakerDAO Collateralized Debt Positions).

There is a distinction to be made with regards to MakerDAO. The organization itself is actually a private company, unlike some of the other examples referenced above. Rather than look at the funds flow of the company as a whole, we will analyze its product, the Collateralized Debt Position contract (CDP). This kind of product is sure to make most accountants heads spin. Below are simple sketches for how CDP users create and interact with CDPs. For a more complex look at this kind of transaction, I find [this article](https://medium.com/coinmonks/maker-dao-transactions-illustrated-691ad2715cf7) useful. The Pledger and Receiver are one in the same in this example.

To briefly summarize, a user essentially opens up a loan with a smart contract. They send ETH as collateral to the contract which will issue them DAI stablecoins. The user has an obligation to pay back the CDP the DAI it borrows and also make stability fee payments in either DAI or MKR (a governance asset). Sort of like making a sacrifice to the CDP gods to keep the crop of DAI stablecoins healthy.

![](/images/blog/dao-image4.png)

![](/images/blog/dao-image3.png)

### Pledger & Receiver

- #### Bookkeeping Entries.

The ETH transactions to create the CDP and request the DAI could be classified under expenses as gas fees.

Generally, bookkeeping entries are not made for collateral. They would just be noted on financial statements under loan liabilities. However, because there is an actual transfer of funds to the counterparty (CDP), an entry should be made. This is where financial statements are not able to fully represent the totality of the situation. We must convert all transactions to USD terms, and so we miss some of the nuances of what is actually happening in the transaction. Let’s go through a sample transaction. For the sake of simplicity, we will ignore some of the complexity of the fee structure, value fluctuation, and risk margins and just get to the core of the loan transaction:

As a very simple example, let’s say we open a CDP and collateralize 100 ETH with a spot price of $10 per ETH, and we want to withdraw 500 DAI. So we have:

1. $1000 of ETH locked as collateral
2. $500 of DAI withdrawn from the contract

One way to handle the situation would be to credit the crypto-asset account $1000 and credit a new liability account for CDP Loan for $1000. We would then debit crypto-asset account $500 to denote the receipt of DAI. This is an accurate accounting of what happened but leaves our books out of balance.

There is one type of entry that might be of use in this situation — debentures as collateral security. Debentures as collateral security occur normally when a lender requires extra collateral from the borrower. The borrower then issues debentures against fixed assets on their balance sheet. In practice, formal entries are not usually made, but instead a note is put on the liabilities side of the balance sheet. For the sake of keeping balanced books though we can make an entry that creates a debentures account under liabilities for $500 and a corresponding debentures suspense account under assets. When the loan is repaid to the CDP, then we can reverse the debentures entries made. If your CDP gets liquidated, the debentures would just sit awkwardly on your balance sheet.

DAI and MKR payments made to the CDP would be entered as any other standard loan repayments would: decrease to crypto-asset accounts and decrease to CDP loan liabilities.

- #### Tax Implication.

As with pretty much every other transaction discussed in this article, each movement of funds is subject to capital gains/loss rules. The USD cost basis must be tracked at each point. The capital gain/loss of DAI would obviously be virtually nonexistent since it is a stablecoin. The brunt of this calculation would need to occur with MKR and ETH.

### Grant Making & Work Commissioning DAOs (MolochDAO, Metacartel DAO, DAOstack).

The fund flow for these DAOs functions somewhat similarly to foundations like the Gates Foundation or Clinton Foundation. Cash is donated to the foundation which is then distributed by the foundation as its decision-makers see fit.

### Pledger

As a reminder, the Pledger is the person or company that is sending funds to a DAO.

- #### Bookkeeping Entries.

The bookkeeping treatment is a little bit dependent on how detailed the Pledger likes to keep their records. One option would be for the Pledger to make one expense entry denoting the amount sent to the DAO smart contract. If the Pledger withdraws their funds, they would need to make a reversing entry. A reversal can become a bit messy to get to balance because it is likely that the value of the asset will have fluctuated from the time of pledging to the time of withdrawal. An expense category called “Allowance for Crypto Differences” could help to account for the difference.

For the more meticulous bookkeeper, one would need to make a series of journal entries. An asset account could be created for the funds contributed to the DAO, which is then depleted over time after each distribution is expensed. For DAOs that have the ability for Pledgers to withdraw their funds, this would be the more appropriate categorization since the funds are still technically in the Pledgers control. This may also be a good way for the Pledger to keep track of the organizations that the DAO is funding. Because of the decentralized nature of the entity, the Pledger would need to be marking the value of the assets distributed according to a consistent policy for converting funds to their native fiat currency. Again an “Allowance for Crypto Differences” account would come in handy when balancing out the differences in price fluctuations.

- ### Tax Implication.

Unless there is a legal non-profit incorporation for a given DAO, the contributions made to the smart contract are not tax-deductible. Like all cryptocurrency transactions, each movement would require an analysis of the liability for capital gains/losses. If the Pledger is marking the distributions made to each recipient of DAO funds, there might be an opportunity for a tax write-off if one of the entities funded is a non-profit.

### Receiver

- #### Bookkeeping Entries.

If your business is the recipient of a grant from a DAO for a product or service, it would be classified as income using the USD value at the time of transfer according to your spot price marking policy.

- #### Tax Implication.

If the income is not converted to fiat upon receipt, a capital gain/loss calculation is incurred.

### Campaign DAOs (YangDAO).

The idea behind contributing to a DAO that in some way funds a presidential campaign is very new territory. It is unlikely that a campaign DAO would be able to register as a Super Pac since it would need to have a tax ID number, bank account, and appointed treasurer. Since the funds would be coming from one wallet, they would likely be subject to campaign finance laws if they plan to fund the campaign directly.

It appears that current intention of YangDAO is to commission works on its own that promote elements of the candidate’s platform.

### Pledger

- #### Bookkeeping Entries.

If the DAO makes distributions to the campaign directly, it is important to track the Pledger’s share of the funds that were distributed and ensure that it doesn’t exceed the limits of the Pledger’s other campaign contributions.

If the DAO funds activities unrelated to the campaign, the bookkeeping entries would align with the treatment of the Grant / Work DAOs.

- #### Tax Implication.

Capital gains/loss must be calculated for each fund flow.

### Receiver

- #### Bookkeeping Entries.

Financial record keeping for political campaigns requires specific support documentation. For a transaction of less than $50, all that is required is the name of the event where it was donated (if any), the date and total amount. For contributions over $50 documentation of the name of the contributor and the mailing address must also be captured. Images of the checks (or in this case block confirmation) must also be stored for audit purposes. For contributions over $200, the name and occupation of the contributor must also be saved. If for some reason, the campaign is unable to gather each data point, they must be able to demonstrate that they made “best efforts” to obtain it.

- #### Tax Implication.

Capital gains/loss must be calculated for each fund flow.

### Conclusion

As with other projects in the DeFi space, DAOs have created an economy of transactions that really don’t fit well into our current structures. We can anticipate that guidance from the AICPA, the SEC, the IRS, and other agencies will not be given for quite some time. One of the lessons we can take away from the SEC’s actions in 2019 though is that the appearance of at least making an effort to be compliant can take a company a long way. We are given an opportunity with these emerging products to pave the way for how these transactions should be treated.

This article serves as the first discussion that I am aware of on this topic. I hope that it can be a preliminary foundation for further debate and exploration about how to handle DAO accounting. If you’re interested in furthering the conversation, please contact me or leave your thoughts in the comments.


#### DeFi Accounting Series

<a href="/dao-accounting">Part 1: Decentralized Autonomous Organization Accounting</a>

<a href="/defi-accounting">Part 2: Crypto Lending & Borrowing Platforms</a>

---

Thanks to Derek Abdekalimi for his review of this article
