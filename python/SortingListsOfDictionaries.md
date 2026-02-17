# SortingListsOfDictionaries

::::::::: {#content dir="ltr" lang="en"}
# Sorting Lists of Dictionaries {#Sorting_Lists_of_Dictionaries}

Frequently you want to sort a list of dictionaries, based on some particular key.

For example:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-bf244c142dd0ba253896c0e80a31f909bced79fc dir="ltr" lang="en"}
   1 a = {"key1": 5 , "key2": 8, "key3": 2}
   2 b = {"key1": 7 , "key2": 4, "key3": 9}
   3 c = {"key1": 6 , "key2": 1, "key3": 1}
   4 undecorated = [a, b, c] # how do you sort this list?
```
:::
::::

There are many ways to do this. Here\'s the fastest way to do it, as it avoids using a custom comparison function, instead using builtin comparisons. This is the *decorate-sort-undecorate* pattern, or the *Schwartzian transform* if you\'re coming from Perl.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-52826bb154fe5c2a4597a28eb370b949d86a14b5 dir="ltr" lang="en"}
   1 sort_on = "key2"
   2 decorated = [(dict_[sort_on], dict_) for dict_ in undecorated]
   3 decorated.sort()
   4 result = [dict_ for (key, dict_) in decorated]
```
:::
::::

(The variable was named `dict_` because `dict` is already a builtin.)

Starting with Py2.4 the `list.sort()` method provides a `key=` argument for doing the transform in a single step. The new `sorted()` built-in function goes a step further and encapsulates making a new sorted list while leaving the original intact. Also, the new `operator.itemgetter()` function helps by constructing functions for key access:

    >>> from operator import itemgetter
    >>> result = sorted(undecorated, key=itemgetter('key2'))

This will sort on arbitrary multiple columns of the dictionary.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-2ca4aa382a5cdfc5557b04b8a78e755788b56577 dir="ltr" lang="en"}
   1 def multikeysort(items, columns):
   2     from operator import itemgetter
   3     comparers = [ ((itemgetter(col[1:].strip()), -1) if col.startswith('-') else (itemgetter(col.strip()), 1)) for col in columns]
   4     def comparer(left, right):
   5         for fn, mult in comparers:
   6             result = cmp(fn(left), fn(right))
   7             if result:
   8                 return mult * result
   9         else:
  10             return 0
  11     return sorted(items, cmp=comparer)
```
:::
::::

You can call it like this:

    >>> result = multikeysort(undecorated, ['key1', 'key2', 'key3'])

Column names preceded by \'-\' are sorted in descending order:

    >>> result = multikeysort(undecorated, ['-key1', '-key2', '-key3'])

## See Also {#See_Also}

- [HowTo/Sorting](./HowTo(2f)Sorting.html)
:::::::::
