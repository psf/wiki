# MacPython/FileMakerPro/FrequentlyAskedQuestions

::: {#content dir="ltr" lang="en"}
**Q:** *I have [FileMakerPro](./FileMakerPro.html){.nonexistent} 6 and 7 on the same machine. How can I be sure I open the right one ?*

**A:** With `fm = app('FileMaker Pro')` or `fm = app('FileMaker Pro.app')`, you\'ll never know. Use `fm6 = app(id='com.filemaker.filemakerpro')` for [FileMakerPro](./FileMakerPro.html){.nonexistent} 6 and `fm7 = app(id='com.filemaker.pro7')` for [FileMakerPro](./FileMakerPro.html){.nonexistent} 7.
:::
