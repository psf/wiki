# PythonXml

::: {#content dir="ltr" lang="en"}
# Python and XML {#Python_and_XML}

A variety of XML processing solutions are available for Python. This page attempts to list the major tools.

## Packages in the standard library {#Packages_in_the_standard_library}

The standard library has a number of tools available, which fall into mainly three categories:

- a pythonesque, simple-to-use and very fast XML tree library:
  - [ElementTree](ElementTree) - the [xml.etree](http://docs.python.org/library/xml.etree.elementtree.html){.http} package (new in Python 2.5 but available for older versions, also see the fast xml.etree.cElementTree and the independent implementation [lxml](http://lxml.de/){.http})
- event-driven XML parsers:
  - [ElementTree](ElementTree)\'s [iterparse()](http://docs.python.org/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse){.http} - a fast and easy-to-use event-driven parser with a high-level XML tree interface

  - pyexpat - a fast, low-level XML parser with an event-based callback interface

  - [Sax](Sax) - the xml.sax package, a Python implementation of the well-known low-level SAX API
- XML tree libraries that adhere to the W3C DOM standard:
  - [MiniDom](MiniDom) - the xml.dom.minidom package

  - [PullDom](PullDom) - the xml.dom.pulldom package

The DOM and SAX packages have the advantage of being compatible with standard or de facto standard APIs, so users who are already familiar with these APIs can use them without learning too many new things. Everyone else should start with the faster and more pythonic [ElementTree](ElementTree) library, which is very well integrated into the Python language, and therefore very easy to learn and use.

## External packages {#External_packages}

A long list of special purpose and general purpose Python XML packages is available from [PyPI](http://pypi.python.org/pypi?:action=browse&show=all&c=500){.http}. The following is a choice of major tools that support a broader set of XML features.

### Pythonic tools {#Pythonic_tools}

- [lxml](http://lxml.de/){.http} - a pythonic, [ElementTree](ElementTree)-compatible binding for the [libxml2](http://xmlsoft.org/){.http} and [libxslt](http://xmlsoft.org/XSLT/){.http} libraries that comes with all sorts of powerful XML (and HTML) tools, well integrated into an easy-to-use Python API

- [lxml.objectify](http://lxml.de/objectify.html){.http} - a Python object API for XML based on lxml

- [PyXB](http://pyxb.sourceforge.net/){.http} - generates Python classes/modules that correspond to data structures/namespaces defined by XMLSchema, with validation

- [PyXSD](http://pyxsd.org/){.http} - an XML Schema mapping too (somewhat dated, last released in 2006)

- [generateDS](http://www.rexx.com/~dkuhlman/generateDS.html){.http} - generates Python data structures (for example, class definitions) from an XML Schema document

- [Amara 2.x](http://xml3k.org/Amara){.http} - Amara provides tools you can trust to conform with XML standards without losing the familiar Python feel

### W3C DOM-like libraries {#W3C_DOM-like_libraries}

- [PyXML](http://sourceforge.net/projects/pyxml/){.http} - external add-on to Python\'s original XML support - (Warning: no longer maintained, does not work with recent Python versions)

- [itools.xml](http://www.ikaaro.org/itools/){.http} - itools provides XML processing support in a fashion similar to that of [PullDom](PullDom)

- [libxml2dom](http://www.python.org/pypi/libxml2dom){.http} - PyXML-style API for the libxml2 Python bindings

- [qtxmldom](http://www.python.org/pypi/qtxmldom){.http} - PyXML-style API for the qtxml Python bindings

- [4Suite](http://4suite.org/){.http} - a framework for XML (and RDF) processing

### XPath Support {#XPath_Support}

- [py-dom-xpath](http://code.google.com/p/py-dom-xpath/){.http} - pure Python XPath implementation for use with DOM libraries

- [lxml](http://lxml.de/){.http} - lxml has standards compliant XPath 1.0 support based on libxml2. It also supports the [EXSLT](http://www.exslt.org/){.http} extensions (including Python regular expressions) and allows calling Python functions from within XPath expressions.

- [Amara 2.x](http://xml3k.org/Amara2){.http} - Amara exposes an API to fully-compliant XPath (including [EXSLT](http://www.exslt.org/){.http})

- [SaxonC](https://www.saxonica.com/saxon-c/documentation12/index.html){.https} from Saxonica includes a Python API with full support for XPath 3.1.

### XSLT Support {#XSLT_Support}

If not mentioned otherwise, this means XSLT 1.0, not XSLT 2.0.

- [lxml](http://lxml.de/){.http} has excellent (and easy-to-use) XSLT support that is based on [libxslt](http://xmlsoft.org/XSLT/){.http}. It also supports calling into Python code from XSL transformations through both XPath and XSLT extensions.

- [XSLTools](http://www.python.org/pypi/XSLTools){.http} - XSL transformations on top of [libxslt](http://xmlsoft.org/XSLT/){.http} and [libxml2dom](http://www.python.org/pypi/libxml2dom){.http}, with added Web development support

- Some tools linked from the [XQuery homepage](http://www.w3.org/XML/Query/#implementations){.http} provide Python bindings for their XSLT2 and XPath2 implementations

- [Amara 2.x](http://xml3k.org/Amara2){.http} - Amara exposes an API to fully-compliant XSLT (including [EXSLT](http://www.exslt.org/){.http})

- [SaxonC](https://www.saxonica.com/saxon-c/documentation12/index.html){.https} from Saxonica includes a Python API with full support for XSLT 3.0

### XML-based Communications {#XML-based_Communications}

- [jabber.py](http://jabberpy.sourceforge.net/){.http} - a Python module for the jabber instant messaging protocol

- [PyXMPP](http://pyxmpp.jajcus.net/){.http} - a Python XMPP (RFC 3920,3921) and [Jabber](http://www.jabber.org/protocol/){.http} implementation

- [xmpppy](http://xmpppy.sourceforge.net/){.http} - a Python library that is targeted to provide easy scripting with Jabber

### Web Services {#Web_Services}

- [XmlRpc](XmlRpc)

  - [DocXmlRpcServer](DocXmlRpcServer)

- see [WebServices](WebServices)

### Object Serialization in XML {#Object_Serialization_in_XML}

- [pyxser](http://coder.cl/software/pyxser/){.http} - a Python extension to serialize/deserialize Python objects into XML

## Books and Articles {#Books_and_Articles}

- [XmlBooks](XmlBooks)

- [Tutorials on XML processing with Python](./Tutorials(20)on(20)XML(20)processing(20)with(20)Python.html)

## SIG {#SIG}

- [http://python.org/community/sigs/current/xml-sig](http://python.org/community/sigs/current/xml-sig){.http}

## Editorial Notes {#Editorial_Notes}

The above lists should be arranged in ascending alphabetical order - please respect this when adding new entries. When specifying release dates please use the format YYYY-MM-DD.
:::
