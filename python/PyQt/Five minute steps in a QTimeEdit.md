# PyQt/Five minute steps in a QTimeEdit

::::: {#content dir="ltr" lang="en"}
# Five minute steps in a QTimeEdit {#Five_minute_steps_in_a_QTimeEdit}

On the `#pyqt`{.backtick} channel on Freenode, `rowinggolfer`{.backtick} asked if it was possible to make QTimeEdit step in five minute intervals.

The following subclass reimplements the `stepBy()`{.backtick} method and calls the base class implementation with an adjusted number of steps.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-6f4987ded1b5886d3cb32ff86131d6f142bd260c dir="ltr" lang="en"}
   1 class FiveMinuteTimeEdit(QTimeEdit):
   2   def stepBy(self, steps):
   3     if self.currentSection() == self.MinuteSection:
   4       QTimeEdit.stepBy(self, steps * 5)
   5     else:
   6       QTimeEdit.stepBy(self, steps)
```
:::
::::
:::::
