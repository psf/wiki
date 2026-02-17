# When I import Tkinter, Python exits.  Why?

::: {#content dir="ltr" lang="en"}
When I import Tkinter, Python exits. Why?

[lwickjr](lwickjr): Several possibilities suggest themselves:

\* You don\'t have [tk](./tk.html){.nonexistent} properly installed.

\* Your version of Python doesn\'t have tk support enabled.

More information is needed:

\* Are you importing [tkinter](./tkinter.html){.nonexistent} from plain [Python](Python), or from [I.D.L.E.](./I(2e)D(2e)L(2e)E(2e).html){.nonexistent}?

\* What else is going on when you try this?

Anyone have any other ideas?

I also have a similar problem.

Traceback (most recent call last):

- File \"C:\\Python23\\scripts\\test.py\", line 1, in -toplevel-
  - from TKinter import \*

[ImportError](./ImportError.html){.nonexistent}: No module named TKinter

*Check your spelling: it\'s Tkinter, not Tkinter. Python\'s a case-sensitive language.*

I have just installed the Python executable on Win2K. Here is the info from the IDLE GUI: Python 2.3.4 (#53, May 25 2004, 21:17:02) \[MSC v.1200 32 bit (Intel)\] on win32.

I also installed the same version of Python on a Win98 system and I do not have this problem. TK inter was selected during the installation, so I assume it was installed, but I don\'t know how to confirm it.

Any help would be appresiciated.

[lwickjr](lwickjr): Does I.D.L.E. work? If so, tk definitely was installed.

------------------------------------------------------------------------

I\'d go ask on [the TkInter wiki.](http://tkinter.unpythonic.net/wiki/){.http} \-- [LionKimbro](LionKimbro) 2004-09-02 20:03:43
:::
