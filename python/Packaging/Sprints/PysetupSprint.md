# Packaging/Sprints/PysetupSprint

::: {#content dir="ltr" lang="en"}
# 1. Pysetup Sprint 2011-04-28 to 2011-05-01 {#Pysetup_Sprint_2011-04-28_to_2011-05-01}

Join members from the \'Pip\' team as we work on completing the pysetup script and review the packaging(distutils2) API!

See the sprint goals for details.

## 1.1. Schedule {#Schedule}

Start at 9:00am EST on 2011-04-28.

## 1.2. Participants {#Participants}

- Kelsey Hightower (Lead) - Atlanta, USA (online) (4/28 - 5/1)
- Jannis Leidel \"jezdez\" (pip) - Berlin, Germany (online) (4/28 - 5/1)
- Hugo Lopes Tavares \"hugobr\" (pip) - Rio de Janeiro, RJ, Brazil (online) (4/28 - 5/1)
- Mathieu Leduc-Hamel \"mlhamel\" - Montreal, QC, Canada (online) (4/28 - 5/1)
- Carl Meyer \"carljm\" (pip) - Rapid City, SD, USA (online, as much as I can) (4/28 - 5/1)
- Alexis Metaireau \"alexis\" (packaging) - Oxford, UK (online) (4/28 - 5/1)

You can participate online by joining the #distutils channel on [freenode](http://freenode.net/){.http} and adding your name above.

## 1.3. Sprint Goals {#Sprint_Goals}

- make it easy for 3rd party tools such as [pip](http://www.pip-installer.org){.http} to integrate with packaging(distutils2) APIs

  - gather feedback and create a TODO list
  - fix whats broken

- finalize the pysetup feature set and implement missing features
  - borrow some idea\'s from pip

- documentation improvements
  - document all pysetup features
  - review and update the pysetup tutorial
  - review and update API documentation

- testing
  - make sure all pysetup features work (functional testing)
  - update packaging(distutils2) API and pysetup related unittests

## 1.4. Requirements {#Requirements}

### 1.4.1. Sign the PSF Contributor Agreement {#Sign_the_PSF_Contributor_Agreement}

Make sure you sign the PSF agreement and send it back to the PSF.

[Contributor Agreements](http://www.python.org/psf/contrib/){.http}

### 1.4.2. Hg repository {#Hg_repository}

    hg clone https://bitbucket.org/tarek/cpython

### 1.4.3. How to run tests {#How_to_run_tests}

    hg clone https://bitbucket.org/tarek/cpython
    cd cpython
    ./configure --with-pydebug
    make -s
    ./python -m test test_packaging

You also can run specifuc tests by doing:

    ./python -m packaging.tests.test_yourtest

### 1.4.4. How to build the docs {#How_to_build_the_docs}

It seems there is a dependency on svn, make sure have it installed before running \'make html;.

    hg clone https://bitbucket.org/tarek/cpython
    cd cpython/Doc
    make html

### 1.4.5. Specific Tasks {#Specific_Tasks}

Sprints run a lot better when there are specific things to work on. Specific tasks will be added to this section over the next couple of days.

- Update documentation that distribute is required for preforming \"setup.py\" based installs or:
  - Do not support installing projects that depend on distribute(setuptools)
- improve logging when running pysetup commands
  - print() vs logging statements, discuss and normalize
    - merwok: see [http://docs.python.org/dev/howto/logging#when-to-use-logging](http://docs.python.org/dev/howto/logging#when-to-use-logging){.http}
- support running pysetup \"actions\" on multiple projects arguments
  -    pysetup install tox nose
           ... install both tox and nose

\* Fix failing tests
:::
