# SummerOfCode/SpeedDotPythonDotOrg

::: {#content dir="ltr" lang="en"}
# Speed.Python.Org {#Speed.Python.Org}

Speed.Python.Org is a Google Summer of Code 2011 Proposal by Jarek Sedlacek.

[PyPy](http://wiki.python.org/moin/PyPy){.http} currently has benchmarks and profiling available at speed.pypy.org. This should be ported to speed.python.

The first goal is to port all of the tests to Python 3.

When all of the tests are ported, a website needs to be created that will run all the tests on CPython, and display the results. This will most likely be done with [codespeed](http://wiki.github.com/tobami/codespeed/){.http}.

## Milestones {#Milestones}

Start of Program (May 24) The first task that will be addressed during the project is porting the tests to python 3. The only thing that needs to be done to prepare for this is to have a version control repository set up.

Midterm Evaluation (July 12) By the mid point of the project, the majority of the tests should be ported to python 3. Ideally they all will be, but some with extenuating circumstances (dependencies on large frameworks like django that are not yet ported to python3, for example) may be impossible to port over the summer.

Final Evaluation (Aug 16) At the end of the summer, a website speed.python.org should exist, showing the latest benchmarks for CPython.

## About Me {#About_Me}

I\'m a currently a student at Rutgers University, studying Physics and Computer Science. I work for Open Systems Solutions at Rutgers, where I work as a member of a team responsible for building and maintaining the RPM packages used through a user community of 70,000 faculty, staff, and students. I also created projects for use at the university, like [SpamAssassin](./SpamAssassin.html){.nonexistent} plugins for detecting spam in foreign languages, and a python program to use Cacti thresholds as Nagios plugins.

I\'ve also spent a summer working for the United States Army Armament Research Development And Engineering Center (ARDEC). I designed and implemented a multi-threaded graphical application in C++ for the Small Arms Deployable Sensor Network (SmADSNet), including:

- an interface in QT for users to visualize information from a mesh network of sensor nodes overlaid on satellite imagery
- a network stack enabling TCP, UDP and serial communication with a mesh network
- MySQL database backend with export ability for post-analysis and the ability to sync from multiple sources

## Contact Info {#Contact_Info}

Name: Jarek Sedlacek

Email: [JarekSedlacek](./JarekSedlacek.html){.nonexistent}\@gmail.com

Phone: 973-229-8333

XMPP: [jarek@rutgers.edu](mailto:jarek@rutgers.edu){.mailto}

Address:

- 29 Lakeshore Dr. Rockaway, NJ 07866 United State of America
:::
