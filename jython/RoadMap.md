# RoadMap

::: {#content dir="ltr" lang="en"}
# Jython Roadmap {#Jython_Roadmap}

## Position Now {#Position_Now}

(Least edited February 2013.)

- v2.5.3 is current.

## Current Plan {#Current_Plan}

(Least edited February 2013: Needs more detail.)

- v2.5.x versions may appear consolidating bug-fixes
- v2.6 is skipped
- v2.7 is the main focus of current work. A beta is imminent (February 2013).
- v3.x (3.3 probably) is under consideration.

## Who is doing what? {#Who_is_doing_what.3F}

- [Bug fixes](http://bugs.jython.org){.http}: anyone

### Towards v2.7 {#Towards_v2.7}

- math module: Oti

- documentation, text_xrange.py, test_complex.py: Josh

- grammar cleanup, test_class.py: Frank

- itertools, collections: Jim

- mercurial move, abcs, exceptions, posix/ntpath, io, tarfile: pjenvey

- `bytearray`{.backtick}, buffer API and a partial `memoryview`{.backtick}: Jeff

### Towards v3.3 {#Towards_v3.3}

- Use of Java 7 `invokedynamic`{.backtick}: Jim?

## Scraps of former plans {#Scraps_of_former_plans}

When the page bore a roadmap was for v2.6, this material was in it. Some of it is still accurate for v2.7, some is probably complete now, and some is no longer relevant. Those who know which is which are able to improve the roadmap!

### 2.6.0 {#A2.6.0}

- Upgrade to Python 2.6 language and builtins, along with a substantial subset of the stdlib

- Redesign [PySystemState](./PySystemState.html){.nonexistent}, [ThreadState](./ThreadState.html){.nonexistent} API

- Mark true-public APIs with a suitable annotation; deprecate and/or remove obsolete APIs

- Remove all user-visible singletons in org.python.core, especially any static public fields (like those in `PySystemState`{.backtick})

- Performance!

- Require minimum Java 6, rip out Java 5 compatibility:
  - Generic.newSetFromMap
  - Believe we can remove the xercesImpl jar, livetribe-jsr223-2.0.5.jar
  - can start utilizing jsr199 (the Java compiler API) for certain things (mostly for unittests I believe)
  - Other things..

### 2.6.? (TBD) {#A2.6..3F_.28TBD.29}

- unicodedata

- [cjkcodecs](http://bugs.jython.org/issue1066){.http}: yyamano

- [bz2 module](http://www.python.org/doc/lib/module-bz2.html){.http}

- [ReplaceJythonc](ReplaceJythonc)

- [MigrateBugtests](MigrateBugtests)

- Import Python from the classpath

- Performance improvements

### Future? {#Future.3F}

- [ctypes module](http://docs.python.org/whatsnew/modules.html#SECTION0001410000000000000000){.http}

- Translate summer of code compiler to Java \*Incorporated, except for pyc support
:::
