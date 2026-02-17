# ProjectFileAndDirectoryLayout

::: {#content dir="ltr" lang="en"}
The topic of how to structure your project invokes lots of opinions. Generally speaking, the relatively agreed guidelines include:

- if the project is a single source file, put it in the top level.
- if you have tests, put them in a tests/ subdirectory (even if the project is a single source file), or if you have subdirectories and prefer to keep unit tests with code, put them there.
- if you have an executable script to run your project, put it in a bin/ subdirectory, without the .py suffix even if it\'s a Python script
- if you have many source files, create a subdirectory with the name of the project, and start populating there
- include a doc/ directory (you have docs, right?)
- create module directories as needed

These guidelines are partly convention, partly because they align well with Python packaging tools.

The Python tutorial shows an example of a more complex layout: [https://docs.python.org/3/tutorial/modules.html#packages](https://docs.python.org/3/tutorial/modules.html#packages){.https}

There are many many other places that describe a layout, not all agreeing. Here are a couple:

- [packaging chapter](https://www.cmi.ac.in/~madhavan/courses/prog2-2012/docs/diveintopython3/packaging.html){.https} of [Dive Into Python 3](https://www.cmi.ac.in/~madhavan/courses/prog2-2012/docs/diveintopython3/packaging.html#structure){.https} for some useful information.

- [https://realpython.com/python-application-layouts](https://realpython.com/python-application-layouts){.https}
:::
