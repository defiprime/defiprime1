---
git-date:
layout: blog
title:  DeFi Smart Contract Audits
permalink: defi-smart-contract-audits
h1title: 'Expert Roundup: DeFi Smart Contract Audits'
pagetitle: 'Expert Roundup: DeFi Smart Contract Audits'
metadescription: 'A software audit is a process where an individual or team examines the code that lies behind a piece of software with the goal of uncovering any bugs, security breaches, or violations of programming conventions before the code gets deployed'
category: blog
featured-image: /images/blog/defi-smart-contract-audits-og.png
quote: /images/blog/defi-smart-contract-audits-quote.png
intro: 'When it comes to “being your own bank,” having the ability to evaluate the security of the tools at your disposal becomes a necessity.'
author: Defiprime
---
When it comes to "being your own bank," having the ability to evaluate the security of the tools at your disposal becomes a necessity.

A software audit is a process where an individual or team examines the code that lies behind a piece of software with the goal of uncovering any bugs, security breaches, or violations of programming conventions before the code gets deployed. Smart contract audits play a critical role in evaluating the technical risks associated with a dApp but as a relatively new form of code, the standards for software audits of smart contracts remain in their infancy.

Companies like [ChainSecurity](https://chainsecurity.com/), [Trail of Bits](https://www.trailofbits.com/), and [Certik](https://certik.org/) provide smart contract audits and have adopted their own standards for how a proper audit should be conducted. Until the industry adopts its own standard, however, customers have to rely on the reputation of these companies and the team members conducting the audit to evaluate the quality of a potential audit. To help you understand the current state of smart contract security, we've gathered insights from a number of industry experts.

![](/images/blog/experts1.png)

### Q1: What is the smart contract audit exactly?
There is a lot of misconceptions in the space, like many of DeFi users thinking that smart contract audit is a sort of silver bullet and sign of security (or lack of) of the dApp.

#### Hubert Ritzdorf, ChainSecurity:

A smart contract audit is an independent review that assesses the security and correctness of the code. This provides the following advantages. First, users obtain an independent opinion on how the smart contract behaves, which can alert them about potential threats. Project managers receive valuable feedback about their projects and can take the necessary steps to mitigate security risks. Finally, developers receive important security advice and concrete security bug reports. However, not all audits are the same. The value provided by an audit depends on the technology used to conduct it and the expertise of the audit team.

#### Dan Guido, Trail of Bits:

Think of security assessments like getting your car inspected: If you do it early enough, the mechanic can recommend parts to replace and preventative maintenance that can avert leaving you stranded at the side of the road later. If you wait until 300,000 miles to get your first service, the damage might be irreparable.

The amount of time you allot for inspection also makes a big difference: Give the mechanic 30 minutes, and they might only have time to use an automated scanner to determine that your spark plugs are bad. Give the mechanic a day, and they might have time to diagnose the underlying cause of why the spark plugs became bad (failed sensors? wiring? engine running rich?).

Scope also matters: Request that the mechanic only diagnose problems with the alternator, and the car may drive away with a repaired alternator as well as a latent, undiagnosed issue with the transmission.

It is the mechanic's job to provide advice, but it is ultimately up to the owner to decide if, when, and how to implement the recommendations.

#### Daryl Hok, CertiK:

In the simplest sense, a smart contract audit is a third-party review of the source code of a smart contract. Although a completed audit means that the code was reviewed, the rigorousness of the audit may vary substantially - and this rigor is really what matters for security, not merely the presence of an audit. For instance, a dApp may flaunt that no errors were found during the audit process, but it's difficult to determine whether this means that the code quality was extremely high or whether the auditor was really bad.

At CertiK, we specialize in using Formal Verification to prove or disprove the correctness of source code; we apply mathematical proofs to compute source code outcomes and prove the absence of bugs, meaning that, if there are no bugs found, it is not possible for the specified vulnerabilities to exist.

### Q2: Are there degrees of "approval"?

Are there some contracts where you're more confident they are solid vs. others where you can't find a problem, but you are less confident?

#### Hubert Ritzdorf, ChainSecurity:

A limited audit scope affects confidence levels. Before the audit begins, we determine the scope together with the customer. It can be decided not to review certain dependencies or components due to time or budget constraints. To clarify this, our audit reports always precisely state the scope of the audit.

#### Dan Guido, Trail of Bits:

We try to make it easy to understand what happened on a security review. If you're investigating the health of a project, then pay attention to these sections in our reports:

1. Executive Summary. This section includes a brief review of what we did, what we found, and what we recommend as next steps. It should make clear how much work is ahead of the project to remediate the risks we identified.
2. Project Dashboard. This easy-to-read table summarizes the level of effort applied to review the codebase and what was found. Did we identify systemic issues? Was every bug identified high severity? Get a visual indicator by glancing at this table.
3. Engagement Goals. This section describes our scope, or, what we set out to do on the project. Did we seek to identify risks that you care about? You'll find out by reviewing our own goals for the project.
4. Coverage. This section discusses our ability to achieve our engagement goals within the constraints of the project. You'll find information on specific contracts and techniques we used to review them here, as well as pointers for future review.

It's no accident that these are the top four sections in all our reports.

#### Daryl Hok, CertiK:

In the case of Formal Verification, the results are binary - when the mathematical model runs, it either identifies an example of the vulnerability in the code, or it does find anything, which means that it's secure. As a result, our confidence is tied to the output of these results in these instances. When it is not feasible for Formal Verification to be applied, we utilize various tools to test the security, while also performing thorough manual examination.

Our confidence level is a collective consideration of the usage of commonly accepted best practices, patterns, libraries, as well as the quality of documentation and test cases. Rare, complex patterns typically reduce our confidence or require more customized review of whether the output is consistent with the intention. Overall, we work with projects to correct all critical vulnerabilities and antipatterns before publishing any passing audit scores.

### Q3: What are the five most common things people miss in smart contracts that make them vulnerable?

#### Hubert Ritzdorf, ChainSecurity:

1. Improper access control: granting access to unauthorized parties or denying access to authorized ones
2. Front-running or back-running: No enforcement of execution order
3. Improper input sanitization: insufficient filtering of untrusted user inputs
4. Logical errors: logical flaws in the code due to faults in the code
5. Numerical errors: rounding errors and incorrect arithmetic calculations

#### Dan Guido, Trail of Bits:

It has everything to do with development process rather than awareness, or not, of individual security issues.

1. Developers are simply not using security tools. Ask any developer about unit tests, and they'll say they won't ship without 100% test coverage. Yet, many of those same people will have never used, or even tried to use, security testing or verification tools. Don't leave it for the security consultants -- nearly all the best tools are [free](https://github.com/crytic).

2. Developers still look at security as the last step before production. I'm writing this interview about a month ahead of DevCon, and my schedule has never been so busy. Developers should seek guidance earlier, including developer training, architectural review, and brief checkins over the lifetime of the project.

3. Developers are writing too much code without a clear idea of its purpose or whether it is needed at all. Developers should start with a specification and then write the minimum amount of code to meet it. Our best-performing clients have documented security requirements in their spec. Complexity breeds insecurity; keep it simple.

4. Developers rush to use bleeding-edge third-party dependencies that increase complexity and reduce the safety of their project. Examples include low-level optimizations, [delegatecall proxy upgrades](https://blog.trailofbits.com/2018/09/05/contract-upgrade-anti-patterns/), ABIEncoderV2, and even the latest version of the Solidity compiler. Be judicious about inherited risks.

I don't think there is a step five. You'll be ahead of nearly every other project if you can do these four.

#### Daryl Hok, CertiK:

1. Integer overflow/underflow
2. Not updating the balance first before further operations. (reentrancy vulnerability)
3. Writing loops without considering the gas cost. (DoS vulnerability)
4. Lack of balance checking for value transfer operations.
5. Lack of permission settings and permission check for public/external functions.
6. Use of `block.timestamp` and `block.number` without considering their drawbacks (`block.timestamp` can be modified by miners; time between two consecutive block numbers is dynamic so `block.number` is not ideal for a stable time delta estimation).

### Q4: I see a project claiming on twitter that they had audited smart contract code.
How can I check if they are not lying? What research do we have to do to see if the audit is not fake or manipulated?

#### Hubert Ritzdorf, ChainSecurity:

Ideally, the project should publish the audit report. The report must identify the auditor and their methodology, the findings, and how these were addressed. This enables users to inspect the credentials of the auditor and to ensure that the audit was conducted professionally and follows best practices.

#### Dan Guido, Trail of Bits:

If you're looking to determine the authenticity of a security review, then the easiest way is to find it on the security vendor's website. Trail of Bits maintains an archive of nearly all the security reviews we've conducted, whether or not they result in a report, on [Github](https://github.com/trailofbits/publications#security-reviews).

If you're judging the validity of the report, then you should see if it identifies precisely who was involved in the audit, for how long, and their contact information. Further, the project should clearly state how each finding in the report was addressed, preferably with cross-references to relevant commits in their source code repository. Ideally, the project engages the assessment team to re-test their code after the fixes, resulting in a revised report with an accounting of remediations.

Finally, it's a red flag when a security review includes opinionated statements like, "This code is secure", "users can trust this project", or similar effusive praise for their clients. Security vendors should be careful to speak about only objective facts. Trail of Bits has [published guidelines](https://github.com/trailofbits/publications/blob/master/reviews/citation_guidelines.pdf) to help our clients speak effectively about our work with them.

#### Daryl Hok, CertiK:

All of CertiK's clients are provided with a cryptographically hashed QR code that act as a badge of proof; anyone can scan the QR code, and they are redirected to a website hosted on our servers that will confirm the validity of an audit. If there is a counterfeit QR code, it will either direct the user to the verified webpage of a different project, or it just won't work. Within these webpages, along with the report itself, the audited commit hash is saved, so you can also keep track of version history. If the code version has changed, we would no longer be able to confirm that the code has been fully audited, but we do allow projects to engage in free re-auditing.


### Q5: How to test the team that is doing the smart contract audit to know if they are real and legit?
I guess not all auditors are the same.

#### Hubert Ritzdorf, ChainSecurity:

Correct, not all auditors are the same. While there is not yet a standard way to evaluate auditors, there are several helpful indicators to assess the expertise of an auditor. For example, users can check the credentials and background of the auditor, read past reports and how these compare to those prepared by other auditors (many security-conscious projects request multiple independent audits which allows for such a comparison), review the technology and methodology used during the audit. A professional auditor always defines a precise specification of the project and details the audit procedure and tools used. In practice, many users tend to also rely on testimonials provided by the auditor's clients.

#### Dan Guido, Trail of Bits:

Here are a few recommendations for evaluating a security vendor:

- Do they have relevant experience in security? It takes years to grow a security engineer. Find a team with a strong foundation of security fundamentals.
- Have they published original research in your field? Blockchain security is a new field with undiscovered pitfalls. It's not enough to only use current best practices.
- Will they share their tools with you? You'll want to build on their progress. Shared tools also ensure that the results are repeatable and verifiable by others.
- What are the outcomes you'll receive? Anyone can provide a list of bugs. Will they have context? Architectural and process recommendations? Custom tools?
- Can they address risk in areas adjacent to the surveyed product? Smart contracts typically depend on advanced cryptography, off-chain oracles, and much more.

Once you find a good security vendor, stick with them! One large review with a qualified security vendor is worth more than two small ones. You'll get more strategic results, better integration of automated testing and verification tools, and a chance to find higher severity bugs that only come with domain knowledge.

#### Daryl Hok, CertiK:

Much can be learned by looking at any publicly available audit reports for an auditor's clients. Within the reports, there should be a description of the tests and workflow performed during the audit process. In these reports, you may want to look past aesthetics and dive into the content of the report to find explanations of different tools and techniques used during the auditing process, familiarity of different EIP (Ethereum Improvement Proposals) and common practices, and general transparency. In CertiK audit reports, we provide a copy of the entire source code, annotated with CertiK's Formal Verification labels, so anyone can independently check and confirm the validity of the mathematical proofs.

### Q6: How important is formal verification?

#### Hubert Ritzdorf, ChainSecurity:

The ultimate goal of an audit is to guarantee that the code is free of bugs and behaves as intended under all circumstances. This can only be achieved if one formally specifies the intended behavior and formally proves the correctness of the code with respect to the specification. Formal verification is, therefore, an essential tool when it comes to proving the correctness of mission-critical applications, such as smart contracts.

#### Dan Guido, Trail of Bits:

It is critical that developers define security properties as they work on their spec and write their code. Helping identify and further define security properties is one of the most important outcomes we provide as security consultants brought in to help them.

However, formal verification has become a buzzword in the blockchain community, to the point that it has lost much of its meaning. It's not a magic technique, or even a single technique, and we commonly identify high-severity flaws in formally verified code.

For example, we recently completed a [historical study](https://blog.trailofbits.com/2019/08/08/246-findings-from-our-smart-contract-audits-an-executive-summary/) of every smart contract review ever completed by Trail of Bits. We found that 50% of the bugs we discover cannot ever be found by any automated analysis, even in theory. Humans are not out of a job yet!

It's also important to understand that there are many ways to verify security properties once you've defined them. If you want to verify access controls, inheritance, upgradeability, or standards conformance, then static analysis might work best, like Slither. If you want to verify state machines, arithmetic operations, or external interactions, then dynamic analysis might work best, like Echidna or Manticore. If you have time to write extensive specs and want to eliminate data validation issues, then klab might work best. It depends!

No matter how you approach it, remember that formal verification is not a way to avoid making other investments in security. Every verification technique comes with limitations and, empirically, 50% of the bugs we find can only be discovered by expert review. Contacting a security vendor will help you prioritize your risk, train your staff, and apply verification techniques in the most effective manner possible.

#### Daryl Hok, CertiK:

Typically, Formal Verification has been associated with mission-critical hardware applications, such as NASA's Mars rovers, drones, and airplanes. Blockchain, however, is a software application that has proven to be just as mission-critical; the publicly viewable, self-executing, and permanent nature of smart contracts have become a lucrative target for malicious hackers. Because centralized "help desks" don't exist in blockchain, users must be meticulous about the security of the infrastructure, particularly if the technology holds high value.

Blockchain is global and trustless, so trust in the underlying security should also be consistent. Mathematics is one of the only objective, independently verifiable, and universally consistent concepts worldwide, so Formal Verification successfully removes the need to trust a centralized entity.

### Conclusion

Auditing your code is a critical part of the software development lifecycle and developing smart contracts is no different. As our experts noted, there are a number of important factors to consider when selecting a security vendor for a smart contract audit. For those who aren't ready for an audit or may not be able to afford one, companies like OpenZeppelin and Trail of Bits have of free tools available for developers to make use of. Regardless of what level of the stack you're working on, smart contract security must be a top priority for those interested in securing the future of DeFi.

Shout out to members of [DeFi Nation FB Group](https://joindefination.com/), who helped to shape this list of questions.

And thanks to our experts:

Hubert Ritzdorf, [ChainSecurity](https://chainsecurity.com/): [@hritzdorf](https://twitter.com/hritzdorf)
Daryl Hok, [Certik](https://certik.org/): [@DarylHok](https://twitter.com/darylhok)
Dan Guido, [Trail of Bits](https://www.trailofbits.com/): [@dguido](https://twitter.com/dguido)
