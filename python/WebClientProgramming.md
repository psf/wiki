# WebClientProgramming

::: {#content dir="ltr" lang="en"}
# Client-Side Web Programming {#Client-Side_Web_Programming}

## Libraries {#Libraries}

- [µTidylib](http://utidylib.berlios.de/){.http} and [mxTidy](http://www.egenix.com/files/python/mxTidy.html){.http} \-- Python interfaces to [html tidy](http://tidy.sourceforge.net/){.http} library to clean up HTML documents.

- [html5lib](http://code.google.com/p/html5lib){.http} A HTML5-compliant library for parsing arbitarily-broken HTML to a range of tree formats including minidom, elementtree (including lxml) and [BeautifulSoup](./BeautifulSoup.html){.nonexistent}

- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/){.http} \-- a permissive HTML parser.

- Don\'t use [HTMLParser (Python 2.x)](https://docs.python.org/2/library/htmlparser.html){.https} or [html.parser (Python 3.x)](https://docs.python.org/3.5/library/html.parser.html){.https} on HTML that might be invalid! That way lies pain. Either clean it up (using tidy), or use a different parser.

- [urllib](http://docs.python.org/library/urllib.html){.http}, [urllib2](http://docs.python.org/library/urllib2.html){.http}, and [httplib](http://docs.python.org/library/httplib.html){.http} in the standard library.

- [ClientCookie](http://wwwsearch.sourceforge.net/old/ClientCookie/){.http}, [ClientForm](http://wwwsearch.sourceforge.net/ClientForm/){.http}, and [Mechanize](http://wwwsearch.sourceforge.net/mechanize/){.http} are higher-level libraries for writing a web client.

- [mechanoid](http://pypi.python.org/pypi?:action=display&name=mechanoid){.http} a mechanize fork.

- [libxml2dom](http://www.python.org/pypi/libxml2dom){.http} can parse HTML by employing libxml2\'s liberal HTML parser.

## Resources {#Resources}

- [Grab a document from the web](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52199){.http} - from the Python Cookbook

- [Python web-client programming general FAQs](http://wwwsearch.sourceforge.net/old/bits/GeneralFAQ.html){.http}.

- [urllib \-- Open arbitrary resources by URL](http://docs.python.org/library/urllib.html){.http}

- [urllib2 \-- extensible library for opening URLs](http://docs.python.org/library/urllib2.html){.http}
:::
