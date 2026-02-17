# MacPython/PhotoShop

::::: {#content dir="ltr" lang="en"}
[/AppscriptModule](./MacPython(2f)PhotoShop(2f)AppscriptModule.html){.nonexistent} scripting for [/PhotoShop](./MacPython(2f)PhotoShop(2f)PhotoShop.html){.nonexistent}

To apply unsharp mask to the first layer of the first document:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3d75479ca5665a59097d36cfd71a2e0d2dbe2c24 dir="ltr" lang="en"}
   1 ps = app("Adobe Photoshop CS")
   2 ps.filter_(ps.documents[1].art_layers[1], using=k.unsharp_mask, with_options={k.threshold:2, k.amount: 200.0, k.radius: 1.0})
```
:::
::::

You need the latest version of [/AppscriptModule](./MacPython(2f)PhotoShop(2f)AppscriptModule.html){.nonexistent} for the ` filter_() ` command to work correctly.
:::::
