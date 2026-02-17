# MementoPattern

::::: {#content dir="ltr" lang="en"}
The memento pattern is defined on [wikipedia](http://en.wikipedia.org/wiki/Memento_pattern){.http}, and discussed on Ward\'s wiki under \[[MementoPattern](http://c2.com/cgi/wiki?MementoPattern "Wiki"){.interwiki}\].

The core intent is to capture an object\'s internal state (for later restoration) *without* violating encapsulation (i.e. uncovering internals for the purpose of externalization). Therefore, the state-representing object - called the *memento* - should satisfy 2 criteria:

1.  The memento should be opaque (aka provide no insight)
2.  The only allowed action with a memento is to return it to its originator for the purpose of state restoration. (This one may be relaxed in some variants to allow passing of states between sibling instances.)

Memento is extremely useful with transactional processing semantics, i.e. when an action is expected to either *entirely* succeed and change the system state in a *defined* way, or, on failure, *not* to change the system state at all.

A [MementoClosure](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/413838){.http} is a generic python implementation of the memento pattern. An example how to use the memento closure follows:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a22bc921990788f7dbe96368f3825cb6a1599b9d dir="ltr" lang="en"}
   1 # Perform a bunch of actions on object obj,
   2 # rollback to prior state on errors
   3 state = Memento(obj)
   4 try:
   5    obj.DoThis()
   6    obj.DoThat()
   7    myBigTransformer.Transform(obj)
   8 except:
   9    state() # restore captured state to obj
  10    raise   # re-raise exception knowing system state has not changed
```
:::
::::

## Discussion {#Discussion}
:::::
