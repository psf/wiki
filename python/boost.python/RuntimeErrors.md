# boost.python/RuntimeErrors

::: {#content dir="ltr" lang="en"}
[boost.python](./boost(2e)python.html) tries hard to provide best possible run-time errors. But often enough they need futher explanation. Some of them are mentioned below:

### TypeError: bad argument type for built-in operation {#TypeError:_bad_argument_type_for_built-in_operation}

Usualy means BPL couldn\'t find c++ method/function with appropriate signature. Very often that is wrong number of arguments, wrong argument(s) type and so on.

### TypeError: No to_python converter found for C++ type: \<type\> {#TypeError:_No_to_python_converter_found_for_C.2B-.2B-_type:_.3Ctype.3E}

### TypeError: No to_python (by-value) converter found for C++ type: \<type\> {#TypeError:_No_to_python_.28by-value.29_converter_found_for_C.2B-.2B-_type:_.3Ctype.3E}

BPL was unable to get C++ value from Python object.

For example, when calling ` extract<int>(<object>.attr("__len__")()) ` to get object length you omitted \"**()**\".

### RuntimeError: This class cannot be instantiated from Python {#RuntimeError:_This_class_cannot_be_instantiated_from_Python}

Attempt to instantiate a class with *no_init* descriptor. It may be private constructor or abstract class.

### RuntimeError: unidentifiable C++ Exception {#RuntimeError:_unidentifiable_C.2B-.2B-_Exception}

Boost.Python provides a default exception handler that translates selected standard exceptions, then gives up with that message.

To install your own exception translator **don\'t** see [tutorial](http://www.boost.org/libs/python/doc/tutorial/doc/exception_translation.html){.http}. ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"} (**&** missed in register_exception_translator call)\
Use that:

    struct PodBayDoorException;
    void translator(const PodBayDoorException& x) {
      PyErr_SetString(PyExc_UserWarning, "I'm sorry Dave...");
    }
    BOOST_PYTHON_MODULE(kubrick) {
      register_exception_translator<
      PodBayDoorException>(&translator);
      ...
    }
:::
