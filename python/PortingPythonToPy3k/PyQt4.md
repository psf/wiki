# PortingPythonToPy3k/PyQt4

::: {#content dir="ltr" lang="en"}
# PyQt 4.6+ {#PyQt_4.6.2B-}

[PyQt](PyQt)-4.6 and greater have a new API called API2 that is the default when run on Python-3.x. The major difference is that QString does not exist in API2; the library uses the native Python3 str type instead.

To keep your code similar on both python3 and python2, you probably want to pick either the old or the new API and then have your code explicitly use that like so:

To pick the old API:

    import sip
    sip.setapi('QString', 1)

    from PyQt4 import QtCore

    # This works as the old API has QString
    print(QtCore.QString)

To use API2 everywhere:

    import sip
    sip.setapi('QString', 2)

    from PyQt4 import QtCore

    # Now QtCore.QString is no longer available -- use python2's unicode type or python3's str type instead

From the [pyqt4 reference manual](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html#selecting-incompatible-apis){.http}
:::
