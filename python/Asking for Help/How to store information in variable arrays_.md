# Asking for Help/How to store information in variable arrays?

::::::::: {#content dir="ltr" lang="en"}
# How to store information in variable arrays? {#How_to_store_information_in_variable_arrays.3F}

How would I store information in variables that I can go back later and compare? Such as

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3bbe682b512956f3ca4468dc8a0db905af2920fa dir="ltr" lang="en"}
   1 x = 1
   2 text = []
   3 while x <= 10:
   4      text.append(int(raw_input("Enter a number: ")))
   5      x = x + 1
   6 
   7 for x in range(10): 
   8     print text[x]
```
:::
::::

I just need to do this to compare a history to make sure a number hasn\'t already been entered earlier. But this is just a small example. I get nasty errors.

Thanks!

edit: that should work now We initialize a list first with `text = []`{.backtick}. Then we just append each element to that list.

------------------------------------------------------------------------

You can use the `in`{.backtick} operator:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-aca064d1720df2b630a5804aa4ef9f510286ae11 dir="ltr" lang="en"}
   1 if number in text:
   2     print "Number already entered!"
```
:::
::::

If you choose to use a set instead of a list\...

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-cbf5c44f49c442b159af008cf18c53f16663ab4a dir="ltr" lang="en"}
   1 text = set()
```
:::
::::

\...then the above test still works, but you\'ll use the `add`{.backtick} method on the set when adding numbers, not an `append`{.backtick} method.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
:::::::::
