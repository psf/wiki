# JythonMonthly/Newsletters/August2010

::::: {#content dir="ltr" lang="en"}
::: {}
  ----------------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***                       ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png"){.external_image}
  **August/September 2010 \-- Issue #45**   
  ----------------------------------------- ---------------------------------------------------------------------------------------------------
:::

This is the Jython Monthly newsletter for the months of August and September of 2010. These are exciting times for Jython as the second beta for 2.5.2 has been released. Please download and test now if you haven\'t done so already! Due to a lack of materials over the past couple of months, the newsletter will combine both August and September together. I plan to distribute a separate special [JavaOne](./JavaOne.html){.nonexistent} update after the conference as well.

If you have any questions or suggestions for the newsletter, please feel free to send them to [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com){.mailto}. I appreciate the feedback!

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com){.http}

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com){.mailto}

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast){.http}

## News {#News}

**Jython 2.5.2 b2 Has Been Released**

The Jython development team has released the second beta for the 2.5.2 release. The list of issues that have been addressed are as follows:

\[ 1327 \] Classloaders cannot GC, which exhausts permgen (partial bug fix)

\[ 1604 \] [PyBuiltinCallable](./PyBuiltinCallable.html){.nonexistent}.Info should be serializable

\[ 1397 \] Bugs in [PyList](./PyList.html){.nonexistent} and [PyJavaType](./PyJavaType.html){.nonexistent}.[ListIndexDelegate](./ListIndexDelegate.html){.nonexistent} slice setting

\[ 1503 \] Java constructors should take keyword arguments

\[ 1648,1495,1516 \] Incomplete implementation of pep328 for relative imports

\[ 1611 \] Jython bytecode violated JLS, causing NPE on Sun\'s JVM when using -Xcomp option

\[ 1643 \] Tools subdirectory still exists in trunk

\[ 1455 \] Classes loaded dynamically from sys.path do not have their package defined

\[ 1555 \] Jython does not publish MIME types via JSR 223 ([ScriptEngine](./ScriptEngine.html){.nonexistent}.getFactory().getMimeTypes() is empty).

\[ 1632 \] cPickle.Unpickler does not allow assignment of find_global

\[ 1395 \] [PyList](./PyList.html){.nonexistent}.indexOf() and [PyTuple](./PyTuple.html){.nonexistent}.indexOf() do not function properly

\[ 1373 \] Jython [ClassLoader](./ClassLoader.html){.nonexistent} getResource does not work

\[ 1506 \] Jython applies PEP263 pattern for determining source-code encoding on noncomments

\[ 1630 \] threading.Thread lacks [tojava]{.u} method

\[ 1558 \] [PyFunction](./PyFunction.html){.nonexistent} to single method interface wrapping does not andle java.lang.Object methods

\[ 1622 \] array type prevents [radd]{.u} fallback

Please go [download](http://www.jython.org/downloads.html){.http} the release and test today! Report any issues to the [Jython bug tracker](http://bugs.jython.org){.http}. Congrats to the development team on another excellent release.

**Blog Series - Jython and Swing**

*By: Bob Gibson*

Bob Gibson\'s blog series on Jython and Swing continues and it is available at [DeveloperWorks Blogs](http://www.stumbleupon.com/su/30gLrh/www.ibm.com/developerworks/mydeveloperworks/blogs/JythonSwing/entry/unsafe_at_any_speed150?ca=twtrJythonSwingSafedth-MydW){.http}. Excellent work done by Bob Gibson, author of Websphere Application Server Administration Using Jython.

## Blogs {#Blogs}

[Jython 2.5.2 Beta 2 Is Released](http://zyasoft.com/pythoneering/2010/09/jython-2.5.2-beta-2-is-released/){.http} - Jim Baker

[Jython 2.5.2 Beta 2 Is Released](http://fwierzbicki.blogspot.com/2010/09/jython-252-beta-2-is-released.html){.http} - Frank Wierzbicki

[Multithreading in Jython](http://blog.asolofnenko.cjb.net/index.php/2010/09/12/multithreading_in_jython){.http}

[Jython Python Function](http://openfoo.org/blog/jython_python_function.html){.http}

## Articles {#Articles}

[Swing Texting Can Be Fun](https://www.ibm.com/developerworks/mydeveloperworks/blogs/JythonSwing/entry/texting_can_be_fun20?oldlang=ko&lang=en){.https} - Bob Gibson

## Discussions {#Discussions}

[Jython Classes and Variable Scope](http://stackoverflow.com/questions/3681002/jython-classes-and-variable-scope){.http}

[Getting the Previous Line in Jython](http://www.weask.us/entry/previous-line-jython){.http}

## Frameworks {#Frameworks}

[Django-Jython Project](http://code.google.com/p/django-jython/){.http}

[Pylons on Jython](http://wiki.pylonshq.com/display/pylonscookbook/Pylons+on+Jython){.http}

[Web2Py](http://www.web2py.com/){.http}

## Documentation {#Documentation}

[Glassfish Server 3.0.1 Scripting Docs](http://docs.sun.com/app/docs/doc/821-1760/gjiam?a=view-oracle){.http}

[Glassfish V3 Admin Console](http://wiki.glassfish.java.net/attach/GlassFishV3AdminConsole/admingui-3.1-modules.html){.http}

[WSO2 Documentation](http://wso2.org/project/wsf/jython/documentation){.http}

## IDE {#IDE}

[Field Project](http://openendedgroup.com/field){.http}

[PyDev 1.6.2](http://pydev.sourceforge.net/){.http}

[Netbeans 6.9.1](http://www.netbeans.org){.http}

[jHepWork](http://jwork.org/jhepwork){.http}

[Intellij](http://www.jetbrains.com/idea/){.http}

[Jython Processor with Swing GUI](http://jythonprocessor.sourceforge.net/){.http}

::: {}
  ----------------------------------------------------------------
  **Links**
  [Jython Home](http://www.jython.org){.http}
  [Python Home](http://www.python.org){.http}
  [Jython WikiPedia](http://en.wikipedia.org/wiki/Jython){.http}
  [Freshmeat.net](http://freshmeat.net/projects/jython/){.http}
  [Python Daily News](http://www.pythonware.com/daily/){.http}
  [Planet Jython](http://planet.jython.org/){.http}
  ----------------------------------------------------------------
:::
:::::
