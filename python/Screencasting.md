# Screencasting

::: {#content dir="ltr" lang="en"}
Screencasting is the process of recording screencast - a video stream of picture from the screen (desktop, application or a single window). It allows to see how another person works through the eyes of this person. Tutorials, announcements, conference talks - many things benefit from a quality made screencast.

In Python, [Blender community](http://www.blendernation.com/){.http} uses screencasts a lot and they even [made Python helper](http://www.davidrevoy.com/index.php?article65/recordscreen-py-video-and-audio-capture-for-linux-with-ffmpeg){.http} to aid the process of capturing screen with FFMPEG on Linux.

Helpful tools for recording and processing screencasts:

### In Python {#In_Python}

- [recordscreen.py](http://www.davidrevoy.com/index.php?article65/recordscreen-py-video-and-audio-capture-for-linux-with-ffmpeg){.http} - video and audio capture for Linux with ffmpeg by Nathan Vegdahl, MIT

  - \`python recordscreen.py -n -w \--vcodec vp8 output.webm\' - select window to capture, turn off sound, record into WebM

- [key-mon](http://code.google.com/p/key-mon/){.http} - keyboard status monitor (Linux, Apache 2.0)

- [Blender Key Status Script, GPL](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Screencast_Key_Status_Tool){.http}

### Other {#Other}

- [LICEcap](http://www.cockos.com/licecap/){.http} - GPL, non-Python tool for Mac OS and Windows that produces screencasting GIFs
:::
