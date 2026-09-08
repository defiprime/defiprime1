import os
import re

KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_.\-]*)\s*:")
YOUTUBE_RE = re.compile(r"\{%-?\s*youtube\s+(.*?)\s*-?%\}", re.S)
INCLUDE_RE = re.compile(r"\{%-?\s*include\s+(figure|tweet)\.html\s*(.*?)\s*-?%\}", re.S)
PARAM_RE = re.compile(r'([A-Za-z0-9_-]+)\s*=\s*"([^"]*)"')
LIST_FORM_RE = re.compile(r"\[\s*([^\[\]]*?)\s*\]")
LIST_ITEM_RE = re.compile(r"^(\s*-\s+)(.*)$")
OFFENDER_RE = re.compile(r"\{%|\{\{\s*site\.|\{\{\s*page\.")
SHORTCODE_NAMES = {"figure": "figure", "tweet": "tweetcard"}


class SyncError(Exception):
    pass


class Report:
    def __init__(self):
        self.youtube = []
        self.figure = []
        self.tweetcard = []
        self.unparseable = []
        self.needs_template = []
        self.body_diffs = {}
        self.preserved_indexes = []
        self.rewritten_indexes = []
        self.offenders = []
        self.missing_golden = []
        self.duplicate_urls = []
        self.deleted = []
        self.written = []
        self.notes = []


def strip_cr(text):
    return text.replace("\r", "")


def write_file(path, text, report, label, drop_case=False):
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    if drop_case:
        base = os.path.basename(path)
        for name in os.listdir(directory):
            if name != base and name.lower() == base.lower():
                os.remove(os.path.join(directory, name))
                report.deleted.append(os.path.join(os.path.dirname(label), name))
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() == text:
                return
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    report.written.append(label)


def split_front_matter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1:])
    return None, text


def parse_front_matter(fm):
    entries = []
    current = None
    for line in fm.split("\n"):
        match = KEY_RE.match(line)
        if match:
            current = (match.group(1), [line])
            entries.append(current)
        elif current is None:
            if line.strip():
                return None
        else:
            current[1].append(line)
    return [(key, trim_trailing_blanks(lines)) for key, lines in entries]


def trim_trailing_blanks(lines):
    out = list(lines)
    while len(out) > 1 and not out[-1].strip():
        out.pop()
    return out


def render_front_matter(entries):
    if not entries:
        return "---\n---\n"
    block = "\n".join("\n".join(lines) for _, lines in entries)
    return "---\n" + block + "\n---\n"


def entry_value(lines):
    return lines[0].split(":", 1)[1].strip()


def rename_key(key, lines):
    return [key + ":" + lines[0].split(":", 1)[1]] + list(lines[1:])


def find_entry(entries, key):
    for index, (name, lines) in enumerate(entries):
        if name == key:
            return index, lines
    return -1, None


def permalink_to_url(value):
    text = value.strip().strip("\"'").strip()
    if not text:
        raise SyncError("empty permalink value")
    if text.endswith("/") or text.endswith(".html"):
        return "/" + text.lstrip("/")
    return "/" + text.lstrip("/") + ".html"


def name_slug(stem):
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")


def youtube_id(url):
    text = url.strip().strip("\"'")
    for pattern in (r"[?&]v=([A-Za-z0-9_-]+)", r"youtu\.be/([A-Za-z0-9_-]+)",
                    r"/embed/([A-Za-z0-9_-]+)"):
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    raise SyncError("unrecognised youtube url: " + text)


def rooted_alias_items(lines):
    out = [lines[0]]
    for line in lines[1:]:
        match = LIST_ITEM_RE.match(line)
        if match is None:
            out.append(line)
            continue
        value = match.group(2).strip()
        quote = ""
        if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'":
            quote, value = value[0], value[1:-1]
        if not value.startswith("/"):
            value = "/" + value
        out.append(match.group(1) + quote + value + quote)
    return out


def convert_entries(entries, rename_type=False, drop_pagination=False):
    out = []
    for key, lines in entries:
        lines = list(lines)
        if key == "pagination" and drop_pagination:
            continue
        if key == "layout":
            match = LIST_FORM_RE.fullmatch(entry_value(lines))
            if match:
                lines = ["layout: " + match.group(1)]
        elif key == "permalink":
            key = "url"
            lines = ["url: " + permalink_to_url(entry_value(lines))]
        elif key == "redirect_from":
            key = "aliases"
            lines = rooted_alias_items(rename_key("aliases", lines))
        elif key == "type" and rename_type:
            key = "product-type"
            lines = rename_key("product-type", lines)
        elif key == "filter-by" and rename_type:
            tokens = [token.strip() for token in entry_value(lines).split(",")]
            tokens = ["product-type" if token == "type" else token for token in tokens]
            lines = ["filter-by: " + ", ".join(tokens)]
        out.append((key, lines))
    return out


def set_url(entries, url):
    out = [(key, lines) for key, lines in entries if key != "url"]
    return [("url", ["url: " + url])] + out


def convert_shortcodes(body):
    def youtube_sub(match):
        return "{{< youtube " + youtube_id(match.group(1)) + " >}}"

    def include_sub(match):
        name = SHORTCODE_NAMES[match.group(1)]
        params = PARAM_RE.findall(match.group(2))
        rendered = " ".join('%s="%s"' % pair for pair in params)
        return "{{< " + name + (" " + rendered if rendered else "") + " >}}"

    return INCLUDE_RE.sub(include_sub, YOUTUBE_RE.sub(youtube_sub, body))


def count_conversions(body):
    kinds = [match.group(1) for match in INCLUDE_RE.finditer(body)]
    return (
        len(YOUTUBE_RE.findall(body)),
        kinds.count("figure"),
        kinds.count("tweet"),
    )


def has_liquid(text):
    return "{%" in text or "{{" in text


def read_collections(text):
    names = []
    inside = False
    for line in strip_cr(text).split("\n"):
        if re.match(r"^collections:\s*$", line):
            inside = True
            continue
        if inside:
            if line.strip() and not line.startswith(" "):
                break
            match = re.match(r"^  ([A-Za-z0-9_.\-]+):\s*$", line)
            if match:
                names.append(match.group(1))
    return names
