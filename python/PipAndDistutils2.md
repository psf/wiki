# PipAndDistutils2

::: {#content dir="ltr" lang="en"}
[Pip](http://www.pip-installer.org/){.http} is a popular installer and uninstaller of Python packages. Currently, pip depends on the third-party packaging extensions in [setuptools](http://peak.telecommunity.com/DevCenter/setuptools){.http}, or the [distribute](http://packages.python.org/distribute/){.http} fork. The future of Python packaging is [distutils2](http://distutils2.notmyidea.org/){.http} (\"packaging\" in the Python 3.3+ standard library), and pip should gain support for using distutils2/packaging as an alternative to setuptools/distribute (though setuptools/distribute support needs to be maintained as well for some time to come).

Possible areas of work for a proposal here:

- Adding support for installing distutils2-style projects (with setup.cfg and possibly no setup.py, [PEP 345](http://www.python.org/dev/peps/pep-0345/){.http} metadata), by using the appropriate distutils2 APIs.

- Adding support for introspecting and uninstalling [PEP 376](http://www.python.org/dev/peps/pep-0376/){.http}-style installed distributions, again using distutils2 APIs wherever possible.

- Charting areas of overlap between pip and distutils2 and modifying pip to optionally prefer distutils2 APIs, if available, for areas of functional overlap (e.g. finding candidate distributions for installation).

Work has been started under the [pip2](https://github.com/osupython/pip2){.https} name.
:::
