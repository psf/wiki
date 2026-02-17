# WikiKurs/16 Wiki-interne Links

::: {#content dir="ltr" lang="de"}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiKurs(2f)16(20)Wiki(2d)interne(20)Links.html?action=print&media=projection) [\^](WikiKurs) [\|\<](./WikiKurs(2f)01(20)Was(20)ist(20)ein(20)MoinMoin(2d)Wiki(3f).html) [\<\<](./WikiKurs(2f)15(20)Tabellen.html) Slide 15 of 27 [\>\>](./WikiKurs(2f)17(20)Externe(20)Links.html) [\>\|](./WikiKurs(2f)52(20)Struktur(20)im(20)Wiki.html)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Wiki-interne Links {#Wiki-interne_Links}

Eine der wichtigsten Funktionen im Wiki ist das Verlinken auf andere Wiki-Seiten - deshalb geht dies auch sehr einfach.

## WikiNamen (\"CamelCase\") {#WikiNamen_.28.22CamelCase.22.29}

Wenn man WorteZusammenschreibt wie z.B. bei VornameNachname oder [CamelCase](CamelCase) oder [MoinMoin](MoinMoin), so dass in einem Wort mindestens 2 Wechsel Großbuchstabe-Kleinbuchstabe(n) vorkommen, so verlinkt [MoinMoin](MoinMoin) dieses Wort automatisch zu der gleichnamigen Seite.

Dies geht sehr einfach, es ist kein Wiki-Markup notwendig. Aber die ungewöhnliche Schreibweise ist nicht jedermanns Sache, daher gibt es eine weitere Alternative, die sog. \"free links\".

### Eingabe {#Eingabe}

    CamelCase !CamelCaseAberNichtVerlinkt

### Anzeige {#Anzeige}

[CamelCase](CamelCase) CamelCaseAberNichtVerlinkt

## Freie Links {#Freie_Links}

Möchte man Seiten verlinken, die nicht [CamelCase](CamelCase) sind oder wenn man einfach kein [CamelCase](CamelCase) mag, kann man wie folgt verlinken:

### Eingabe {#Eingabe-1}

    Ein [[freier Link]] und [[andere Seite|eine andere Seite]].

### Anzeige {#Anzeige-1}

Ein [freier Link](./freier(20)Link.html){.nonexistent} und [eine andere Seite](./andere(20)Seite.html){.nonexistent}.

# Rückwärtsverfolgung von Links {#R.2BAPw-ckw.2BAOQ-rtsverfolgung_von_Links}

Wenn man auf den Seitennamen im Navigationsbereich klickt, sucht das Wiki nach Seiten, die auf diesen Seitennamen verlinken.

Dies wird z.B. für sogenannte Wiki-Badges (Wiki-Sticker) verwendet. Man schreibt einfach irgendwo hin:

[ToDo](./ToDo.html){.nonexistent}: Kunden XY zurückrufen wegen \...

[ToDo](./ToDo.html){.nonexistent} ist [CamelCase](CamelCase) und verlinkt daher auf eine gleichnamige Seite, was nicht weiter aufregend ist. ![:)](/wiki/modernized/img/smile.png ":)"){height="16" width="16"}

Man kann aber auf der Seite [ToDo](./ToDo.html){.nonexistent} einfach auf den Seitennamen klicken und siehe da, man findet alle Seiten, auf denen es noch irgendetwas \"zu tun\" gibt! ![(!)](/wiki/modernized/img/idea.png "(!)"){height="16" width="16"}
:::
