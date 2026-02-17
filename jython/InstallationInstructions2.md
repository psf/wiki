# InstallationInstructions2

:::::::: {#content dir="ltr" lang="en"}
# Installation

::: {#contents .contents .topic}
Contents

- [Jython 2.5.x and 2.2.x](#jython-2-5-x-and-2-2-x){#id1 .reference .internal}
  - [Basic Install](#basic-install){#id2 .reference .internal}
  - [Standalone mode](#standalone-mode){#id3 .reference .internal}
  - [Installation options](#installation-options){#id4 .reference .internal}
:::

:::::: {#jython-2-5-x-and-2-2-x .section}
### [Jython 2.5.x and 2.2.x](#id1){.toc-backref}

::: {#basic-install .section}
#### [Basic Install](#id2){.toc-backref}

Jython 2.5 and 2.2.1 are distributed as executable jar file installers. After [downloading](DownloadInstructions){.reference .external} it, either double click the jython_installer-2.5.0.jar or run java with the -jar option

    java -jar jython_installer-2.5.0.jar

This will start the regular GUI installer on most systems, or a console installer on headless systems. To force the installer to work in headless mode invoke the installer as:

    java -jar jython_installer-2.5.0.jar --console

The installer will then walk through a similar set of steps in graphical or console mode: showing the license, selecting an install directory and JVM and actually copying Jython to the filesystem. After this completes, Jython is installed in the directory you selected. Executing a script in the install directory, `jython` on Unix-like systems or `jython.bat` on Windows, will start up the Jython console, which can be used to dynamically explore Jython and the Java runtime, or to run Jython scripts.
:::

::: {#standalone-mode .section}
#### [Standalone mode](#id3){.toc-backref}

The standalone option does no caching and so avoids the startup overhead (most likely at the cost of some speed in calling Java classes, but I have not profiled it)

You can try it out by running the installer:

    $ java -jar jython_installer-2.5.0.jar

then when you come to the \"Installation type\" page, select \"Standalone\".

The installation will generate a `jython.jar` with the Python standard library (`/Lib`) files included, which can be run as:

    $ java -jar jython.jar

Of course you can run scripts just by calling them as you might expect:

    $ java -jar jython.jar script.py

Or, add this file to the classpath of your application.
:::

::: {#installation-options .section}
#### [Installation options](#id4){.toc-backref}

You can get a list of installer options (to install Jython unattended, for example) by running:

    $ java -jar jython_installer-2.5.0.jar --help
:::
::::::
::::::::
