# PythonSpeed/Profiling

::: {#content dir="ltr" lang="en"}
# Profiling Python Programs {#Profiling_Python_Programs}

See [PythonDebuggingTools#Profilers](PythonDebuggingTools#Profilers) for a list of profilers

## Scalene {#Scalene}

The [Scalene profiler](https://github.com/emeryberger/scalene){.https} is both easy to use and provides a number of advantages over the profilers bundled with Python:

1.  Scalene is **fast**. It uses sampling instead of instrumentation or relying on Python\'s tracing facilities. Its overhead is typically no more than 10-20% (and often less).

2.  Scalene is **precise**. Unlike most other Python profilers, Scalene performs CPU profiling at the line level, pointing to the specific lines of code that are responsible for the execution time in your program. This level of detail can be much more useful than the function-level profiles returned by most profilers.

3.  Scalene separates out time spent running in Python from time spent in native code (including libraries). Most Python programmers aren\'t going to optimize the performance of native code (which is usually either in the Python implementation or external libraries), so this helps developers focus their optimization efforts on the code they can actually improve.

4.  Scalene profiles **memory usage**. In addition to tracking CPU usage, Scalene also points to the specific lines of code responsible for memory growth. It accomplishes this via an included specialized memory allocator.

5.  Scalene produces **per-line memory profiles**, making it easier to track down leaks.

6.  Scalene profiles **copying volume**, making it easy to spot inadvertent copying, especially due to crossing Python/library boundaries (e.g., accidentally converting numpy arrays into Python arrays, and vice versa).

See the [Scalene home page](https://github.com/emeryberger/scalene){.https} for installation and usage instructions.

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
:::
