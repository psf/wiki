# DatabaseInterfaces

:::: {#content dir="ltr" lang="en"}
::: table-of-contents
Contents

1.  [Generic Database Interfaces and APIs](#Generic_Database_Interfaces_and_APIs)
    1.  [ODBC Support](#ODBC_Support)
    2.  [ADO Support](#ADO_Support)
2.  [Database Interfaces for Relational Database Systems](#Database_Interfaces_for_Relational_Database_Systems)
    1.  [General Purpose Database Systems](#General_Purpose_Database_Systems)
    2.  [Data Warehouse Database Systems](#Data_Warehouse_Database_Systems)
    3.  [Database Systems for Embedding Into Applications](#Database_Systems_for_Embedding_Into_Applications)
3.  [Non-Relational Databases](#Non-Relational_Databases)
    1.  [Record-based Databases](#Record-based_Databases)
    2.  [XML Databases](#XML_Databases)
    3.  [Graph Databases](#Graph_Databases)
4.  [Native Python Databases](#Native_Python_Databases)
:::

This page lists database interfaces available for Python. It may also help in finding a suitable database engine for you to use in your Python database applications.

# Generic Database Interfaces and APIs {#Generic_Database_Interfaces_and_APIs}

- The Python standard for database interfaces is the [Python DB-API (PEP 249)](http://www.python.org/dev/peps/pep-0249/){.http} Most Python database interfaces adhere to this standard.

- Most databases have ODBC support; see the section below on ODBC modules.

- Java databases usually support JDBC, and can be used from Jython.

- See also [DbApiModuleComparison](DbApiModuleComparison)

## ODBC Support {#ODBC_Support}

- See [ODBC](ODBC)

## ADO Support {#ADO_Support}

- See [ADO](ADO)

# Database Interfaces for Relational Database Systems {#Database_Interfaces_for_Relational_Database_Systems}

Database systems employing a relational model, with support for SQL.

## General Purpose Database Systems {#General_Purpose_Database_Systems}

- IBM [DB2](DB2)

- [Firebird](Firebird) (and Interbase)

- [Informix](Informix)

- [Ingres](Ingres)

- [MySQL](MySQL)

- [Oracle](Oracle)

- [PostgreSQL](PostgreSQL)

- [SAP DB](./SAP(20)DB.html) (also known as \"MaxDB\")

- Microsoft [SQL Server](./SQL(20)Server.html)

- Microsoft [Access](./Microsoft(20)Access.html)

- [Sybase](Sybase)

- [InterSystems IRIS](./InterSystems(20)IRIS.html)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## Data Warehouse Database Systems {#Data_Warehouse_Database_Systems}

- [Teradata](Teradata)

- IBM [Netezza](Netezza)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## Database Systems for Embedding Into Applications {#Database_Systems_for_Embedding_Into_Applications}

The following database systems are more oriented towards embedded applications:

- [asql](asql)

- [GadFly](./GadFly.html){.nonexistent}

- [SQLite](SQLite)

- [ThinkSQL](ThinkSQL)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

# Non-Relational Databases {#Non-Relational_Databases}

## Record-based Databases {#Record-based_Databases}

Databases working on flat files or fixed records.

- [MetaKit](MetaKit)

- [ZODB](ZODB)

- [BerkeleyDB](BerkeleyDB)

- [KirbyBase](KirbyBase)

- [Durus](Durus)

- [atop](./atop.html){.nonexistent}

- [buzhug](buzhug)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## XML Databases {#XML_Databases}

- 4Suite server

- Oracle/Sleepycat DB XML ([howto](http://jimmyg.org/blog/2008/oracle-db-xml-was-sleepycat.html){.http})

## Graph Databases {#Graph_Databases}

- [Neo4j](./Neo4j.html){.nonexistent}

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

# Native Python Databases {#Native_Python_Databases}

- [buzhug](buzhug)

- [SnakeSQL](SnakeSQL)
::::
