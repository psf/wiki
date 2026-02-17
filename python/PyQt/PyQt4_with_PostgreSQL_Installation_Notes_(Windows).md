# PyQt/PyQt4_with_PostgreSQL_Installation_Notes_(Windows)

::: {#content dir="ltr" lang="en"}
### Overview {#Overview}

These instructions describe how to configure Qt on Windows so the drivers for PostgreSQL are built and usable by [PyQt4](PyQt4). They do not go into detail on how to build Qt, SIP and [PyQt4](PyQt4) from source. Here is the OS and software versions that were used:

- Windows Vista

- PostgreSQL 8.2.4 (binary installation)

- MinGW 5.1.3

- Qt 4.3.0

- SIP 20070714 snapshot

- [PyQt4](PyQt4) 20070721 snapshot

### Install PostgreSQL {#Install_PostgreSQL}

Install PostgreSQL into a directory without spaces. e.g., C:\\PostgreSQL. Add the PostgreSQL bin path to your system path: C:\\PostgreSQL\\bin.

### Configure Qt {#Configure_Qt}

Configure Qt to compile the psql driver. You will need to tell Qt where to find the PostgreSQL include files and the pq library.

    configure.exe -qt-sql-psql -I C:/PostgreSQL/include -L C:/PostgreSQL/lib -l pq

Note that spaces are important. -lpq does not work.

### SIP and PyQt4 {#SIP_and_PyQt4}

Compile and install SIP and [PyQt4](PyQt4) normally.
:::
