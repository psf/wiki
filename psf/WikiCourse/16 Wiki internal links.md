# WikiCourse/16 Wiki internal links

::: {#content dir="ltr" lang="en"}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiCourse(2f)16(20)Wiki(20)internal(20)links.html?action=print&media=projection) [\^](WikiCourse) [\|\<](./WikiCourse(2f)01(20)What(20)is(20)a(20)MoinMoin(20)wiki(3f).html) [\<\<](./WikiCourse(2f)15(20)Tables.html) Slide 15 of 27 [\>\>](./WikiCourse(2f)17(20)External(20)links.html) [\>\|](./WikiCourse(2f)52(20)Structure(20)in(20)the(20)wiki.html)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Wiki internal links {#Wiki_internal_links}

One of the most important features of the wiki is the internal linking to other wiki pages, therefore it is quite simple.

## WikiNames (\"CamelCase\") {#WikiNames_.28.22CamelCase.22.29}

If you WriteWordsTogether like FistnameLastname or [CamelCase](CamelCase) or [MoinMoin](MoinMoin), so that there are at least two changes between capital letters and lower case letters, [MoinMoin](MoinMoin) will automatically link this word to the page of the same name.

This is quite simple, because wiki markup isn\'t necessary. But the unusual syntax isn\'t everyone\'s cup of tea, so there is one more alternative, the so-called \"free link\".

### Input {#Input}

    CamelCase !CamelCaseButNotLinked

### Display {#Display}

[CamelCase](CamelCase) CamelCaseButNotLinked

## Free links {#Free_links}

If you want to link pages, which aren\'t in [CamelCase](CamelCase) or if you just don\'t like [CamelCase](CamelCase), you can also link this way:

### Input {#Input-1}

    A [[free link]] and [[other page|another page]].

### Display {#Display-1}

A [free link](./free(20)link.html){.nonexistent} and [another page](./other(20)page.html){.nonexistent}.

# Tracing backwards from links {#Tracing_backwards_from_links}

If you click on the page name in the navigation area, the wiki looks for pages which link to this page name.

This can be used for so-called wiki badges. You just write somewhere:

[ToDo](./ToDo.html){.nonexistent}: Call costumer foobar regarding \...

[ToDo](./ToDo.html){.nonexistent} is [CamelCase](CamelCase), so it links to a homonymous page, which isn\'t very exciting. ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}

![(!)](/wiki/europython/img/idea.png "(!)"){height="16" width="16"} But you can click on the page name on the page [ToDo](./ToDo.html){.nonexistent} and lo and behold, you find every page that also includes a [ToDo](./ToDo.html){.nonexistent}.
:::
