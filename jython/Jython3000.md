# Jython3000

::::::: {#content dir="ltr" lang="en"}
# Ideas for backwards incompatible changes in 3.x

It would be good if most of these can have warnings in 2.6

::: {#java .section}
### Java

- In our core code kill methods that do not take a ThreadState when there is a method that does (mainly in PyObject)
- Kill all of Py.java (It\'s a giant global that we should be able to split up \-- maybe it will just become tiny)
:::

::: {#registry .section}
### Registry

- Kill respectJavaAccessibility
:::

::: {#package-cache .section}
### Package Cache

- Disable by default, add an easy flag to enable.
:::

::: {#proxy-generation .section}
### Proxy generation

- Remove event properties \-- they are arbitrary, hazardous and easy to go wrong with
:::
:::::::
