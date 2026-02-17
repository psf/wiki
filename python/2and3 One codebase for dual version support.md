# 2and3 One codebase for dual version support

::: {#content dir="ltr" lang="en"}
Tips for those wishing to create and maintain one Python codebase that works for both Python 2.X and Python 3.Y interpreters (for some value of X and Y).

## Why? {#Why.3F}

Seeing [one (very good) rant](http://ondrejcertik.blogspot.ch/2013/08/how-to-support-both-python-2-and-3.html){.http} about how hard it is to use the officially blessed way of using 2to3 reminded me that I also ask users on [Rosetta Code](http://rosettacode.org/wiki/Category:Python){.http} to allow code written in a style to work on both versions of Python interchangeably.

I thought we needed some central repository giving tips on how to do this and thought I would start with the rules stated on RC.

## Simple rules for making code work on both 2.X and 3.Y {#Simple_rules_for_making_code_work_on_both_2.X_and_3.Y}

1.  Use brackets in print statements/functions of one expression.
2.  Use zip and not izip; keys(), values(), items() and not their iter- forms.
3.  Check for raw_input and set raw_input to input if not found.
4.  Conditionally import reduce if it is not found.
:::
