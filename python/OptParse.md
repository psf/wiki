# OptParse

::::: {#content dir="ltr" lang="en"}
OptParse is a module introduced in Python2.3 that makes it easy to write command line tools. See \"[Option parsing tools](./Option(20)parsing(20)tools.html)\" for others. Note that OptParse is considered deprecated (in Python 2.7 and 3.2) in favor of the [argparse](http://docs.python.org/3/library/argparse.html){.http} module.

You give a description of the options that the program can receive, and OptParse will do reasonable stuff for you.

For example:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-6fe03808a88f14d45c8e9357ef029182efb2028b dir="ltr" lang="en"}
   1 import optparse
   2 
   3 if __name__=="__main__":
   4     parser = optparse.OptionParser("usage: %prog [options] arg1 arg2")
   5     parser.add_option("-H", "--host", dest="hostname",
   6                       default="127.0.0.1", type="string",
   7                       help="specify hostname to run on")
   8     parser.add_option("-p", "--port", dest="portnum", default=80,
   9                       type="int", help="port number to run on")
  10 
  11     (options, args) = parser.parse_args()
  12     if len(args) != 2:
  13         parser.error("incorrect number of arguments")
  14     hostname = options.hostname
  15     portnum = options.portnum
```
:::
::::

*args* contains your fixed arguments, *options* contains your values.

For example, `options.portnum` would contain the integer `80`, in the example above.

## References {#References}

- [Official Python optparse Documentation](http://docs.python.org/lib/module-optparse.html){.http}

## Complaints {#Complaints}

- optparse does not support \'required\' arguments. The documentation justifies this by saying \'options are optional\'. But look at python and its use of keyword arguments. And look at optparse iself! It has the required option \'action\'! optparse is a utility! Not a way to enforce a philosphy.

  See [this thread](http://mail.python.org/pipermail/getopt-sig/2002-February/000016.html){.http} in the retired [getopt-sig](http://mail.python.org/mailman/listinfo/getopt-sig){.http} mailing list. I also seem to remember a more protracted discussion about \"required\" arguments/options. *\-- David Boddie*
:::::
