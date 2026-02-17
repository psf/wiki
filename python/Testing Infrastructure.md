# Testing Infrastructure

::: {#content dir="ltr" lang="en"}
# What is it ? {#What_is_it_.3F}

The Python Package Index (namely PyPI) allows anyone to upload projects. This testing infrastructure wants to provide a way to analyse the distributions available at pypi using metrics such as test coverage, test results, PEP8 etc. as well as feedback on the installation (does it went well? are some weird files modified? etc.)

This wiki page defines the features that will be part of this testing infrastructure, as well as the metrics that will be used.

## Features {#Features}

- A clean Master/Slave architecture
- A RAW API for the slaves to communicate results to the master
- KISS
- A simple plugin architecture, so it is easy to plug new \"analysers\" on the execution part (to have new metrics)

## Metrics {#Metrics}

Here is a list of possible metrics that would be useful to have

- Are the tests passing?
- What is the test coverage? (does the project even have tests?)
- Is the project compliant to PEP 345 (packaging)?
- Does the project makes uncommon changes on the filesystem at installation time?
- Does the project tries to reach the network at installation time? (for something else than packaging)
- Is the project PEP8 compliant?
- Is the project active? (Number of versions in the last year)
:::
