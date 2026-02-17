# WritingExceptionClasses

::::::::: {#content dir="ltr" lang="en"}
# Writing Exception Classes {#Writing_Exception_Classes}

Exception classes are not special, you just derive them from Exception:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b0fff76fb9e1ec624c1dd2f46c1a7f45f04a43e5 dir="ltr" lang="en"}
   1 class HostNotFound(Exception):
   2     def __init__( self, host ):
   3         self.host = host
   4         Exception.__init__(self, 'Host Not Found exception: missing %s' % host)
```
:::
::::

You may later write:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-39476e85ab4877350c751c54ebf8029861778a5d dir="ltr" lang="en"}
   1 try:
   2     raise HostNotFound("taoriver.net")
   3 except HostNotFound, exc:
   4     # Handle exception.
   5     print exc  # -> 'Host Not Found exception: missing taoriver.net'
   6     print exc.host  # -> 'taoriver.net'
```
:::
::::

## See Also {#See_Also}

[HandlingExceptions](HandlingExceptions), [TracebackModule](./TracebackModule.html){.nonexistent}

## Questions {#Questions}

- How do you relay the traceback information? *Relay the traceback information? Moving it higher up the call-stack? Could you try to explain your question?*

  - When you\'re logging exceptions, you want access to the traceback information to. After some research, I believe what you use is extract_tb or extract_stack from the traceback module. \-- [LionKimbro](LionKimbro) 2003-09-07 15:23:43

  *Look at cgitb for how to do detailed TB introspection, and as an example of why mixing logic and (HTML) layout is a very bad thing.*

- What better exception-foo is out there?

  *[AlexMartelli](AlexMartelli)\'s \"Dos and Don\'ts\".*

- The new text involving `super` doesn\'t seem to work for me.

Using Python 2.3:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-399201797c6dedb76fe414df683661dbb6797404 dir="ltr" lang="en"}
   1 class LocalNamesSyntaxError(Exception):
   2     def __init__(self, msg):
   3         self.msg=msg
   4         super(LocalNamesSyntaxError, self).__init__('Local Names v1.1 Syntax Error: %s' % msg)
```
:::
::::

    Traceback (most recent call last):
      File "parser.py", line 92, in ?
        pprint.pprint(parse_text(test_string))
      File "parser.py", line 69, in parse_text
        cursor=parse_record_type(cursor,line,results)
      File "parser.py", line 43, in parse_record_type
        raise LocalNamesSyntaxError("unrecognized v1.1 record type- require LN, NS, X, or PATTERN")
      File "parser.py", line 17, in __init__
        super(LocalNamesSyntaxError, self)('Local Names v1.1 Syntax Error: %s' % msg)
    TypeError: super() argument 1 must be type, not classobj

Is this a Python2.4 v. Python2.3 thing? Or is there a simple error in my code? \-- [LionKimbro](LionKimbro)

super() only works for new-style classes. Exception is still an old-style class: type \'classobj\'. I\'ve fixed the example. \-- [JohannesGijsbers](JohannesGijsbers)

Thanks a lot, I was having hardtime figureing this out, as exactly the same construct worked in other places. \-- [HariDara](./HariDara.html){.nonexistent}

It might become a 2.4 vs 2.5 thing though, as 2.5 should allow new-style classes.

Don\'t forget the method name after `super`; it doesn\'t magically assume `__init__`. (fixed above) -kcarnold
:::::::::
