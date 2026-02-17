# UsingPickle

::::::: {#content dir="ltr" lang="en"}
# Using Pickle {#Using_Pickle}

- [Official Pickle Use Documentation](http://docs.python.org/library/pickle.html#data-stream-format){.http}

- [Official Pickle Module Documentation](https://docs.python.org/3/library/pickle.html#module-pickle){.https}

## Pickle Example {#Pickle_Example}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4432c9c973c553ebd06665a3edc404c23544eb46 dir="ltr" lang="en"}
   1 # Save a dictionary into a pickle file.
   2 import pickle
   3 
   4 favorite_color = { "lion": "yellow", "kitty": "red" }
   5 
   6 pickle.dump( favorite_color, open( "save.p", "wb" ) )
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-10a60777cc6a4f82f809e00de9efde0d29c23f9f dir="ltr" lang="en"}
   1 # Load the dictionary back from the pickle file.
   2 import pickle
   3 
   4 favorite_color = pickle.load( open( "save.p", "rb" ) )
   5 # favorite_color is now { "lion": "yellow", "kitty": "red" }
```
:::
::::

For more examples and API details, see the [official Pickle use documentation.](http://docs.python.org/library/pickle.html){.http}

## Flying Pickle Alert! {#Flying_Pickle_Alert.21}

Pickle files can be hacked. If you receive a raw pickle file over the network, *don\'t trust it!* It could have malicious code in it, that would run arbitrary python when you try to de-pickle it.

However, if you are doing your own pickle writing and reading, you\'re safe. (Provided no one else has access to the pickle file, of course.)

## What can you Pickle? {#What_can_you_Pickle.3F}

Generally you can pickle any object if you can pickle every attribute of that object. Classes, functions, and methods cannot be pickled \-- if you pickle an object, the object\'s class is not pickled, just a string that identifies what class it belongs to. This works fine for most pickles (but note the discussion about long-term storage of pickles).

With pickle protocol v1, you *cannot* pickle open file objects, network connections, or database connections. When you think about it, it makes sense \-- pickle cannot will the connection for file object to exist when you unpickle your object, and the process of creating that connection goes beyond what pickle can automatically do for you. If you really want to pickle something that has an attribute that is causing problems, look at the pickle documentation for `__getstate__`, `__setstate__`, and `__getinitargs__` \-- using these you can exclude problematic attributes.

With pickle protocol v2, you are able to pickle open file objects. This will change in a future version of Python. See [this bug report](http://bugs.python.org/issue10180){.http} for more information.

See [the pickle documentation](https://docs.python.org/3/library/pickle.html#data-stream-format){.https} for more recent protocols (up to v5 as of Python 3.8).

## Contributors {#Contributors}

[LionKimbro](LionKimbro), [IanBicking](IanBicking), [lwickjr](lwickjr)

## Discussion {#Discussion}

Pickles can cause problems if you save a pickle, then update your code and read the pickle in. Attribute added to your `__init__` may not be present in the unpickled object; also, if pickle can\'t find your class and module (e.g., if you renamed the module) you will get errors. However you can handle renaming modules and classes as described in [UsingPickle/RenamingModules](./UsingPickle(2f)RenamingModules.html)

For this reason, you should be wary of using pickles for long-term storage where the underlying code is not highly stable.

[\[lwickjr](./(5b)lwickjr.html){.nonexistent}\]: Another possibility re unpicklable objects is to register pickling and unpickling functions with `copy_reg`. Regarding renaming modules/classes/functions: I\'ve had to deal with this repeatedly in my own code. I have developed an ad-hock procedure that works for me:

- 1 Edit the source code to create the object under the new name AND store a copy under the old name. 2 Unpickle and re-pickle EVERY pickle affected by the change. 3 Edit the source code to remove storing the new object under the old name.

A more robust approach would be to perform step one above, and just leave it at that, in case you missed a pickle or two. If desired, you can then perform step 3 after you judge normal processing to have performed step 2 for you, say, a couple years later. ![;)](/wiki/europython/img/smile4.png ";)"){height="16" width="16"}

Awkward, but it works. Anyone have any ideas for a better way to do this? \--[lwickjr](lwickjr)
:::::::
