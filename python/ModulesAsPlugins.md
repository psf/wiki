# ModulesAsPlugins

:::::::::::: {#content dir="ltr" lang="en"}
Here\'s how to find all the modules in some directory, and import them.

::: table-of-contents
Contents

1.  1.  [Finding Modules in a Directory](#Finding_Modules_in_a_Directory)
    2.  [Importing the Modules](#Importing_the_Modules)
    3.  [Finding the Things Inside a Module](#Finding_the_Things_Inside_a_Module)
    4.  [Finding Functions Within a Module](#Finding_Functions_Within_a_Module)
    5.  [See Also](#See_Also)
2.  [Discussion](#Discussion)
:::

## Finding Modules in a Directory {#Finding_Modules_in_a_Directory}

Is there a better way than just listing the contents of the directory, and taking those tiles that end with \".pyc\" or \".py\"..?

But perhaps there isn\'t.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-608ee6802d2e0d5fd684c07c30c4722c5ef8250c dir="ltr" lang="en"}
   1 import os
   2 
   3 def find_modules(path="."):
   4     """Return names of modules in a directory.
   5 
   6     Returns module names in a list. Filenames that end in ".py" or
   7     ".pyc" are considered to be modules. The extension is not included
   8     in the returned list.
   9     """
  10     modules = set()
  11     for filename in os.listdir(path):
  12         module = None
  13         if filename.endswith(".py"):
  14             module = filename[:-3]
  15         elif filename.endswith(".pyc"):
  16             module = filename[:-4]
  17         if module is not None:
  18             s.add(module)
  19     return list(modules)
```
:::
::::

## Importing the Modules {#Importing_the_Modules}

How do you import a module, once you have it\'s name?

With the [ImpModule](ImpModule)! It dynamically loads named modules.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-dbd6584a1f7a79a0010c31c499f4c8989c445a52 dir="ltr" lang="en"}
   1 import imp
   2 
   3 def load_module(name, path=["."]):
   4     """Return a named module found in a given path."""
   5     (file, pathname, description) = imp.find_module(name, path)
   6     return imp.load_module(name, file, pathname, description)
   7 
   8 modules = [load_module(name) for name in find_modules()]
```
:::
::::

## Finding the Things Inside a Module {#Finding_the_Things_Inside_a_Module}

Once you have your module, you can look inside it, with `.__dict__`.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-39802305090c9383e3442921828f481b6233d6a6 dir="ltr" lang="en"}
   1 module.__dict__
```
:::
::::

## Finding Functions Within a Module {#Finding_Functions_Within_a_Module}

We just look for dictionary values that are of type `types.FunctionType`.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ac088e4acff8e22049974cb653d2e2385ab6240f dir="ltr" lang="en"}
   1 def functions_in_module(module)
   2     functions = []
   3     for obj in module.__dict__.values():
   4         if isinstance(obj, types.FunctionType):
   5             functions.append(obj)
   6     return functions
```
:::
::::

## See Also {#See_Also}

The [DocXmlRpcServer](DocXmlRpcServer) page includes code demonstrating the use of these techniques.

# Discussion {#Discussion}

I got this error when executing find_modules() in a package directory. That is the directory contained an ` __init.py__` file:

      File "C:\Python254\lib\site-packages\joedorocak\find_modules.py", line 27, in find_modules
        s.add(module)
    NameError: global name 's' is not defined

It looks to me like s needs to be initialized (some place near \"modules = set()\"). I\'m not sure what the protocol is here, so I\'m just going to leave this comment in the discussion.

Here\'s what seems to work for me. I got rid of \'s\' altogether.

    def find_modules(path="."):
        """Return names of modules in a directory.

        Returns module names in a list. Filenames that end in ".py" or
        ".pyc" are considered to be modules. The extension is not included
        in the returned list.
        """
        modules = set()
        for filename in os.listdir(path):
            module = None
            if filename.endswith(".py"):
                module = filename[:-3]
            elif filename.endswith(".pyc"):
                module = filename[:-4]
            if module is not None:
                modules.add(module)
        return list(modules)

All the best,

[JoeDorocak](./JoeDorocak.html){.nonexistent}
::::::::::::
