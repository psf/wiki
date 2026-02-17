# BetterZope2BlobSupportSprint

::: {#content dir="ltr" lang="en"}
## Better Zope 2 Blob Support Sprint {#Better_Zope_2_Blob_Support_Sprint}

At [PyCon](PyCon) 2004, we came up with an interface that made it possible to quickly and efficiently return read-only filelike data (\"blobs\") to viewers of Zope websites. I\'d like continue this work, attempting to come up with a sane API which would allow us to persist pointers to bloblike objects into the ZODB and treat them like files for both read and write operations (particularly while maintaining transactional integrity for write operations).

\*\*NOTE\*\* This sprint is subsumed by the [ZodbSprint](ZodbSprint).
:::
