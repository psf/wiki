# EuroPython2007/VisualStudio2005

::: {#content dir="ltr" lang="en"}
# Visual Studio 2005 Sprint {#Visual_Studio_2005_Sprint}

## This sprint has been canceled due to lack of interest {#This_sprint_has_been_canceled_due_to_lack_of_interest}

------------------------------------------------------------------------

### This is a sprint suggestion to work on making Visual Studio 2005 a fully supported build platform for python 2.5 and 2.6 {#This_is_a_sprint_suggestion_to_work_on_making_Visual_Studio_2005_a_fully_supported_build_platform_for_python_2.5_and_2.6}

- Where: Vilnius, Lithuania

- When: after [EuroPython](EuroPython), 12-14 july

- Organizer: Kristján Valur Jónsson \<[kristjan@ccpgames.com](mailto:kristjan@ccpgames.com){.mailto}\>

Visual Studio 2005 has been availible for more than two years but still it is not an officially supported compiler for python. The benefits of using it are:

- greater performance, particularly through profiler guided optimization
- cross compilation for amd64 platform.

Although the PCBuild8 subdirectory is availible in the release25-maint branch and the trunk, a few things need to be done to make it complete:

- Fixup dependency on externals for some modules (bz2 etc), particularly for amd64
- Polish automatic PGO builds
- Fix and polish install script generation, and CRT redistribution
- Work on setting up a buildbot

Please contact me at \<[kristjan@ccpgames.com](mailto:kristjan@ccpgames.com){.mailto}\> if you think this is a worthwhile project and want to participate.
:::
