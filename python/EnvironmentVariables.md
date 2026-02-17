# EnvironmentVariables

::::: {#content dir="ltr" lang="en"}
## Bash-like Global Substitution {#Bash-like_Global_Substitution}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-cfe76820d3e964222eb4083dd1ab4607d1a571ab dir="ltr" lang="en"}
   1 globals().update(os.environ)  # Import environment
   2 
   3 
   4 def replace_w_global_value(mo):
   5     key = mo.group(0)
   6     without_dollar = key[1:]
   7     return str(globals().get(without_dollar, key))
   8 
   9 
  10 def subs(input):
  11     """Perform Bash-like substitutions.
  12 
  13     Any "$FOO" in a string will be replaced with the value of FOO.
  14     If it's not defined, it stays as it was: "$FOO".
  15     """
  16     return re.sub('[$][A-Za-z_]+', replace_w_global_value, input)
```
:::
::::

# Discussion {#Discussion}

The only question I have is: Is there a way to make all assignments within the module, automatically call `os.putenv`?

So, intercept assignment with [setattr]{.u} or something, on the module.

I don\'t know how to get a handle to the current module, though.

\-- [LionKimbro](LionKimbro) 2005-12-16 20:37:07
:::::
