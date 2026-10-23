# Pyrex on Windows

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Step-by-step guide to install Pyrex on Windows and compile your first extension**

## A: Pyrex installation on Windows XP 

### step A.1 

Install [Python](http://www.python.org) (we used version 2.4.2)

### step A.2 

Run the windows installer for [Pyrex](http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/) (e.g. `Pyrex-0.9.3.1.win32.exe`)

### step A.3 

Install [Mingw](http://www.mingw.org/download.shtml), the gcc compiler for Windows (download and run `MinGW-5.1.2.exe` and choose only the \"base tools\": `mingw-runtime 3.9`, `w32api-3.6`, `binutils 2.15.91` and `gcc-core 3.4.2`. Add Mingw path (`C:\MinGW\bin`) to the Windows `Path` environment variable. If you already have cygwin installed, add `C:\MinGW\bin` before the Cygwin path.

### step A.4 

Edit the file `c:/Python2x/Lib/distutils/distutils.cfg` (if it does not exist, create it) and add the following lines:

    [build]
    compiler = mingw32

### step A.5 

MinGW links with `msvcrt.dll` whereas the main Python distribution links with `msvcr71.dll` (due to Visual C++ 2003). It is not safe to mix and blend these two different C runtime libraries. In order to make minGW link with `msvcr71.dll`, edit the text file `c:\mingw\lib\gcc\mingw32\3.2.4\specs` and change `-lmsvcrt` to `-lmsvcr71`.

------------------------------------------------------------------------

## B: Create your first Pyrex module 

### step B.1 

Create a working directory (e.g. `D:\pyrex_module\`). Write a pyrex module and save it with a `pyx` extension (e.g. `primes.pyx`, code available [here](http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/))

### step B.2 

Write the following python script and save it as `setup.py` in your working directory.

    from distutils.core import setup
    from distutils.extension import Extension
    from Pyrex.Distutils import build_ext
    setup(
      name = "PyrexGuide",
      ext_modules=[
        Extension("primes", ["primes.pyx"])
        ],
      cmdclass = {'build_ext': build_ext}
    )

If you want to compile several modules, duplicate the line starting with `Extension` and replace `primes` by your module names.

### step B.3 

In your working directory, create a batch file called `build_and_install.bat` containing the following lines. To run the batch, double-click the file. You will see many \"Warning\" messages during the building process: do not worry, it is normal.

    C:\Python24\python.exe setup.py build_ext install
    pause

### step B.4 

Mission completed. The file `primes.pyd` (a Python Extension DLL) is now located in `C:\Python24\Lib\site-packages` and the `primes` module is available in Python. In your working directory, you can delete `primes.c` and the `build` folder created by the building process.

You can now test your new module at the python shell:

    >>> import primes
    >>> primes.primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
