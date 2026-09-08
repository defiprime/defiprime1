#!/usr/bin/env python3
"""
Link crawler test for Hugo migration.
Starts from / on the local Hugo server, follows every internal link,
and reports any non-200 HTTP responses.

Usage:
    python3 tests/crawl-test.py [--base-url http://localhost:1313] [--verbose]
"""

import sys
import argparse
import time
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urldefrag
from html.parser import HTMLParser
from collections import defaultdict


class LinkExtractor(HTMLParser):
    """Extract href and src attributes from HTML."""

    def __init__(self):
        super().__init__()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a" and "href" in attrs_dict:
            self.links.add(attrs_dict["href"])
        elif tag in ("img", "script") and "src" in attrs_dict:
            self.links.add(attrs_dict["src"])
        elif tag == "link" and "href" in attrs_dict:
            self.links.add(attrs_dict["href"])
        # Also check data-src (lazyload)
        if "data-src" in attrs_dict:
            self.links.add(attrs_dict["data-src"])


def extract_links(html_content, current_url):
    """Extract and resolve all links from HTML content."""
    parser = LinkExtractor()
    try:
        parser.feed(html_content)
    except Exception:
        pass

    resolved = set()
    for link in parser.links:
        if not link or link.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        # Remove fragment
        link, _ = urldefrag(link)
        if not link:
            continue
        # Resolve relative URLs
        absolute = urljoin(current_url, link)
        resolved.add(absolute)

    return resolved


def is_internal(url, base_url):
    """Check if URL is internal (same host)."""
    parsed_base = urlparse(base_url)
    parsed_url = urlparse(url)
    return parsed_url.netloc == parsed_base.netloc or parsed_url.netloc == ""


def is_page_url(url):
    """Check if URL is likely an HTML page (not a static asset)."""
    parsed = urlparse(url)
    path = parsed.path.lower()
    # Skip common static asset extensions
    static_exts = (
        ".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
        ".woff", ".woff2", ".ttf", ".eot", ".pdf", ".zip", ".xml",
        ".json", ".webp", ".mp4", ".webm", ".ogg", ".mp3",
    )
    return not any(path.endswith(ext) for ext in static_exts)


def fetch_url(url, timeout=10):
    """Fetch a URL and return (status_code, content, content_type)."""
    req = Request(url, headers={"User-Agent": "DefiprimeCrawlTest/1.0"})
    try:
        response = urlopen(req, timeout=timeout)
        content_type = response.headers.get("Content-Type", "")
        content = ""
        if "text/html" in content_type:
            content = response.read().decode("utf-8", errors="replace")
        return response.status, content, content_type
    except HTTPError as e:
        return e.code, "", ""
    except URLError as e:
        return 0, "", str(e.reason)
    except Exception as e:
        return 0, "", str(e)


def crawl(base_url, verbose=False):
    """Crawl all internal pages starting from base_url."""
    start_time = time.time()

    # Track state
    visited = set()          # URLs we've fetched
    queue = [base_url]       # URLs to visit
    results = {}             # url -> status_code
    errors = []              # (url, status_code, found_on)
    link_sources = defaultdict(set)  # url -> set of pages that link to it
    asset_checked = set()    # Static assets we've checked

    # Stats
    pages_crawled = 0
    assets_checked_count = 0

    print(f"\n{'='*70}")
    print(f"  Link Crawler Test")
    print(f"  Base URL: {base_url}")
    print(f"{'='*70}\n")

    while queue:
        url = queue.pop(0)

        # Normalize: remove trailing fragment, ensure consistent form
        url, _ = urldefrag(url)

        if url in visited:
            continue

        if not is_internal(url, base_url):
            continue

        visited.add(url)

        # Determine if this is a page or static asset
        is_page = is_page_url(url)

        status, content, content_type = fetch_url(url)
        results[url] = status

        if is_page:
            pages_crawled += 1
            if verbose:
                status_icon = "OK" if status == 200 else f"ERR({status})"
                print(f"  [{status_icon}] {url}")
            elif pages_crawled % 50 == 0:
                print(f"  ... crawled {pages_crawled} pages so far ...")
        else:
            assets_checked_count += 1
            asset_checked.add(url)

        if status != 200:
            sources = link_sources.get(url, {"(start page)"})
            errors.append((url, status, sources))
            if not verbose:
                print(f"  [ERR {status}] {url}")
                for src in sorted(sources)[:3]:
                    print(f"           found on: {src}")

        # Extract links from HTML pages and add to queue
        if content and "text/html" in content_type:
            links = extract_links(content, url)
            for link in links:
                if is_internal(link, base_url):
                    link_clean, _ = urldefrag(link)
                    link_sources[link_clean].add(url)
                    if link_clean not in visited:
                        queue.append(link_clean)

    elapsed = time.time() - start_time

    # Print results
    print(f"\n{'='*70}")
    print(f"  RESULTS")
    print(f"{'='*70}")
    print(f"  Pages crawled:    {pages_crawled}")
    print(f"  Assets checked:   {assets_checked_count}")
    print(f"  Total URLs:       {len(visited)}")
    print(f"  Time:             {elapsed:.1f}s")
    print()

    # Categorize errors
    page_errors = [(u, s, src) for u, s, src in errors if is_page_url(u)]
    asset_errors = [(u, s, src) for u, s, src in errors if not is_page_url(u)]

    if not errors:
        print(f"  ALL {len(visited)} URLs returned 200 OK")
        print(f"{'='*70}\n")
        return 0

    # Page errors (critical)
    if page_errors:
        print(f"  PAGE ERRORS ({len(page_errors)}):")
        print(f"  {'-'*66}")
        for url, status, sources in sorted(page_errors, key=lambda x: x[1]):
            print(f"    [{status}] {url}")
            for src in sorted(sources)[:3]:
                print(f"          linked from: {src}")
        print()

    # Asset errors (warnings)
    if asset_errors:
        print(f"  ASSET ERRORS ({len(asset_errors)}):")
        print(f"  {'-'*66}")
        for url, status, sources in sorted(asset_errors, key=lambda x: x[1]):
            print(f"    [{status}] {url}")
            for src in sorted(sources)[:3]:
                print(f"          linked from: {src}")
        print()

    # Summary by status code
    status_counts = defaultdict(int)
    for _, status, _ in errors:
        status_counts[status] += 1
    print(f"  Error summary:")
    for status, count in sorted(status_counts.items()):
        label = {0: "Connection Error", 404: "Not Found", 500: "Server Error"}.get(status, f"HTTP {status}")
        print(f"    {label}: {count}")

    print(f"\n{'='*70}")
    total_errors = len(page_errors)
    if total_errors > 0:
        print(f"  FAIL: {total_errors} page error(s) found")
    else:
        print(f"  WARN: {len(asset_errors)} asset error(s), but all pages OK")
    print(f"{'='*70}\n")

    return 1 if page_errors else 0


def main():
    parser = argparse.ArgumentParser(description="Crawl local Hugo site and check for broken links")
    parser.add_argument("--base-url", default="http://localhost:1313", help="Base URL to crawl (default: http://localhost:1313)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print status of every URL")
    args = parser.parse_args()

    # Verify server is running
    print(f"Checking server at {args.base_url} ...")
    try:
        status, _, _ = fetch_url(args.base_url, timeout=5)
        if status != 200:
            print(f"ERROR: Server returned {status} for {args.base_url}")
            sys.exit(2)
    except Exception as e:
        print(f"ERROR: Cannot reach {args.base_url} - {e}")
        print("Make sure Hugo server is running: hugo server")
        sys.exit(2)

    print("Server is up. Starting crawl...")
    exit_code = crawl(args.base_url, verbose=args.verbose)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
