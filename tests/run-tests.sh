#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PUBLIC="$ROOT/public"
GOLDEN="${JEKYLL_GOLDEN:-/Users/sneg55/Documents/GitHub/defiprime-jekyll-golden/_site}"
PASS=0
FAIL=0
WARN=0

pass() { PASS=$((PASS + 1)); echo "  PASS: $1"; }
fail() { FAIL=$((FAIL + 1)); echo "  FAIL: $1"; }
warn() { WARN=$((WARN + 1)); echo "  WARN: $1"; }

echo "=== Building Hugo site ==="
cd "$ROOT"
hugo --minify --quiet
echo "Build complete."
echo ""

echo "--- Test 1: Build succeeds ---"
if [ -d "$PUBLIC" ]; then
  pass "Hugo build produced output directory"
else
  fail "No public/ directory found"
fi

PAGE_COUNT=$(find "$PUBLIC" -name "*.html" | wc -l | tr -d ' ')
echo "  Total HTML files: $PAGE_COUNT"
if [ "$PAGE_COUNT" -gt 600 ]; then
  pass "Page count > 600 ($PAGE_COUNT pages)"
else
  fail "Page count too low: $PAGE_COUNT (expected > 600)"
fi

echo ""
echo "--- Test 2: Parity harness ---"
if [ -d "$GOLDEN" ]; then
  if python3 "$ROOT/tests/parity.py" --golden "$GOLDEN" --public "$PUBLIC"; then
    pass "Parity harness: no unsuppressed findings"
  else
    fail "Parity harness: unsuppressed findings against golden build"
  fi
else
  warn "Golden build not found at $GOLDEN, skipping parity harness"
fi

echo ""
echo "--- Test 3: Key Pages Exist ---"

if [ -f "$PUBLIC/index.html" ]; then pass "Homepage exists"; else fail "Homepage missing"; fi

if [ -f "$PUBLIC/blog/index.html" ]; then pass "Blog listing exists"; else fail "Blog listing missing"; fi

if [ -f "$PUBLIC/blog/2/index.html" ]; then pass "Blog pagination page 2 exists"; else fail "Blog pagination page 2 missing"; fi

if [ -f "$PUBLIC/aave-mess-decentralized-governance/index.html" ]; then pass "Blog post exists"; else fail "Blog post missing"; fi

if [ -f "$PUBLIC/product/aave.html" ]; then
  pass "Product page exists (Aave)"
else
  fail "Product page missing (Aave)"
fi

if [ -f "$PUBLIC/t/lending.html" ]; then
  pass "Tag page exists (lending)"
else
  fail "Tag page missing (lending)"
fi

for eco in ethereum bitcoin solana polygon; do
  if [ -f "$PUBLIC/$eco/index.html" ]; then pass "Ecosystem: /$eco"; else fail "Ecosystem missing: /$eco"; fi
done

for page in about events; do
  if [ -f "$PUBLIC/$page/index.html" ]; then pass "Page: /$page"; else fail "Page missing: /$page"; fi
done

if [ -f "$PUBLIC/404.html" ]; then pass "404 page exists"; else fail "404 page missing"; fi

if [ -f "$PUBLIC/feed.xml" ]; then pass "RSS feed exists"; else fail "RSS feed missing"; fi

if [ -f "$PUBLIC/sitemap.xml" ]; then pass "Sitemap exists"; else fail "Sitemap missing"; fi

echo ""
echo "--- Test 4: HTML Content Checks ---"

BLOG_FILE="$PUBLIC/aave-mess-decentralized-governance/index.html"
if [ -f "$BLOG_FILE" ]; then
  if grep -q 'BlogPosting' "$BLOG_FILE"; then pass "Blog JSON-LD schema present"; else fail "Blog JSON-LD schema missing"; fi
  if grep -q 'og:title' "$BLOG_FILE"; then pass "Blog OG meta tags present"; else fail "Blog OG meta tags missing"; fi
  if grep -q 'class="tag"' "$BLOG_FILE"; then pass "Blog tag links present"; else fail "Blog tag links missing"; fi
fi

HOME_FILE="$PUBLIC/index.html"
if [ -f "$HOME_FILE" ]; then
  if grep -q 'Organization' "$HOME_FILE"; then pass "Homepage Organization schema present"; else fail "Homepage Organization schema missing"; fi
  if grep -q 'og:title' "$HOME_FILE"; then pass "Homepage OG meta present"; else fail "Homepage OG meta missing"; fi
fi

PRODUCT_FILES=$(find "$PUBLIC/product" -name "index.html" 2>/dev/null | head -3)
if [ -n "$PRODUCT_FILES" ]; then
  FIRST_PRODUCT=$(echo "$PRODUCT_FILES" | head -1)
  if grep -q 'BreadcrumbList' "$FIRST_PRODUCT"; then pass "Product BreadcrumbList schema"; else warn "Product BreadcrumbList schema missing"; fi
  if grep -q '"@type": "Product"' "$FIRST_PRODUCT" || grep -q '"@type":"Product"' "$FIRST_PRODUCT"; then pass "Product schema present"; else warn "Product schema missing"; fi
fi

echo ""
echo "--- Test 5: Internal Link Spot Check ---"
if [ -f "$HOME_FILE" ]; then
  for link in blog about events; do
    if [ -d "$PUBLIC/$link" ] || [ -f "$PUBLIC/$link/index.html" ]; then
      pass "Internal link /$link resolves"
    else
      fail "Internal link /$link broken"
    fi
  done
fi

echo ""
echo "--- Test 6: Redirects (Aliases) ---"
for redirect in product decentralized_lending analytics custodian_services; do
  if [ -f "$PUBLIC/$redirect/index.html" ] && grep -q 'refresh' "$PUBLIC/$redirect/index.html" 2>/dev/null; then
    pass "Redirect /$redirect exists"
  elif [ -f "$PUBLIC/$redirect/index.html" ]; then
    warn "/$redirect exists but may not be a redirect"
  else
    warn "Redirect /$redirect not found"
  fi
done

echo ""
echo "============================================="
echo "  TEST RESULTS"
echo "============================================="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo "  WARN: $WARN"
echo "============================================="

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
