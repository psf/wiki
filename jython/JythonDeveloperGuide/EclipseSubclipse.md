# JythonDeveloperGuide/EclipseSubclipse

::: {#content dir="ltr" lang="en"}
# Setting up the jython development environment in Eclipse with Subclipse {#Setting_up_the_jython_development_environment_in_Eclipse_with_Subclipse}

Another way (see [EclipseNotes](./EclipseNotes.html){.nonexistent}) to obtain the jython sources to Eclipse is to use the Subclipse plugin (Subversion for Eclipse). (I\'m not sure whether sf.net has some temporary technical problems right now, but at least I wasn\'t able get the sources via CVS at all.)

This advice is applicable to Eclipse 3.2, but might work for previous releases too.

## Installing the Subclipse plugin {#Installing_the_Subclipse_plugin}

- Go to Help -\> Software Updates -\> Find and Install\...

- Go to Search for new features to install

- Add a new remote site: [http://subclipse.tigris.org/update_1.2.x](http://subclipse.tigris.org/update_1.2.x){.http} (see [http://subclipse.tigris.org/callisto.html](http://subclipse.tigris.org/callisto.html){.http} for more details)

- Install the plugin by selecting the product from the subclipse site.

## Checking out the Jython project {#Checking_out_the_Jython_project}

- Switch to SVN Repository Exploring perspective

- Add a new SVN repository, URL: [https://svn.sourceforge.net/svnroot/jython](https://svn.sourceforge.net/svnroot/jython){.https}

- Select trunk/jython from the repository tree and Checkout the project as usual.
:::
