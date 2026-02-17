# WebComponents

::: {#content dir="ltr" lang="en"}
# Web Components {#Web_Components}

For use with some of the frameworks listed on [WebFrameworks](WebFrameworks), the components/libraries/toolkits on this page often attempt to solve common problems in a way that can work with more than one particular framework; the idea being that you choose the component which does a particular job and it hopefully works with the framework you\'re developing your application in.

## Authorization Toolkits {#Authorization_Toolkits}

These allow you to add authorization to your web applications.

- [AuthKit](http://pypi.python.org/pypi/AuthKit){.http} is a WSGI framework that provides a structure for implementing your own authorization and authentication system. (Note [AuthKit has been discontinued since 2010-06-04.](http://wiki.pylonshq.com/display/authkitcookbook/Home){.http})

- [LibAuthKit](http://isotopesoftware.ca/wiki/LibAuthKit){.http} - A fork of AuthKit.

- [repoze.who](http://docs.repoze.org/who/){.http} - a WSGI authentication framework implemented as middleware.

- [repoze.what](http://what.repoze.org/docs/1.0/){.http} - a WSGI authorization framework implemented as middleware.

- [Auth modules](http://www.chrisarndt.de/en/software/python/#auth){.http} - a module collection for authentication purposes (last updated 2002)

- [Dataenc](http://www.voidspace.org.uk/python/archive.shtml#dataenc){.http} - allows secure and time limited logins to be encoded into Web pages for use with Web applications (last updated 2004)

- [HTTP basic authentication example](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/305288){.http} (this is a CGI script)

## Form Handling {#Form_Handling}

- [wheezy.html](https://bitbucket.org/akorn/wheezy.html){.https} is a lightweight HTML widget rendering library with preprocessing features for template engines.

- [wheezy.validation](https://bitbucket.org/akorn/wheezy.validation){.https} is a lightweight model update and validation library.

- [WTForms](http://wtforms.simplecodes.com/){.http} is a forms validation and rendering library for python web development.

- [FormEncode](http://formencode.org/){.http} - is a validation and form generation package.

- [FormBuild](http://pypi.python.org/pypi/FormBuild/){.http} is a package designed to help with the generation of HTML form components.

- [tw.forms](http://pypi.python.org/pypi/tw.forms/){.http} - Web Widgets for building and validating forms.

- [Deform](http://docs.repoze.org/deform){.http} is a featureful framework-agnostic form generation system.

## Request Dispatchers {#Request_Dispatchers}

A dispatcher takes the requests (i.e. the URL that a user types in) and then provides the response (i.e. the web application that creates the webpage that the user sees).

- [wheezy.routing](https://bitbucket.org/akorn/wheezy.routing){.https} is a lightweight path routing library. It is a simple mapping between URL patterns (as plain simple strings, curly expressions or regular expressions) to a handler that can be anything you like. The mapping can include other mappings and constructed dynamically.

- [Routes](http://routes.groovie.org/){.http} is a Python re-implementation of the Rails routes system for mapping URL\'s to Controllers/Actions and generating URL\'s. Routes makes it easy to create pretty and concise URL\'s that are RESTful with little effort.

- [selector](http://pypi.python.org/pypi/selector/){.http} - provides WSGI middleware for \"RESTful\" mapping of URL paths to WSGI applications.

- [Colubrid](http://wsgiarea.pocoo.org/colubrid/){.http} is a WSGI publisher which simplifies Python web developement. However, it should be possible to do the same things using [Werkzeug](http://werkzeug.pocoo.org/){.http}, a more recent Pocoo project offering a collection of web components.

## Templating Engines {#Templating_Engines}

Templating engines allow you to separate your application code from the presentation. Many of these engines can be used alone or within a high-level framework. A more extensive list can be found on the [Templating](Templating) page.

- [wheezy.template](https://bitbucket.org/akorn/wheezy.template){.https} is written in pure Python code. It is a lightweight template library. The design goals achived:

  - Compact, Expressive, Clean: Minimizes the number of keystrokes required to build a template. Enables fast and well read coding.
  - Intuitive, No time to Learn: Basic Python programming skills plus HTML markup. You are productive just from start. Use full power of Python with minimal markup required to denote python statements.
  - Do Not Repeat Yourself: Master layout templates for inheritance; include and import directives for maximum reuse.
  - Blazingly Fast: Maximum rendering performance: ultimate speed and context preprocessor features.

- [Jinja2](http://jinja.pocoo.org/2/){.http} is a small but fast and easy to use stand-alone template engine written in pure python.

- [Chameleon](http://chameleon.repoze.org/){.http} is a fast implementation of both TAL and Genshi syntaxes that compiles templates to python byte-code on first use.

- [ClearSilver](http://www.clearsilver.net/){.http} is a templating framework for Python/C/Perl, this templating system is used in Google Groups & \...

- [Mako](http://www.makotemplates.org/){.http} is an all-new templating engine which represents the best ideas of Myghty distilled into a completely-rewritten and updated API and syntax.

- [Ophelia](http://www.thomas-lotze.de/en/software/ophelia/){.http} (0.3 Released 2007-07-06) Generates XHTML pages from TAL templates. This avoids repetitive code, allows the site content to reside in the file system instead of a database, and lets Python scripts make the content dynamic.

- [JonsPythonModules](JonsPythonModules) (1.06 Released 2004-04-11) a set of simple yet powerful multi-threaded object-oriented CGI/FastCGI/mod_python/html-templating modules for Python

- [Cheetah](http://www.cheetahtemplate.org/){.http} - Cheetah is a Python-powered template engine and code generator. It may be used as a standalone utility or combined with other tools.

- [Genshi](http://genshi.edgewall.org/){.http} is a Python library that provides an integrated set of components for parsing, generating, and processing HTML, XML or other textual content for output generation on the web.
:::
