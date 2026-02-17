# HigherLevelDatabaseProgramming

::: {#content dir="ltr" lang="en"}
There are several wrappers that provide improved or simplified interfaces to SQL databases. Some of these might be referred to as object relational mappers, or ORM in this list \-- these create Pythonic objects out of database rows. Others may only help generate SQL, or provide simple mapping support.

# Object Relational Mappers (ORMs) {#Object_Relational_Mappers_.28ORMs.29}

- [Axiom](https://github.com/twisted/axiom/){.https}: MIT-licensed, SQLite-based

- [Bazaar ORM](http://www.nongnu.org/bazaar/){.http}: Easy to use and powerful abstraction layer between relational database and object oriented application.

- [dal.py](http://code.google.com/p/web2py/source/browse/gluon/dal.py){.http}: a Database Abstraction Layer (DAL), an API that maps Python objects into database objects such as queries, tables, and records. [101 video](http://vimeo.com/20760298){.http} (This module is normally distributed as part of web2py but it does not depend on web2py, except for few some web2py specific functionalities)

- [DbObj](DbObj): ORM

- [Dejavu](http://www.aminus.net/dejavu){.http}: Public domain, thread-safe, Data Mapper ORM. (latest rel. 1.5 dd. 2007-01-24)

- [forgetSQL](http://forgetsql.sourceforge.net/){.http}: ORM

- [libschevo](https://pypi.python.org/pypi/libschevo/3.2.10/){.https}: Next-generation Object-Oriented DBMS.

- [MiddleKit](MiddleKit): ORM

- [Modeling Object-Relational Bridge](http://modeling.sourceforge.net/){.http}: ORM and schema design with Zope integration

- [Object Relational Membrame](http://orm.nongnu.org/){.http} ([Freshmeat entry](http://freshmeat.net/projects/orm/){.http}): ORM

- [ORB](http://docs.projexsoftware.com/api/orb){.http}: easy to use ORM with Pythonic query markup language for multiple databases, works with the [Orbiter](http://www.projexsoftware.com/products/orbiter){.http} ORM designer

- [PyDo](./PyDo.html): ORM

- [quick_orm](http://pypi.python.org/pypi/quick_orm/){.http}: ORM on top of SQLAlchemy to make things simple

- [SQLObject](http://sqlobject.org/){.http}: ORM

- [SQLAlchemy](http://www.sqlalchemy.org/){.http}: SQL Toolkit and ORM

- [Storm](https://storm.canonical.com){.https}: Clean and powerful ORM by Canonical.

# SQL Wrappers & Generators {#SQL_Wrappers_.26_Generators}

- [db_row](http://opensource.theopalgroup.com/){.http}: SQL result wrapper

- [gnue-common](http://gnuenterprise.org/tools/common/){.http}: gnue.common.datasources module - Database abstraction layer

- [Roundup\'s hyperdb](http://roundup.sf.net/){.http}: set of constrained data types with relations (many-to-many included) over multiple backends including SQL, metakit and db (yes, relations in an anydbm-backed database ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}

- [ll.sql](http://www.livinglogic.de/Python/sql/){.http}: SQL generator

- [PDO](http://pdo.neurokode.com){.http}: Python Database Objects - allows use of most DBAPI modules with a clean, simple API similar in scope to ADO or JDBC. Column access by name is provided by a low overhead mechanism.

- [pySQLFace](https://fedorahosted.org/pySQLFace/){.https}: SQL interface over DBAPI2. It provides a database specific API to retrive and save data by creating SQL/DML command objects from a configuration file.

- [PyTable](PyTable)

- The [PythonWebModules](PythonWebModules) web.database module - Database abstraction layer to make it possible to run the same SQL on different databases without changing your code.

- The [PythonWebModules](PythonWebModules) web.database.object module - ORM - treat an SQL database like python objects for easy programming, the SQL is done behind the scenes. Supports one and many to many mappings and can generate HTML forms for the data automatically.

- QLime ([Freshmeat entry](http://freshmeat.net/projects/qlime/){.http}): Easy to use, transparent data access to relational databases or other data sources. See examples here: [http://www.qlime-project.org/example.rst](http://www.qlime-project.org/example.rst){.http}

- [simpleQL](http://www.python.org/pypi/simpleQL){.http}: SQL generator using live translation of generator expressions

- [SQLBuilder](http://py.vaults.ca/apyllo2.py/D21777795){.http}: SQL generator

- [SQLDict](http://dustman.net/andy/python/SQLDict){.http}: SQL wrapper

- [prototype SchemQL/Roe-like thing in Python](http://lists.canonical.org/pipermail/kragen-hacks/2004-April/000394.html){.http} \-\-- Python objects representing relational algebra expressions, backed by lazy compilation to SQL and an iterable interface.

# Relational Python {#Relational_Python}

- [Dee](http://www.quicksort.co.uk){.http}: A proposal to supersede SQL and the need for database sub-languages. Adds truly relational capabilities to Python (no wrappers, no mappers).

See also [PersistenceSystems](http://www.thinkware.se/cgi-bin/thinki.cgi/PersistenceSystems "Thinki"){.interwiki} and [ObjectOrientedDatabase](http://www.thinkware.se/cgi-bin/thinki.cgi/ObjectOrientedDatabase "Thinki"){.interwiki}

## Editorial Notes {#Editorial_Notes}

The above lists should be arranged in ascending alphabetical order - please respect this when adding new entries. When specifying release dates please use the format YYYY-MM-DD.

------------------------------------------------------------------------
:::
