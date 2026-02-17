# UpgradeTo25CPythonLib

::::::: {#content dir="ltr" lang="en"}
::: {#buildbots .section}
### Buildbots

- [http://www.acm.uiuc.edu/jython-buildbot/waterfall](http://www.acm.uiuc.edu/jython-buildbot/waterfall){.http .reference .external}
- [http://bob.underboss.org:8080/](http://bob.underboss.org:8080/){.http .reference .external}
:::

::: {#to-fix .section}
### To Fix

- test_import_jy - ?
- Windows failures - files not being properly closed
:::

::: {#flaky-arch .section}
### Flaky/arch?

- test_socket - historically this is the case on SO_RCVBUF, SO_SNDBUF. particularly flakey on solaris buildbots
- test_select - flakey on FreeBSD hudson buildbot
:::

::: {#under-development .section}
### Under Development

Or perhaps more accurately, the following *should* be under development.

- test_unicode
  - test_codecs_idna - no idna encoding (which needs unicodedata 3.2.0) [http://bugs.jython.org/issue1153](http://bugs.jython.org/issue1153){.http .reference .external}
- test_stringprep - [http://bugs.jython.org/issue1758320](http://bugs.jython.org/issue1758320){.http .reference .external}
- \_rawffi (for ctypes, ported from PyPy)
- bz2 (Georgy Berdyshev is looking at this. Leo User\'s bz2 module code is available from here: [http://underboss.org/\~pjenvey/jython/jythonx-bits.tar.bz2](http://underboss.org/~pjenvey/jython/jythonx-bits.tar.bz2){.http .reference .external} )
- multibytecodec (implies test_multibytecodec_support)
- unicodedata - need a Java implementation, not our current Jython workaround (too slow to load, on the order of a couple of seconds)
:::
:::::::
