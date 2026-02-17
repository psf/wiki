# FormatReference

::: {#content dir="ltr" lang="en"}
Formatting Cheat Sheet (string.format):

           "{" [field_name] ["!" conversion] [":" format_spec] "}"
              /                  "r"|"s"                   \
             /               (r)epr   (s)tr                 \
    arg_name                                                 \
    | ("." attribute_name | "[" element_index "]")*           \
    |        |                       |                         \
    |     identifier         integer | index_string            |
    |                                   (quotes                |
    [identifier                          not required)         |
     |integer]                                                 |
                                                               |
     _________________________________________________________/ \________
    /                                                                    \
          ":"
             [[fill]align][sign][#][0][width][,][.precision][type]
      [default]--> < left    +   |  |  (int)       (int)    b base 2
      [default --> > right  [-]  |  |                       c character
       for         ^ center " "  |  \                       d base 10
       numbers]    =             |   `zero padding          e exponent (e)
                                 |                          E exponent (E)
                                use 0b,0o,0x                f fixed point
                                 for 2  8 16                F ^^(same)^^
      b base 2     c character                 [default]--> g general (???)
      o base 8     s string                                 G general 2 (?)
      d base 10                                             n number (general 3)
      x base 16                                             o base 8
      X base 16                                             s string
      e, E    exponent                         (lower case) x base 16
      f, F, % fixed point                      (upper case) X base 16
      g, G, n (general numbers)                   (x100, f) % percentage

## See Also {#See_Also}

- [Format String Syntax](http://docs.python.org/library/string.html#format-string-syntax){.http} (Python 2.x documentation)

- \* [Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax){.https} (Python 3.x documentation)

- [Format Specification Mini-Language](http://docs.python.org/library/string.html#format-specification-mini-language){.http} (Python 2.x documentation)

- \* [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language){.https} (Python 3.x documentation)
:::
