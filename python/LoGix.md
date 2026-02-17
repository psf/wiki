# LoGix

::: {#content dir="ltr" lang="en"}
A front-end to Python that has powerful macro capabilities.

[http://livelogix.net/logix/](http://livelogix.net/logix/){.http} For example, adding an \"isa\" operator:

    [base]: defop 50 expr "isa" expr func ob typ:
          :     return isinstance(ob, typ)

    [base]: 'a' isa str
    True

------------------------------------------------------------------------

See also: [BooLanguage](BooLanguage), [IronPython](IronPython)
:::
