# MultiLineStringsInDocTest

:::::::::::: {#content dir="ltr" lang="en"}
The [DocTest](DocTest) module requires special actions / processing for multi-line strings.

::: table-of-contents
Contents

1.  [Multi-Line Strings in commands](#Multi-Line_Strings_in_commands)
2.  [Multi-Line Strings in output](#Multi-Line_Strings_in_output)
:::

# Multi-Line Strings in commands {#Multi-Line_Strings_in_commands}

Consider a function `get_html_title` designed to extract the title from an HTML page. Here is some python code to test the function:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1380e2ba8b92389815096287a4d3bcc31f9769bd dir="ltr" lang="en"}
   1 >>> html = '''
   2 <html>
   3 <head>
   4 <title>This is the page title</title>
   5 </head>
   6 <body>
   7 This is the body
   8 </body>
   9 </html>
  10 '''
  11 >>> title = get_html_title(html)
  12 >>> assert(title == "This is the page title")
```
:::
::::

Putting this directly into a doctest results in an exception, such as:

    Failed example:
        html = '''
    Exception raised:
        Traceback (most recent call last):
          File "C:\Python24\lib\doctest.py", line 1243, in __run
            compileflags, 1) in test.globs
          File "<doctest sample.tests[1]>", line 1
             html = '''
                       ^
         SyntaxError: EOF while scanning triple-quoted string

The solution is to add the command continuation characters:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4d5023eae1ac6d0df2b48126f2001db539ef8e01 dir="ltr" lang="en"}
   1 >>> html = '''
   2 ... <html>
   3 ... <head>
   4 ... <title>This is the page title</title>
   5 ... </head>
   6 ... <body>
   7 ... This is the body
   8 ... </body>
   9 ... </html>
  10 ... '''
  11 >>> title = get_html_title(html)
  12 >>> assert(title == "This is the page title")
```
:::
::::

# Multi-Line Strings in output {#Multi-Line_Strings_in_output}

Blank lines in the output need to be specially handled. For example, the following doctest will fail:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-dffb7eec3a9e1c7a7b2a3b280f5fdbaeda94e96c dir="ltr" lang="en"}
   1 >>> test = "Here is a blank line\n\nBlank line is above"
   2 >>> print test
   3 Here is a blank line
   4 
   5 Blank line is above
```
:::
::::

This is because the blank line is used to seperate commands and comments. With Python 2.4, a `<BLANKLINE>` keyword was added, so the proper doctest is now:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-745d58b50e7b4eab541b550e5825f5b883bb3ba2 dir="ltr" lang="en"}
   1 >>> test = "Here is a blank line\n\nBlank line is above"
   2 >>> print test
   3 Here is a blank line
   4 <BLANKLINE>
   5 Blank line is above
```
:::
::::
::::::::::::
