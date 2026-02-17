# LoadingModulesDynamically

::::::::: {#content dir="ltr" lang="en"}
You can load a module dynamically like so:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f476c1e100a564d645fd3329050e4969996bc89d dir="ltr" lang="en"}
   1 __import__("os")
```
:::
::::

If you do that, though, \"os\" isn\'t bound to anything.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-fce0b4ef1a9b8d399daf91c0188a4d6d7e7d863b dir="ltr" lang="en"}
   1 >>> __import__("os")
   2 <module 'os' from '/usr/lib/python2.3/os.pyc'>
   3 >>> os
   4 Traceback (most recent call last):
   5   File "<stdin>", line 1, in ?
   6 NameError: name 'os' is not defined
   7 >>>
```
:::
::::

Once you have the module, you probably want to find classes and functions and data inside of it.

Use `getattr`:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-5fc07efc65d1c3a54972f90e10c9fe1f450fd42f dir="ltr" lang="en"}
   1 >>> m=__import__("mine")
   2 >>> m
   3 <module 'mine' from 'mine.pyc'>
   4 >>> getattr(m, "eggs")
   5 4654
   6 >>> getattr(m, "ham")
   7 'Monty Python'
```
:::
::::
:::::::::
