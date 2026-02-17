# PoundPythonWeb

::: {#content dir="ltr" lang="en"}
# #python.web FAQ {#A.23python.web_FAQ}

This is a list of Frequently Asked Questions for the #python.web IRC channel on Freenode.

### Nobody\'s around! What do I do? {#Nobody.27s_around.21_What_do_I_do.3F}

Okay, so nobody actually asks this, but we frequently see someone pop in, ask a question, and leave fifteen minutes later. A half hour later, someone unidles, and would answer the question, but the person who asked it is gone. So, if nobody answers your question, just stick around. We idle a lot.

### Can you help me with mod_python? {#Can_you_help_me_with_mod_python.3F}

Sure. Don\'t use mod_python.

It causes people no end of trouble and was never really a good idea in the first place. Yes, this is our opinion, but it\'s an opinion that\'s been borne out by experience. If you think #python.web ought to help people with mod_python, great. Come give help. We can use active people.

[More on mod_python from #python.web](./PoundPythonWeb(2f)mod_python.html)

### What framework should I use? {#What_framework_should_I_use.3F}

This is widely considered to be one of the \"religious\" issues, along with choice of programming editor and operating system. There\'s also no substitute for experimenting with a wide range of frameworks. A good list can be found at [WebProgramming](WebProgramming).

That said, people keep asking for our opinions, so here they are:

[JonRosebaugh](./JonRosebaugh.html){.nonexistent} (Chairos) says \"Assuming you\'re interested in a MVC-style architecture, probably the most important consideration is how much support the framework has for [WSGI](http://www.python.org/peps/pep-0333.html){.http}, because WSGI is the direction Python web programming is heading in. Some frameworks enthusiastically embrace WSGI, some have superficial support, and some don\'t address it at all. I\'d recommend [Pylons](http://pylonshq.com/){.http} (and [TurboGears](http://www.turbogears.org/){.http}, once TG2 is out). [Django](http://www.djangoproject.com/){.http} is also good for apps that don\'t need too much in the way of flexibility.\"

patx says \"I personally like Django. It lets me do everything I need to run all of my different Python web scripts. Google [AppEngine](AppEngine) is always good too. GAE lets meeasily use Django with my GAE scripts, making it \'double nice\'.\"

If you\'d like to add your opinion, feel free to do so; if you\'d like to disagree with what one of us wrote here, the best place to do that is probably on the IRC channel.

### I need help with FooWeb framework! (Or: Why doesn\'t it work when I do bar?) {#I_need_help_with_FooWeb_framework.21_.28Or:_Why_doesn.27t_it_work_when_I_do_bar.3F.29}

Well, we\'ll try to help. But we\'re not experts at everything, so don\'t be surprised if your question about running FooWeb through [mod_python](ModPython) on IRIX goes unanswered. There are times it may be better to seek out a community specific to your framework or toolkit.

Maybe there is also a channel for your framework. Here a list of known support channels on freenode:

- #django for Django
- #turbogears for Turbogears
- #pylons for Pylons
- #myghty for Myghty
- #pythonpaste for Paste
- #pocoo for Werkzeug
- #zope for Zope 2
- #zope3-dev for Zope 3
- #circuits for Circuits
- #appengine for Google Appengine

### Can I bring my IRC bot into the channel? {#Can_I_bring_my_IRC_bot_into_the_channel.3F}

No. We are trying to reduce idlers, and it so happens that bots are worst of idlers. Sorry.

### My question wasn\'t covered here. {#My_question_wasn.27t_covered_here.}

Well, come on in and ask it. We don\'t bite. Really.

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
:::
