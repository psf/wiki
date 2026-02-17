# Iterator

::::::::: {#content dir="ltr" lang="en"}
An **iterable** object is an object that implements `__iter__`, which is expected to return an **iterator** object.

An **iterator** object implements `__next__`, which is expected to return the next element of the iterable object that returned it, and to raise a `StopIteration` exception when no more elements are available.

In the simplest case, the iterable will implement `__next__` itself and return `self` in `__iter__`. However, this has its limitations and may produce unexpected results in concurrent environments (e.g. with the multiprocessing API).

You can use iterables in for loops, to construct lists with list comprehensions, or as input arguments for the `list` function.

## Example Iterator {#Example_Iterator}

Here is an iterator that returns a random number of 1\'s:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c24cec6c5535b3b63560f9c3b997f013f7351d06 dir="ltr" lang="en"}
   1 import random
   2 
   3 class RandomIterable:
   4     def __iter__(self):
   5         return self
   6     def __next__(self):
   7         if random.choice(["go", "go", "stop"]) == "stop":
   8             raise StopIteration  # signals "the end"
   9         return 1
```
:::
::::

**Q:** Why is `__iter__` there, if it just returns self?

**A:** This is a very simple case. More complex iterables may very well return separate iterator objects.

**Q:** When would I need an extra iterator?

**A:** Iterators will typically need to maintain some kind of position state information (e.g., the index of the last element returned). If the iterable maintained that state itself, it would become inherently non-reentrant (meaning you could use it only one loop at a time).

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-aa0df00b1b47cc5b1a8b23e1364e421ddd753794 dir="ltr" lang="en"}
   1 for eggs in RandomIterable():
   2     print(eggs)
```
:::
::::

You can also use it in list construction:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-05c109f8bedd918fe68419fab53bb8d621267183 dir="ltr" lang="en"}
   1 >>> list(RandomIterable())
   2 [1]
   3 >>> list(RandomIterable())
   4 []
   5 >>> list(RandomIterable())
   6 [1, 1, 1, 1, 1]
   7 >>> list(RandomIterable())
   8 [1]
```
:::
::::

\...both of these uses require `__iter__`.

An object isn\'t iterable unless it provides `__iter__`. And for an object to be a valid iterator, it must provide `__next__`.

## Manual usage {#Manual_usage}

Although you won\'t need this in most cases, you can manually get the iterator from an iterable object by using the `iter()` function. Similary, you can manually call `__next___` using the `next()` function.

## Links {#Links}

- [PEP-234: Iterators](http://www.python.org/peps/pep-0234.html){.http}

- [Itertools: Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html){.https}

- [Functional programming and iterators](https://docs.python.org/3/howto/functional.html?highlight=iterator#functional-howto-iterators){.https}

- [Python iterator basics (how they work + examples)](https://python.land/deep-dives/python-iterator){.https}

See also: [Generators](Generators)
:::::::::
