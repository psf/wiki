# DependencyInjectionPattern

::: {#content dir="ltr" lang="en"}
# Dependency Injection Pattern {#Dependency_Injection_Pattern}

The Dependency Injection Pattern, is described in [Martin Fowler\'s article](http://www.martinfowler.com/articles/injection.html){.http}. It is closely related to the [DependencyInversionPrinciple](./DependencyInversionPrinciple.html){.nonexistent} and the so called Inversion of Control (IoC) containers.

IoC is aimed at loosening the coupling of application components. The key concepts are:

- Components do not know each other directly.
- Components specify external dependencies using some kind of a key.
- Some \"superior instance\" (the IoC container, for example) resolves the dependencies once for each component and hereby \"wires\" the components together.

It is quite a challenge to implement an IoC container for statically typed languages. In python, however, the core concepts can be implemented quite easily. [DependencyInjectionThePythonWay](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/413268){.http} describes how.

## See Also {#See_Also}

[PEAK:InversionOfControl](http://peak.telecommunity.com/DevCenter/InversionOfControl){.http} \-- Inversion of Control is a more general concept (small components relinquishing control, or networking control, rather than maintaining it internally,) but the name was overloaded historically to mean what is named by DependencyInjectionPattern. [PEAK](./PEAK.html){.nonexistent} makes use of dependency injection, and the larger meaning of \"Inversion of Control.\" The target page describes dependency injection.

## Discussion {#Discussion}
:::
