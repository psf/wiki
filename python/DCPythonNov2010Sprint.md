# DCPythonNov2010Sprint

:::::::::::::::::::::::::::::::: {#content dir="ltr" lang="en"}
# DCPython Meetup Sprint Plan (Nov 2010)

This is the project planning page for the [Python Beginner\'s Open Source Sprint](http://meetup.zpugdc.org/calendar/15036971/){.http .reference .external}, organized by the [DCPython Meetup](http://meetup.zpugdc.org/){.http .reference .external} (primarily Alex Clark).

There are a lot of people planning to attend, so a little advance planning is worthwhile. If people can figure out what projects they want to work on and use this page to connect with others interested in the same projects, it should be easier to get ourselves organized when we get together.

This is organized with a section for each \"larger\" project. If you\'re interested in a project listed here, add your name and any emphasis you\'d like to bring to the sprint. If you want to work on a project not listed already, add it!

::::: {#beginners .section}
### Beginners

Everyone attending the sprint that has never sprinted before, add your name under \"Developers\". If you plan to be available to help these folks, add your name and add (helper) afterward.

::: {#developers .section}
#### Developers

- [Alex Clark](AlexClark){.reference .external} (helper)
- [Fred Drake](FredDrake){.reference .external} (helper)
- Eric Groo
- Owen Martin
- Barry Austin
- Bob Schmertz
- Mohamed Ainab \<MohamedAinab\>
- Eric Palakovich Carr
- Londell
- Gabriel Getzie
- Mike Onzay
- Adam Reilly
- Sergejs Melderis
- Ryan Luu
:::

::: {#tasks .section}
#### Tasks

- Pick a project
- Get your laptop setup for development
- Fix bugs!
:::
:::::

::::: {#python-core .section}
### Python core

The interpreter and standard library.

::: {#id1 .section}
#### Developers

- [Eric Smith](./EricSmith.html){.nonexistent .reference .external}
- [Fred Drake](FredDrake){.reference .external}
:::

::: {#id2 .section}
#### Tasks

- [PEP-382](http://www.python.org/dev/peps/pep-0382/){.http .reference .external}, namespace packages
- Add [alternate float format specifiers](http://bugs.python.org/issue7094){.http .reference .external} (and Decimal, if time)
- Straighten out the JSON issues:
  - [json.load failure when C optimizations aren\'t built](http://bugs.python.org/issue9233){.http .reference .external}
  - [Incomplete json tests](http://bugs.python.org/issue5723){.http .reference .external}
:::
:::::

::::: {#distutils2-d2 .section}
### distutils2 (d2)

The next generation of Python packaging. You\'ll need [Mercurial (hg)](http://mercurial.selenic.com/){.http .reference .external} for revision control, and several versions of Python. See [http://bitbucket.org/fdrake/d2dev/src/tip/README.txt](http://bitbucket.org/fdrake/d2dev/src/tip/README.txt){.http .reference .external} for detailed preparation instructions.

For this, it\'s important to use \"clean\" Pythons; you don\'t want to have any extras installed in your site-python directory.

::: {#id3 .section}
#### Developers

- [Fred Drake](FredDrake){.reference .external}
- [Alex Clark](AlexClark){.reference .external}
- [Arc Riley](ArcRiley){.reference .external}
:::

::: {#id4 .section}
#### Tasks

- Remove fancygetopt; move to a clean application of optparse.
- the command line tool is now in run.py, with new options, and pass it to dist+fancygetopt to call the old system so what could be done is to list:
  1.  all command line options in dist.py that are not a call to a command and its options
  2.  move them to run.py
  3.  remove fancygetopt and clean up dist.
- Try converting a few projects to use d2, preferably based on the documentation alone.
- Continue the work on py3 support (ask tarek or regebro on irc)
:::
:::::

::: {#zope-toolkit-ztk .section}
### Zope Toolkit (ZTK)
:::

::::: {#django .section}
### Django

Look at fixing some long-standing and reasonably trivial documentation issues. Shared exploration of the code base. Help 1.3 get out the door.

::: {#id5 .section}
#### Developers

- [Steve Holden](SteveHolden){.reference .external} but not on my own! ;-)
- [Steve Waterbury](StephenWaterbury){.reference .external} but this is not a Steves-only project! ;-)
- [Alex Clark](AlexClark){.reference .external} Maybe I\'ll watch! :-)
- Eric Palakovich Carr
- Adam Reilly
:::

::: {#id6 .section}
#### Tasks

- [http://code.djangoproject.com/ticket/4027](http://code.djangoproject.com/ticket/4027){.http .reference .external}
- [http://code.djangoproject.com/ticket/3529](http://code.djangoproject.com/ticket/3529){.http .reference .external}
- [http://code.djangoproject.com/wiki/Sprints#Preparingforthesprint](http://code.djangoproject.com/wiki/Sprints#Preparingforthesprint){.http .reference .external}

Possibly consider whether context objects might benefit from the use of structural modifications.
:::
:::::

::::: {#plone .section}
### Plone

Python-based, open-source CMS

::: {#id7 .section}
#### Developers

- [Alex Clark](AlexClark){.reference .external}
:::

::: {#id8 .section}
#### Tasks

- PloneSoftwareCenter add-on ([http://plone.org/products/plonesoftwarecenter](http://plone.org/products/plonesoftwarecenter){.http .reference .external}) development
  - Fix bugs: [http://dev.plone.org/plone.org/search?q=psc&noquickjump=1&ticket=on](http://dev.plone.org/plone.org/search?q=psc&noquickjump=1&ticket=on){.http .reference .external}
  - Fix broken tests
:::
:::::

::::: {#parse2plone .section}
### Parse2Plone

Utility app for importing static website content into Plone

::: {#id9 .section}
#### Developers

- [Alex Clark](AlexClark){.reference .external}
:::

::: {#id10 .section}
#### Tasks

- Improve test coverage from 50% to 100% for parse2plone (you\'ll need a github account for this, so you can fork: [https://github.com/collective/parse2plone](https://github.com/collective/parse2plone){.https .reference .external} and send me pull requests.)
:::
:::::

::::: {#zc-buildout .section}
### zc.buildout

A tool for creating repeatable environments

::: {#id11 .section}
#### Developers

- [Alex Clark](AlexClark){.reference .external}
:::

::: {#id12 .section}
#### Tasks

- Fix bugs: [https://bugs.launchpad.net/zc.buildout](https://bugs.launchpad.net/zc.buildout){.https .reference .external}
:::
:::::

::::::::: {#dcpython-meetup-sprint-wrap-up .section}
[]{#wrap-up}

### DCPython Meetup Sprint Wrap Up

Here is a wrap-up of what was accomplished at the sprint.

::: {#id13 .section}
#### Distutils2 (d2)

- People
  - **Fred Drake**
  - Alex Clark
  - Travis Pinney
  - Arc Riley
  - Jim Fulton
- Progress
  - Fred schooled Travis, Alex and Jim in distutils2 setup, with a dev environment from:
    - [http://bitbucket.org/fdrake/d2dev](http://bitbucket.org/fdrake/d2dev){.http .reference .external} and a distutils2 checkout from:
    - [https://bitbucket.org/tarek/distutils2](https://bitbucket.org/tarek/distutils2){.https .reference .external}
  - The group ran the tests, but unfortunately did not manage to get much further than that.
  - Fred worked on ripping out the \"Fancy option parser\" to replace it with optparse.
  - Arc added Python 3 support to distutils2 setup.py and started adapting its unit tests to run clean on Py3.
:::

::: {#buildout .section}
#### Buildout

- People
  - **Jim Fulton**
  - Alex Clark
- Progress
  - Jim and Alex brainstormed on the status quo: \"brittle tests\" (i.e. tests giving spurious results depending on the system they are being run on), and then began to fix tests.
  - Jim worked on a test failure having to do with zc.recipe.egg tests that used the interpreter parameter to create a script ; the script being created in the tests used a technique only valid on newer ubuntus and Windows (where #!/path/to/exe refers to another script that has #!/path/to/exe instead of an executable)
  - Alex worked on a test having to do with Buildout being able to work with more than one version of Python ; so the test requires that more than one version of Python be found. I committed a \"modernization\" here: [http://svn.zope.org/zc.buildout/?rev=118514&view=rev](http://svn.zope.org/zc.buildout/?rev=118514&view=rev){.http .reference .external} \<[http://svn.zope.org/zc.buildout/?rev=118514&view=rev](http://svn.zope.org/zc.buildout/?rev=118514&view=rev){.http .reference .external}\> (to make the test find 2.6 and 2.5 vs. 2.4 and 2.3)
    - Alex plans to do further improvements that will make the test look for all 2.x versions.
:::

::: {#id14 .section}
#### Beginners

- People

  - **Steve Holden**
  - Bob Schmertz
  - Anyone else?

- Progress

  - Steve Holden was corralled with the beginners and discussed basic Python concepts
  - Looked at urllib as a code example
  - Some of the beginners broke off to do a \"fun\" project.
    - The \"fun\" project group mostly worked on bootstrapping an Android environment to develop an Android app with Python. The project created is called \'ConnectUs\' and the project is hosted on Google Code. [http://code.google.com/p/connectus/](http://code.google.com/p/connectus/){.http .reference .external}
  - All participants joined on other projects after lunch.

  I think next time we need to be better prepared for the beginners, and have a simple project that they can work on.
:::

::: {#id15 .section}
#### Python Core

- People

  - **Eric Smith**
  - Eric Groo
  - Vlad Korolev
  - Bob Schmertz
  - Owen Martin

- Progress

  - The core group worked on \"Alternate float formatting\", [http://bugs.python.org/issue7094](http://bugs.python.org/issue7094){.http .reference .external}, which actually affects float, Decimal, and complex. Eric Smith has posted their patch, is cleaning it up and will commit it for Python 3.2.

  - Additional comments from Londell:

        During the sprint, I also worked on some python core stuff too.  I'm chasing a buffering issue in the pty code (that I stumbled upon before
        participating in the sprint).  Eric gave me some ideas of some people to who I could reach out for more info on the pty code base.

        Additionally, Arc and I had several discussions.  He challenged me to dig deeper into the C/Python bridging code, and he challenged me to
        rethink how I implement behavior in my code to handle C and Python exceptions in the bridging code.
:::

::: {#id16 .section}
#### Django

- People
  - **Steve Holden**
  - Anyone else?
- Progress
  - Steve Holden and at Gabe Getzie worked on and submitted a documentation bug fix for issue #3529, a long-standing though minor bug in the documentation for context.update(). This served to refresh memory about the documentation setup.
:::

::: {#geodjango .section}
#### GeoDjango

- People:
  - Eric Palakovich Carr
  - Travis Pinney
  - Adam Reilly
  - Barry Austin
- Progress:
  - The GeoDjango group managed to get a patch out for [http://code.djangoproject.com/ticket/14284](http://code.djangoproject.com/ticket/14284){.http .reference .external}.
:::
:::::::::
::::::::::::::::::::::::::::::::
