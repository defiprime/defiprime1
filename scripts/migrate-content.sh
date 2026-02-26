#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONTENT="$ROOT/content"

echo "=== Jekyll to Hugo Content Migration ==="
echo "Root: $ROOT"
echo ""

# 1. Blog Posts
echo "--- Migrating blog posts ---"
mkdir -p "$CONTENT/blog"
POST_COUNT=0
PRODUCT_POST_COUNT=0

for f in "$ROOT/collections/_posts/"*.md; do
  [ -f "$f" ] || continue
  filename=$(basename "$f")
  if grep -q 'category: products' "$f"; then
    PRODUCT_POST_COUNT=$((PRODUCT_POST_COUNT + 1))
    permalink=$(grep '^permalink:' "$f" | head -1 | sed 's/^permalink: *//' | tr -d '"' | tr -d "'" | tr -d ' ')
    if [ -n "$permalink" ]; then
      target="$CONTENT/${permalink}.md"
      mkdir -p "$(dirname "$target")"
      cp "$f" "$target"
    fi
  else
    POST_COUNT=$((POST_COUNT + 1))
    target="$CONTENT/blog/$filename"
    sed 's/^layout: \[blog\]/layout: blog/' "$f" > "$target"
    if grep -q 'redirect_from:' "$target"; then
      sed -i '' 's/^redirect_from:/aliases:/' "$target"
    fi
  fi
done

echo "  Blog posts migrated: $POST_COUNT"
echo "  Product listing posts migrated: $PRODUCT_POST_COUNT"

# 2. Product Collections
echo "--- Migrating product collections ---"
PRODUCT_COUNT=0

for col in lending derivatives analytics assets-management-tools exchanges infrastructure insurance assets-tokenization kyc_identity marketplaces prediction_markets stablecoins perps payments staking dao alternative-savings yield-aggregators; do
  src="$ROOT/collections/_${col}"
  dst="$CONTENT/product/${col}"
  if [ -d "$src" ]; then
    mkdir -p "$dst"
    for f in "$src/"*.md; do
      [ -f "$f" ] || continue
      filename=$(basename "$f")
      lower_filename=$(echo "$filename" | tr '[:upper:]' '[:lower:]')
      cp "$f" "$dst/$lower_filename"
      PRODUCT_COUNT=$((PRODUCT_COUNT + 1))
    done
  fi
done

echo "  Product items migrated: $PRODUCT_COUNT"

# 3. Airdrops
echo "--- Migrating airdrops ---"
AIRDROP_COUNT=0
src="$ROOT/collections/_airdrops"
dst="$CONTENT/airdrop"
mkdir -p "$dst"
if [ -d "$src" ]; then
  for f in "$src/"*.md; do
    [ -f "$f" ] || continue
    cp "$f" "$dst/$(basename "$f")"
    AIRDROP_COUNT=$((AIRDROP_COUNT + 1))
  done
fi
echo "  Airdrops migrated: $AIRDROP_COUNT"

# 4. Alternatives
echo "--- Migrating alternatives ---"
ALT_COUNT=0
src="$ROOT/collections/_alternatives"
dst="$CONTENT/alternatives"
mkdir -p "$dst"
if [ -d "$src" ]; then
  for f in "$src/"*.md; do
    [ -f "$f" ] || continue
    cp "$f" "$dst/$(basename "$f")"
    ALT_COUNT=$((ALT_COUNT + 1))
  done
fi
echo "  Alternatives migrated: $ALT_COUNT"

# 5. Events
echo "--- Migrating events ---"
EVENT_COUNT=0
src="$ROOT/collections/_events"
dst="$CONTENT/events"
mkdir -p "$dst"
if [ -d "$src" ]; then
  for f in "$src/"*.md; do
    [ -f "$f" ] || continue
    cp "$f" "$dst/$(basename "$f")"
    EVENT_COUNT=$((EVENT_COUNT + 1))
  done
fi
echo "  Events migrated: $EVENT_COUNT"

# 6. Top-level pages
echo "--- Migrating top-level pages ---"
PAGE_COUNT=0

for f in ethereum.md bitcoin.md solana.md polygon.md avalanche.md base.md bsc.md optimism.md arbitrum.md canto.md cosmos.md eos.md placeholder.md about.md alternatives.md crypto-airdrops.md solana-airdrops.md defi-events.md dex-volume.md gas-price.md sitemap-html.md tokenlist.md media-assets.md 404.md; do
  if [ -f "$ROOT/$f" ]; then
    cp "$ROOT/$f" "$CONTENT/$f"
    PAGE_COUNT=$((PAGE_COUNT + 1))
  fi
done

# Blog index
if [ -f "$ROOT/blog.md" ]; then
  cp "$ROOT/blog.md" "$CONTENT/blog/_index.md"
  PAGE_COUNT=$((PAGE_COUNT + 1))
fi

# Homepage
if [ -f "$ROOT/index.md" ]; then
  cp "$ROOT/index.md" "$CONTENT/_index.md"
  PAGE_COUNT=$((PAGE_COUNT + 1))
fi

echo "  Top-level pages migrated: $PAGE_COUNT"

# Summary
echo ""
echo "=== Migration Complete ==="
echo "  Blog posts:     $POST_COUNT"
echo "  Listing pages:  $PRODUCT_POST_COUNT"
echo "  Products:       $PRODUCT_COUNT"
echo "  Airdrops:       $AIRDROP_COUNT"
echo "  Alternatives:   $ALT_COUNT"
echo "  Events:         $EVENT_COUNT"
echo "  Pages:          $PAGE_COUNT"
TOTAL=$((POST_COUNT + PRODUCT_POST_COUNT + PRODUCT_COUNT + AIRDROP_COUNT + ALT_COUNT + EVENT_COUNT + PAGE_COUNT))
echo "  TOTAL:          $TOTAL"
