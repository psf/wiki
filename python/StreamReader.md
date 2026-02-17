# StreamReader

::::::: {#content dir="ltr" lang="en"}
As of Python2.5, `StreamReader` wraps (contains) a stream. It defines `read` and other respective methods to read the data from the stream and \"decode\" them. The class exposes all other methods of the stream instance.

Pseudocode of the `codecs.StreamReader` definition:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-263f3b8f4fdcb6c3dd7d5b0581b6badc48da286b dir="ltr" lang="en"}
   1 class StreamReader(Codec):
   2     def __init__(self, stream):
   3         ....
   4 
   5     def read(self):
   6         return self.decode(stream.read())
```
:::
::::

The `decode` method normally converts values of type `str` to `unicode`.

Codec modules will attach the `decode` method to the class definition derived from `StreamReader` during the initialization. An excerpt from `encodings.utf_8.StreamReader`:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a150414bba6f4c0a5d3aa30d90d2c20366270041 dir="ltr" lang="en"}
   1 class StreamReader(codecs.StreamReader):
   2     decode = codecs.utf_8_decode
```
:::
::::

------------------------------------------------------------------------

See also: [StreamWriter](StreamWriter), [StreamReaderWriter](StreamReaderWriter), [StreamRecoder](StreamRecoder).

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
:::::::
