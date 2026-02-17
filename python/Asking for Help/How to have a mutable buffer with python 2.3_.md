# Asking for Help/How to have a mutable buffer with python 2.3?

::::: {#content dir="ltr" lang="en"}
# Asking for Help: How to have a mutable buffer with python 2.3? {#Asking_for_Help:_How_to_have_a_mutable_buffer_with_python_2.3.3F}

Use the MutableString class in the UserString module:

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

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
:::::
