# TestSoftware

::: {#content dir="ltr" lang="en"}
## Complete Taxonomy {#Complete_Taxonomy}

- Please visit the [PythonTestingToolsTaxonomy](PythonTestingToolsTaxonomy) for a much more complete list of test tools of all kinds.

## Software {#Software}

- [UnitTest](./UnitTest.html){.nonexistent} in the standard library ([http://docs.python.org/lib/module-unittest.html](http://docs.python.org/lib/module-unittest.html){.http})

- [PyUnit](PyUnit) at [http://pyunit.sourceforge.net](http://pyunit.sourceforge.net){.http}

- [StatementCoverage](http://www.garethrees.org/2001/12/04/python-coverage/){.http} This module runs your code, then produces a report on how many statements were executed, and which ones were not. Use it to ensure your unit tests test everything.

- [DataTest](./DataTest.html){.nonexistent} at [http://formencode.org/docs/DataTest/README.html](http://formencode.org/docs/DataTest/README.html){.http}

- [McCabe](./McCabe.html){.nonexistent}-like Python Cyclomatic Complexity analysis tools are available at [http://journyx.com/curt/complexity.html](http://journyx.com/curt/complexity.html){.http}. They\'re written in Perl, but read and analyze only Python code. Complexity is bad, this will help you simplify code - especially code you didn\'t write.

- [zope.testing](http://www.python.org/pypi/zope.testing){.http} provides a powerful test runner that supports test discovery and a wide range of options to control how tests are run and results reported.

- [nose](http://somethingaboutorange.com/mrl/projects/nose/){.http} is \"a discovery-based [unittest](./unittest.html){.nonexistent} [extension](./extension.html){.nonexistent}\" that generally also supports [PyTest](PyTest) functionality.

## Best Practices {#Best_Practices}

## Discussion {#Discussion}

Sprouted out by [http://formencode.org/docs/DataTest/TODO.html](http://formencode.org/docs/DataTest/TODO.html){.http}.

What I need is a layered test system like

- test suit
  - with fast/normal/detailed mode
  - with known failing tests excluded
- test package to group related tests with preset parameters
- individual test
  - with options like log details
  - with ability to flex parameters, extend options etc.
- test utilities
  - fuzzy difference
  - different logging/reporting/visualization helpers
  - with output capture capability

\-- [MikeRovner](MikeRovner) 2004-02-27 19:25:32
:::
