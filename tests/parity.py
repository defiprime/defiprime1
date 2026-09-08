#!/usr/bin/env python3
import argparse
import os
import sys

from parity_allow import AllowlistError, load_allowlist, is_allowed
from parity_html import compare_links, compare_meta, parse_meta_file
from parity_paths import (
    GOLDEN_IGNORE_GLOBS,
    GOLDEN_IGNORE_NAMES,
    PUBLIC_IGNORE_GLOBS,
    PUBLIC_IGNORE_NAMES,
    collect_paths,
)


class Result:
    def __init__(self):
        self.missing = []
        self.missing_suppressed = 0
        self.extra = []
        self.extra_suppressed = 0
        self.meta = []
        self.meta_suppressed = 0
        self.links = []
        self.links_suppressed = 0
        self.exit_code = 0


def run(golden_dir, public_dir, allow_path, only=None):
    allow_entries = load_allowlist(allow_path)

    golden_paths = collect_paths(golden_dir, GOLDEN_IGNORE_NAMES, GOLDEN_IGNORE_GLOBS)
    public_paths = collect_paths(public_dir, PUBLIC_IGNORE_NAMES, PUBLIC_IGNORE_GLOBS)

    if only:
        golden_paths = {p for p in golden_paths if p.startswith(only)}
        public_paths = {p for p in public_paths if p.startswith(only)}

    result = Result()

    for path in sorted(golden_paths - public_paths):
        if is_allowed(allow_entries, "MISSING", path):
            result.missing_suppressed += 1
        else:
            result.missing.append(path)

    for path in sorted(public_paths - golden_paths):
        if is_allowed(allow_entries, "EXTRA", path):
            result.extra_suppressed += 1
        else:
            result.extra.append(path)

    common_html = sorted(p for p in (golden_paths & public_paths) if p.endswith(".html"))
    for path in common_html:
        gm = parse_meta_file(os.path.join(golden_dir, path))
        hm = parse_meta_file(os.path.join(public_dir, path))

        for field, gval, hval in compare_meta(gm, hm):
            if is_allowed(allow_entries, "META", path, field):
                result.meta_suppressed += 1
            else:
                result.meta.append((path, field, gval, hval))

        missing_links, extra_links = compare_links(gm, hm)
        if missing_links or extra_links:
            if is_allowed(allow_entries, "LINKS", path):
                result.links_suppressed += 1
            else:
                result.links.append((path, missing_links, extra_links))

    if result.missing or result.extra or result.meta or result.links:
        result.exit_code = 1

    return result


def print_findings(result, show, summary_only):
    if not summary_only:
        _print_capped("MISSING {}".format, result.missing, show, "MISSING")
        _print_capped("EXTRA {}".format, result.extra, show, "EXTRA")
        _print_capped(
            lambda item: f"META {item[0]} {item[1]}: golden={item[2]} hugo={item[3]}",
            result.meta,
            show,
            "META",
        )
        _print_capped(
            lambda item: f"LINKS {item[0]}: missing={item[1]} extra={item[2]}",
            result.links,
            show,
            "LINKS",
        )

    print("")
    print("=== Parity summary ===")
    print(f"MISSING: {len(result.missing)} found, {result.missing_suppressed} suppressed")
    print(f"EXTRA:   {len(result.extra)} found, {result.extra_suppressed} suppressed")
    print(f"META:    {len(result.meta)} found, {result.meta_suppressed} suppressed")
    print(f"LINKS:   {len(result.links)} found, {result.links_suppressed} suppressed")


def _print_capped(formatter, items, show, label):
    for item in items[:show]:
        print(formatter(item))
    if len(items) > show:
        print(f"  ... {len(items) - show} more {label} not shown")


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--golden", required=True)
    parser.add_argument("--public", required=True)
    default_allow = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parity-allow.txt")
    parser.add_argument("--allow", default=default_allow)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--only", default=None)
    parser.add_argument("--show", type=int, default=20)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv if argv is not None else sys.argv[1:])
    try:
        result = run(args.golden, args.public, args.allow, only=args.only)
    except AllowlistError as e:
        print(f"parity: {e}", file=sys.stderr)
        return 2
    print_findings(result, args.show, args.summary)
    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
