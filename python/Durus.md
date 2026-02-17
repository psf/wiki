# Durus

:::: {#content dir="ltr" lang="en"}
::: table-of-contents
Contents

1.  [Masthead](#Masthead)
2.  [DB API 2.0 Drivers](#DB_API_2.0_Drivers)
    1.  1.  [Comments](#Comments)
        2.  [Programming Model](#Programming_Model)
        3.  [Comments](#Comments-1)
3.  [Supported Python applications](#Supported_Python_applications)
4.  [Pros](#Pros)
5.  [Cons](#Cons)
:::

## Masthead {#Masthead}

URL

:   [https://pypi.python.org/pypi/libdurus/4.0.0](https://pypi.python.org/pypi/libdurus/4.0.0){.https}

License
:   MIT

Platforms

:   Python 2.7, PyPy 5.9, Python 3.5

Version
:   4.0.0

Maintainer
:   The current libdurus port maintainer may be contacted at tkadm30\[dot\]yandex.ru

## DB API 2.0 Drivers {#DB_API_2.0_Drivers}

Not applicable. Durus is an object database, similar in approach to ZODB.

#### Comments {#Comments}

Durus is a persistent object system for applications written in the Python programming language. Durus offers an easy way to use and maintain a consistent collection of object instances used by one or more processes. Access and change of a persistent instances is managed through a cached Connection instance which includes commit() and abort() methods so that changes are transactional.

#### Programming Model {#Programming_Model}

The programming interface is nearly the same as ZODB (Durus is heavily influenced by the ZODB design). Durus aggressively caches data and does not do locking. As a result it performs very well for applications do mostly reading and only a little writing. See the [FAQ](http://www.mems-exchange.org/software/durus/doc/FAQ.html){.http}

#### Comments {#Comments-1}

## Supported Python applications {#Supported_Python_applications}

- [Schevo](Schevo)

## Pros {#Pros}

- Supports epoll through the python-epoll extension.

## Cons {#Cons}
::::
