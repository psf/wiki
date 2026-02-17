# SyntaxReference

::::::::::::::::: {#content dir="ltr" lang="en"}
This page aims to introduce the most important elements of [MoinMoin](MoinMoin)\'s syntax at a glance, showing first the markup verbatim and then how it is rendered by the wiki engine. Additionally, you\'ll find links to the relative help pages. Please note that some of the features depend on your configuration.

# Table of Contents {#Table_of_Contents}

    '''Contents''' (up to the 2nd level)
    <<TableOfContents(2)>>

**Contents** (up to the 2nd level)

::: table-of-contents
Contents

1.  [Table of Contents](#Table_of_Contents)
2.  [Headings](#Headings)
3.  [heading 1st level](#heading_1st_level)
    1.  [heading 2nd level](#heading_2nd_level)
4.  [Text Formatting](#Text_Formatting)
5.  [Hyperlinks](#Hyperlinks)
    1.  [Internal Links](#Internal_Links)
    2.  [External Links](#External_Links)
    3.  [Avoid or Limit Automatic Linking](#Avoid_or_Limit_Automatic_Linking)
6.  [Drawings](#Drawings)
7.  [Blockquotes and Indentations](#Blockquotes_and_Indentations)
8.  [Lists](#Lists)
    1.  [Unordered Lists](#Unordered_Lists)
    2.  [Ordered Lists](#Ordered_Lists)
    3.  [Definition Lists](#Definition_Lists)
9.  [Horizontal Rules](#Horizontal_Rules)
10. [Tables](#Tables)
    1.  [Tables](#Tables-1)
    2.  [Cell Width](#Cell_Width)
    3.  [Spanning Rows and Columns](#Spanning_Rows_and_Columns)
    4.  [Alignment of Cell Contents](#Alignment_of_Cell_Contents)
    5.  [Coloured Table Cells](#Coloured_Table_Cells)
    6.  [HTML-like Options for Tables](#HTML-like_Options_for_Tables)
11. [Macros and Variables](#Macros_and_Variables)
    1.  [Macros](#Macros)
    2.  [Variables](#Variables)
12. [Smileys and Icons](#Smileys_and_Icons)
13. [Parsers](#Parsers)
    1.  [Verbatim Display](#Verbatim_Display)
    2.  [Syntax Highlighting](#Syntax_Highlighting)
    3.  [Using the wiki parser with css classes](#Using_the_wiki_parser_with_css_classes)
14. [Admonitions](#Admonitions)
15. [Comments](#Comments)
:::

# Headings {#Headings}

***see:** [HelpOnHeadlines](HelpOnHeadlines)*

    = heading 1st level =
    == heading 2nd level ==
    === heading 3rd level ===
    ==== heading 4th level ====
    ===== heading 5th level =====

# heading 1st level {#heading_1st_level}

## heading 2nd level {#heading_2nd_level}

### heading 3rd level {#heading_3rd_level}

#### heading 4th level {#heading_4th_level}

##### heading 5th level {#heading_5th_level}

# Text Formatting {#Text_Formatting}

***see:** [HelpOnFormatting](HelpOnFormatting)*

     * ''emphasized (italics)''
     * '''boldface'''
     * '''''bold italics'''''
     * `monospace`
     * {{{source code}}}
     * __underline__
     * ,,sub,,script
     * ^super^script
     * ~-smaller-~
     * ~+larger+~
     * --(strike through)--

- *emphasized (italics)*

- **boldface**

- ***bold italics***

- `monospace`{.backtick}

- `source code`

- [underline]{.u}

- ~sub~script

- ^super^script

- [smaller]{.small}

- larger

- [strike through]{.strike}

# Hyperlinks {#Hyperlinks}

***see:** [HelpOnLinking](HelpOnLinking)*

## Internal Links {#Internal_Links}

     * FrontPage
     * [[FrontPage]]
     * HelpOnEditing/SubPages
     * /SubPage
     * ../SiblingPage
     * [[FrontPage|named link]]
     * [[#anchorname]]
     * [[#anchorname|description]]
     * [[PageName#anchorname]]
     * [[PageName#anchorname|description]]
     * [[attachment:filename.txt]]

- [FrontPage](FrontPage)

- [FrontPage](FrontPage)

- [HelpOnEditing/SubPages](./HelpOnEditing(2f)SubPages.html)

- [/SubPage](./SyntaxReference(2f)SubPage.html){.nonexistent}

- [../SiblingPage](./SiblingPage.html){.nonexistent}

- [named link](FrontPage)

- [#anchorname](SyntaxReference#anchorname)

- [description](SyntaxReference#anchorname)

- [PageName#anchorname](./PageName.html#anchorname){.nonexistent}

- [description](./PageName.html#anchorname){.nonexistent}

- [filename.txt]( "Upload new attachment "filename.txt""){.attachment .nonexistent}

## External Links {#External_Links}

     * http://moinmo.in/
     * [[http://moinmo.in/]]
     * [[http://moinmo.in/|MoinMoin Wiki]]
     * [[http://static.moinmo.in/logos/moinmoin.png]]
     * {{http://static.moinmo.in/logos/moinmoin.png}}
     * [[http://static.moinmo.in/logos/moinmoin.png|moinmoin.png]]
     * MeatBall:InterWiki
     * [[MeatBall:InterWiki|InterWiki page on MeatBall]]
     * [[file://///servername/share/full/path/to/file/filename%20with%20spaces.txt|link to file filename with spaces.txt]]
     * user@example.com

- [http://moinmo.in/](http://moinmo.in/){.http}

- [http://moinmo.in/](http://moinmo.in/){.http}

- [MoinMoin Wiki](http://moinmo.in/){.http}

- [http://static.moinmo.in/logos/moinmoin.png](http://static.moinmo.in/logos/moinmoin.png){.http}

- ![](http://static.moinmo.in/logos/moinmoin.png "http://static.moinmo.in/logos/moinmoin.png"){.external_image}

- [moinmoin.png](http://static.moinmo.in/logos/moinmoin.png){.http}

- [InterWiki](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall"){.interwiki}

- [InterWiki page on MeatBall](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall"){.interwiki}

- [link to file filename with spaces.txt](file://///servername/share/full/path/to/file/filename%20with%20spaces.txt){.file}

- [user@example.com](mailto:user@example.com){.mailto}

## Avoid or Limit Automatic Linking {#Avoid_or_Limit_Automatic_Linking}

     * Wiki''''''Name
     * Wiki``Name
     * !WikiName
     * WikiName''''''s
     * WikiName``s
     * `http://www.example.com`
     * [[http://www.example.com/]]notlinked

- WikiName

- WikiName

- WikiName

- [WikiName](WikiName)s

- [WikiName](WikiName)s

- `http://www.example.com`{.backtick}

- [http://www.example.com/](http://www.example.com/){.http}notlinked

# Drawings {#Drawings}

- [![myexample.tdraw](./SyntaxReference.html?action=AttachFile&do=box&target=myexample.tdraw&member=drawing.png "myexample.tdraw"){.drawing}](attachments/SyntaxReference/myexample.tdraw)

# Blockquotes and Indentations {#Blockquotes_and_Indentations}

     indented text
      text indented to the 2nd level

- indented text
  - text indented to the 2nd level

# Lists {#Lists}

***see:** [HelpOnLists](HelpOnLists)*

## Unordered Lists {#Unordered_Lists}

     * item 1

     * item 2 (preceding white space)
      * item 2.1
       * item 2.1.1
     * item 3
      . item 3.1 (bulletless)
     . item 4 (bulletless)
      * item 4.1
       . item 4.1.1 (bulletless)

- item 1
- item 2 (preceding white space)
  - item 2.1
    - item 2.1.1
- item 3
  - item 3.1 (bulletless)
- item 4 (bulletless)
  - item 4.1
    - item 4.1.1 (bulletless)

## Ordered Lists {#Ordered_Lists}

### with Numbers {#with_Numbers}

     1. item 1
       1. item 1.1
       1. item 1.2
     1. item 2

1.  item 1
    1.  item 1.1
    2.  item 1.2
2.  item 2

### with Roman Numbers {#with_Roman_Numbers}

     I. item 1
       i. item 1.1
       i. item 1.2
     I. item 2

I.  item 1
    i.  item 1.1
    ii. item 1.2
II. item 2

### with Letters {#with_Letters}

     A. item A
       a. item A. a)
       a. item A. b)
     A. item B

A.  item A
    a.  item A. a)
    b.  item A. b)
B.  item B

## Definition Lists {#Definition_Lists}

     term:: definition
     object::
     :: description 1
     :: description 2

term
:   definition

object

:   

:   description 1

:   description 2

# Horizontal Rules {#Horizontal_Rules}

***see:** [HelpOnRules](HelpOnRules)*

    ----
    -----
    ------
    -------
    --------
    ---------
    ----------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

# Tables {#Tables}

***see:** [HelpOnTables](HelpOnTables)*

## Tables {#Tables-1}

    ||'''A'''||'''B'''||'''C'''||
    ||1      ||2      ||3      ||

::: {}
  ------- ------- -------
  **A**   **B**   **C**
  1       2       3
  ------- ------- -------
:::

## Cell Width {#Cell_Width}

    ||minimal width ||<99%>maximal width ||

::: {}
  --------------- ---------------
  minimal width   maximal width
  --------------- ---------------
:::

## Spanning Rows and Columns {#Spanning_Rows_and_Columns}

    ||<|2> cell spanning 2 rows ||cell in the 2nd column ||
    ||cell in the 2nd column of the 2nd row ||
    ||<-2> cell spanning 2 columns ||
    ||||use empty cells as a shorthand ||

::: {}
+:--------------------:+--------------------------------------:+
| cell spanning 2 rows | cell in the 2nd column                |
|                      +---------------------------------------+
|                      | cell in the 2nd column of the 2nd row |
+----------------------+---------------------------------------+
| cell spanning 2 columns                                      |
+--------------------------------------------------------------+
| use empty cells as a shorthand                               |
+--------------------------------------------------------------+
:::

## Alignment of Cell Contents {#Alignment_of_Cell_Contents}

    ||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||
    ||<)> right ||
    ||<(> left ||

::: {}
+:--------------:+:-----------------:+:-----------------:+
| top (combined) | center (combined) | bottom (combined) |
|                +-------------------+                   |
|                | right             |                   |
|                +-------------------+                   |
|                | left              |                   |
+----------------+-------------------+-------------------+
:::

## Coloured Table Cells {#Coloured_Table_Cells}

    ||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||
    ||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||

::: {}
  ------ --------- --------
  blue   green     red
  cyan   magenta   yellow
  ------ --------- --------
:::

## HTML-like Options for Tables {#HTML-like_Options_for_Tables}

    ||A ||<rowspan="2"> like <|2> ||
    ||<bgcolor="#00FF00"> like <#00FF00> ||
    ||<colspan="2"> like <-2>||

::: {}
+------------------+--------------+
| A                | like \<\|2\> |
+------------------+              |
| like \<#00FF00\> |              |
+------------------+--------------+
| like \<-2\>                     |
+---------------------------------+
:::

# Macros and Variables {#Macros_and_Variables}

## Macros {#Macros}

***see:** [HelpOnMacros](HelpOnMacros)*

- `<<Anchor(anchorname)>>`{.backtick} inserts a link anchor `anchorname`{.backtick}

- `<<BR>>`{.backtick} inserts a hard line break

- `<<FootNote(Note)>>`{.backtick} inserts a footnote saying `Note`{.backtick}

- `<<Include(HelpOnMacros/Include)>>`{.backtick} inserts the contents of the page `HelpOnMacros/Include`{.backtick} inline

- `<<MailTo(user AT example DOT com)>>`{.backtick} obfuscates the email address `user@example.com`{.backtick} to users not logged in

## Variables {#Variables}

***see:** [HelpOnVariables](HelpOnVariables)*

- `@`{.backtick}`SIG`{.backtick}`@`{.backtick} inserts your login name and timestamp of modification

- `@`{.backtick}`TIME`{.backtick}`@`{.backtick} inserts date and time of modification

# Smileys and Icons {#Smileys_and_Icons}

***see:** [HelpOnSmileys](HelpOnSmileys)*

:::: {}
::: {}
  ------------ --------------------------------------------------------------------------- -- ------------ -------------------------------------------------------------------------- -- ------------ ---------------------------------------------------------------------------- -- ------------ ----------------------------------------------------------------------------
  **Markup**   **Display**                                                                    **Markup**   **Display**                                                                   **Markup**   **Display**                                                                     **Markup**   **Display**
  `X-(`        ![X-(](/wiki/europython/img/angry.png "X-("){height="16" width="16"}           `:D`         ![:D](/wiki/europython/img/biggrin.png ":D"){height="16" width="16"}          `<:(`        ![\<:(](/wiki/europython/img/frown.png "<:("){height="16" width="16"}           `:o`         ![:o](/wiki/europython/img/redface.png ":o"){height="16" width="16"}
  `:(`         ![:(](/wiki/europython/img/sad.png ":("){height="16" width="16"}               `:)`         ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}            `B)`         ![B)](/wiki/europython/img/smile2.png "B)"){height="16" width="16"}             `:))`        ![:))](/wiki/europython/img/smile3.png ":))"){height="16" width="16"}
  `;)`         ![;)](/wiki/europython/img/smile4.png ";)"){height="16" width="16"}            `/!\`        ![/!\\](/wiki/europython/img/alert.png "/!\"){height="16" width="16"}         `<!>`        ![\<!\>](/wiki/europython/img/attention.png "<!>"){height="16" width="16"}      `(!)`        ![(!)](/wiki/europython/img/idea.png "(!)"){height="16" width="16"}
  `:-?`        ![:-?](/wiki/europython/img/tongue.png ":-?"){height="16" width="16"}          `:\`         ![:\\](/wiki/europython/img/ohwell.png ":\"){height="16" width="16"}          `>:>`        ![\>:\>](/wiki/europython/img/devil.png ">:>"){height="16" width="16"}          `|)`         ![\|)](/wiki/europython/img/tired.png "|)"){height="16" width="16"}
  `:-(`        ![:-(](/wiki/europython/img/sad.png ":-("){height="16" width="16"}             `:-)`        ![:-)](/wiki/europython/img/smile.png ":-)"){height="16" width="16"}          `B-)`        ![B-)](/wiki/europython/img/smile2.png "B-)"){height="16" width="16"}           `:-))`       ![:-))](/wiki/europython/img/smile3.png ":-))"){height="16" width="16"}
  `;-)`        ![;-)](/wiki/europython/img/smile4.png ";-)"){height="16" width="16"}          `|-)`        ![\|-)](/wiki/europython/img/tired.png "|-)"){height="16" width="16"}         `(./)`       ![(./)](/wiki/europython/img/checkmark.png "(./)"){height="16" width="16"}      `{OK}`       ![{OK}](/wiki/europython/img/thumbs-up.png "{OK}"){height="16" width="16"}
  `{X}`        ![{X}](/wiki/europython/img/icon-error.png "{X}"){height="16" width="16"}      `{i}`        ![{i}](/wiki/europython/img/icon-info.png "{i}"){height="16" width="16"}      `{1}`        ![{1}](/wiki/europython/img/prio1.png "{1}"){height="13" width="15"}            `{2}`        ![{2}](/wiki/europython/img/prio2.png "{2}"){height="13" width="15"}
  `{3}`        ![{3}](/wiki/europython/img/prio3.png "{3}"){height="13" width="15"}           `{*}`        ![{\*}](/wiki/europython/img/star_on.png "{*}"){height="16" width="16"}       `{o}`        ![{o}](/wiki/europython/img/star_off.png "{o}"){height="16" width="16"}                       
  ------------ --------------------------------------------------------------------------- -- ------------ -------------------------------------------------------------------------- -- ------------ ---------------------------------------------------------------------------- -- ------------ ----------------------------------------------------------------------------
:::
::::

# Parsers {#Parsers}

***see:** [HelpOnParsers](HelpOnParsers)*

## Verbatim Display {#Verbatim_Display}

    {{{
    def hello():
        print "Hello World!"
    }}}

    def hello():
        print "Hello World!"

## Syntax Highlighting {#Syntax_Highlighting}

    {{{#!python
    def hello():
        print "Hello World!"
    }}}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-78c687fbb04d58d5ee5c7f64fd6654a3595f0c88 dir="ltr" lang="en"}
   1 def hello():
   2     print "Hello World!"
```
:::
::::

## Using the wiki parser with css classes {#Using_the_wiki_parser_with_css_classes}

    {{{#!wiki red/solid
    This is wiki markup in a '''div''' with __css__ `class="red solid"`.
    }}}

::: {.red .solid}
This is wiki markup in a **div** with [css]{.u} `class="red solid"`{.backtick}.
:::

# Admonitions {#Admonitions}

***see:** [HelpOnAdmonitions](HelpOnAdmonitions)*

    {{{#!wiki caution
    '''Don't overuse admonitions'''

    Admonitions should be used with care. A page riddled with admonitions will look restless and will be harder to follow then a page where admonitions are used sparingly.
    }}}

::: caution
**Don\'t overuse admonitions**

Admonitions should be used with care. A page riddled with admonitions will look restless and will be harder to follow then a page where admonitions are used sparingly.
:::

# Comments {#Comments}

***see:** [HelpOnComments](HelpOnComments)*

    Click on "Comments" in edit bar to toggle the /* comments */ visibility.

Click on \"Comments\" in edit bar to toggle the [comments]{.comment style="display:none"} visibility.

    {{{#!wiki comment/dotted
    This is a wiki parser section with class "comment dotted" (see HelpOnParsers).

    Its visibility gets toggled the same way.
    }}}

::: {.comment .dotted style="display:none"}
This is a wiki parser section with class \"comment dotted\" (see [HelpOnParsers](HelpOnParsers)).

Its visibility gets toggled the same way.
:::
:::::::::::::::::
