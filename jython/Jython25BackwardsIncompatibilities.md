# Jython25BackwardsIncompatibilities

::: {#content dir="ltr" lang="en"}
\* You can no longer do `PyFile`{.backtick}(inputStream) directly from Jython code. This is because a `PyFile`{.backtick} that gets an `InputStream`{.backtick} \[INSERT REAL REASON\], so that the recommended approach is to replace code like:

    from java.io import FileInputStream
    from org.python.core import PyFile
    fis = FileInputStream("error.txt")
    pyf = PyFile(fis)

with code like:

    from java.io import FileInputStream
    from org.python.core.util import FileUtil
    fis = FileInputStream("error.txt")
    pyf = FileUtil.wrap(fis)

\* types.[ArrayType](./ArrayType.html){.nonexistent} has been removed as CPython never had it. Use array.[ArrayTypes](./ArrayTypes.html){.nonexistent} instead (which is available in both 2.2 and 2.5)

\* The pre and xreadlines modules have been removed
:::
