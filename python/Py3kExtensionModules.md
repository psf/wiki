# Py3kExtensionModules

:::::::::: {#content dir="ltr" lang="en"}
::: caution
**Python 2.x will no longer be supported after 1 Jan 2020.** Python 2 reaches end of life in January 2020, and will no longer receive security updates. This page has resources to help with porting applications still running Python 2 to Python 3.
:::

This is a list of suggestions about the migration of Python C extension modules to Python 3.0. Feel free to expand the list!

- First of all, see [Porting extension modules to 3.0](http://docs.python.org/dev/3.0/howto/cporting.html){.http} in the official Python 3 documentation.

- Use conditional compilation to make your code able to compile under both Python 2.x and 3.0 C-API.

- Now Python 3 uses Unicode as internal string representation, all the class name, method name, etc are Unicode strings. So check all the occurrences of [PyString](./PyString.html){.nonexistent}\_\*, most of them should be replaced with [PyUnicode](./PyUnicode.html){.nonexistent}\_\*. When you suffer a segmentation fault, sometimes it\'s because you provided a [PyString](./PyString.html){.nonexistent} where the C-API is expecting a [PyUnicode](./PyUnicode.html){.nonexistent}. Also, for the return value of your C extension function, you may use [PyUnicode](./PyUnicode.html){.nonexistent} instead of [PyString](./PyString.html){.nonexistent}, otherwise you may break your client\'s code.

- [PyInt](./PyInt.html){.nonexistent}\_\* removed, but you can explicitly #include \<intobject.h\> to define aliases that redirect most [PyInt](./PyInt.html){.nonexistent}\_\* symbols to [PyLong](./PyLong.html){.nonexistent}\_\*.

- PEP 3123: Making [PyObject](./PyObject.html){.nonexistent}\_HEAD conform to standard C ([http://www.python.org/dev/peps/pep-3123/](http://www.python.org/dev/peps/pep-3123/){.http}). When initializing type objects, replace

:::: {.highlight .cpp}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f42faa1c6562a32a42eafbd922cf6f0034973d45 dir="ltr" lang="en"}
   1 PyObject_HEAD_INIT(NULL)
   2 0, /* ob_size */
```
:::
::::

- with

:::: {.highlight .cpp}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-320e78809e6616f9f84c0b40e705f294f677f62b dir="ltr" lang="en"}
   1 PyVarObject_HEAD_INIT(NULL, 0)
```
:::
::::

- And you\'d better use pre-defined macros Py_TYPE(o), Py_REFCNT(o), Py_SIZE(o) to access o-\>ob_type, o-\>ob_refcnt and o-\>ob_size separately. For more details please read the PEP.

- Changes in [PyNumberMethods](./PyNumberMethods.html){.nonexistent}: nb_divide, nb_coerce, nb_oct, nb_hex and nb_inplace_divide removed.

- Read PEP 3121 Extension Module Initialization and Finalization ([http://www.python.org/dev/peps/pep-3121/](http://www.python.org/dev/peps/pep-3121/){.http}) and change your code to the new API. It solved many problems for module initialization and finalization.

- Now [PyObject](./PyObject.html){.nonexistent}\_Compare() raises exception when comparing two objects of different type. (In case of Python 2.x, it compares their pointer.)

- If your object has slicing interface (eg. obj\[2:5\]), you should notice that [getitem]{.u}, [setitem]{.u} and [delitem]{.u} now receive [PySliceObject](./PySliceObject.html){.nonexistent} instead of a pair of integer value.

- Unbound method removed. In Python 3 you can use [PyInstanceMethod](./PyInstanceMethod.html){.nonexistent}\_New() C-API to generate an unbound method for your C function.

- [PyClass](./PyClass.html){.nonexistent}\_Check() removed. Consider this as a workaround:

:::: {.highlight .cpp}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-78778b8900d67b2b8b2d6054cb2346058f527716 dir="ltr" lang="en"}
   1 #define PyClass_Check(obj) PyObject_IsInstance(obj, (PyObject *)&PyType_Type)
   2 
```
:::
::::

- [PyInstance](./PyInstance.html){.nonexistent}\_[NewRaw](./NewRaw.html){.nonexistent}() removed, try to use [PyBaseObject](./PyBaseObject.html){.nonexistent}\_Type.tp_new() for replacement.

- In py3k dict.items() method returns a dict_items object, you can use [PySequence](./PySequence.html){.nonexistent}\_Fast() to convert it to a sequence.

- struct member flags: The RO shorthand for READONLY is gone.
::::::::::
