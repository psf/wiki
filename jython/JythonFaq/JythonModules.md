# JythonFaq/JythonModules

:::: {#content dir="ltr" lang="en"}
# Jython modules {#Jython_modules}

[JythonFaq](JythonFaq)

::: table-of-contents
Contents

1.  [Jython modules](#Jython_modules)
    1.  [What parts of the Python library are supported?](#What_parts_of_the_Python_library_are_supported.3F)
    2.  [Can I use the python DB API from Jython?](#Can_I_use_the_python_DB_API_from_Jython.3F)
    3.  [Can I use the Numeric package from Jython?](#Can_I_use_the_Numeric_package_from_Jython.3F)
:::

------------------------------------------------------------------------

## What parts of the Python library are supported? {#What_parts_of_the_Python_library_are_supported.3F}

The good news is that Jython now supports almost all of the standard Python library.

If there is some standard Python module that you have a real need for that doesn\'t work with Jython yet, please file a bug.

------------------------------------------------------------------------

## Can I use the python DB API from Jython? {#Can_I_use_the_python_DB_API_from_Jython.3F}

Use zxJDBC which gives data database connectivity from Jython using the Python DB API 2.0 interface. For more information about using zxJDBC see:

\- [http://www.jython.org/docs/zxjdbc.html](http://www.jython.org/docs/zxjdbc.html){.http}

Note: the use of zxJDBC is now discouraged in favour of JyJDBC. One reason for that is the lack of testing in zxJDBC, which makes non trivial to change it.

\- [https://code.google.com/p/jyjdbc/](https://code.google.com/p/jyjdbc/){.https}

------------------------------------------------------------------------

## Can I use the Numeric package from Jython? {#Can_I_use_the_Numeric_package_from_Jython.3F}

Take a look at at Tim Hochberg\'s Java implementation of Numeric, JNumeric.

\- [http://jnumerical.sourceforge.net/index.html](http://jnumerical.sourceforge.net/index.html){.http}
::::
