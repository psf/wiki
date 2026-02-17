# RPM

::: {#content dir="ltr" lang="en"}
RPM is a package format used by Fedora, Red Hat and some other Linux distributions. So if you want to make your package available there, you need to know how to create RPMs.

Before Python 3 there was a `bdist_rpm`{.backtick} command, which had gone in `packaging`{.backtick} (Distutils2). If you\'re interested to know - ask Tarek (and don\'t forget to update the info here). Now there are two packages to help make .rpm out of Python package (setup.py?):

- Tarek\'s [pypi2rpm](https://bitbucket.org/tarek/pypi2rpm){.https} - aims at providing the same features and much more

- [py2pack](http://pypi.python.org/pypi/py2pack){.http} by Sascha Peilicke.

### Comparison {#Comparison}

- **Availability**

  - PyPI
    - py2pack - [version 0.2.11](http://pypi.python.org/pypi/py2pack/0.2.11){.http} uploaded to PyPI on 2010-12-11

    - pypi2rpm - [version 0.1](http://pypi.python.org/pypi/pypi2rpm/0.1){.http} uploaded on 2010-10-28
  - Fedora (because you want to use supported RPM package to build RPM\'s, obviously)
    - py2pack - [Yes](https://admin.fedoraproject.org/pkgdb/acls/name/python-py2pack){.https}

    - pypi2rpm - No
:::
