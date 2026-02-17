# MacPython/Safari

::: {#content dir="ltr" lang="en"}
You can get the current URL of the current window from Safari with the following appscript:

    import appscript
    print appscript.app("Safari").windows.first.current_tab.URL()
:::
