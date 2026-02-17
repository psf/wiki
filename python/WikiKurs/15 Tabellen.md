# WikiKurs/15 Tabellen

::: {#content dir="ltr" lang="de"}
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiKurs(2f)15(20)Tabellen.html?action=print&media=projection) [\^](WikiKurs) [\|\<](./WikiKurs(2f)01(20)Was(20)ist(20)ein(20)MoinMoin(2d)Wiki(3f).html) [\<\<](./WikiKurs(2f)14(20)Text(2d)Stil.html) Slide 14 of 27 [\>\>](./WikiKurs(2f)16(20)Wiki(2d)interne(20)Links.html) [\>\|](./WikiKurs(2f)52(20)Struktur(20)im(20)Wiki.html)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tabellen {#Tabellen}

## Einfachste Tabelle {#Einfachste_Tabelle}

     || eins || zwei || drei ||
     || vier || fünf || sechs ||

- ::: {}
    ------ ------ -------
    eins   zwei   drei
    vier   fünf   sechs
    ------ ------ -------
  :::

## Allgemeines Tabellen-Layout {#Allgemeines_Tabellen-Layout}

     ||||||<tablewidth="80%">'''Kopfzeile'''||
     ||Zelle 1||Zelle 2||Zelle 3||
     ||<rowspan=2> Zeilen-übergreifend||||<bgcolor="#AAAAFF"> 2 Spalten übergreifend||
     ||<rowbgcolor="#FFFFAA">Zelle 2||Zelle 3||

- ::: {}
  +:-------------------:+:-----------:+:-----------:+
  | **Kopfzeile**                                   |
  +---------------------+-------------+-------------+
  | Zelle 1             | Zelle 2     | Zelle 3     |
  +---------------------+-------------+-------------+
  | Zeilen-übergreifend | 2 Spalten übergreifend    |
  |                     +-------------+-------------+
  |                     | Zelle 2     | Zelle 3     |
  +---------------------+-------------+-------------+
  :::

## Zellenbreite {#Zellenbreite}

     || schmal ||<:99%> breit ||

- ::: {}
    -------- -------
    schmal    breit
    -------- -------
  :::

## Übergreifende Zeilen und Spalten {#A.2BANw-bergreifende_Zeilen_und_Spalten}

     ||<|2> 2 Zeilen || Zeile 1 ||
     || Zeile 2 ||
     ||<-2> Zeile 3, 2 Spalten übergreifend ||

- ::: {}
  +:----------------:+-----------------:+
  | 2 Zeilen         | Zeile 1          |
  |                  +------------------+
  |                  | Zeile 2          |
  +------------------+------------------+
  | Zeile 3, 2 Spalten übergreifend     |
  +-------------------------------------+
  :::

## Ausrichtung {#Ausrichtung}

     ||<(50%> links ||<^|3> oben ||<v|3> unten ||
     ||<:> mittig ||
     ||<)> rechts ||

- ::: {}
  +:-------+:----:+:-----:+
  | links  | oben | unten |
  +--------+      |       |
  | mittig |      |       |
  +--------+      |       |
  | rechts |      |       |
  +--------+------+-------+
  :::

## Farben {#Farben}

     ||<#FF0000> rot ||<#00FF00> grün ||<#0000FF> blau ||

- ::: {}
    ----- ------ ------
    rot   grün   blau
    ----- ------ ------
  :::
:::
