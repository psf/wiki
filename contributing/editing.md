# Editing Wiki Pages

### On GitHub

The most straightforward path. Every wiki page is a `.md` file under one of three directories:

- `python/` -- the main Python wiki (3,274 pages)
- `psf/` -- Python Software Foundation governance and programs (378 pages)
- `jython/` -- Jython, the JVM implementation (433 pages)

Find the file you want to change, edit it, and open a pull request. GitHub's web editor works fine for quick fixes. For anything more involved, clone the repo and work locally (see [Local Development](development.md) for setup instructions).

Pages use MyST Markdown, which is standard Markdown plus a handful of Sphinx directives. You can use `{admonition}`, `{toctree}`, `{grid}`, code blocks, tables -- all the usual stuff. The [MyST docs](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html) cover the full syntax.

#### Adding a new page

1. Create a `.md` file in the right directory. Start it with a top-level heading (`# Page Title`).
2. Add the filename (without `.md`) to the `{toctree}` in the parent `index.md`.

If you're making a new subdirectory, put an `index.md` inside it with its own toctree, then reference `subdir/index` from the parent.

#### Page format

Pages migrated from MoinMoin have a legacy notice at the top. You can remove it if you're substantially rewriting the content. New pages don't need one.

The notice's opening fence must be `` ```{admonition} Legacy Wiki Page ``. Putting `{admonition}` inside a `plain` code block displays the directive literally instead of rendering the notice.

A minimal page looks like:

```markdown
## My Page Title

Content goes here. Standard Markdown works -- links, lists, code blocks, tables.

Use [MyST directives](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)
when you need admonitions, toctrees, or tab panels.
```

#### What about redirects?

The old MoinMoin wiki encoded special characters in URLs in its own way -- spaces became `(20)`, slashes became `(2f)`, German umlauts like `Ä` became `(c384)`. All 5,400+ redirects from old URLs to new paths live in `_redirects.json`.

If you move or rename a page, add an entry there so existing links don't break. You can regenerate the full redirect map with:

```bash
make redirects
```

### On GitHub with CMS

For people who'd rather not touch Git directly, there's a browser-based editor at `/edit/` on the live site, also linked from the **Contribute** menu. It's powered by [Sveltia CMS](https://sveltiacms.app/).

You log in with your GitHub account, pick a page from any of the three wiki sections, edit it in a rich-text-ish Markdown editor, and save. Each wiki section is shown as a folder tree, and new pages get a folder picker so you can choose where they go and a **Slug** field for the file name. Existing pages can't be renamed from the CMS, since moving a page needs a redirect (see above). Saving commits the change straight to `main` -- there's no pull request or review step -- so the CMS only works for accounts with write access to `psf/wiki`. Everyone else should use the pull request flow above.

The CMS configuration lives in `_extra/edit/config.yml` and defines three collections, one per wiki section. The Sveltia version is pinned in `_extra/edit/index.html`; when you bump it, load `/edit/` once to check for new configuration errors.

### Without GitHub

:::{admonition} Work in progress
:class: warning

We're looking into options for allowing edits without requiring a GitHub account at all. The current CMS flow and the standard PR workflow both need one. If you have content to contribute but no GitHub account, reach out to the PSF or open an issue and we'll figure something out.
:::
