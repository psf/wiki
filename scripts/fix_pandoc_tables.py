#!/usr/bin/env python3
"""Convert pandoc-only table markup left over from the MoinMoin migration.

The migration ran pandoc with its own Markdown dialect, which produced two
constructs MyST cannot render:

* ``::: {}`` fenced divs.  MyST reads them as a directive with an empty name
  and drops the whole block, so every table inside silently disappears.
* Pandoc simple, multiline and grid tables.  Outside a ``::: {}`` block they
  render as horizontal rules and run-together paragraphs.

This script unwraps the divs and rewrites the tables as GFM pipe tables (one
line per cell, with a header row) or MyST ``list-table`` directives
(multi-line cells, block content, or no header row).

Column positions cannot be trusted: ``strip_attrs.py`` removed ``{.http}``
style attributes *after* pandoc had aligned the columns, shifting text left by
a varying amount.  Without help, cells are assigned to columns heuristically.
Pass ``--raw-dir`` (the MoinMoin HTML export, ``RAW_DIR/<wiki>/<Page>.html``)
and each row is instead aligned word by word against the matching table in
the export, which resolves every row whose text agrees with it.

Usage:
    python scripts/fix_pandoc_tables.py [--raw-dir RAW_DIR] [--dry-run] [PATH ...]
    python scripts/fix_pandoc_tables.py --verify RAW_DIR [PATH ...]

``--verify`` compares every converted table cell by cell with the export and
prints one line per page that does not match.  It does not write files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from functools import cache
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIRS = ("python", "jython", "psf", "people")

DIV_OPEN = re.compile(r"^(?P<prefix>[ \t]*(?:(?:[-*+]|\d+[.)])[ \t]+)?)(?P<fence>:{3,})[ \t]*\{\}[ \t]*$")
SEG_RULE = re.compile(r"^[ \t]*-+(?: +-+)+[ \t]*$")
FULL_RULE = re.compile(r"^[ \t]*-{3,}[ \t]*$")
GRID_RULE = re.compile(r"^[ \t]*\+(?:[-=:]+\+)+[ \t]*$")
CODE_FENCE = re.compile(r"^[ \t]*(`{3,}|~{3,})")
NON_CODE_DIRECTIVE = re.compile(r"\{(?!code\}|code-block\}|sourcecode\}|raw\})[\w-]+\}")
# Pandoc attribute residue that strip_attrs.py skipped (preceded by a backtick).
# Between two code spans it splits one MoinMoin span: `a`{.backtick}`b` is `ab`.
ATTR_BETWEEN_SPANS = re.compile(r"`\{\.[\w-]+\}`")
ATTR_RESIDUE = re.compile(r"(?<=`)\{\.[\w-]+\}")
SEARCH_FORM = "Display context of search results"
LINK_TARGET = r"\((?:[^()\s]|\([^()]*\))*(?:\s+\"[^\"]*\")?\)"


@dataclass
class Table:
    rows: list[list[str]]
    header_rows: int = 0


@dataclass(frozen=True)
class Column:
    lo: int
    hi: int
    left: bool  # some line has text starting exactly at ``lo``


# --------------------------------------------------------------------------
# Text normalisation (shared by alignment and verification)
# --------------------------------------------------------------------------


def norm(s: str) -> str:
    """Letters and digits of the visible text of a Markdown or HTML fragment."""
    s = re.sub(r"!\[[^\]]*\]" + LINK_TARGET, "", s)
    s = re.sub(r"\]" + LINK_TARGET, "]", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[^0-9a-z]", "", s.lower())


# --------------------------------------------------------------------------
# Guidance from the MoinMoin export
# --------------------------------------------------------------------------


class _HTMLTables(HTMLParser):
    """Collect the text of every table cell inside ``<div id="content">``."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[str]]] = []
        self.stack: list[list[list[str]]] = []
        self.cell: list[str] | None = None
        self.span = 1
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "div" and (self.depth or a.get("id") == "content"):
            self.depth += 1
        if not self.depth:
            return
        if tag == "table":
            self.stack.append([])
        elif tag == "tr" and self.stack:
            self.stack[-1].append([])
        elif tag in ("td", "th") and self.stack:
            self.cell = []
            self.span = int(a.get("colspan") or 1)

    def handle_endtag(self, tag):
        if not self.depth:
            return
        if tag == "div":
            self.depth -= 1
        elif tag in ("td", "th") and self.cell is not None and self.stack:
            self.stack[-1][-1].append("".join(self.cell))
            self.stack[-1][-1].extend([""] * (self.span - 1))
            self.cell = None
        elif tag == "table" and self.stack:
            self.tables.append(self.stack.pop())

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)


def _squash(s: str) -> str:
    return "".join(s.split()).lower()


def export_tables(paths: list[Path], key=norm) -> list[list[list[str]]]:
    """Tables of a page's MoinMoin export(s), cell text passed through ``key``."""
    out = []
    for p in paths:
        parser = _HTMLTables()
        parser.feed(p.read_text(errors="replace"))
        out += [[[key(c) for c in r] for r in t] for t in parser.tables]
    return out


class Guide:
    """Looks up export rows by their text to align cells against them."""

    def __init__(self, paths: list[Path]) -> None:
        # A row's concatenated text does not depend on how its words are
        # split into cells, so it identifies the export row.
        self.rows: dict[str, list[tuple[list[str], list[str]]]] = {}
        for t, raw in zip(export_tables(paths), export_tables(paths, key=_squash), strict=True):
            for r, rr in zip(t, raw, strict=True):
                self.rows.setdefault("".join(r), []).append((r, rr))

    def targets(self, group: list[str], ncols: int) -> list[tuple[list[str], list[str]]]:
        found = self.rows.get(norm(" ".join(group)), [])
        pad = [""] * ncols
        return [(r + pad[len(r) :], rr + pad[len(rr) :]) for r, rr in found if len(r) <= ncols]


def align(group: list[str], target: list[str], raw: list[str]) -> list[str] | None:
    """Assign the words of one table row (one or more lines) to cells so the
    text of each cell matches ``target`` (normalised export cell text).

    ``raw`` is the export cell text with only whitespace removed.  It places
    punctuation-only words such as ``?`` (invisible to ``norm``) in the cell
    that shows them, and requires every non-empty export cell to get a word.
    """
    lines = [re.findall(r"\S+", ln) for ln in group]
    words = [[norm(w) for w in ws] for ws in lines]
    n = len(target)

    def punct(w: str) -> str | None:
        if norm(w) or "](" in w:
            return None
        return re.sub(r"[\\*`]", "", w).lower() or None

    puncts = [[punct(w) for w in ws] for ws in lines]

    @cache
    def solve(li: int, wi: int, col: int, filled: tuple[int, ...], used: tuple[bool, ...]) -> tuple | None:
        if li == len(lines):
            done = all(filled[k] == len(target[k]) and (used[k] or not raw[k]) for k in range(n))
            return () if done else None
        if wi == len(lines[li]):
            rest = solve(li + 1, 0, -1, filled, used)
            return None if rest is None else ((li, None), *rest)
        w, p = words[li][wi], puncts[li][wi]
        # Stay in the current cell first, then try each later cell.
        for k in ([col] if col >= 0 else []) + list(range(col + 1, n)):
            end = filled[k] + len(w)
            if target[k][filled[k] : end] != w or (p and p not in raw[k]):
                continue
            rest = solve(li, wi + 1, k, (*filled[:k], end, *filled[k + 1 :]), (*used[:k], True, *used[k + 1 :]))
            if rest is not None:
                return ((li, k), *rest)
        return None

    plan = solve(0, 0, -1, (0,) * n, (False,) * n)
    solve.cache_clear()
    if plan is None:
        return None
    parts: list[list[list[str]]] = [[[] for _ in lines] for _ in range(n)]
    it = iter(plan)
    for li, ws in enumerate(lines):
        for w in ws:
            _, k = next(it)
            parts[k][li].append(w)
        next(it)  # end-of-line marker
    return [_join_lines([" ".join(p) for p in parts[k]]) for k in range(n)]


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _spans(rule: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in re.finditer(r"-+", rule)]


def _columns(rule: str, lines: list[str]) -> list[Column]:
    def starts_at(line: str, pos: int) -> bool:
        return pos < len(line) and line[pos] != " " and (pos == 0 or line[pos - 1] == " ")

    return [Column(lo, hi, any(starts_at(ln, lo) for ln in lines)) for lo, hi in _spans(rule)]


def _assign(line: str, cols: list[Column]) -> list[str]:
    """Heuristically split one table line into cells.

    Text may have moved left since layout, by an amount that never decreases
    along the line.  Runs of text separated by two or more spaces are cells.
    A left-aligned column takes a cell that starts at or before its original
    start; a centred or right-aligned column takes any cell that fits inside
    it.  A cell is split at a single space when the next word lines up exactly
    with a later column's start.
    """
    segments: list[list[tuple[int, int, str]]] = []
    for m in re.finditer(r"\S+", line):
        w = (m.start(), m.end(), m.group())
        if segments and w[0] - segments[-1][-1][1] < 2:
            segments[-1].append(w)
        else:
            segments.append([w])

    cells = [""] * len(cols)
    col, shift, last = -1, 0, len(cols) - 1
    while segments:
        seg = segments.pop(0)
        for k, (ws, _, _) in enumerate(seg[1:], 1):
            if any(c.left and c.lo == ws + shift for c in cols[col + 2 :]):
                segments.insert(0, seg[k:])
                seg = seg[:k]
                break
        s, e = seg[0][0], seg[-1][1]
        for j in range(col + 1, len(cols)):
            c = cols[j]
            if j == last:
                d = max(shift, c.lo - s)
            elif c.left:
                d = c.lo - s
                if d < shift or e + d > c.hi:
                    continue
            else:
                d = max(shift, c.lo - s)
                if e + d > c.hi:
                    continue
            col, shift = j, d
            break
        else:
            col = max(col, 0)
        text = " ".join(w[2] for w in seg)
        cells[col] = f"{cells[col]} {text}" if cells[col] else text
    return cells


def _join_lines(parts: list[str]) -> str:
    """Join the lines of one cell; a trailing backslash is a hard line break."""
    out = ""
    for p in parts:
        if not p:
            continue
        if not out:
            out = p
        elif out.endswith("\\"):
            out = out[:-1].rstrip() + "<br>" + p
        else:
            out += " " + p
    return out.removesuffix("\\").rstrip()


def _groups(lines: list[str], multiline: bool) -> list[list[str]]:
    """Lines of each row: one line per row, or blank-line separated rows."""
    if not multiline:
        return [[ln] for ln in lines]
    groups, cur = [], []
    for ln in [*lines, ""]:
        if ln.strip():
            cur.append(ln)
        elif cur:
            groups.append(cur)
            cur = []
    return groups


def _rows(groups: list[list[str]], cols: list[Column], guide: Guide | None) -> list[list[str]]:
    rows = [[_join_lines(list(p)) for p in zip(*(_assign(ln, cols) for ln in g), strict=False)] for g in groups]
    if not guide:
        return rows
    for r, g in enumerate(groups):
        targets = guide.targets(g, len(cols))
        # Keep the heuristic split when it already agrees with an export row:
        # same text per cell, and no visible export cell left empty.
        if any(
            [norm(c) for c in rows[r]] == t and all(c or not rw for c, rw in zip(rows[r], raw, strict=True))
            for t, raw in targets
        ):
            continue
        rows[r] = next((a for t, raw in targets if (a := align(g, t, raw))), rows[r])
    return rows


def parse_dash_table(lines: list[str], i: int, guide: Guide | None) -> tuple[Table, int, int] | None:
    """Parse a simple/multiline table whose segmented rule is at ``lines[i]``.

    Returns (table, first_line, end_line_exclusive) or None.
    """
    rule = lines[i]
    prev = lines[i - 1] if i > 0 else ""

    if prev.strip() and not SEG_RULE.match(prev):
        # Header above the rule.
        top = i - 1
        while top > 0 and lines[top - 1].strip() and not FULL_RULE.match(lines[top - 1]):
            top -= 1
        if top > 0 and FULL_RULE.match(lines[top - 1]):
            # Multiline table with header: full rule, header, seg rule, rows, full rule.
            j = i + 1
            while j < len(lines) and not FULL_RULE.match(lines[j]):
                j += 1
            if j == len(lines):
                return None
            cols = _columns(rule, lines[top:j])
            groups = [lines[top:i], *_groups(lines[i + 1 : j], multiline=True)]
            return Table(_rows(groups, cols, guide), 1), top - 1, j + 1
        if top != i - 1:
            return None
        # Simple table with one header line; rows run to a blank line.
        j = i + 1
        while j < len(lines) and lines[j].strip():
            j += 1
        body_end = j - 1 if FULL_RULE.match(lines[j - 1]) or SEG_RULE.match(lines[j - 1]) else j
        body = lines[i + 1 : body_end]
        cols = _columns(rule, [prev, *body])
        return Table(_rows([[prev], *_groups(body, multiline=False)], cols, guide), 1), i - 1, j

    # Headerless: rows until the matching closing rule.
    spans = _spans(rule)
    j = i + 1
    while j < len(lines) and not (SEG_RULE.match(lines[j]) and _spans(lines[j]) == spans):
        if GRID_RULE.match(lines[j]):
            return None
        j += 1
    if j == len(lines):
        return None
    body = lines[i + 1 : j]
    cols = _columns(rule, body)
    groups = _groups(body, multiline=any(not ln.strip() for ln in body))
    return Table(_rows(groups, cols, guide)), i, j + 1


def parse_single_column(lines: list[str], i: int) -> tuple[Table, int, int] | None:
    """One-column headerless table (only recognised inside a ``::: {}`` block)."""
    j = i + 1
    while j < len(lines) and not FULL_RULE.match(lines[j]):
        j += 1
    if j == len(lines):
        return None
    body = lines[i + 1 : j]
    groups = _groups(body, multiline=any(not ln.strip() for ln in body))
    return Table([[_join_lines([ln.strip() for ln in g])] for g in groups]), i, j + 1


def _split_grid_line(line: str) -> list[str]:
    inner = line.strip()
    inner = inner[1:-1] if inner.endswith("|") else inner[1:]
    return re.split(r"(?<=\s)\|(?=\s)", " " + inner + " ")


def parse_grid_table(lines: list[str], i: int) -> tuple[Table, int, int] | None:
    ncols = lines[i].strip().count("+") - 1
    rows: list[list[str]] = []
    header_rows = 0
    current: list[list[str]] = [[] for _ in range(ncols)]
    j = i + 1
    while j < len(lines):
        s = lines[j].strip()
        if GRID_RULE.match(lines[j]):
            rows.append(["\n".join(c).strip("\n") for c in current])
            if "=" in s:
                header_rows = len(rows)
            current = [[] for _ in range(ncols)]
            j += 1
            if j >= len(lines) or not lines[j].strip().startswith("|"):
                break
            continue
        if not s.startswith("|"):
            return None
        if re.search(r"\+[-=:]{3,}", s):
            return None  # row span: a partial border inside a row
        parts = _split_grid_line(lines[j])
        if len(parts) > ncols:
            return None
        # Column span: fewer cells than columns. Keep text in the first cell.
        parts += [" "] * (ncols - len(parts))
        for k, p in enumerate(parts):
            current[k].append(p[1:].rstrip() if p.startswith(" ") else p.rstrip())
        j += 1
    else:
        return None
    for row in rows:
        for k, cell in enumerate(row):
            ls = cell.split("\n")
            pad = min((_indent(ln) for ln in ls if ln.strip()), default=0)
            row[k] = "\n".join(ln[pad:] for ln in ls).strip("\n")
    return Table(rows, header_rows), i, j


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


BOLD_CELL = re.compile(r"\*\*(?P<text>[^*\n](?:.*[^*\n])?)\*\*(?P<tail>[?:.]?)")


def _is_bold(cell: str) -> bool:
    """A bold label, possibly followed by MoinMoin's ``?`` (missing page)."""
    return not cell or bool(BOLD_CELL.fullmatch(cell))


def render(table: Table) -> list[str]:
    rows = [[ATTR_RESIDUE.sub("", ATTR_BETWEEN_SPANS.sub("", c)) for c in r] for r in table.rows]
    if not rows:
        return []
    multiline = any("\n" in c for r in rows for c in r)
    # list-table rejects a header that leaves no body rows.
    header_rows = min(table.header_rows, len(rows) - 1)
    if not header_rows and len(rows) > 1 and any(rows[0]) and all(_is_bold(c) for c in rows[0]):
        header_rows = 1
        rows[0] = [BOLD_CELL.sub(r"\g<text>\g<tail>", c) for c in rows[0]]
    if not multiline and header_rows == 1 and len(rows) > 1:
        return _render_pipe(rows)
    return _render_list_table(rows, header_rows)


def _pipe_cell(c: str) -> str:
    return re.sub(r"(?<!\\)\|", r"\\|", c)


def _render_pipe(rows: list[list[str]]) -> list[str]:
    out = ["| " + " | ".join(_pipe_cell(c) for c in rows[0]) + " |"]
    out.append("|" + "|".join("---" for _ in rows[0]) + "|")
    out += ["| " + " | ".join(_pipe_cell(c) for c in r) + " |" for r in rows[1:]]
    return out


def _render_list_table(rows: list[list[str]], header_rows: int) -> list[str]:
    longest = max((len(m.group()) for r in rows for c in r for m in re.finditer(r"`{3,}", c)), default=2)
    fence = "`" * max(3, longest + 1)
    out = [fence + "{list-table}"]
    if header_rows:
        out.append(f":header-rows: {header_rows}")
    out.append("")
    for r in rows:
        for k, cell in enumerate(r):
            lead = "* - " if k == 0 else "  - "
            ls = cell.split("\n") if cell else [""]
            out.append((lead + ls[0]).rstrip())
            out += [("    " + ln).rstrip() for ln in ls[1:]]
    out.append(fence)
    return out


# --------------------------------------------------------------------------
# Document rewriting
# --------------------------------------------------------------------------


def convert_tables(lines: list[str], in_div: bool, guide: Guide | None) -> tuple[list[str], int]:
    """Rewrite every pandoc table in ``lines``; code blocks are left alone."""
    out: list[str] = []
    count = 0
    i = 0
    fence: str | None = None
    directives: list[str] = []  # open ```{name} fences; their bodies are Markdown
    while i < len(lines):
        line = lines[i]
        m = CODE_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and line.strip() == m.group(1):
                fence = None
            out.append(line)
            i += 1
            continue
        if m:
            ticks = m.group(1)
            if directives and line.strip() == directives[-1]:
                directives.pop()
            elif NON_CODE_DIRECTIVE.match(line.strip()[len(ticks) :]):
                directives.append(ticks)
            else:
                fence = ticks
            out.append(line)
            i += 1
            continue

        parsed = None
        if not in_div and _indent(line) >= 4:
            pass  # indented code block: preformatted text, not a pandoc table
        elif GRID_RULE.match(line):
            parsed = parse_grid_table(lines, i)
        elif SEG_RULE.match(line):
            parsed = parse_dash_table(lines, i, guide)
        elif in_div and FULL_RULE.match(line) and i + 1 < len(lines) and lines[i + 1].strip():
            parsed = parse_single_column(lines, i)
        if not parsed:
            out.append(line)
            i += 1
            continue
        table, start, end = parsed
        if i > start:  # header lines above the rule were already emitted
            del out[len(out) - (i - start) :]
        ind = "" if in_div else " " * min(_indent(ln) for ln in lines[start:end] if ln.strip())
        out += [(ind + ln).rstrip() if ln else ln for ln in render(table)]
        count += 1
        i = end
    return out, count


def unwrap_divs(lines: list[str], guide: Guide | None) -> tuple[list[str], int, int]:
    """Replace each ``::: {}`` block with its (converted) body."""
    out: list[str] = []
    divs = tables = 0
    i = 0
    while i < len(lines):
        m = DIV_OPEN.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        prefix, fence = m.group("prefix"), m.group("fence")
        width = len(prefix.expandtabs())
        closer = re.compile(r"^" + " " * width + re.escape(fence) + r"[ \t]*$")
        j = i + 1
        while j < len(lines) and not closer.match(lines[j]):
            j += 1
        body = [ln[width:] if ln[:width].strip() == "" else ln for ln in lines[i + 1 : j]]
        body, inner_divs, inner_tables = unwrap_divs(body, guide)
        body, n = convert_tables(body, in_div=True, guide=guide)
        divs += 1 + inner_divs
        tables += n + inner_tables
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        if not body or SEARCH_FORM in "\n".join(body):
            # Empty, or MoinMoin search-form chrome that was never content.
            if prefix.strip():
                out.append(prefix.rstrip())
        else:
            out.append((prefix + body[0]).rstrip())
            out += [(" " * width + ln).rstrip() if ln.strip() else "" for ln in body[1:]]
        i = j + 1
    return out, divs, tables


def fix_text(text: str, guide: Guide | None = None) -> tuple[str, int, int]:
    lines = text.split("\n")
    lines, divs, div_tables = unwrap_divs(lines, guide)
    lines, tables = convert_tables(lines, in_div=False, guide=guide)
    return "\n".join(lines), divs, div_tables + tables


# --------------------------------------------------------------------------
# Locating exports and verifying the result
# --------------------------------------------------------------------------


class Exports:
    """Map current page paths to their MoinMoin HTML export file(s)."""

    def __init__(self, raw_dir: Path) -> None:
        self.raw_dir = raw_dir
        self.index: dict[str, list[Path]] = {}
        redirects = json.loads((ROOT / "_redirects.json").read_text())
        for old, new in redirects.items():
            p = raw_dir / (old + ".html")
            if p.exists():
                self.index.setdefault(new, []).append(p)

    def for_page(self, path: Path) -> list[Path]:
        rel = path.relative_to(ROOT).with_suffix("").as_posix()
        if rel in self.index:
            return self.index[rel]
        if not rel.startswith("people/"):
            return []
        # people/X/First Last[/Sub] were merged from per-wiki user pages.
        parts = rel.split("/")[2:]
        if parts and parts[-1] == "index":
            parts = parts[:-1]
        found = []
        for joiner in ("", "(20)"):
            stem = "(2f)".join(p.replace(" ", joiner) for p in parts)
            found += [p for w in ("python", "jython", "psf") if (p := self.raw_dir / w / f"{stem}.html").exists()]
        return found


def _md_tables(text: str) -> list[list[list[str]]]:
    """Cells of the tables this script renders (pipe and list-table)."""
    tables: list[list[list[str]]] = []
    lines = text.split("\n")
    sep = re.compile(r"\|(?:---\|)+")
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("| ") and i + 1 < len(lines) and sep.fullmatch(lines[i + 1].strip()):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not sep.fullmatch(lines[i].strip()):
                    rows.append(re.split(r"(?<!\\)\|", lines[i].strip()[1:-1]))
                i += 1
            tables.append(rows)
            continue
        m = re.match(r"^(\s*(?:[-*+]\s+)?)(`{3,})\{list-table\}", lines[i])
        if m:
            base, fence, rows = len(m.group(1)), m.group(2), []
            i += 1
            while i < len(lines) and lines[i].strip() != fence:
                ln, t = lines[i], lines[i].strip()
                # Row and cell markers sit at the table's own indentation;
                # deeper "- " lines are lists inside a cell.
                if _indent(ln) == base and (t.startswith("* - ") or t == "* -"):
                    rows.append([t[4:]])
                elif _indent(ln) == base + 2 and (t.startswith("- ") or t == "-"):
                    rows[-1].append(t[2:])
                elif rows and t and not t.startswith(":"):
                    rows[-1][-1] += " " + t
                i += 1
            tables.append(rows)
        i += 1
    return tables


def verify(path: Path, exports: Exports) -> str | None:
    raws = exports.for_page(path)
    if not raws:
        return "no raw export found"

    def rows(table: list[list[str]]) -> list[list[str]]:
        # Ragged export rows omit trailing empty cells; so do empty rows.
        out = []
        for r in table:
            while r and not r[-1]:
                r = r[:-1]
            if r:
                out.append(r)
        return out

    md = [rows([[norm(c) for c in row] for row in t]) for t in _md_tables(path.read_text())]
    problems = []
    for raw in raws:
        html = [rows(t) for t in export_tables([raw])]
        if md == html:
            return None
        if len(md) != len(html):
            problems.append(f"{raw.name}: {len(md)} tables vs {len(html)} in export")
            continue
        for ti, (a, b) in enumerate(zip(md, html, strict=False)):
            if a == b:
                continue
            row = next((ri for ri, (ra, rb) in enumerate(zip(a, b, strict=False)) if ra != rb), None)
            if row is None:
                problems.append(f"{raw.name}: table {ti + 1}: {len(a)} rows vs {len(b)}")
            else:
                problems.append(f"{raw.name}: table {ti + 1} row {row + 1}: {a[row]} != {b[row]}")
            break
    return "; ".join(problems)


# --------------------------------------------------------------------------


def iter_pages(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p).resolve() for p in paths]
    return sorted(p for d in WIKI_DIRS for p in (ROOT / d).rglob("*.md"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--raw-dir", type=Path, help="MoinMoin HTML export used to align cells")
    ap.add_argument("--verify", metavar="RAW_DIR", type=Path, help="compare converted tables with the export")
    args = ap.parse_args()

    pages = iter_pages(args.paths)
    if args.verify:
        exports = Exports(args.verify.resolve())
        bad = 0
        for p in pages:
            if not _md_tables(p.read_text()):
                continue
            problem = verify(p, exports)
            if problem:
                bad += 1
                print(f"{p.relative_to(ROOT)}\t{problem}")
        print(f"{bad} page(s) differ from the export", file=sys.stderr)
        sys.exit(1 if bad else 0)

    exports = Exports(args.raw_dir.resolve()) if args.raw_dir else None
    changed = divs = tables = 0
    for p in pages:
        text = p.read_text(encoding="utf-8")
        if "::: {}" not in text and not re.search(r"^[ \t]*(?:-+ +-|\+[-=:]{3,}\+)", text, re.M):
            continue
        guide = Guide(exports.for_page(p)) if exports else None
        new, d, t = fix_text(text, guide)
        if new != text:
            changed += 1
            divs += d
            tables += t
            if not args.dry_run:
                p.write_text(new, encoding="utf-8")
    verb = "Would rewrite" if args.dry_run else "Rewrote"
    print(f"{verb} {changed} page(s): {divs} ::: {{}} block(s) unwrapped, {tables} table(s) converted")


if __name__ == "__main__":
    main()
