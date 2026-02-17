# teng

::: {#content dir="ltr" lang="en"}
A framework for [WebProgramming](WebProgramming).

### Masthead {#Masthead}

URL

:   [http://teng.sf.net](http://teng.sf.net){.http}

version

:   1.1.2 (*2005-05-26*)

licence

:   OSI approved licence - open source. (See [http://teng.sourceforge.net/?page=download](http://teng.sourceforge.net/?page=download){.http}.)

documentation

:   [http://teng.sourceforge.net/?page=manual](http://teng.sourceforge.net/?page=manual){.http}

platforms
:   Teng was tested on Linux x86, Linux amd64.

Python versions
:   2.1, 2.2, 2.3, 2.4

### Comments {#Comments}

Teng is a general purpose templating engine (whence Teng). Teng is primary a C++ library with easy\--to\--use API but it is also available (at least) as Python module and PHP extension. Teng strictly separates application logic from presentation logic. Programmer writes code which fetches data (for example from database, application server etc.) and supplies them to the templating engine. Presentation coder (for example web designer) writes templates and doesn\'t bother about data origin. The only thing programmer and presentation coder must obey is that data structure must conform to the template. Probably the most important use of Teng is generating HTML pages for web presentations. It is also wery useful for generating mail messages (but not spams). Teng composes resulting text/page/file by combining input template with program supplied data together with (optional) configuration and localization (language) dictionary. Localization support of Teng allows you to just write single template set for any number of supported languages. Templates and dictionaries are cached by engine for further use.
:::
