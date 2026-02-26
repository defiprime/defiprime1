---
git-date:
layout: [blog]
title: "Canton Network vs. EVM-Compatible Blockchains: A Technical Reckoning"
permalink: canton-vs-evm
h1title: "Canton Network vs. EVM-Compatible Blockchains: A Technical Reckoning"
pagetitle: "Canton Network vs. EVM-Compatible Blockchains: A Technical Reckoning"
metadescription: "A deep technical comparison of Canton Network and EVM-compatible blockchains. Explore execution models, privacy guarantees, trust assumptions, scalability, and where each platform excels for institutional and DeFi use cases."
category: blog
featured-image: /images/blog/cantonevm.png
intro: "The blockchain landscape has split more sharply than most architects acknowledge. The EVM ecosystem and Canton answer different questions—comparing them as if they were racing toward the same finish line misses the point."
author: Defiprime
tags: ["DeFi Guides", "Infrastructure"]
---

The blockchain landscape has split more sharply than most architects acknowledge. The EVM ecosystem—[Ethereum](/ethereum) and its compatible chains—runs on a shared global state machine that anyone can read, write to, and build on without permission. [Canton](https://canton.network), built atop [Digital Asset](https://www.digitalasset.com)'s [Daml](https://docs.canton.network) smart contract language, was designed around privacy by default, optional legal enforceability, and the ability to support both permissionless participation and regulated applications on the same network. These two systems answer different questions. Comparing them as if they were racing toward the same finish line misses the point.

Getting the comparison right means tracing each system back to the assumptions its architects made: what they decided the ledger was _for_, who they imagined would use it, and which failure modes kept them up at night.

---

## The philosophy gap

**EVM: the transparent world computer**

Ethereum's original thesis was a globally shared, permissionless, censorship-resistant computer where anyone could deploy code and anyone could inspect the results. The EVM treats the blockchain as a single replicated state machine. Every full node maintains a complete copy of the global state trie. Every transaction that mutates that state must be executed by every validator. Transparency isn't incidental—it's load-bearing. The security model depends on everyone being able to verify everything.

This philosophy produced a remarkably active software ecosystem. [Uniswap](/uniswap-explained), [Aave](/aave), [MakerDAO](/makerdao-compared-to-equilibrium), and thousands of other protocols exist because deploying to Ethereum requires no permission, no legal agreement, and no institutional relationship. The EVM's Turing-completeness and open composability made [DeFi](/decentralized-finance-5-things-you-should-know) possible. It also made privacy structurally impossible at the base layer.

**Canton: the confidential sub-transaction network**

Canton starts from a different premise: for most institutional financial workflows—securities settlement, syndicated lending, FX netting, derivative clearing—_selective disclosure_ is a regulatory and commercial requirement, not a preference. A bond issuer cannot expose its complete order book to every network participant. A bank cannot share the details of a bilateral derivative with counterparties who have no relationship to that trade.

Digital Asset's response was to abandon the shared global state model. In Canton, there is no global ledger that all participants maintain. Each piece of data—each "contract" in Daml parlance—is known only to the parties explicitly named in it. The ledger is not a database everyone reads; it is a collection of private sub-ledgers whose consistency is guaranteed by cryptographic proofs and a synchronization protocol between synchronizers and participant nodes. The network does not achieve consensus on a single world-state. It achieves consensus on _the sub-set of state that each participant is entitled to see_, and those sub-ledgers are kept consistent by a protocol that guarantees global coherence without global visibility.

That architectural choice has consequences for execution, privacy, scalability, and trust throughout the stack.

---

## Execution models

**The EVM execution environment** within each block. When a transaction is submitted, it specifies a target contract address, a function selector, encoded arguments, and a gas limit. The EVM—an isolated stack machine with 256-bit word sizes—executes the bytecode at that address, potentially making inter-contract calls (CALL, DELEGATECALL, STATICCALL), reading from and writing to a key-value storage trie associated with the contract's address. All state reads and writes are visible to any observer with access to an archive node.

Gas is the metering mechanism. Every EVM opcode has a fixed gas cost; the sum must not exceed the block gas limit. This prevents infinite loops and creates a fee market, but it also means that complex smart contracts must be carefully optimized to avoid exceeding per-transaction gas bounds. The EVM has no native support for off-chain computation or private inputs—any data written to a contract is public.

[Solidity](https://soliditylang.org) and [Vyper](https://vyper.readthedocs.io) compile to EVM bytecode. The ABI encoding scheme is standardized, enabling composability across contracts: [Uniswap](/uniswap-explained) can call [Chainlink](/chainlink), which can call [Aave](/aave), and the entire multi-protocol transaction either atomically succeeds or atomically reverts. This atomicity across the global state is one of the EVM's most powerful features. It is also what makes truly private computation so difficult—atomic cross-contract calls only work if both contracts share the same execution context, which requires visibility.

[Layer 2 systems](/ethereum-l2)—Optimistic Rollups like [Arbitrum](https://arbitrum.io) and [Optimism](https://optimism.io), ZK-Rollups like [zkSync](https://zksync.io) and [StarkNet](https://www.starknet.io)—modify this model by batching EVM transactions off-chain and posting compressed results (with fraud proofs or validity proofs) to Ethereum mainnet. But the execution semantics within an L2 remain EVM-compatible: the global state model, the bytecode interpreter, and the transparency assumptions all carry over. L2s improve throughput and reduce fees; they do not change who can see what.

**The Canton/Daml execution environment**

Canton's execution model is built around the concept of a _contract_—not in the Ethereum sense of "code living at an address," but in the legal-contract sense: a data structure representing an agreement between named parties, along with a set of permissible actions (choices) that those parties can exercise. Daml contracts have explicit signatories (parties whose authority created the contract), observers (parties who can see the contract), and controllers (parties who can exercise specific choices).

When a Daml choice is exercised, the transaction is represented as a _transaction tree_: a hierarchical structure of create, exercise, and archive actions. This tree is decomposed before being submitted to the network. Each node in the tree is disclosed only to the participants who need to see it—the parties to the contracts involved in that node. The Canton protocol routes these fragments to the appropriate participant nodes via a synchronizer. The synchronizer—which contains a sequencer and a mediator—handles ordering, delivery, and a two-phase atomic commit, but does not execute or validate any transaction. Validation is performed by participant nodes (Validators), which confirm only the sub-transactions they are party to, without seeing sub-transactions that belong to other parties.

The result is _sub-transaction privacy_: in a multi-step workflow involving Party A, Party B, and Party C, Party A does not automatically learn the details of the step that occurs only between Party B and Party C, even if that step is part of the same atomic transaction. This is architecturally unavailable in the EVM without a separate off-chain computation layer and cryptographic proofs (as ZK co-processors like [Risc Zero](https://www.risczero.com) attempt to provide).

Canton [Validators](https://docs.global.canton.network) process these transactions on the participant side. The synchronizer—a separate infrastructure component—provides BFT-based ordering and a two-phase atomic commit protocol, but does not see the content of private contract data. Validators confirm the transactions they are party to, apply them to their local contract state, and maintain only the slice of the global ledger that belongs to them. Anonymous Validators can join the network and contribute to transaction processing without disclosing their identity.

One operational distinction worth noting: Canton transactions reference _specific contract instances by their unique contract ID_, not by a globally shared storage slot. This means Canton's execution model resembles a UTXO model more than an account model—contracts are created, referenced by subsequent transactions, and eventually archived. There is no mutable global key-value store that all participants read from and write to. This has significant implications for concurrency, addressed in the scalability section.

---

## Privacy guarantees

**EVM chains: pseudo-anonymity at best**

On Ethereum mainnet, all transaction data—sender address, target address, input data, event logs, state diffs—is permanently public and indexed by the global state. The pseudo-anonymity of addresses is meaningful only before an address is linked to a real-world identity, and the on-chain transaction graph is often enough to deanonymize sophisticated actors. Chain analytics firms like [Chainalysis](https://www.chainalysis.com) and [Elliptic](https://www.elliptic.co) trace address clusters and transaction patterns as a commercial service.

Privacy-preserving techniques in the EVM ecosystem include:

_Tornado Cash / mixers_ — pool deposits from multiple senders and allow withdrawals from new addresses, breaking on-chain linkability. OFAC sanctioned Tornado Cash in 2022 and arrested its developer in 2023, which should give pause to anyone treating "censorship resistant" as an unconditional property. The approach also provides no privacy for the _content_ of transactions, only the sender's identity.

_Commit-reveal schemes_ — parties commit to a hash of their data on-chain, then reveal later. Useful for auctions and voting, but still exposes final values and does not suit ongoing confidential relationships.

_FHE / TEEs_ — emerging approaches from protocols like [Fhenix](https://fhenix.io) (FHE) and [Oasis Network](https://oasis.network) (TEEs) that allow computation on encrypted data. Promising but currently impractical for complex financial logic at scale due to computational overhead (FHE) or hardware trust assumptions (TEEs).

_ZK co-processors_ — [Aztec Network](https://aztec.network) is building a private smart contract layer using ZK proofs, where the EVM bytecode is compiled to a circuit and the proof attests to correct execution without revealing inputs. Technically sound but still nascent, with significant developer experience friction and proving time overhead.

None of these approaches is native to the EVM itself. They are layers applied on top of a transparent system.

**Canton: privacy by construction**

Canton's privacy model is built into the transaction model rather than layered over it. The key mechanisms:

_Party-level privacy_ — a contract's data is stored only on the participant nodes of the parties explicitly named in the contract. The synchronizer sees encrypted metadata necessary for ordering but not the contract payload itself.

_Sub-transaction privacy_ — as described above, different legs of a multi-leg transaction can be disclosed to different subsets of parties. A CCP (central counterparty) might see only the net obligations between parties, not the gross bilateral trades that produced them.

_Divulgence_ — Canton supports a mechanism by which a party can be shown a contract's data (for verification purposes) without being made a signatory or observer. This allows auditors or compliance nodes to be granted read access to specific contracts without becoming participants in the workflow itself.

_Cryptographic verification_ — participants validate transactions cryptographically, checking that exercises on contracts are authorized by the correct parties and that the transaction tree is internally consistent, without needing to see contracts held by other parties. This uses Merkle proofs and commitment schemes embedded in the Canton protocol.

Concretely: a Canton deployment at a bank consortium can have participant A and participant B transact with each other, with participant C operating the synchronizer, without participant C learning the economic terms of A and B's trade. On any EVM chain, this requires additional cryptographic machinery that does not yet exist at production scale for complex financial contracts.

The tradeoff: Canton's privacy model makes global verifiability hard. A third party who is not a named participant in a contract cannot verify its contents—which is exactly the point, but it means Canton cannot support the permissionless "anyone can verify" security model that Ethereum depends on.

---

## Trust assumptions

**EVM trust model: cryptoeconomic security**

Ethereum mainnet's security derives from [Proof of Stake](/staking) consensus among a permissionless validator set. As of mid-2025, roughly 1 million validators have staked ETH to participate. A 51% attack requires controlling ~33% of stake for finality attacks or ~51% for safety violations—economically prohibitive at current ETH valuations, though the theoretical risk exists. The trust assumption is cryptoeconomic: rational actors will not attack the network because slashing destroys their stake.

EVM smart contracts are trustless in a specific sense: once deployed, they execute deterministically according to their bytecode, with no ability for the deployer to unilaterally modify behavior (unless the contract contains upgrade mechanisms). This "code is law" property works well in permissionless contexts but creates problems in enterprise settings where regulatory requirements may necessitate reversibility.

EVM-compatible L1s and L2s vary significantly in their trust assumptions. [BNB Chain](https://www.bnbchain.org) has 21 active validators—effectively a federated system controlled by Binance-aligned entities. [Polygon](https://polygon.technology) PoS has roughly 100 validators. [Arbitrum](https://arbitrum.io)'s sequencer is currently a single operator (Offchain Labs) with a planned transition to a decentralized sequencer set. These are not Ethereum's security model; they are pragmatic compromises that institutional buyers should understand clearly.

**Canton trust model: cryptographic and protocol-level guarantees**

Canton's trust model relies on protocol-enforced guarantees rather than a single enforcement mechanism:

_Cryptographic correctness_ — transaction validity is enforced by the [Daml](https://docs.canton.network) runtime and Canton protocol. Validators cryptographically verify that exercises on contracts are authorized by the correct parties, that contract invariants hold, and that the transaction tree is internally consistent. This is deterministic, not probabilistic.

_Synchronizer operator trust_ — the synchronizer provides ordering, delivery, and a two-phase atomic commit. On the [Global Synchronizer](https://docs.global.canton.network), this operates under BFT consensus: all actions require a two-thirds supermajority, so no individual node can censor or block transactions, either actively or by being unavailable. Private subnets may still choose a centralized synchronizer—much as many EVM L2s run centralized sequencers—but the main network does not require a trust relationship with any single operator.

_Legal enforceability as an option_ — Daml was designed so that a smart contract _can_ be a direct expression of a legal agreement. The signatories on a Daml contract have the same semantics as signatories on a legal document. Applications built on Canton can choose to leverage traditional legal frameworks, with the ledger serving as an auditable record. This is an application-level choice, not a network-level requirement.

_Synchronized sub-ledger consistency_ — the Canton protocol guarantees that if two participants hold contracts on different synchronizers, a transaction that spans both is executed atomically or not at all. On the Global Synchronizer, this is guaranteed by BFT consensus and a cryptographic commitment scheme, removing the need to trust any individual synchronizer operator.

Canton accommodates a range of trust models: from fully permissionless participation at the network level (where any party can join, hold assets, and transact without credentials) to application-level permissioning (where specific apps may require KYC or credentials for their users). This separation is how Canton can be both permissionless and regulatory-compliant simultaneously.

---

## Scalability

**EVM scalability: the scaling stack**

Ethereum mainnet currently processes roughly 15–30 transactions per second, bounded by block gas limits and 12-second block times. This is deliberately conservative—Ethereum prioritizes decentralization and security over throughput. The roadmap—[Proto-Danksharding (EIP-4844)](https://eips.ethereum.org/EIPS/eip-4844), Danksharding, and eventually full sharding—is designed to increase data availability bandwidth by orders of magnitude, enabling L2 rollups to post far more transaction data at lower cost.

The rollup ecosystem is Ethereum's primary scaling answer. [Arbitrum](https://arbitrum.io) One handles roughly 10–40 TPS at network load, with theoretical capacity much higher. ZK-Rollups like [zkSync Era](https://era.zksync.io) process similar volumes with faster finality guarantees. For most [DeFi](/exchanges) applications this is workable. For institutional transaction volumes—DTCC processes roughly 120 million transactions per day, Visa handles ~24,000 TPS at peak—it is not sufficient without multiple parallel rollups and off-chain aggregation.

EVM chains scale horizontally only at the cost of fragmentation: a transaction on [Arbitrum](https://arbitrum.io) and a transaction on [Base](https://base.org) are not atomic with each other. Cross-chain atomic transactions require [bridges](/history-of-cross-chain-bridge-hacks), which are a persistent source of security risk—hundreds of millions of dollars have been lost to bridge exploits.

The EVM's sequential execution model creates a bottleneck within a domain: transactions touching the same state must be serialized. Parallel EVM initiatives ([Monad](https://monad.xyz), [Sei](https://www.sei.io)) are attempting to execute non-conflicting transactions simultaneously using optimistic concurrency control, but this requires sophisticated conflict detection and remains in early production stages.

**Canton scalability: horizontal parallelism by design**

Canton's scalability works differently. Because the ledger is partitioned by contract—each contract exists on one or more synchronizers, and transactions reference specific contract IDs—transactions on different contracts can be processed in parallel without conflict detection overhead. There is no global state trie creating write contention.

Adding a new synchronizer effectively adds a new parallel track for transactions. The network scales horizontally: throughput is proportional to the number of synchronizers, which operate in parallel without coordinating on every transaction. Cross-synchronizer transactions use a two-phase atomic commit protocol, which adds latency but maintains atomicity guarantees.

Digital Asset has published benchmarks showing Canton participant nodes handling thousands of transactions per second per synchronizer. Total network throughput across all synchronizers can scale to enterprise volumes without the global sequencing bottleneck that constrains EVM chains.

Since the launch of the Global Synchronizer in mid-2024, Canton's scalability is not bounded by a permissioned participant set. Anonymous Validators can join the network to contribute to transaction processing, and Validator ownership can be transferred after onboarding without disclosure. Adding throughput does not require credentialed or identified operators.

One nuance: Canton's horizontal scaling comes with a composability cost. In the EVM, any contract can call any other contract atomically because they share a global state. In Canton, cross-synchronizer atomic transactions are supported but require coordination between synchronizer operators. Two contracts on the same synchronizer can transact with minimal overhead; two contracts on different synchronizers require the two-phase commit protocol, which adds round-trip latency. This is manageable in workflows where transaction graphs are pre-defined, but it imposes a design discipline that EVM developers do not face.

---

## Decentralization

This is perhaps where the two systems' philosophies are most nakedly at odds.

**EVM: permissionless decentralization as a core value**

Ethereum's validator set is permissionless—anyone with 32 ETH can become a validator. The client diversity across Prysm, Lighthouse, Teku, Nimbus, and Lodestar reduces the risk of a single software bug taking down the network. Contracts can be deployed by any address, called by any address, and their state can be read by any node.

This permissionlessness is what makes Ethereum genuinely censorship-resistant. Post-Merge, Ethereum has shown resilience against validator-level censorship through MEV-Boost and OFAC compliance debates—the network continues to include non-OFAC-compliant transactions, albeit with some validator-level filtering. No single entity can prevent a transaction from eventually being included.

EVM L2s sacrifice degrees of decentralization for performance. [Arbitrum](https://arbitrum.io)'s sequencer is centralized today. [Base](https://base.org) is operated by Coinbase. [zkSync](https://zksync.io)'s prover infrastructure is controlled by Matter Labs. These are pragmatic choices that meaningfully change the trust model—participants in these systems are trusting specific companies, not a decentralized validator set.

**Canton: permissionless network, permissioned applications**

Canton's decentralization model is more nuanced than a simple "permissioned" label suggests. At the _network level_, Canton is permissionless: any party can join, hold assets (Canton Coin, CBTC, USDC, and others), and transact without any permissioning or gating. Node operators do not have to disclose their identity. Hundreds of thousands of uncredentialed users already participate in the network.

Permissioning operates at the _application level_. If a user wants to join a specific regulated application—say, a permissioned securities settlement platform—that application may issue credentials. But this governs the right to use that application, not the network itself. This separation is analogous to how the internet is permissionless infrastructure, while individual websites may require login credentials.

The [Global Synchronizer](https://docs.global.canton.network) provides a decentralized ordering layer for the Canton Network. It is built on a BFT consensus ordering layer under Canton's two-phase atomic commit protocol—not on Besu. Super Validators are known entities _by choice_, not by requirement. They advertise their identity voluntarily but operate with complete independence from each other. Every action they take—both on-chain and in off-chain operational and governance decisions—is a vote via two-thirds supermajority. There are no written agreements, contracts, or SLAs between them. Each Super Validator is an independent power center with equal on-chain rights.

Super Validators provide no SLA, cannot be held legally accountable for misbehavior, and do not operate under regulatory supervision. They run only the Canton Coin tokenomics app, the Canton Coin Scan app, a name registry, and the Global Synchronizer governance app—none of which are subject to regulation. This is a stronger form of decentralization than Proof of Stake, where validators are economically aligned but can be pressured through their staked capital.

At the network level, Canton does offer censorship resistance. Transactions cannot be blocked by synchronizer operators on the Global Synchronizer, because all ordering and commit operations require BFT consensus. Individual application providers may choose to block transactions within their applications, but this is a feature of those applications, not of the network or the protocol. This is how Canton can be both permissionless and regulatory-compliant simultaneously: the network is open, while applications built on it can enforce whatever compliance requirements their use case demands.

---

## Enterprise suitability

**What enterprises actually need**

Regulated financial institutions face requirements the EVM was not designed to satisfy:

_KYC/AML compliance_ — counterparty identity must be verified before transacting. The EVM's pseudonymous address model does not natively support this; it must be layered on through identity registries ([ENS](https://ens.domains), ERC-725) or off-chain attestation (Verifiable Credentials).

_Regulatory auditability_ — regulators may need to see transaction details that counterparties do not. Canton's divulgence mechanism handles this natively. On EVM chains, everything is already public—but this creates data privacy problems under GDPR and similar frameworks for private data.

_Settlement finality_ — [Ethereum](/ethereum) provides probabilistic finality (effectively final after ~64 blocks, roughly 13 minutes), though Casper FFG now provides one-slot finality under certain conditions. Most institutional applications require deterministic finality for settlement accounting. Canton's synchronizer provides deterministic finality upon ordering.

_Reversibility and legal override_ — Daml's design allows authorized parties (regulators, courts) to archive contracts and create replacement contracts reflecting a corrected state. This is incompatible with EVM's "code is law" philosophy but essential for environments where courts can order asset freezes or trade corrections.

_Operational recovery_ — if a Canton participant's node goes offline, only that participant's ability to transact is affected. Other participants continue operating. If an EVM L2 sequencer goes offline, the entire L2 halts—as [Arbitrum](https://arbitrum.io)'s sequencer outage in 2023 demonstrated.

Canton addresses all of these requirements by design. EVM chains address some through workarounds, and fail structurally on others.

**Where the EVM enterprise story works**

The EVM ecosystem is not irrelevant for enterprise. For _public settlement layers_—tokenized assets that need to be traded on open markets, cross-institution liquidity pools, or public reference prices—Ethereum's transparency is the point. An institutional tokenized money market fund issued on Ethereum can be inspected by any market participant, facilitating price discovery and enabling composability with DeFi protocols. BlackRock's [BUIDL fund](https://www.blackrock.com/us/individual/products/397800/ishares-blackrock-usd-institutional-digital-liquidity-fund), tokenized on Ethereum, illustrates this: transparency builds market confidence.

[Enterprise Ethereum Alliance](https://entethalliance.org) members and frameworks like [Quorum](https://consensys.io/quorum) (a permissioned Ethereum fork) attempt to bridge the gap by adding privacy layers (Tessera private transactions, Orion) to EVM chains, but these solutions are technically complex, reduce composability, and still expose transaction graph metadata.

---

## DeFi suitability

**EVM DeFi: the benchmark**

DeFi, as it exists, is an EVM phenomenon. The combination of permissionless access, global state atomicity, composability, and token standards ([ERC-20](https://eips.ethereum.org/EIPS/eip-20), [ERC-721](https://eips.ethereum.org/EIPS/eip-721), [ERC-4626](https://eips.ethereum.org/EIPS/eip-4626)) has produced a self-reinforcing ecosystem with over \$100 billion in TVL at its peak. [Automated market makers](/exchanges), lending protocols, yield aggregators, [perpetual futures](/perps), and structured products have been built and iterated at a pace no permissioned system can match.

The EVM's suitability for DeFi rests on several distinctive properties:

_Permissionless composability_ — any protocol can integrate with any other without coordination. Flash loans exist because anyone can atomically borrow, use, and repay within a single transaction.

_Transparent liquidity_ — AMM pools aggregate liquidity from anonymous market makers globally. Price discovery is continuous and transparent.

_Censorship resistance_ — protocols like [Uniswap](/uniswap-explained) cannot be shut down by a single legal entity, which is what makes them useful as neutral infrastructure.

Canton also supports DeFi—and increasingly does so in production. The network hosts atomic swaps, repo markets, and other financial primitives in Daml. Canton's DeFi differs from EVM DeFi in that liquidity is _private_ rather than transparent: participants and their positions are not visible to the entire network unless an application and its users choose to make information public. This is a different design point, not a limitation—for many financial participants, private liquidity is preferable to transparent liquidity. However, the EVM's deep existing liquidity pools, composability across arbitrary protocols, and transparent price discovery remain advantages that Canton's DeFi ecosystem has not yet matched in scale.

**Canton's financial market infrastructure angle**

Where Canton excels is in the _post-trade_ workflow that DeFi has so far ignored: settlement, custody, collateral management, margin calls, corporate actions, and fund administration. These are multi-party, multi-step workflows where privacy, legal identity, and regulatory oversight are prerequisites, not obstacles. [DTCC](https://www.dtcc.com)'s Project Whitney (exploring Daml for post-trade) and ASX's CHESS replacement both targeted this space.

A word on ASX: the project was ultimately shelved—not because Daml was technically inadequate, but because organizational change management at an entrenched infrastructure provider proved more difficult than the technology. Canton has advanced significantly since then, but the lesson about institutional adoption friction is worth keeping in mind.

---

## Comparative summary

| Dimension                   | Ethereum Mainnet                             | EVM L2s (Arbitrum, zkSync)                   | Canton Network                                          |
| --------------------------- | -------------------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| **Execution model**         | Global shared state, sequential              | Global shared state, sequential (within L2)  | Sub-ledger, contract-scoped parallelism                 |
| **Privacy**                 | Fully transparent                            | Fully transparent (within L2)                | Sub-transaction privacy by construction                 |
| **Smart contract language** | Solidity/Vyper → EVM bytecode                | Solidity/Vyper → EVM bytecode                | Daml → Canton protocol                                  |
| **Finality**                | ~12 min (probabilistic → near-deterministic) | Minutes (optimistic) / seconds (ZK)          | Deterministic, per-synchronizer                         |
| **Throughput**              | ~15–30 TPS                                   | ~1,000–10,000 TPS (theoretical)              | Thousands TPS per synchronizer, horizontally scalable   |
| **Decentralization**        | Permissionless, ~1M validators               | Semi-permissioned (sequencer centralization) | Permissionless network; app-level permissioning         |
| **Censorship resistance**   | High                                         | Medium                                       | High at network level; app-level controls optional      |
| **KYC/AML integration**     | External, fragile                            | External, fragile                            | App-level, optional per application                     |
| **Regulatory compliance**   | Requires workarounds                         | Requires workarounds                         | Core design goal                                        |
| **Composability**           | Global, permissionless                       | Within L2; bridges for cross-L2              | Within synchronizer (atomic); cross-synchronizer (two-phase commit) |
| **Legal enforceability**    | Code is law                                  | Code is law                                  | Daml can express legal agreements (app-level choice)    |
| **Developer ecosystem**     | Massive, mature                              | Large, growing                               | Smaller, institutional-focused                          |
| **Reversibility**           | Immutable by default                         | Immutable by default                         | Authorized reversal supported                           |
| **Ideal use case**          | DeFi, public tokenization, open markets      | DeFi with lower fees, gaming, consumer apps  | Private DeFi, post-trade settlement, regulated FMI      |
| **Trust model**             | Cryptoeconomic (anonymous validators)        | Operator + cryptoeconomic hybrid             | BFT consensus + cryptographic verification              |

---

## Where Canton wins

**1. Bilateral and multi-lateral financial contracts requiring confidentiality**

A credit default swap between two banks should not be visible to other market participants. In Canton, the economic terms are known only to the counterparties and any designated observer (e.g., a reporting repository). On any EVM chain, this is impossible without a ZK layer that does not yet exist at production scale for complex financial contracts.

**2. Regulatory compliance in jurisdictions with strict data privacy requirements**

GDPR Article 17 (right to erasure) is irreconcilable with Ethereum's immutable public ledger. A Canton deployment can design data flows such that personally identifiable information never touches a shared ledger—it lives on the participant's local node. The shared ledger holds only hashed references and cryptographic commitments.

**3. Post-trade workflows requiring deterministic finality and legal override**

Trade corrections, failed settlement remediation, corporate action processing, and regulatory seizure orders all require the ability to modify or reverse a record under defined legal authority. Daml supports this through the authorized archival and recreation of contracts. Smart contracts on EVM chains have no equivalent mechanism without privileged admin keys—which reintroduce centralization and are operationally fraught.

**4. Institutional collateral management**

Collateral moves between custodians, prime brokers, and CCPs throughout a trading day. These moves involve multiple legal entities, are subject to regulatory oversight, and require atomic execution (collateral should not be in transit with no owner for any period). Canton's atomic cross-synchronizer transaction capability, combined with its privacy model, maps cleanly to this workflow. [EVM bridges](/history-of-cross-chain-bridge-hacks)—the closest analogue—have lost hundreds of millions of dollars to security exploits and cannot provide the legal identity guarantees required.

**5. Enterprises requiring auditability without transparency**

A fund administrator may need to prove to regulators that all NAV calculations were performed correctly, without exposing investor allocations to competitors. Canton's divulgence mechanism allows a designated auditor node to inspect specific contract lineages without being a party to the ongoing relationship. On Ethereum, the auditor either sees everything (public chain) or nothing (encrypted private data).

---

## Where EVM chains win

**1. Open, permissionless markets**

Any application that benefits from _transparent_, global liquidity provision—[decentralized exchanges](/exchanges), lending pools, yield aggregators—where public price discovery and visible order books are the point, the EVM's transparent model is a natural fit. Canton supports permissionless participation at the network level, but its privacy-first design means liquidity is private by default. For applications where full transparency of all positions and trades is the desired property, EVM chains remain the dominant choice.

**2. Token issuance for public secondary markets**

A tokenized equity that needs to trade on a public DEX, be held in [MetaMask](https://metamask.io), and be listed on Coinbase must live on a public EVM chain. While Canton is permissionless at the network level, its privacy-first architecture does not connect natively to these transparent distribution channels. Institutional issuers who want both private primary market workflows (using Canton for issuance and settlement) and public secondary market access (using Ethereum for trading) must bridge between the two systems—adding complexity and risk.

**3. Developer velocity and ecosystem maturity**

Ethereum's [Solidity](https://soliditylang.org) developer pool numbers in the hundreds of thousands. The tooling—[Hardhat](https://hardhat.org), [Foundry](https://getfoundry.sh), [Tenderly](https://tenderly.co), [OpenZeppelin](https://openzeppelin.com)—is deep and battle-tested. [Daml](https://docs.canton.network) has a steeper learning curve, a smaller developer community, and fewer open-source libraries. For teams that need to ship quickly, iterate based on user feedback, and hire from a large talent pool, the EVM is the pragmatic choice. This is an underrated consideration: the productivity difference between having thousands of answered Stack Overflow questions versus having to read source code is real.

**4. Composability-dependent applications**

Flash loans, liquidation bots, MEV strategies, and complex multi-protocol yield strategies all depend on global state atomicity across arbitrary contracts. A [flash loan](/aave) that borrows from [Aave](/aave), arbitrages [Uniswap](/uniswap-explained), and repays within a single transaction is only possible because all three protocols share the same EVM state. Canton's synchronizer-partitioned model does not support this kind of arbitrary cross-contract composition without pre-coordination.

**5. Consumer applications and NFT markets**

Consumer-facing applications—NFT marketplaces, gaming, loyalty programs, social protocols—prioritize ease of onboarding, wallet compatibility, and network effects over privacy and regulatory compliance. The EVM's [MetaMask](https://metamask.io) ecosystem, [ENS](https://ens.domains), and [ERC-721](https://eips.ethereum.org/EIPS/eip-721) standards dominate here, and there is no meaningful case for deploying these applications on Canton.

---

## The convergence question

The interesting question for the next five years is whether these ecosystems converge or remain separate. There are signals in both directions.

Privacy on EVM is advancing faster than it was three years ago. [Aztec](https://aztec.network)'s Noir language, [Risc Zero](https://www.risczero.com)'s ZK co-processor, and [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) collectively push toward a model where private smart contracts are possible on EVM-compatible infrastructure. If ZK proofs become fast enough and the developer experience becomes tractable, the EVM's privacy gap could narrow substantially. At that point, the EVM ecosystem's network effects—tooling, liquidity, developer talent—become formidable competition for Canton in institutional use cases.

Conversely, Canton has already moved toward public permissionless participation. The [Canton Network](https://canton.network)'s Global Synchronizer operates with an open validator set and BFT consensus, allowing anonymous Validators to join. [Digital Asset](https://www.digitalasset.com) has announced interoperability frameworks with public chains, and both the Canton and [Splice](https://github.com/hyperledger-labs/splice) (governance and Canton Coin for the Global Synchronizer) codebases are publicly available. The vision of Canton as "privacy-preserving smart contracts on a permissionless network that can also interoperate with public chains" is already partially realized—not a future aspiration.

The most likely near-term outcome is complementarity rather than convergence: institutions use Canton for private multi-party workflows and settlement netting, while using Ethereum (or an L2) as a public reference and distribution layer for tokenized assets. The settlement leg is private; the issuance and secondary market leg is public. This mirrors how regulated markets already work—bilateral OTC derivatives settle privately; exchange-traded derivatives use public price feeds.

---

## Conclusion

Canton and EVM-compatible blockchains are not rivals in the same market. They are solutions to different problems that happen to use overlapping vocabulary. Calling both of them "blockchains" is a bit like calling both PostgreSQL and Apache Kafka "data stores": accurate but not very useful.

The EVM ecosystem's strengths—permissionless access, global composability, deep liquidity, ecosystem maturity—flow directly from its transparency and shared global state. You cannot have [Uniswap](/uniswap-explained) without every participant being able to see every trade. The EVM is the right answer for open, permissionless financial applications, and it will likely remain so even as its privacy tooling matures.

Canton's strengths—sub-transaction privacy, optional legal enforceability, application-level regulatory compliance, deterministic finality—also flow from its architectural choices: partitioned sub-ledgers, a permissionless network with privacy by default, and a trust model built on BFT consensus rather than cryptoeconomic incentives. These properties cannot be added to EVM as bolt-ons; they require the decisions Canton made from the start. Notably, Canton achieves this without sacrificing permissionless participation at the network level—a design that defies the traditional "permissioned vs. permissionless" dichotomy.

For engineers and architects making platform decisions: if your application benefits from transparent global state, open liquidity pools, and composability across arbitrary public protocols, build on EVM. If your application requires confidential multi-party workflows, privacy-preserving DeFi, or the ability to layer regulatory compliance at the application level while operating on a permissionless network, Canton is worth serious architectural consideration. The question is not which platform is better—it is which platform's assumptions match your application's requirements. Getting that analysis right before committing is worth considerably more than any feature comparison, including this one.
