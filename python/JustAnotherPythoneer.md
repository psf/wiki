# JustAnotherPythoneer

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content dir="ltr" lang="en"}
::: table-of-contents
Contents

1.  [Discussion](#Discussion)
2.  [The Problem](#The_Problem)
3.  [The Limited Set of Good Solutions](#The_Limited_Set_of_Good_Solutions)
4.  [The Larger Set of Not-So-Good Solutions](#The_Larger_Set_of_Not-So-Good_Solutions)
    1.  [Normal Printing/Concatination](#Normal_Printing.2FConcatination)
    2.  [Substitution](#Substitution)
    3.  [Reversal](#Reversal)
    4.  [Iteration](#Iteration)
    5.  [Slicing and Indexing](#Slicing_and_Indexing)
    6.  [Recursion](#Recursion)
    7.  [Decoding](#Decoding)
    8.  [Exception Handling](#Exception_Handling)
    9.  [Introspection](#Introspection)
    10. [Runtime Code](#Runtime_Code)
5.  [Credits](#Credits)
:::

## Discussion {#Discussion}

Perl coders are proud that Perl\'s motto is \"There\'s more than one way to do it.\"\
In comparison, Python is sometimes stereotyped as \"There\'s only one way to do it\", but this is of course not true. The Zen of Python, accessed via

    import this

includes the maxims:\
*Beautiful is better than ugly.*\
*Explicit is better than implicit.*\
*Simple is better than complex.*\
*Complex is better than complicated.*\
*Flat is better than nested.*\
*Sparse is better than dense.*\
*Readability counts.*\
*If the implementation is hard to explain, it\'s a bad idea.*\
*There should be one\-- and preferably only one \--obvious way to do it.*\

The net effect is that there is a limited set of good solutions for a given problem, and users are strongly encouraged to use them.

While Python attempts to discourage bad practices, and its indentation-based block structure and limited anonymous blocks (lambdas) make certain techniques difficult, it is possible to produce many more bad solutions than good for a given problem.

Please Feel Free to add/reorder/reallocate examples.

## The Problem {#The_Problem}

Your signature block (up to four lines of 78 characters each) needs code that prints \"Just another Pythoneer\".

## The Limited Set of Good Solutions {#The_Limited_Set_of_Good_Solutions}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-083a86991c3cf01ceccea1d0c8db3e3f5c757ab7 dir="ltr" lang="en"}
   1 print "Just another Pythoneer"
```
:::
::::

(Though someone may point out that as a Python user following correct Pythonic practice, you are more correctly a *Pythonista*\... and give you a brief 6000 word essay on the historical debate over the naming of Python Users and the etymology of the root *Python* and the stem *-ista*\... and advise you against using the combination in an impromptu Spanish examination)

## The Larger Set of Not-So-Good Solutions {#The_Larger_Set_of_Not-So-Good_Solutions}

### Normal Printing/Concatination {#Normal_Printing.2FConcatination}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-7cf255c7ad9fb2e17f55c4314992a0b4d2d9ac60 dir="ltr" lang="en"}
   1 print "Just", "another", "Pythoneer"
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4db91f00d342e6edbf9fb262db559b1f63e2e016 dir="ltr" lang="en"}
   1 print "Just "\
   2       "another "\
   3       "Pythoneer"
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-77d8bb424c5192f6c9aabd66e6546cdf6f6774fd dir="ltr" lang="en"}
   1 j = "Just "
   2 a = "another "
   3 p = "Pythoneer"
   4 print j+a+p
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-d32dc74025c46480608dd862a3ac72ce7c922450 dir="ltr" lang="en"}
   1 import sys; sys.stdout.write("Just another Pythoneer\n")
```
:::
::::

### Substitution {#Substitution}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-36ad6dd9a6fd12936ff2fb799ab28567dd212f3a dir="ltr" lang="en"}
   1 print '''%s %s %s''' % ("Just", "another", "Pythoneer")
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c11bc6d8734c75ac984c97cf51773ba1eec10de3 dir="ltr" lang="en"}
   1 print '%(j)s %(a)s %(py)s' % { "j": "Just", "a": "another", \
   2   "pl": "Perl Hacker", "py": "Pythoneer", "c": "C Coder", \
   3   "f": "Fortran Freak", "turtle" : "Logo Lover" }
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-65e4045a97f493b29e0dea4c25bcb3bbd77f6bfd dir="ltr" lang="en"}
   1 class JAPy(int):
   2     def __str__(self):
   3         return "%s"*5%("Just",chr(self),"another", chr(self), "Pythoneer")
   4 print JAPy(32)
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-39d011983270e14d01be25af9f262168b466fc1b dir="ltr" lang="en"}
   1 class JAPy(int): pass
   2 def s(s): s+=1; return "Just" + chr(s) + "another" + chr(s) + "Pythoneer"
   3 n, JAPy.__str__ = JAPy(31), s
   4 print n
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-da3d74cf27da69fa9881d46af6e7db3ea8262462 dir="ltr" lang="en"}
   1 print "Just another Perl Hacker".replace("Perl Hacker", "Pythoneer")
```
:::
::::

### Reversal {#Reversal}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3e81e95c39cb5c99635ab361df591f64e07735d8 dir="ltr" lang="en"}
   1 x = ['r','e','e','n','o','h','t','y','P',' ','r','e','h','t','o','n','a',' ',
   2      't','s','u','J']
   3 x.reverse()
   4 print "".join(x)
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-cec9465347975474ae5742aba7b2b53dabba29fb dir="ltr" lang="en"}
   1 print "".join(['r','e','e','n','o','h','t','y','P',' ','r','e','h','t','o','n',
   2                'a',' ','t','s','u','J'][::-1])
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4a86384e5610d5500b204b1ac5d4bb046b2b5f2e dir="ltr" lang="en"}
   1 print "reenohtyP rehtona tsuJ"[::-1]
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-d36b63aba3abde1eaccd3f596f162e593f683bb7 dir="ltr" lang="en"}
   1 print "".join([x for x in list('reenohtyP rehtona tsuJ')[::-1]])
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9ec6844521cd96e8c18d75b0ca671ec1f137d9fd dir="ltr" lang="en"}
   1 print "".join([x for x in list('reenohtyP rehtona tsuJ')][::-1])
```
:::
::::

### Iteration {#Iteration}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9b7a8b2ee5fc1abc1909c07fffcb156a0a28040a dir="ltr" lang="en"}
   1 import sys
   2 for c in "Just another Pythoneer\n":
   3     sys.stdout.write(c)
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b56cf9f496cf10b3e7bfd0ec9f6ae9af2b98f30e dir="ltr" lang="en"}
   1 import sys; [sys.stdout.write(c) for c in "Just another Pythoneer\n"]
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-d7a34c2f00e0209d922efb71e723d6124071809b dir="ltr" lang="en"}
   1 x = ["Just", "another", "Pythoneer"]
   2 while x: print x[0], ; x = x[1:]
   3 print
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-e25152b10db0bfd650425ccf61de98bb7bb62a84 dir="ltr" lang="en"}
   1 x = ["Pythoneer", "another", "Just",]
   2 while x: print x[-1], ; x.pop()
   3 print
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-bfec4e7fcef68bee217e7343c1b82a979dffa151 dir="ltr" lang="en"}
   1 import random, sys; x = "Just another Pythoneer\n"
   2 while x:
   3   y = random.choice(x);
   4   if y == x[0]: sys.stdout.write(y); x = x[1:]
```
:::
::::

### Slicing and Indexing {#Slicing_and_Indexing}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a5dc8ee15617a82b7550d311bab9ec19725f28b4 dir="ltr" lang="en"}
   1 print "Just another Pythoneer and not a Perl Hacker".split(" and")[0]
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1e3fc4a66854fc64de95697aed4c4eb3532d666e dir="ltr" lang="en"}
   1 print "I'm just another Pythoneer".split(" ",1)[1].capitalize()
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-671e0dd58f122868dd46384c3d56d218275fe585 dir="ltr" lang="en"}
   1 import re
   2 a = ["Pythoneer", "extra", "Just", "words", "another", "Hello!"]
   3 m = re.match("(?P<three>\d+).(?P<one>\d+).(?P<two>\d+)", "1A5l2")
   4 print a[m.start("one")], a[m.start("two")], a[m.start("three")]
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-77e13a7ae0d768268af2fe8951f912986fa86e44 dir="ltr" lang="en"}
   1 #Sometimes_code_does_not_really_need_to_have_syntacally_significant_whitespace
   2 g,u,n=range(3),"Why don't I use Java or Perl?",lambda(x),y:reduce(x.__add__,y)
   3 print"".join([u[P:H+P]for(H,P)in(zip(n(list,n(tuple,[([d],n(list,[[1+c%2]*(c+1
   4 )for(c)in(g)]))for(d)in(g)])[1:]),[16,12,8,19,6,5,8,1,25,23,2,8,1,5,14,25]))])
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-8ceaa33692141ee8eaf6d2a78eb1b55ceeef5b13 dir="ltr" lang="en"}
   1 import platform as p; d=[list(x)for x in open(p.__file__[:-1])]; a=d[28]+d[12]
   2 for f,t in zip([0,5,7,8,10,12,19,20,21,22],[15,6,9,14,19,41,25,24,23,99]):
   3     del a[f:t]; a[8]=a[8].lower()
   4 print "".join(a)
```
:::
::::

### Recursion {#Recursion}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f3fec9b3adba24ada4f32973790950b3cbc9dd75 dir="ltr" lang="en"}
   1 japy = lambda x: isinstance(x,dict) and x.keys()[0] + japy(x.values()[0]) or x
   2 print japy({"Just ": {"another ": "Pythoneer"}})
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4b43524936e2505031a4bbbe3539ec94d39f8747 dir="ltr" lang="en"}
   1 def k(x):
   2     if type(x) == type({}): return x.keys()[0] + k(x.values()[0])
   3     return x
   4 print k({"Just ": {"another ": "Pythoneer"}})
```
:::
::::

### Decoding {#Decoding}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-02983f0de33b757535765f6d429f7a0603744ba3 dir="ltr" lang="en"}
   1 import uu, StringIO
   2 s = StringIO.StringIO(); uu.decode(StringIO.StringIO('begin 666 '+\
   3   '-\01262G5S="!A;F]T:&5R(%!Y=&AO;F5E<@  \012 \012end\012'), s)
   4 print s.getvalue()
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a82e19ac4039d90aa048ef8018cc7b9fd36b067f dir="ltr" lang="en"}
   1 d,o=0x3B55094199ACFB742DB37F3F97B11175C0C8EL,[]
   2 while d:
   3     d,m=divmod(d,100);o.append(chr(m+32))
   4 print "".join(o)
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-fc972821a5c73c7aa04c43ce4941a41bff4e1c31 dir="ltr" lang="en"}
   1 def japy(d=0x3B55094199ACFB742DB37F3F97B11175C0C8EL):
   2     while d:
   3         d,m=divmod(d,100);yield m+32
   4 print "".join([chr(x) for x in japy()])
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b67e1809d3d8f81aaaa9a9b8f0e5f2f2256f0cdd dir="ltr" lang="en"}
   1 import pickle; print pickle.loads("S'Just another Pythoneer'\012p0\012.")
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-6ebfee57870b903d93999c5ed98e61b7c5b7de9f dir="ltr" lang="en"}
   1 print u"Whfg nabgure Clgubarre".encode('rot13')
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-5790f28b2a318c4149376c88e295a919966d50bc dir="ltr" lang="en"}
   1 d,n=dict(zip("0123456789ABx"," aehnosturyPJ")), 10157833755785421529629225
   2 print "".join([d[c] for c in str(hex(n))[:-1]]).strip()
```
:::
::::

### Exception Handling {#Exception_Handling}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-01bc5eaf38615213c5ad100ab9ccf9e2d336ad35 dir="ltr" lang="en"}
   1 try:
   2   vars()["Just another Pythoneer"]
   3 except KeyError, e:
   4   print eval(str(e))
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0fe5958e68aff607f7dabf5363e3c2abab03b090 dir="ltr" lang="en"}
   1 try:
   2   raise "Just another Pythoneer"
   3 except:
   4   print sys.exc_info()[0]
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4490b5f1300b98c1523c44dcdd1021b0df7b274b dir="ltr" lang="en"}
   1 try: __import__("Just another Pythoneer")
   2 except ImportError, m: print str(m)[-22:]
```
:::
::::

### Introspection {#Introspection}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-6c31e841dc27ad9447ab0d6e672085c4ac57d0e4 dir="ltr" lang="en"}
   1 """Just another Pythoneer"""
   2 print __doc__
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c37db1fd1dc2068bff5feb0add16937a2dde4798 dir="ltr" lang="en"}
   1 class Print:
   2     def __call__(self): print
   3     def __getattr__(self, name): print name, ; return self
   4 Print().Just.another.Pythoneer()
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ed35cec5caaeda61eb5d647dde0d1b3016dc66e6 dir="ltr" lang="en"}
   1 class JAPy: pass
   2 def i(self,x="Just another Pythoneer"): pass
   3 def s(self): return self.__init__.func_defaults[0]
   4 print JAPy.__dict__.update({"__init__":i,"__str__":s}) or JAPy()
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4d6943a1db50d6c9a6ecae119a5956afba02fd24 dir="ltr" lang="en"}
   1 class func_defaults:
   2     func_defaults = "Just another Pythoneer";func_defaults=lambda \
   3     func_defaults = func_defaults:func_defaults.func_defaults.func_defaults[0]
   4 print func_defaults.func_defaults(func_defaults())
```
:::
::::

    class func_defaults:
        func_defaults = "Just another Pythoneer"
        def func_defaults(func_defaults=func_defaults):pass
    func_defaults,=func_defaults().func_defaults.func_defaults;print func_defaults

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-311ad5647441698951f87e8de4fcfda9f417cc7c dir="ltr" lang="en"}
   1 class Just_another_Pythoneer(object):
   2     def __init__(self):
   3         print " ".join(self.__class__.__name__.split("_"))
   4 Just_another_Pythoneer()
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-635056b3754a03a1c9cd9d0f9259be5190b5f964 dir="ltr" lang="en"}
   1 def Just_another_Pythoneer(fn):
   2     print fn.func_name.replace("_"," ")
   3 Just_another_Pythoneer(Just_another_Pythoneer)
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-76cdd8e593ed1bdcef92a81a4fde2e7050988d52 dir="ltr" lang="en"}
   1 def _(Just, another, Pythoneer):_
   2 print " ".join(_.func_code.co_varnames)
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-944d5eac0ed6fa9e35673ecee34796db60e8251c dir="ltr" lang="en"}
   1 def f(z):
   2   '''Just another Pythoneer (and remember to document your code!)'''
   3   pass
   4 print f.__doc__[:22]
```
:::
::::

### Runtime Code {#Runtime_Code}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9e147d91e116c33ffaeb18722116afc43788d9b5 dir="ltr" lang="en"}
   1 exec "print 'Just another Pythoneer'"
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-e07e375035f922f7fffb51ae07318fb4898c475e dir="ltr" lang="en"}
   1 x = compile("print 'Just another Pythoneer'\n", "japy", "single")
   2 eval(x)
```
:::
::::

## Credits {#Credits}

[AndrewDalke](./AndrewDalke.html){.nonexistent}\
[HansNowak](./HansNowak.html){.nonexistent}\
\"Snippet 181\"\
[TaroOgawa](./TaroOgawa.html){.nonexistent}\
[KazuoMoriwaka](./KazuoMoriwaka.html){.nonexistent}\
\"just another Pythoneer\"
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
