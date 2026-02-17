# PyrexOnWindows

::: {#content dir="ltr" lang="en"}
**Step-by-step guide to install Pyrex on Windows and compile your first extension**

## A: Pyrex installation on Windows XP {#A:_Pyrex_installation_on_Windows_XP}

### step A.1 {#step_A.1}

Install [Python](http://www.python.org){.http} (we used version 2.4.2)

### step A.2 {#step_A.2}

Run the windows installer for [Pyrex](http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/){.http} (e.g. `Pyrex-0.9.3.1.win32.exe`{.backtick})

### step A.3 {#step_A.3}

Install [Mingw](http://www.mingw.org/download.shtml){.http}, the gcc compiler for Windows (download and run `MinGW-5.1.2.exe` and choose only the \"base tools\": `mingw-runtime 3.9`{.backtick}, `w32api-3.6`{.backtick}, `binutils 2.15.91`{.backtick} and `gcc-core 3.4.2`{.backtick}. Add Mingw path (`C:\MinGW\bin`{.backtick}) to the Windows `Path`{.backtick} environment variable. If you already have cygwin installed, add `C:\MinGW\bin`{.backtick} before the Cygwin path.

### step A.4 {#step_A.4}

Edit the file `c:/Python2x/Lib/distutils/distutils.cfg`{.backtick} (if it does not exist, create it) and add the following lines:

    [build]
    compiler = mingw32

### step A.5 {#step_A.5}

MinGW links with `msvcrt.dll`{.backtick} whereas the main Python distribution links with `msvcr71.dll`{.backtick} (due to Visual C++ 2003). It is not safe to mix and blend these two different C runtime libraries. In order to make minGW link with `msvcr71.dll`{.backtick}, edit the text file `c:\mingw\lib\gcc\mingw32\3.2.4\specs`{.backtick} and change `-lmsvcrt`{.backtick} to `-lmsvcr71`{.backtick}.

------------------------------------------------------------------------

## B: Create your first Pyrex module {#B:_Create_your_first_Pyrex_module}

### step B.1 {#step_B.1}

Create a working directory (e.g. `D:\pyrex_module\`{.backtick}). Write a pyrex module and save it with a `pyx`{.backtick} extension (e.g. `primes.pyx`{.backtick}, code available [here](http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/){.http})

### step B.2 {#step_B.2}

Write the following python script and save it as `setup.py`{.backtick} in your working directory.

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

If you want to compile several modules, duplicate the line starting with `Extension`{.backtick} and replace `primes`{.backtick} by your module names.

### step B.3 {#step_B.3}

In your working directory, create a batch file called `build_and_install.bat`{.backtick} containing the following lines. To run the batch, double-click the file. You will see many \"Warning\" messages during the building process: do not worry, it is normal.

    C:\Python24\python.exe setup.py build_ext install
    pause

### step B.4 {#step_B.4}

Mission completed. The file `primes.pyd`{.backtick} (a Python Extension DLL) is now located in `C:\Python24\Lib\site-packages`{.backtick} and the `primes`{.backtick} module is available in Python. In your working directory, you can delete `primes.c`{.backtick} and the `build`{.backtick} folder created by the building process.

You can now test your new module at the python shell:

    >>> import primes
    >>> primes.primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
:::
