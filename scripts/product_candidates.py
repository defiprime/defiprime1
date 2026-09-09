import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))
import product_frontmatter as fm
from product_taxonomy import TAXONOMY

ROOT = Path(__file__).resolve().parent.parent
PRODUCT_ROOT = ROOT / "content" / "product"
USER_AGENT = "Mozilla/5.0 (Macintosh) defiprime-directory-check/1.0"
PROTOCOLS_URL = "https://api.llama.fi/protocols"
DEXS_URL = "https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true"
OPTIONS_URL = "https://api.llama.fi/overview/options?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true"
STABLES_URL = "https://stablecoins.llama.fi/stablecoins?includePrices=false"
TVL_FLOOR = 1_000_000
LIMIT = 25
SKIP_CATEGORIES = {"CEX", "Launchpad", "Chain"}

TVL_CATEGORIES = {
    "lending": {"Lending", "CDP", "RWA Lending"},
    "yield-aggregators": {"Yield", "Yield Aggregator", "Onchain Capital Allocator", "Basis Trading"},
    "staking": {"Liquid Staking", "Liquid Restaking", "Restaking", "Staking Pool"},
    "assets-tokenization": {"RWA"},
    "insurance": {"Insurance", "Risk Curators"},
    "prediction_markets": {"Prediction Market"},
}

SUFFIXES = re.compile(r"\s+(V\d+|v\d+|Lite|Classic|Legacy)$")
OVERVIEW_SUFFIXES = re.compile(r"(\s+(AMM|Spot Orderbook|Options|Slipstream|Infinity|DLMM|CLOB|DEX|[Vv]\d+))+$")
STOPWORDS = ("finance", "protocol", "dao", "network", "labs")


def money(text):
    text = text.strip().lstrip("$").lower()
    scale = {"k": 1e3, "m": 1e6, "b": 1e9, "t": 1e12}
    if text and text[-1] in scale:
        return float(text[:-1]) * scale[text[-1]]
    return float(text)


def host(url):
    name = urlparse(url).hostname or ""
    parts = name.split(".")
    if parts and parts[0] in {"www", "app"}:
        parts = parts[1:]
    return ".".join(parts)


def fetch_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def parent_name(protocol):
    parent = protocol.get("parentProtocol")
    if parent:
        return parent.split("#", 1)[1].replace("-", " ").title()
    return SUFFIXES.sub("", protocol["name"])


def rank_protocols(protocols, categories, limit=LIMIT):
    groups = {}
    for protocol in protocols:
        if protocol.get("category") not in categories or protocol.get("category") in SKIP_CATEGORIES:
            continue
        key = protocol.get("parentProtocol") or protocol["slug"]
        group = groups.setdefault(key, {"name": parent_name(protocol), "slug": protocol["slug"], "url": protocol.get("url"), "twitter": protocol.get("twitter"), "metric": 0.0, "metric_name": "tvl", "source": f"{PROTOCOLS_URL} {date.today()}", "chains": [], "category": protocol.get("category"), "best": 0.0})
        tvl = float(protocol.get("tvl") or 0)
        group["metric"] += tvl
        if tvl > group["best"]:
            group.update(slug=protocol["slug"], url=protocol.get("url"), twitter=protocol.get("twitter"), best=tvl, category=protocol.get("category"))
        for chain in protocol.get("chains") or []:
            if chain not in group["chains"]:
                group["chains"].append(chain)
    rows = sorted(groups.values(), key=lambda g: -g["metric"])
    for row in rows:
        row.pop("best", None)
    return [row for row in rows if row["metric"] >= TVL_FLOOR][:limit]


def overview_base_name(name):
    previous = None
    while previous != name:
        previous = name
        name = OVERVIEW_SUFFIXES.sub("", name).strip()
    return name


def rank_overview(payload, source, limit=LIMIT):
    groups = {}
    for protocol in payload.get("protocols", []):
        name = protocol.get("displayName") or protocol["name"]
        base = overview_base_name(name)
        metric = float(protocol.get("total30d") or 0)
        group = groups.setdefault(base, {"name": base, "slug": protocol.get("module") or protocol["name"], "url": None, "twitter": None, "metric": 0.0, "metric_name": "volume30d", "source": f"{source} {date.today()}", "chains": protocol.get("chains") or [], "category": protocol.get("category"), "best": 0.0})
        group["metric"] += metric
        if metric > group["best"]:
            group.update(slug=protocol.get("module") or protocol["name"], chains=protocol.get("chains") or [], category=protocol.get("category"), best=metric)
    rows = sorted(groups.values(), key=lambda g: -g["metric"])
    for row in rows:
        row.pop("best", None)
    return rows[:limit]


def rank_stablecoins(payload, limit=LIMIT):
    rows = []
    for asset in payload.get("peggedAssets", []):
        if asset.get("pegType") != "peggedUSD":
            continue
        rows.append({"name": f"{asset['name']} ({asset['symbol']})", "slug": asset.get("gecko_id") or asset["symbol"].lower(), "url": None, "twitter": None, "metric": float((asset.get("circulating") or {}).get("peggedUSD") or 0), "metric_name": "circulating", "source": f"{STABLES_URL} {date.today()}", "chains": asset.get("chains") or [], "category": asset.get("pegMechanism")})
    return sorted(rows, key=lambda r: -r["metric"])[:limit]


def parse_perps_snapshot(text):
    rows = []
    for line in text.splitlines():
        parts = line.split()
        if len(parts) < 3 or ":" in parts[0]:
            continue
        tail = [p for p in parts if re.fullmatch(r"\$?[\d.]+[kmbt]?|-", p)]
        if not tail:
            continue
        name = " ".join(parts[: len(parts) - len(tail)])
        rows.append({"name": name, "slug": name.lower().replace(" ", "-"), "url": None, "twitter": None, "metric": money(tail[-1]), "metric_name": "volume30d", "source": f"https://defillama.com/perps {date.today()}", "chains": [], "category": "Derivatives"})
    return sorted(rows, key=lambda r: -r["metric"])


def http_status(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code
    except (urllib.error.URLError, TimeoutError, ValueError, OSError):
        return None


def normalize_name(name):
    name = name.lower()
    name = re.sub(r"\s*\([^)]*\)\s*$", "", name)
    for word in STOPWORDS:
        name = re.sub(rf"\b{word}\b", " ", name)
    return re.sub(r"[^a-z0-9]", "", name)


def candidate_symbol(name):
    match = re.search(r"\(([^()]+)\)\s*$", name)
    return match.group(1) if match else None


def is_listed(candidate, existing_hosts, existing_keys, existing_symbols):
    if candidate.get("url") and host(candidate["url"]) in existing_hosts:
        return True
    if normalize_name(candidate["name"]) in existing_keys:
        return True
    symbol = candidate_symbol(candidate["name"])
    if symbol and symbol.lower() in existing_symbols:
        return True
    return False


def llama_index(protocols):
    by_host = {}
    by_name = {}
    for protocol in protocols:
        tvl = float(protocol.get("tvl") or 0)
        if protocol.get("url"):
            by_host[host(protocol["url"])] = max(by_host.get(host(protocol["url"]), 0), tvl)
        by_name[parent_name(protocol).lower()] = max(by_name.get(parent_name(protocol).lower(), 0), tvl)
    return by_host, by_name


def check_existing(protocols, stable_names):
    by_host, by_name = llama_index(protocols)
    report = {}
    for path in sorted(PRODUCT_ROOT.glob("*/*.md")):
        if path.name == "_index.md":
            continue
        meta, _ = fm.load(path)
        title = str(meta["product-title"])
        product_host = host(str(meta["product-url"]))
        status = http_status(str(meta["product-url"]))
        tvl = by_host.get(product_host) or by_name.get(title.lower())
        is_stable = title.lower() in stable_names
        featured = bool(meta.get("featured"))
        keep = True if (status == 200 or (tvl and tvl >= TVL_FLOOR) or is_stable or featured) else None
        row = {
            "file": str(path.relative_to(ROOT)),
            "title": title,
            "host": product_host,
            "http": status,
            "llama_tvl": tvl,
            "tvl_source": f"{PROTOCOLS_URL} {date.today()}" if tvl else None,
            "stablecoin": is_stable,
            "stablecoin_source": f"{STABLES_URL} {date.today()}" if is_stable else None,
            "ticker": meta.get("ticker"),
            "keep": keep,
        }
        if featured:
            row["featured"] = True
        report.setdefault(path.parent.name, []).append(row)
    return report


def write_report(path, data):
    lines = [
        f"# Product candidates, {date.today()}",
        "",
        "Metric sources are named per row. `keep: null` means site and DefiLlama checks both failed and the X account check decides. `stablecoin` means the title matched the DefiLlama stablecoin list by name.",
        "",
    ]
    for directory in TAXONOMY:
        block = data.get(directory, {})
        lines.append(f"## {TAXONOMY[directory]['title']} ({directory})")
        lines.append("")
        lines.append("### Existing")
        for row in block.get("existing", []):
            if row.get("featured"):
                flag = "keep (featured)"
            elif row["keep"]:
                flag = "keep"
            else:
                flag = "CHECK X"
            lines.append(f"- {flag}: {row['title']} ({row['file']}) http={row['http']} tvl={row['llama_tvl']} tvl_source={row['tvl_source']} stablecoin_source={row['stablecoin_source']}")
        lines.append("")
        lines.append("### Candidates not yet listed")
        existing_hosts = {r["host"] for r in block.get("existing", [])}
        existing_keys = {normalize_name(r["title"]) for r in block.get("existing", [])}
        existing_symbols = {r["title"].lower() for r in block.get("existing", [])}
        existing_symbols |= {r["ticker"].lower() for r in block.get("existing", []) if r.get("ticker")}
        for row in block.get("candidates", []):
            if not is_listed(row, existing_hosts, existing_keys, existing_symbols):
                lines.append(f"- {row['name']}: {row['metric_name']}={row['metric']:,.0f} chains={', '.join(row['chains'][:4])} source={row['source']}")
        lines.append("")
    Path(path).write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--perps-snapshot", required=True)
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--report-out", required=True)
    args = parser.parse_args()
    protocols = fetch_json(PROTOCOLS_URL)
    stables = fetch_json(STABLES_URL)
    stable_names = {a["name"].lower() for a in stables.get("peggedAssets", [])}
    existing = check_existing(protocols, stable_names)
    data = {directory: {"existing": existing.get(directory, []), "candidates": []} for directory in TAXONOMY}
    for directory, categories in TVL_CATEGORIES.items():
        data[directory]["candidates"] = rank_protocols(protocols, categories)
    data["exchanges"]["candidates"] = rank_overview(fetch_json(DEXS_URL), DEXS_URL) + rank_protocols(protocols, {"DEX Aggregator"}, limit=8)
    data["derivatives"]["candidates"] = parse_perps_snapshot(Path(args.perps_snapshot).read_text())[:LIMIT] + rank_overview(fetch_json(OPTIONS_URL), OPTIONS_URL, limit=8)
    data["stablecoins"]["candidates"] = rank_stablecoins(stables)
    Path(args.json_out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.json_out).write_text(json.dumps(data, indent=2))
    write_report(args.report_out, data)
    print(f"wrote {args.json_out} and {args.report_out}")


if __name__ == "__main__":
    main()
