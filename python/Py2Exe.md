# Py2Exe

::: {#content dir="ltr" lang="en"}
**py2exe** is a module that makes it so you can compile Python code to Windows executables.

## Linux compatibility {#Linux_compatibility}

py2exe and NSIS through WINE (for making Windows executables) is handy, but py2exe produces invalid Win32 executables

Problem 1

- [http://bugs.winehq.org/show_bug.cgi?id=3591](http://bugs.winehq.org/show_bug.cgi?id=3591){.http}

Problem 2

- [http://bugs.winehq.org/show_bug.cgi?id=3897](http://bugs.winehq.org/show_bug.cgi?id=3897){.http}

- fixme:resource:get_resource_section .rsrc isn\'t the last section

- [RuntimeError](./RuntimeError.html){.nonexistent}: [EndUpdateResource](./EndUpdateResource.html){.nonexistent}: Success

## See Also {#See_Also}

- [py2exe home page and wiki](http://www.py2exe.org){.http}

- [DistributionUtilities](DistributionUtilities)

------------------------------------------------------------------------

## Discussion {#Discussion}

I\'m wondering: Is there something like Py2Exe, but for Linux?

We have some Python code that we\'d like clients to be able to run, but we don\'t want them to have to install Python.

I know that Python is a required install on Red Hat 9 and up, but I don\'t think it is a required install on Suse, or Mandrake, or yadda yadda yadda. So, I think this would be useful. If we had somethig like Py2Exe *for Linux,* then we can justify using Python here at work.

The question is: Does something like this exist right now?

No, we can\'t require our users to install something new. Everything has to just run, right out of the box, with zero installation.

Try googling for \"freeze\". It\'s in the Python distribution (in fact, there\'s a FAQ section called [1.4 Where is Freeze for Windows?](http://python.org/doc/faq/windows.html#where-is-freeze-for-windows){.http}, waddayamean, is there a Py2Exe for Linux ;)).

\-- [JohannesGijsbers](JohannesGijsbers)

Heh! Well, I just never saw anything about Freeze online. I googled for \"compile Python to executable\" and stuff like that, for about 30 minutes, and never saw a single mention of Freeze. \"If it\'s not on the net, it may well not exist,\" right?

So, [Freeze](Freeze) will now have a place on the net: right here.

Score 1 for wiki. ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}

\-- [LionKimbro](LionKimbro) 2004-08-30 03:43:57

Why dont you make one yourself, it\'s probably not that hard\... \-- *anon*

\"probably\"? Anon sounds like an optimist. \-- [RetrogradeOrbit](RetrogradeOrbit)

One other idea, still playing around with it, is pyinstaller. [http://www.pyinstaller.org/](http://www.pyinstaller.org/){.http}. If you want a GUI for it, try [PythonCard](./PythonCard.html){.nonexistent} [StandAloneBuilder](./StandAloneBuilder.html){.nonexistent}, [http://www.linux2000.org/pm.html](http://www.linux2000.org/pm.html){.http}. Seems like there might be some bugs, but some things seem to work seamlessly. \--Alestan

\-- hipersayan_x 2009-12-22 12:34:00

is it possible to get py2exe to run on linux? I only have a linux pc and my client does not want python installed on all of there computers.

\-- [CyberKing](./CyberKing.html){.nonexistent} 2010-04-07 11:03:00

About:

[http://bugs.winehq.org/show_bug.cgi?id=3591](http://bugs.winehq.org/show_bug.cgi?id=3591){.http}

Try using Teleport Me Now! to create portable programs from Linux to Windows with wine.

[https://sourceforge.net/projects/tpmn/](https://sourceforge.net/projects/tpmn/){.https}

Is Alpha but it work fine. Here you have an real example of use:

[http://sushi-huh.sourceforge.net](http://sushi-huh.sourceforge.net){.http} \-- *anonymous*

It IS possible to create working executables with py2exe under Linux. I do create setups of fairly complex programs which use PyGTK and which depend on modules which are also compiled on Linux with MinGW ( ie. I do create windows setups on a 100% pure Linux system ). The one real hack I needed to do this is to call PETools for each created binary to fix the image size header field ( in PETools: \"Optional Header\"-\>\"Size Of Image\". Press \"?\" there and it will correct the size ), otherwise the application won\'t run. I use [InnoSetup](./InnoSetup.html){.nonexistent} under wine to create an actual setup. \-- *Arne Caspari*
:::
