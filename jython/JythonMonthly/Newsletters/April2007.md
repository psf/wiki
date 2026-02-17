# JythonMonthly/Newsletters/April2007

::::: {#content dir="ltr" lang="en"}
::: {}
  ------------------------------ ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***            ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png"){.external_image}
  **April 2007 \-- Issue #10**   
  ------------------------------ ---------------------------------------------------------------------------------------------------
:::

Welcome to the April 2007 issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge. Please contribute to future newsletters by writing articles or tutorials based on your experiences with Jython!

**At this time, I would like to formally request a new editor to take over the Jython Monthly newsletter. Life brings about many changes, and some recent developments in my life will drastically reduce the amount of time I have for tasks such as this. I really enjoyed being the editor for Jython Monthly, unfortunately I will have to pass it along at this time. If there is anyone interested in taking over as editor for the Jython Monthly newsletter, please feel free to contact me at [jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com){.mailto}. I look forward to responding to your emails!**

At this time, this will be the final distribution of Jython Monthly under my care. Thanks to all who have contributed and read the newsletter!

\- Josh Juneau

Questions, comments, or suggestions?

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com){.mailto} or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net){.mailto} for discussion.

# Presentations {#Presentations}

[Dynamic Scripting on Java](http://downloads.pushtotest.com/presentations/2007_TSSJS_Scripting.pdf){.http}

# Articles {#Articles}

**There were no article submissions this month**

# Off The Lists {#Off_The_Lists}

***Question:***

I need to redirect all stdout and stderr to files. This redirection needs to also include the output of imported Java modules that I use. The following example readily given on the Web only catches the script\'s output, Jythons output - not external Java modules output:

sys.stdout = open(\"/tmp/jythonstdout\", \"w\") sys.stderr = open(\"/tmp/jythonstderr\", \"w\")

print \>\> sys.stdout, \"out\" \# Java modules output is not captured

I then thought that I should instead use dup2, also a common example on the Web:

stdoutlog = open(\"/tmp/jythonstdout\", \"w\") stderrlog = open(\"/tmp/jythonstderr\", \"w\")

os.dup2(stdoutlog.fileno(), sys.stdout.fileno()) os.dup2(stderrlog.fileno(), sys.stderr.fileno())

Unfortunately, the above code produces the following error: [NameError](./NameError.html){.nonexistent}: name \"file\" is not defined. I took this as a sign that I\'m supposed to be using open() instead of file, which is said to be an alias for file(). Except, that also generates an error:

IOError: fileno() is not supported in jpython

Can someone please steer me in the right direction?

***Answer:***

from java.io import \* from java.lang import \* \# \-\--method

------------------------------------------------------------------------

def redirect():

- directory = File(\"c:/jython/myprojects/redirect/\") errFile = File.createTempFile(\"stderr\", \".txt\", directory)

  System.setErr([PrintStream](./PrintStream.html){.nonexistent}([FileOutputStream](./FileOutputStream.html){.nonexistent}(errFile))) outFile = File.createTempFile(\"stdout\", \".txt\", directory) System.setOut([PrintStream](./PrintStream.html){.nonexistent}([FileOutputStream](./FileOutputStream.html){.nonexistent}(outFile)))

\# \--main code

------------------------------------------------------------------------

System.out.println(\"test before redirect\"); redirect() System.out.println(\"test after redirect\");

# Interested in Developing Jython? {#Interested_in_Developing_Jython.3F}

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867){.http} and submit patches for items which you can repair.

# Jython Blogs {#Jython_Blogs}

[Standalone Jython Import](http://stevegilham.blogspot.com/2007/03/standalone-jython-importerror-no-module.html#links){.http}

# IDE {#IDE}

[JythonConsole](./JythonConsole.html){.nonexistent} 0.0.4 Released - [http://code.google.com/p/jythonconsole/](http://code.google.com/p/jythonconsole/){.http}

***Pydev and Pydev Extensions 1.3.1 have been released***

Details on Pydev Extensions: [http://www.fabioz.com/pydev](http://www.fabioz.com/pydev){.http} Details on Pydev: [http://pydev.sf.net](http://pydev.sf.net){.http} Details on its development: [http://pydev.blogspot.com](http://pydev.blogspot.com){.http}

Release Highlights in Pydev Extensions:

------------------------------------------------------------------------

\* Interactive Console: jython process can receive vmargs (configured in the preferences page) \* Code-Completion: auto-import completions will not be brought for tokens in the current module \* Code-Completion: auto-import inserted as last import in imports list (so, [future]{.u} imports will remain in the 1st position) \* Code-Analysis: Only adds unused parameters in methods that have some statement that is not a \'pass\' or string \* Fix: Find Occurrences: will not \'overlap\' occurrences anymore \* Fix: Code-Analysis: deep attribute access after finding [getattr]{.u} does not signal unresolved import errors anymore

Release Highlights in Pydev:

------------------------------------------------------------------------

\* Mylar integration: the pydev package explorer now supports mylar (packaged as a separate feature: org.python.pydev.mylar.feature ) \* Code-completion: comment completion is now the same as string completion \* Debug: Breakpoints can be set in external files \* Debug: Breakpoint annotations now show in external files \* Package Explorer: filter for import nodes created \* Fix: Package Explorer Actions: Open action does not expand children when opening python file \* Fix: Project Explorer (WTP) integration: does not conflict with elements from other plugins anymore (such as java projects) \* Fix: halt in new project wizard: when creating a new project from the pydev wizard it was halting in some platforms \* Fix: \${string_prompt} in run config: now only evaluated on the actual run \* Fix: Code-Completion: jython shell was not handling java.lang.[NoClassDefFoundError](NoClassDefFoundError) correctly

# Interesting Facts {#Interesting_Facts}

Jython - Average Job Salary & Stats in UK [http://www.itjobswatch.co.uk/jobs/uk/jython.do](http://www.itjobswatch.co.uk/jobs/uk/jython.do){.http}

# Useful Links {#Useful_Links}

[Jacl v2.5 Released](http://www-1.ibm.com/support/docview.wss?rs=180&uid=swg24012144){.http}

The IBM® Jacl to Jython Conversion Assistant ([Jacl2Jython](./Jacl2Jython.html){.nonexistent}) is a program that assists in converting [WebSphere](WebSphere)® administrative (wsadmin) scripts written in Jacl into Jython syntax.

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
