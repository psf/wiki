# Py3kConversionTools

::: {#content dir="ltr" lang="en"}
Converting Python 2.x code to Python 3.x code

------------------------------------------------------------------------

Since Python 2.6, Python has include a standard tool 2to3 to assist in the conversion. [http://docs.python.org/library/2to3.html](http://docs.python.org/library/2to3.html){.http}

Program features that need to be changed

- has_key changed to x in dict
- apply() removed
- reduce() changed to functools.reduce()

Infrastructure for automatic refactoring

- tokenize module
- Python 2.5 compile() return ast objects
:::
