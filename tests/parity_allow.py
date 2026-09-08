import fnmatch
import os

ALLOWLIST_KINDS = {"MISSING", "EXTRA", "META", "LINKS"}


class AllowlistError(Exception):
    pass


def load_allowlist(path):
    entries = []
    if not os.path.exists(path):
        return entries
    with open(path, encoding="utf-8") as f:
        for lineno, raw_line in enumerate(f, 1):
            line = raw_line.rstrip("\n")
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                continue
            if "#" not in line:
                raise AllowlistError(
                    f"{path}:{lineno}: missing mandatory reason after '#': {line!r}"
                )
            body, reason = line.split("#", 1)
            reason = reason.strip()
            if not reason:
                raise AllowlistError(f"{path}:{lineno}: empty reason: {line!r}")
            parts = body.split()
            if len(parts) != 3:
                raise AllowlistError(
                    f"{path}:{lineno}: expected '<kind> <path-glob> <field-or-*>': {line!r}"
                )
            kind, path_glob, field_glob = parts
            if kind not in ALLOWLIST_KINDS:
                raise AllowlistError(f"{path}:{lineno}: unknown kind {kind!r}")
            entries.append((kind, path_glob, field_glob, reason))
    return entries


def is_allowed(entries, kind, path, field=None):
    for entry_kind, path_glob, field_glob, _reason in entries:
        if entry_kind != kind:
            continue
        if not fnmatch.fnmatch(path, path_glob):
            continue
        if kind == "META" and field_glob != "*" and field_glob != field:
            continue
        return True
    return False
