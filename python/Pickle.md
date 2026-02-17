# Pickle

::: {#content dir="ltr" lang="en"}
# What is Pickle? {#What_is_Pickle.3F}

[http://docs.python.org/library/pickle.html](http://docs.python.org/library/pickle.html){.http}

# Should I use Pickle? {#Should_I_use_Pickle.3F}

Of course not.

- It is insecure. Untrusted pickles can do arbitrary things. For example, this pickle executes arbitrary Python expressions: `pickle.loads("c__builtin__\neval\n(c__builtin__\nraw_input\n(S'py> '\ntRtR.")`{.backtick}

- It is Python-only: pickles cannot be loaded in any other programming language / environment.

- It is schemaless and opaque. See: [http://bpaste.net/show/d0UZUSsAHtekA0pDiQzu/](http://bpaste.net/show/d0UZUSsAHtekA0pDiQzu/){.http}

# Alternatives {#Alternatives}

- The json module ([http://docs.python.org/library/json.html](http://docs.python.org/library/json.html){.http}) can handle dicts, lists, ints, floats, strings, booleans, and None. It cannot handle reference cycles, however. (pickle can.)

- PyYAML ([http://pyyaml.org/](http://pyyaml.org/){.http}) can handle everything json can, as well as having comments inside source data, and reference cycles. However, it defaults to an unsafe pickle-like loader.
:::
