# JythonDeveloperGuide/IntellijTricks

::::::: {#content dir="ltr" lang="en"}
# Intellij IDEA Tricks {#Intellij_IDEA_Tricks}

This page describes useful tricks for Intellij IDEA users. If you haven\'t created an Intellij project for Jython yet, see [JythonDeveloperGuide/IntellijNotes](./JythonDeveloperGuide(2f)IntellijNotes.html).

::: table-of-contents
Contents

1.  [Intellij IDEA Tricks](#Intellij_IDEA_Tricks)
    1.  [Eclipse Code Formatter](#Eclipse_Code_Formatter)
    2.  [Running Jython and JUnit tests inside IDEA](#Running_Jython_and_JUnit_tests_inside_IDEA)
        1.  [Jython](#Jython)
            1.  [Example: Regression Tests](#Example:_Regression_Tests)
        2.  [JUnit tests](#JUnit_tests)
            1.  [Example: \_ioTest](#Example:__ioTest)
:::

## Eclipse Code Formatter {#Eclipse_Code_Formatter}

Configuring the [CodingStandards](CodingStandards) by hand is an annoying task. Fortunately there is a plugin to import Eclipse code formatting rules into Intellij IDEA: Eclipse Code Formatter. It is available in the plugin repository.

The Eclipse Code Styles file is attached to the [CodingStandards](CodingStandards) page.

Eclipse Code Formatter can be configured under *Settings* (shortcut: ctrl + alt + s) \--\> *Eclipse Code Formatter*

## Running Jython and JUnit tests inside IDEA {#Running_Jython_and_JUnit_tests_inside_IDEA}

General *Run/Debug Configurations* settings:

::: {}
  --------------------- ---------------------------------------------------------------------------------------------------------------------
  Parameter Name        Value
  VM options            *-Dpython.home=dist -Dpython.console=org.python.util.[InteractiveConsole](./InteractiveConsole.html){.nonexistent}*
  Working directory     project basedir
  Classpath of module   *jython-trunk*
  --------------------- ---------------------------------------------------------------------------------------------------------------------
:::

### Jython {#Jython}

Configuration Type: **Application**

Additional parameters:

::: {}
  ------------------------------ ----------------------------------------------------------
  Parameter Name                 Value
  Main class                     *org.python.util.jython*
  Program arguments (optional)   Parameters for Jython, e.g. the python module to execute
  ------------------------------ ----------------------------------------------------------
:::

#### Example: Regression Tests {#Example:_Regression_Tests}

Running the regression tests in IDEA is interesting for at least two reasons:

1.  Code Coverage
2.  Debugger

![JythonRegressionTestConfiguration.jpg](attachments/JythonDeveloperGuide(2f)IntellijTricks/JythonRegressionTestConfiguration.jpg "JythonRegressionTestConfiguration.jpg"){.attachment}

See *regrtest.py* for detailed information about additional program arguments.

### JUnit tests {#JUnit_tests}

Configuration Type: **JUnit**

Additional parameters:

::: {}
  ------------------------------ ----------------------------------------------------------
  Parameter Name                 Value
  Main class                     *org.python.util.jython*
  Program arguments (optional)   Parameters for Jython, e.g. the python module to execute
  ------------------------------ ----------------------------------------------------------
:::

#### Example: \_ioTest {#Example:__ioTest}

![JythonJUnitConfiguration.jpg](attachments/JythonDeveloperGuide(2f)IntellijTricks/JythonJUnitConfiguration.jpg "JythonJUnitConfiguration.jpg"){.attachment}
:::::::
