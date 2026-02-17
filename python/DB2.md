# DB2

::: {#content dir="ltr" lang="en"}
# IBM DB2 {#IBM_DB2}

## General Information {#General_Information}

URL

:   [http://www.ibm.com/db2](http://www.ibm.com/db2){.http}

licence
:   proprietary

platforms
:   Linux, UNIX, Windows, z/OS

------------------------------------------------------------------------

## DB API 2.0 Drivers {#DB_API_2.0_Drivers}

### ibm_db

URL

:   [https://github.com/ibmdb/python-ibmdb](https://github.com/ibmdb/python-ibmdb){.https}

licence
:   Apache License Version 2.0

platforms
:   OS Independent

Python versions

:   *to be specified*

### PyDB2 {#PyDB2}

URL

:   [http://sourceforge.net/projects/pydb2/](http://sourceforge.net/projects/pydb2/){.http}

licence
:   GNU Library or Lesser General Public License (LGPL)

platforms
:   OS Independent

Python versions

:   *to be specified*

### ceODBC {#ceODBC}

URL

:   [http://ceodbc.sourceforge.net/](http://ceodbc.sourceforge.net/){.http}

licence
:   GNU Library or Lesser General Public License (LGPL)

platforms
:   OS Independent

Python versions

:   *to be specified*

### pyodbc

URL

:   [https://github.com/mkleehammer/pyodbc](https://github.com/mkleehammer/pyodbc){.https}

License
:   MIT

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, Any (source provided)

Python versions
:   2.4 - 2.6

Actively maintained Open Source project.

Precompiled binaries are available for Windows. RedHat Enterprise Linux, Centos, and Fedora have precompiled RPMs available in their Extras repositories.

### mxODBC {#mxODBC}

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/){.http}

Licence
:   commercial

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

DB2\'s native CLI is ODBC compatible and mxODBC can link directly against these libraries on Unix. It also supports the DB2 ODBC driver on Windows, including the those for DB2 running on z/OS.

### mxODBC Connect {#mxODBC_Connect}

URL

:   [http://www.egenix.com/products/python/mxODBCConnect/](http://www.egenix.com/products/python/mxODBCConnect/){.http}

License
:   eGenix Commercial License 1.3.0

Platforms
:   Client: all Python platforms; Server: Windows, Linux

Python versions
:   2.5 - 2.7

mxODBC Connect is a commercial client-server product that allows connecting Python to ODBC compatible databases running on remote servers without requiring an ODBC driver on the client side. The product uses mxODBC on the server side and provides a highly portable Python library for the client side. As such it supports all database backend that mxODBC supports, but allows connecting to these from many different Python-supported platforms.

mxODBC Connect supports asynchronous query execution via the popular [gevent package](http://www.gevent.org/){.http}, provides secure certificate based authentication, SSL encrypted database connections, comes with full support for stored procedures, multiple result sets, Unicode, a common interface on all platforms and implements [many other useful features](http://www.egenix.com/products/python/mxODBCConnect/#Features){.http}.

mxODBC Connect Server is compatible with the IBM DB2 ODBC drivers.
:::
