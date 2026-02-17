# PyMeld

::: {#content dir="ltr" lang="en"}
A framework for [WebProgramming](WebProgramming).

### Masthead {#Masthead}

URL

:   [http://www.entrian.com/PyMeld/](http://www.entrian.com/PyMeld/){.http}

version
:   2.1.4 ( 2009)

licence
:   Sleepycat

platforms
:   Most if not all

Python versions
:   2.2

### Deployment Platforms {#Deployment_Platforms}

PyMeld is one of the available [DataRepresentation](DataRepresentation) technologies for Python. It could probably be deployed in most of the Web frameworks currently available.

### Suitability {#Suitability}

Dependent on the means of deployment.

### Development Interfaces {#Development_Interfaces}

A mix of template definition and programmatic \"instantiation\" of those templates, reminiscent of Enhydra\'s XMLC but arguably without the hierarchical nature of the XMLC data model. In effect, after defining templates whose elements are tagged with certain identifiers, the developer must then invoke certain calls to replace the contents of the tagged elements by specifying the identifiers and the text to be used instead. The choice of identifiers appears to be arbitrary.

### Environment Access {#Environment_Access}

Since Python code is required to instantiate the templates, other Python modules could be used to enhance this process.

### Session, Identification and Authentication {#Session.2C_Identification_and_Authentication}

Not applicable.

### Persistence Support {#Persistence_Support}

Not applicable.

### Presentation Support {#Presentation_Support}

PyMeld uses templates which can be considered as implementing [StructureAnnotation](StructureAnnotation), but a [Programmatic](Programmatic) approach is still required to instantiate these templates.

### InTheirOwnWords {#InTheirOwnWords}

Lets you manipulate HTML (and XML, informally) using a Pythonic object model. PyMeld is a single Python module, PyMeld.py. It works with all versions of Python from 1.5.2 upwards.

### Comments {#Comments}

PyMeld gets round the frequently encountered limitation that additional tags or attributes in HTML, used by template systems for instantiation purposes, are not universally accepted by various HTML editors. To do this, it employs \'id\' attributes within the HTML elements to be used in the instantiation process, thus potentially giving the possibility for round-trip editing of the templates - the template files can be given to designers using WYSIWYG tools for enhancement and then returned to the developers for additional annotation without the original annotations necessarily being completely destroyed.

### Hosting {#Hosting}

Not applicable.
:::
