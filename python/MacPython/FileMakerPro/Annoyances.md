# MacPython/FileMakerPro/Annoyances

:::: {#content dir="ltr" lang="en"}
**About the Table class:**

- in some case, specifying the table class as `class_=k.table` doesn\'t work, use `class_='cTBL'` instead:

::: {}
  ----------------------------------------- ----------------------------------------
  **Instead of:**                           **do:**
  `fm.databases[1].count(class_=k.table)`   `fm.databases[1].count(class_='cTBL')`
  ----------------------------------------- ----------------------------------------
:::
::::
