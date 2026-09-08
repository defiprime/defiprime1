import os

from sync_content_core import (
    SyncError, convert_entries, convert_shortcodes, count_conversions, entry_value, find_entry,
    name_slug, parse_front_matter, read_collections, render_front_matter, set_url,
    split_front_matter, strip_cr,
)

SKIPPED_COLLECTIONS = ("posts", "events", "alternatives")


def read_text(path):
    with open(path, "r", encoding="utf-8") as handle:
        return strip_cr(handle.read())


def drop_case_variants(directory, rel, report):
    base = os.path.basename(rel)
    for name in os.listdir(directory):
        if name != base and name.lower() == base.lower():
            os.remove(os.path.join(directory, name))
            report.deleted.append(os.path.join(os.path.dirname(rel), name))


def write_text(dest, rel, text, report):
    path = os.path.join(dest, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    drop_case_variants(os.path.dirname(path), rel, report)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() == text:
                return
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    report.written.append(rel)


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
    write_text(dest, rel, render_front_matter(entries) + body, report)
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


def sync_products(source, dest, report, managed, golden):
    for collection in read_collections(read_text(os.path.join(source, "_config.yml"))):
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
            rel = "content/product/" + collection + "/" + name.lower()
            converted = set_url(convert_entries(entries, rename_type=True),
                                "/product/" + slug + ".html")
            emit(dest, rel, converted, convert_body(body, rel, report), report, managed)
            check_golden(golden, "product/" + slug + ".html", rel, report)


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
        write_text(dest, rel, read_text(os.path.join(directory, name)), report)
        managed.add(rel)
