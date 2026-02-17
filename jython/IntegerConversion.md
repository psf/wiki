# IntegerConversion

:::: {#content dir="ltr" lang="en"}
::: {}
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------
  **CPython function**                                                                                                                                                                                            **Jython method**
  long intobject::[PyInt](./PyInt.html){.nonexistent}\_[AsLong](./AsLong.html){.nonexistent}(register [PyObject](./PyObject.html){.nonexistent} \*op)                                                             int [PyObject](./PyObject.html){.nonexistent}.asInt()
  [PyObject](./PyObject.html){.nonexistent}\* intobject::[PyInt](./PyInt.html){.nonexistent}\_[FromString](./FromString.html){.nonexistent}(char \*s, char \*\*pend, int base)                                    [PyObject](./PyObject.html){.nonexistent} [PyObject](./PyObject.html){.nonexistent}.`__int__`()
  Py_ssize_t intobject::[PyInt](./PyInt.html){.nonexistent}\_[AsSsize](./AsSsize.html){.nonexistent}\_t(register [PyObject](./PyObject.html){.nonexistent} \*op)                                                  int [PyObject](./PyObject.html){.nonexistent}.`__int__`().asInt()
  Py_ssize_t abstract::[PyNumber](./PyNumber.html){.nonexistent}\_[AsSsize](./AsSsize.html){.nonexistent}\_t([PyObject](./PyObject.html){.nonexistent} \*item, [PyObject](./PyObject.html){.nonexistent} \*err)   int [PyObject](./PyObject.html){.nonexistent}.asIndex(err)
  int abstract.h::[PyIndex](./PyIndex.html){.nonexistent}\_Check([PyObject](./PyObject.html){.nonexistent} \*ob)                                                                                                  boolean [PyObject](./PyObject.html){.nonexistent}.isIndex()
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------
:::

When using asInt, consider whether you want to ensure the original object is an instanceof [PyInteger/PyLong](./PyInteger(2f)PyLong.html){.nonexistent} prior to calling asInt on it. It\'s common to do this check before calling asInt, but is not required \-- otherwise asInt will attempt to implicitly convert non int/longs via user defined `__int__` methods.
::::
