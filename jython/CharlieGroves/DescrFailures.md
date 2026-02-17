# CharlieGroves/DescrFailures

::: {#content dir="ltr" lang="en"}
# Fixed {#Fixed}

- mro can\'t be modified by subtypes
  - altmro

- [http://jython.org/bugs/1603315](http://jython.org/bugs/1603315){.http} - jython doesn\'t line up with CPython\'s expected kwargs

  - kwdargs

- [http://jython.org/bugs/1603312](http://jython.org/bugs/1603312){.http} - an overflow error isn\'t raised by int subclasses for large values

  - ints

# Filed {#Filed}

- [http://jython.org/bugs/1603314](http://jython.org/bugs/1603314){.http} - [PyModule](./PyModule.html){.nonexistent} is old style class

  - pymods
  - test_dir
  - modules

- [http://jython.org/bugs/1603315](http://jython.org/bugs/1603315){.http} - jython doesn\'t line up with CPython\'s expected kwargs

  - keywords

- [http://jython.org/bugs/1506749](http://jython.org/bugs/1506749){.http} - instance dicts can\'t be set or deleted

  - setdict

- [http://jython.org/bugs/1604250](http://jython.org/bugs/1604250){.http}

  - descrdoc

- [http://jython.org/bugs/1604252](http://jython.org/bugs/1604252){.http}

  - setclass

- copy doesn\'t work on instances of new style classes - [http://jython.org/bugs/1604258](http://jython.org/bugs/1604258){.http}

  - copies
  - copy_setstate

- [http://jython.org/bugs/1604264](http://jython.org/bugs/1604264){.http}

  - str_of_str_subclass

- [PyStringMap](./PyStringMap.html){.nonexistent} is missing iter methods - [http://jython.org/bugs/1604265](http://jython.org/bugs/1604265){.http}

  - dictproxyiterkeys
  - dictproxyitervalues
  - dictproxyiteritems

- [http://jython.org/bugs/1605006](http://jython.org/bugs/1605006){.http}

  - str_of_str_subclass

- [http://jython.org/bugs/1605009](http://jython.org/bugs/1605009){.http}

  - string_exceptions

- [http://jython.org/bugs/1605011](http://jython.org/bugs/1605011){.http} - assigning [bases]{.u} doesn\'t change lookup in classes

  - test_mutable_bases
  - test_mutable_bases_catch_mro_conflict

- [http://jython.org/bugs/1605019](http://jython.org/bugs/1605019){.http} - binding instance method to class calls class instead of instance

  - methods

- [http://jython.org/1605023](http://jython.org/1605023){.http} - new on metaclass not called

  - metaclass

# To File {#To_File}

- mutable_names - setting [name]{.u} on a class does nothing

- slotspecials - slots need [weakref]{.u}

# Don\'t Understand Failure {#Don.27t_Understand_Failure}

- supers - subclassing super causes binding to break

- overloading - a\[0:10\] = \"foo\" doesn\'t call [setslice]{.u} on a

- comparison method on inherited class not called, superclass is used instead
  - inherits
  - binopoverride
  - str_subclass_as_dict_key
  - rich_comparisons

# Cpython Specific Tests {#Cpython_Specific_Tests}

- checks that things aren\'t allowed to inherit CFunction. I doubt we care.
  - errors

- expects immediate gc
  - slots
  - subtype_resurrection
  - weakref

- expects attributes to be descriptors
  - classic

- expects id == hash on object
  - specials
  - subclasspropagation

- expects classes to have [basicsize]{.u}

  - slotmultipleinheritance

# To Investigate {#To_Investigate}

- pickles
- delhook
- pickleslots
- subclass_right_op
- meth_class_get
- isinst_isclass
- proxysuper
- carloverre
:::
