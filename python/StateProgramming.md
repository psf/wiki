# StateProgramming

::::::: {#content dir="ltr" lang="en"}
# State Programming {#State_Programming}

### Why, When {#Why.2C_When}

Very often, the response of a function will depend on the state of this object. With this pattern, It\'s easy to do such a thing ! You just have to write several sub-classes, each per state, inherit the State class and call the setState when the object need to change state.

### Code {#Code}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0cdcdbaa0687565c1122afdda3b01485ce1e1572 dir="ltr" lang="en"}
   1 # Code is Public Domain.
   2 class State:
   3     
   4     def setState(self,stateClass):
   5         #print stateClass.__dict__
   6         for (name,attr) in stateClass.__dict__.iteritems():
   7             if not name.startswith('_') and callable(attr):
   8                 f = getattr(stateClass,name)
   9                 l = f.__get__(self,self.__class__)
  10                 setattr(self,name,l)
```
:::
::::

### Example {#Example}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f45887b82ecb541834899d432dc129a4f220cb46 dir="ltr" lang="en"}
   1 # Code is Public Domain.
   2 class test(State):
   3     def __init__(self,a):
   4         self.a = a
   5     
   6     def showMe(self):
   7         print self.a
   8 
   9     def showYou(self,other):
  10         print self.a,other
  11 
  12     def changeToOne(self):
  13         self.setState(StateOne)
  14 
  15     def changeToTwo(self):
  16         self.setState(StateTwo)
  17 
  18 class StateOne(test):
  19 
  20     def showMe(self):
  21         print self.a,'State One'
  22 
  23     def showYou(self,other):
  24         print self.a,'State One',other
  25 
  26 class StateTwo(test):
  27 
  28     def showMe(self):
  29         print self.a,'State Two'
  30 
  31     def showYou(self,other):
  32         print self.a,'State Two',other
  33         
  34 
  35 t1 = test('t1')
  36 t2 = test('t2')
  37 t1.showMe()
  38 t2.showMe()
  39 t1.showYou("you")
  40 t1.changeToOne()
  41 t1.showMe()
  42 t2.changeToTwo()
  43 t2.showMe()
  44 t1.showYou("you")
  45 t1.changeToTwo()
  46 t2.changeToOne()
  47 t1.showMe()
  48 t2.showMe()
  49 t1.showYou("you")
  50 t2.showYou('you')
```
:::
::::

Output is

    t1
    t2
    t1 you
    t1 State One
    t2 State Two
    t1 State One you
    t1 State Two
    t2 State One
    t1 State Two you
    t2 State One you
:::::::
