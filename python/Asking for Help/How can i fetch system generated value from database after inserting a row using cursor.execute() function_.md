# Asking for Help/How can i fetch system generated value from database after inserting a row using cursor.execute() function?

::: {#content dir="ltr" lang="en"}
# Asking for Help: How can I fetch a system-generated value from a database after inserting a row using the cursor.execute() function? {#Asking_for_Help:_How_can_I_fetch_a_system-generated_value_from_a_database_after_inserting_a_row_using_the_cursor.execute.28.29_function.3F}

The API is described in [PEP 249](http://www.python.org/dev/peps/pep-249 "PEP"){.interwiki}. Unfortunately, the return value of `cursor.execute`{.backtick} is not defined in the specification, however, but it may be the case that your database adapter may provide a meaningful return value. When issuing `insert`{.backtick} statements in SQL, sometimes the number of rows inserted may be returned (which is probably what you\'re referring to), but even in systems like PostgreSQL where this can be observed, there can be situations where a result of 0 is given instead of the actual number of inserted rows. I seem to recall that table partitions, for instance, don\'t (or didn\'t) support non-zero results from `insert`{.backtick} when statements were issued in the SQL client. \-- [PaulBoddie](PaulBoddie) 2012-05-31 12:03:22

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
:::
