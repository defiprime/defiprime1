TAXONOMY = {
    "stablecoins": {
        "listing": "stablecoins.md",
        "url": "/stablecoins.html",
        "title": "Stablecoins",
        "h1title": "Stablecoins",
        "coltitle": "Stablecoins",
        "filters": ["Fiat-backed", "Crypto-backed", "Synthetic", "Yield-bearing"],
    },
    "assets-tokenization": {
        "listing": "assets-tokenization.md",
        "url": "/assets-tokenization.html",
        "title": "Tokenization & RWA",
        "h1title": "Tokenization & Real-World Assets",
        "coltitle": "Tokenization & RWA",
        "filters": ["Treasuries", "Private Credit", "Equities", "Commodities", "Issuance Platform"],
    },
    "lending": {
        "listing": "decentralized-lending.md",
        "url": "/decentralized-lending.html",
        "title": "Lending & Borrowing",
        "h1title": "DeFi Lending",
        "coltitle": "Lending",
        "filters": ["Lend", "Borrow", "CDP", "Fixed Rate", "No KYC"],
    },
    "exchanges": {
        "listing": "exchanges.md",
        "url": "/exchanges.html",
        "title": "Decentralized Exchanges",
        "h1title": "Decentralized Exchanges",
        "coltitle": "Decentralized exchanges",
        "filters": ["Spot", "Aggregator", "Stable Swap", "NFT", "No KYC"],
    },
    "derivatives": {
        "listing": "derivatives.md",
        "url": "/derivatives.html",
        "title": "Perps & Derivatives",
        "h1title": "Perps & Derivatives",
        "coltitle": "Perps & Derivatives",
        "filters": ["Perpetual", "Options", "Synthetics", "Yield Trading"],
    },
    "yield-aggregators": {
        "listing": "yield-aggregators.md",
        "url": "/yield-aggregators.html",
        "title": "Yield & Vaults",
        "h1title": "Yield & Vaults",
        "coltitle": "Yield & Vaults",
        "filters": ["Vaults", "Curator", "Yield Trading", "Fixed Yield", "Lottery"],
    },
    "staking": {
        "listing": "staking.md",
        "url": "/staking.html",
        "title": "Staking & Restaking",
        "h1title": "Staking & Restaking",
        "coltitle": "Staking & Restaking",
        "filters": ["Liquid Staking", "Restaking", "Validator", "Bitcoin Staking"],
    },
    "prediction_markets": {
        "listing": "prediction-markets.md",
        "url": "/prediction-markets.html",
        "title": "Prediction Markets",
        "h1title": "Prediction Markets",
        "coltitle": "Prediction Markets",
        "filters": ["Sports", "Politics", "Crypto", "Aggregator"],
    },
    "payments": {
        "listing": "payments.md",
        "url": "/payments.html",
        "title": "Payments & Cards",
        "h1title": "Payments & Cards",
        "coltitle": "Payments & Cards",
        "filters": ["Cards", "On-ramp", "Streaming", "Invoicing", "Lightning"],
    },
    "assets-management-tools": {
        "listing": "assets-management-tools.md",
        "url": "/assets-management-tools.html",
        "title": "Wallets & Portfolio",
        "h1title": "Wallets & Portfolio",
        "coltitle": "Wallets & Portfolio",
        "filters": ["Wallet", "Portfolio", "Automation", "Multisig"],
    },
    "analytics": {
        "listing": "defi-analytics.md",
        "url": "/defi-analytics.html",
        "title": "Analytics",
        "h1title": "Analytics",
        "coltitle": "Analytics",
        "filters": ["Dashboards", "On-chain Data", "Portfolio", "Risk", "Research"],
    },
    "infrastructure": {
        "listing": "infrastructure.md",
        "url": "/infrastructure.html",
        "title": "Infrastructure & Dev Tooling",
        "h1title": "DeFi Infrastructure & Dev Tooling",
        "coltitle": "Infrastructure",
        "filters": ["Oracles", "Bridges", "RPC", "Indexing", "Governance", "Identity", "Dev Tools", "Account Abstraction"],
    },
    "insurance": {
        "listing": "insurance.md",
        "url": "/insurance.html",
        "title": "Risk & Insurance",
        "h1title": "Risk & Insurance",
        "coltitle": "Risk & Insurance",
        "filters": ["Cover", "Risk Curator", "Security Monitoring", "Bug Bounty", "Audit"],
    },
}

REMOVED_DIRS = {
    "perps": "derivatives",
    "alternative-savings": "yield-aggregators",
    "dao": "infrastructure",
    "kyc_identity": "infrastructure",
    "marketplaces": "exchanges",
}

REMOVED_LISTINGS = {
    "/perps": "/derivatives",
    "/alternative-savings": "/yield-aggregators",
    "/dao": "/infrastructure",
    "/decentralized_kyc_identity": "/infrastructure",
    "/decentralized_marketplaces": "/exchanges",
}

ECOSYSTEMS = {
    "ethereum", "bsc", "bitcoin", "tron", "stellar", "eos", "polygon", "solana",
    "arbitrum", "base", "optimism", "avalanche", "hyperliquid", "cosmos", "sui",
    "aptos", "ton", "gnosis", "linea", "scroll", "zksync", "mantle", "sonic",
    "berachain", "monad", "plasma", "tempo",
}

PRODUCT_TYPES = {"non-custodial", "cefi", "non-custodial, CDP"}

REQUIRED_KEYS = [
    "url", "git-date", "product-title", "product-url", "image", "ecosystem",
    "product-description", "coltitle", "colpermalink", "product-type", "filter",
]

KEY_ORDER = [
    "url", "git-date", "product-title", "product-url", "image", "ecosystem",
    "product-description", "coltitle", "colpermalink", "product-type", "filter",
    "rank", "twitter", "github", "analytics", "ticker", "contract", "decimals",
    "platform", "alternative-to", "featured", "build",
]

DESCRIPTION_MIN = 40
DESCRIPTION_MAX = 400


def colpermalink(directory):
    return TAXONOMY[directory]["url"].lstrip("/").removesuffix(".html")
