# Oracle

::::: {#content dir="ltr" lang="en"}
# Oracle {#Oracle-1}

URL

:   [http://www.oracle.com/index.html](http://www.oracle.com/index.html){.http}

FAQ

:   [http://www.orafaq.com/](http://www.orafaq.com/){.http}

Wiki

:   [http://www.orawiki.com/](http://www.orawiki.com/){.http}

Wikipedia

:   [http://en.wikipedia.org/wiki/Oracle_database](http://en.wikipedia.org/wiki/Oracle_database){.http}

license

:   commercial/proprietary; free for development from [Oracle Technology Network](http://www.oracle.com/technology//index.html){.http}; [Oracle XE](http://www.oracle.com/technology/software/products/database/xe/index.html){.http} is free for production and development (and an excellent option all-around)

platforms
:   Unix, Linux, win32, win64

## Pros {#Pros}

- Reputation for being capable of handling large scale databases
- Typically the database system others compare themselves to

## Cons {#Cons}

- Usually requires bloated Oracle client installation on any machine that the app will run on
- Frequently the subject of migration discussions (to alternatives), usually for reasons of cost

------------------------------------------------------------------------

## DB API 2.0 Drivers {#DB_API_2.0_Drivers}

### cx_Oracle {#cx_Oracle}

URL

:   [http://cx-oracle.sourceforge.net/](http://cx-oracle.sourceforge.net/){.http}

licence

:   [BSD like](http://cx-oracle.sourceforge.net/LICENSE.txt){.http}

platforms
:   Unix, win32

Python versions
:   2.5 - 3.2

Oracle versions
:   10i - 11g

Last release
:   5.1 (March 19, 2011)

### DCOracle2 {#DCOracle2}

URL

:   [http://www.zope.org/Members/matt/dco2](http://www.zope.org/Members/matt/dco2){.http}

licence
:   ZPL

platforms
:   Unix, win32

Python versions

:   

Last release
:   1.3beta (Feb 10, 2003)

DCOracle2 targets Oracle 8i and up.

There also is DCOracle ([http://www.zope.org/Products/DCOracle/](http://www.zope.org/Products/DCOracle/){.http}) for the older Oracle 7 and 8 versions, but this is unmaintained.

### mxODBC {#mxODBC}

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/){.http}

Licence
:   eGenix Commercial License

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

mxODBC is compatible with the Oracle ODBC drivers on Windows and Unix, such as the ones included in the [Oracle Instant Client](http://www.oracle.com/technology/tech/oci/instantclient/index.html){.http}.

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

### OJDBC and JayDeBeApi {#OJDBC_and_JayDeBeApi}

URL

:   [http://pypi.python.org/pypi/JayDeBeApi](http://pypi.python.org/pypi/JayDeBeApi){.http}

licence
:   LGPL

platforms
:   Any (requires Java)

Python versions
:   Tested on CPython 2.6.6 and Jython 2.5.2

Oracle versions
:   Any supported by Oracle\'s JDBC drivers (currently 8.1.7 to 11.2.0.2.0)

Last release
:   0.1 (2010-08-16)

No [InstantClient](./InstantClient.html){.nonexistent} required. Download an Oracle JDBC driver (the filename will be something like ojdbc6.jar) from the [Oracle website](http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html){.http}, and set the classpath to include the driver. Note that if not running under Jython, JPype is required. Use code like the following:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-5408d7de2e0e6f44834d4284942402588154f19c dir="ltr" lang="en"}
   1 environ['JAVA_HOME'] = '/usr/lib/jvm/java-6-openjdk/jre'
   2 jpype.startJVM(jpype.getDefaultJVMPath(), '-Djava.class.path=ojdbc6.jar')
   3 conn = jaydebeapi.connect('oracle.jdbc.driver.OracleDriver', 'jdbc:oracle:thin:user/pass@server:1521:dbname')
```
:::
::::

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

mxODBC Connect Server is compatible with the [Oracle Instant Client](http://www.oracle.com/technology/tech/oci/instantclient/index.html){.http} ODBC drivers.

------------------------------------------------------------------------

## Supported Python Applications {#Supported_Python_Applications}

- [Zope](Zope)

- an Oracle (DCOracle and DCOracle2) driver exists for [PyDO](PyDO) (Python Data Objects)

## Web Links {#Web_Links}

[Oracle Forum](http://www.orafaq.com/forum){.http}

Oracle Wiki\'s: [English](http://www.orafaq.com/wiki){.http} [German](http://www.oracle-10g.de/oracle-wiki){.http}

Oracle Documentation: [10g](http://www.oracle-doku.de/oracle_10g_documentation/index.htm){.http} [9i](http://www.oracle-doku.de/oracle_9i_documentation/index.htm){.http} [8i](http://www.oracle-doku.de/oracle_8i_documentation/index.htm){.http} [7](http://www.oracle-doku.de/oracle_7_documentation/index.htm){.http}
:::::
