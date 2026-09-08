import filecmp
import os
import shutil

from sync_content_core import has_liquid, split_front_matter, strip_cr

IGNORED_NAMES = {".DS_Store"}
ROOT_ASSETS = ("defiprime.tokenlist.json", "favicon.ico", "favicon.png", "ogp-template.png")
STATIC_MIRRORED = ("defiprime.tokenlist.json", "favicon.ico", "favicon.png")


def relative_files(root):
    out = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in IGNORED_NAMES]
        for name in filenames:
            if name in IGNORED_NAMES:
                continue
            out.add(os.path.relpath(os.path.join(dirpath, name), root))
    return out


def copy_if_different(src, dst, report, label):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False):
        return
    shutil.copyfile(src, dst)
    report.written.append(label)


def mirror_images(source, dest, report):
    src_root = os.path.join(source, "images")
    if not os.path.isdir(src_root):
        return
    wanted = relative_files(src_root)
    dst_root = os.path.join(dest, "static", "images")
    for rel in sorted(wanted):
        copy_if_different(os.path.join(src_root, rel), os.path.join(dst_root, rel),
                          report, os.path.join("static", "images", rel))
    if not os.path.isdir(dst_root):
        return
    for rel in sorted(relative_files(dst_root) - wanted):
        os.remove(os.path.join(dst_root, rel))
        report.deleted.append(os.path.join("static", "images", rel))


def copy_root_assets(source, dest, report):
    for name in ROOT_ASSETS:
        src = os.path.join(source, name)
        if not os.path.isfile(src):
            continue
        copy_if_different(src, os.path.join(dest, name), report, name)
        if name in STATIC_MIRRORED:
            copy_if_different(src, os.path.join(dest, "static", name), report,
                              os.path.join("static", name))


def write_text_asset(path, text, report, label):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() == text:
                return
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    report.written.append(label)


def read_body(path):
    with open(path, "r", encoding="utf-8") as handle:
        text = strip_cr(handle.read())
    front_matter, body = split_front_matter(text)
    return body if front_matter is not None else text


def copy_authors(source, dest, report):
    src = os.path.join(source, "_data", "authors.yml")
    if not os.path.isfile(src):
        return
    with open(src, "r", encoding="utf-8") as handle:
        text = strip_cr(handle.read())
    write_text_asset(os.path.join(dest, "data", "authors.yaml"), text, report,
                     os.path.join("data", "authors.yaml"))


def copy_text_roots(source, dest, report):
    robots = os.path.join(source, "robots.txt")
    if os.path.isfile(robots):
        write_text_asset(os.path.join(dest, "static", "robots.txt"), read_body(robots),
                         report, os.path.join("static", "robots.txt"))
    llms = os.path.join(source, "llms.txt")
    if not os.path.isfile(llms):
        return
    body = read_body(llms)
    if has_liquid(body):
        report.needs_template.append("llms.txt")
        return
    write_text_asset(os.path.join(dest, "static", "llms.txt"), body, report,
                     os.path.join("static", "llms.txt"))


def sync_assets(source, dest, report):
    mirror_images(source, dest, report)
    copy_root_assets(source, dest, report)
    copy_authors(source, dest, report)
    copy_text_roots(source, dest, report)
