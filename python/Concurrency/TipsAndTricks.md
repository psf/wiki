# Concurrency/TipsAndTricks

::::::: {#content dir="ltr" lang="en"}
# Concurrency Tips & Tricks {#Concurrency_Tips_.26_Tricks}

## Use with statement to manage locks {#Use_with_statement_to_manage_locks}

Starting in Python 2.5, the `with`{.backtick} statement is a far easier way to manage locks:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-efb4ef2d8dfffad4fdfc4b35b7e015cb75fa2108 dir="ltr" lang="en"}
   1 some_lock = threading.Lock()
   2 
   3 with some_lock:
   4     do_stuff_requiring_lock()
```
:::
::::

This is equivalent to:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-09f0ef092b3b2c6926e00ef4eb278b3e1297d680 dir="ltr" lang="en"}
   1 some_lock = threading.Lock()
   2 
   3 some_lock.acquire():
   4 try:
   5     do_stuff_requiring_lock()
   6 finally:
   7     some_lock.release()
```
:::
::::

## Adjust checkinterval {#Adjust_checkinterval}

Increasing the [check interval](http://docs.python.org/library/sys.html#sys.setcheckinterval){.http} may improve performance for CPU-bound multithreaded programs, at the cost of I/O responsiveness.
:::::::
