# PyFileBenchmarks

::::::::::::::::::: {#content dir="ltr" lang="en"}
Some [PyFile](./PyFile.html){.nonexistent} benchmarks, mostly to show off the [PyFile](./PyFile.html){.nonexistent} nio

Tests done on OS X 10.4.10 Java 1.5.0_07 in server mode

Preparations: 10

Test iterations (average taken of): 5

Notes:

\* This page is made for a larger browser window so that the small and big graphs lie on the same row

\* jython\'s file iter is roughly the same code as its readline, whereas CPython\'s readline is not as optimized as its iter. So the fact that our readline speed is very close to CPython\'s isn\'t totally fair, CPython\'s iter still beats us

\* The few anomalies in the smaller benchmarks are due to JIT kicking in. Ideally we would run more preparations and iterations

\* i don\'t have text mode benchmarks because they\'re only applicable to windows. their read times would be a little faster than \'U\' mode. write times would be slower than \'rb\' but still faster than old [PyFile](./PyFile.html){.nonexistent}

\* The write times show both writing to a ram disk and writing to a hard disk. Writing to a hard disk shows how much slower Jython\'s old [PyFile](./PyFile.html){.nonexistent} really is in a normal workload, compared to CPython and [PyFile](./PyFile.html){.nonexistent} nio, whose write times are limited to the speed of the hard disk. Writing to a ram disk shows how potentially fast CPython and [PyFile](./PyFile.html){.nonexistent} nio can write

Reading:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ac6c4f6465bc1c19d8f256d77870beeb9b3374b0 dir="ltr" lang="en"}
   1     def test_read(self, fp):
   2         fp.read()
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_read.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_read.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_read.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_read.jpg"){.external_image}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-37f4b0a7fc4bf0ead86ea38cb680dc9f41279f2d dir="ltr" lang="en"}
   1     def test_iter(self, fp):
   2         for line in fp:
   3             pass
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_iter.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_iter.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_iter.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_iter.jpg"){.external_image}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-71ae3d4408f5d84e104d3088904f9c82fed958bf dir="ltr" lang="en"}
   1     def test_readline(self, fp):
   2         while fp.readline():
   3             pass
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline.jpg"){.external_image}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3433e7d18707f87523a1df60e26b5c0aa20d4f8e dir="ltr" lang="en"}
   1     def test_readline_with_tell(self, fp):
   2         while fp.readline():
   3             fp.tell()
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline_with_tell.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline_with_tell.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline_with_tell.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline_with_tell.jpg"){.external_image}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-198bdfdb257cc00b5c352eaa7eadf51939c8fd05 dir="ltr" lang="en"}
   1     def test_readlines(self, fp):
   2         fp.readlines()
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readlines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readlines.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readlines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readlines.jpg"){.external_image}

Writing:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-5fb24ab704022cfebf650a63c14149c8483bd859 dir="ltr" lang="en"}
   1 MSG = ('abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz123456789'
   2        '0abcdefgh\r\n')
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-7c8eb9493de3ae6bc522f570c053735cfc1f26ac dir="ltr" lang="en"}
   1     def test_write(self, fp, lines):
   2         write = fp.write
   3         for i in range(lines):
   4             write(MSG)
```
:::
::::

To a ramdisk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_write.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_write.jpg"){.external_image}

To disk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_write.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_write.jpg"){.external_image}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0f3137d23a9654e696a01b4cf9541a4cf0c04113 dir="ltr" lang="en"}
   1     def test_writelines(self, fp, lines):
   2         lines = [MSG for i in range(lines)]
   3         fp.writelines(lines)
```
:::
::::

To a ramdisk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_writelines.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_writelines.jpg"){.external_image}

To disk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_writelines.jpg"){.external_image} ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_writelines.jpg"){.external_image}
:::::::::::::::::::
