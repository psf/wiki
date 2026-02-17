# Security

::: {#content dir="ltr" lang="en"}
Notes about Python Security.

## tav\'s jail {#tav.27s_jail}

[http://tav.espians.com/a-challenge-to-break-python-security.html](http://tav.espians.com/a-challenge-to-break-python-security.html){.http}

- Remove evil attributes like frame.f_globals or object.[subclasses]{.u}

- Remove evil builtins like compile(), import() or reload()

## Zope security {#Zope_security}

[http://svn.zope.org/zope.security/trunk/src/zope/security/](http://svn.zope.org/zope.security/trunk/src/zope/security/){.http}

- Sandboxing
- Object proxies

## Taint mode {#Taint_mode}

Nicole King at one point wrote a taint mode for CPython 3.0, but the site ([http://www.cats-muvva.net/software/](http://www.cats-muvva.net/software/){.http}) is no longer functioning.

Problems:

- amaury: *The patch is indeed huge!*

- fijall: *it seems that every function that returns a [PyObject](./PyObject.html){.nonexistent} must be modified*

- fijall: *need to patch (\...) all places that might modify anything. (All side effects)*

=\> ncoghlan: *[PyPy](PyPy) is still a \*much\* better platform for that kind of experimentation than CPython*

See also the presentation: [Securing Python: Controlling the abilities of the interpreter](http://us.pycon.org/common/talkdata/PyCon2007/062/PyCon_2007.pdf){.http}, [PyCon](PyCon) US 2007, Brett Cannon and Eric Wohlstadter

Related issue: [Taint a la Perl?](http://bugs.python.org/issue500698){.http}.

## Python Security Response Team {#Python_Security_Response_Team}

Some members:

- Brett Cannon

Email: security AT python.org

## Controlling Access to Resources Within The Python Interpreter {#Controlling_Access_to_Resources_Within_The_Python_Interpreter}

- URL: [Python security paper online](http://sayspy.blogspot.com/2007/04/python-security-paper-online.html){.http}

- Paper: [Controlling Access to Resources Within The Python Interpreter](http://www.cs.ubc.ca/~drifty/papers/python_security.pdf){.http}, Brett Cannon and Eric Wohlstadter, University of British Columbia

## Sandboxing {#Sandboxing}

- [PyPy](PyPy) project: [PyPy\'s sandboxing features](http://codespeak.net/pypy/dist/pypy/doc/sandbox.html){.http}.

- [CapPython](http://mail.python.org/pipermail/python-dev/2008-September/082475.html){.http} is an object-capability subset of Python, inspired by Joe-E and Caja/Cajita, which are object-capability subsets of Java and Javascript respectively.

- [SandboxedPython](SandboxedPython)

- [How can I run an untrusted Python script safely (i.e. Sandbox)](./How(20)can(20)I(20)run(20)an(20)untrusted(20)Python(20)script(20)safely(2028)i(2e)e(2e20)Sandbox(29).html){.nonexistent}

- [CPython in the web browser under Native Client](http://mail.python.org/pipermail/python-dev/2009-June/090038.html){.http}

## Unsafe modules {#Unsafe_modules}

- os.kill(), os.chown(), os.unlink(), \...
- imageop: many bugs
  - [CVE-2007-4965: Integer overflow in imageop module](http://bugs.python.org/issue1179){.http} (2007-09 .. 2008-08)

  - [Buffer overflow in imageop module](http://bugs.python.org/issue4317){.http} (rgb2rgb8): fixed in Python 2.6.1 and Python 3.0

## Fuzzing {#Fuzzing}

Victor Stinner wrote a fuzzer called [Fusil](https://github.com/clem1/segvault/tree/master/fusil){.https} to test Python. It already helped to fix many bugs. fusil-python works on Python 2.4 .. 3.0.

Fusil was also used on [PyPy](PyPy) ([Finding Bugs in PyPy with a Fuzzer](http://morepypy.blogspot.com/2008/07/finding-bugs-in-pypy-with-fuz.html){.http}).
:::
