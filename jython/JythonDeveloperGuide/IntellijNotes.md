# JythonDeveloperGuide/IntellijNotes

:::::::::::: {#content dir="ltr" lang="en"}
# Intellij project creation notes {#Intellij_project_creation_notes}

Jython is an Ant project. This makes it a bit difficult to import into Intellij IDEA. This step by step guide should help you to get started.

::: table-of-contents
Contents

1.  [Intellij project creation notes](#Intellij_project_creation_notes)
    1.  [Prequisites](#Prequisites)
        1.  [Software packages (outside Intellij)](#Software_packages_.28outside_Intellij.29)
        2.  [Intellij Plugins](#Intellij_Plugins)
    2.  [Steps](#Steps)
        1.  [Make a clean checkout](#Make_a_clean_checkout)
        2.  [Remove Intellij files from jython](#Remove_Intellij_files_from_jython)
        3.  [Run ant](#Run_ant)
        4.  [Import jython as Eclipse-Project in Intellij IDEA](#Import_jython_as_Eclipse-Project_in_Intellij_IDEA)
        5.  [Configure SDKs](#Configure_SDKs)
        6.  [InformixDataHandler and OracleDataHandler](#InformixDataHandler_and_OracleDataHandler)
        7.  [Make](#Make)
    3.  [What did we?](#What_did_we.3F)
:::

## Prequisites {#Prequisites}

### Software packages (outside Intellij) {#Software_packages_.28outside_Intellij.29}

- ant

- mercurial

- Java JDK

- Python 2.7

- Intellij IDEA 12 ([http://www.jetbrains.com/idea/](http://www.jetbrains.com/idea/){.http})

There is a free \"Community Edition\" of Intellij that might work (I\'m only unsure about the Python integration). However as I ([SvenDehmlow](./SvenDehmlow.html){.nonexistent}) use the Ultimate Edition, this tutorial is tested with this edition.

Intellij offers free IDEA licenses for Open Source projects. Perhaps it might be a good idea to apply for them.

### Intellij Plugins {#Intellij_Plugins}

- Ant Support (Bundled)
- Eclipse Integration (Bundled)
- hg4idea (Bundled)
- Python (Custom, i.e. must be installed from Intellij plugin repository)

Of course there are many other useful plugins, but these four are essential for importing Jython into Intellij IDEA.

## Steps {#Steps}

### Make a clean checkout {#Make_a_clean_checkout}

:::: {.highlight .bash}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1f44a61e7268d07d6124f351c3f1fc2a92c1e780 dir="ltr" lang="en"}
   1 hg clone http://bitbucket.org/jython/jython jython
```
:::
::::

### Remove Intellij files from jython {#Remove_Intellij_files_from_jython}

Unfortunately the Intellij project files in the jython source directory don\'t work (anymore?). We\'ll delete them. Later Intellij IDEA will create new ones for us.

Change into the jython directory:

:::: {.highlight .bash}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-e4db1d5aba8d1213378faa1f7b938ad94fbb1bb8 dir="ltr" lang="en"}
   1 cd jython
```
:::
::::

Remove files:

:::: {.highlight .bash}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-8b574bd19f391dd21d14be6b7c9055ec9094aa7c dir="ltr" lang="en"}
   1 rm -rf .idea/
   2 rm Jython27.iml
```
:::
::::

### Run ant {#Run_ant}

Run this in the jython source directory (if you made the previous step, you\'re already there):

:::: {.highlight .bash}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-64bd05d89142566144bce27f4904a322d8d9e836 dir="ltr" lang="en"}
   1 ant
```
:::
::::

### Import jython as Eclipse-Project in Intellij IDEA {#Import_jython_as_Eclipse-Project_in_Intellij_IDEA}

Start Intellij IDEA. Close the last open project (if there\'s any), to get to the start screen.

Choose *Import Project*:

![WelcomeToIntellijIdea.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/WelcomeToIntellijIdea.png "WelcomeToIntellijIdea.png"){.attachment align="top"}

Select jython source directory:

![SelectFileOrDirectoryToImport.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/SelectFileOrDirectoryToImport.png "SelectFileOrDirectoryToImport.png"){.attachment align="top"}

*Import project from external model* \--\> *Eclipse*:

![ImportProject.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/ImportProject.png "ImportProject.png"){.attachment align="top"}

Check *Link created Intellij IDEA modules to Eclipse project files*. For other fields the defaults should be sufficient.

![ImportProject2.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/ImportProject2.png "ImportProject2.png"){.attachment align="top"}

*Finish*:

![ImportProject3.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/ImportProject3.png "ImportProject3.png"){.attachment align="top"}

Drag and drop the ant build.xml from the project window to the ant window. This will make Intellij aware of the ant project.

![DragAndDropAnt.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/DragAndDropAnt.png "DragAndDropAnt.png"){.attachment align="top"}

### Configure SDKs {#Configure_SDKs}

If you\'ve configured more than one SDK for Python oder Java in Intellij IDEA, you should open the *Project Structure* (Shortcut: Strg + Alt + Shift + s) and check that the right SDKs are used for Jython.

I think a JDK \>= 6 and CPython corresponting to the current Jython version (2.7) are good guesses.

![ProjectStructureFacetPython.jpg](attachments/JythonDeveloperGuide(2f)IntellijNotes/ProjectStructureFacetPython.jpg "ProjectStructureFacetPython.jpg"){.attachment align="top"}

![ProjectStructureProjectSDK.jpg](attachments/JythonDeveloperGuide(2f)IntellijNotes/ProjectStructureProjectSDK.jpg "ProjectStructureProjectSDK.jpg"){.attachment align="top"}

### InformixDataHandler and OracleDataHandler {#InformixDataHandler_and_OracleDataHandler}

The classes [InformixDataHandler](./InformixDataHandler.html){.nonexistent} and [OracleDataHandler](./OracleDataHandler.html){.nonexistent} depend on proprietary Jars. Downloading the Oracle odbc.jar for example requires a reqistration at Oracles Website.

If you just want to get your project running, delete both classes ([InformixDataHandler](./InformixDataHandler.html){.nonexistent} and [OracleDataHandler](./OracleDataHandler.html){.nonexistent}). Thats it. ![:)](/wiki/modernized/img/smile.png ":)"){height="16" width="16"}

If you\'re going to work in the area of JDBC data handlers, figure from build.xml out which jars you\'ll need (one for Infromix and one for Oracle), download them and put them into the extlibs directory.

### Make {#Make}

Build the project to see, if everything went well. For this either use *Build* \--\> *Make Project* in the menu or the shortcut Ctrl + F9.

## What did we? {#What_did_we.3F}

Speaking in Intellij jargon, we adopted the whole *Project Structure* (classpath, source and test directories, libaries) from the Eclipse project files. We could have done this manually, but this way was much easier and less error-prone.

It\'s a good idea to take a look at the *Project Structure* (Shortcut: Ctrl + Alt + Shift + s) as e.g. the classpath might change with the next update.
::::::::::::
