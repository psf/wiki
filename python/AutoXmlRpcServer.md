# AutoXmlRpcServer

:::::::::::: {#content dir="ltr" lang="en"}
This is an \"automatic [DocXmlRpcServer](DocXmlRpcServer).\" There is also a CGI variant: [AutoXmlRpcCgi](AutoXmlRpcCgi).

::: table-of-contents
Contents

1.  1.  [Tutorial](#Tutorial)
    2.  [Notes](#Notes)
    3.  [Code: xrserver.py](#Code:_xrserver.py)
2.  [Discussion](#Discussion)
:::

## Tutorial {#Tutorial}

Suppose you have a Python module:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-8435b0a743f29894f4e881444b26d95cf2ecbaf7 dir="ltr" lang="en"}
   1 def spam():
   2     return "spam"
```
:::
::::

How can you share that on [IRC?](http://www.irchelp.org/){.http}

Mark it like this:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-d4894e2547147338aec757b93719bc265d106b3f dir="ltr" lang="en"}
   1 XMLRPC_namespace = "eggs"
   2 
   3 def spam():
   4     return "spam"
```
:::
::::

Now, just run the AutoXmlRpcServer from that directory, and you\'re done!

    $ ./xrserver.py
    Sat Apr 16 21:29:24 2005 Application Starting.

You\'re XML-RPC server\'s up and running, port 8000.

Your friends can now call your function!

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1484af5e2699d69df10a68f68ab33182838630d4 dir="ltr" lang="en"}
   1 import xmlrpclib
   2 
   3 server = xmlrpclib.ServerProxy("http://example.com:8000/")
   4 print server.eggs.spam()
```
:::
::::

There it is!

## Notes {#Notes}

- What if you can\'t run a server? Use [AutoXmlRpcCgi](AutoXmlRpcCgi)!

- You can change the host and portname. Run \"./xrserver \--help\" for options.

- If you set XMLRPC_namespace to None, then namespaces aren\'t used.

- This code demonstrates [ModulesAsPlugins](ModulesAsPlugins), [DocXmlRpcServer](DocXmlRpcServer), [OptParse](OptParse), and (hopefully) [PythonStyle](PythonStyle).

- If you define a function \"uli\" (`def uli(msg):`), you can call it in IRC with [UliBot!](http://onebigsoup.wiki.taoriver.net/moin.cgi/UliBot){.http}

## Code: xrserver.py {#Code:_xrserver.py}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-57bf90880a739c5ba6ab21579b0d57c0e7111c9e dir="ltr" lang="en"}
   1 #!/usr/bin/env python
   2 """Serve specially marked modules by XML-RPC.
   3 
   4   -Hhostname   host name, default ""
   5   -Pportnum    port number, default 8000
   6 
   7 This script starts an XML-RPC server, and publishes auto-detected
   8 modules from the working directory.
   9 
  10 Functions within Modules that define the name "XMLRPC_namespace" are
  11 published. Function names that begin with an underscore (ex: _eggs) are
  12 not published. Functions are published within the XML-RPC namespace
  13 designated by the XMLRPC_namespace value, or the base namespace if the
  14 value is None.
  15 """
  16 
  17 import time
  18 import os
  19 import imp
  20 import types
  21 
  22 import optparse
  23 import DocXMLRPCServer
  24 
  25 
  26 def find_modules(path="."):
  27     """Return names of modules in a directory.
  28 
  29     Returns module names in a list. Filenames that end in ".py" or
  30     ".pyc" are considered to be modules. The extension is not included
  31     in the returned list.
  32     """
  33     modules = set()
  34     for filename in os.listdir(path):
  35         module = None
  36         if filename.endswith(".py"):
  37             module = filename[:-3]
  38         elif filename.endswith(".pyc"):
  39             module = filename[:-4]
  40         if module is not None:
  41             modules.add(module)
  42     return list(modules)
  43 
  44 
  45 def load_module(name, path=["."]):
  46     """Return a named module found in a given path."""
  47     (file, pathname, description) = imp.find_module(name, path)
  48     return imp.load_module(name, file, pathname, description)
  49 
  50 
  51 def find_xmlrpc_modules():
  52     """Find modules that define XMLRPC_namespace.
  53 
  54     Loads all modules in the current working directory. Returns a list
  55     of modules, the modules that define XMLRPC_namespace.
  56     """
  57     modules = [load_module(m) for m in find_modules()]
  58     xmlrpc_modules = []
  59     for m in modules:
  60         if m.__dict__.has_key("XMLRPC_namespace"):
  61             xmlrpc_modules.append(m)
  62     return xmlrpc_modules
  63 
  64 
  65 def functions_in_module(module):
  66     """Find all functions in a module."""
  67     functions = []
  68     for obj in module.__dict__.values():
  69         if isinstance(obj, types.FunctionType):
  70             functions.append(obj)
  71     return functions
  72 
  73 
  74 if __name__ == "__main__":
  75     parser = optparse.OptionParser(__doc__)
  76     parser.add_option("-H", "--host", dest="hostname",
  77                       default="127.0.0.1", type="string",
  78                       help="specify hostname to run on")
  79     parser.add_option("-p", "--port", dest="portnum", default=8000,
  80                       type="int", help="port number to run on")
  81 
  82     (options, args) = parser.parse_args()
  83     if len(args) != 0:
  84         parser.error("incorrect number of arguments")
  85 
  86     ServerClass = DocXMLRPCServer.DocXMLRPCServer
  87     server = ServerClass((options.hostname, options.portnum),
  88                          logRequests=0)
  89 
  90     for module in find_xmlrpc_modules():
  91         for func in functions_in_module(module):
  92             if func.__name__.startswith("_"):
  93                 continue
  94             full_name = func.__name__
  95             if module.XMLRPC_namespace is not None:
  96                 full_name = "%s.%s" % (module.XMLRPC_namespace,
  97                                        full_name)
  98             server.register_function(func, full_name)
  99 
 100     server.set_server_title("xrserver")
 101     server.register_introspection_functions()
 102 
 103     print time.asctime(), 'Application Starting.'
 104     server.serve_forever()
 105     print time.asctime(), 'Application Finishing.'
```
:::
::::

# Discussion {#Discussion}

This could be improved. Some ideas:

- Make it so you can specify modules (and possibly namespaces for them) with command line options. (hint: [OptParse](OptParse).)

- What if there\'s an exception while loading a module? What then?

- Respond gracefully to CTRL-C.

- Log modules successfully loaded.
  - If you\'re either brave or insane, make use of the [LoggingModule](./LoggingModule.html){.nonexistent}.

\-- [LionKimbro](LionKimbro) 2005-04-17 05:51:41
::::::::::::
