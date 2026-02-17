# LocalNamesDescription

::: {#content dir="ltr" lang="en"}
I hope nobody minds; This is an experimental description of the wiki\'s space using [\"Local Names.\"](http://onebigsoup.wiki.taoriver.net/moin.cgi/LocalNamesBasics){.http}

This is so that people can link into this space (and other spaces) conveniently and automatically with some tools.

If it\'s any consolation, the tools happen to be written in Python. ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}

# Discussion {#Discussion}

Please keep comments here, above the description section. \-- [LionKimbro](LionKimbro) 2004-07-06 23:39:32

# Description {#Description}

      http://purl.net/net/localnames/

This page is accessed by: [http://www.python.org/cgi-bin/moinmoin/LocalNamesDescription?action=raw](http://www.python.org/cgi-bin/moinmoin/LocalNamesDescription?action=raw){.http}

See [LocalNamesBasics](http://onebigsoup.wiki.taoriver.net/moin.cgi/LocalNamesBasics){.http} and [LocalNamesFormat](http://onebigsoup.wiki.taoriver.net/moin.cgi/LocalNamesFormat){.http} for more information.

      NamesListPattern http://www.python.org/cgi-bin/moinmoin/$NAME
      NamesList http://www.python.org/cgi-bin/moinmoin/TitleIndex?action=titleindex
      KeyValue INVALIDATE-UPON-CHANGE-TO http://www.python.org/cgi-bin/moinmoin/LocalNamesDescription
      KeyValue ACCEPT-ADDITION-BY-FORM http://www.python.org/cgi-bin/moinmoin/$NAME

      OtherNameSpaces
        LibraryReference http://www.python.org/cgi-bin/moinmoin/LibraryReferencesNames?action=raw
        LibRef http://www.python.org/cgi-bin/moinmoin/LibraryReferencesNames?action=raw
        Modules http://www.python.org/cgi-bin/moinmoin/LibraryReferencesNames?action=raw

      DefaultNameSpaces
        LibraryReference

INVALIDATE-UPON-CHANGE-TO: Means if a local nameserver somehow hears that the given URL has changed, to invalidate it\'s cache of the namespace.

ACCEPT-ADDITION-BY-FORM: Means if a local nameserver somehow hears that a URL has been added of the given form, to add it to the namespace description.

      LastResortNamePattern http://www.python.org/cgi-bin/moinmoin/$NAME
:::
