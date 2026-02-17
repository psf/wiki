#!/usr/bin/env python3
"""Generate static HTML redirect pages from _redirects.json.

Reads the redirect mapping and writes simple HTML files with meta refresh
tags into _redirects_html/. Sphinx copies these into the build output via
html_extra_path, so no build-time extension is needed.

Usage:
    python scripts/gen_redirect_pages.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from os.path import relpath
from pathlib import Path, PurePosixPath

TEMPLATE = """\
<html>
    <head>
        <noscript>
            <meta http-equiv="refresh" content="0; url={rel_url}"/>
        </noscript>
    </head>
    <body>
        <script>
            window.location.href = '{rel_url}' + (window.location.search || '') + (window.location.hash || '');
        </script>
        <p>You should have been redirected.</p>
        <a href="{rel_url}">If not, click here to continue.</a>
    </body>
</html>
"""


def resolve_chains(graph: dict[str, str]) -> dict[str, str]:
    """Follow redirect chains so A->B->C becomes A->C, B->C."""
    resolved = {}
    for src in graph:
        visited = []
        node = src
        while node in graph:
            if node in visited:
                print(f"  WARNING: circular redirect: {' -> '.join(visited + [node])}")
                break
            visited.append(node)
            node = graph[node]
        for v in visited:
            resolved[v] = node
    return resolved


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    redirects_file = Path("_redirects.json")
    if not redirects_file.exists():
        print("No _redirects.json found")
        raise SystemExit(1)

    graph = json.loads(redirects_file.read_text())
    redirects = resolve_chains(graph)

    out_dir = Path("_redirects_html")
    if not dry_run:
        if out_dir.exists():
            import shutil
            shutil.rmtree(out_dir)
        out_dir.mkdir()

    written = 0
    skipped = 0

    for src, dst in sorted(redirects.items()):
        src_html = Path(src).with_suffix("") / ".." / Path(src).stem
        # Normalize: src and dst are docnames like "python/foo"
        src_path = Path(f"{src}.html")
        dst_path = Path(f"{dst}.html")

        # Calculate relative URL from src's location to dst's location
        src_parent = src_path.parent
        rel = PurePosixPath(relpath(dst_path, src_parent))

        if dry_run:
            if written < 10:
                print(f"  {src_path} -> {rel}")
            written += 1
            continue

        out_file = out_dir / src_path
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(TEMPLATE.format(rel_url=str(rel)))
        written += 1

    if dry_run:
        if written > 10:
            print(f"  ... and {written - 10} more")
        print(f"Would write {written} redirect files")
    else:
        print(f"Wrote {written} redirect files to {out_dir}/")


if __name__ == "__main__":
    main()
