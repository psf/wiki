# OptionParsing

::::: {#content dir="ltr" lang="en"}
::: table-of-contents
Contents

1.  [Builtin Tools](#Builtin_Tools)
2.  [External tools](#External_tools)
3.  [The goal of option parsing](#The_goal_of_option_parsing)
4.  [See Also](#See_Also)
:::

## 1. Builtin Tools {#Builtin_Tools}

Overview of Python modules for option parsing

- [getopt](http://docs.python.org/2/library/getopt.html){.http} - procedural interface in stdlib for refugees from the C camp

- [optparse](OptParse) - stdlib name for Optik, a revolutionary API for option parsing in Python 2.x

- [argparse](http://docs.python.org/3/library/argparse.html){.http} - `optparse`{.backtick} pumped up for Python 3.x (and included in Python 2.7)

## 2. External tools {#External_tools}

::: {}
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| **Name**                                                                       | **[365 Day Ranking](https://hugovk.github.io/top-pypi-packages/){.https}** | **Latest Release**  | **Description**                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| [Abseil Python Common Libraries](https://github.com/abseil/abseil-py){.https}\ | 103                                                                        | 0.11.0 (2020-10-27) | gflags merged into this                                                                       |
| (pypi: [absl-py](https://pypi.org/project/absl-py/){.https})                   |                                                                            |                     |                                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| [Click](https://palletsprojects.com/p/click/){.https}\                         | 34                                                                         | 7.1.2 (2020-04-27)  | create beautiful command line interfaces in a composable way with as little code as necessary |
| (pypi: [click](https://pypi.org/project/click/){.https})                       |                                                                            |                     |                                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| [Typer](https://typer.tiangolo.com/){.https}\                                  | 2321                                                                       | 0.3.2 (2020-08-16)  | build great CLIs. Easy to code. Based on Python type hints.                                   |
| (pypi: [typer](https://pypi.org/project/typer/){.https})                       |                                                                            |                     |                                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
:::

More:

- [cmdopts](http://code.google.com/p/py-command-line-options){.http} - \...

- [docopt](http://docopt.org/){.http} - no API calls needed, it\'s awesome!

## 3. The goal of option parsing {#The_goal_of_option_parsing}

The option parsing goal can be split in two parts:

1.  identifying the command user needs to execute
2.  changing configuration for the program

For the first part, it will be good if option parsing library could handle \'subcommands\'. It is known that \'argparse\' can do this and \'optparse\' cannot. \'docopt\' probably handles this transparently.

For the second thing there should be some strategy to choose how (and which) options are merged into configuration to make the process of program configuration easy for the user and occasional patch contributors.

## 4. See Also {#See_Also}

- [ConfigParser](ConfigParser)

- [CommandlineTools](CommandlineTools)
:::::
