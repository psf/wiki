# L.I.S.A

::: {#content dir="ltr" lang="en"}
# About {#About}

This project is like the J.A.R.V.I.S AI developed by Tony Stark in Iron Man.

I decided to create my own Digital Life Assistant because I didn\'t found any good project to contribute, or the concept wasn\'t good enough to fit my needs. I want something fast, easy to understand, easy to edit, easy to add features. Something small enough to run on a cheap computer like Raspberry Pi.

L.I.S.A will assist me like a Digital Like Assistant. It will give me usefull informations even if I didn\'t ask these, and answer me when I will ask something I want to know or to do. I actually have my house managed by a Vera-Lite controller (Zwave). L.I.S.A will be able to manage it (and other box with a simple module) and allow me to control with my house by voice.

# Architecture {#Architecture}

The architecture of L.I.S.A will be like this :

![](https://raw.github.com/Seraf/LISA/master/docs/images/lisa-schema.png "https://raw.github.com/Seraf/LISA/master/docs/images/lisa-schema.png"){.external_image}

The goal is to have the possibility to separate each element and let them communicate by network. With this system you will be able to have one IA, multiple speech engine, and multiple clients.

Using twisted, the client should be able to transmit the data of the microphone but also the zone where the sound come from. So the program will be able to answer in the zone where the sound was recorded.

# Documentation {#Documentation}

You will find all documentation needed on [https://readthedocs.org/projects/lisa/](https://readthedocs.org/projects/lisa/){.https}

# State of the project {#State_of_the_project}

![](https://travis-ci.org/Seraf/LISA.png "https://travis-ci.org/Seraf/LISA.png"){.external_image}
:::
