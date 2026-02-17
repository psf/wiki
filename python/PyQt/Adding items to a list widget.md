# PyQt/Adding items to a list widget

::::: {#content dir="ltr" lang="en"}
# Adding items to a list widget {#Adding_items_to_a_list_widget}

On the `#pyqt`{.backtick} channel at Freenode, `afief`{.backtick} asked for an example that showed how to add items to a list widget using QListWidgetItem rather than just plain strings.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-39c3e558f54f83207ae46e8aa90220ff181f60e9 dir="ltr" lang="en"}
   1 import sys
   2 from PyQt4.QtGui import *
   3 
   4 app = QApplication(sys.argv)
   5 
   6 listWidget = QListWidget()
   7 
   8 for i in range(10):
   9     item = QListWidgetItem("Item %i" % i)
  10     listWidget.addItem(item)
  11 
  12 listWidget.show()
  13 sys.exit(app.exec_())
```
:::
::::

Although this example seems easy, there is one subtle point worth noting: the list widget takes ownership of each of the items added to it. This means that you cannot add an item to more than one list widget.
:::::
