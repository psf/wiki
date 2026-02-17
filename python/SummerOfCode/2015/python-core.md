# SummerOfCode/2015/python-core

::: {#content dir="ltr" lang="en"}
# CPython {#CPython}

CPython is the default, most widely used implementation of the Python programming language. It is mostly written in C, most of the modules are written in Python itself. In case you want to make the changes which will be used by all the Python programmers worldwide, this is the project to work for.

## Contacting CPython developers {#Contacting_CPython_developers}

One can contact the core developers over IRC or using mailing lists. #python-dev (on freenode) is the channel for core developers, [the core mentorship mailing list](https://mail.python.org/mailman/listinfo/core-mentorship){.https} is the place to an email discussion. Remember that the developers are may not be in your timezone, so it might take time to get a reply from anyone.

## Getting Started {#Getting_Started}

The best place to get started is the [devguide](https://docs.python.org/devguide/index.html){.https}. You will find all the instructions required to build your own CPython. Before contacting the mentors, it is better you start solving few [bugs](http://bugs.python.org/){.http} first.

# Ideas {#Ideas}

We\'re still waiting to find out which mentors are available for Core Python/CPython projects. In the meantime, you can discuss ideas on [the core mentorship mailing list](https://mail.python.org/mailman/listinfo/core-mentorship){.https}.

## 1. bugs.python.org improvements {#A1._bugs.python.org_improvements}

- **Project description**: The goal of this project is to improve the [bug tracker used by CPython](https://bugs.python.org/){.https}.

- **Skills**: Python, HTML/CSS/JS, Roundup, DVCS.

- **Difficulty level**: Intermediate.

- **Related Readings/Links**: The details are still being discussed on the [core-workflow ML](https://mail.python.org/pipermail/core-workflow/2015-March/thread.html#132){.https}.

- **Potential mentors**: Ezio Melotti.

### Project Details {#Project_Details}

There are several different tasks that can be tackled.

- Some features previously discussed on this ML and summarized at [https://wiki.python.org/moin/TrackerDevelopmentPlanning](https://wiki.python.org/moin/TrackerDevelopmentPlanning){.https}

- Some other miscellaneous features listed at [https://wiki.python.org/moin/DesiredTrackerFeatures](https://wiki.python.org/moin/DesiredTrackerFeatures){.https}

- Better integration with Rietveld (e.g. add messages to roundup when someone posts a review)

- Smarter branch detection in patches (sometimes patches don\'t get the review link)

- Patch analysis (information such as affected files could be extracted from the files and used by Roundup, check pep8 compliance)

- Integration with [BitBucket](./BitBucket.html){.nonexistent} (and possibly [GitHub](./GitHub.html){.nonexistent}) pull requests (might use [https://pypi.python.org/pypi/vcs](https://pypi.python.org/pypi/vcs){.https})

- Investigate Kallithea/Phabricator integration

- Mercurial extension to simplify tracker interaction (e.g. upload patches automatically, might be based on [https://bitbucket.org/ncoghlan/cpydev/src/default/cpyhg.py?at=default](https://bitbucket.org/ncoghlan/cpydev/src/default/cpyhg.py?at=default){.https} - might be similar to [https://github.com/openstack-infra/git-review](https://github.com/openstack-infra/git-review){.https})

- Reviewing and applying patches submitted on the meta-tracker

- Fix other issues listed on the meta-tracker

Students can select a substantial subset of these tasks for their proposal. The actual tasks and the order can be discussed with the mentor.

## 2. Add a REST API to Roundup {#A2._Add_a_REST_API_to_Roundup}

- **Project description**: The goal of this project is to add a REST API to Roundup

- **Skills**: Python, basic HTML/JS skills.

- **Difficulty level**: Intermediate.

- **Related Readings/Links**: [http://issues.roundup-tracker.org/issue2550734](http://issues.roundup-tracker.org/issue2550734){.http} [http://sourceforge.net/p/roundup/mailman/message/33589328/](http://sourceforge.net/p/roundup/mailman/message/33589328/){.http}

- **Potential mentors**: Hieu Nguyen.

### Project Details {#Project_Details-1}

For this project the student will design and develop a REST API for bugs.python.org. Even though this project is initially aimed to bugs.python.org, the plan is to eventually contribute the code upstream. This is what the student is expect to do during the project:

1.  design the REST API (see also [https://mail.python.org/pipermail/core-workflow/2015-March/000142.html](https://mail.python.org/pipermail/core-workflow/2015-March/000142.html){.https})

2.  implement it in our Roundup clone ([https://hg.python.org/tracker/roundup/](https://hg.python.org/tracker/roundup/){.https})

3.  develop some basic tool that uses the API (improved stats page, [dashboard](https://dashboard.djangoproject.com/){.https})

4.  possibly tweak the API if there are problems

5.  when stable, contribute it upstream (could happen after GSoC)

## 3. Use more unittest features in regrtest {#A3._Use_more_unittest_features_in_regrtest}

- **Project description**: The goal of this project is to improve the CPython test suite by using more unittest features.

- **Skills**: Python, unittest.

- **Difficulty level**: Intermediate.

- **Related Readings/Links**: [http://bugs.python.org/issue10967](http://bugs.python.org/issue10967){.http}, [https://hg.python.org/cpython/file/default/Lib/test/regrtest.py](https://hg.python.org/cpython/file/default/Lib/test/regrtest.py){.https}

- **Potential mentors**: No mentor (you can put together a proposal and ask for one on [the core mentorship ML](https://mail.python.org/mailman/listinfo/core-mentorship){.https}).
:::
