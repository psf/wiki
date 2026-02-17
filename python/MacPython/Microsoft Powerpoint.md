# MacPython/Microsoft Powerpoint

::: {#content dir="ltr" lang="en"}
Powerpoint and Word have extensive Applescript dictionaries.

Here\'s how to get the path of the folder of the current presentation in Powerpoint, and the name of the file:

      from appscript import *
      a = app("Microsoft Powerpoint")
      path = a.active_presentation.path()
      file = a.active_presentation.name()
      print path, file
:::
