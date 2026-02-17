# AlternateLambdaSyntax

::::::::::::::::::::::::::::::::::::::::::::::: {#content dir="ltr" lang="en"}
As it stands, Guido van Rossum has suggested that lambda forms will disappear in [Python3.0](./Python3(2e)0.html). This started a number of threads on comp.lang.python suggesting alternate syntaxes for lambda in the hopes that one of them might be more amenable to GvR\'s tastes. This pages summarizes these suggestions.

- Update: GvR has changed his tune; lambda will remain unchanged.

  (Reference: [http://mail.python.org/pipermail/python-dev/2006-February/060415.html](http://mail.python.org/pipermail/python-dev/2006-February/060415.html){.http}). This page is kept as a historic record only \-- none of the proposals below satisfied GvR\'s taste.

The main hope of this page is to find a way to retain the functionality of existing Python lambdas - a way to create simple deferred expressions within another expression. For many uses (e.g. lazy argument evaluation, or simple callbacks) separating the deferred expression out into a named function can actually reduce clarity, as it overemphasises the deferred expression at the expense of the expression that the deferred expression is only one part of.

## Goals for Alternate Form {#Goals_for_Alternate_Form}

### Definitely Desirable Features {#Definitely_Desirable_Features}

- Acceptable to BDFL
  - If Guido doesn\'t like it, it ain\'t gonna happen!
- At least as capable as current lambda expressions
  - If a new syntax is to replace the status quo, it needs to be at least equivalent in expressiveness
- More Pythonic / Less ugly
  - The current lambda syntax simply doesn\'t blend well with the rest of Python\'s syntax. A syntax which mixes in with other expressions as cleanly as list comprehensions and generator expressions do should have a much better chance of gaining BDFL approval.
- More friendly to inexperienced users
  - Compared to other Python keywords, \'lambda\' is rather esoteric. In the challenge for \"farthest outside day-to-day English usage\", its closest competitor would probably be \'assert\', as even \'def\' and \'elif\' are just abbreviations for \'define\' and \'else if\'. Use of simpler keywords may make deferred expressions appear less intimidating than they seem with the current unusual keyword.
- Less external baggage
  - One of the problems with lambda is that developers familiar with lambda calculus expect more of it than it provides. They expect full anonymous functions, whereas Python\'s lambda expressions allow deferred evaluation of only a single expression. An alternate syntax described as providing deferred evaluation of expressions rather than anonymous functions may be less prone to trigger complaints about the single expression limitation (consider: how often are complaints heard regarding the restriction of the expression section of list comprehensions or generator expressions to single expressions?).

### Arguably Desirable Features {#Arguably_Desirable_Features}

- Support anonymous suites
  - No discussion of lambda is complete without it being suggested that it should be possible to embed entire suites inside expressions. Accordingly, some suggestions along these lines are included below under the heading Real Closures.

## Current Syntax {#Current_Syntax}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-01af740678751d309ba94660711c4d205130f8dc dir="ltr" lang="en"}
   1 lambda a, b, c:f(a) + o(b) - o(c)
   2 lambda x: x * x
   3 lambda : x
   4 lambda *a, **k: x.bar(*a, **k)
   5 ((lambda x=x, a=a, k=k: x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

## New Syntaxes {#New_Syntaxes}

### Args Before Expression {#Args_Before_Expression}

Alyssa Coghlan: def-to syntax [1](./(5b).html#a){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0ba7b04642be29e84173abb7618c645828b031e7 dir="ltr" lang="en"}
   1 (def (a, b, c) to f(a) + o(b) - o(c))
   2 (def (x) to x * x)
   3 (def () to x)
   4 (def (*a, **k) to x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) to x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: def-arrow syntax [1](./(5b).html#a){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-57558e0a98e649a5e6600b674cce874a419e296a dir="ltr" lang="en"}
   1 (def (a, b, c) -> f(a) + o(b) - o(c))
   2 (def (x) -> x * x)
   3 (def () -> x)
   4 (def (*a, **k) -> x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) -> x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alex Martelli: def-as syntax [2](./(5b).html#b){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-36e935945f4d44de57220dae9d2566a706eb8723 dir="ltr" lang="en"}
   1 (def (a, b, c) as f(a) + o(b) - o(c))
   2 (def (x) as x * x)
   3 (def () as x)
   4 (def (*a, **k) as x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) as x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Dave Benjamin: fun syntax [7](./(5b).html#g){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ac277f2bb1fe31c5227c3e33c587ceddd6e7242b dir="ltr" lang="en"}
   1 (fun(a, b, c): f(a) + o(b) - o(c))
   2 (fun(x): x * x)
   3 (fun(): x)
   4 (fun(*a, **k): x.bar(*a, **k))
   5 ((fun(x=x, a=a, k=k): x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Roman Suzi: quote-colon syntax [9](./(5b).html#i){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-31def791bc8b0929090bae03e4badbe68219b9d0 dir="ltr" lang="en"}
   1 ` a, b, c:f(a) + o(b) - o(c)
   2 ` x: x * x
   3 ` : x
   4 ` *a, **k: x.bar(*a, **k)
   5 ((` x=x, a=a, k=k: x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Ka-Ping Yee: arrow syntax

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f03570bc1559df3270bfd8603b8339af4db418b3 dir="ltr" lang="en"}
   1 a, b, c -> f(a) + o(b) - o(c)
   2 x -> x * x
   3 -> x
   4 *a, **k -> x.bar(*a, **k)
   5 ((x=x, a=a, k=k) -> x(*a, **k) for x, a, k in funcs_and_args_list)
```
:::
::::

to-syntax

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-fe9dae230c68232673f30aba42acbe6305787bf0 dir="ltr" lang="en"}
   1 a, b, c to f(a) + o(b) - o(c)
   2 x to x * x
   3 to x
   4 *a, **k to x.bar(*a, **k)
   5 ((x=x, a=a, k=k) to x(*a, **k) for x, a, k in funcs_and_args_list)
```
:::
::::

Tom Anderson: anonymous def syntax, normal form [12](./(5b).html#j){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9f99fba557d8bcc82e8028d3f917e8abade4c00b dir="ltr" lang="en"}
   1 def (a, b, c): return f(a) + o(b) - o(c)
   2 def (x): return x * x
   3 def (): return x
   4 def (*a, **k): return x.bar(*a, **k)
   5 ((def (x=x, a=a, k=k): return x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Tom Anderson: anonymous def syntax, shorthand form [12](./(5b).html#j){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0053c004264d866e530f49630addd5ff681d756c dir="ltr" lang="en"}
   1 def (a, b, c) = f(a) + o(b) - o(c)
   2 def (x) = x * x
   3 def () = x
   4 def (*a, **k) = x.bar(*a, **k)
   5 ((def (x=x, a=a, k=k) = x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Anders Munch: bare def syntax

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-843bd6fa2d5efe6d0bd61fea7520ed1a7acf5744 dir="ltr" lang="en"}
   1 (def (a, b, c) f(a) + o(b) - o(c))
   2 (def (x) x*x)
   3 (def () x)
   4 (def (*a, **k) x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

### Expression Before Args {#Expression_Before_Args}

Alyssa Coghlan: post-def syntax This is based on the \"normally nested expression before statement keyword\" idiom used with generator expressions, list comprehensions and PEP 308 conditional expressions.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3bc9c45cf5b40ad6d605df2e1681834cc0191c8d dir="ltr" lang="en"}
   1 (f(a) + o(b) - o(c) def (a, b, c))
   2 (x * x def (x))
   3 (x def ()) # Making the empty param list optional would be good for lazy arguments: (x def)
   4 (x.bar(*a, **k) def (*a, **k))
   5 ((x(*a, **k) def (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: for syntax [6](./(5b).html#f){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b056b41ec54f6c76b6a6084c8e732827c600bb77 dir="ltr" lang="en"}
   1 (f(a) + o(b) - o(c) for (a, b, c))
   2 (x * x for (x))
   3 (x for ())
   4 (x.bar(*a, **k) for (*a, **k))
   5 ((x(*a, **k) for (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Robert Brewer: for (no-parens) syntax [3](./(5b).html#c){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0f272afc872f0fbee26dd6495d6827783464d488 dir="ltr" lang="en"}
   1 (f(a) + o(b) - o(c) for a, b, c)
   2 (x * x for x)
   3 (x for ())
   4 (x.bar(*a, **k) for *a, **k)
   5 ((x(*a, **k) for (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: def-from syntax [4](./(5b).html#d){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-132ccee6862d726c188f90a03743aa64b8ab8d1e dir="ltr" lang="en"}
   1 (def f(a) + o(b) - o(c) from (a, b, c))
   2 (def x * x from (x))
   3 (def x from ())
   4 (def x.bar(*a, **k) from (*a, **k))
   5 ((def x(*a, **k) from (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: from syntax (posted to clp, no reference handy)

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b3900b75fe092e39c059e6f8266b2472f8db69d8 dir="ltr" lang="en"}
   1 (f(a) + o(b) - o(c) from (a, b, c))
   2 (x * x from (x))
   3 (x from ())
   4 (x.bar(*a, **k) from (*a, **k))
   5 ((x(*a, **k) from (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Michael Spencer: from-args syntax [5](./(5b).html#e){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f064e8fed6afa53a58e878bbd2b8d52e40d7d6a8 dir="ltr" lang="en"}
   1 (f(a) + o(b) - o(c) from args(a, b, c))
   2 (x * x from args(x))
   3 (x from args())
   4 (x.bar(*a, **k) from args(*a, **k))
   5 ((x(*a, **k) from args(x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Michael Spencer: for-args syntax [5](./(5b).html#e){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-370ec7fd27955aea72ffdb44bfc285f9d3c6838b dir="ltr" lang="en"}
   1 (f(a) + o(b) - o(c) for args(a, b, c))
   2 (x * x for args(x))
   3 (x for args())
   4 (x.bar(*a, **k) for args(*a, **k))
   5 ((x(*a, **k) for args()) for x, a, k in funcs_and_args_list)
```
:::
::::

Bengt Richter: colon-function-application syntax [8](./(5b).html#h){.nonexistent}\]

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4dafa711a0d3a993f4762ed2b1b25cc5d3a60921 dir="ltr" lang="en"}
   1 (:f(a) + o(b) - o(c))(a, b, c)
   2 (:x*x)(X)
   3 (:x)()
   4 (:x.bar(*a, **k))(*a, **k)
   5 ((:x(*a, **k))(x=x, a=a, k=k) for x, a, k in funcs_and_args_list)
```
:::
::::

Talin: \'given\' keyword (Same as the \'for no parens\' except uses a different keyword.)

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-139fc26ef77cff996792d1312b53e9833f080342 dir="ltr" lang="en"}
   1 (f(a) + o(b) - o(c) given a, b, c)
   2 (x * x given x)
   3 (x given ())
   4 (x.bar(*a, **k) given *a, **k)
   5 ((x(*a, **k) given (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

### functional syntax {#functional_syntax}

[lwickjr](lwickjr): How about converting the `lambda` functionality into a function? For example, in pure can-do-now Python:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ae8771ba6b295c346c60ad93d100950747d06743 dir="ltr" lang="en"}
   1 from types import FunctionType as function
   2 def anonymous(
   3         name=None,
   4         filename=None,
   5         mode="eval",
   6         func_globals=None,
   7         func_closure=None,
   8         func_argdefs=(),
   9         flags=0,
  10         dont_inherit=False,
  11         source=None,
  12         code=None,
  13         ):
  14         """Create a possibly anonymous function inline"""
  15         ## Compute suitable default values from stack frame, omitted for brevity.
  16         if source: code = compile(soource, filename, mode, flags, dont_inherit=True)
  17         return function(code, func_globals, name, func_argdefs, func_closure)
```
:::
::::

If you don\'t like `anynomous` for the name, suggest something else! ![;)](/wiki/europython/img/smile4.png ";)"){height="16" width="16"}

### Real Closures {#Real_Closures}

Real closures subsume the functionality of lambda plus allow for multi-line statements.

------------------------------------------------------------------------

Curly braces for single-line and anonymous def for multi-line (from [10](./(5b).html#h){.nonexistent}\], boo [11](./(5b).html#h){.nonexistent}\], and this is also very similar to how Ruby does it):

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-50b4fd47e5becdad3b5b94d030a5cd29969633d4 dir="ltr" lang="en"}
   1 #single-line (similar to ruby syntax)
   2 {a,b,c | return f(a) + o(b) - o(c)}
   3 {x | return x*x}
   4 {return x}
   5 {*a, **k | return x.bar(*a, **k)}
   6 
   7 #multi-line
   8 x = def (a,b,c):
   9     return f(a) + o(b) - o(c)
```
:::
::::

------------------------------------------------------------------------

Perhaps anonymous def for single line, anonymous def for single-line?

    foo.addCallback(def (result): result + 1)
    foo.addCallback(def (result, myExtra, args):
                         print 'hi!'
                         result += 1
                         return result
                    , extra, args=here)

Tom Anderson\'s syntax (which is subtly different - it still wants a return in single-line anonymous defs) could also be used for multi-line closures in this way.

## References {#References}

- \[1\] [http://mail.python.org/pipermail/python-list/2004-December/256859.html](http://mail.python.org/pipermail/python-list/2004-December/256859.html){.http}

- \[2\] [http://mail.python.org/pipermail/python-list/2004-December/256881.html](http://mail.python.org/pipermail/python-list/2004-December/256881.html){.http}

- \[3\] [http://mail.python.org/pipermail/python-list/2004-December/257023.html](http://mail.python.org/pipermail/python-list/2004-December/257023.html){.http}

- \[4\] [http://boredomandlaziness.skystorm.net/2004/12/anonymous-functions-in-python.html](http://boredomandlaziness.skystorm.net/2004/12/anonymous-functions-in-python.html){.http}

- \[5\] [http://mail.python.org/pipermail/python-list/2004-December/257893.html](http://mail.python.org/pipermail/python-list/2004-December/257893.html){.http}

- \[6\] [http://mail.python.org/pipermail/python-list/2004-December/257977.html](http://mail.python.org/pipermail/python-list/2004-December/257977.html){.http}

- \[7\] [http://mail.python.org/pipermail/python-list/2005-January/258441.html](http://mail.python.org/pipermail/python-list/2005-January/258441.html){.http}

- \[8\] [http://mail.python.org/pipermail/python-list/2005-January/258578.html](http://mail.python.org/pipermail/python-list/2005-January/258578.html){.http}

- \[9\] [http://mail.python.org/pipermail/python-list/2005-January/258581.html](http://mail.python.org/pipermail/python-list/2005-January/258581.html){.http}

- \[10\] [http://mail.python.org/pipermail/python-list/2005-January/258113.html](http://mail.python.org/pipermail/python-list/2005-January/258113.html){.http}

- \[11\] [http://boo.codehaus.org/Closures](http://boo.codehaus.org/Closures){.http}

- \[12\] [http://mail.python.org/pipermail/python-list/2005-June/287966.html](http://mail.python.org/pipermail/python-list/2005-June/287966.html){.http}
:::::::::::::::::::::::::::::::::::::::::::::::
