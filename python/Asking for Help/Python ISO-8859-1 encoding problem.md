# Asking for Help/Python ISO-8859-1 encoding problem

:::::: {#content dir="ltr" lang="en"}
# Asking for Help: Python ISO-8859-1 encoding problem {#Asking_for_Help:_Python_ISO-8859-1_encoding_problem}

Hi all,

I\'m facing a huge encoding problem in Python when dealing with ISO-8859-1 / Latin-1 character set.

When using os.listdir to get the contents of a folder I\'m getting the strings encoded in ISO-8859-1 (ex: *Ol\\xe1 Mundo*), however in the Python interpreter the same string is encoded to a different charset:

In : \'Olá Mundo\'.decode(\'latin-1\')

Out: u\'Ol\\xa0 Mundo\'

How can I force Python to decode the string to the same format. I\'ve seen that os.listdir is returning the strings correctly encoded but the interpreter is not (\'á\' character corresponds to \'\\xe1\' in ISO-8859-1, not to \'\\xa0\'):

[http://en.wikipedia.org/wiki/ISO/IEC_8859-1](http://en.wikipedia.org/wiki/ISO/IEC_8859-1){.http}

This is happening

Any thoughts on how to overcome ?

------------------------------------------------------------------------

Some questions:

- Is your interactive session using the same locale as the code which uses `os.listdir`{.backtick}?

- Have you tried using `os.listdir`{.backtick} in the interactive session and capturing the filename directly? For example:

  :::: {.highlight .python}
  ::: {.codearea dir="ltr" lang="en"}
  ``` {#CA-1c20c6ab68f0df8a086293d75ce2d5568fa84b97 dir="ltr" lang="en"}
  filenames = os.listdir(folder)
  print filenames                     # to see which one you want
  filenames[INDEX].decode('latin-1')  # substitute the position of the interesting file for INDEX
  ```
  :::
  ::::

In my console, doing `'Olá Mundo'.decode('latin-1')`{.backtick} gives `u'Ol\xe1 Mundo'`{.backtick}, but then my locale looks like this:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-04ed5b0906a50dc549d8b39e9ec5ef0b0b1bb707 dir="ltr" lang="en"}
>>> from locale import *
>>> setlocale(LC_ALL, "")
'en_US.ISO-8859-15'
>>> getlocale(LC_ALL)
('en_US', 'ISO8859-15')
```
:::
::::

The `latin-1`{.backtick} encoding is virtually the same as this one. Maybe you should see which locale you\'re using. \-- [PaulBoddie](PaulBoddie) 2011-11-13 17:16:11

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help](./Asking(20)for(20)Help.html) page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
::::::
