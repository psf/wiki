# Email SIG

::: {#content dir="ltr" lang="en"}
# The email package SIG {#The_email_package_SIG}

The [email package](http://www.python.org/doc/current/library/email.html){.http} is a large, complicated package that comes with Python, and which supports parsing, manipulating and generating email messages in RFC compliant formats. Its development is ongoing. Current focus is on version 6.0, with a target release in Python 3.2 (back ported to Python 2.7), and with standalone packages available to older versions of Python.

The information and pages below are used to record decisions and status related to the email package\'s development. Discussions should be conducted on the [Email SIG mailing list](http://mail.python.org/mailman/listinfo/email-sig){.http} [(archive)](http://mail.python.org/pipermail/email-sig/){.http}.

## Goals {#Goals}

## Schedule and Status {#Schedule_and_Status}

Ideally, email 6.0 would be ready for Python 3.2 (release scheduled for 2010-12-11). In order to be ready for Python 3.2, we would need to be feature complete and field tested by the first scheduled beta (2010-09-18). If we can\'t be ready by then, we\'ll target Python 3.3 which will be 18-24 months after Python 3.2. In all cases, we\'ll provide standalone packages via the [(cheeseshop)](http://pypi.python.org/pypi){.http} for older Python versions, including Python 2.x at least back to Python 2.6.

R. David Murray applied for a grant from the PSF to work on implementing the proposed design. The PSF provided seed funding and offered support for further fundraising. (See Initiatives and Proposals below.) The initial work is ongoing, additional fundraising is not really in gear yet.

## Resources {#Resources}

- [Relevant RFCs](./Email(20)SIG(2f)RelevantRFCs.html)

- [Glossary](./Email(20)SIG(2f)Glossary.html)

- [Open Issue Summary](http://www.bitdance.com/test/projects/email6/issues/){.http}

## Initiatives and Proposals {#Initiatives_and_Proposals}

- [Design Overview Proposal](./Email(20)SIG(2f)DesignOverviewProposal.html)

- [Use Cases](./Email(20)SIG(2f)UseCases.html)

- [stdlib clients](./Email(20)SIG(2f)stdlibCLients.html)

- [More Detailed Design Thoughts](./Email(20)SIG(2f)DesignThoughts.html)

- [PSF Grant Proposal](http://www.bitdance.com/test/projects/email6/psfproposal/){.http}

- [Notice of seed funding approval](http://www.python.org/psf/records/board/minutes/2009-12-14/#funding-for-python-3-email-module){.http}

## Code {#Code}

We\'ve elected to host the code development in BZR on launchpad.

- [Launchpad Repository](https://launchpad.net/python-email6){.https}

- [Docs snapshot](http://www.bitdance.com/test/projects/email6/doc/email/){.http}
:::
