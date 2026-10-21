#!/usr/bin/env python3
"""Generate static redirects, including the Python wiki's legacy /moin/ URLs.

Reads _redirects.json and the current Python page inventory, then writes
HTML redirects into _redirects_html/. Sphinx regenerates these at build time
and copies them into its output via html_extra_path.

Usage:
    python scripts/gen_redirect_pages.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from os.path import relpath
from pathlib import Path, PurePosixPath
from urllib.parse import quote

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


def generate_redirects(root: Path, *, dry_run: bool = False) -> None:
    """Generate redirects without requiring the raw MoinMoin archive."""
    graph = json.loads((root / "_redirects.json").read_text())

    # /python/ was the migration's internal namespace; public links used /moin/.
    # Include surviving pages too, since unchanged names have no move entry.
    python_pages = {
        page.relative_to(root).with_suffix("").as_posix()
        for page in (root / "python").rglob("*.md")
        if "_attachments" not in page.parts
    }
    aliases = {
        f"moin/{source.removeprefix('python/')}": source
        for source in sorted(python_pages | {key for key in graph if key.startswith("python/")})
    }
    # Static hosts prefer a directory over its sibling .html file. A legacy
    # parent page must still reach its content, not a generated subpage listing.
    directories = {str(parent) for source in aliases for parent in PurePosixPath(source).parents}
    for source in list(aliases):
        if source in directories:
            aliases[f"{source}/index"] = source
    aliases["moin/index"] = "python/index"
    for source, target in aliases.items():
        graph.setdefault(source, target)
    redirects = resolve_chains(graph)

    out_dir = root / "_redirects_html"
    if not dry_run:
        if out_dir.exists():
            import shutil
            shutil.rmtree(out_dir)
        out_dir.mkdir()

    written = 0

    for src, dst in sorted(redirects.items()):
        # Normalize: src and dst are docnames like "python/foo"
        src_path = Path(f"{src}.html")
        dst_path = Path(f"{dst}.html")

        # Calculate relative URL from src's location to dst's location
        src_parent = src_path.parent
        rel = quote(str(PurePosixPath(relpath(dst_path, src_parent))), safe="/()")

        if dry_run:
            if written < 10:
                print(f"  {src_path} -> {rel}")
            written += 1
            continue

        out_file = out_dir / src_path
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(TEMPLATE.format(rel_url=rel))
        written += 1

    if dry_run:
        if written > 10:
            print(f"  ... and {written - 10} more")
        print(f"Would write {written} redirect files")
    else:
        print(f"Wrote {written} redirect files to {out_dir}/")


def _generate_for_sphinx(app) -> None:
    generate_redirects(Path(app.srcdir))


def setup(app):
    app.connect("builder-inited", _generate_for_sphinx)
    return {"parallel_read_safe": True, "parallel_write_safe": True}


def main() -> None:
    generate_redirects(Path.cwd(), dry_run="--dry-run" in sys.argv)



if __name__ == "__main__":
    main()
