# LearnByObservation

::::::::::: {#content dir="ltr" lang="en"}
Note : This is an experimental page, Python can be learned interactively from a prompt, and learning by observations is a good habit, so this page. \-- [BaijuMuthukadan](BaijuMuthukadan)

(This page is not linked from main pages yet.)

### Creating Integer Objects {#Creating_Integer_Objects}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b791545199cde1b17d7099c67945c78237d0b10d dir="ltr" lang="en"}
   1 >>> a = 1
   2 >>> a
   3 1
   4 >>> type(a)
   5 <type 'int'>
   6 >>> b = int(1)
   7 >>> b
   8 1
   9 >>> type(b)
  10 <type 'int'>
```
:::
::::

### \_\_del\_\_ workings {#A__del___workings}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a8c8e49e81b1c4a5a363dd5b87f9b4f73255ce0d dir="ltr" lang="en"}
   1 >>> class C:
   2 ...     def __del__(self):
   3 ...         print "HI"
   4 ... 
   5 >>> c=C()
   6 >>> del(c)
   7 HI
   8 >>> c=C()
   9 >>> c=1
  10 HI
  11 >>> c
  12 1
  13 >>> c=C()
  14 >>> d=c
  15 >>> c=4
  16 >>> d=7
  17 >>> d
  18 HI
  19 7
  20 >>> c=C()
  21 >>> d=c
  22 >>> c=4
  23 >>> d=7
  24 HI
```
:::
::::

### list append and assignment {#list_append_and_assignment}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-52051f4aa1667fe0b3ced09d8b02bf379e9b0ab0 dir="ltr" lang="en"}
   1 >>> a=[1,2,3]
   2 >>> print a
   3 [1, 2, 3]
   4 >>> a=a.append(4)
   5 >>> print a
   6 None
```
:::
::::

### staticmethod vs. classmethod {#staticmethod_vs._classmethod}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a5bbfc08447dc7e2615da07042ce68d940125b6f dir="ltr" lang="en"}
   1 >>> class C:
   2 ...     a=1
   3 ...     @staticmethod
   4 ...     def temp():
   5 ...             print C.a
   6 ... 
   7 >>> C.temp()
   8 1
   9 >>> class C:
  10 ...     a=1
  11 ...     @classmethod
  12 ...     def temp(cls):
  13 ...             print cls.a
  14 ... 
  15 >>> C.temp()
  16 1
```
:::
::::
:::::::::::
