# JythonFaq/EmbeddingJython

:::::::::::::: {#content dir="ltr" lang="en"}
# Embedding Jython {#Embedding_Jython}

[JythonFaq](JythonFaq)

::: table-of-contents
Contents

1.  [Embedding Jython](#Embedding_Jython)
    1.  [How can I use jython classes from my java application?](#How_can_I_use_jython_classes_from_my_java_application.3F)
        1.  [Using PythonInterpreter in Factories to instantiate python classes](#Using_PythonInterpreter_in_Factories_to_instantiate_python_classes)
        2.  [Using jythonc (deprecated)](#Using_jythonc_.28deprecated.29)
    2.  [My modules can not be found when imported from an embedded application](#My_modules_can_not_be_found_when_imported_from_an_embedded_application)
    3.  [Library types and functions can\'t be found by my embedded application](#Library_types_and_functions_can.27t_be_found_by_my_embedded_application)
:::

------------------------------------------------------------------------

## How can I use jython classes from my java application? {#How_can_I_use_jython_classes_from_my_java_application.3F}

There are several ways to do that. The best way depends on the needs of your application.

### Using PythonInterpreter in Factories to instantiate python classes {#Using_PythonInterpreter_in_Factories_to_instantiate_python_classes}

- [Simple and Efficient Jython Object Factories](http://wiki.python.org/jython/JythonMonthly/Articles/October2006/3){.http} from [CharlieGroves](CharlieGroves)

- [Object Factories](http://www.jython.org/jythonbook/en/1.0/JythonAndJavaIntegration.html#using-jython-within-java-applications){.http} from Jython Book v1.0

### Using jythonc (deprecated) {#Using_jythonc_.28deprecated.29}

Compile the python class into a real java class using the jythonc command. This real java can be used and instances can be created from your application.

**Note: It is no longer recommended that jythonc be used, see [ReplaceJythonc](ReplaceJythonc)**

Create a python module (say Foo.py) and make a class with the same name as the python module. The class must inherit from a java class or interface. If you don\'t need a particular java superclass, just use java.lang.Object.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-04f877428c93d5774dc54c5d662154cc674c605f dir="ltr" lang="en"}
   1   import java
   2   class Foo(java.util.Date):
   3       def toString(self):
   4           return "Foo[" + java.util.Date.toString(self) + "]"
```
:::
::::

The python class can overwrite all existing methods on the java superclass or interface and these overridden methods can be called from the java application. New methods can by default not be accessed from java. If we add a \"bar\" method, the method can be used from python, but not from java.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c71069ca5d2760050d922252c05bff46b110b6e4 dir="ltr" lang="en"}
   1   import java
   2   class Foo(java.util.Date):
   3       def __init__(self):
   4           self.count = 0
   5       def bar(self, incr=1):
   6           self.count += incr
   7           return self.count
   8       def toString(self):
   9           cnt = self.bar()
  10           return "Foo[" + java.util.Date.toString(self) + " " + `cnt` + "]"
```
:::
::::

The jythonc compiler can also create java methods for the python methods, but it need some additional help. This help is specified as a \@sig line in the doc-string for the method. A doc-string is added to the example above.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-529d25448d183c1a72588314c4551aed964ddc43 dir="ltr" lang="en"}
   1   import java
   2   class Foo(java.util.Date):
   3       def __init__(self):
   4           self.count = 0
   5       def bar(self, incr=1):
   6           """@sig void bar(int incr)"""
   7           self.count += incr
   8           return self.count
   9       def toString(self):
  10           cnt = self.bar()
  11           return "Foo[" + java.util.Date.toString(self) + " " + `cnt` + "]"
```
:::
::::

When this class is compiled with jythonc, A java class Foo.java and Foo.class is created with the java methods toString(), bar() and bar(int incr).

When compiling the Foo.py class, make sure that the Foo actually extends the desired java class. You can check the output from the compilation. It should contain lines like:

      Required packages:
        java.util

      Creating adapters:

      Creating .java files:
        Foo module
          Foo extends java.util.Date

If jython fails to recognize the superclass as a java class, it will silently assume that it is a python class and will not generate the desired java methods.

The new Foo class can be used from java class like this:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1984e00f192e8f97f736ef456241920c82aa3034 dir="ltr" lang="en"}
   1    public class FooTest {
   2        public static void main(String[] args) {
   3            Foo foo = new Foo();
   4            System.out.println(foo);
   5            foo.bar();
   6            foo.bar(43);
   7            System.out.println(foo);
   8        }
   9    }
```
:::
::::

When compiling the [FooTest](./FooTest.html){.nonexistent}.java class, the \"jpywork\" directory should be appended to your classpath.

When running this little application, the jython.jar runtime must be available on the CLASSPATH or specified on the java command line.

------------------------------------------------------------------------

## My modules can not be found when imported from an embedded application {#My_modules_can_not_be_found_when_imported_from_an_embedded_application}

The default value for sys.path in an embedded application depend on several things:

1.  A python.path property, if found in the registry file or in the \$HOME/.jython file will be used.

2.  The \<python.home\>/Lib directory is added.

An application can override the python.path property by calling [PythonInterpreter](./PythonInterpreter.html){.nonexistent}.initialize(..) before any other python code is called:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-82b51a19720fb3198e7cfe985c9eaa0958f41bef dir="ltr" lang="en"}
   1     Properties props = new Properties();
   2     props.setProperty("python.path", "/home/modules:scripts");
   3     PythonInterpreter.initialize(System.getProperties(), props,
   4                                  new String[] {""});
```
:::
::::

The value for python.path must follow the operating system conventions for the PATH environment var (\':\' separator for unix, \';\' for windows)

------------------------------------------------------------------------

## Library types and functions can\'t be found by my embedded application {#Library_types_and_functions_can.27t_be_found_by_my_embedded_application}

When you run the jython installer, one of the choices is to install as a callable JAR. Use that selection to create a standalone JAR which can be used to embed. The jython.jar in the standard install isn\'t complete to be used as a standalone JAR (despite the fact that they have the same name).
::::::::::::::
