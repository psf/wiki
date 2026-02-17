# ScriptingJava

::: {#content dir="ltr" lang="en"}
# Tools for scripting Java using Python {#Tools_for_scripting_Java_using_Python}

This page lists tools for Java/Python interoperatbility.

The purpose of this page is to provide:

- a list of tools for Java/Python interoperability
- a summary of the capabilities/uses of each tool
- brief overview information about the developers, maintainers, and current status of each project.

------------------------------------------------------------------------

## Active Projects {#Active_Projects}

------------------------------------------------------------------------

[JCC](http://www.python.org/pypi/JCC){.http} is a wrapper generator for Java APIs, exposing them to C++ and Python, and producing Python extensions which communicate via JNI with a Java virtual machine.

- Used in the [PyLucene](http://pylucene.osafoundation.org/){.http} project to provide access to the Lucene Java API (instead of using GCJ and SWIG).

- Announced in November 2007 as part of the Chandler 0.7 release.

[Jepp](http://jepp.sourceforge.net/){.http} embeds CPython in Java. It is safe to use in a heavily threaded environment, it is quite fast and its stability is a main feature and goal.

- Version 2.0 was released in October 2006.

- Jepp was developed by *Trinity Capital*, a division of Bank of the West.

- For a quick introduction see this [article on NewsForge](http://programming.newsforge.com/programming/06/10/20/1423240.shtml?tid=54&amp;amp;tid=109){.http}.

[JPype](http://jpype.sourceforge.net/){.http} is an effort to allow python programs full access to java class libraries. This is achieved not through re-implementing Python, as Jython/JPython has done, but rather through interfacing at the native level in both Virtual Machines.

- For information on the current status of the project, see the [JPype Blog](http://jpype.blogspot.com/){.http}

- The author of JPype is Steve Menard.

- Version 0.5 was released May 2006.

- As of November 2006 version 0.6 is being developed.

[Jython](http://www.jython.org/Project/index.html){.http} (formerly: JPython) is a Python-to-Java bytecode compiler. It is written in Java. Most Python scripts should run with little or no modification on Jython. The exception is scripts that use Python extensions written in C. Some modules in the standard library may not be available in Jython.

- Jython has recently seen renewed interest. With the recent emphasis on dynamic languages for the JVM, Jython appears to be getting new contributors and making progress again.

- For information about the current status of the project see [Frank Wierzbicki\'s blog](http://fwierzbicki.blogspot.com/){.http} or the [Jython wiki](http://wiki.python.org/jython/){.http}

- JPython was created in late 1997 by Jim Hugunin.

- In February 1999 Barry Warsaw took over as primary developer and released JPython version 1.1.

- In October 2000 Barry helped move the software to [SourceForge](SourceForge) where it was renamed to Jython, and Finn Bock became the primary maintainer.

- In December 2001, Jython version 2.1 was released. For more information see the old [Jython 2.1 homepage](http://jython.sourceforge.net/Jython21.html){.http}.

- In 2004, the [PSF awarded a grant](http://www.python.org/psf/grants/){.http} for a *Moving Jython Forward* project led by Brian Zimmer.

- An alpha version of 2.2 was released in July 2005. This was an experimental, unstable release with significant known issues.

- Frank Wierzbicki became the project\'s chief maintainer in November 2005.

- In August 2007, Jython 2.2 was finally released, followed by Jython 2.2.1 in October 2007.

[Laurent Pointal](./Laurent(20)Pointal.html){.nonexistent} comments on these and a few other Java-related Python projects in a [page he maintains](http://www.limsi.fr/Individu/pointal/python.html#liens-intautlang-java){.http}.

------------------------------------------------------------------------

## Discontinued Projects {#Discontinued_Projects}

------------------------------------------------------------------------

[javaclass](http://www.python.org/pypi/javaclass){.http} is a project which attempts to import Java class files as Python modules by translating the structures and bytecode.

- **Project Status** as of 2005 is **discontinued**, although there remains a vague possibility of it being re-evaluated in the light of recent Python releases.

[JPE](http://jpe.sourceforge.net/){.http} (Java-Python Extension) uses JNI to provide a bridging mechanism between Java and a Python interpreter (including use of C extensions for Python).

- **Project Status** as of 2002 is **discontinued**.

[JPI](http://www.ndim.edrc.cmu.edu/dougc/jpi/Home.html){.http} was a two-way Python-Java Interface.

- **Project Status** as of 2002 is **discontinued**.

------------------------------------------------------------------------
:::
