# MacPython/PackageManager

::: {#content dir="ltr" lang="en"}
[PackageManager](./PackageManager.html){.nonexistent} is [MacPython](MacPython)\'s means for making it easy (easy enough) for users to install and upgrade [MacPython](MacPython) extensions. The GUI is buggy. If you have problems, trying running the pimp module, which can be used as a command line tool like so:

    [crack:~] bob% python `python -c "import pimp; print pimp.__file__"`
    Usage: pimp [options] -s [package ...] List installed status
           pimp [options] -l [package ...] Show package information
           pimp [options] -i package ... Install packages
           pimp -d Dump database to stdout
           pimp -V Print version number
    Options:
           -v Verbose
           -f Force installation
           -D dir Set destination directory
                  (default: /System/Library/Frameworks/Python.framework/Versions/2.3/lib/python2.3/site-packages)
           -u url URL for database
                  (default: http://www.python.org/packman/version-0.3/darwin-7.2.0-Power_Macintosh.plist)

Feel free to make your own shell script or alias to shorten that command line ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}

How is it that one is supposed to run those commands (e.g. \"pimp -i package\")? The best I could come up with was:

    python /Library/Frameworks/Python.framework/Versions/2.3/lib/python2.3/plat-mac/pimp.py -i package

but it seems that there should be an easier way.

Make sure to check out [PackageManagerRepository](./PackageManagerRepository.html){.nonexistent}, there are alternate databases that have a wealth of additional packages.

# How do I get it? {#How_do_I_get_it.3F}

[PackageManager](./PackageManager.html){.nonexistent} comes with a full [MacPython](MacPython) distribution. For OS X 10.3 users, get the [MacPythonPantherAddons](./MacPythonPantherAddons.html){.nonexistent}.

# Related Links {#Related_Links}

- [/PackageManagerRepository](./MacPython(2f)PackageManager(2f)PackageManagerRepository.html){.nonexistent}

- [/PackageManagerBugs](./MacPython(2f)PackageManager(2f)PackageManagerBugs.html){.nonexistent}
:::
