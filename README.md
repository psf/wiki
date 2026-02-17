# The [Python Wiki](https://wiki.python.org)

A Sphinx-based rebuild of the Python community wiki, migrated from the old MoinMoin installation.
Three wiki sections live here: **python**, **psf**, and **jython**.

## Setup

You'll need [uv](https://docs.astral.sh/uv/) and Python 3.14+.

```bash
make install
```

That's it. No virtualenv management, no pip — uv handles everything.

## Contributing

All content lives as Markdown files under `python/`, `psf/`, and `jython/`. Each section has its own `index.md` with a toctree. Subdirectories group related pages (workgroups, conferences, etc.) and have their own `index.md` files too.

To edit a page, find the `.md` file and change it directly. The format is [MyST Markdown](https://myst-parser.readthedocs.io/) — standard Markdown plus a few Sphinx directives like `{toctree}` and `{admonition}`.

### Previewing your changes

The wiki has ~3500 pages across all three sections, so a full build takes a while. You almost certainly don't need to build everything.

**Build just the section you're working on:**

```bash
# PSF wiki only (~400 pages, builds in under a minute)
make docs-serve-fast WIKI=psf

# Jython wiki only (~460 pages)
make docs-serve-fast WIKI=jython

# Python wiki (~3400 pages — still the big one)
make docs-serve-fast WIKI=python
```

**Build a single subsection** when you're focused on one area:

```bash
# Just the Packaging WG pages (~113 pages, builds in seconds)
make docs-serve-fast WIKI=psf SECTION=PackagingWG

# Just the Advocacy section
make docs-serve-fast WIKI=python SECTION=Advocacy

# Just the Summer of Code pages
make docs-serve-fast WIKI=python SECTION=SummerOfCode
```

Both commands start a live-reload server — save a file and the browser refreshes automatically.

**Full build** (all sections, for CI or final checks):

```bash
make docs
```

### Adding a new page

1. Create a `.md` file in the right directory
2. Add it to the parent `index.md` toctree
3. Start the file with a top-level heading (`# Page Title`)

If you're creating a new subdirectory, add an `index.md` inside it with a toctree listing its pages, then reference that `subdir/index` from the parent toctree.

### Page format

Pages migrated from MoinMoin have a legacy notice at the top — you can remove it if you're substantially rewriting the content. New pages don't need one.

A minimal page looks like:

```markdown
# My Page Title

Content goes here. Standard Markdown works — links, lists, code blocks, tables.

Use [MyST directives](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)
when you need admonitions, toctrees, or tab panels.
```

## Other make targets

```
make help             Show all available targets
make sync             Pull raw HTML from the wiki server
make convert          Re-run the MoinMoin-to-Markdown conversion
make lint             Run pre-commit hooks
make clean            Remove all build artifacts
make docs-clean       Remove just the Sphinx build output
```

## Project structure

```
python/               Python wiki content
psf/                  PSF wiki content
jython/               Jython wiki content
scripts/              Conversion and maintenance scripts
  convert.py          MoinMoin HTML → MyST Markdown converter
  strip_attrs.py      Strips pandoc attribute syntax from .md files
_templates/           Sphinx HTML templates
_static/              CSS and static assets
conf.py               Sphinx configuration
```
