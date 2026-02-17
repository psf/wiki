# PyQt/Previewing a form

::::: {#content dir="ltr" lang="en"}
# Previewing a form {#Previewing_a_form}

On the `#pyqt`{.backtick} channel on [Freenode](http://freenode.net){.http}, `a_l_e`{.backtick} asked for a way to preview a main window form created in Qt Designer.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f884d1d6407195cb3416781af60d20d16b781e47 dir="ltr" lang="en"}
   1 import sys
   2 
   3 from PyQt4.QtGui import QApplication
   4 from PyQt4.uic import loadUi
   5 
   6 if __name__ == "__main__":
   7 
   8     app = QApplication(sys.argv)
   9     
  10     if len(app.arguments()) != 2:
  11     
  12         sys.stderr.write("Usage: %s <ui file>\n" % app.arguments()[0])
  13         sys.exit()
  14     
  15     window = loadUi(app.arguments()[1])
  16     window.show()
  17     sys.exit(app.exec_())
```
:::
::::
:::::
