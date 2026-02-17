# DreamPieMacSupport

::: {#content dir="ltr" lang="en"}
[DreamPie](http://dreampie.sourceforge.net/){.http} requires PyGTK, which, for Mac, requires [MacPorts](http://www.macports.org){.http}.

The installation instructions are:

- Install MacPorts.

- Install X11.

- Download the source archive and unpack it.

- Run `sudo port install py26-pygtksourceview`. This may take a long time (even hours).

- Run `python2.6 dreampie`.

Please add here any comments or suggestions.

Also, if anybody volunteers to create a MacPorts package, it would be very nice!

## GError: Couldn\'t recognize the image file format for file {#GError:_Couldn.27t_recognize_the_image_file_format_for_file}

Joe VanAndel experienced this problem, which caused DreamPie to not start at all.

The fix is was to run `setenv XDG_DATA_DIRS /opt/local/share` before running DreamPie.

See: [https://bugs.launchpad.net/dreampie/+bug/526197](https://bugs.launchpad.net/dreampie/+bug/526197){.https}
:::
