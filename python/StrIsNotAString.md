# StrIsNotAString

::: {#content dir="ltr" lang="en"}
## History of Python Strings {#History_of_Python_Strings}

[Python](Python) was started by [GuidoVanRossum](./GuidoVanRossum.html){.nonexistent} in December of 1989, Unicode was started in 1991. It is hard to expect that Python developers could introduce [Unicode](Unicode) strings since early versions. Trying to \"reinvent\" Unicode was not an option either since Unicode is a really huge work. Python developers simply introduced strings as they existed in C and many other languages of that time. In the C language a string is a sequence of bytes, and so is Python `str`{.backtick} type.

## Python Strings Today {#Python_Strings_Today}

There is no consensus how to call these strings now, in the age of Unicode. Some people call them byte strings, some call them generic strings, and others call them 8-bit strings, but what is more confusing for a unicode newbie is that a lot of people simply call them strings most of the time.

If you want to understand python unicode you have to understand the difference between byte strings and unicode strings.

In [Python2.4](./Python2(2e)4.html){.nonexistent}, `str` is a string of bytes, and `unicode` is internally represented unicode. `basestring` is a parent class for `unicode` and `str`.

[Python3.0](./Python3(2e)0.html) will clear up this confusion by getting rid of byte strings and introducing the new type `bytes`{.backtick}. The strings you surround with quotation marks will all be unicode strings, automatically. [1](./(5b).html#b){.nonexistent}\]

### See Also {#See_Also}

- \[1\] [PEP 358 \-- The \"bytes\" Object](http://python.org/peps/pep-0358.html){.http}

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
:::
