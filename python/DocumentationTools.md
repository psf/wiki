# DocumentationTools

::: {#content dir="ltr" lang="en"}
This page is primarily about tools that help, specifically, in generating **documentation for software written in Python**, i.e., tools that can use language-specific features to automate at least a part of the code documentation work for you. The last section also lists general documentation tools with no specific support for Python (though some of them are themselves written in Python).

Tools that support auto-documentation of code can be broadly classified into tools that:

- import the code to generate documentation based on runtime introspection
- parse and analyze the code statically (without running it)

See [here](./API(20)Extraction.html) for a longer explanation of the two concepts.

Tools that generate documentation from user-provided input typically use plain text markup formats such as [reStructuredText](reStructuredText) (reST, the markup used for writing the official Python documentation) or [Markdown](http://daringfireball.net/projects/markdown/){.http}.

## Python docstrings {#Python_docstrings}

Python modules are usually documented using docstrings. You can read a module\'s docstrings from the Python interactive prompt with the `help()`{.backtick} function. For example:

    import distutils
    help(distutils)

The `help()`{.backtick} function uses Python\'s standard pydoc module, as does the `pydoc`{.backtick} command that comes with Python.

## Automatic Python API documentation generation tools {#Automatic_Python_API_documentation_generation_tools}

- [autosummary](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html){.https}, an extension for the Sphinx documentation tool.

- [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html){.https}, a Sphinx-based processor that processes/allows reST doc strings.

- [pdoc](https://pdoc.dev/){.https}, a simple Python 3 command line tool and library to auto-generate API documentation for Python modules. Supports Numpydoc / Google-style docstrings, doctests, reST directives, PEP 484 type annotations, custom templates \...

- [pdoc3](https://pdoc3.github.io/pdoc/){.https}, a fork of pdoc for Python 3 with support for Numpydoc / Google-style docstrings, doctests, LaTeX math, reST directives, PEP 484 type annotations, custom templates \...

- [PyDoc](https://www.pydoc.io){.https}, a documentation browser (in HTML) and/or an off-line reference manual. Also in the standard library as [pydoc](http://docs.python.org/lib/module-pydoc.html){.http}.

- [pydoctor](https://launchpad.net/pydoctor){.https}, a replacement for now inactive Epydoc, born for the needs of Twisted project.

- [Doxygen](http://www.doxygen.org){.http} can create documentation in various formats (HTML, LaTeX, PDF, \...) and you can include formulas in your documentation (great for technical/mathematical software). Together with [Graphviz](http://graphviz.org/){.http}, it can create diagrams of your code (inhertance diagram, call graph, \...). Another benefit is that it handles not only Python, but also several other programming languages like C, C++, Java, etc.

# No longer under development {#No_longer_under_development}

- Another [PythonDoc](./PythonDoc.html){.nonexistent} - uses [JavaDoc](./JavaDoc.html){.nonexistent}-style comments, and produces HTML and XML output. Can also be used as a library, producing [ElementTree](ElementTree) descriptions of your source code. [http://effbot.org/zone/pythondoc.htm](http://effbot.org/zone/pythondoc.htm){.http}

- [EpyDoc](EpyDoc), [http://epydoc.sourceforge.net/](http://epydoc.sourceforge.net/){.http}

- [Endo](https://svn.enthought.com/enthought/wiki/EndoHowTo){.https} from Enthought Tool Suite - generates HTML API documentation from docstrings and from plain comments that immediately precede variable assignments.

- [Pudge](http://pudge.lesscode.org/){.http} (defunct)

- [HappyDoc](http://happydoc.sourceforge.net/){.http} ([not supported](http://sourceforge.net/projects/happydoc/forums/forum/30132/topic/3563472?message=8100340){.http}) - documentation extraction tool that uses the parse tree for a module to derive the information used in its output, rather that importing the module directly.

- [EasyDoc](./EasyDoc.html){.nonexistent} - uses an HTML-like markup language, similar to the language used by [JavaDoc;](http://c2.com/cgi/wiki?JavaDoc%3B "Wiki"){.interwiki} and produces HTML output ([http://htmltmpl.sourceforge.net/easydoc.html](http://htmltmpl.sourceforge.net/easydoc.html){.http})

- [PythonDoc](./PythonDoc.html){.nonexistent} - uses [StructuredText](StructuredText) input format (*not* reST), and can produce HTML and XML output. It uses XML as an intermediate representation, to simplify the addition of new output formats. [http://starship.python.net/crew/danilo/pythondoc/](http://starship.python.net/crew/danilo/pythondoc/){.http}

- Apydia, [http://apydia.ematia.de/](http://apydia.ematia.de/){.http}

## Documentation processing tools {#Documentation_processing_tools}

- [DocUtils](DocUtils), [http://docutils.sourceforge.net/](http://docutils.sourceforge.net/){.http} [reStructuredText](reStructuredText) processing engine

- [Sphinx](Sphinx), [https://www.sphinx-doc.org/](https://www.sphinx-doc.org/){.https} - converts reStructuredText documentation into various formats

## Other projects that can be used to produce API documentation {#Other_projects_that_can_be_used_to_produce_API_documentation}

- [XIST](http://www.livinglogic.de/Python/xist/index.html){.http} - an XML based extensible HTML generator written in Python.

- [HtmlGen](http://starship.python.net/crew/friedrich/HTMLgen/html/main.html){.http} - a Python library for generating HTML documents.

## Other documentation processing tools {#Other_documentation_processing_tools}

- [Pandoc](http://johnmacfarlane.net/pandoc/){.http} \-- written in Haskell, this tool can read and write a number of formats (including reST).

- [Rippledoc](http://www.unexpected-vortices.com/sw/rippledoc/){.http} (formerly known as Gouda) \-- a command-line tool written in Clojure (using Pandoc under the hood) to generate multi-chapter html documents from Markdown text files.

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
:::
