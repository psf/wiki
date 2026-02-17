# ProfileReplacementProject

::: {#content dir="ltr" lang="en"}
\"If you\'re looking for a moderate size self-contained task, writing a replacement for the profile and pstats modules that worked directly with hotshot data would be a nice little project. Right now, to use hotshot data, you have to load it up and turn it into profile-compatible data - for any decent amount of data, this takes a \_lot\_ of time. Plus, the existing profiler API is extremely unpythonic.\"

So said Anthony Baxter.

Note that a patch for an alternate profiler already exists: [patch #1212837](http://sourceforge.net/tracker/index.php?func=detail&aid=1212837&group_id=5470&atid=305470){.http}.

A replacement stats module that worked directly with hotshot would also solve the licensing issues with profile.py and pstats.py.
:::
