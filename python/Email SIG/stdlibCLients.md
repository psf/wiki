# Email SIG/stdlibCLients

::: {#content dir="ltr" lang="en"}
# stdlib Clients

Other parts of the stdlib rely on the email package for various services. Right now this is just a list of import dependencies; this should be expanded into a brief description of the stdlib use cases so we can make sure we continue to support them properly.

  -----------------------------------------------------------------------
  Package                Email imports
  ---------------------- ------------------------------------------------
  http/client.py         email.parser, email.message

  http/server.py         email.parser, email.message

  urllib/request         email, email.utils (also mimetypes)

  smtplib                email.utils

  cgi                    email.parser

  pydoc                  email.message

  mailbox                email, email.message, email.generator

  distutils/dist.py      email.message_from_file
  -----------------------------------------------------------------------

There are also dependencies in the test suites:

  -----------------------------------------------------------------------
  Test                       Email imports
  -------------------------- --------------------------------------------
  urllib2_localnet           email

  smtplib                    email.utils

  test_http_cookiejar        email

  test_urllibnet             email.message

  test_mailbox               email, email.message

  test_zipfile               email

  test_urllib2               email, email.utils
  -----------------------------------------------------------------------
:::
