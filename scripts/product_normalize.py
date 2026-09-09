import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))
import product_frontmatter as fm
from product_taxonomy import TAXONOMY, colpermalink

ROOT = Path(__file__).resolve().parent.parent
PRODUCT_ROOT = ROOT / "content" / "product"

RENAMES = {
    "lending": {"Borrow Cryptocurrency": "Borrow", "Lend Cryptocurrency": "Lend", "No KYC": "No KYC"},
    "exchanges": {"No KYC": "No KYC", "Aggregators": "Aggregator", "digital art": "NFT", "NFTs": "NFT"},
    "derivatives": {"Options": "Options", "Perpetual": "Perpetual", "Synthetic Assets": "Synthetics", "Synthetic": "Synthetics"},
    "stablecoins": {"Fiat-backed": "Fiat-backed", "Crypto-backed": "Crypto-backed", "Algorithmic": "Synthetic"},
    "staking": {"Liquid Staking Derivatives": "Liquid Staking", "Restaking": "Restaking"},
    "yield-aggregators": {"Yield Tokenization": "Yield Trading"},
    "analytics": {},
    "infrastructure": {"Oracles": "Oracles", "Cross-chain": "Bridges"},
    "assets-management-tools": {"smart-contract wallets": "Wallet", "Asset Management Platforms": "Portfolio"},
    "assets-tokenization": {},
    "insurance": {},
    "prediction_markets": {},
    "payments": {},
}

DEFAULTS = {
    "lending": "Lend, Borrow",
    "exchanges": "Spot",
    "derivatives": "Synthetics",
    "stablecoins": "Crypto-backed",
    "staking": "Validator",
    "yield-aggregators": "Vaults",
    "analytics": "Dashboards",
    "infrastructure": "Dev Tools",
    "assets-management-tools": "Wallet",
    "assets-tokenization": "Issuance Platform",
    "insurance": "Cover",
    "prediction_markets": "Crypto",
    "payments": "Streaming",
}

OVERRIDES = {
    "yield-aggregators/pooltogether.md": "Lottery",
    "yield-aggregators/pendle.md": "Yield Trading",
    "exchanges/hyperliquid.md": "Spot",
    "derivatives/hyperliquid.md": "Perpetual",
    "derivatives/aster.md": "Perpetual",
    "derivatives/dydx.md": "Perpetual",
    "derivatives/liquid.md": "Perpetual",
    "derivatives/aevo.md": "Perpetual, Options",
    "payments/moonpay.md": "On-ramp",
    "payments/ramp.md": "On-ramp",
    "payments/transak.md": "On-ramp",
    "payments/sablier.md": "Streaming",
    "payments/superfluid.md": "Streaming",
    "payments/request.md": "Invoicing",
    "payments/lightning-network.md": "Lightning",
    "assets-tokenization/ondo.md": "Treasuries",
    "assets-tokenization/openeden.md": "Treasuries",
    "assets-tokenization/backed.md": "Equities",
    "assets-tokenization/matrixdock.md": "Treasuries",
    "assets-tokenization/maple.md": "Private Credit",
    "assets-tokenization/centrifuge.md": "Private Credit",
    "assets-tokenization/securitize.md": "Issuance Platform",
    "assets-tokenization/polymath-network.md": "Issuance Platform",
    "assets-tokenization/templum.md": "Issuance Platform",
    "prediction_markets/polymarket.md": "Politics, Sports, Crypto",
    "lending/liquity.md": "Borrow, CDP",
    "lending/mai-finance.md": "Borrow, CDP",
    "lending/abracadabra.md": "Borrow, CDP",
    "lending/alchemix.md": "Borrow, CDP",
}

GOVERNANCE = {"aragon", "colony", "daohaus", "dxdao", "realms", "snapshot", "tally"}
IDENTITY = {"3box", "blockpass", "bloom", "brightid", "civic", "colendi", "degenscore", "hydro", "identity.com", "jolocom", "selfkey"}


def new_filter(directory, stem, old):
    key = f"{directory}/{stem}.md"
    if key in OVERRIDES:
        return OVERRIDES[key]
    if directory == "infrastructure" and stem in GOVERNANCE:
        return "Governance"
    if directory == "infrastructure" and stem in IDENTITY:
        return "Identity"
    if directory == "exchanges" and stem in {"blur", "foundation", "looksrare", "opensea", "rarible", "superrare", "tensor", "zora"}:
        return "NFT"
    kept = []
    for value in str(old or "").split(", "):
        mapped = RENAMES[directory].get(value)
        if mapped and mapped not in kept:
            kept.append(mapped)
    if "CDP" in str(old or "") and directory == "lending" and "CDP" not in kept:
        kept.append("CDP")
    return ", ".join(kept) if kept else DEFAULTS[directory]


def normalize(path):
    meta, body = fm.load(path)
    directory = path.parent.name
    meta["coltitle"] = TAXONOMY[directory]["coltitle"]
    meta["colpermalink"] = colpermalink(directory)
    meta["filter"] = new_filter(directory, path.stem, meta.get("filter"))
    description = str(meta.get("product-description", ""))
    meta["product-description"] = description.replace(" \u2014 ", ", ").replace("\u2014", ", ")
    if "product-type" in meta and "CDP" in str(meta["product-type"]) and "CDP" not in meta["filter"]:
        meta["filter"] += ", CDP"
    fm.dump(path, meta, body)


def main():
    for path in sorted(PRODUCT_ROOT.glob("*/*.md")):
        if path.name != "_index.md":
            normalize(path)


if __name__ == "__main__":
    main()
