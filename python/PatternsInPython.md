# PatternsInPython

::: {#content dir="ltr" lang="en"}
Patterns along the lines of [GangOfFour](http://c2.com/cgi/wiki?GangOfFour "Wiki"){.interwiki}

- [Visitor Pattern](http://peak.telecommunity.com/DevCenter/VisitorRevisited){.http}

- [DependencyInjectionPattern](DependencyInjectionPattern)

- [DecoratorPattern](DecoratorPattern)

- [ObserverPattern](ObserverPattern)

- [FunctionWrappers](FunctionWrappers)

- [MementoPattern](MementoPattern)

------------------------------------------------------------------------

I\'ve removed \"Inversion of Control in Python\" from the side of [DependencyInjectionPattern](DependencyInjectionPattern). \"Inversion of Control\" is a larger concept than Dependency injection. Dependency injection is a particular mechanism that is frequently used in systems that exhibits IoC type thinking. Even combined with the idea of service location (as opposed to dependency injection,) we still are a smaller idea than \"Inversion of Control.\" [Martin Fowler himself has said this many times.](http://martinfowler.com/articles/injection.html#InversionOfControl){.http}

Even \"Inversion of Control\" may even be poorly named; I would want to call it \"Network of Control.\" But that is neither here nor there, for the purposes of this page.

\-- [LionKimbro](LionKimbro) 2005-05-05 18:00:02
:::
