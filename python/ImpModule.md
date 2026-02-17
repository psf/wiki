# ImpModule

::::::::::: {#content dir="ltr" lang="en"}
The **imp module** lets you load a module at run-time, knowing just the name of the module.

## Playing with imp Module {#Playing_with_imp_Module}

Make a file \"eraseme.py\":

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-eff17bf30ad866ebae42ccc1df19f3b43a8fd33d dir="ltr" lang="en"}
   1 print "Successfully imported!"
```
:::
::::

Then, at the python shell,

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-d8eb8d59e3b99dae623bfc6514f1396ef6a73f29 dir="ltr" lang="en"}
   1 >>> import imp
   2 >>> returned = imp.find_module("eraseme", ["."])
   3 >>> returned
   4 (<open file 'eraseme.py', mode 'U' at 0xb7f62220>, 'eraseme.py', ('.py', 'U', 1))
   5 >>>
```
:::
::::

The `find_module` line searches for \"eraseme\" in the current working directory (\".\").

The first two returned items are self-explanatory, but what about that tuple- `('.py', 'U', 1)` ..?

The first (\".py\") is obviously the extension.

\'U\' means, \"I opened the file in [UniversalNewline](./UniversalNewline.html){.nonexistent} mode.\" Basically, universal newline mode is like read (\"r\"), except that it interprets all newline forms the same way.

Finally, the 1 is a code that matches against imp.PY_SOURCE (1), imp.PY_COMPILED (2), or imp.C_EXTENSION (3). Basically, it\'s telling us that the .py file is a source file.

Once you have this stuff, it\'s easy to load:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-e40e96a1e68239c1485ea4ce5d383d10f61399d3 dir="ltr" lang="en"}
   1 >>> eraseme = imp.load_module("eraseme", returned[0], returned[1], returned[2])
   2 successfully imported!
   3 >>> eraseme
   4 <module 'eraseme' from './eraseme.py'
```
:::
::::

Note that, you don\'t have to play by the rules. If you wanted to, you could have said:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-d379fe3fbed8ad8365e556a942e91f9cf32de1a0 dir="ltr" lang="en"}
   1 >>> module = imp.load_module("eggs", returned[0], "spam.py", returned[2])
   2 successfully imported!
   3 >>> module
   4 <module 'eggs' from 'spam.py'>
   5 >>> dir(module)
   6 ['__builtins__', '__doc__', '__file__', '__name__']
   7 >>> module.__name__
   8 'eggs'
   9 >>> module.__file__
  10 'spam.py'
  11 >>>
```
:::
::::

\...even though the file\'s *real* name is \"eggs.py\".

## See Also {#See_Also}

- [ModulesAsPlugins](ModulesAsPlugins)

- [Python documentation for imp module](http://docs.python.org/lib/module-imp.html){.http}

# Discussion {#Discussion}

- (none yet!)
:::::::::::
