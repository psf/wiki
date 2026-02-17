# XmlRpc

::::::::: {#content dir="ltr" lang="en"}
# XML-RPC {#XML-RPC}

XML-RPC is a neat way to send messages across the Internet.

The neat thing about XML-RPC is that it transports *native data structures*- you can ship off lists, strings, dictionaries, and numbers.

You can [read more about it over on C2,](http://c2.com/cgi/wiki?XmlRpc "Wiki"){.interwiki} or on [the XML-RPC home page.](http://www.xmlrpc.com/){.http}

## Sample Code {#Sample_Code}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-8086857753664840679992df19b2887872ea8c2e dir="ltr" lang="en"}
   1 import xmlrpclib
   2 
   3 XMLRPC_SERVER_URL = "http://www.python.org/cgi-bin/moinmoin/?action=xmlrpc"
   4 
   5 pythoninfo = xmlrpclib.ServerProxy( XMLRPC_SERVER_URL )
   6 allpages = pythoninfo.getAllPages() # this is the XML-RPC call
   7 
   8 print ", ".join( allpages )
```
:::
::::

This code calls the [PythonInfo](PythonInfo) wiki, and receives the [TitleIndex](TitleIndex) as a list.

## Message Format {#Message_Format}

If you can communicate strings, you can do XML-RPC. You could even do it by e-mail!

Here\'s how to make your string:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-cb6dd057992b1f57597ccc4e31e6ce80310ed042 dir="ltr" lang="en"}
   1 import xmlrpclib
   2 
   3 func_name = "foo"
   4 arg_1 = "robot"
   5 arg_2 = { "some":1, "dict":2 }
   6 arg_3 = [1,2,3,4,5]
   7 
   8 call_string = xmlrpclib.dumps( (arg_1,arg_2,arg_3,), func_name )
```
:::
::::

\...resulting in the following `call_string` value:

    <?xml version='1.0'?>
    <methodCall>
    <methodName>foo</methodName>
    <params>
    <param>
    <value><string>robot</string></value>
    </param>
    <param>
    <value><struct>
    <member>
    <name>dict</name>
    <value><int>2</int></value>
    </member>
    <member>
    <name>some</name>
    <value><int>1</int></value>
    </member>
    </struct></value>
    </param>
    <param>
    <value><array><data>
    <value><int>1</int></value>
    <value><int>2</int></value>
    <value><int>3</int></value>
    <value><int>4</int></value>
    <value><int>5</int></value>
    </data></array></value>
    </param>
    </params>
    </methodCall>

\...which can then be turned *back* into Python data:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-df1bbfcdb669cceb1d3f9a9e3836b105d7a19d54 dir="ltr" lang="en"}
   1 call_data = xmlrpclib.loads( call_string )
```
:::
::::

\...which then builds:

    (('robot', {'some': 1, 'dict': 2}, [1, 2, 3, 4, 5]), u'foo')

That is, the first item is the arguments tuple, and the second item is the name of the function.

The capabilities are described under \"Convenience Functions\" in [the xmlrpclib documentation.](http://docs.python.org/lib/module-xmlrpclib.html){.http}

## See Also {#See_Also}

- [official xmlrpclib example](http://docs.python.org/lib/xmlrpc-client-example.html){.http}

- [xmlrpclib documentation](https://docs.python.org/2/library/xmlrpclib.html){.https}

- [XML-RPC: It Works Both Ways (onlamp.com)](http://www.onlamp.com/pub/a/python/2001/01/17/xmlrpcserver.html){.http}

- [DocXmlRpcServer](DocXmlRpcServer) - class to help make an XML-RPC server

- [Providing XML-RPC Services via CGI](http://effbot.org/zone/xmlrpc-cgi.htm){.http}
:::::::::
