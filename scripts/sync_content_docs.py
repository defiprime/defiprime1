import os

from sync_content_core import (
    SyncError, convert_entries, convert_shortcodes, count_conversions, entry_value, find_entry,
    name_slug, parse_front_matter, read_collections, render_front_matter, set_url,
    split_front_matter, strip_cr, write_file,
)

SKIPPED_COLLECTIONS = ("posts", "events", "alternatives")
SHADOW_BUILD = ("build", ["build:", "  render: link", "  list: always"])


def read_text(path):
    with open(path, "r", encoding="utf-8") as handle:
        return strip_cr(handle.read())


def load_doc(path, rel, report):
    front_matter, body = split_front_matter(read_text(path))
    if front_matter is None:
        return None
    entries = parse_front_matter(front_matter)
    if entries is None:
        report.unparseable.append(rel)
        return None
    return entries, body


def convert_body(body, rel, report):
    youtube, figure, tweet = count_conversions(body)
    if youtube:
        report.youtube.append((rel, youtube))
    if figure:
        report.figure.append((rel, figure))
    if tweet:
        report.tweetcard.append((rel, tweet))
    return convert_shortcodes(body)


def emit(dest, rel, entries, body, report, managed):
    write_file(os.path.join(dest, rel), render_front_matter(entries) + body, report, rel, True)
    managed.add(rel)


def source_names(directory):
    if not os.path.isdir(directory):
        return []
    return sorted(name for name in os.listdir(directory) if name.endswith(".md"))


def check_golden(golden, relative, rel, report):
    if golden is None:
        return
    if not os.path.isfile(os.path.join(golden, relative)):
        report.missing_golden.append((rel, relative))


def sync_posts(source, dest, report, managed):
    directory = os.path.join(source, "collections", "_posts")
    for name in source_names(directory):
        rel_source = os.path.join("collections", "_posts", name)
        doc = load_doc(os.path.join(directory, name), rel_source, report)
        if doc is None:
            report.unparseable.append(rel_source)
            continue
        entries, body = doc
        category = find_entry(entries, "category")[1]
        listing = category is not None and entry_value(category).strip("\"'") == "products"
        converted = convert_entries(entries, rename_type=listing)
        if listing:
            permalink = find_entry(entries, "permalink")[1]
            if permalink is None:
                raise SyncError("listing post without permalink: " + rel_source)
            rel = "content/" + entry_value(permalink).strip("\"'").strip("/") + ".md"
        else:
            rel = "content/blog/" + name
        emit(dest, rel, converted, convert_body(body, rel, report), report, managed)


def collect_products(source, report):
    docs = []
    order = read_collections(read_text(os.path.join(source, "_config.yml")))
    for rank, collection in enumerate(order):
        if collection in SKIPPED_COLLECTIONS:
            continue
        directory = os.path.join(source, "collections", "_" + collection)
        if not os.path.isdir(directory):
            report.notes.append("collection directory missing: _" + collection)
            continue
        for name in source_names(directory):
            rel_source = os.path.join("collections", "_" + collection, name)
            doc = load_doc(os.path.join(directory, name), rel_source, report)
            if doc is None:
                report.unparseable.append(rel_source)
                continue
            entries, body = doc
            slug = name_slug(name[:-3])
            docs.append({
                "rank": rank,
                "rel": "content/product/" + collection + "/" + name.lower(),
                "slug": slug,
                "url": "/product/" + slug + ".html",
                "entries": entries,
                "body": body,
            })
    return docs


def shadowed_products(docs, report):
    claims = {}
    for doc in docs:
        claims.setdefault(doc["url"], []).append((doc["rank"], doc["rel"]))
    shadowed = set()
    for url in sorted(claims):
        ranked = sorted(claims[url])
        if len(ranked) < 2:
            continue
        winner = ranked[-1][1]
        for _, rel in ranked[:-1]:
            shadowed.add(rel)
            report.duplicate_urls.append((url, winner, rel))
    return shadowed


def sync_products(source, dest, report, managed, golden):
    docs = collect_products(source, report)
    shadowed = shadowed_products(docs, report)
    for doc in docs:
        converted = set_url(convert_entries(doc["entries"], rename_type=True), doc["url"])
        if doc["rel"] in shadowed:
            converted = [item for item in converted if item[0] != SHADOW_BUILD[0]]
            converted.append((SHADOW_BUILD[0], list(SHADOW_BUILD[1])))
        body = convert_body(doc["body"], doc["rel"], report)
        emit(dest, doc["rel"], converted, body, report, managed)
        check_golden(golden, "product/" + doc["slug"] + ".html", doc["rel"], report)


def sync_alternatives(source, dest, report, managed, golden):
    directory = os.path.join(source, "collections", "_alternatives")
    for name in source_names(directory):
        rel_source = os.path.join("collections", "_alternatives", name)
        doc = load_doc(os.path.join(directory, name), rel_source, report)
        if doc is None:
            report.unparseable.append(rel_source)
            continue
        entries, body = doc
        rel = "content/alternatives/" + name.lower()
        converted = convert_entries(entries)
        emit(dest, rel, converted, convert_body(body, rel, report), report, managed)
        url = find_entry(converted, "url")[1]
        if url is not None:
            check_golden(golden, entry_value(url).lstrip("/"), rel, report)


def sync_events(source, dest, report, managed):
    directory = os.path.join(source, "collections", "_events")
    for name in source_names(directory):
        rel = "content/events/" + name
        write_file(os.path.join(dest, rel), read_text(os.path.join(directory, name)),
                   report, rel, True)
        managed.add(rel)
