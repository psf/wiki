# Distutils/Proposals/SetupClass

::: {#content dir="ltr" lang="en"}
## Setup as a Class not a procedure {#Setup_as_a_Class_not_a_procedure}

---David Lyon

Let\'s modernise setup and make it Object Oriented.

This will make it more user friendly and easier to learn and use.

To do this, we\'ll need to:

1\) Extend setup.cfg to hold more/all-of the metadata

2\) Turn \'setup\' into a class (rather than a procedure)

3\) Provide member information:

- destination directory (self.destination?).
- self.os_name - Operating system.
- self.window_manager - Window manager.
- self.scripts - location of script directories.
- self.data_dir - location of data directories.
- self.doc_dir - location of docs directories.
- self.desktop_shortcuts - an object for adding shortcuts.
- self.program_shortcuts - an object for adding shortcuts.
- self.packages -list of python packages already installed
- self.web_environment - information about the web environment

4\) self.pre_setup() - A method run before setup

- This method can read member properties and do pre-setup
  - initialisation.
- When the \"self.\"\* properties are then all adjusted
  - the code can proceed to the \'self.setup()\' method where the actual install can be done.

5\) self.post_setup() - A method for post-install configuration

- This then gives the application a chance to do post
  - setup initialisation.
- Examples are modifying attributes, registering
  - libraries, generating documentation\...
:::
