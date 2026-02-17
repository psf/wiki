# PackagingSprints

:::: {#content dir="ltr" lang="en"}
# Join us at sprints! {#Join_us_at_sprints.21}

We welcome package maintainers, backend and frontend web developers, infrastructure administrators, technical writers, and testers to join us at sprints to help us make the new PyPI, and [the entire packaging/distribution toolchain](https://packaging.python.org/key_projects/#pypa-projects){.https}, as usable and robust as possible.

We\'re working on Warehouse, setuptools, pip, twine, virtualenv, pipenv, readme-renderer, bandersnatch, conda, conda-build, manylinux, and tox. We\'re using Pyramid, Pylons, StimulusJS, CSS, static typechecking with mypy, ElasticSearch, Sphinx, and regular Python, and we also need help with Travis CI and continuous integration, and Anaconda and Windows support.

Newcomers are usually welcome \-- we\'ll help you learn and contribute!

Members of the Packaging Working Group and the Python Packaging Authority will be at these sprints/events:

::: table-of-contents
Contents

1.  [Join us at sprints!](#Join_us_at_sprints.21)
    1.  [Upcoming events](#Upcoming_events)
        1.  [EuroPython 2020](#EuroPython_2020)
        2.  [And\...](#And...)
    2.  [Past events](#Past_events)
        1.  [Pre-PyGotham sprint day and night, autumn 2019](#Pre-PyGotham_sprint_day_and_night.2C_autumn_2019)
        2.  [June 2019 NYC sprint day](#June_2019_NYC_sprint_day)
        3.  [PyCon North America 2019](#PyCon_North_America_2019)
        4.  [Sprint](#Sprint)
        5.  [PyPA October 2018 sprint at Bloomberg](#PyPA_October_2018_sprint_at_Bloomberg)
        6.  [PyCon North America 2018](#PyCon_North_America_2018)
        7.  [Sprint](#Sprint-1)
        8.  [EuroPython 2018](#EuroPython_2018)
        9.  [April 2018: NYC Python/PyLadies Sprint Night](#April_2018:_NYC_Python.2FPyLadies_Sprint_Night)
        10. [Packaging BoF/Open Space at PyCon 2018](#Packaging_BoF.2FOpen_Space_at_PyCon_2018)
        11. [Pipenv BoF/Open Space](#Pipenv_BoF.2FOpen_Space)
:::

## Upcoming events {#Upcoming_events}

### EuroPython 2020 {#EuroPython_2020}

[July 25-26, online](https://wiki.python.org/moin/EuroPython2020/PackagingSprint){.https}. More info coming soon; see [sprint wiki page](https://wiki.python.org/moin/EuroPython2020/PackagingSprint){.https}!

### And\... {#And...}

You\'re free to plan another one! Probably good to announce it on [https://discuss.python.org/](https://discuss.python.org/){.https} .

## Past events {#Past_events}

### Pre-PyGotham sprint day and night, autumn 2019 {#Pre-PyGotham_sprint_day_and_night.2C_autumn_2019}

**Dates**: Thursday, 3 October 2019

**Times**: 10am-5pm daytime, 6:30-9:30pm evening

**Location:** a location in New York City; remote folks can [join us via IRC](https://webchat.freenode.net/?channels=%23pypa-dev){.https}; [https://www.meetup.com/nycpython/events/265028634/](https://www.meetup.com/nycpython/events/265028634/){.https}

**Attending**:

- Sumana Harihareswara

- Katie McLaughlin

- Trishank Kuppusamy

- Julian Berman

- Brian Rutledge

- \[additional contributors\] - speak up in [https://discuss.python.org/t/pygotham-talks-and-sprint-hackday/2018/2](https://discuss.python.org/t/pygotham-talks-and-sprint-hackday/2018/2){.https} if you\'re coming

**Things we are working on**:

Twine, pip, Warehouse; review some open pull requests, triage bugs to find ones we can close as no longer reproducible, and explain stuff to each other.

(If you have never contributed to Python packaging/distribution tools before, and you want to start, this is probably not the best event for you. Instead, look for [an NYC Python project night in October](https://www.meetup.com/nycpython/events/){.https} about packaging. Or, speak up [on Discourse](https://discuss.python.org/t/pygotham-talks-and-sprint-hackday/2018/2){.https} and we\'ll set up a more introductory event in the future.)

Notes from the event:

Tutorials/resources

1.  If you don\'t know git: [https://swcarpentry.github.io/git-novice/](https://swcarpentry.github.io/git-novice/){.https}

2.  If you have never packaged a Python project before: [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/){.https}

3.  If you want to understand the internals of PyPI & pip: [https://warehouse.readthedocs.io/application/](https://warehouse.readthedocs.io/application/){.https} & [https://pip.pypa.io/en/latest/development/architecture/](https://pip.pypa.io/en/latest/development/architecture/){.https}

4.  [https://www.pypa.io/en/latest/presentations/](https://www.pypa.io/en/latest/presentations/){.https}

5.  [https://nsls-ii.github.io/scientific-python-cookiecutter/preliminaries.html](https://nsls-ii.github.io/scientific-python-cookiecutter/preliminaries.html){.https}

Ways to contribute:

Pair up with someone to work on these!

- [https://github.com/pypa/auditwheel/issues/108](https://github.com/pypa/auditwheel/issues/108){.https} Auditwheel should warn on invalid versions, e.g. `dev`{.backtick}

- in progress [https://github.com/pypa/warehouse/issues/6722](https://github.com/pypa/warehouse/issues/6722){.https} Move \"show password\" checkbox on login form

- in progress [https://github.com/pypa/warehouse/issues/6691](https://github.com/pypa/warehouse/issues/6691){.https} Typo \"Top Storage users\" in Stats page

- [https://github.com/pypa/warehouse/issues/6552](https://github.com/pypa/warehouse/issues/6552){.https} Project description: rendering of \<pre\> in lists ugly

- DONE [https://github.com/conda-forge/conda-forge.github.io/issues/884](https://github.com/conda-forge/conda-forge.github.io/issues/884){.https} Minor typo: \"relict\" in documentation

- DONE [https://github.com/conda-forge/conda-forge.github.io/issues/885](https://github.com/conda-forge/conda-forge.github.io/issues/885){.https} Minor style issue: capitalizing \"Anaconda Cloud\" in documentation

- DONE [https://github.com/conda-forge/conda-forge.github.io/issues/886](https://github.com/conda-forge/conda-forge.github.io/issues/886){.https} Minor style issue: capitalizing OS names in documentation

- DONE [https://github.com/pypa/twine/issues/500](https://github.com/pypa/twine/issues/500){.https} Minor typo in docs: \"distributions\" should be \"distribution\'s\"

- DONE [https://github.com/pypa/twine/issues/501](https://github.com/pypa/twine/issues/501){.https} Update copyright year to 2019

- [https://github.com/pypa/virtualenv/issues/1193](https://github.com/pypa/virtualenv/issues/1193){.https} Creating virtualenvs from a virtualenv always yells at me

- DONE [https://github.com/pypa/warehouse/pull/6747](https://github.com/pypa/warehouse/pull/6747){.https} Make translations actually work

- [https://github.com/pypa/warehouse/issues/6451](https://github.com/pypa/warehouse/issues/6451){.https} Retaining audit log events after project/user deletion \-- this is not a good first issue for someone to try

- [https://github.com/pypa/warehouse/issues/6407](https://github.com/pypa/warehouse/issues/6407){.https} Endpoint for testing API token validity \-- this is not a good first issue for someone to try

CondaForge links for packages

- [https://conda-forge.org/](https://conda-forge.org/){.https}

- [https://github.com/pulls?utf8=%E2%9C%93&q=archived%3Afalse+org%3Aconda-forge+is%3Aopen+label%3A%22Hacktoberfest%22+](https://github.com/pulls?utf8=%E2%9C%93&q=archived%3Afalse+org%3Aconda-forge+is%3Aopen+label%3A%22Hacktoberfest%22+){.https}

- [https://github.com/regro/cf-scripts/issues?q=is%3Aissue+is%3Aopen+label%3AHacktoberfest](https://github.com/regro/cf-scripts/issues?q=is%3Aissue+is%3Aopen+label%3AHacktoberfest){.https}

Things we\'re sprinting with:

- Add your package \-- help grow the ecosystem (depends how painful your package is!)
- Make the docs better (easy-ish)
- Make adhoc-builds more easy using kubernetes (advanced)

link to slide re Warehouse: [https://docs.google.com/presentation/d/1OV_LjtPxeO5NXxrvPuGYWxztoQWksh58gX2okhObRZA/edit?usp=sharing](https://docs.google.com/presentation/d/1OV_LjtPxeO5NXxrvPuGYWxztoQWksh58gX2okhObRZA/edit?usp=sharing){.https}

link to in-toto slides: [http://bit.ly/30FXC4N](http://bit.ly/30FXC4N){.http}

### June 2019 NYC sprint day {#June_2019_NYC_sprint_day}

**Dates**: Saturday, 9 June 2019

**Times**: 10am-4pm

**Location:** a coworking lounge in New York City; remote folks can [join us via IRC](https://webchat.freenode.net/?channels=%23pypa-dev){.https}

**Attending**:

- Sumana Harihareswara, Warehouse project manager (coordinator)
- \[a few other contributors\]

**Things we are working on**:

Twine, pip, Warehouse; review some open pull requests, triage bugs to find ones we can close as no longer reproducible, and explain stuff to each other.

(If you have never contributed to Python packaging/distribution tools before, and you want to start, this is probably not the best event for you; let me know, and I\'ll set up a more introductory event in the future.)

### PyCon North America 2019 {#PyCon_North_America_2019}

### Sprint {#Sprint}

**Dates**: [May 6-9, 2019, at PyCon North America in Cleveland, Ohio, USA](https://us.pycon.org/2019/community/sprints/){.https}

**Times**: generally 9am-5pm all days

**Room:** 26C Monday-Wednesday \-- room 19 on Thursday

**Attending**:

- Sumana Harihareswara, Warehouse project manager (coordinator) (some days - specifics TBA)
- Pradyun Gedam
- Dustin Ingram
- Cooper Lees
- Jason R. Coombs
- Conda, conda-forge, and Anaconda team
- You?

**Things we are working on**:

See [http://bit.ly/pypa2019 (Google Doc)](https://docs.google.com/document/d/1Wz2-ECkicJgAmQDxMFivWmU2ZunKvPZ2UfQ59zDGj7g/edit){.https} for a live updated list!

- Updating [the PyPA roadmap](https://www.pypa.io/en/latest/roadmap/){.https} & planning for the next 6-12 months of Warehouse, `pip`{.backtick}, `pipenv`{.backtick}, and `twine`{.backtick} work

  - Articulating which tools cover which jobs in the toolchain, checking for overlaps and gaps in scope

  - Discussing which practices/functionality should be actively discouraged or deprecated in `setuptools`{.backtick}

  - Sorting out what should be in `setup()`{.backtick} vs `setup.cfg`{.backtick} vs `pyproject.toml`{.backtick}

  - Creating a [package index upload API spec](https://github.com/pypa/packaging-problems/issues/128){.https}

- User testing
  - Walk through the [package distributing tutorial](https://packaging.python.org/tutorials/distributing-packages/){.https} and find bugs in our documentation

- API and backend work on Warehouse
  - [Determining the new Warehouse API URL structure](https://github.com/pypa/warehouse/issues/284){.https} (and planning to replace the XML-RPC endpoint; Donald Stufft\'s focus)

  - [Bandersnatch](https://bitbucket.org/pypa/bandersnatch/){.https} mirroring for PyPI

  - Adding [API keys](https://github.com/pypa/warehouse/issues/994){.https} and [two-factor auth](https://github.com/pypa/warehouse/issues/996){.https} (Luke Sneeringer\'s project) to Warehouse

  - Adding a [\"mark this release as deprecated\" feature](https://github.com/pypa/warehouse/issues/3709){.https} to Warehouse

  - Adding [two-phase release upload](https://github.com/pypa/warehouse/issues/726){.https} to Warehouse

- Making a [\"bus factor\" promo page](https://github.com/pypa/warehouse/issues/3121){.https}

- Triaging [Packaging Problems issues](https://github.com/pypa/packaging-problems/issues/){.https}

- Talking with Anaconda engineers about conda/pip compatibility, pip resolver reuse, etc.

### PyPA October 2018 sprint at Bloomberg {#PyPA_October_2018_sprint_at_Bloomberg}

**Dates**: Sponsored and hosted by [Bloomberg](https://www.techatbloomberg.com/){.https}, October 27-28, 2018, simultaneously in London and New York City. We hope mentors can arrive Thursday night 25 Oct, do prep, setup, and dinner on Friday, then participate Sat-Sun, then leave Sunday evening or Monday.

Attending: free and open to the public, please RSVP for the relevant events:

- NYC, 10/27: [https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/new-york-city/58377](https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/new-york-city/58377){.https}

- NYC, 10/28: [https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/new-york-city/58382](https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/new-york-city/58382){.https}

- LON, 10/27: [https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/london/58402](https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/london/58402){.https}

- LON, 10/28: [https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/london/58403](https://generalassemb.ly/education/bloomberg-open-source-weekend-pypa/london/58403){.https}

Bloomberg will host this, pay for a maintainers\'/mentors\' dinner the night before, provide clusters of cloud virtual machines for the attendees to use, and book and pay for some contributors\' lodging and travel.

If you live in North America or Europe and would need assistance to attend this as a mentor, email **[di@python.org](mailto:di@python.org){.mailto}** .

**TO DO NOW**: If you live outside of the US or UK and would need an invitation letter to get a visa to travel to one of these sprints, please write to Kevin P. Fleming at Bloomberg, kpfleming AT bloomberg DOT net, and he\'ll start setting you up.

**Purpose**: advance Python packaging/distro tools, teach new contributors (including many Bloomberg employees), and yeah, if you want to get to know Bloomberg for career reasons, that too. ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"} See [the Tech At Bloomberg site](https://www.techatbloomberg.com/events/){.https}.

Thanks to Bloomberg folks Mario Corchero and Henry Kleynhans in London and Kevin P. Fleming in New York City for coordinating this, and thanks especially to Mario and to Paul Ganssle for suggesting it!

**Things we could work on**:

- PyPA roadmap
- next version of virtualenv
- More

### PyCon North America 2018 {#PyCon_North_America_2018}

### Sprint {#Sprint-1}

**Dates**: [May 14-17, 2018, at PyCon North America in Cleveland, Ohio, USA](https://us.pycon.org/2018/community/sprints/){.https}

**Times**: generally 9am-5pm all days

**Room:** [26B]{.strike} moved to Room 20

**Attending**:

- Sumana Harihareswara, Twine and Warehouse maintainer (coordinator) (all 4 days)

- Dustin Ingram, Warehouse maintainer (all 4 days)

- Ernest W. Durbin III, Warehouse maintainer & Infrastructure Working Group chair (partially attending)

- Nick Coghlan, core Python developer (came for first/second day)

- Donald Stufft, `pip`{.backtick} maintainer (came for first day)

- Luke Sneeringer, Warehouse contributor ([hoping to come]{.strike} came first day)

- Thea Flowers, Python Packaging User Guide and `readme_renderer`{.backtick} maintainer (came for first day)

- Cooper Lees, `bandersnatch`{.backtick} maintainer (all 4 days)

- Paul Ganssle, library maintainer (came for first 2 days)

- Jason R. Coombs, `setuptools`{.backtick} maintainer (all 4 days)

- Laura Hampton, Warehouse and Twine contributor

- Dan Ryan/techalchemy, Pipenv maintainer (came for first day)

- Bryan Clark, product manager for GitHub (first 2 days)

- Kenneth Reitz, BDFL of Pipenv (first day)

- Michael Sarahan, conda-build maintainer (all 4 days)

- Kale Franz, conda maintainer (all 4 days)

- You?

**Things we are working on**:

- Updating [the PyPA roadmap](https://www.pypa.io/en/latest/roadmap/){.https} & planning for the next 6-12 months of Warehouse, `pip`{.backtick}, `pipenv`{.backtick}, and `twine`{.backtick} work

  - Articulating which tools cover which jobs in the toolchain, checking for overlaps and gaps in scope

  - Discussing which practices/functionality should be actively discouraged or deprecated in `setuptools`{.backtick}

  - Sorting out what should be in `setup()`{.backtick} vs `setup.cfg`{.backtick} vs `pyproject.toml`{.backtick}

  - Creating a [package index upload API spec](https://github.com/pypa/packaging-problems/issues/128){.https}

- User testing
  - Walk through the [package distributing tutorial](https://packaging.python.org/tutorials/distributing-packages/){.https} and find bugs in our documentation

- API and backend work on Warehouse
  - [Determining the new Warehouse API URL structure](https://github.com/pypa/warehouse/issues/284){.https} (and planning to replace the XML-RPC endpoint; Donald Stufft\'s focus)

  - [Bandersnatch](https://bitbucket.org/pypa/bandersnatch/){.https} mirroring for PyPI

  - Adding [API keys](https://github.com/pypa/warehouse/issues/994){.https} and [two-factor auth](https://github.com/pypa/warehouse/issues/996){.https} (Luke Sneeringer\'s project) to Warehouse

  - Adding a [\"mark this release as deprecated\" feature](https://github.com/pypa/warehouse/issues/3709){.https} to Warehouse

  - Adding [two-phase release upload](https://github.com/pypa/warehouse/issues/726){.https} to Warehouse

- Making a [\"bus factor\" promo page](https://github.com/pypa/warehouse/issues/3121){.https}

- Discussing a new Twine API for use by `zest.releaser`{.backtick}, `flit`{.backtick}, etc.

- Triaging [Packaging Problems issues](https://github.com/pypa/packaging-problems/issues/){.https}

- Talking with GitHub product manager Bryan Clark about how GitHub could support Python packagers and package users better

- Talking with Anaconda engineers about conda/pip compatibility, pip resolver reuse, etc.

### EuroPython 2018 {#EuroPython_2018}

**Dates**: [EuroPython in Edinburgh, Scotland, July 28 & 29, 2018](https://ep2018.europython.eu/){.https}

**Attending**:

- Nicole Harris, Warehouse maintainer (coordinator)
- Pooja Gadige, Warehouse contributor (hoping/planning to come)
- You?

**Things we could work on**:

- User testing

- [Bus factor promo page](https://github.com/pypa/warehouse/issues/3121){.https}

- Frontend improvements

### April 2018: NYC Python/PyLadies Sprint Night {#April_2018:_NYC_Python.2FPyLadies_Sprint_Night}

[Thursday, April 26, New York City, NY](https://www.python.org/events/python-user-group/700/){.https} \-- [6:00 PM to 8:30 PM, at Microsoft Technology Center](https://www.meetup.com/nycpython/events/249722192){.https}

Attending:

- Laura Hampton (coordinator)
- Sumana Harihareswara
- You? People of all genders are welcome.

Things we could work on:

- User testing

- [Good first issues](https://github.com/pypa/warehouse/issues?q=is:issue+is:open+label:%22good+first+issue%22){.https}

- [Assessing](https://github.com/pypa/warehouse/issues/3252){.https} trending projects feed and libraries.io option

### Packaging BoF/Open Space at PyCon 2018 {#Packaging_BoF.2FOpen_Space_at_PyCon_2018}

**Date:** We held an [open space](https://us.pycon.org/2018/events/open-spaces/){.https}/Birds of a Feather session, a conversation on packaging.

**Attending**:

- Ian Stapledon Cordasco, Twine maintainer

- Peter Wang, founder/CTO of Anaconda

- *practically everyone listed as attending the sprint \-- except Jason R. Coombs could not make it*

**Topics**:

- *See [this Etherpad](https://pad.sfconservancy.org/p/gDHkDUtfi5){.https}*

### Pipenv BoF/Open Space {#Pipenv_BoF.2FOpen_Space}

**Date**: May 13, an [open space](https://us.pycon.org/2018/events/open-spaces/){.https}/Birds of a Feather session specifically on Pipenv.

**Attending**:

- Kenneth Reitz, BDFL of Pipenv (coordinator)

**Topics**:

- Pipenv
::::
