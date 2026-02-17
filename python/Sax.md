# Sax

::::: {#content dir="ltr" lang="en"}
\"Sax\" is an XML parser that operates element by element, line by line.

[MiniDom](MiniDom) sucks up an entire XML file, holds it in memory, and lets you work with it. Sax, on the other hand, emits events as it goes step by step through the file.

**NOTE**: A similarly fast but much simpler way to extract information from an XML document in an event-driven, memory efficient fashion is [ElementTree.iterparse()](http://docs.python.org/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse){.http}.

## Example {#Example}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-32fa4678096c8fdfaefb7aa9052525fd7f8bdf3e dir="ltr" lang="en"}
   1 import xml.sax
   2 
   3 class InkscapeSvgHandler(xml.sax.ContentHandler):
   4     def startElement(self, name, attrs):
   5         if name == "svg":
   6             for (k,v) in attrs.items():
   7                 print k + " " + v
   8 
   9 parser = xml.sax.make_parser()
  10 parser.setContentHandler(InkscapeSvgHandler())
  11 parser.parse(open("svg.xml","r"))
```
:::
::::

## Links {#Links}

- [HtmlParser](./HtmlParser.html){.nonexistent} \-- similar module, tailored to HTML interpretation

- [Python Library Reference, xml.sax](http://docs.python.org/lib/module-xml.sax.html){.http} \-- API documentation

- [Python XML FAQ and How-to](http://www.rexx.com/~dkuhlman/pyxmlfaq.html){.http} \-- describes sax & [MiniDom](MiniDom)

- [SAX: The Simple API for XML](http://pyxml.sourceforge.net/topics/howto/section-SAX.html){.http} \-- wordy tutorial

- [Charming Python:Revisiting XML tools for Python](http://www-106.ibm.com/developerworks/linux/library/l-pxml.html){.http} \-- kind of old

- [Usings SAX for Proper XML Output](http://www.xml.com/pub/a/2003/03/12/py-xml.html){.http}
:::::
