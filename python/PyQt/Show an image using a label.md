# PyQt/Show an image using a label

::::: {#content dir="ltr" lang="en"}
# Show an image using a label {#Show_an_image_using_a_label}

On the `#pyqt`{.backtick} IRC channel on Freenode, `elhobab`{.backtick} asked how to show an image.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c302a4cf176053ec8ceff300efd842c7dfc2afd6 dir="ltr" lang="en"}
   1 import sys
   2 from PyQt4.QtGui import *
   3 
   4 app = QApplication(sys.argv)
   5 
   6 label = QLabel()
   7 pixmap = QPixmap(sys.argv[1])
   8 label.setPixmap(pixmap)
   9 label.show()
  10 
  11 sys.exit(app.exec_())
```
:::
::::
:::::
