# Asking for Help/How can I convert a hex representation to an integer?

::::::::::: {#content dir="ltr" lang="en"}
## Converting a Hex representation to an Integer {#Converting_a_Hex_representation_to_an_Integer}

I\'m running into some trouble when trying to convert a series of hex representations into an integer\... I\'m sure there is a builtin to do this (wouldn\'t make sense not to have one) but I can\'t find it for the life of me.

This is a dump of my interpreter session:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a69043af4ebe3ae19f5816d3ba243550ae1d9397 dir="ltr" lang="en"}
   1 >>> file=open("C:/test.m4a")
   2 >>> contents=file.read()
   3 >>> contents.find('user')
   4 592
   5 >>> contents[592:600]
   6 'user\x00\xcc\x15\xa4'
```
:::
::::

and I need to convert the values following user (\'\\x00\\xcc\\x15\\xa4\') into an integer value\... what am I doing wrong here?

\[\'anon\'\]: try

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-7af6c8be2a3fb9f236907c62630c18191d14ac1e dir="ltr" lang="en"}
   1 >>> 0x00cc15a4
   2 13374884
```
:::
::::

[lwickjr](lwickjr): you use

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-61ac171546fd5f94fb1c2559b27fb3b73dac2168 dir="ltr" lang="en"}
   1 >>> print int('0a', 16)
   2 10
   3 >>>
```
:::
::::

\...but these aren\`t hex values. Try ord() on each character, and see if that gives you the results you need.

[YerMat](./YerMat.html){.nonexistent}:

See module [struct](http://docs.python.org/lib/module-struct.html){.http} !

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-2a610a44ac8d164777bde1468e306c2e0e2d6b75 dir="ltr" lang="en"}
   1 >>> import struct
   2 >>> struct.unpack('I', '\x00\xcc\x15\xa4')
   3 (2752891904L,)
   4 >>> struct.unpack('i', '\x00\xcc\x15\xa4')
   5 (-1542075392,)
   6 >>>
```
:::
::::

## See Also {#See_Also}

- [BitManipulation](BitManipulation) has a bunch on working with hex

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
:::::::::::
