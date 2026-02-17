# PyTextile

::::: {#content dir="ltr" lang="en"}
# PyTextile {#PyTextile-1}

[PyTextile](http://pypi.python.org/pypi/textile){.http} is a *very* easy to use text-to-HTML converter.

You can test the following demonstration of Textile code, which can convert *this:*

    _This_ is a *test.*

    * One
    * Two
    * Three

    Link to "Slashdot":http://slashdot.org/

to *this:*

            <p><em>This</em> is a <strong>test.</strong></p>
     
     
    <ul>
            <li>One</li>
            <li>Two</li>
            <li>Three</li>
    </ul>
     
            <p>Link to <a href="http://slashdot.org/">Slashdot</a></p>

## Using PyTextile {#Using_PyTextile}

First, [download the latest PyTextile.](http://pypi.python.org/pypi/textile){.http}

Untar it, and enter the `textile` directory. Start a python interpreter.

Type:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0b0cc4b248d24332f3a2465f8cd24c1550fc37f2 dir="ltr" lang="en"}
   1 import textile
   2 
   3 s = """
   4 _This_ is a *test.*
   5 
   6 * One
   7 * Two
   8 * Three
   9 
  10 Link to "Slashdot":http://slashdot.org/
  11 """
  12 
  13 html = textile.textile( s )
  14 
  15 print html
```
:::
::::

You\'ll see beautiful HTML on the other side, ready for inclusion in a web page. ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}

### Options {#Options}

PyTextile takes 3 optional arguments:

    def textile(self, text, rel=None, head_offset=0, html_type='xhtml', sanitize=False):

## See Also: {#See_Also:}

[reStructuredText](reStructuredText) as a markup format to convert text to HTML.

# Discussion {#Discussion}

(none yet!)
:::::
