---
git-date:
layout: blog
title:  "Communications 101: Best Practices in Disclosing Software Vulnerabilities and Responding to Cyberattacks"
permalink: communications-cyberattacks
h1title: "Communications 101: Best Practices in Disclosing Software Vulnerabilities and Responding to Cyberattacks"
pagetitle: "DeFi Communications 101: Disclosing Software Vulnerabilities and Responding to Cyberattacks"
metadescription: "How to handle communications when disclosing software vulnerabilities and responding to cyberattacks. Best Practices 2020."
category: blog
featured-image: /images/blog/cyberattacks-og.png
intro: "How to handle communications when disclosing software vulnerabilities and responding to cyberattacks"
author: goldfarb
tags: ['For Builders']
---

“To err is human, to forgive divine.” -- Alexander Pope

Everybody makes mistakes. Whether you’re simply building useful software or trying to scale a startup into the next unicorn, you’re bound to hit some bumps along the way.

With so many cyberattacks being reported by the media, it’s become easy to forget about all of the vulnerabilities security professionals _are_ able to catch.

Fortunately for builders, people tend to be understanding when others take responsibility for their mistakes and make a sincere effort to correct them.

Whether you’re planning to deal with potential cyberattacks and reports of vulnerability or currently find yourself dealing with those issues, this article details best practices for communication when disclosing software vulnerabilities and responding to cyberattacks.

Read on to learn about best practices in handling the responsible disclosure of potential vulnerabilities and communication with stakeholders during cyberattacks.

## Terminology

It’s important to clarify some of the terms we’ll be using before we get into best practices for disclosing vulnerabilities and responding to cyberattacks.

Terms like “threat,” “vulnerability,” and “risk” may be used interchangeably in everyday conversation but these words take on very specific meanings when used in the context of security.

**Assets** include data, devices, and anything else relating to the management of information.

**Risks** are the potential problems that could arise if a threat were to exploit a vulnerability.

**Security Controls** refer to measures taken to prevent, detect, counter, and minimize risk.

**Threats** include the people and things that can exploit vulnerabilities.

**Vulnerability** refers to anything that can be exploited to gain unauthorized access to a system.


## Managing Responsible Disclosure

Dealing with software vulnerabilities in a professional manner is an effective way for DeFi developers to earn the loyalty of fellow developers, users, and other stakeholders and the best way to put that into practice is by respecting the principles of responsible disclosure.

**Responsible disclosure** is a protocol for notifying the appropriate stakeholders after discovering a vulnerability.

In contrast with [full disclosure](https://en.wikipedia.org/wiki/Full_disclosure_(computer_security)), responsible disclosure involves giving the developers of a piece of software an opportunity to address vulnerabilities before making them public.

The basic principles of responsible disclosure include:

*   Alerting the owner(s) of the software of your discovery as soon as possible.
*   Providing a reasonable amount of time for the owner(s) to respond to your notification, address the issue, and make a public statement.

What constitutes a “reasonable” amount of time is up to interpretation, which is what makes communication so important.

In spite of a reportedly lackluster response from Starbucks, Egor Homakov managed to alert the coffee giant to a vulnerability allowing him to [hack gift cards for free coffee](http://sakurity.com/blog/2015/05/21/starbucks.html) and get the issue resolved in less than two weeks.

On the other hand, the [Meltdown vulnerability](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html) disclosed by the Project Zero team at Google caused Intel x86 microprocessors and some ARM-based microprocessors to expose data in unintended ways and took seven months of work to get resolved.


### Communicating About a Potential Vulnerability

When managing the disclosure of potential vulnerabilities, providing an accessible path to responsible disclosure, respecting the value of those disclosures, and publicizing analysis of reported vulnerabilities are the keys to earning trust from fellow developers and stakeholders.

*   Set up an email or select your preferred communications channels for receiving disclosures and provide an accessible section on your website outlining contact information and policies around the disclosure of potential vulnerabilities.
*   Create a folder in the dApp’s front-end or main website  ./well-known/ and include a file called security.txt with that contact information and policies around disclosure to make it easier to find your bug program (see the example at [https://securitytxt.org/](https://securitytxt.org/)).
*   When someone reports a potential vulnerability, respond in a respectful and timely manner. Let the sender know you’ve received their report and provide a timeframe in which they can expect a follow-up.
*   Assume the best, but prepare for the worst. When dealing with bad actors, remain professional in communicating your position and only prepare a more elaborate response if the bad actor has the influence to harm the reputation of your organization.
*   Once you’ve had an opportunity to review the report and assess the potential vulnerability, follow-up with the sender to notify them of your findings and detail a plan for addressing the vulnerability.

Without maintaining regular and respectful communications, whoever reported the vulnerability may find it appropriate to publicize the vulnerability or take white-hat actions to prevent harm to users of the software.


### Publicizing a Vulnerability

After assessing the potential vulnerability and communicating with whoever made the disclosure, it’s important to have a plan for communicating immediate risks and following up with details on your analysis of the vulnerability and actions to mitigate it.

*   Designate a primary channel for publishing detailed information about vulnerabilities and maintain a list of secondary channels for broadcasting that information (ex. Email, Reddit, Telegram, Twitter, etc.).
*   If the vulnerability requires immediate attention, communicate what’s happening and what steps you’re taking to deal with the situation.
*   If the vulnerability can be handled without affecting regular use of the software, write a post-mortem including a timeline of events, credit to whoever reported the vulnerability, and details about the vulnerability and the steps being taken to fix it.

Here are some good examples of articles detailing disclosures:

*   [Argent bug bounty award to OpenZeppelin](https://www.argent.xyz/blog/argent-bug-bounty-claimed-by-openzeppelin/)
*   [Authereum disclosure reported by samczsun](https://medium.com/authereum/account-vulnerability-disclosure-ec9e288c6a24)

While responsible disclosure doesn’t address compensation for security professionals, providing bug bounties to compensate security professionals for their work is considered a best practice.

Examples of bug bounties in the DeFi ecosystem include:

*   [Argent](https://www.argent.xyz/argent-bug-bounty/)
*   [bZx](https://medium.com/@KyleJKistner/introducing-the-bzx-bug-bounty-program-ad74d3171444)
*   [Set Protocol](https://medium.com/set-protocol/introducing-the-set-protocol-bug-bounty-program-5790f16d2b8c)
*   [Uniswap](https://uniswap.org/bug-bounty)


## Managing a Cyberattack

In spite of the best efforts of security auditors, the fact that smart contracts have only existed for a few years means combined with the composability of DeFi applications means that all dApps face the possibility of exploitation through vulnerabilities that have never been seen before.

This isn’t to say that people shouldn’t use dApps and explore DeFi; it does, however, imply that users and developers should be aware of the risks and prepare accordingly.

The following sections will outline how to prepare for a cyberattack, what to do during the attack, and how to handle the aftermath.


### Develop a communication strategy

*   If your company stores any type of sensitive data, develop a plan for contacting users in the event of a breach.
*   DeFi projects that don’t store user data or maintain accounts via email should designate a particular communications channel for providing real-time updates and create a plan for sharing updates with users, the media, investors, and fellow team members.
*   Consider consulting a PR firm for advice on communicating with journalists when creating your communications strategy and/or setting aside funds to retain a PR firm in the event of a cyberattack to help manage your communications.

### Communicate with Stakeholders

*   Was the attack brought to your attention by a non-threatening source? If so, let them know you’ve received their message about the attack and where they can find updates on your response.
*   Select a primary channel for real-time communication, provide regular updates, and include a link to it in all updates regarding the vulnerability (ex. Telegram, Discord, email, etc.).
*   Maintain a list of secondary channels for broadcasting updates (ex. Twitter, Reddit, Medium, etc.).
*   If the breach involves the disclosure of personally identifiable information (PII) or other sensitive data, contact the affected parties to let them know what happened, how you’re responding, and where they can go for the most timely update on the situation.

### Dealing with FUD

*   Not everyone spreading FUD and misinformation deserves a response but any response should be proportional to the individual or organization’s influence on your reputation.
*   Have a community manager or designated individual responsible for responding to questions and concerns to prevent speculation from damaging your narrative.
*   Consider retaining a PR firm to advise on interactions with journalists, general communications, and how to preserve the reputation of the organization.

### Manage the Aftermath

*   Whether damages result from the cyberattack or not, transparency is the key to building and retaining trust from stakeholders.
*   Follow through on all communication with stakeholders, publish and distribute a “post-mortem” or “debriefing” detailing what happened during the attack, how you responded, and what will be different going forward.
*   Plan to field questions from reporters and be sure all team members understand what happened, how the organization responded, and how the organization prefers to handle communication with journalists.

A thorough post-mortem should:

*   Provide a timeline of events
*   Explain what allowed the exploit to happen
*   Detail the response to the attack
*   Talk about what will be different going forward
*   End with links and a “call-to-action” explaining who stakeholders can contact for further details and where to go for more information

Examples of post-mortems in the DeFi ecosystem include:

*   [bZx](https://bzx.network/blog/mea-culpa)
*   [Opyn](https://medium.com/opyn/opyn-eth-put-exploit-post-mortem-1a009e3347a8)


### Thanks for Reading

Interested in learning more about risk in DeFi? Check out the article: [A guide to financial risk in DeFi](https://defiprime.com/risks-in-defi).

Special thanks to Ken Hodler for advising on cybersecurity, and Harry Denley for article peer review.
