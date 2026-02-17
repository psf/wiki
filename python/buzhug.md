# buzhug

:::: {#content dir="ltr" lang="en"}
::: table-of-contents
Contents

1.  [General Information](#General_Information)
2.  [Programming Model](#Programming_Model)
3.  [Pros](#Pros)
4.  [Cons](#Cons)
:::

## General Information {#General_Information}

URL

:   [http://buzhug.sourceforge.net](http://buzhug.sourceforge.net){.http}

licence
:   BSD

platforms
:   all platforms supporting Python 2.3+

## Programming Model {#Programming_Model}

buzhug is a fast, portable, pure-Python database engine, using a pythonic non-SQL syntax for all operations

A database is an iterator, yielding objects with attributes matching the fields defined for the base . Requests can be expressed as list comprehensions or generator expressions, instead of SQL.

The data is stored and accessed on disk (it is not an in-memory database). The implementation has been designed to make all operations, and especially selection, as fast as possible with an interpreted language.

A limited benchmark using the same use cases as SQLite\'s author shows that buzhug is much faster than other pure-Python modules ([KirbyBase](KirbyBase), gadfly). SQLite, which is implemented in C, is faster, but only less than 3 times on the average.

## Pros {#Pros}

- most operations are faster than on other pure-Python databases
- concurrency control by versioning of records
- simple system to link databases dynamically (a record of a base can be a field of another base)
- complete documentation

## Cons {#Cons}

- still beta : bug reports needed
- no thread-safe feature : should be used behind an asynchronous server for multiple users
::::
