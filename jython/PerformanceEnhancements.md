# PerformanceEnhancements

:::::::: {#content dir="ltr" lang="en"}
# Performance Enhancements Resources

Jython benchmarks (from PyPy\'s suite): [http://freya.cs.uiuc.edu/\~njriley/benchmark.html](http://freya.cs.uiuc.edu/~njriley/benchmark.html){.http .reference .external}

Plots of microbenchmarks (also from PyPy): [http://freya.cs.uiuc.edu/\~njriley/plots.html](http://freya.cs.uiuc.edu/~njriley/plots.html){.http .reference .external}

::::::: {#ideas .section}
### Ideas

jbaker & thobe\'s JavaOne \'08 talk: [Jython Implementing Dynamic Language Features For The Java Ecosystem](http://developers.sun.com/learning/javaoneonline/2008/pdf/TS-6039.pdf?cid=925321){.http .reference .external}

::: {#allocation-gc-expense .section}
#### Allocation/GC Expense

Our algorithms are not always the problem, sometimes it\'s memory {de}allocations that slow you down

- dicts/stringmap

PyStringMap/PyDictionary pay a penalty on allocation now that they\'re backed by ConcurrentHashMap. We could probably tweak the ConcurrentHashMap initialCapacity, concurrentLevel to reduce this cost

- Frames

Frames are allocated for every Python method call, which is a GC expense. CPython (and JRuby?) recycle frame objects. Reducing the number of fields on the frame can also help (but this likely isn\'t possible)
:::

::: {#advanced-compiler .section}
#### Advanced Compiler
:::

::: {#modules-to-rewrite-in-java .section}
#### Modules to rewrite in Java

- \_heapq
- select
- socket
- unicodedata
:::

::: {#iterlen-support .section}
#### iterlen support

Adds a length hint to various objects, mainly for smarter allocation during map and list. See test_iterlen
:::
:::::::
::::::::
