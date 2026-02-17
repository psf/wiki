# JythonFaq/ExtendingJython

:::: {#content dir="ltr" lang="en"}
# Extending Jython {#Extending_Jython}

[JythonFaq](JythonFaq)

::: table-of-contents
Contents

1.  [Extending Jython](#Extending_Jython)
    1.  [How do I create Java classes that emulate Jython Dictionaries and Sequences?](#How_do_I_create_Java_classes_that_emulate_Jython_Dictionaries_and_Sequences.3F)
    2.  [How do I emulate Jython object attribute access with a Java class?](#How_do_I_emulate_Jython_object_attribute_access_with_a_Java_class.3F)
    3.  [How do I support \*args and \*\*kw in Java methods?](#How_do_I_support_.2Aargs_and_.2A.2Akw_in_Java_methods.3F)
:::

------------------------------------------------------------------------

## How do I create Java classes that emulate Jython Dictionaries and Sequences? {#How_do_I_create_Java_classes_that_emulate_Jython_Dictionaries_and_Sequences.3F}

In order to emulate Dictionaries and Sequences, first your Java class must \"extend\" the org.python.core.[PyObject](./PyObject.html){.nonexistent} class. The following methods can then be defined on your class in order to emulate these basic Jython types:

- :::: {.highlight .java}
  ::: {.codearea dir="ltr" lang="en"}
  ``` {#CA-e183680ca932ee42622ab07e506c082b34e5df7a dir="ltr" lang="en"}
     1     public PyObject __finditem__(PyObject key);
     2 
     3     public void __setitem__(PyObject key, PyObject value);
     4 
     5     public void __delitem__(PyObject key);
  ```
  :::
  ::::

Additionally, you might want to throw the org.python.core.Py.[KeyError](./KeyError.html){.nonexistent} object if you have any exceptions (Note, you need not declare the Java method as throwing anything.)

------------------------------------------------------------------------

## How do I emulate Jython object attribute access with a Java class? {#How_do_I_emulate_Jython_object_attribute_access_with_a_Java_class.3F}

You can develop your own Java class that emulates Jython objects by first extending the org.python.core.[PyObject](./PyObject.html){.nonexistent} class. Then, implement the following methods on your Java class:

- :::: {.highlight .java}
  ::: {.codearea dir="ltr" lang="en"}
  ``` {#CA-16ff32273a6f8f78548ab893813d7a11c73e04c9 dir="ltr" lang="en"}
     1     public PyObject __findattr__(String name);
     2 
     3     public void __setattr__(String name, PyObject value);
     4 
     5     public void __delattr__(String name);
  ```
  :::
  ::::

You may also want to raise exceptions using the org.python.core.Py.[AttributeError](./AttributeError.html){.nonexistent} error class. (Note, you do not need to declare that the method throws this class.)

As in CPython, \"a = foo.bar\" calls the [findattr]{.u} method on foo, \"foo.bar = \'baz\'\" calls the [setattr]{.u} method on foo, and \"delattr(foo, \'bar\')\" calls the [delattr]{.u} method on foo.

If you plan on storing functions as attributes of your Java object (so that you could say \"foo.bar(\'baz\', \'fizzle\')\", be forwarned that Jython \*may or may not\* call the [findattr]{.u} method to find the function object depending on the number/types of parameters. You should, additionally, implement the following methods:

- :::: {.highlight .java}
  ::: {.codearea dir="ltr" lang="en"}
  ``` {#CA-6fc2821d2a7118d6eb4d634bbcd411c3a551b02a dir="ltr" lang="en"}
     1     public PyObject invoke(String name);
     2 
     3     public PyObject invoke(String name, PyObject arg1);
     4 
     5     public PyObject invoke(String name, PyObject arg1, PyObject arg2);
     6 
     7     public PyObject invoke(String name, PyObject[] args);
     8 
     9     public PyObject invoke(String name, PyObject[] args, String[] keywords);
  ```
  :::
  ::::

------------------------------------------------------------------------

## How do I support \*args and \*\*kw in Java methods? {#How_do_I_support_.2Aargs_and_.2A.2Akw_in_Java_methods.3F}

*(thanks to Finn Bock for the information)*

In Jython (note, this does not work in JPython), you can support keyword arguments on Java methods by defining the method like so (the parameters are the important point):

- :::: {.highlight .java}
  ::: {.codearea dir="ltr" lang="en"}
  ``` {#CA-4872e22d075145c09e9a60be5ca4e3c7577c7014 dir="ltr" lang="en"}
     1     public PyObject foo(PyObject[] args, String[] keywords);
  ```
  :::
  ::::

The keywords array contains all of the keywords for the keyword-defined arguments. For example, if you called foo with:

- :::: {.highlight .python}
  ::: {.codearea dir="ltr" lang="en"}
  ``` {#CA-eec6cefcbe55661bf7939037b900474c11475cf7 dir="ltr" lang="en"}
     1     foo(1,2,3,four=4,five=5)
  ```
  :::
  ::::

args would be: \[1, 2, 3, 4, 5\] and keywords would be: \[\'four\', \'five\'\] (an array of 2 elements.)

Additionally, you can use the experimental argument parser org.python.core.[ArgParser](./ArgParser.html){.nonexistent} to deal mapping these two arrays. Consult the Javadocs (or source) for further details on org.python.core.[ArgParser](./ArgParser.html){.nonexistent}.

------------------------------------------------------------------------
::::
