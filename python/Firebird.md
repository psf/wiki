# Firebird

::: {#content dir="ltr" lang="en"}
# Firebird {#Firebird-1}

URL

:   [https://firebirdsql.org](https://firebirdsql.org/){.https}

licence
:   Interbase Public License, Initial Developer Public License

platforms
:   Unix, Win 32/x64, Mac OS X

## Pros {#Pros}

- Powerful and stable cross-platform database

- Extensive SQL standards support

- Python driver binary distribution available for : Mageia ,Fedora, Redhat , FreeBSD (Debian, Ubuntu will come soon) but you can to compile and install easily for other platforms : [here](http://mapopa.blogspot.ro/2012/04/i-love-pip-install.html){.http} is the Howto install it on Ubuntu with pip.

------------------------------------------------------------------------

## DB API 2.0 Drivers {#DB_API_2.0_Drivers}

#### Python 2.x-3.x Driver (Official Stable) {#Python_2.x-3.x_Driver_.28Official_Stable.29}

Pure python ctypes based driver (fbclient library is required) is located in svn repository (All official driver development is done in this repository) In addition to feature set of the standard Python DB API, fdb also exposes nearly the entire native client API of the database engine, including two-phase commit, server-side events, and an administrative API.

URL

:   [https://firebirdsql.org/en/python-driver/](https://firebirdsql.org/en/python-driver/){.https}

GIT

:   [https://github.com/FirebirdSQL/fdb](https://github.com/FirebirdSQL/fdb){.https}

pypi

:   [https://pypi.python.org/pypi/fdb/](https://pypi.python.org/pypi/fdb/){.https}

Documentation

:   [https://pythonhosted.org/fdb/](https://pythonhosted.org/fdb/){.https}

Python versions
:   2.7 - 3.x

It was tested with cpython

#### Pure Python 3.x Driver {#Pure_Python_3.x_Driver}

New pure python 3.x driver (no C compiler needed or fbclient library) development is located on github repository

URL

:   [https://github.com/nakagami/pyfirebirdsql](https://github.com/nakagami/pyfirebirdsql){.https}

pypi

:   [https://pypi.python.org/pypi/firebirdsql/](https://pypi.python.org/pypi/firebirdsql/){.https}

Documentation

:   [https://nakagami.github.com/pyfirebirdsql/](https://nakagami.github.com/pyfirebirdsql/){.https}

Python versions
:   3.x

It was tested with cpython , jython, ironpython and pypy
:::
