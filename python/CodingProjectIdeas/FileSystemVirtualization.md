# CodingProjectIdeas/FileSystemVirtualization

::: {#content dir="ltr" lang="en"}
Note: this idea was originally written for SoC 2005. Since then [PEP 355](http://www.python.org/dev/peps/pep-0355/){.http} was written, which describes an interface for a path object. This should serve as the basis for any implementation.

There are several object-oriented ways to access filesystems in Python, though none have reached a critical mass of popularity. Two instances are [py.local](http://codespeak.net/py/current/doc/){.http} and [path](http://www.jorendorff.com/articles/python/path/){.http}.

Given that OO interface, you can create objects that look like filesystems but access other resources, like WebDAV servers, databases, etc. py.local contains an implementation that accesses a svn repository.

One of these could be extended, or a generic interface for filesystems could be developed alongside several functional implementations of that interface.

------------------------------------------------------------------------

- Take a look at Tcl\'s virtual file system for some inspiration. \-- Brett Cannon

- An existing work in Python is [itools.vfs](http://download.ikaaro.org/doc/itools/Chapter--VFS.html){.http}. Work on filesystem virtualisation should also take into account the existing urllib/urllib2 modules (and improvements - see [CleanupUrlLibProject](CleanupUrlLibProject)) along with other packages which provide file-like and os/os.path-like interfaces, notably [ftputil](http://ftputil.sschwarzer.net/){.http}. \-- [PaulBoddie](PaulBoddie)

- Check out [filelike](http://pypi.python.org/pypi/filelike/0.2.2){.http}
:::
