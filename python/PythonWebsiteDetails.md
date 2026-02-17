# PythonWebsiteDetails

::: {#content dir="ltr" lang="en"}
## Where do I put assets? (images, files, html pages, etc)? {#Where_do_I_put_assets.3F_.28images.2C_files.2C_html_pages.2C_etc.29.3F}

In most cases, place them into the same location as the yml and html template files. The build copies them into place automatically. For html trees, place them into a directory that contains a file called NOBUILD. This tells the build system to just copy the html files instead of trying to process them.

Site-wide and style related images go into in /images instead.

## Changing templates {#Changing_templates}

If you change templates, you have to make sure that the build/new-build/ is updated on the server and then trigger a website rebuild from scratch.

1.  log in to the server
2.  cd to the /data/website-build/build dir
3.  svn update .
4.  make clean

Then issues a small checkin to the data/content.ht file (e.g. add a space somewhere) to trigger a rebuild and check the build on the status page:

- [http://www.python.org/status/](http://www.python.org/status/){.http}

*Note:* For some reason the automatic build process only updates a few directories in the build/ dir on the server, not all of them. The new-build/ dir containing the templates is not among the automatically updated ones, so the above manual process has to be done in order to update the templates.

## Debugging in Wing IDE {#Debugging_in_Wing_IDE}

To debug pyramid in Wing IDE, set up a project, add the build script as the main debug file and set the parameters and starting directory in the File Properties (right click on file or file\'s name in project view) to match those in the invocation in the Makefile. This can help with debugging build problems.

## Migrating old Pages {#Migrating_old_Pages}

(This is increasingly uncommon)

Some pages are still in the old website format and copied over from an instance of the old website automatically during the build process. If you plan to migrate any of these pages to the new site, read the [PythonWebsitePyramidUsersGuide](PythonWebsitePyramidUsersGuide) section on converting content with mkpydir and see also some older content migration notes we\'ve saved in [PythonWebsiteContentMigration](PythonWebsiteContentMigration).

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
:::
