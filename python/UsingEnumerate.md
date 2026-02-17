# UsingEnumerate

::::: {#content dir="ltr" lang="en"}
**`enumerate`** is easy to use:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-17a52fe6d6ab26dc8dadeba71d70d36fb7149206 dir="ltr" lang="en"}
   1 for index, character in enumerate("hello"):
   2   print "#%d: %s" % (index, character)
```
:::
::::

\...which prints out:

    #0: h
    #1: e
    #2: l
    #3: l
    #4: o

You can use it on just about any iterable sequence.
:::::
