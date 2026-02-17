# ListOfPerformanceRelatedPatches

::: {#content dir="ltr" lang="en"}
Pending:

- [\[ 1479611](http://www.python.org/sf/1479611){.http} \] speed up function calls TP

- [\[ 876193](http://www.python.org/sf/876193){.http} \] reorganize, extend function call optimizations TP

- [\[ 1107887](http://www.python.org/sf/1107887){.http} \] Speed up function calls/can add more introspection info TP

- [\[ 1087418](http://www.python.org/sf/1087418){.http} \] long int bitwise ops speedup TP

- [\[ 1366311](http://www.python.org/sf/1366311){.http} \] SRE engine do not release the GIL

- [\[ 1346214](http://www.python.org/sf/1346214){.http} \] Better dead code elimination for the AST compiler GB

  - New patch posted, ready for review

- [\[ 1243654](http://www.python.org/sf/1243654){.http} \] Faster output if message already has a boundary SH

Addressed:

- [\[ 1145039](http://www.python.org/sf/1145039){.http} \] Remove some invariant conditions and assert in ceval TP

- [\[ 1442927](http://www.python.org/sf/1442927){.http} \] `PyLong_FromString`{.backtick} optimization

- [\[ 1335972](http://www.python.org/sf/1335972){.http} \] combo speedup and bugfix for string-\>int conversion

- [\[ 876206](http://www.python.org/sf/876206){.http} \] scary frame speed hacks \[SUCCESS\]

- [\[ 1281707](http://www.python.org/sf/1281707){.http} \] Speed up gzip.readline (\~40%) \[SUCCESS\]

- [\[ 1337051](http://www.python.org/sf/1337051){.http} \] remove 4 ints from [PyFrameObject](./PyFrameObject.html){.nonexistent}

- [\[ 1243730](http://www.python.org/sf/1243730){.http} \] Big speedup in email message parsing SH **no speedup observed**

- [\[ 921466](http://www.python.org/sf/921466){.http} \] Reduce number of open calls on startup GB

- [\[ 1359618](http://www.python.org/sf/1359618){.http} \] Speed charmap encoder \[patch approved, MAL to apply\]

Deferred:

- [\[ 813436](http://www.python.org/sf/813436){.http} \] Scalable zipfile extension

  - Addressed by SoC student

- [\[ 738094](http://www.python.org/sf/738094){.http} \] for i in range(N) optimization

  - Related to [\[ 1472639](http://www.python.org/sf/1472639){.http} \] make range be xrange

  - Topic was discussed endlessly for some times.

- [\[ 936813](http://www.python.org/sf/936813){.http} \] fast modular exponentiation

  - Going to need a lot of attention, not suitable for the sprint.

- [\[ 923643](http://www.python.org/sf/923643){.http} \] long \<-\> byte-string conversion

  - This is a feature request.

- [\[ 1353872](http://www.python.org/sf/1353872){.http} \] a faster Modulefinder (Related to py2exe runtime performance)

  - No one interested in it.

- [\[ 1492828](http://www.python.org/sf/1492828){.http} \] Improvements to ceval.c \--\> [RaymondHettinger](./RaymondHettinger.html){.nonexistent}

- [\[ 1346238](http://www.python.org/sf/1346238){.http} \] A constant folding optimization pass for the AST
:::
