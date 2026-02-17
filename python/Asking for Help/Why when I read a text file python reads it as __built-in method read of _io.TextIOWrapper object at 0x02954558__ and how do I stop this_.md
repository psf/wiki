# Asking for Help/Why when I read a text file python reads it as "<built-in method read of _io.TextIOWrapper object at 0x02954558>" and how do I stop this?

::::::::: {#content dir="ltr" lang="en"}
# Asking for Help: Why when I read a text file python reads it as \"\<built-in method read of \_io.TextIOWrapper object at 0x02954558\>\" and how do I stop this? {#Asking_for_Help:_Why_when_I_read_a_text_file_python_reads_it_as_.22.3Cbuilt-in_method_read_of__io.TextIOWrapper_object_at_0x02954558.3E.22_and_how_do_I_stop_this.3F}

I am writing a program that uses text files to store user information like their name and password. I am using this information to check login info against the info they have provided. This never worked so I decided to do a simple open files program to find the problem.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c9d541371613b3df063d3f103c5b55a0ab48cd17 dir="ltr" lang="en"}
   1 f = open('test.txt', 'r')
   2 a = f.read
   3 f.close
   4 print(a)
```
:::
::::

and when I ran it on Idle it printed: \<built-in method read of \_io.TextIOWrapper object at 0x02954558\> Instead of what I had in my text file. Does anyone know why this is happening or how to stop it?

------------------------------------------------------------------------

You have to actually call the `read`{.backtick} method as follows:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-84d2bf3f776355161f9b309383c5422349a860cc dir="ltr" lang="en"}
a = f.read()
```
:::
::::

The brackets are important because they tell Python to actually *call* the method, and this produces the content of the file to be assigned to `a`{.backtick}. If you don\'t have the brackets, all you are doing is obtaining the `read`{.backtick} method and assigning it to `a`{.backtick}. Thus, when you print `a`{.backtick} you see a piece of text describing the method (which is what `<built-in method read of _io.TextIOWrapper object at 0x02954558>`{.backtick} means) instead of the content of the file.

So the point to remember is this: referring to the method (like with `f.read`{.backtick}) just lets you obtain the method, but if you want to call the method, you have to add brackets. The following also works:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3c41985d0d053b87ce6d3b37a1267713b810ffd2 dir="ltr" lang="en"}
method = f.read
a = method()
```
:::
::::

Here, we split up the part where you get the method from the part where you call the method. There really are two different things going on. \-- [PaulBoddie](PaulBoddie) 2011-12-17 18:41:14

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
:::::::::
