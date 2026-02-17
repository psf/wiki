# Asking for Help/Why do I see b'string' when i print a c_char_p string?

:::::: {#content dir="ltr" lang="en"}
# Asking for Help: \... {#Asking_for_Help:_...}

\...

I was trying to use ctypes to get Windows clipboard contents and the value that gets returned is a ctypes.c_char_p string. When I print it the string looks like b\'contents_of_clipboard\'. I am not sure why this happens or how to get rid of it. anyone know. The code that I pilfered from the net to do this is below

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-bf43b9c3f931ba6fa71bb20fabd44f94fce0b960 dir="ltr" lang="en"}
   1 import ctypes, sys
   2 
   3 def winGetClipboard():
   4         ctypes.windll.user32.OpenClipboard(0)
   5         pcontents = ctypes.windll.user32.GetClipboardData(1) # 1 is CF_TEXT
   6         data = ctypes.c_char_p(pcontents).value
   7         ctypes.windll.user32.CloseClipboard()
   8         return data
```
:::
::::

If I had Hello World on the clipboard the returned output would be **b\'Hello World\'**

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help](./Asking(20)for(20)Help.html) page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
::::::
