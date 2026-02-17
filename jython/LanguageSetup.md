# LanguageSetup

:::::::: {#content dir="ltr" lang="en"}
# Welcome {#Welcome}

::: {}
+:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+:---------------------------------------------------------------------------------:+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![(./)](/wiki/modernized/img/checkmark.png "(./)"){height="16" width="16"} ![/!\\](/wiki/modernized/img/alert.png "/!\"){height="16" width="16"} ![\<!\>](/wiki/modernized/img/attention.png "<!>"){height="16" width="16"} | If you have just installed or upgraded your wiki you are not in the wrong place.\ | ![\<!\>](/wiki/modernized/img/attention.png "<!>"){height="16" width="16"} ![/!\\](/wiki/modernized/img/alert.png "/!\"){height="16" width="16"} ![(./)](/wiki/modernized/img/checkmark.png "(./)"){height="16" width="16"} |
|                                                                                                                                                                                                                             | Just read the informations given below.                                           |                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

## System and Help Page Package installation {#System_and_Help_Page_Package_installation}

MoinMoin comes with no system and help pages installed by default (the page you read right now is the only page after a fresh installation).

### Becoming superuser {#Becoming_superuser}

For installation of the language packages, it is required that you are superuser:

1.  If you do not already have an account, create one (see hints on the login page).

2.  If the wiki is not already configured to recognize you as a superuser, change wiki config appropriately:

            superuser = [u"YourLoginName", ]

    See [HelpOnConfiguration](http://master.moinmo.in/HelpOnConfiguration "MoinMaster"){.interwiki} for more details.

3.  Restart the wiki to make it load the changed configuration.

4.  Login in (with the login name you configured as superuser).

### Installing page packages {#Installing_page_packages}

You can install help and system page packages for any language you want to support for your wiki users. You should see links for each supported language, and below an **install** link for each page package of that language --- click on it for each of the packages you wish to install. When you\'re finished, restart the wiki (otherwise it won\'t recognize the newly installed pages correctly).

![/!\\](/wiki/modernized/img/alert.png "/!\"){height="16" width="16"} Make sure you at least install the essential system page package for the `language_default`{.backtick} you might have configured (the default for this setting is `en`{.backtick}, i.e English). Note however that if you don\'t install the whole page set, the installed pages may contain broken links to the non-installed.

![/!\\](/wiki/modernized/img/alert.png "/!\"){height="16" width="16"} If you want to use translated categories and templates, after installing their corresponding pages you still need to update your `page_category_regex`{.backtick} and `page_template_regex`{.backtick} configs to match the translated page names. See [HelpOnConfiguration](http://master.moinmo.in/HelpOnConfiguration "MoinMaster"){.interwiki} and [http://moinmo.in/ConfigMarket](http://moinmo.in/ConfigMarket){.http} for more details.

## FrontPage configuration {#FrontPage_configuration}

For the root URL of your wiki, moin will use a special page (called the \"front page\"). Users can be given a translated front page in their preferred language, or they can be given any other single page you specify.

Note: you **must** set `page_front_page`{.backtick} to get rid of this page being the front page:

        # Choose this, if most wiki content is in a single language.
        # If English is not your wiki's main language, choose something in YOUR wiki language
        page_front_page = u"MyStartingPage"

OR

        # Choose this, if wiki content is maintained in multiple languages.
        # In the navigation, "FrontPage" will get automatically translated for installed languages.
        page_front_page = u"FrontPage"

If you go the *single language* way, you can copy some of the content of FrontPage (or one of its translations) to the page you choose as your `page_front_page`{.backtick}.

If you go the *multiple language* way, don\'t forget to edit all translations of FrontPage.

![/!\\](/wiki/modernized/img/alert.png "/!\"){height="16" width="16"} If you go the *multiple languages* way, people reaching your wiki will be directed to the front page corresponding to their browser language setting. If you did not prepare that page (see front page name for different languages in [wiki comment](http://master.moinmo.in/HelpOnComments "MoinMaster"){.interwiki} below), they will see the default page for their language and have the impression the wiki is empty or badly maintained.

:::: {.comment style="display:none"}
::: {}
  ---------------------- -------------------------------- ------- --------------------------------------------------------------------------------------------------------
  Arabic                 Arabic (written in Arabic XXX)   ar      none
  Bulgarian              Български                        bg      [НачалнаСтраница](./(d09dd0b0d187d0b0d0bbd0bdd0b0d0a1d182d180d0b0d0bdd0b8d186d0b0).html){.nonexistent}
  Catalan                català                           ca      [PàginaPrincipal](./P(c3a0)ginaPrincipal.html){.nonexistent}
  Czech                  Čeština                          cs      [HlavniStranka](./HlavniStranka.html){.nonexistent}
  Danish                 Dansk                            da      [ForSide](./ForSide.html){.nonexistent}
  German                 Deutsch                          de      [StartSeite](StartSeite)
  Greek                  Ελληνικά                         el      none
  English                English                          en      none
  Spanish                Español                          es      [PáginaInicial](./P(c3a1)ginaInicial.html){.nonexistent}
  Persian                Persian                          fa      [صفحه اولیه](./(d8b5d981d8add98720d8a7d988d984db8cd987).html){.nonexistent}
  Finnish                Suomi                            fi      [EtuSivu](./EtuSivu.html){.nonexistent}
  French                 Français                         fr      [PageD\'Accueil](./PageD(27)Accueil.html)
  Galician               galego                           gl      [PáxinaInicial](./P(c3a1)xinaInicial.html){.nonexistent}
  Hebrew                 עברית                            he      [דף ראשי](./(d793d7a320d7a8d790d7a9d799).html){.nonexistent}
  Hindi                  Hindi (XXX in Hindi)             hi      none
  Croatian               Hrvatski                         hr      [Početna](./Po(c48d)etna.html){.nonexistent}
  Hungarian              Magyar                           hu      [KezdőLap](./Kezd(c591)Lap.html){.nonexistent}
  Indonesian             Bahasa Indonesia                 id      [HalamanMuka](./HalamanMuka.html){.nonexistent}
  Italian                Italiano                         it      [PaginaPrincipale](./PaginaPrincipale.html){.nonexistent}
  Japanese               Japanese                         ja      [フロントページ](./(e38395e383ade383b3e38388e3839ae383bce382b8).html){.nonexistent}
  Korean                 한국어                           ko      [대문](./(eb8c80ebacb8).html){.nonexistent}
  Kurdish                Kurdish (XXX in kurdish)         ku      none
  Lithuanian             Lietuvių                         lt      [PirmasisPuslapis](./PirmasisPuslapis.html){.nonexistent}
  Latvian                Latviešu                         lv      [SākumLapa](./S(c481)kumLapa.html){.nonexistent}
  Macedonian             Македонски                       mk      [Почетна](./(d09fd0bed187d0b5d182d0bdd0b0).html){.nonexistent}
  Mongolian              Mongolian (XXX in Mongolian)     mn      [Эхний хуудас](./(d0add185d0bdd0b8d0b920d185d183d183d0b4d0b0d181).html){.nonexistent}
  Norwegian Bokmal       Norsk Bokmål                     nb      [StartSide](./StartSide.html){.nonexistent}
  Dutch                  Nederlands                       nl      [VoorPagina](./VoorPagina.html){.nonexistent}
  Polish                 Polski                           pl      [StronaGłówna](./StronaG(c582c3b3)wna.html){.nonexistent}
  Brazilian Portuguese   Português do Brasil              pt-br   [PáginaPrincipal](./P(c3a1)ginaPrincipal.html){.nonexistent}
  Portuguese             Português                        pt      [PáginaPrincipal](./P(c3a1)ginaPrincipal.html){.nonexistent}
  Romanian               Română                           ro      [PaginaPrincipală](./PaginaPrincipal(c483).html){.nonexistent}
  Russian                Русский                          ru      [ГлавнаяСтраница](./(d093d0bbd0b0d0b2d0bdd0b0d18fd0a1d182d180d0b0d0bdd0b8d186d0b0).html){.nonexistent}
  Slovak                 slovenčina                       sk      [HlavnáStránka](./Hlavn(c3a1)Str(c3a1)nka.html){.nonexistent}
  Slovenian              slovenščina                      sl      [PrvaStran](./PrvaStran.html){.nonexistent}
  Serbian                Srpski                           sr      [НасловнаСтрана](./(d09dd0b0d181d0bbd0bed0b2d0bdd0b0d0a1d182d180d0b0d0bdd0b0).html){.nonexistent}
  Swedish                Svenska                          sv      [StartSida](./StartSida.html){.nonexistent}
  Turkish                Türkçe                           tr      [AnaSayfa](./AnaSayfa.html){.nonexistent}
  Ukrainian              Українська                       uk      [Початок](./(d09fd0bed187d0b0d182d0bed0ba).html){.nonexistent}
  Vietnamese             Tiếng Việt                       vi      [Trang đầu](./Trang(20c491e1baa7)u.html){.nonexistent}
  Simplified Chinese     简体中文                         zh      [首页](./(e9a696e9a1b5).html){.nonexistent}
  Chinese/Taiwan         繁體中文                         zh-tw   [首頁](./(e9a696e9a081).html){.nonexistent}
  ---------------------- -------------------------------- ------- --------------------------------------------------------------------------------------------------------
:::
::::

## User interface text translations {#User_interface_text_translations}

MoinMoin tries to adapt the user interface to the language the user prefers.

If the user puts a specific language preference into his user preferences, that language will be used for the user interface. But the user doesn\'t even need to do that if he already has configured his browser with his language preferences.

If there is no specific user preferences language setting, moin tries to adapt to the languages the user configured in his browser. So if the browser tells moin that its preference is Canadian English, then German, then English in general and moin has German and English available (but not a specific configuration for Canadian English), then the user will get a German user interface.

If there is no common language in the user\'s browser configuration and in moin or if you have set `language_ignore_browser = True`, moin will fall back to using what is configured as `language_default`. This is also the case if the user\'s browser does not specify any language.

The usual case when you want to set `language_ignore_browser = True` is when running a local wiki with no international audience and you maintain the wiki in only one (your local) language. Don\'t forget to specify your one-and-only language using language_default when doing this.

## System and help page translations and the navigation bar {#System_and_help_page_translations_and_the_navigation_bar}

The MoinMoin distribution archive contains the system pages (like `RecentChanges`{.backtick}) in different languages, selecting the correct language in the same way as for the user interface.

For example, if the navi_bar contains a link to `RecentChanges`{.backtick}, moin will first look for a translation of `RecentChanges`{.backtick} into the user\'s language. So if the user\'s language is German (de), the translation is `AktuelleÄnderungen`{.backtick}. Moin will use `AktuelleÄnderungen`{.backtick} in the navi_bar display if that page actually exists; otherwise, it will fall back to using `RecentChanges`{.backtick}.

## Understanding Language packs {#Understanding_Language_packs}

::: note
**Quickstart (for lazy people)**: Install the package `all_pages` for the language(s) in which you provide some content.
:::

For each language, there is up 17 packages of underlay pages. The underlay pages are split by priorities (`essential`, `optional` and \"`all`\") and by categories:

- `*_System_*` - Page needed run the wiki like [RecentChanges](RecentChanges), [FindPage](FindPage) and [FrontPage](FrontPage).

- `*_Help_*` - Some help pages (mostly for wiki editors)

- `*_Template_*` - Templates !

- `*_Category_*` - MoinMoin built-in categories (like `Category``Category`)

- `*_Admin_*` - Pages useful for wiki administrators only

- `*_pages` - Contains the content of all 5 packages above.

Language packs are named like `essential_help_pages.zip`, where `essential` and `help` are the priority and category. Here\'s a matrix with the packages available:

::: {}
+--------------------+:------------------------:+:----------------------:+:--------------------------:+:--------------------------:+:-------------:+:------------------:+
|                    | Categories                                                                                                                                       |
+--------------------+--------------------------+------------------------+----------------------------+----------------------------+---------------+--------------------+
|                    | **System**               | **Help**               | **Template**               | **Category**               | **Admin**     | **All Categories** |
+--------------------+--------------------------+------------------------+----------------------------+----------------------------+---------------+--------------------+
| **Essential**      | `essential_system_pages` | `essential_help_pages` | `essential_template_pages` | `essential_category_pages` |               | `essential_pages`  |
+--------------------+--------------------------+------------------------+----------------------------+----------------------------+---------------+--------------------+
| **Optional**       | `optional_system_pages`  | `optional_help_pages`  | `optional_template_pages`  |                            |               | `optional_pages`   |
+--------------------+--------------------------+------------------------+----------------------------+----------------------------+---------------+--------------------+
| **All priorities** | `all_system_pages`       | `all_help_pages`       | `all_template_pages`       | `all_category_pages`       | `admin_pages` | **`all_pages`**    |
+--------------------+--------------------------+------------------------+----------------------------+----------------------------+---------------+--------------------+
:::

[The language packs are compiled according to pages listed in [MoinMoin/i18n/strings.py](http://hg.moinmo.in/moin/1.9/file/ac5dc19e0a0e/MoinMoin/i18n/strings.py){.http} (using the command `moin maint mkpagepacks`)]{.comment style="display:none"}
::::::::
