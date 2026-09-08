#!/usr/bin/env python3
import argparse
import difflib
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sync_content_assets import sync_assets
from sync_content_core import (
    OFFENDER_RE, Report, SyncError, convert_entries, convert_shortcodes, entry_value,
    find_entry, has_liquid, name_slug, parse_front_matter, permalink_to_url,
    render_front_matter, set_url, split_front_matter, strip_cr, youtube_id,
)
from sync_content_docs import (
    convert_body, emit, load_doc, sync_alternatives, sync_events, sync_posts, sync_products,
)

ROOT_SKIP = ("README.md", "CONTRIBUTING.md", "BLOG-IMAGE-STYLE-GUIDE.md", "CLAUDE.md",
             "AGENTS.md", "Plans.md")
ROOT_INDEXES = {"index.md": "content/_index.md", "blog.md": "content/blog/_index.md",
                "alternatives.md": "content/alternatives/_index.md"}
NO_LAYOUT_TARGETS = ("content/_index.md",)
STRICT_ROOTS = ("content/blog/", "content/product/", "content/alternatives/")


def merge_entries(converted, branch_entries, drop_layout):
    if drop_layout:
        converted = [(key, block) for key, block in converted if key != "layout"]
    elif branch_entries is not None:
        branch = find_entry(branch_entries, "layout")[1]
        index = find_entry(converted, "layout")[0]
        if branch is not None and index >= 0:
            converted = list(converted)
            converted[index] = ("layout", branch)
        elif branch is not None:
            converted = [("layout", branch)] + list(converted)
    if branch_entries is None:
        return list(converted)
    taken = {key for key, _ in converted}
    if drop_layout:
        taken.add("layout")
    return list(converted) + [(key, block) for key, block in branch_entries if key not in taken]


def page_body(master_body, branch_body, rel, report):
    if has_liquid(master_body) and branch_body is not None:
        report.body_diffs[rel] = "".join(difflib.unified_diff(
            master_body.splitlines(True), branch_body.splitlines(True),
            fromfile="master", tofile="branch"))
        body = branch_body
    else:
        body = convert_body(master_body, rel, report)
    if has_liquid(body):
        report.needs_template.append(rel)
    return body


def is_generated_output(entries):
    sitemap = find_entry(entries, "sitemap")[1]
    layout = find_entry(entries, "layout")[1]
    return (sitemap is not None and entry_value(sitemap) == "false"
            and layout is not None and entry_value(layout) == "null")


def sync_pages(source, dest, report, managed):
    for name in sorted(os.listdir(source)):
        if not name.endswith(".md") or name in ROOT_SKIP:
            continue
        doc = load_doc(os.path.join(source, name), name, report)
        if doc is None:
            continue
        entries, master_body = doc
        if is_generated_output(entries):
            continue
        rel = ROOT_INDEXES.get(name, "content/" + name)
        converted = convert_entries(entries, drop_pagination=True)
        if not rel.endswith("_index.md") and find_entry(converted, "url")[1] is None:
            converted = set_url(converted, permalink_to_url(name[:-3]))
        branch_entries, branch_body = None, None
        branch_path = os.path.join(dest, rel)
        if os.path.isfile(branch_path):
            branch = load_doc(branch_path, rel, report)
            if branch is not None:
                branch_entries, branch_body = branch
        if rel.endswith("_index.md"):
            report.rewritten_indexes.append(rel)
        emit(dest, rel, merge_entries(converted, branch_entries, rel in NO_LAYOUT_TARGETS),
             page_body(master_body, branch_body, rel, report), report, managed)


def prune(dest, managed, report):
    for name in ("content/airdrop", "content/.claude"):
        path = os.path.join(dest, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
            report.deleted.append(name + "/")
    legacy = os.path.join(dest, "scripts", "migrate-content.sh")
    if os.path.isfile(legacy):
        os.remove(legacy)
        report.deleted.append("scripts/migrate-content.sh")
    for dirpath, dirnames, filenames in os.walk(os.path.join(dest, "content")):
        dirnames[:] = sorted(dirnames)
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), dest)
            if rel in managed:
                continue
            if name == "_index.md":
                report.preserved_indexes.append(rel)
                continue
            os.remove(os.path.join(dest, rel))
            report.deleted.append(rel)


def scan_offenders(dest, managed, report):
    strict = []
    for rel in sorted(managed):
        path = os.path.join(dest, rel)
        if not os.path.isfile(path):
            continue
        with open(path, "r", encoding="utf-8") as handle:
            body = split_front_matter(handle.read())[1]
        if not OFFENDER_RE.search(body):
            continue
        report.offenders.append(rel)
        if rel.startswith(STRICT_ROOTS):
            strict.append(rel)
    if strict:
        raise SyncError("liquid left in generated content: " + ", ".join(strict))


def sync(source, dest, golden=None):
    report = Report()
    managed = set()
    sync_posts(source, dest, report, managed)
    sync_products(source, dest, report, managed, golden)
    sync_alternatives(source, dest, report, managed, golden)
    sync_events(source, dest, report, managed)
    sync_pages(source, dest, report, managed)
    prune(dest, managed, report)
    sync_assets(source, dest, report)
    scan_offenders(dest, managed, report)
    if report.missing_golden:
        raise SyncError("urls absent from the golden build: " + ", ".join(
            "%s -> %s" % pair for pair in report.missing_golden))
    return report


def summarise(report):
    lines = [
        "written: %d" % len(report.written),
        "deleted: %d" % len(report.deleted),
        "youtube: %d in %d files" % (sum(n for _, n in report.youtube), len(report.youtube)),
        "figure: %d in %d files" % (sum(n for _, n in report.figure), len(report.figure)),
        "tweetcard: %d in %d files" % (sum(n for _, n in report.tweetcard),
                                       len(report.tweetcard)),
        "preserved _index.md: %d" % len(report.preserved_indexes),
        "rewritten _index.md: %d" % len(report.rewritten_indexes),
        "branch bodies kept: %d" % len(report.body_diffs),
        "needs a hugo layout: %s" % (", ".join(report.needs_template) or "none"),
        "liquid offenders reported: %s" % (", ".join(report.offenders) or "none"),
        "duplicate product urls: %s" % (", ".join(
            "%s won by %s over %s" % triple for triple in report.duplicate_urls) or "none"),
        "unparseable front matter: %s" % (", ".join(report.unparseable) or "none"),
    ]
    return "\n".join(lines + report.notes)


def main(argv=None):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="../defiprime")
    parser.add_argument("--dest", default=root)
    parser.add_argument("--golden", default=None)
    parser.add_argument("--diffs", default=None)
    args = parser.parse_args(argv)
    golden = args.golden if args.golden and os.path.isdir(args.golden) else None
    report = sync(os.path.abspath(args.source), os.path.abspath(args.dest), golden)
    print(summarise(report))
    if args.diffs:
        with open(args.diffs, "w", encoding="utf-8") as handle:
            for rel in sorted(report.body_diffs):
                handle.write("=== %s ===\n%s\n" % (rel, report.body_diffs[rel]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
