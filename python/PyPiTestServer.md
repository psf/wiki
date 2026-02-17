# PyPiTestServer

::: {#content dir="ltr" lang="en"}
# Create a server that tests uploaded packages on PyPI. {#Create_a_server_that_tests_uploaded_packages_on_PyPI.}

## Work to be done {#Work_to_be_done}

The work is separated into three steps:

1.  a solution capable of running scripts when an event occurs (a new release of project X is available on PyPI)
2.  a Continuous integration server able to run the testsuite for those distributions
3.  a quality mesurement tool, able to provide feedback and indicators on the code (compliance PEP8, pyflakes, potentially malicious softwares etc.)

## Resources {#Resources}

\- [2010 idea](http://tarekziade.wordpress.com/2010/03/21/another-gsoc-idea-a-pypi-testing-infrastructure/){.http} and [code](https://bitbucket.org/mouad/pypi-testing-infrastructure-pyti/overview){.https}

\- [2011 updated idea](http://tarekziade.wordpress.com/2011/02/21/qa-portal-ideas/){.http}

\- On this wiki: [PyPITestingInfrastructure](PyPITestingInfrastructure)

## What do people want {#What_do_people_want}

### What do people what to run {#What_do_people_what_to_run}

- Run quality indicators about the code
- Run quality indicators about the packaging (compat with du2 standards for instance)
- Run Test
- Run setup.

### What do people what to know {#What_do_people_what_to_know}

- Report about the run itself (does the test pass ? does the install went well ?)
- Report about system access done (FS network)
- Report about resource used ? (bonus)
:::
