# WebServers

::: {#content dir="ltr" lang="en"}
# Web Servers and Python {#Web_Servers_and_Python}

Python-based Web servers have been available in the standard library for many years (see the BaseHTTPServer, SimpleHTTPServer and CGIHTTPServer modules). To address various issues of scalability, robustness and convenience with such existing servers, other server frameworks and solutions have been developed since that time.

## Web Servers written in Python {#Web_Servers_written_in_Python}

- [Chaussette](https://pypi.python.org/pypi/chaussette/){.https} - A web server capable of running using multiple different underlying http engines

- [CherryPy - a pythonic, object-oriented HTTP framework](http://www.cherrypy.org){.http}

- [Gunicorn](http://gunicorn.org/){.http} - inspired by the Ruby server, Unicorn

- [Rocket](https://launchpad.net/rocket/){.https} - a pure python HTTP server for WSGI applications and static files which runs on cPython 2.5-3.x and Jython 2.5

- [Spawning](http://pypi.python.org/pypi/Spawning/){.http} - a WSGI server which supports multiple processes, multiple threads, green threads, non-blocking HTTP io, and automatic graceful upgrading of code.

- [Tornado](http://www.tornadoweb.org/){.http} - an open source version of the scalable, non-blocking web server and tools that power [FriendFeed](./FriendFeed.html){.nonexistent}.

- Twisted includes [a very scalable web server](http://twistedmatrix.com/trac/wiki/TwistedWeb){.http} written in Python.

- [Waitress](https://pypi.org/project/waitress/){.https} - A WSGI server that runs on Windows and UNIX under [PyPy](PyPy), CPython 2.X and CPython 3.X.

## Web Servers embedding Python {#Web_Servers_embedding_Python}

In addition to the above, some non-Python-based Web servers support Python-based applications by embedding the Python virtual machine for improved performance:

- [G-WAN](http://gwan.ch/){.http} is a (Linux-only) Web application server that supports servlet scripts written in Python among other languages

- [mod_wsgi](http://www.modwsgi.org){.http} embeds Python in the Apache HTTP server

- [Modjy](http://modjy.xhaus.com/){.http} embeds a jython interpreter in Java Servlet containers, e.g. Tomcat, Glassfish, Websphere, etc, and supports WSGI. Distributed with jython since March 2009.

- [ModPython](ModPython) embeds Python in the Apache HTTP server

- [Nginx WSGI](http://wiki.nginx.org/NginxNgxWSGIModule){.http} support module for Nginx HTTP server

- [PyWX](PyWX) embeds Python in AOLServer

## Standard Library Technologies {#Standard_Library_Technologies}

- [BaseHTTPServer](BaseHttpServer) (along with successors such as [DocXmlRpcServer](DocXmlRpcServer)) can be considered as the original Python Web framework, but it really just provides the ability to process HTTP requests and to generate responses using a relatively primitive API. Some [WebFrameworks](WebFrameworks) use it as the basis for serving content, however.

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite) [CategoryJython](CategoryJython) [CategoryJython](CategoryJython)
:::
