# Distutils2/Sprints

::: {#content dir="ltr" lang="en"}
# Participating to a Distutils2 Sprint {#Participating_to_a_Distutils2_Sprint}

## Before: Getting Set up {#Before:_Getting_Set_up}

To get ready for a Distutils2 sprint, you need to complete these steps:

- Install **Python** 2.5, 2.6 or 2.7 (recommended). If your operating system has a package manager, use it (and also install a python2.y-devel or python2.y-dev package if it exists), otherwise follow the [instructions](http://python.org/download/){.http}.

- Install **Mercurial**. If needed, read [instructions](http://hg-scm.org/downloads/){.http} (or [Windows instructions](http://tortoisehg.bitbucket.org/download/){.http}). If you have never used it, read [Ground up Mercurial](http://hginit.com/01.html){.http} and [Setting up for a Team](http://hginit.com/02.html){.http}.

- If you don\'t have **TortoiseHg**, you need to install a [merge tool](http://mercurial.selenic.com/wiki/MergeProgram){.http}.

- Install **[unittest2](http://pypi.python.org/pypi/unittest2){.http}** and **[docutils](http://pypi.python.org/pypi/docutils){.http}**, they are needed to run the tests for Distutils2. If your package manager has them, use it; if you use virtualenv, you know how to install them; otherwise, you will need to download them from the Python Packages Index, unpack the archives and install them with the command `python setup.py install --user`. On the sprint day we will have copies of the zip/tar files on USB sticks for your convenience.

- Mercurial requires a bit of **configuration** before you can use it. You need to define a user name (in the form "Name \<email@address\>") in a [configuration file](http://mercurial.aragost.com/kick-start/en/basic/#installation-configuration){.http}. Some very useful features of Mercurial can also be enabled in the same config file; this page will be edited later with examples or we\'ll do it at the start of the sprint.

- You can now get a **clone** of the Distutils2 repository. Open a terminal or command prompt and type this: `hg clone https://bitbucket.org/mtlpython/distutils2` . When you have a changeset ready to push, just ask someone of the team to add your account to the repository's members.

A legal note: Because Distutils2 is distributed by the Python Software Foundation under the Python license, you will have to sign a **contributor agreement** to allow the PSF to redistribute your code. You can read and prepare [the agreement](http://www.python.org/psf/contrib/){.http} before the sprint, or use one of the copies we will have with us.

## During: Finding a Bug or Feature to Work on {#During:_Finding_a_Bug_or_Feature_to_Work_on}

At the beginning of the sprint we will explain quickly what Distutils2 does, how it works and how to fix bugs. These are the bugs that can be tackled by someone new to the codebase; please add your name when you choose one to avoid work duplication.

- [http://bugs.python.org/issue12944](http://bugs.python.org/issue12944){.http}

- [ [http://bugs.python.org/issue13614](http://bugs.python.org/issue13614){.http} ]{.strike} \[PP et mlhamel\]

- [http://bugs.python.org/issue13399](http://bugs.python.org/issue13399){.http} \[Patrice\]

- [http://bugs.python.org/issue13331](http://bugs.python.org/issue13331){.http} \[Denis\]

- [http://bugs.python.org/issue13400](http://bugs.python.org/issue13400){.http} (two patches needed)

- [http://bugs.python.org/issue6114](http://bugs.python.org/issue6114){.http} (Rory was interested)

- [http://bugs.python.org/issue13317](http://bugs.python.org/issue13317){.http} \[Patrice\]

- [ [http://bugs.python.org/issue10374](http://bugs.python.org/issue10374){.http} ]{.strike} \[PP\]

- [http://bugs.python.org/issue7677](http://bugs.python.org/issue7677){.http} \[Kim\]

- [http://bugs.python.org/issue1222585](http://bugs.python.org/issue1222585){.http}

- [http://bugs.python.org/issue5342](http://bugs.python.org/issue5342){.http} \[Jonathan\]

- [http://bugs.python.org/issue13400](http://bugs.python.org/issue13400){.http} \[Julien\]

- [http://bugs.python.org/issue763043](http://bugs.python.org/issue763043){.http} needs a doc patch; talk with merwok about that

- [http://bugs.python.org/issue5300](http://bugs.python.org/issue5300){.http}

- [http://bugs.python.org/issue8501](http://bugs.python.org/issue8501){.http} needs tests

- [http://bugs.python.org/issue809163](http://bugs.python.org/issue809163){.http} has a patch which needs a test and a review

- [http://bugs.python.org/issue14270](http://bugs.python.org/issue14270){.http} \[mlhamel\]

If a report does not clearly describe what the problem is or how we may fix it, just ask.

## After: Staying in Touch {#After:_Staying_in_Touch}

If your patch is not finished at the end of the sprint, or if you want to work on another thing, you can use the bug tracker or the montreal-python mailing list to ask questions and send patches. The best place is the bug tracker; it only requires creating a user account and keeps a record of the problems found and choices made during development.
:::
