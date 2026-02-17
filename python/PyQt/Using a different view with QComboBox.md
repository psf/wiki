# PyQt/Using a different view with QComboBox

::::: {#content dir="ltr" lang="en"}
# Using a different view with QComboBox {#Using_a_different_view_with_QComboBox}

On the PyQt mailing list, Adam W. asked for \"[A simple way to add another column to QComboBox?](http://www.riverbankcomputing.com/pipermail/pyqt/2009-September/024242.html){.http}\". Here is some sample code that does this:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ff6520533d3120b0c99395fcf7534303da654f27 dir="ltr" lang="en"}
   1 import sys
   2 from PyQt4.QtCore import Qt, QVariant
   3 from PyQt4.QtGui import *
   4 
   5 
   6 app = QApplication(sys.argv)
   7 model = QStandardItemModel()
   8 
   9 items = [("ABC", True),
  10          ("DEF", False),
  11          ("GHI", False)]
  12 
  13 for text, checked in items:
  14 
  15     text_item = QStandardItem(text)
  16     checked_item = QStandardItem()
  17     checked_item.setData(QVariant(checked), Qt.CheckStateRole)
  18     model.appendRow([text_item, checked_item])
  19 
  20 view = QTreeView()
  21 view.header().hide()
  22 view.setRootIsDecorated(False)
  23 
  24 combo = QComboBox()
  25 combo.setView(view)
  26 combo.setModel(model)
  27 combo.show()
  28 
  29 sys.exit(app.exec_())
```
:::
::::

Note that we set the model on the combo box, not the view.

Some improvements could be made to this code. For example, at small sizes the pop-up doesn\'t always show both columns. Perhaps the combo box\'s [sizeAdjustPolicy](http://qt.nokia.com/doc/4.5/qcombobox.html#sizeAdjustPolicy-prop){.http} property would help with this.

An alternative way to display custom items in the combo box would be to implement a custom item delegate and set that on the combo box.
:::::
