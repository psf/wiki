# JythonDeveloperGuide/PleaseAdoptMe

::: {#content dir="ltr" lang="en"}
## Getting to a 2.2 release {#Getting_to_a_2.2_release}

- **proper `__del__`{.backtick} support for user-defined new style classes** [Notes as I bootstrap into Jython](http://sourceforge.net/mailarchive/forum.php?thread_id=30988615&forum_id=5587){.http}

- **metaclasses, super and others are still broken** [Re: bugs 1603312 and 1603315](http://sourceforge.net/mailarchive/message.php?msg_id=37533518){.http}

- variety of bugs in tracker [status on new style classes](http://sourceforge.net/mailarchive/forum.php?thread_id=31129765&forum_id=5587){.http}

- Update the README.

- Update the copyright date in LICENSE.txt to 2006.

## What\'s needed for 2.3 {#What.27s_needed_for_2.3}

Samuele: The next big things that we can foresee are indeed **finding a solution for jythonc** and **improving our overloaded java methods resolution** so that it can behave properly once we introduce bools.

(extracted from [Re: Notes as I bootstrap into Jython](http://sourceforge.net/mailarchive/forum.php?thread_id=30988616&forum_id=5587){.http})

## Componentizing JAR Indexing {#Componentizing_JAR_Indexing}

[Componentizing JAR Indexing](http://sourceforge.net/mailarchive/forum.php?thread_id=30988620&forum_id=5587){.http}

Charles asked: How much effort would it take to **componentize the whole jar-indexing** subsystem? We\'d be interested in using it for \"import\" purposes in JRuby

Charlie replied: the indexing code could use a significant cleanup. It\'s mostly contained in the [PackageManager](./PackageManager.html){.nonexistent} class hierarchy. [SysPackageManager](SysPackageManager) extends [PathPackageManager](./PathPackageManager.html){.nonexistent} which extends [CachedJarsPackageManager](./CachedJarsPackageManager.html){.nonexistent} which extends [PackageManager](./PackageManager.html){.nonexistent}. Disentangling the interactions between that mess of inheritance makes working on the caching system harder than it should be.

Charles added: **making the dynlangs be able to call across each other** without some awful marshalling layer to/from java. In other words, we should be able to pass an object from JRuby to Jython to Rhino and read fields and invoke methods without difficulty. That\'s where a common underlying runtime or set of interfaces will be an absolute necessity.

## Compelling Goals {#Compelling_Goals}

(extracted from [Setting a compelling goal](http://sourceforge.net/mailarchive/forum.php?thread_id=30988621&forum_id=5587){.http}) Charles: Just supporting Python is not enough of a goal to compel folks to contribute precious off-hours to the project. Working toward support for apps like Django would do a lot more for publicity and project interest.

- django

- [TurboGears](./TurboGears.html){.nonexistent}

  - SQLObject and/or SQLAlchemy

  - [CherryPy](./CherryPy.html){.nonexistent} see [cherrypy 2.0.0](http://sourceforge.net/mailarchive/message.php?msg_id=37496554){.http} and [generators](http://sourceforge.net/mailarchive/forum.php?thread_id=31099865&forum_id=5587){.http}

  - Kid and/or Genshi

- Twisted (using [Alan Kennedy\'s select implementation](http://www.xhaus.com/alan/python/jynio/select.html){.http})

- WSGI (using [modjy](http://www.xhaus.com/modjy/index.html){.http})

- Trac
:::
