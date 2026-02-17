# Python3LinuxDistroPortingStatus

:::: {#content dir="ltr" lang="en"}
Page started at [PyCon](PyCon) 2015 for cross-distro collaboration on Python 3 Linux distro porting status.

::: table-of-contents
Contents

1.  [Additional Python 3 porting helpers](#Additional_Python_3_porting_helpers)
    1.  [Python Future](#Python_Future)
    2.  [py3c](#py3c)
2.  [Possible revised semantics for \"python\" symlink](#Possible_revised_semantics_for_.22python.22_symlink)
    1.  [Background reading](#Background_reading)
    2.  [Why not the \"alternatives\" system?](#Why_not_the_.22alternatives.22_system.3F)
    3.  [Possible integration with Software Collections & Environment Modules](#Possible_integration_with_Software_Collections_.26_Environment_Modules)
3.  [Other Notes/Tasks](#Other_Notes.2FTasks)
:::

Ubuntu status: [https://bugs.launchpad.net/ubuntu/+bugs?field.tag=python3](https://bugs.launchpad.net/ubuntu/+bugs?field.tag=python3){.https}

Fedora status: [http://fedora.portingdb.xyz/](http://fedora.portingdb.xyz/){.http}

openSUSE status: [https://en.opensuse.org/openSUSE:Python_3_Status](https://en.opensuse.org/openSUSE:Python_3_Status){.https}

# Additional Python 3 porting helpers {#Additional_Python_3_porting_helpers}

## Python Future {#Python_Future}

Expansive Python 2/3 compatibility layer (provides a more \"Python 3\" experience in Python 2 than the more minimalist six compatibility module)

Documentation: [http://python-future.org/](http://python-future.org/){.http}

PyPI module: [https://pypi.python.org/pypi/future](https://pypi.python.org/pypi/future){.https}

Ubuntu PPA (bio-linux): [https://launchpad.net/\~nebc/+archive/ubuntu/bio-linux/+packages?field.name_filter=python&field.status_filter=published&field.series_filter=](https://launchpad.net/~nebc/+archive/ubuntu/bio-linux/+packages?field.name_filter=python&field.status_filter=published&field.series_filter=){.https}

Fedora COPR: ??

Debian ITP: [ [https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=782250](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=782250){.https} ]{.strike}

Fedora review request:

## py3c

\"Six for extension modules\"

Documentation: [https://py3c.readthedocs.org/en/latest/](https://py3c.readthedocs.org/en/latest/){.https}

# Possible revised semantics for \"python\" symlink {#Possible_revised_semantics_for_.22python.22_symlink}

- Current semantics: \"Python 2\" (as per [PEP 394](https://www.python.org/dev/peps/pep-0397/){.https})

- Suggested semantics: administrator controlled \"default Python\" with command line selection of alternative runtimes

Conceptually along the lines of the \"Python launcher for Windows\" ([https://www.python.org/dev/peps/pep-0397/](https://www.python.org/dev/peps/pep-0397/){.https}), but wouldn\'t automatically update to refer to new versions when they were installed - the launcher configuration would need to be explicitly updated to select a new default.

## Background reading {#Background_reading}

- Discussion at 2015 Python Language Summit: [https://lwn.net/Articles/640296/](https://lwn.net/Articles/640296/){.https}

- linux-sig thread on providing a \"py\" launcher: [https://mail.python.org/pipermail/linux-sig/2015-October/000000.html](https://mail.python.org/pipermail/linux-sig/2015-October/000000.html){.https}

- Geoffrey Thomas\'s \"python\" launcher concept for Debian: [https://ldpreload.com/blog/usr-bin-python-23](https://ldpreload.com/blog/usr-bin-python-23){.https}

## Why not the \"alternatives\" system? {#Why_not_the_.22alternatives.22_system.3F}

- Debian alternatives: [https://wiki.debian.org/DebianAlternatives](https://wiki.debian.org/DebianAlternatives){.https}

- Fedora alternatives: [https://fedoraproject.org/wiki/Packaging:Alternatives](https://fedoraproject.org/wiki/Packaging:Alternatives){.https}

The problem with the alternatives system for this use case is that there\'s no support for command line overriding of the selected version - \"python\" would always refer to the administrator selected version. We\'d prefer the runtime selectivity offered by the Python launcher for Windows CLI or Fedora\'s rubypick ([https://github.com/fedora-ruby/rubypick](https://github.com/fedora-ruby/rubypick){.https})

Counter-argument: tools like \'conda\', \'pyenv\', \'virtualenv\', and the Linux-specific utilities discussed in the next section already offer environment based control over which Python you get on a per user and per application basis, so an administrator set default is arguably the only missing piece, and that\'s exactly the problem the alternatives system is designed to handle.

## Possible integration with Software Collections & Environment Modules {#Possible_integration_with_Software_Collections_.26_Environment_Modules}

Software collections are a tool for the Fedora/RHEL/CentOS ecosystem that allows parallel installation of multiple versions of language, database and web server runtimes: [https://www.softwarecollections.org/en/](https://www.softwarecollections.org/en/){.https}

SCL 2.0+ natively supports the cross-distro environment modules system ([http://modules.sourceforge.net/](http://modules.sourceforge.net/){.http}), while SCL 1.x supports automated conversion to environment modules ([https://access.redhat.com/documentation/en-US/Red_Hat_Software_Collections/1/html/Packaging_Guide/sect-Converting_Software_Collection_Scriptlets_into_Environment_Modules.html](https://access.redhat.com/documentation/en-US/Red_Hat_Software_Collections/1/html/Packaging_Guide/sect-Converting_Software_Collection_Scriptlets_into_Environment_Modules.html){.https})

If \"/usr/bin/python\" becomes a Python launcher style executable rather than a direct symlink to a specific Python runtime, then it would likely be desirable to make it easy to have it point to a software collection or other environment module installed under /opt in addition to being able to use it to switch between native system packages installed under /usr.

# Other Notes/Tasks {#Other_Notes.2FTasks}

Update Python 3 extension module porting guide ([https://docs.python.org/dev/howto/cporting.html](https://docs.python.org/dev/howto/cporting.html){.https}): [https://bugs.python.org/issue23897](https://bugs.python.org/issue23897){.https} (Barry Warsaw, Petr Viktorin)

Use [https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef#Python_extension_modules](https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef#Python_extension_modules){.https}
::::
