# MacPython/CoreAudio

::: {#content dir="ltr" lang="en"}
Links:

- [MusicKit](http://www.musickit.org/){.http} - [/PyObjC](./MacPython(2f)CoreAudio(2f)PyObjC.html){.nonexistent}

- [Boodler](http://www.eblong.com/zarf/boodler/){.http} - [/Python](./MacPython(2f)CoreAudio(2f)Python.html){.nonexistent}

I ([DonovanPreston](DonovanPreston)) have been noodling around with wrapping the low level [/CoreAudio](./MacPython(2f)CoreAudio(2f)CoreAudio.html){.nonexistent} APIs necessary to generate sound on Mac OS X using Python. After struggling with threading and callbacks into Python issues I managed to get a simple hello world going which just plays a sine wave for 5 seconds. The bulk of the code is in a pyrex file here:

- [http://soundfarmer.com/content/code/coreaudio/coreaudio.pyx](http://soundfarmer.com/content/code/coreaudio/coreaudio.pyx){.http}

And here is the simple driver python script:

- [http://soundfarmer.com/content/code/coreaudio/catest.py](http://soundfarmer.com/content/code/coreaudio/catest.py){.http}

You compile the pyrex to a c file, and then there is a setup script which will build the extension module:

- [http://soundfarmer.com/content/code/coreaudio/setup.py](http://soundfarmer.com/content/code/coreaudio/setup.py){.http}

Other links:

- [http://aldebaran.armory.com/\~zenomt/macosx/](http://aldebaran.armory.com/~zenomt/macosx/){.http}

- [http://www.mat.ucsb.edu/\~c.ramakr/illposed/craudiounits.html](http://www.mat.ucsb.edu/~c.ramakr/illposed/craudiounits.html){.http}

- [http://www.pete.yandell.com/software/pymidi/Read%20Me.html](http://www.pete.yandell.com/software/pymidi/Read%20Me.html){.http}
:::
