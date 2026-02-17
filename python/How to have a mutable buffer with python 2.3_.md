# How to have a mutable buffer with python 2.3?

::::: {#content dir="ltr" lang="en"}
Use the [MutableString](./MutableString.html){.nonexistent} class in the [UserString](./UserString.html){.nonexistent} module:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1135fb4b1a5de4c4f93c35b6177adfe6acb4aec8 dir="ltr" lang="en"}
   1 >>> from UserString import MutableString
   2 >>> s = MutableString('python')
   3 >>> s[2:4] = 'l'
   4 >>> print s
   5 pylon
```
:::
::::
:::::
