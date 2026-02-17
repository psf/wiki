# Distutils/StandardizeEggInfo

::: {#content dir="ltr" lang="en"}
The [distutils --- PEP 376](http://www.python.org/dev/peps/pep-0376/){.http} describes a new .egg.info infrastructure.

Please look at the direct svn link which has the latest version : [svn link](http://svn.python.org/projects/peps/trunk/pep-0376.txt){.http}

- make sure the new standard (which is compatible with all tools out there in its current state - see PEP 376) contains everything we need.
- work on the uninstall story, by looking at PEP 262 and seeing how the RECORD file need to be
- make sure the APIs proposed are complete
- think hard to see if we want a reference install/uninstall script in distutils (I am +1 personnaly)

# code prototype {#code_prototype}

- get_metadata : [http://bugs.python.org/issue4908](http://bugs.python.org/issue4908){.http}
:::
