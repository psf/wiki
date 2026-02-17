# JythonMonthly/Newsletters/August2006

:::::: {#content dir="ltr" lang="en"}
::: {}
  ------------------------------ ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***            ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png"){.external_image}
  **August 2006 \-- Issue #2**   
  ------------------------------ ---------------------------------------------------------------------------------------------------
:::

Welcome to the another issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge. I want to encourage the readers of Jython Monthly to send any articles, tips, tricks, or any other Jython related material to me if you think it should be distributed with this newsletter.

\- Josh Juneau

Questions, comments, or suggestions???

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com){.mailto} or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net){.mailto} for discussion.

# Articles {#Articles}

## Add Logging to Jython Using Log4J {#Add_Logging_to_Jython_Using_Log4J}

[http://wiki.python.org/jython/JythonMonthly/Articles/August2006/1](http://wiki.python.org/jython/JythonMonthly/Articles/August2006/1){.http}

*Submitted by: Josh Juneau*

Are you still using the Jython *print* command to show your errors? How about in a production environment, are you using any formal logging? If not, you should be doing so\...and the Apache log4j API makes it easy to do so. Many Java developers have grown to love the log4j API and it is utilized throughout much of the community. That is great news for Jython developers since we\'ve got direct access to Java libraries!

### Setting Up Your Environment {#Setting_Up_Your_Environment}

The most difficult part about using log4j with Jython is the setup. You must ensure that the log4j.jar archive resides somewhere within your Jython PATH (usually this entails setting the CLASSPATH to include necessary files in Windows environment). You then set up a properties file for use with log4j. Within the properties file, you can include appender information, where logs should reside, and much more.

Example properties file:

    log4j.rootLogger=debug, stdout, R

    log4j.appender.stdout=org.apache.log4j.ConsoleAppender
    log4j.appender.stdout.layout=org.apache.log4j.PatternLayout

    # Pattern to output the caller's file name and line number.
    log4j.appender.stdout.layout.ConversionPattern=%5p [%t] (%F:%L) - %m%n

    log4j.appender.R=org.apache.log4j.RollingFileAppender
    log4j.appender.R.File=C:\\Jython\\testlog4j.log

    log4j.appender.R.MaxFileSize=100KB
    # Keep one backup file
    log4j.appender.R.MaxBackupIndex=1

    log4j.appender.R.layout=org.apache.log4j.PatternLayout
    log4j.appender.R.layout.ConversionPattern=%p %t %c - %m%n 

You are now ready to use log4j in your Jython application. As you can see, if you\'ve ever used log4j with Java, it is pretty much the same.

### Using log4j in a Jython Application {#Using_log4j_in_a_Jython_Application}

Once again, using log4j within a Jython application is very similar to it\'s usage in the Java world.

First, you must import the log4j packages:

    from org.apache.log4j import * 

Second, you obtain a new logger for your class or module and set up a [PropertyConfigurator](./PropertyConfigurator.html){.nonexistent}:

     Logger logger = Logger.getLogger("myClass")
      # Assume that the log4j properties resides within a folder named "utilities"
      PropertyConfigurator.configure(sys.path[0] + "/utilities/log4j.properties")

Lastly, use log4j:

      # Example module within the class:
       def submitDocument(self, event):
           try:
               # Assume we perform some SQL here              
           except SQLException, ex:
               self.logger.error("docPanel#submitDocument ERROR: %s" % (ex)) 

Your logging will now take place within the file you specified in the properties file for *log4j.appender.R.File*.

### Using log4j in Jython Scripts {#Using_log4j_in_Jython_Scripts}

Many may ask, why in the world would you be interested in logging information about your scripts? Most of the time a script is executed interactively via the command line. However, there are plenty of instances where it makes sense to have the system invoke a script for you. As you probably know, this technique is used quite often within an environment to run nightly tasks, or even daily tasks which are automatically invoked on a scheduled basis. For these cases, it can be extremely useful to log errors or information using log4j. Some may even wish to create a separate automated task to email these log files after the tasks complete.

The overall implementation is the same as above, the most important thing to remember is that you must have the log4j.jar archive and properties file within your Jython path. Once this is ready to go you can use log4j in your script.

     from org.apache.log4j import *
     logger = Logger.getLogger("scriptname")
     PropertyConfigurator.configure("C:\path_to_properties\log4j.properties")
     logger.info("Test the logging")

### Future Possibilities {#Future_Possibilities}

Log4J is nice, but there are other logging frameworks which could be extremely useful in Jython as well. As a matter of fact, there is a new logging \"anti-framework\" which is called [SimpleLog](./SimpleLog.html){.nonexistent} 2.0 and it looks helpful. I haven\'t yet reviewed [SimpleLog](./SimpleLog.html){.nonexistent} 2.0, but I plan to do so in the near future!

Check it out at: [https://simple-log.dev.java.net/](https://simple-log.dev.java.net/){.https}

# Tips and Tricks {#Tips_and_Tricks}

## Create a Jython Time Profiler {#Create_a_Jython_Time_Profiler}

A module that helps to inject time profiling code in other modules to measure actual execution times of blocks of code. This has been tested and verified with Jython!

[Python Cookbook Recipe](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496938){.http}

# BECOME THE FIRST JYTHON DEVELOPER ON SUN GRID AND WIN YOUR SHARE OF \$50,000 IN PRIZES! {#BECOME_THE_FIRST_JYTHON_DEVELOPER_ON_SUN_GRID_AND_WIN_YOUR_SHARE_OF_.2450.2C000_IN_PRIZES.21}

- ![](https://coolapps.developer.network.com/banner.JPG "https://coolapps.developer.network.com/banner.JPG"){.external_image}

Test your skills with the Coolaps Developer Challenge: There are two ways to compete - the best application that runs on Sun Grid Compute Utility, and the best application built with the Compute Server Plugin for [NetBeans](./NetBeans.html){.nonexistent}. We designed things this way to allow as many people as possible to participate, including International participants, who cannot access the Sun Grid Compute Utility today.

Learn more about the Coolapps Developer Challenge: [https://coolapps.developer.network.com/](https://coolapps.developer.network.com/){.https}

# Off The Lists {#Off_The_Lists}

Question: *I would like to know what you think is the best way to recognize - right at the beginning of a script -, whether the code is run by Jython or pure Python interpreter, because I will get [ImportError](./ImportError.html){.nonexistent} when Python sees the \"import java\" lines etc. (also if the script is part of a package and another module is imported)*

Answers:

{{{import sys if sys.platform.startswith(\'java\'):

- ..}}}

OR {{{import sys isJython = hasattr(sys,\'classLoader\') }}} OR {{{import sys

if sys.platform.startswith(\'java\'):

- JAVA = 1

else:

- JAVA=0

}}}

Pydev and Pydev Extensions 1.2.2 have been released

Details on Pydev Extensions: [http://www.fabioz.com/pydev](http://www.fabioz.com/pydev){.http} Details on Pydev: [http://pydev.sf.net](http://pydev.sf.net){.http} Details on its development: [http://pydev.blogspot.com](http://pydev.blogspot.com){.http}

# Mentionable Books {#Mentionable_Books}

Check out this new book by *Kuassi Mensah* entitled [Oracle Database Programming Using Java and Web Services](http://www.amazon.com/gp/product/1555583296/102-2444634-2799355?redirect=true){.http}. It includes some experimental examples of running Jython in the database using Java runtime.

Check out this blog for more details: [Kuassi Mensah Blog](http://db360.blogspot.com/2006/08/oracle-database-programming-using-java_01.html){.http}

# Interested in Developing Jython? {#Interested_in_Developing_Jython.3F}

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867){.http} and submit patches for items which you can repair.

[Oldie but goodie for those interested in helping to develop Jython](http://www.informit.com/articles/article.asp?p=26127&rl=1){.http}

# Who\'s Using Jython? {#Who.27s_Using_Jython.3F}

[ActiveGrid chooses Jython to bring LAMP closer to Java](http://www.pythonthreads.com/news/latest/activegrid-chooses-jython-to-bring-lamp-development-closer-to-java..html){.http}

[ProtoCard](http://sourceforge.net/projects/protocard){.http}

[Grinder - Java Load Testing Framework](http://grinder.sourceforge.net/index.html){.http}

# IDE Information {#IDE_Information}

[JyConsole](http://sourceforge.net/projects/jyconsole){.http}

[JyConsole](./JyConsole.html){.nonexistent} is an advanced Java graphic console for Jython. [JyConsole](./JyConsole.html){.nonexistent} provides an object-oriented completion on Java and Python objects and allows the direct manipulation of objects. [JyConsole](./JyConsole.html){.nonexistent} includes command history, script loading and GUI preference.

How To Get Cluster Name via Jython in wsadmin?

[http://www-128.ibm.com/developerworks/forums/dw_thread.jsp?forum=266&thread=123951&cat=9](http://www-128.ibm.com/developerworks/forums/dw_thread.jsp?forum=266&thread=123951&cat=9){.http}

# Jython Blogs {#Jython_Blogs}

Jython Considered Dangerous? - [http://dev2dev.bea.com/blog/simonvc/archive/2006/07/jython_consider.html](http://dev2dev.bea.com/blog/simonvc/archive/2006/07/jython_consider.html){.http}

Scripting Oracle with Jython - [http://prpi.blogspot.com/2006/05/scripting-oracle-with-jython.html](http://prpi.blogspot.com/2006/05/scripting-oracle-with-jython.html){.http}

Jython, Swing & Curry - [http://www.smallshire.org.uk/sufficientlysmall/2005/12/03/jython-swing-curry/](http://www.smallshire.org.uk/sufficientlysmall/2005/12/03/jython-swing-curry/){.http}

# Interesting Facts {#Interesting_Facts}

Jython - Average Job Salary & Stats in UK [http://www.itjobswatch.co.uk/jobs/uk/jython.do](http://www.itjobswatch.co.uk/jobs/uk/jython.do){.http}

# Useful Links {#Useful_Links}

::: {}
  ----------------------------------------------------------------------------------------------------------------------------------
  **Articles**
  [Using Jython to Test Hibernate Criteria Queries](http://jroller.com/page/techkriti?entry=using_jython_to_test_hibernate){.http}
  ----------------------------------------------------------------------------------------------------------------------------------
:::

::: {}
  ----------------------------------------------------------------
  **Links**
  [Jython Home](http://www.jython.org){.http}
  [Python Home](http://www.python.org){.http}
  [Jython WikiPedia](http://en.wikipedia.org/wiki/Jython){.http}
  [Freshmeat.net](http://freshmeat.net/projects/jython/){.http}
  ----------------------------------------------------------------
:::
::::::
