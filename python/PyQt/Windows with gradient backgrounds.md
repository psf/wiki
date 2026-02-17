# PyQt/Windows with gradient backgrounds

::::: {#content dir="ltr" lang="en"}
# Windows with gradient backgrounds {#Windows_with_gradient_backgrounds}

On the #pyqt channel on Freenode, `felipe__`{.backtick} asked if it was possible to change the background colour of a window.

This code shows how it can be done with a fixed gradient. If you are subclassing QWidget or another widget class, it may be worth reimplementing its `resizeEvent()`{.backtick} method to modify the gradient so that it changes when the window is resized.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9727e01a9b628c4ec99b931c3c587448e05fd25b dir="ltr" lang="en"}
   1 import sys
   2 from PyQt4.QtGui import *
   3 
   4 if __name__ == "__main__":
   5 
   6     app = QApplication([])
   7     
   8     w = QWidget()
   9     
  10     p = QPalette()
  11     gradient = QLinearGradient(0, 0, 0, 400)
  12     gradient.setColorAt(0.0, QColor(240, 240, 240))
  13     gradient.setColorAt(1.0, QColor(240, 160, 160))
  14     p.setBrush(QPalette.Window, QBrush(gradient))
  15     w.setPalette(p)
  16     
  17     w.show()
  18     app.exec_()
```
:::
::::
:::::
