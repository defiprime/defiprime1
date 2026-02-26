#!/usr/bin/env bash
# Hugo Migration Test Suite for DeFiPrime
# Tests URL parity, front matter preservation, HTML output, and build correctness
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PUBLIC="$ROOT/public"
FIXTURES="$ROOT/tests/fixtures"
PASS=0
FAIL=0
WARN=0

pass() { PASS=$((PASS + 1)); echo "  PASS: $1"; }
fail() { FAIL=$((FAIL + 1)); echo "  FAIL: $1"; }
warn() { WARN=$((WARN + 1)); echo "  WARN: $1"; }

# Build first
echo "=== Building Hugo site ==="
cd "$ROOT"
hugo --quiet 2>/dev/null
echo "Build complete."
echo ""

# -------------------------------------------------------
# TEST 1: Build succeeds
# -------------------------------------------------------
echo "--- Test 1: Build succeeds ---"
if [ -d "$PUBLIC" ]; then
  pass "Hugo build produced output directory"
else
  fail "No public/ directory found"
fi

# Count pages
PAGE_COUNT=$(find "$PUBLIC" -name "*.html" | wc -l | tr -d ' ')
echo "  Total HTML files: $PAGE_COUNT"
if [ "$PAGE_COUNT" -gt 600 ]; then
  pass "Page count > 600 ($PAGE_COUNT pages)"
else
  fail "Page count too low: $PAGE_COUNT (expected > 600)"
fi

# -------------------------------------------------------
# TEST 2: URL Inventory Parity
# -------------------------------------------------------
echo ""
echo "--- Test 2: URL Inventory Parity ---"
if [ -f "$FIXTURES/url-inventory.txt" ]; then
  TOTAL_URLS=0
  FOUND_URLS=0
  MISSING_URLS=0

  while IFS= read -r url; do
    # Skip comments and empty lines
    case "$url" in \#*|"") continue ;; esac
    TOTAL_URLS=$((TOTAL_URLS + 1))

    # Check if the URL exists in Hugo output
    # Hugo generates clean URLs: /path → public/path/index.html
    # Or: /path.html → public/path.html
    url_clean=$(echo "$url" | sed 's:^/*::' | sed 's:/*$::')

    if [ -z "$url_clean" ]; then
      # Root URL
      if [ -f "$PUBLIC/index.html" ]; then
        FOUND_URLS=$((FOUND_URLS + 1))
      else
        MISSING_URLS=$((MISSING_URLS + 1))
      fi
    elif echo "$url_clean" | grep -q '\.html$\|\.xml$'; then
      # File with extension — check both exact file and clean URL directory
      url_no_ext=$(echo "$url_clean" | sed 's/\.html$//')
      if [ -f "$PUBLIC/$url_clean" ] || [ -f "$PUBLIC/$url_no_ext/index.html" ]; then
        FOUND_URLS=$((FOUND_URLS + 1))
      else
        MISSING_URLS=$((MISSING_URLS + 1))
        if [ "$MISSING_URLS" -le 20 ]; then
          echo "    MISSING: /$url_clean"
        fi
      fi
    else
      # Clean URL — check both /path/index.html and /path.html
      if [ -f "$PUBLIC/$url_clean/index.html" ] || [ -f "$PUBLIC/$url_clean.html" ] || [ -f "$PUBLIC/${url_clean}/index.html" ]; then
        FOUND_URLS=$((FOUND_URLS + 1))
      else
        MISSING_URLS=$((MISSING_URLS + 1))
        if [ "$MISSING_URLS" -le 20 ]; then
          echo "    MISSING: /$url_clean"
        fi
      fi
    fi
  done < "$FIXTURES/url-inventory.txt"

  echo "  URLs checked: $TOTAL_URLS"
  echo "  Found: $FOUND_URLS"
  echo "  Missing: $MISSING_URLS"

  PARITY_PCT=$((FOUND_URLS * 100 / TOTAL_URLS))
  if [ "$PARITY_PCT" -ge 95 ]; then
    pass "URL parity: ${PARITY_PCT}% ($FOUND_URLS/$TOTAL_URLS)"
  elif [ "$PARITY_PCT" -ge 80 ]; then
    warn "URL parity: ${PARITY_PCT}% ($FOUND_URLS/$TOTAL_URLS) — some URLs missing"
  else
    fail "URL parity: ${PARITY_PCT}% ($FOUND_URLS/$TOTAL_URLS) — too many missing"
  fi
else
  warn "No url-inventory.txt fixture found, skipping URL parity test"
fi

# -------------------------------------------------------
# TEST 3: Key pages exist
# -------------------------------------------------------
echo ""
echo "--- Test 3: Key Pages Exist ---"

# Homepage
if [ -f "$PUBLIC/index.html" ]; then pass "Homepage exists"; else fail "Homepage missing"; fi

# Blog listing
if [ -f "$PUBLIC/blog/index.html" ]; then pass "Blog listing exists"; else fail "Blog listing missing"; fi

# Blog pagination
if [ -f "$PUBLIC/blog/2/index.html" ]; then pass "Blog page 2 exists"; else fail "Blog page 2 missing"; fi

# Sample blog post (most recent)
if [ -f "$PUBLIC/aave-mess-decentralized-governance/index.html" ]; then pass "Blog post exists"; else fail "Blog post missing"; fi

# Sample product page
if [ -f "$PUBLIC/product/lending/aave.md/index.html" ] || [ -f "$PUBLIC/product/aave/index.html" ] || find "$PUBLIC/product" -path "*/aave*" -name "index.html" | head -1 | grep -q .; then
  pass "Product page exists (Aave)"
else
  fail "Product page missing (Aave)"
fi

# Ecosystem pages
for eco in ethereum bitcoin solana polygon; do
  if [ -f "$PUBLIC/$eco/index.html" ]; then pass "Ecosystem: /$eco"; else fail "Ecosystem missing: /$eco"; fi
done

# Static pages
for page in about events crypto-airdrops; do
  if [ -f "$PUBLIC/$page/index.html" ]; then pass "Page: /$page"; else fail "Page missing: /$page"; fi
done

# 404
if [ -f "$PUBLIC/404.html" ] || [ -f "$PUBLIC/404.html/index.html" ]; then pass "404 page exists"; else fail "404 page missing"; fi

# RSS feed
if [ -f "$PUBLIC/feed.xml" ]; then pass "RSS feed exists"; else fail "RSS feed missing"; fi

# Sitemap
if [ -f "$PUBLIC/sitemap.xml" ]; then pass "Sitemap exists"; else fail "Sitemap missing"; fi

# -------------------------------------------------------
# TEST 4: HTML content checks
# -------------------------------------------------------
echo ""
echo "--- Test 4: HTML Content Checks ---"

# Check blog post has expected elements
BLOG_FILE="$PUBLIC/aave-mess-decentralized-governance/index.html"
if [ -f "$BLOG_FILE" ]; then
  if grep -q 'BlogPosting' "$BLOG_FILE"; then pass "Blog JSON-LD schema present"; else fail "Blog JSON-LD schema missing"; fi
  if grep -q 'og:title' "$BLOG_FILE"; then pass "Blog OG meta tags present"; else fail "Blog OG meta tags missing"; fi
  if grep -q 'class="tag"' "$BLOG_FILE"; then pass "Blog tag links present"; else fail "Blog tag links missing"; fi
fi

# Check homepage has expected elements
HOME_FILE="$PUBLIC/index.html"
if [ -f "$HOME_FILE" ]; then
  if grep -q 'Organization' "$HOME_FILE"; then pass "Homepage Organization schema present"; else fail "Homepage Organization schema missing"; fi
  if grep -q 'og:title' "$HOME_FILE"; then pass "Homepage OG meta present"; else fail "Homepage OG meta missing"; fi
fi

# Check product pages have expected structure
PRODUCT_FILES=$(find "$PUBLIC/product" -name "index.html" 2>/dev/null | head -3)
if [ -n "$PRODUCT_FILES" ]; then
  FIRST_PRODUCT=$(echo "$PRODUCT_FILES" | head -1)
  if grep -q 'BreadcrumbList' "$FIRST_PRODUCT"; then pass "Product BreadcrumbList schema"; else warn "Product BreadcrumbList schema missing"; fi
  if grep -q '"@type": "Product"' "$FIRST_PRODUCT" || grep -q '"@type":"Product"' "$FIRST_PRODUCT"; then pass "Product schema present"; else warn "Product schema missing"; fi
fi

# -------------------------------------------------------
# TEST 5: Tag pages
# -------------------------------------------------------
echo ""
echo "--- Test 5: Tag Pages ---"
TAG_COUNT=$(find "$PUBLIC/tags" -name "index.html" 2>/dev/null | wc -l | tr -d ' ')
if [ "$TAG_COUNT" -gt 0 ]; then
  pass "Tag pages generated: $TAG_COUNT"
else
  warn "No tag pages found in /tags/"
fi

# Check for /t/ tag pages (Jekyll format)
T_COUNT=$(find "$PUBLIC/t" -name "*.html" 2>/dev/null | wc -l | tr -d ' ')
if [ "$T_COUNT" -gt 0 ]; then
  pass "Jekyll-format tag pages in /t/: $T_COUNT"
else
  warn "No /t/ tag pages found (Jekyll used /t/{tag}.html format)"
fi

# -------------------------------------------------------
# TEST 6: No broken internal links (basic check)
# -------------------------------------------------------
echo ""
echo "--- Test 6: Internal Link Spot Check ---"
BROKEN=0
# Check some key internal links from the homepage
if [ -f "$HOME_FILE" ]; then
  for link in blog about events crypto-airdrops; do
    if [ -d "$PUBLIC/$link" ] || [ -f "$PUBLIC/$link/index.html" ]; then
      pass "Internal link /$link resolves"
    else
      fail "Internal link /$link broken"
      BROKEN=$((BROKEN + 1))
    fi
  done
fi

# -------------------------------------------------------
# TEST 7: Redirects/Aliases
# -------------------------------------------------------
echo ""
echo "--- Test 7: Redirects (Aliases) ---"
# Hugo creates redirect HTML files for aliases
for redirect in product decentralized_lending analytics custodian_services; do
  if [ -f "$PUBLIC/$redirect/index.html" ] && grep -q 'refresh' "$PUBLIC/$redirect/index.html" 2>/dev/null; then
    pass "Redirect /$redirect exists"
  elif [ -f "$PUBLIC/$redirect/index.html" ]; then
    warn "/$redirect exists but may not be a redirect"
  else
    warn "Redirect /$redirect not found"
  fi
done

# -------------------------------------------------------
# Summary
# -------------------------------------------------------
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
