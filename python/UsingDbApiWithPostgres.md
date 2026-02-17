# UsingDbApiWithPostgres

::::::::::::::::::::::: {#content dir="ltr" lang="en"}
# Use cases of the DB API for a PostgreSQL database

  ------------ -----------------------------------------------------
  Author:      Pavel Vinogradov
  Version:     1.0.1
  Copyright:   This document has been placed in the public domain.
  ------------ -----------------------------------------------------

::: {#contents .contents .topic}
Contents

- [Introduction](#introduction){#id1 .reference .internal}
- [Python DB-API](#python-db-api){#id2 .reference .internal}
- [PostgreSQL](#postgresql){#id3 .reference .internal}
- [Python interfaces to PostgreSQL](#python-interfaces-to-postgresql){#id4 .reference .internal}
  - [PyGreSQL](#pygresql){#id5 .reference .internal}
  - [pyPgSQL](#pypgsql){#id6 .reference .internal}
  - [psycopg2](#psycopg2){#id7 .reference .internal}
- [Basic examples](#basic-examples){#id8 .reference .internal}
  - [Getting Started](#getting-started){#id9 .reference .internal}
  - [Create database](#create-database){#id10 .reference .internal}
  - [Create table](#create-table){#id11 .reference .internal}
  - [Add data](#add-data){#id12 .reference .internal}
  - [Retrieve data](#retrieve-data){#id13 .reference .internal}
  - [Delete data](#delete-data){#id14 .reference .internal}
  - [Close Connection](#close-connection){#id15 .reference .internal}
- [Advanced examples](#advanced-examples){#id16 .reference .internal}
  - [Advanced querying](#advanced-querying){#id17 .reference .internal}
  - [Transactions](#transactions){#id18 .reference .internal}
- [References](#references){#id19 .reference .internal}
:::

::: {#introduction .section}
### [Introduction](#id1){.toc-backref}

Python lets you write programs that access, display and update the information in the database with minimal effort.

There are lots of commercial and freeware databases available, and most of them provide Structured Query Language (SQL) for retrieving and adding information. However, while most databases have SQL in common, the details of how to perform an SQL operation vary. The various individuals who wrote the Python database modules invented their own interfaces, and the resulting proliferation of different Python modules caused problems: no two of them were exactly alike, so if you decided to switch to a new database product, you had to rewrite all the code that retrieved and inserted data.

To solve the problem, a Special Interest Group (or SIG) for databases was formed. After some discussion, the Database SIG produced a specification for a consistent interface to relational databases \-- the DB-API.
:::

::: {#python-db-api .section}
### [Python DB-API](#id2){.toc-backref}

Thanks to DB-API specification, there\'s only one interface to learn. Porting code to use a different database product is much simpler, often requiring the change of only a few lines.

This API has been defined to encourage similarity between the Python modules that are used to access databases. By doing this, we hope to achieve a consistency leading to more easily understood modules, code that is generally more portable across databases, and a broader reach of database connectivity from Python.

Current version of DB-API is 2.0 (PEP 249) replaced older DB-API 1.0 version (PEP 248). Modules for most known relational databases now conform to DB-API 2.0 (or at least 1.0)
:::

::: {#postgresql .section}
### [PostgreSQL](#id3){.toc-backref}

**PostgreSQL** is a powerful, open source relational database system. It has more than 15 years of active development and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness. It runs on all major operating systems.

It includes most SQL92 and SQL99 data types. It also supports storage of binary large objects, including pictures, sounds, or video. It has native programming interfaces for C/C++, Java, .Net, Perl, Python, Ruby, Tcl, ODBC, among others.

[PostgreSQL homepage](http://www.postgresql.org/){.http .reference .external}
:::

:::::: {#python-interfaces-to-postgresql .section}
### [Python interfaces to PostgreSQL](#id4){.toc-backref}

::: {#pygresql .section}
#### [PyGreSQL](#id5){.toc-backref}

> **PyGreSQL** is an open-source Python module that interfaces to a PostgreSQL database. It embeds the PostgreSQL query library to allow easy use of the powerful PostgreSQL features from a Python script.
>
> [PyGreSQL homepage](http://www.pygresql.org/){.http .reference .external}
:::

::: {#pypgsql .section}
#### [pyPgSQL](#id6){.toc-backref}

> **pyPgSQL** is a package of two modules that provide a Python DB-API 2.0 compliant interface to PostgreSQL databases. The first module, libpq, exports the PostgreSQL C API to Python. This module is written in C and can be compiled into Python or can be dynamically loaded on demand. The second module, PgSQL, provides the DB-API 2.0 compliant interface.
>
> [pyPgSQL homepage](http://pypgsql.sourceforge.net/){.http .reference .external}
:::

::: {#psycopg2 .section}
#### [psycopg2](#id7){.toc-backref}

> **psycopg2** is a PostgreSQL database adapter for the Python programming language. Its main advantages are that it supports the full Python DBAPI 2.0 and it is thread safe at level 2. It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a conspicuous number of concurrent INSERTs or UPDATEs.
>
> [psycopg homepage](http://initd.org/psycopg/){.http .reference .external}
:::
::::::

:::::::::: {#basic-examples .section}
### [Basic examples](#id8){.toc-backref}

All examples tested on Python 2.4.4 and PostgreSQL 8.2 under Debian GNU/Linux 4.0, but should work on greater Python versions and other operational systems.

This part will take you on a fast tour of the main features of DB-API 2.0, showing howto:

- open a connection to the database
- create cursor
- execute various query
- close connection

All listed examples include SQL and DB-API version of actions.

::: {#getting-started .section}
#### [Getting Started](#id9){.toc-backref}

For the first time we need to run python interpreter, import database module (e.g. psycopg2) and connect to database. Also we need to obtain a **cursor** object, which acts as a handle for a given SQL query; it allows retrieval of one or more rows of the result, until all the matching rows have been processed.

**Python DB-API**:

    import psycopg2 as dbapi2
    db = dbapi2.connect (database="python", user="python", password="python")
    cur = db.cursor()
:::

::: {#create-database .section}
#### [Create database](#id10){.toc-backref}

Usually your system administrator must create databases for you, but if you use your own PostgreSQL server you can do it without assistance.

**SQL**:

    CREATE DATABASE python;
:::

::: {#create-table .section}
#### [Create table](#id11){.toc-backref}

The created database is empty, so it doesn\'t contain any user tables or data. We must create a new table and specify its columns.

**SQL**:

    CREATE TABLE versions (released date, version varchar, status varchar);

**DB-API 2.0**:

    cur.execute ("""CREATE TABLE versions (released date, version varchar, status varchar)""")
:::

::: {#add-data .section}
#### [Add data](#id12){.toc-backref}

To insert data into the table we can use the execute method of the cursor object. Use the commit() method to commit, i.e. make permanent, the changes to the database.

**SQL**:

    INSERT INTO versions VALUES ('2007-10-18', '2.4.4', 'stable');
    INSERT INTO versions VALUES ('2007-04-18', '2.5.1', 'stable');
    INSERT INTO versions (version, status) VALUES ('2.6.0', 'devel')
    INSERT INTO versions (verson, status) VALUES ('3.0.0', 'alpha')

**DB-API 2.0**:

    cur.execute ("INSERT INTO versions VALUES ('2007-10-18', '2.4.4', 'stable')")
    cur.execute ("INSERT INTO versions VALUES ('2007-04-18', '2.5.1', 'stable')")
    cur.execute ("INSERT INTO versions (version, status) VALUES ('2.6.0', 'devel')")
    cur.execute ("INSERT INTO versions (version, status) VALUES ('3.0.0', 'alpha')")
    conn.commit ()
:::

::: {#retrieve-data .section}
#### [Retrieve data](#id13){.toc-backref}

Use the execute function to run sql SELECT queries.

**SQL**:

    SELECT * FROM versions;

**DB-API 2.0**:

    cur.execute ("SELECT * FROM versions");
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print "Row", i, "value = ", row

    Row 0 value =  (datetime.date(2007, 10, 18), '2.4.4', 'stable')
    Row 1 value =  (datetime.date(2007, 4, 18), '2.5.1', 'stable')
    Row 2 value =  (None, '2.6.0', 'devel')
    Row 3 value =  (None, '3.0.0', 'alpha')
:::

::: {#delete-data .section}
#### [Delete data](#id14){.toc-backref}

Use the execute function to run sql DELETE or DROP TABLE. You don\'t need to delete all the rows from the table before dropping it.

**SQL**:

    DELETE FROM versions;
    DROP TABLE versions;

**DB-API 2.0**:

    cur.execute ("DELETE FROM versions")
    cur.execute ("DROP TABLE versions")
:::

::: {#close-connection .section}
#### [Close Connection](#id15){.toc-backref}

When you finish work with a cursor or database, closing the cursor and connection is good practice (but isn\'t necessary).

**DB-API 2.0**:

    cur.close()
    db.close()
:::
::::::::::

::::: {#advanced-examples .section}
### [Advanced examples](#id16){.toc-backref}

::: {#advanced-querying .section}
#### [Advanced querying](#id17){.toc-backref}

You can use all the normal SQL operators like WHERE, GROUP BY, ORDER BY, etc in queries which execute through the execute() method of a cursor object. But be careful when you use database dependent operators, because your code will depends on used database.

**SQL**:

    SELECT * FROM versions WHERE status = 'stable' ORDER BY version DESC;

**DB-API 2.0**:

    cur.execute ("""SELECT * FROM versions WHERE status = 'stable' ORDER BY version DESC;""")
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print "Row", i, "value = ", row

    Row 0 value =  (datetime.date(2007, 4, 18), '2.5.1', 'stable')
    Row 1 value =  (datetime.date(2007, 10, 18), '2.4.4', 'stable')
:::

::: {#transactions .section}
#### [Transactions](#id18){.toc-backref}

For databases that support transactions, the Python interface silently starts a transaction when the cursor is created. The commit() method commits the updates made using that cursor, and the rollback() method discards them. Each method then starts a new transaction. Some databases don\'t have transactions, but simply apply all changes as they\'re executed. On these databases:

> - commit() does nothing, but you should still call it in order to be compatible with those databases that do support transactions.
> - rollback() should throw an exception or not be implemented.

**SQL**:

    BEGIN TRANSACTION;
    UPDATE versions SET status='stable' where version='2.6.0';
    UPDATE versions SET status='old' where version='2.4.4';
    SELECT * FROM versions;
    released  | version | status
    ------------+---------+--------
    2007-04-18 | 2.5.1   | stable
               | 3.0.0   | alpha
               | 2.6.0   | stable
    2007-10-18 | 2.4.4   | old
    ROLLBACK
    SELECT * FROM versions;
    released  | version | status
    ------------+---------+--------
    2007-10-18 | 2.4.4   | stable
    2007-04-18 | 2.5.1   | stable
               | 2.6.0   | devel
               | 3.0.0   | alpha

**DB-API 2.0**:

    try:
        cur.execute ("""UPDATE versions SET status='stable' where version='2.6.0' """)
        cur.execute ("""UPDATE versions SET status='old' where version='2.4.4' """)
        db.commit()
    except Exception, e:
        db.rollback()
:::
:::::

::: {#references .section}
### [References](#id19){.toc-backref}

1.  The Python DB-API interface [http://www.amk.ca/python/writing/DB-API.html](http://www.amk.ca/python/writing/DB-API.html){.http .reference .external} by Andrew Kuchling
2.  Python Database API Specification v2.0 [http://www.python.org/dev/peps/pep-0249/](http://www.python.org/dev/peps/pep-0249/){.http .reference .external}
3.  Accessing Databases using the Python DBAPI-2.0 [http://www.initd.org/pub/software/psycopg/dbapi20programming.pdf](http://www.initd.org/pub/software/psycopg/dbapi20programming.pdf){.http .reference .external}
:::
:::::::::::::::::::::::
