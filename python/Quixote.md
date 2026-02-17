# Quixote

::: {#content dir="ltr" lang="en"}
A framework for [WebProgramming](WebProgramming).

### Masthead {#Masthead}

URL

:   [http://www.mems-exchange.org/software/quixote/](http://www.mems-exchange.org/software/quixote/){.http}, [http://www.quixote.ca](http://www.quixote.ca){.http}

version

:   2.2 (*2005-09-27*)

licence
:   CNRI Open Source License.

platforms
:   Primarily developed on and for Unix, but it seems to work with Apache on Windows too.

Python versions
:   2.x required

### Suitability {#Suitability}

Aimed at sites where complex programming is required, Quixote lets the developer apply as many of their existing Python development skills as possible. For example, you write a Web application by writing a Python package and configuring Quixote to use that package. HTML templates are written in Python-like syntax and can be imported just like other Python code.

### Deployment Platforms {#Deployment_Platforms}

Quixote will work with any Web server that supports CGI and/or [FastCGI](http://www.fastcgi.com/){.http}. [NeilSchemenauer](NeilSchemenauer)\'s new [SCGI protocol](http://arctrix.com/nas/scgi/protocol.txt){.http} is also supported, although SCGI has so far only been implemented for Apache. FastCGI or SCGI provide much better performance than CGI, and SCGI has proven more reliable than FastCGI. Finally, Quixote also supports Apache\'s [mod_python](http://www.modpython.org/){.http}. See doc/web-server.txt in the source distribution for configuration information.

Quixote can also be deployed using the [Twisted](TwistedMatrix) framework. An example script is available in the Quixote sources under `services/twisted_http.py`{.backtick}

### Development Interfaces {#Development_Interfaces}

Just like writing any Python application, with the twist that you can also import code from PTL modules (.ptl files, compiled to .ptlc).

### Environment Access {#Environment_Access}

Same as from ordinary Python code \-- application authors have complete and unhindered access to the platform Quixote is running on.

Most CGI environment variables are exposed in a more Pythonic way, ie. as attributes and/or methods of the ubiquitous HTTPRequest object.

### Session, Identification and Authentication {#Session.2C_Identification_and_Authentication}

Quixote provides a session management API; sessions are tracked via cookies. By default, session information is lost when the current process terminates, but it\'s easy to make sessions persistent: you just have to provide a persistent mapping object for Quixote to use instead of an ordinary dictionary.

[Dulcinea](http://www.mems-exchange.org/software/dulcinea/){.http} is a collection of modules useful for developing applications with Quixote and Durus. This includes user management classes.

Authentication is currently not addressed by Quixote; applications must provide their own authentication code. This will probably change in a future release (0.6?).

### Persistence Support {#Persistence_Support}

Outside the scope of Quixote. You can use it with a relational database, with [the Durus persistent object system](http://www.mems-exchange.org/software/durus/){.http}, with the ZODB, or with any other Python module for persistence.

### Presentation Support {#Presentation_Support}

#### Available Options {#Available_Options}

While Quixote comes with a templating language (PTL), it is only loosely integrated. Using PTL is optional and other templating languages or presentation support can easily be added.

#### PTL Introduction {#PTL_Introduction}

PTL, Python Template Language, is used to generate HTML from Python code (or to simply embed HTML in Python); the basic syntax is nearly the same as Python\'s, but expressions are converted to strings and appended to the output. An example snippet of PTL:

    def numbers [plain] (n):
        for i in range(n):
            i
            " " # PTL does not add any whitespace

If this is in a file named foo.ptl, you can now write `from foo import numbers ; numbers(5)`, which will produce the output \"1 2 3 4 5 \".

#### PTL Advantages {#PTL_Advantages}

All of Python\'s power is available in a way familiar to Python programmers. Exceptions and tracebacks are handled just like regular Python code. It\'s easy insert debugging code. PDB and the Python profiler can be used. Compiled PTL modules are saved like .pyc modules and once compiled are quick to load. You can use the Python module and package system to organize templates.

#### PTL Philosophy {#PTL_Philosophy}

Separating model and view is good. However, to achieve this separation it is not necessarily to cripple the templating language. Real programmers use abstractions. One way to apply abstraction to HTML page generation is to use templates that can be composed to build web pages (much like functions in traditional languages). As these abstractions become higher level, the amount of HTML markup used decreases. Normally, HTML markup is used mostly in low-level templates that are reused many times. In this situation it is logical to put the markup inside of some kind of quotes instead of outside. Take a look a large web applications written in PHP like Sourceforge or Squirrelmail. Notice that most of the code (including presentation releated code) is inside ?php tags.

The model and view should still be separated. This requires good design and some effort; a templating language is not going to do it for you. One good test is to imagine that you need to use a different technology for the interface (e.g. all web browsers stopped working, or, more likely, some better technology emerged). How much of your application code could be reused if all the interface code was thrown away?

PTL is not appropriate for every situation. If the interface is being built by a web designer rather than someone who knows how to program then it would be better to use something like [ZopePageTemplates](ZopePageTemplates) or something similar.

### InTheirOwnWords {#InTheirOwnWords}

The design goals for Quixote were:

1.  To allow easy development of Web applications where the accent is more on complicated programming logic than complicated templating.
2.  To make the templating language as similar to Python as possible. The aim is to make as many of the skills and techniques learned from writing regular Python code applicable to the task of writing Web applications.
3.  No magic. When it\'s not obvious what to do in a certain case, Quixote refuses to guess.

If you view a web site as a program, and web pages as subroutines, Quixote just might be the tool for you. If you view a web site as a graphic design showcase, and each web page as an individual work of art, Quixote is probably not what you\'re looking for.

A lengthier explanation of the design and of how the MEMS Exchange uses Quixote can be found at [http://www.amk.ca/python/writing/mx-architecture/](http://www.amk.ca/python/writing/mx-architecture/){.http} .

Post questions or add material to the [Quixote wiki](http://www.quixote.ca/qx){.http}.

### Comments {#Comments}

PTL breaks common utilities like `pydoc` and `pychecker`.
:::
