# PyQt/Using a translation of Qt

::::: {#content dir="ltr" lang="en"}
# Using a translation of Qt {#Using_a_translation_of_Qt}

On the `#pyqt`{.backtick} channel on [freenode](http://freenode.net){.http}, `Fisiu`{.backtick} asked about getting localized versions of the Qt dialogs.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9d6490909f568cb4bf8083599d32d6d7d0473f29 dir="ltr" lang="en"}
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 if __name__ == "__main__":
   6 
   7     app = QApplication(sys.argv)
   8     
   9     qt_translator = QTranslator()
  10     qt_translator.load("qt_" + QLocale.system().name(),
  11                        QLibraryInfo.location(QLibraryInfo.TranslationsPath))
  12     app.installTranslator(qt_translator)
  13     
  14     QMessageBox.aboutQt(None)
  15     sys.exit()
```
:::
::::
:::::
