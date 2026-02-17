# ComparisonJavaJython

:::: {#content dir="ltr" lang="en"}
Describe ComparisonJavaJython here.

::: {}
  ------------------ ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------
  **Description**    **In Java**                                                                              **In Jython**
  array of doubles   xCoord = Double\[25\]                                                                    xCoord = jarray.zeros(25, \"d\")
  Size of array      mx = data.length;                                                                        mx = len(data)
  array assignment   double re = reFun.evaluate(new double\[\] {data\[i\]\[j\]\[0\], data\[i\]\[j\]\[1\]});   re = self.reFun.evaluate(\[data\[i\]\[j\]\[0\], data\[i\]\[j\]\[1\]\])
  ------------------ ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------
:::
::::
