# TestFailures

::: {#content dir="ltr" lang="en"}
# Failing tests on the 2.3 branch {#Failing_tests_on_the_2.3_branch}

## Ones with reasons {#Ones_with_reasons}

test_binascii: exceptions are strings, not classes, so issubclass() raises an exception; a2b_qp not implemented; a2b_uu has a logic error that makes it fail on the UUencoding of an empty string.

test_StringIO: root cause: *.join(\[unicode, str\]) returns str, should be unicode*

test_dumbdbm: with very large strings, the value retrieved is incorrect.

test_format: \'%d\' % \'1\' works, should raise a [TypeError](./TypeError.html){.nonexistent}.

test_fileinput: patch in SF.
:::
