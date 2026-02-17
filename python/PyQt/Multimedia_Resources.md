# PyQt/Multimedia_Resources

::: {#content dir="ltr" lang="en"}
# Multimedia Resources {#Multimedia_Resources}

There seem to be a few cross-platform resources for playing video and decoding movies, some of which are available in Python. It might be worthwhile trying to create wrappers for some of the more interesting projects.

## Non-Python Resources {#Non-Python_Resources}

The [avifile](http://avifile.sourceforge.net/){.http} project provides a Qt 3-based player on Linux, and would seem to be a reasonable candidate for a [PyQt](PyQt) wrapper. However, there doesn\'t seem to be much documentation for it outside the header files, but it might be possible to create a reasonably high-level wrapper using SIP, and at least we know it will work with Qt\'s event loop.

[FFmpeg](http://ffmpeg.mplayerhq.hu/){.http} provides a set of tools and libraries that could be used to play and manipulate video.

## Python Resources {#Python_Resources}

- [PyMedia](http://pymedia.org/){.http} is a Python package that supports various audio and video formats.

- In [a message](http://www.riverbankcomputing.com/pipermail/pyqt/2009-September/024240.html){.http} to [the PyQt mailing list](./PyQt(2f)TheMailingList.html), Baz Walter gives an example of using GStreamer bindings for Python with PyQt (see [Using GStreamer with PyQt](./PyQt(2f)Using(20)GStreamer(20)with(20)PyQt.html)).

## Out of Process Wrappers {#Out_of_Process_Wrappers}

Henning Schröder posted a link to his PyQt (Qt 3) MPlayer wrapper widget in [a message](http://www.riverbankcomputing.com/pipermail/pyqt/2007-June/016277.html){.http} to [the mailing list](./TheMailingList.html){.nonexistent}. He has kindly donated the code to the community, and it can also be obtained from the [MPlayerWidget](./PyQt(2f)Multimedia_Resources(2f)MPlayerWidget.html) page.
:::
