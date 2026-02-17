# MacPython/Camino

::: {#content dir="ltr" lang="en"}
You can get the current URL of the current window from Camino with the following appscript:

    import appscript
    print appscript.app("Camino").windows.first.current_tab.URL()
:::
