# UsefulModules

:::: {#content dir="ltr" lang="en"}
::: table-of-contents
Contents

1.  [Useful Modules, Packages and Libraries](#Useful_Modules.2C_Packages_and_Libraries)
    1.  [Standard Library Backports](#Standard_Library_Backports)
    2.  [Cryptography](#Cryptography)
    3.  [Database](#Database)
    4.  [Foreign Function Interface](#Foreign_Function_Interface)
    5.  [Game Development](#Game_Development)
    6.  [GIS (Geographic Information System)](#GIS_.28Geographic_Information_System.29)
    7.  [GUI](#GUI)
        1.  [Console](#Console)
    8.  [Audio / Music](#Audio_.2F_Music)
    9.  [ID3 Handling](#ID3_Handling)
    10. [Image Manipulation](#Image_Manipulation)
    11. [Indexing and Searching](#Indexing_and_Searching)
    12. [Java](#Java)
    13. [Networking](#Networking)
    14. [Platform-Specific](#Platform-Specific)
        1.  [Mac](#Mac)
        2.  [Windows](#Windows)
    15. [Plotting](#Plotting)
    16. [Presentation](#Presentation)
    17. [RDF Processing](#RDF_Processing)
    18. [Scientific](#Scientific)
    19. [Standard Library Enhancements](#Standard_Library_Enhancements)
    20. [Threading](#Threading)
    21. [System administration](#System_administration)
    22. [Web Development](#Web_Development)
        1.  [HTML Forms](#HTML_Forms)
        2.  [HTML Parser](#HTML_Parser)
    23. [Workflow](#Workflow)
    24. [XML Processing](#XML_Processing)
    25. [Flow Based Programming](#Flow_Based_Programming)
    26. [Editorial Notes](#Editorial_Notes)
:::

# Useful Modules, Packages and Libraries {#Useful_Modules.2C_Packages_and_Libraries}

The intent of this page is to list some of the most commonly used Python modules, in the hope that it will provide useful recommendations for other programmers (especially beginners). Remember that in addition to the listings below, there are other directories of Python modules - see [PublishingPythonModules](PublishingPythonModules) for details. Another collection of library details can be found on the [Libraries](Libraries) page.

Be warned that this list is subjective by its very nature - it is only intended as a helpful guide. It is not definitive in any way, nor should it discourage developers from developing their own modules.

## Standard Library Backports {#Standard_Library_Backports}

- [StandardLibraryBackports](StandardLibraryBackports) - modules that make later standard library functionality available in earlier version

## Cryptography {#Cryptography}

- [Python and Cryptography](Cryptography)

## Database {#Database}

- [SQLAlchemy](http://www.sqlalchemy.org/){.http} or [SQLObject](http://sqlobject.org/){.http} - Object oriented access to several different database systems

- [DatabaseInterfaces](DatabaseInterfaces) - Direct Python interfaces to relational and non-relational database backends

- See also [DatabaseProgramming](DatabaseProgramming) for guidance on choosing a database backend system

## Foreign Function Interface {#Foreign_Function_Interface}

- [CTypes](http://starship.python.net/crew/theller/ctypes/){.http} - A package for calling the functions of dlls/shared libraries. Now included with Python 2.5 and up.

- [Cython](http://cython.org/){.http} is an extension language for the CPython runtime. It translates Python code to fast C code and supports calling external C and C++ code natively. As opposed to ctypes, it requires a C compiler to translate the generated code.

## Game Development {#Game_Development}

- [PyGame](http://www.pygame.org/){.http} - Principal wrapper of the SDL library.

- See also [GameProgramming](GameProgramming). A more comprehensive list of packages can be found on the [PythonGameLibraries](PythonGameLibraries) page.

## GIS (Geographic Information System) {#GIS_.28Geographic_Information_System.29}

- [GIS Web services](./GIS(2f)Web_services.html) - Packages to access to Google Maps, Yahoo! MapsÃ¢Â€Â¦ and more information

## GUI {#GUI}

- [PyGtk](PyGtk) - Bindings for the cross-platform Gtk toolkit.

- [PyQt](PyQt) - Bindings for the cross-platform Qt framework.

- [TkInter](TkInter) - The traditional Python user interface toolkit.

- [WxPython](WxPython) - wxWidgets bindings for Python supporting [PythonCard](./PythonCard.html){.nonexistent}, [Wax](Wax) and other frameworks.

- [PyjamasDesktop](PyjamasDesktop) - Bindings and a framework for the cross-platform [webkit](http://webkit.org){.http}.

- [PySimpleGUI](PySimpleGUI) - Wrapper for [TkInter](TkInter), Qt, wxpython and Remi (Web) that makes GUI development easy and compact

- GUI Programming is, in many cases, a matter of taste. See a more extensive list on the [GuiProgramming](GuiProgramming) page.

### Console {#Console}

- [Ascii Table](./Console(2f)Ascii_table.html) packages

## Audio / Music {#Audio_.2F_Music}

- [Audio in Python](Audio)

## ID3 Handling {#ID3_Handling}

- [Mutagen](http://code.google.com/p/mutagen/){.http} - Mutagen is a Python module to handle audio metadata. It supports FLAC, M4A, Musepack, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True Audio, and [WavPack](./WavPack.html){.nonexistent} audio files. All versions of ID3v2 are supported, and all standard ID3v2.4 frames are parsed. It can read Xing headers to accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags can be edited regardless of audio format. It can also manipulate Ogg streams on an individual packet/page level. **It only writes ID3v2.4** (introduced in 2000, but as of Windows 8 still not supported by [MediaPlayer](./MediaPlayer.html){.nonexistent}).

- [ID3Reader](http://www.nedbatchelder.com/code/modules/id3reader.html){.http} - \"Id3reader.py is a Python module that reads ID3 metadata tags in MP3 files. It can read ID3v1, ID3v2.2, ID3v2.3, or ID3v2.4 tags. It does not write tags at all\" (from site). Used in ID3Writer. Does not work with Python 3000. Not maintained since 2006.

- [PyID3](http://sourceforge.net/projects/pyid3){.http} - \"\"(Appears to be inactive)\"\"Module for manipulating ID3 informational tags in MP3 audio files. Not as good as ID3Writer, but no issues w/ genre, unlike ID3Writer. Not maintained since 2007.

- [pytagger](http://www.liquidx.net/pytagger/){.http} - tag reader and writer implemented purely in Python. Supports ID3v1, ID3v1.1, ID3v2.2, ID3v2.3 and ID3v2.4

- [eyeD3](http://eyed3.nicfit.net/){.http} - is a Python module and program for processing ID3 tags. It can extract information such as bit rate, sample frequency, play time, etc. It supports ID3 v1.0/v1.1 and v2.3/v2.4.

- [hsaudiotag](http://pypi.python.org/pypi/hsaudiotag3k#downloads){.http} - Py3k - hsaudiotag is a pure Python library that lets you read metadata (bitrate, sample rate, duration and tags) from mp3, mp4, wma, ogg, flac and aiff files. It can only read tags, not write to them, but unlike more complete libraries (like Mutagen), it is BSD licensed.

- [pytaglib](https://pypi.python.org/pypi/pytaglib){.https} - Python 3.x and 2.x support - bindings to the C++ [taglib](http://taglib.github.io){.http} library, reads and writes mp3, ogg, flac, mpc, speex, opus, [WavPack](./WavPack.html){.nonexistent}, [TrueAudio](./TrueAudio.html){.nonexistent}, wav, aiff, mp4 and asf files.

## Image Manipulation {#Image_Manipulation}

- [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/){.http} - Supports many file formats, and provides powerful image processing and graphics capabilities.

- [pyqtgraph](http://www.pyqtgraph.org/){.http} - Pure-python graphics library for scientific applications with image/video display, multidimensional image slicing, and interactive manipulation tools.

## Indexing and Searching {#Indexing_and_Searching}

- [InformationRetrieval](InformationRetrieval)

## Java {#Java}

- [Java scripting](ScriptingJava)

## Networking {#Networking}

- [asyncoro](http://asyncoro.sourceforge.net){.http} - Asynchronous, concurrent programming framework with coroutines with thread-like interface

- [Gevent](http://gevent.org){.http} - Coroutine-based network library

- [TwistedMatrix](http://twistedmatrix.com){.http} - Event-driven networking framework

- [RPyC](http://rpyc.wikispaces.com){.http} - Transparent RPC/distributed-computing framework

- [PyRO](http://pyro.sourceforge.net){.http} - powerful OO RPC

- [HTTPLib2](http://code.google.com/p/httplib2/){.http} - A comprehensive HTTP client library that supports many features left out of other HTTP libraries, like httplib on the standard library.

- [Celery](http://celeryproject.org){.http} - Distributed task queue for out of band processing/RPC and more.

## Platform-Specific {#Platform-Specific}

- [Psyco](http://psyco.sourceforge.net/){.http} - Psyco can speed up the execution of any Python code (x86 only).

- [PyInstaller](http://www.pyinstaller.org/){.http} - Packages Python programs into stand-alone executables, under Windows, Linux and Irix.

### Mac {#Mac}

- [py2app](http://pythonmac.org/wiki/py2app){.http} - Creates stand-alone apps (like py2exe for Mac)

- [PyObjC](http://pyobjc.sourceforge.net){.http} - Bridge between the Python and Objective-C. Most important usage of this is writing Cocoa GUI applications on Mac OS X in pure Python

### Windows {#Windows}

- [PyWin32](https://sourceforge.net/projects/pywin32/){.https} - Python extensions for Windows.

- [Py2exe](http://www.py2exe.org/){.http} - Converts python scripts into executable windows programs, able to run without requiring a python installation.

## Plotting {#Plotting}

- [Chaco](http://code.enthought.com/chaco/){.http} - Creates interactive plots

- [gnuplot.py](http://gnuplot-py.sourceforge.net/){.http} - Based on gnuplot

- [Matplotlib](http://matplotlib.sourceforge.net/){.http} - Production quality output in a wide variety of formats

- [Plotly](https://plot.ly/){.https} - Interactive, publication-quality, web based charts

- [PyX](http://pyx.sourceforge.net/){.http} - Postscript and PDF output, (La)TeX integration

- [ReportLab](http://www.reportlab.org/){.http} includes a charting package

- [Veusz](http://home.gna.org/veusz/){.http} - Postscript output with a [PyQt](PyQt) front end

- [pyqtgraph](http://www.pyqtgraph.org/){.http} - Pure-python plotting and graphics library based on [PyQt](PyQt) and numpy.

The [SciPy](SciPy) [topical software](http://scipy.org/Topical_Software#head-b98ffdb309ccce4e4504a25ea75b5c806e4897b6){.http} page has a longer list.

## Presentation {#Presentation}

- [http://docutils.sourceforge.net/docs/user/tools.html#rst2s5-py](http://docutils.sourceforge.net/docs/user/tools.html#rst2s5-py){.http} - Create HTML slides from .rst files

- [http://seld.be/notes/introducing-slippy-html-presentations](http://seld.be/notes/introducing-slippy-html-presentations){.http} - For your Python presentations in browser

## RDF Processing {#RDF_Processing}

- See [RdfLibraries](RdfLibraries) for a list of available RDF processing solutions.

## Scientific {#Scientific}

- [Visual Python](http://vpython.org/){.http} - Offers real-time 3D output, is easily usable by novice programmers, excellent for physics.

- [SciPy](http://www.scipy.org/){.http} - Includes modules for graphics and plotting, optimization, integration, special functions, signal and image processing, genetic algorithms, ODE solvers, and others.

- [Python Bindings for R](http://rpy.sourceforge.net/){.http} - R is a well known, open source (GPL 2) statistical package. RPy has two versions. Version 2 is still in development but is already usable.

- [numpy](./numpy.html){.nonexistent}

- [PyIMSL](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx){.http} is a collection of Python wrappers to the mathematical and statistical algorithms in the IMSL C Numerical Library. Developers can use Python, PyIMSL and the IMSL C Numerical Library for rapid prototyping. [PyIMSL Studio](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx){.http} is a complete packaged, supported and documented development environment designed for deploying mathematics and statistics prototype models into production applications. PyIMSL Studio includes the PyIMSL wrappers, the IMSL C Numerical Library, a Python distribution and a selection of open source python modules useful for prototype analytical development. PyIMSL Studio is available for download at no charge for non-commercial use or for commercial evaluation.

## Standard Library Enhancements {#Standard_Library_Enhancements}

- [Python Path](http://pypi.python.org/pypi/path.py){.http} - Wraps the functionality of the os.path module and provides something more convenient.

- [Requests](https://pypi.python.org/pypi/requests){.https} - An improvement upon urllib etc., for sending HTTP requests.

- [Dateutil](https://pypi.python.org/pypi/python-dateutil){.https} - Provides powerful extensions to the datetime module.

- [sh](https://pypi.python.org/pypi/sh){.https} - Can call any external program as if it were a function.

- [DocOpt](https://pypi.python.org/pypi/docopt){.https} - Command line arguments parser, with declarative approach (docstring).

- [PyLibrary](http://sourceforge.net/projects/pylibrary/){.http} - Collection of Libraries useful for Python developers.

## Threading {#Threading}

- [ThreadPool](http://chrisarndt.de/projects/threadpool/){.http} - Intuitive approach to threads, well-explained.

- See the [ParallelProcessing](ParallelProcessing) page for other multiprocessing or parallel processing approaches.

## System administration {#System_administration}

- [psutil](https://github.com/giampaolo/psutil){.https} - cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network) in Python.

## Web Development {#Web_Development}

- [Django](http://www.djangoproject.com){.http} - High-level web framework.

- [Pyramid](http://docs.pylonsproject.org/){.http} - Turbogears, Pylons, Repoz.bfg merged as Pyramid.

  - [TurboGears](http://www.turbogears.org){.http} - Rapid web development megaframework.

  - [Pylons](http://pylonshq.com){.http} - A lightweight web framework emphasizing flexibility and rapid development.

- [web2py](http://web2py.com/){.http} - High-level framework for agile development.

- [Flask](http://flask.pocoo.org/){.http} - microframework for Python based on Werkzeug, Jinja 2. (It\'s BSD licensed)

- See a more complete list of topics on the [WebProgramming](WebProgramming) page and frameworks on the [WebFrameworks](WebFrameworks) page.

### HTML Forms {#HTML_Forms}

- [ClientForm](http://wwwsearch.sourceforge.net/ClientForm/){.http} - \"[ClientForm](./ClientForm.html){.nonexistent} is a Python module for handling HTML forms on the client side, useful for parsing HTML forms, filling them in and returning the completed forms to the server. It developed from a port of Gisle Aas\' Perl module HTML::Form, from the libwww-perl library, but the interface is not the same.\" - from the website.

- [FormEncode](http://formencode.org/){.http}

- [lxml.html](http://lxml.de/){.http} has support for dealing with forms in HTML documents

- See also the [WebProgramming](WebProgramming) and [WebFrameworks](WebFrameworks) pages.

### HTML Parser {#HTML_Parser}

- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/){.http} - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.

- [PyQuery](http://packages.python.org/pyquery/){.http} - implements jQuery in Python; faster than [BeautifulSoup](./BeautifulSoup.html){.nonexistent}, apparently.

- [mxTidy](http://www.egenix.com/products/python/mxExperimental/mxTidy/){.http} - HTML cleanup tool. This is a library version of the popular HTML Tidy command-line application which will convert HTML (even badly formatted) into e.g. XHTML.

- [lxml.html](http://lxml.de/){.http} is a very fast, easy-to-use and versatile library for handling (and fixing up) HTML

- See also [PythonXml](PythonXml) for related tools.

## Workflow {#Workflow}

- [openflow](http://www.openflow.it/Openflow){.http} - A workflow engine for Zope 2.

- [Goflow](http://code.djangoproject.com/wiki/GoFlow){.http} - A workflow engine for Django, with same design as openflow.

## XML Processing {#XML_Processing}

- [ElementTree](http://effbot.org/zone/element-index.htm){.http} - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. \--Note: Python 2.5 and up has [ElementTree](ElementTree) in the Standard Library\--

- [lxml](http://lxml.de/){.http} is a very fast, easy-to-use and versatile library for XML handling that is mostly compatible with but much more feature-rich than [ElementTree](ElementTree)

- [Amara](http://wiki.xml3k.org/Amara2){.http} - Amara provides tools you can trust to conform with XML standards without losing the familiar Python feel. (see also the [1.x version](http://wiki.xml3k.org/Amara){.http})

- [PythonXml](PythonXml) provides a list of available XML processing solutions.

## Flow Based Programming {#Flow_Based_Programming}

- [Python and Flow Based Programming (pipelines)](FlowBasedProgramming)

## Editorial Notes {#Editorial_Notes}

Please avoid listing modules where\...

- You are one of the developers (and you just want to promote your work somewhere).
- The modules in question do not have widespread approval or usage.

If you do want to make people aware of a module, package or library (perhaps your own), consider submitting it to one or more of the directories mentioned in [PublishingPythonModules](PublishingPythonModules), perhaps also adding it to the topic-specific part of this site (eg. [WebProgramming](WebProgramming), [GuiProgramming](GuiProgramming)).

Do list modules that:

- Get recommended often in the Tutor or comp.lang.python lists

Please provide a short description for each module. Try to put each module in the category that matches its \"main\" audience, since a module might fall into a number of categories.
::::
