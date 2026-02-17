# SpeedUp2to3PatternMatching

::: {#content dir="ltr" lang="en"}
The largest part of the the [2to3](http://wiki.python.org/moin/2to3){.http} runtime is spent in the pattern matching algorithm. This currently uses a fairly naive back-tracking approach. Replacing it with an algorithm based on the computation of finite state machines out of the patterns should allow efficient simultaneous matching of patterns with many alternatives. Interested students should contact [martin@v.loewis.de](mailto:martin@v.loewis.de){.mailto}.
:::
