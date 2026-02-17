# PyQt/Customising a tab to contain a menu

::::: {#content dir="ltr" lang="en"}
# Customising a tab to contain a menu {#Customising_a_tab_to_contain_a_menu}

On the `#pyqt`{.backtick} channel on [Freenode](http://freenode.net){.http}, `rowinggolfer`{.backtick} asked if it was possible to put a pop-up menu in a tab bar. The following code shows one way to approach the problem.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-da231dd709658d5970412648ab42417d328d16af dir="ltr" lang="en"}
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import *
   4 
   5 if __name__ == "__main__":
   6 
   7     app = QApplication(sys.argv)
   8     tabWidget = QTabWidget()
   9     tabWidget.addTab(QTextEdit(), "Hello")
  10     tabWidget.addTab(QCalendarWidget(), "World")
  11     
  12     tabBar = tabWidget.tabBar()
  13     menu = QMenu()
  14     menu.addAction("Open")
  15     menu.addAction("Close")
  16     menuButton = QToolButton()
  17     menuButton.setArrowType(Qt.DownArrow)
  18     menuButton.setMenu(menu)
  19     menuButton.setToolButtonStyle(Qt.ToolButtonFollowStyle)
  20     tabBar.setTabButton(0, QTabBar.RightSide, menuButton)
  21     
  22     tabWidget.show()
  23     sys.exit(app.exec_())
```
:::
::::
:::::
