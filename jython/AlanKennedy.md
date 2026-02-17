# AlanKennedy

::: {#content dir="ltr" lang="en"}
Alan Kennedy is a current jython committer, and has contributed

1.  A [NewSocketModule](NewSocketModule) with support for

    - Timeout and non-blocking operations
    - UDP / Datagrams
    - Socket Options
    - Client side SSL and certificate verification
    - Internet Protocol V6 (IPV6)
    - Internationalized Domain Names for Applications (IDNA)

2.  A [SelectModule](SelectModule) with

    - Support for the select function
    - Support for poll objects
    - Dedicated functions for cpython-compatibility

3.  [modjy](http://modjy.xhaus.com){.http}, which is a bridge between [WSGI](http://www.python.org/dev/peps/pep-0333/){.http} and java servlets, i.e. it permits any WSGI application to run inside a java servlet container such as [Tomcat](http://tomcat.apache.org){.http}.

Alan will address any jython issues relating to these modules, or modules that use them, including the following.

Please consider the cpython 2.5 documentation (linked below under the module names) for these modules to be authoritative for jython 2.5. If jython 2.5 behaviour differs from documented cpython 2.5 behaviour, or if you come across a network-related bug in any of these modules, please [File a bug on the jython tracker](http://bugs.jython.org){.http}.

- [socket](http://docs.python.org/release/2.5/lib/module-socket.html){.http}

- [select](http://docs.python.org/release/2.5/lib/module-select.html){.http}

- [asynchat](http://docs.python.org/release/2.5/lib/module-asynchat.html){.http}

- [asyncore](http://docs.python.org/release/2.5/lib/module-asyncore.html){.http}

- [BaseHTTPServer](http://docs.python.org/release/2.5/lib/module-BaseHTTPServer.html){.http}

- [SimpleXMLRPCServer](http://docs.python.org/release/2.5/lib/module-SimpleXMLRPCServer.html){.http}

- [SocketServer](http://docs.python.org/release/2.5/lib/module-SocketServer.html){.http}

- [ftplib](http://docs.python.org/release/2.5/lib/module-ftplib.html){.http}

- [gopherlib](http://docs.python.org/release/2.5/lib/module-gopherlib.html){.http}

- [httplib](http://docs.python.org/release/2.5/lib/module-httplib.html){.http}

- [imaplib](http://docs.python.org/release/2.5/lib/module-imaplib.html){.http}

- [nntplib](http://docs.python.org/release/2.5/lib/module-nntplib.html){.http}

- [poplib](http://docs.python.org/release/2.5/lib/module-poplib.html){.http}

- [smtpd](http://docs.python.org/release/2.5/lib/module-smtpd.html){.http}

- [smtplib](http://docs.python.org/release/2.5/lib/module-smtplib.html){.http}

- [telnetlib](http://docs.python.org/release/2.5/lib/module-telnetlib.html){.http}

- [urllib](http://docs.python.org/release/2.5/lib/module-urllib.html){.http}

- [urllib2](http://docs.python.org/release/2.5/lib/module-urllib2.html){.http}

- [xmlrpclib](http://docs.python.org/release/2.5/lib/module-xmlrpclib.html){.http}

Alan also runs a jython-related blog: [Jython Journeys](http://jython.xhaus.com){.http} and a [Jython Open Source Portal](http://opensource.xhaus.com){.http}, where you can find [jyson](http://jyson.xhaus.com){.http}, a fast pure-java [JSON](http://json.org){.http} codec for jython.
:::
