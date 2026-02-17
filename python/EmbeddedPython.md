# EmbeddedPython

::: {#content dir="ltr" lang="en"}
# Embedded Python {#Embedded_Python}

Python can be used in embedded, small or minimal hardware devices, depending on how limiting the devices actually are.

## Devices capable of running CPython {#Devices_capable_of_running_CPython}

Some modern embedded devices have enough memory and a fast enough CPU to run a typical Linux-based environment, for example, and running CPython on such devices is mostly a matter of compilation (or cross-compilation) and tuning.

Devices which could be considered as \"embedded\" by modern standards and which can run tuned versions of CPython include the following:

- [Gumstix](http://www.gumstix.org/){.http}

- [Raspberry Pi](http://www.raspberrypi.org/){.http}

- [BeagleBone Black](http://beagleboard.org/Products/BeagleBone%20Black){.http}

- FIC [Neo1973](http://wiki.openmoko.org/wiki/Neo1973){.http} and [Neo FreeRunner](http://wiki.openmoko.org/wiki/Neo_FreeRunner){.http} ([Python on Openmoko](http://wiki.openmoko.org/wiki/Python){.http})

- [Telit GSM/GPRS modules](http://www.telit.com/en/products/python/why-python.php){.http} (also available as [AarLogic family](http://www.roundsolutions.com/aarlogic/index.htm){.http} GPRS/GPS QUAD Band Modules)

See also [PythonForArmLinux](PythonForArmLinux) and [OpenEmbedded](OpenEmbedded).

## Work to improve CPython for embedded applications {#Work_to_improve_CPython_for_embedded_applications}

Various efforts have been made to make CPython more usable for embedded applications:

- [Patches in the OpenEmbedded repository](http://cgit.openembedded.org/cgit.cgi/openembedded/tree/recipes/python){.http}

- Cross-compilation issues: [1006238](http://bugs.python.org/issue1006238 "Issue"){.interwiki}, [5404](http://bugs.python.org/issue5404 "Issue"){.interwiki}, [3871](http://bugs.python.org/issue3871 "Issue"){.interwiki}

- General interpreter startup costs: [SpeedUpInterpreterStartup](SpeedUpInterpreterStartup)

- File access overhead on startup: [Improving interpreter startup speed](http://mail.python.org/pipermail/python-list/2008-October/467718.html){.http}, [Tons of stats/opens to non-existing files increases Python\'s startup on loaded NFS servers](http://mail.python.org/pipermail/python-list/2005-May/339691.html){.http}, [Startup time](http://mail.python.org/pipermail/python-dev/2003-May/035359.html){.http}

- Import-related costs: [\_\_file\_\_](http://mail.python.org/pipermail/python-dev/2010-March/098042.html){.http}

- Using a launcher process where \"expensive\" modules are required: [Introducing python-launcher](http://blogs.gnome.org/johan/2007/01/18/introducing-python-launcher/){.http}

## Reduced or reworked Python implementations {#Reduced_or_reworked_Python_implementations}

Some devices may be more restrictive in that the typical memory footprint of CPython may exceed the amount of memory available on the device. In such cases, a re-engineered or adapted version of CPython, perhaps even to the point where it can be considered a new implementation of Python, might be appropriate.

Examples of such implementations include the following:

- [PyMite](PyMite)

- [Tiny Python](./Tiny(20)Python.html)

- [Zerynth](Zerynth) formerly Viper

On the other hand, one can start with a full build, and simply remove unneeded modules, *e.g.*, Tkinter, etc., to realize a reduced-size Python with little effort.

## Python-based tools for developing embedded applications {#Python-based_tools_for_developing_embedded_applications}

Sometimes the embedded environment is just too restrictive to support a Python virtual machine. In such cases, various Python tools can be employed for prototyping, with the eventual application or system code being generated and deployed on the device.

Tools that support this kind of development include the following:

- [MyHDL](https://myhdl.org/){.https}

- [WhatOS](https://sourceforge.net/projects/whatos/){.https}
:::
