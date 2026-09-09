import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import product_candidates as pc


class ParseTest(unittest.TestCase):
    def test_money_to_float(self):
        self.assertEqual(pc.money("216.821b"), 216.821e9)
        self.assertEqual(pc.money("680.54m"), 680.54e6)
        self.assertEqual(pc.money("$1.5k"), 1500.0)

    def test_perps_snapshot(self):
        text = "source: page\nHyperliquid 8.079b 8.079b 14.669b 45.343b 216.821b\nVest Markets - 81.63m 93.36m 416.73m 2.955b\n"
        rows = pc.parse_perps_snapshot(text)
        self.assertEqual(rows[0]["name"], "Hyperliquid")
        self.assertEqual(rows[0]["metric"], 216.821e9)
        self.assertEqual(rows[1]["name"], "Vest Markets")
        self.assertEqual(rows[1]["metric"], 2.955e9)

    def test_collapse_children_keeps_parent_once(self):
        protocols = [
            {"name": "Aave V3", "slug": "aave-v3", "tvl": 30e9, "category": "Lending", "parentProtocol": "parent#aave", "url": "https://aave.com", "twitter": "aave", "chains": ["Ethereum"]},
            {"name": "Aave V2", "slug": "aave-v2", "tvl": 1e9, "category": "Lending", "parentProtocol": "parent#aave", "url": "https://aave.com", "twitter": "aave", "chains": ["Ethereum"]},
            {"name": "Morpho", "slug": "morpho", "tvl": 8e9, "category": "Lending", "url": "https://morpho.org", "twitter": "MorphoLabs", "chains": ["Ethereum", "Base"]},
        ]
        rows = pc.rank_protocols(protocols, {"Lending"}, limit=10)
        self.assertEqual([r["name"] for r in rows], ["Aave", "Morpho"])
        self.assertEqual(rows[0]["metric"], 31e9)

    def test_host(self):
        self.assertEqual(pc.host("https://app.aave.com/?referral=28"), "aave.com")
        self.assertEqual(pc.host("https://www.morpho.org"), "morpho.org")

    def test_rank_overview_collapses_versions(self):
        payload = {
            "protocols": [
                {"displayName": "Uniswap V3", "module": "uniswap-v3", "total30d": 10.0, "category": "Dexs", "chains": ["Ethereum"]},
                {"displayName": "Uniswap V4", "module": "uniswap-v4", "total30d": 5.0, "category": "Dexs", "chains": ["Ethereum"]},
                {"displayName": "Curve DEX", "module": "curve", "total30d": 3.0, "category": "Dexs", "chains": ["Ethereum"]},
            ]
        }
        rows = pc.rank_overview(payload, "source")
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["name"], "Uniswap")
        self.assertEqual(rows[0]["metric"], 15.0)

    def test_is_listed_matches_decorated_stablecoin_name(self):
        existing = [{"title": "Dai", "host": "makerdao.com", "ticker": None}]
        existing_hosts = {r["host"] for r in existing}
        existing_keys = {pc.normalize_name(r["title"]) for r in existing}
        existing_symbols = {r["title"].lower() for r in existing}
        candidate = {"name": "Dai (DAI)", "url": None}
        self.assertTrue(pc.is_listed(candidate, existing_hosts, existing_keys, existing_symbols))


if __name__ == "__main__":
    unittest.main()
