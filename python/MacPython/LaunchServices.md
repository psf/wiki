# MacPython/LaunchServices

::::: {#content dir="ltr" lang="en"}
# /LaunchServices {#A.2FLaunchServices}

[LaunchServices](./LaunchServices.html){.nonexistent} is a pythonic wrapper for just about everything Apple\'s [Launch Services API](http://developer.apple.com/technotes/tn/tn2017.html){.http} has to offer. It was developed primarily to make [/aeve](./MacPython(2f)LaunchServices(2f)aeve.html){.nonexistent} a hell of a lot easier to use.

# status

[LaunchServices](./LaunchServices.html){.nonexistent} is at its first public release, 0.1

# examples

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c3b933f7467ee056e65a10a3b1f945e1280a111d dir="ltr" lang="en"}
   1 >> import LaunchServices as LS
   2 >> LS.GetDisplayNameForPath('/')
   3 u'Crack'
   4 >> LS.GetKindStringForPath('/')
   5 u'Volume'
   6 >> LS.GetApplicationPathForInfo(extension='mp3')
   7 u'/Applications/iTunes.app'
   8 >> LS.GetApplicationPathForInfo(creator='MACS')
   9 u'/System/Library/CoreServices/Finder.app'
  10 >> LS.FindApplicationPath(bundle='com.apple.iChat')
  11 u'/Applications/iChat.app'
```
:::
::::
:::::
