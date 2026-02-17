# FiniteStateMachine

:::: {#content dir="ltr" lang="en"}
::: table-of-contents
Contents

1.  [Introduction](#Introduction)
2.  [Finite State Machine Editor](#Finite_State_Machine_Editor)
3.  [Tulip (Temporal Logic Planning Toolbox)](#Tulip_.28Temporal_Logic_Planning_Toolbox.29)
4.  [FSA - Finite State Automation in Python](#FSA_-_Finite_State_Automation_in_Python)
5.  [Noah Spurrier\'s FSM](#Noah_Spurrier.27s_FSM)
6.  [fsmpy](#fsmpy)
7.  [Decorator-based FSM](#Decorator-based_FSM)
8.  [Skip Montanaro\'s FSM](#Skip_Montanaro.27s_FSM)
9.  [python-fsm FSM module with PyGraphViz support](#python-fsm_FSM_module_with_PyGraphViz_support)
10. [fysom](#fysom)
:::

## Introduction {#Introduction}

This is a summary of FSM implementations in Python right now. Licensing remains unclear.

For general information about finite state machines, see:

- [Wikipedia:Finite_state_machine](http://www.wikipedia.com/wiki/Finite_state_machine "WikiPedia"){.interwiki} \-- ![B)](/wiki/europython/img/smile2.png "B)"){height="16" width="16"} *excellent!* ![B)](/wiki/europython/img/smile2.png "B)"){height="16" width="16"}

- [Wiki:FiniteStateMachine](http://c2.com/cgi/wiki?FiniteStateMachine "Wiki"){.interwiki}

## Finite State Machine Editor {#Finite_State_Machine_Editor}

[FSME](http://fsme.sourceforge.net/){.http} is a tool where you can draw FSM diagrams, and then compile to a Python module (or C++ code.) It also makes an XML description of the FSM.

Requires QT for the editor. (Not the compiler, though, which probably reads XML.)

- [tutorial](http://fsme.sourceforge.net/doc/tutorial.html){.http}

- [project wiki](http://fsme.sourceforge.net/phpwiki/){.http}

## Tulip (Temporal Logic Planning Toolbox) {#Tulip_.28Temporal_Logic_Planning_Toolbox.29}

[tulip](http://tulip-control.sourceforge.net/){.http} includes a subpackage called [transys](https://github.com/tulip-control/tulip-control/tree/master/tulip/transys){.https} that provides classes for (finite state)

1.  Transition systems ([Kripke Structures](https://en.wikipedia.org/wiki/Kripke_structure_%28model_checking%29){.https}, also known as generators of languages):

    - for closed systems
    - for open systems (that play against adversarial environments)

    The above support edge labeling, as well as state labeling (in that respect they are not pure Kripke structures and can be used to construct Labeled-transition systems, depending on the semantics assigned to the graph).

2.  [Automata](https://en.wikipedia.org/wiki/Automata_theory){.https} (also known as acceptors):

    1.  Finite-word:
        - [Deterministic Finite Automata](https://en.wikipedia.org/wiki/Deterministic_finite_automaton){.https} (DFA)

        - [Non-Deterministic Finite Automata](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton){.https} (NFA)

    2.  [Infinite-word](https://en.wikipedia.org/wiki/%CE%A9-automaton){.https} (= ω-automata):

        - [Buchi Automata](https://en.wikipedia.org/wiki/B%C3%BCchi_automaton){.https} (BA)

        - Rabin Automata (RA)

        - Parity Automata

3.  [Machines](https://en.wikipedia.org/wiki/Finite_state_transducer){.https} (also known as transducers):

    - [Mealy machines](https://en.wikipedia.org/wiki/Mealy_machine){.https}

    - [Moore machines](https://en.wikipedia.org/wiki/Moore_machine){.https}

The toolbox includes an extension of [networkx.MultiDiGraph](http://networkx.github.io/documentation/networkx-1.9/reference/classes.multidigraph.html?highlight=multidigraph#networkx.MultiDiGraph){.http} to define typed labeling and also a subpackage for exporting the above classes to:

- [GraphViz dot](https://en.wikipedia.org/wiki/DOT_%28graph_description_language%29){.https} (inluding: TikZ (LaTeX), ipython qtconsole inline plot support of graphviz output)

- [Promela](https://en.wikipedia.org/wiki/Promela){.https} (for transition systems only)

- [d3](https://en.wikipedia.org/wiki/D3.js){.https}

The implemented algorithms include the synchronous product between transition systems and Buchi automata.

Tulip itself is a package for synthesizing correct-by-construction systems from a logic specification and a model expressed as a transition system, including - among other - functions for abstracting the continuous dynamics of systems governed by differential equations to finite state transition systems.

## FSA - Finite State Automation in Python {#FSA_-_Finite_State_Automation_in_Python}

[FSA](http://osteele.com/software/python/fsa/){.http} seems to be all about creating finite state machines, but I don\'t see a whole lot on how to use them.

## Noah Spurrier\'s FSM {#Noah_Spurrier.27s_FSM}

[http://www.noah.org/python/FSM/](http://www.noah.org/python/FSM/){.http}

Noah\'s implementation is pure Python code. You init an FSM, register transitions, and then throw inputs at it. States and inputs must be hashable.

It\'s fairly similar to Skip\'s implementation (below).

## fsmpy

[fsmpy module](http://www.research.att.com/projects/mohri/fsm/doc4/fsmpy.html){.http}

This seems to be a Python wrapper around [AT&T\'s FSM library.](http://www.research.att.com/projects/mohri/fsm/){.http} It\'s all oriented around \"weighted\" finite state machines, so I\'m not so sure how suitable it is if you just want to use unweighted FSM.

## Decorator-based FSM {#Decorator-based_FSM}

An [example using decorators](http://wiki.python.org/moin/State%20Machine%20via%20Decorators){.http} is in the Decorator Library on this site. The module simplifies implementation of FSM\'s based on UML 2.0 state diagrams. The FSM is implemented as a class, with methods of the class associated with transitions or with states. The design is not the best for constructing FSMs to parse text being somewhat slower than alternatives.

## Skip Montanaro\'s FSM {#Skip_Montanaro.27s_FSM}

[fsm.py.](http://www.smontanaro.net/python/fsm.py){.http}

Features transition actions.

## python-fsm FSM module with PyGraphViz support {#python-fsm_FSM_module_with_PyGraphViz_support}

An concise yet comprehensive implementation based on Wikipedia spec of Finite State Machines. The module can be used to build and further describe finite state automata with DOT graphs. It implements acceptors and transducers (Moore and Mealy machines) and provides an straight-forward way to inject and execute state change actions for entry, exit, input and transition.

Licensed under the new BSD license.

[http://code.google.com/p/python-fsm/](http://code.google.com/p/python-fsm/){.http}

## fysom

A port of Jake Gordon\'s [javascript-state-machine](https://github.com/jakesgordon/javascript-state-machine){.https}. The module lets the user define callbacks for before/after events as well as callbacks on entering/leaving states. Events are exposed as object methods which when called, causes the appropriate state transition. The module also provides asynchronous callback functionality which allows delaying a state transition.

[https://github.com/oxplot/fysom](https://github.com/oxplot/fysom){.https}
::::
