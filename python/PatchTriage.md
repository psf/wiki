# PatchTriage

::: {#content dir="ltr" lang="en"}
This page records triage of patches made by the community. Please don\'t add any rationale for your assessment here, but instead record it in the patch itself. For each line, put your name or initials next to the assessment, so that it\'s easy to see who added what entry.

(hint: you can link to items with `SF:Number`{.backtick}.)

# Clear Accept {#Clear_Accept}

List of patches that should be accepted.

- [1520879](http://bugs.python.org/issue1520879 "SF"){.interwiki} (Han-Wen Nienhuys)

- [1669481](http://bugs.python.org/issue1669481 "SF"){.interwiki} (Jason Orendorff)

- [1704621](http://bugs.python.org/issue1704621 "SF"){.interwiki} (Jason Orendorff)

- [1692664](http://bugs.python.org/issue1692664 "SF"){.interwiki} (Jason Orendorff)

- [1676135](http://bugs.python.org/issue1676135 "SF"){.interwiki} (Jason Orendorff)

# Clear Reject {#Clear_Reject}

List of patches that should be rejected.

- [1608267](http://bugs.python.org/issue1608267 "SF"){.interwiki} (Han-Wen Nienhuys)

- [1339673](http://bugs.python.org/issue1339673 "SF"){.interwiki} (Han-Wen Nienhuys)

- [1528074](http://bugs.python.org/issue1528074 "SF"){.interwiki} (JimJJewett)

- [1678345](http://bugs.python.org/issue1678345 "SF"){.interwiki} (JimJJewett)

- [1704547](http://bugs.python.org/issue1704547 "SF"){.interwiki} (Jason Orendorff)

- [1678345](http://bugs.python.org/issue1678345 "SF"){.interwiki} (Jason Orendorff)

- [1673007](http://bugs.python.org/issue1673007 "SF"){.interwiki} (Jason Orendorff)

- [1665292](http://bugs.python.org/issue1665292 "SF"){.interwiki} (Jason Orendorff)

- [1652328](http://bugs.python.org/issue1652328 "SF"){.interwiki} (Jason Orendorff)

# Needs PEP {#Needs_PEP}

List of patches that cannot go in without a PEP being approved first

# Conflict {#Conflict}

List of patches with conflicting reviews (some speaking for, some against)

- [1678339](http://bugs.python.org/issue1678339 "SF"){.interwiki} JimJJewett recommends rejection, because the \"failing\" behavior is intentional. I put it under conflict because the test is arguably consistent with the docs, so Georg (after Paul Hankin\'s review) added it to outstanding bugs. (I agree that there is a bug, but feel the bug is in the doco.)

# Being Worked {#Being_Worked}

List of patches which are not ready yet, but may become so \-- the person who put them here should move them to another status if they go more than a month or so without progress. And no, this doesn\'t really keep them out of sight for committers yet, but it may eventually move them the never-touched-again patches to reject.
:::
