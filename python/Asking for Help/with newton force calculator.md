# Asking for Help/with newton force calculator

:::::::::: {#content dir="ltr" lang="en"}
# Asking for Help: with newton force calculator {#Asking_for_Help:_with_newton_force_calculator}

## Verables: {#Verables:}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-fe2744776f7edcb20937cd07cb9025c89c174290 dir="ltr" lang="en"}
N = newton force,
M = Mass,
X = X axis,
Z = Z axis,
Y = Y axis,
YR = Yaw,
PR = Pitch,
RR = Roll,
XA = X axis acceleration,
ZA = Z axis acceleration,
YA = Y axis acceleration,
YRA = Yaw acceleration,
PRA = Pitch acceleration,
RRA = Roll acceleration,
obj = 3D object
```
:::
::::

## get values from main app: {#get_values_from_main_app:}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-a50b7c4c9e1f6ab33300cfe24cac0d4f3989c0f9 dir="ltr" lang="en"}
obj_Main.M = 3000 MTons,
obj_thruster is parented to obj_main,
obj_thruster.X = 10,
obj_thruster.Z = 20,
obj_thruster.Y = 30, 
obj_thruster.YR = 90,
obj_thruster.PR = 180,
obj_thruster.RR = 270,
Obj_thruster.N.X = 400 MTons
```
:::
::::

## calculate acceleration: {#calculate_acceleration:}

### Need help finding code to go here {#Need_help_finding_code_to_go_here}

the calculator gives me

## out put to main app: {#out_put_to_main_app:}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-3b0d8b023d947fa6c9fdfb3e181c0ea1f404ae42 dir="ltr" lang="en"}
obj_main.XA,
obj_main.ZA,
obj_main.YA,
obj_main.YRA, 
obj_main.PRA,
obj_main.RRA
```
:::
::::

I will run the calculator once for every thruster on the obj. Add them together and get haw the object moves in space. then do it again and add both to see how fast the obj is moving now. And where it has moved to. this way I can set the obj to travel though space in a realistic way not this unrealistic follow the path key framed fashion.

I have tried to find to find the formulas need to due this for days. I\'m new to python but the program i\'m trying to right this plugin for just started using python and it is simple enough for me to work with. Please please help.

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help](./Asking(20)for(20)Help.html) page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
::::::::::
