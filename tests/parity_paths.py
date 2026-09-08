import fnmatch
import os

EXTENSIONS = {".html", ".xml", ".txt", ".json"}

GOLDEN_IGNORE_NAMES = {
    "bin",
    "docs",
    "assets",
    "images",
    "CLAUDE.md",
    "BLOG-IMAGE-STYLE-GUIDE.md",
    "LICENSE.txt",
    "netlify.toml",
    "vercel.json",
    "wrangler.toml",
    "redirects.json",
    "package-lock.json",
    "insert_date.sh",
    "ogp-template.png",
}
GOLDEN_IGNORE_GLOBS = ["favicon.*"]

PUBLIC_IGNORE_NAMES = {"assets", "images", "css", "js"}
PUBLIC_IGNORE_GLOBS = []


def is_ignored_top(name, ignore_names, ignore_globs):
    if name in ignore_names:
        return True
    for pattern in ignore_globs:
        if fnmatch.fnmatch(name, pattern):
            return True
    return False


def collect_paths(root, ignore_names, ignore_globs):
    paths = set()
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == ".":
            dirnames[:] = [d for d in dirnames if not is_ignored_top(d, ignore_names, ignore_globs)]
        for name in filenames:
            if rel_dir == "." and is_ignored_top(name, ignore_names, ignore_globs):
                continue
            ext = os.path.splitext(name)[1]
            if ext not in EXTENSIONS:
                continue
            rel_path = name if rel_dir == "." else os.path.join(rel_dir, name)
            paths.add(rel_path.replace(os.sep, "/"))
    return paths
