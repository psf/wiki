# MercurialOnJython

::: {#content dir="ltr" lang="en"}
Jason Briggs did some investigation of Hg on Jython ([http://blog.headius.com/2007/08/business-case-for-supporting-jython.html](http://blog.headius.com/2007/08/business-case-for-supporting-jython.html){.http .reference .external}), apparently this requires implementing at least:

- bz2 - part of UpgradeTo25CPythonLib, we might be able to use [http://www.kohsuke.org/bzip2/](http://www.kohsuke.org/bzip2/){.http .reference .external}
- cx_bsdiff - Source code here, [http://sourceforge.net/projects/cx-bsdiff/](http://sourceforge.net/projects/cx-bsdiff/){.http .reference .external} with more documentation at [http://starship.python.net/crew/atuining/cx_bsdiff/](http://starship.python.net/crew/atuining/cx_bsdiff/){.http .reference .external}
:::
