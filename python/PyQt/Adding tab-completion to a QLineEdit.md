# PyQt/Adding tab-completion to a QLineEdit

::::: {#content dir="ltr" lang="en"}
# Adding tab-completion to a QLineEdit {#Adding_tab-completion_to_a_QLineEdit}

On the `#pyqt`{.backtick} IRC channel on [Freenode](http://www.freenode.net){.http}, `sonic`{.backtick} asked how to handle key events for a QLineEdit widget to enable tab-completion.

The following code shows how to subclass QLineEdit and reimplement the `keyPressEvent()`{.backtick} method. The tab-completion code isn\'t ideal - you should probably consider using a QCompleter object to handle the process of completing an incomplete piece of text.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a473d8be3aca2b5ef1d86e88a747f2d87bbfd164 dir="ltr" lang="en"}
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import QApplication, QLineEdit
   4 
   5 class LineEdit(QLineEdit):
   6 
   7     completion_items = [
   8         u"hello",
   9         u"world"
  10         ]
  11 
  12     def __init__(self, parent = None):
  13     
  14         QLineEdit.__init__(self, parent)
  15     
  16     def keyPressEvent(self, event):
  17     
  18         if event.key() == Qt.Key_Tab:
  19             for item in self.completion_items:
  20                 if item.startswith(self.text()):
  21                     self.setText(item)
  22                     break
  23             
  24             event.accept()
  25         else:
  26             QLineEdit.keyPressEvent(self, event)
  27 
  28 
  29 if __name__ == "__main__":
  30 
  31     app = QApplication(sys.argv)
  32     window = LineEdit()
  33     window.show()
  34     sys.exit(app.exec_())
```
:::
::::
:::::
