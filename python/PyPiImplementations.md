# PyPiImplementations

:::: {#content dir="ltr" lang="en"}
The goal of this page is to list alternatives to the [reference implementation](CheeseShopDev), since it\'s quite hard to find them in any index (most hits will be about packages available *in* the package index, not *about* it).

::: table-of-contents
Contents

1.  [Full implementations](#Full_implementations)
2.  [Mirrors / Proxies](#Mirrors_.2F_Proxies)
3.  [Tools / Extensions](#Tools_.2F_Extensions)
4.  [Simple repository with fallback using Apache](#Simple_repository_with_fallback_using_Apache)
5.  [Things that would be nice](#Things_that_would_be_nice)
:::

## Full implementations {#Full_implementations}

Applications that implement the [Package Index API](http://peak.telecommunity.com/DevCenter/EasyInstall#package-index-api){.http}:

- [PyPI](CheeseShopDev) (aka [CheeseShop](CheeseShop)) - The reference implementation, powering the main index.

- [chishop](https://github.com/ask/chishop){.https} and its more recent [djangopypi](https://github.com/benliles/djangopypi){.https} fork - django based

- [Plone Software Center](https://pypi.python.org/pypi/Products.PloneSoftwareCenter){.https}

- [pypiserver](http://pypi.python.org/pypi/pypiserver){.http} - minimal pypi server, easy to install & use

- [Warehouse](https://pypi.python.org/pypi/warehouse){.https} Next Generation Python Package Repository

- [GitLab](https://docs.gitlab.com/ee/user/packages/pypi_repository/){.https} implements a PyPI compatible package repository/registry that can also proxy to [pypi.org](https://pypi.org/){.https}

Less maintained:

- [ClueReleaseManager](http://pypi.python.org/pypi/ClueReleaseManager){.http} - link to project page is broken, last release in 2009

- [EggBasket](http://chrisarndt.de/projects/eggbasket/){.http} - A simple, lightweight Python Package Index (aka Cheeseshop) clone.

- [haufe.eggserver](http://pypi.python.org/pypi/haufe.eggserver){.http} - Grok-based local repository with upload and no security model.

## Mirrors / Proxies {#Mirrors_.2F_Proxies}

- [z3c.pypimirror](http://www.openplans.org/projects/pypi-mirroring/project-home){.http}

## Tools / Extensions {#Tools_.2F_Extensions}

- [iw.dist](http://pypi.python.org/pypi/iw.dist/){.http} - Extension that implements the [EnhancedPyPI](EnhancedPyPI) changes to `.pypirc`{.backtick}.

## Simple repository with fallback using Apache {#Simple_repository_with_fallback_using_Apache}

The following implements two local repositories that fall back to PyPI for packages that have no local override. \"dev\" is for development snapshots and open for all developers, \"stable\" is only writable by the QC team. Note that creating a local copy of a package shadows *all* versions in PyPI, since the index page is then generated locally and does not include the versions found on PyPI.

httpd.conf

:   # Mount pypi repositories into URI space
        Alias /pypi   /var/pypi

        # /pypi/dev: Redirect for unknown packages (fallback to pypi)
        RewriteCond   /var/pypi/dev/$1 !-d
        RewriteCond   /var/pypi/dev/$1 !-f
        RewriteRule   ^/pypi/dev/([^/]+)/?$ http://pypi.python.org/pypi/$1/ [R,L]

        RewriteCond   /var/pypi/dev/$1/$2 !-f
        RewriteRule   ^/pypi/dev/([^/]+)/([^/]+)$ http://pypi.python.org/pypi/$1/$2 [R,L]

        # /pypi/stable: Redirect for unknown packages (fallback to pypi)
        RewriteCond   /var/pypi/stable/$1 !-d
        RewriteCond   /var/pypi/stable/$1 !-f
        RewriteRule   ^/pypi/stable/([^/]+)/?$ http://pypi.python.org/pypi/$1/ [R,L]

        RewriteCond   /var/pypi/stable/$1/$2 !-f
        RewriteRule   ^/pypi/stable/([^/]+)/([^/]+)$ http://pypi.python.org/pypi/$1/$2 [R,L]

These rules assume the RewriteEngine is switched on, and that directory index generation is enabled.

## Things that would be nice {#Things_that_would_be_nice}

- A local PyPI repository that also allows to proxy / cache external repositories
  - needed in enterprise environments

  - mix and match proprietary and public packages

  - no need for an always-up internet connection (just mostly-up)

  - auditable, repeatable releases (you have a local copy of any package you ever put into production)

  - compare to usual Maven proxies from Java land \-- they have these features

  - unlike [EnhancedPyPI](EnhancedPyPI), puts multi-repo support into the index and thus works with any compliant software w/o change

------------------------------------------------------------------------

[CategoryDevelopmentProcess](CategoryDevelopmentProcess)
::::
