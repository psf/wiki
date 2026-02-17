# Distutils/Extensions/DefendAgainstFruit

::: {#content dir="ltr" lang="en"}
# Vision {#Vision}

[Defend Against Fruit](http://teamfruit.github.io/defend_against_fruit/){.http} is focused on providing a pragmatic, continuous deployment style build system for Python. Current Python build systems do not properly account for the needs of effective continuous deployment. This package extends the Python tooling to add the missing pieces.

With an eye to agile development principles and [fast-feedback](https://github.com/teamfruit/defend_against_fruit/wiki#fast-feedback-is-critical){.https}, we want a build system which satisfies the following goals:

- Every SCM change-set committed should result in a potentially shippable release candidate.
- When a defect is introduced, we want to immediately detect and isolate the offending SCM change-set. This is true even if the defect was introduced into a library we depend upon.
- Library management should be so easy as to never impede code changes, even in multi-component architecture.

For in-depth documentation with lots of pretty diagrams, [take a look at the wiki](https://github.com/teamfruit/defend_against_fruit/wiki){.https}.

# Authors {#Authors}

The majority of Defend Against Fruit has been co-developed by [James Carpenter](http://www.linkedin.com/in/jamescarpenter1){.http} and [Matthew Tardiff](http://www.linkedin.com/in/matthewtardiff){.http}, but many others provided considerable assistance.

For more details, please see the [Authors and Contributors](https://github.com/teamfruit/defend_against_fruit/wiki/Authors-And-Contributors){.https} wiki page.
:::
