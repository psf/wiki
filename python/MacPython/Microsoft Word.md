# MacPython/Microsoft Word

::: {#content dir="ltr" lang="en"}
Powerpoint and Word have extensive Applescript dictionaries.

Here\'s how to get the path of the folder of the current document in Word, and the name of the file:

      from appscript import *
      a = app("Microsoft Word")
      path = a.active_document.path()
      file = a.active_document.name()
      print path, file
:::
