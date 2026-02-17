# PyQt/Mac_OS_X_Installation_Notes

::: {#content dir="ltr" lang="en"}
# Mac OS X Installation Notes {#Mac_OS_X_Installation_Notes}

This page contains a list of problems that people have encountered with Python and [PyQt](PyQt) on Mac OS X.

## Fatal Python error: Interpreter not initialized (version mismatch?) {#Fatal_Python_error:_Interpreter_not_initialized_.28version_mismatch.3F.29}

[Kevin Cureton writes](http://mats.imk.fraunhofer.de/pipermail/pykde/2006-July/013722.html){.http}:

    Once I rebuilt Python as a framework, along with rebuilding the various extensions, SIP, and PyQt, things worked fine.

    Here are the commands to build Python as a framework from the source.

         configure --enable-framework
         make
         sudo make frameworkinstall
:::
