# DefaultEncoding

::::: {#content dir="ltr" lang="en"}
Python users who are new to Unicode sometimes are attracted by default encoding returned by sys.getdefaultencoding(). The first thing you should know about default encoding is that you don\'t need to care about it. Its value should be \'ascii\' and it is used when converting byte strings [StrIsNotAString](StrIsNotAString) to unicode strings. As in this example:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4222857a88f26d1fca17b37f3113e7a15babae3e dir="ltr" lang="en"}
   1 a = "abc" + u"bcd"
```
:::
::::

When you concatenate byte string \"abc\" with unicode string u\"bcd\" Python will first convert \"abc\" into u\"abc\" by calling \"abc\".decode(sys.getdefaultencoding()). If you put non-ascii characters into byte string then .decode(sys.getdefaultencoding()) method will fail with `UnicodeDecodeError`, therefore byte strings should not contain non-ascii characters. In [Python3.0](./Python3(2e)0.html) sys.getdefaultencoding will be removed.

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
:::::
