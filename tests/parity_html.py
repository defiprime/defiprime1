import html
import json
import re
from html.parser import HTMLParser

META_FIELDS = ["title", "description", "canonical", "og", "twitter", "robots", "ld-types", "h1"]
META_FIELD_KEY = {"ld-types": "ld_types"}
META_TAG_MAP_FIELDS = {"og", "twitter"}


def collapse_ws(text):
    return re.sub(r"\s+", " ", text).strip()


def normalize_link(href):
    href = html.unescape(href)
    if href.startswith("https://defiprime.com"):
        href = href[len("https://defiprime.com"):]
    elif not href.startswith("/"):
        return None
    href = href.split("#", 1)[0]
    href = href.split("?", 1)[0]
    if href == "":
        href = "/"
    href = re.sub(r"/+", "/", href)
    return href


def collect_ld_types(obj, out):
    if isinstance(obj, dict):
        value = obj.get("@type")
        if isinstance(value, str):
            out.add(value)
        elif isinstance(value, list):
            out.update(v for v in value if isinstance(v, str))
        for v in obj.values():
            collect_ld_types(v, out)
    elif isinstance(obj, list):
        for item in obj:
            collect_ld_types(item, out)


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self.description = None
        self.canonical = None
        self.robots = None
        self.og = {}
        self.twitter = {}
        self.h1 = None
        self.links = set()
        self.ld_json_blocks = []
        self._in_title = False
        self._title_parts = []
        self._in_h1 = False
        self._h1_parts = []
        self._in_ldjson = False
        self._ldjson_parts = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "title" and self.title is None:
            self._in_title = True
            self._title_parts = []
        elif tag == "meta":
            name = d.get("name")
            prop = d.get("property")
            content = d.get("content") or ""
            if name == "description" and self.description is None:
                self.description = content
            elif name == "robots" and self.robots is None:
                self.robots = content
            elif prop and prop.startswith("og:"):
                self.og.setdefault(prop, content)
            elif name and name.startswith("twitter:"):
                self.twitter.setdefault(name, content)
        elif tag == "link":
            if d.get("rel") == "canonical" and self.canonical is None:
                self.canonical = d.get("href") or ""
        elif tag == "h1" and self.h1 is None and not self._in_h1:
            self._in_h1 = True
            self._h1_parts = []
        elif tag == "a":
            href = d.get("href")
            if href:
                self.links.add(href)
        elif tag == "script" and d.get("type") == "application/ld+json":
            self._in_ldjson = True
            self._ldjson_parts = []

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self._in_title = False
            self.title = "".join(self._title_parts)
        elif tag == "h1" and self._in_h1:
            self._in_h1 = False
            self.h1 = "".join(self._h1_parts)
        elif tag == "script" and self._in_ldjson:
            self._in_ldjson = False
            self.ld_json_blocks.append("".join(self._ldjson_parts))

    def handle_data(self, data):
        if self._in_title:
            self._title_parts.append(data)
        if self._in_h1:
            self._h1_parts.append(data)
        if self._in_ldjson:
            self._ldjson_parts.append(data)


def parse_meta(text):
    parser = MetaParser()
    parser.feed(text)
    parser.close()

    ld_types = set()
    for block in parser.ld_json_blocks:
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        collect_ld_types(data, ld_types)

    links = set()
    for href in parser.links:
        normalized = normalize_link(href)
        if normalized is not None:
            links.add(normalized)

    return {
        "title": html.unescape(parser.title or ""),
        "description": html.unescape(parser.description or ""),
        "canonical": html.unescape(parser.canonical or ""),
        "robots": html.unescape(parser.robots or ""),
        "og": {k: html.unescape(v) for k, v in parser.og.items()},
        "twitter": {k: html.unescape(v) for k, v in parser.twitter.items()},
        "h1": collapse_ws(html.unescape(parser.h1 or "")),
        "ld_types": sorted(ld_types),
        "links": links,
    }


def parse_meta_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return parse_meta(f.read())


def format_field_value(field, value):
    if field == "ld-types":
        return "[" + ", ".join(value) + "]"
    return value


def compare_meta(gm, hm):
    diffs = []
    for field in META_FIELDS:
        key = META_FIELD_KEY.get(field, field)
        gv = gm[key]
        hv = hm[key]
        if field in META_TAG_MAP_FIELDS:
            for tag in sorted(set(gv) | set(hv)):
                gtag = gv.get(tag, "")
                htag = hv.get(tag, "")
                if gtag != htag:
                    diffs.append((tag, gtag, htag))
            continue
        if gv != hv:
            diffs.append((field, format_field_value(field, gv), format_field_value(field, hv)))
    return diffs


def compare_links(gm, hm):
    missing = sorted(gm["links"] - hm["links"])
    extra = sorted(hm["links"] - gm["links"])
    return missing, extra
