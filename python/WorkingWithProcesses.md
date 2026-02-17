# WorkingWithProcesses

::::: {#content dir="ltr" lang="en"}
These are just some notes about working with processes in Python.

The module of interest is `os`. [(os module documentation)](http://www.python.org/doc/current/lib/module-os.html){.http}

Environment variables are accessed through a dictionary, `os.environ`.

Processes are created with `os.popen`, [described in os 6.1.2.](http://www.python.org/doc/current/lib/os-newstreams.html#os-newstreams){.http}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-6094bc9f3bdb5b1256a217c1f6daf6de4a560023 dir="ltr" lang="en"}
   1 import os
   2 
   3 # Export an environment variable
   4 os.environ["FOO"] = "BAR"
   5 
   6 # Make sure environment variable set for child processes
   7 for line in os.popen("bash -c 'env'").read().splitlines():
   8     if line.startswith("FOO="):
   9         print line
  10 
  11 # Since environment variable "FOO" is exported, and since child
  12 # processes inherit environment variables from their parents, this
  13 # works.
```
:::
::::
:::::
