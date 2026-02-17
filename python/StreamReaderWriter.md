# StreamReaderWriter

::::: {#content dir="ltr" lang="en"}
The Python2.5\'s `codecs.StreamReaderWriter` combines [StreamReader](StreamReader) and [StreamWriter](StreamWriter). The wrapper will read narrow `str` strings from the underlying stream and decode them to `unicode` strings. On writing `unicode` data to the wrapper, it will encode them to narrow `str` strings.

The user of the wrapper should specify character sets by supplying class definitions for the respective stream reader and writer.

Pseudocode:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a24e65c6bde664170bb9d19f0888f94a3f874ad5 dir="ltr" lang="en"}
   1 class StreamReaderWriter:
   2     def __init__(self, stream, class_sr, class_sw):
   3         self.r = class_sr(stream)
   4         self.w = class_sw(stream)
   5 
   6     def read(self):
   7         return self.r.read()
   8 
   9     def write(self, data):
  10         return self.w.write(data)
```
:::
::::

The `codecs` module defines a function `codecs.open(name, encoding)` that returns an instance of `StreamReaderWriter` configured with the supplied encoding.

------------------------------------------------------------------------

See also: [StreamReader](StreamReader), [StreamWriter](StreamWriter), [StreamRecoder](StreamRecoder).

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
:::::
