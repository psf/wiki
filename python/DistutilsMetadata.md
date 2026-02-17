# DistutilsMetadata

::: {#content dir="ltr" lang="en"}
Describe DistutilsMetadata here.

= See also =

See cabal (the \"haskell distutils\") for an example

[http://www.haskell.org/cabal/release/cabal-latest/doc/users-guide/authors.html#pkg-descr](http://www.haskell.org/cabal/release/cabal-latest/doc/users-guide/authors.html#pkg-descr){.http}

There is a setup.hs to drive the build/installation, and a .cabal file for the metadata. It looks like simple packages can get away with only the simple, static .cabal file + a trivial setup.hs. For things which cannot be defined statically (system dependent options, etc\...), there are hooks, which are implemented in setup.hs.
:::
