# DataRepresentation

::: {#content dir="ltr" lang="en"}
## Data on the web {#Data_on_the_web}

There are several approaches to represent data using Python on a web page (see [WebProgramming](WebProgramming)).

- [PythonInWebPage](PythonInWebPage)

- [StructureAnnotation](StructureAnnotation)

- [Programmatic](Programmatic)

Another interesting article about this is [\"Choosing a Templating System\"](http://www.perl.com/pub/a/2001/08/21/templating.html){.http}.

### Syntax {#Syntax}

Different approaches lead to different design decisions. Often it is the principal reason that new template systems get invented:

- [ElementBasedSyntax](ElementBasedSyntax)

- [CommentBasedSyntax](CommentBasedSyntax)

- [AttributeBasedSyntax](AttributeBasedSyntax)

### Examples {#Examples}

Some presentation systems fall neatly into the categories above. Others are less easy to classify but have a closer association to one category than the others.

#### PythonInWebPage {#PythonInWebPage}

- Castalian

- [Cheetah](Cheetah)

- PSP (from [Webware](./Webware.html))

- [Spyce](Spyce)

#### StructureAnnotation {#StructureAnnotation}

- [ClearSilver](ClearSilver)

- DOMTemplate (from [TwistedMatrix](TwistedMatrix))

- DTML (Document Template Markup Language - see [Zope](Zope))

- [Woven](http://www.twistedmatrix.com/documents/howto/woven){.http} (from [TwistedMatrix](TwistedMatrix))

- wt (see [JonsPythonModules](JonsPythonModules))

- ZPT (Zope Page Templates - see [Zope](Zope))

#### Hybrids {#Hybrids}

- CHTL and CGTL (from [CherryPy](CherryPy)) - [PythonInWebPage](PythonInWebPage) and [StructureAnnotation](StructureAnnotation)

- [PyMeld](PyMeld) - [StructureAnnotation](StructureAnnotation) and [Programmatic](Programmatic)

- [STML](./STML.html){.nonexistent} (from [SkunkWeb](SkunkWeb)) - [PythonInWebPage](PythonInWebPage), [StructureAnnotation](StructureAnnotation), and [Programmatic](Programmatic) being all equally apt (or equally inadequate)

#### Programmatic {#Programmatic}

- PTL (from [Quixote](Quixote))

### Notes {#Notes}

Feel free to add more abstract descriptions and more examples to help people decide what they are looking for!

Do you need to use full-fledged python, embedded bits of definitions but no functions \-- there is a range of options depending on your problem. Sometimes there\'s no python in \"the output page\" \-- as in raw documents put thru a filter. Or there may be limited amounts of embedded python \-- as in YAPTU and other filters. Or python may be the matrix language, with text embedded within it. Your handler code can be anything from a substituter (using, say, regular expressions to catch things to be altered) to a mini python engine. See [\'Python Journal 3(1)\'](http://pythonjournal.cognizor.com){.http} a feature article that draws together several of the options above into a series on the pure-text to pure-python \"dimension\". See what your options are.
:::
