# JythonMonthly/Newsletters/February2007

::::: {#content dir="ltr" lang="en"}
::: {}
  -------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***              ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png"){.external_image}
  **February 2007 \-- Issue #8**   
  -------------------------------- ---------------------------------------------------------------------------------------------------
:::

Welcome to the February 2007 issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge. I want to encourage the readers of Jython Monthly to send any articles, tips, tricks, or any other Jython related material to me if you think it should be distributed with this newsletter.

There has been quite a bit of activity in the past couple of months within the Jython community. Jython development has been quite active, Jython 2.2 Beta 1 has been released, and the user base is also growing. As a whole, the CPython language and all of its implementations are actively growing more each day. As such is the case, this year\'s [PyCon](http://us.pycon.org/TX2007/HomePage){.http} event is sure to be a worthy event. I would like to encourage all reader\'s that live near Dallas or have the ability to travel to attend this event. It will be held Feb 23-25 in Addison Texas. For more information, please visit the [PyCon 2007](http://us.pycon.org/TX2007/HomePage){.http} home page.

Special thanks to those who submitted material for this month\'s newsletter!

\- Josh Juneau

Questions, comments, or suggestions?

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com){.mailto} or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net){.mailto} for discussion.

# News {#News}

Welcome the most recent release of the Jython scripting language, Jython 2.2 Beta 1! This represents a major milestone in the life cycle of the Jython scripting language as this is the first release since the summer of 2005. The Jython developer and user community is extremely active right now and I predict that the gap between future releases will be much smaller.

Thanks to the developers for working hard on this release! Now it is up to the user community to test and give feedback for Beta 1. [Download](http://sourceforge.net/project/downloading.php?groupname=jython&filename=jython_installer-2.2b1.jar&use_mirror=osdn){.http} it now and get started!!

# Articles {#Articles}

## Adding JARs to sys.path During Runtime {#Adding_JARs_to_sys.path_During_Runtime}

*Submitted By: Steve Langer*

During Oct-Nov 2006 there was a thread in the jython-users group titled \"adding JARs to sys.path\". More accurately the objective there was to add JARs to the sys.path at runtime. Several people asked the question, \"Why would you want to do that?\" Well there are at least 2 good reasons. First, if you want to distribute a jython or Java package that includes non-standard Jars in it. Perhaps you want to make life easier for the target user and not demand that they know how to set environment variables. A second even more compelling reason is when there is no normal user account to provide environment variables.

[Read Entire Article](http://wiki.python.org/jython/JythonMonthly/Articles/January2007/3){.http}

# Off The Lists {#Off_The_Lists}

***Question From Luca Cassioli:***

- I need I have a function \"waiting in background\" for an event to be triggered. Can it be done from console, or should I write a script? In other words, I want to port such a source to Jython: import javax.telephony.\*; import javax.telephony.events.\*;

  []{.comment style="display:none"}

- The [MyInCallObserver](./MyInCallObserver.html){.nonexistent} class implements the [CallObserver](./CallObserver.html){.nonexistent} and

- recieves all Call-related events.

  public class [MyInCallObserver](./MyInCallObserver.html){.nonexistent} implements [CallObserver](./CallObserver.html){.nonexistent} {

  - public void callChangedEvent([CallEv](./CallEv.html){.nonexistent}\[\] evlist) { \[\....\] \[handle event\] }

  } import javax.telephony.\*; import javax.telephony.events.\*;

  import [MyInCallObserver](./MyInCallObserver.html){.nonexistent}; \[\....\] try {

  - Terminal terminal = myprovider.getTerminal(\"1234567890\");

    terminal.addCallObserver(new [MyInCallObserver](./MyInCallObserver.html){.nonexistent}());

  } catch (Exception excp) {

  - System.out.println(\"Can't get Terminal: \" + excp.toString()); System.exit(0);

  } }

***Answer From Jeff Emanuel:***

see [http://www.jython.org/Project/userguide.html#a-short-example](http://www.jython.org/Project/userguide.html#a-short-example){.http}

Direct translation:

\# imports omitted class [MyInCallObserver](./MyInCallObserver.html){.nonexistent}([CallObserver](./CallObserver.html){.nonexistent}):

- def callChangedEvent(self, evList):
  - \# handle event \...

try:

- terminal = myprovider.getTerminal(\'1234567890\')

  terminal.addCallObserver([MyInCallObserver](./MyInCallObserver.html){.nonexistent}())

except java.lang.Exception, ex:

- print \"Can\'t get terminal \" + ex.toString() System.exit(0)

Or try the bean events technique ([http://www.jython.org/Project/userguide.html#event-properties](http://www.jython.org/Project/userguide.html#event-properties){.http}):

def handleCall(evList):

- \# handleEvent

try:

- terminal = myprovider.getTerminal(\'1234567890\') terminal.callChangedEvent=handleCall

except java.lang.Exception, ex:

- print \"Can\'t get terminal \" + ex.toString() System.exit(0)

# Interested in Developing Jython? {#Interested_in_Developing_Jython.3F}

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867){.http} and submit patches for items which you can repair.

# Tips and Tricks {#Tips_and_Tricks}

[Python Cookbook: BaseHTTPServer with Socket Timeout](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/499376){.http}

[Python Cookbook: Generator for an arbitrary number of \'for\' loops](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/502194){.http}

[Python Cookbook: Another generator for an arbitrary number of \'for\' loops](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/502199){.http}

# Jython Blogs {#Jython_Blogs}

[Jython Roadmap \-- Frank Wierzbicki](http://fwierzbicki.blogspot.com/2007/02/jython-roadmap.html){.http}

[Jython 2.2 - Beta 1 Released \-- Frank Wierzbicki](http://fwierzbicki.blogspot.com/2007/02/jython-22-beta1-released.html){.http}

[Jython 2.2 Beta 1 \-- Josh Juneau](http://jj-blogger.blogspot.com/2007/02/jython-22-beta-1-released.html){.http}

[Improvised AOP with Jython](http://henkenotes.blogspot.com/2007_01_01_archive.html){.http}

[GUESS: A cool graph visualization application using Jython](http://www.jroller.com/page/languages?entry=guess_cool_graph_visualization_application){.http}

[Jython 2.2 Hits Major Milestone \-- Push To Test](http://www.pushtotest.com/thecohenblog/jython22.html){.http}

# IDE {#IDE}

**Pydev and Pydev Extensions 1.2.6 have been released**

Details on Pydev Extensions: [http://www.fabioz.com/pydev](http://www.fabioz.com/pydev){.http}

Details on Pydev: [http://pydev.sf.net](http://pydev.sf.net){.http}

Details on its development: [http://pydev.blogspot.com](http://pydev.blogspot.com){.http}

# Discussions {#Discussions}

[Jython & Alice](http://www.alice.org/community/showthread.php?t=612){.http}

[Connect to Java RMI Server from Jython](http://forums.thedailywtf.com/forums/thread/109138.aspx){.http}

[Extended Repository Service & Jython Scripting](http://www-128.ibm.com/developerworks/forums/dw_thread.jsp?forum=778&thread=151729&cat=9){.http}

*Discussion Submitted by Thomas Muller* \-- ***Second Notice***

Hello jython users,

I want to suggest a new project, but need your help. There is an open source python written serverless instant messenger out (based on a kademlia DHT lookup for buddies):

[http://cspace.in](http://cspace.in){.http}

Version 1.26 (though the icons in version 1.24 are better). As well a linux porting exists. [http://www.aabdalla.com/releases/](http://www.aabdalla.com/releases/){.http}

I want to initiate a project to port the python messenger to java using jython. But I cannot do it alone. We could register a sf.net project for \"cspace-java\". Is jython ready to just compile it and get a jar out and a source-file out? Can someone send this through jython or help?

The server is serverless and this means independence from any central instance. It uses to identify the buddy a RSA-Key and a CSpace-ID from the developer-server. In the long run, only the RSA-Key should be used. Unfortunatly you cannot a) create an RSA-key without that central server and b) you cannot launch the application without the Cspace-ID.

Anyway, we can use it with the tachyon server for creation, but communication and buddy-lookup is decentral and encrypted like skype as well.

But what we need is a java version. Maybe the cspace developers did not played around with jython either, and instead of coding windows and Linux or MacOSX port, we can switch to interoperable java.

But as there are less resources, I want to ask the mailinglist of jython to fix the current status of the application over jython to java please.

The serverless Messenger in java could be easily built in into many applications, which need an instant messenger:

\- yacy.net - serverless p2p webindex search engine in java - sf.net/projects/antsp2p - already a jeti-jabber buddylist integrated for bootstrapping, but it is central. - limewire.com of course - azureus.sf.net of course - wikisari, the google pendant, still under development [http://lists.wikia.com/pipermail/search-l/2006-December/000004.html](http://lists.wikia.com/pipermail/search-l/2006-December/000004.html){.http}

Does anyone agree on that potentials? kind regards tom

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
