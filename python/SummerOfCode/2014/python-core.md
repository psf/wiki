# SummerOfCode/2014/python-core

::: {#content dir="ltr" lang="en"}
# Project ideas for Python Core in GSoC 2014 {#Project_ideas_for_Python_Core_in_GSoC_2014}

Students interested in \"Python Core\" projects will be working on the [CPython](http://en.wikipedia.org/wiki/CPython){.http} Python language interpreter and related core packages.

## Getting in touch with mentors {#Getting_in_touch_with_mentors}

There are two important lists for students interested in Core Python development:

- [https://mail.python.org/mailman/listinfo/python-dev](https://mail.python.org/mailman/listinfo/python-dev){.https} is the main development list for python.

- [https://mail.python.org/mailman/listinfo/core-mentorship](https://mail.python.org/mailman/listinfo/core-mentorship){.https} is the introductory list for people just getting started in Python development, and as such is usually the place for new students to start communicating with mentors and getting their environment set up.

Students should subscribe to and read both lists, but should use the core-mentorship list to post questions and get started.

## Getting Started {#Getting_Started}

In addition to the mailing lists, students interested in contributing to core Python should take a look at the [Developers guide](http://docs.python.org/devguide/){.http}

------------------------------------------------------------------------

## Projects {#Projects}

### Email {#Email}

#### Possible email projects {#Possible_email_projects}

- 1.1 Add header-type-specific parsing for additional header types (Received, Message-Id, References) to the new 3.3 provisional policies.

- 1.2 Work on support for [RFC 6532](http://tools.ietf.org/html/rfc6532){.http} in the email package.

- 1.3 Work on support for [RFC 6531](http://tools.ietf.org/html/rfc6531){.http} in smtplib and/or smtpd.

#### Email project mentors {#Email_project_mentors}

- R. David Murray
- Antoine Pitrou

### IDLE {#IDLE}

Don\'t spend your summer IDLE around the swimming pool spend your summer working on IDLE and make a difference. IDLE is Python\'s Integrated Development Environment (IDE) that is shipped with each Python release. Since IDLE ships with Python it is often the first IDE a new Python programmer uses. We want to make IDLE an awesome experience especially for people that are learning Python.

#### Possible IDLE projects {#Possible_IDLE_projects}

- A unit test framework for Idle was created in the spring and summer of 2013. Some test modules created by 2013 GSOC students were created within the framework and are now part of Python\'s daily tests on multiple systems and versions. There is still much more to add. One priority project would be to add tests for existing tracker bug and enhancement issues. Another would be a non-buildbot human test to sequentially display every window and dialog to check that they do display without raising an exception and that they look \'correct\'.

- Create an Idle extension that would integrate 3rd party code checkers with Editor Windows. See message 195711 of [http://bugs.python.org/issue18704](http://bugs.python.org/issue18704){.http}.

- Add an option to connect to user subprocesses with subprocess.Popen and pipes. If this works well enough, it could replace the current connection by sockets, which sometimes fails. [http://bugs.python.org/issue18823](http://bugs.python.org/issue18823){.http}

- Make Idle more completely a GUI application by using popup windows rather than a console to report errors. The latter is a problem when there is no visible console, as is normal on Windows.

- Optionally add line numbers to code in an edit window. The underlying tk Text widget apparently keeps track of line numbers, but Idle can only control its behavior through the interface made available. So what is possible might be less than what we would like.

- In the shell window, separate prompts from input or output. Or otherwise make it possible to use 4 space indents, at least after the first.

- Look at other Idle enhancement issues on the tracker. However, inquire first since not all ideas on the tracker will ever be accepted.

#### IDLE project mentors {#IDLE_project_mentors}

- Terry Reedy
- Tal Einat
:::
