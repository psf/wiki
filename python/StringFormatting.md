# StringFormatting

::::::::::::::: {#content dir="ltr" lang="en"}
# String Formatting {#String_Formatting}

The [section of the manual on String Formatting Operations](http://docs.python.org/lib/typesseq-strings.html){.http} is hidden in the section on [Sequence types.](http://docs.python.org/lib/typesseq.html){.http}

Tutorial on the new string formatting method `format()`{.backtick} in Python 3.0: [Py3kStringFormatting](Py3kStringFormatting)

## Direct Variable Reference {#Direct_Variable_Reference}

A common trick you can use when writing strings is to refer directly to variables.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a27d879d091a8dd4bb61141fa352994a6034fa8f dir="ltr" lang="en"}
   1 a = "hello, world!"
   2 x = 34
   3 y = 96
   4 
   5 print """
   6 a = %(a)s
   7 x,y = (%(x)s,%(y)s)
   8 """ % vars() # local variables
```
:::
::::

If you want to refer to global variables, you can replace `vars()` with `globals()`.

## Printing Percentages {#Printing_Percentages}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-6d43ff1d5bb340c6bf146a47f71863f4f6b324f4 dir="ltr" lang="en"}
   1 percent = lambda x:"%2.2f%%" % x
   2 
   3 print percent(35.3567) # prints "35.35%"
```
:::
::::

## Print strings without newlines and spaces {#Print_strings_without_newlines_and_spaces}

You may find it tricky to print out a feed of numbers (as output from within a loop) on one line, without being separated by a space. An example could be output such as

    Processing...
    [1][2][3][4][5][6]
    Completed.

The standard `print`{.backtick} statement automatically inserts newlines. This can be overcome with

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3400d11a0fc729235fa8df013980a18a85da1728 dir="ltr" lang="en"}
   1 for i in range(10):
   2     print '['+str(i)+']',  # NOTE the trailing comma
```
:::
::::

but a space will get inserted between successive prints. One way to get around this is using `sys.stdout`{.backtick}:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-deab79f6455c079e187a20765601fa179ed422d5 dir="ltr" lang="en"}
   1 import sys
   2 for i in range(10):
   3     sys.stdout.write('['+str(i)+']')
```
:::
::::

which will work properly.

## See Also {#See_Also}

[EscapingHtml](EscapingHtml), [WorkingWithTime](WorkingWithTime)

# Discussion {#Discussion}

You can also print a backspace (`'\b'`{.backtick}) to swallow the extra space. eg:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-07f72884988b9a8a90e68e7363f4c1b892abc841 dir="ltr" lang="en"}
   1 for i in range(10):
   2     print '\b%d' % i,
   3 # Prints: 0123456789
```
:::
::::

Unfortunately, this produces a mess if output is being directed to a file; it\'s best to avoid printing the space if you don\'t want it.

## Variable name substitution using format and eval {#Variable_name_substitution_using_format_and_eval}

I want to print out all member of `sys`{.backtick}, then what I need is

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-de065b93050129fd00addd4e3ad1de462c4647aa dir="ltr" lang="en"}
   1 for member in dir(sys):
   2     print "sys." + member, "->", repr(getattr(sys, member))
```
:::
::::
:::::::::::::::
