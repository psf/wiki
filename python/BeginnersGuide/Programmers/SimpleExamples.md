# BeginnersGuide/Programmers/SimpleExamples

::::::::::::::::::::::::::::: {#content dir="ltr" lang="en"}
Here are some samples to help get a better idea of Python\'s syntax:

Hello World (the traditional first program)

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-27986105805cf23422d40fc399ad845f1c78b68d dir="ltr" lang="en"}
print('Hello world!')
```
:::
::::

String formatting

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-c2c3d67df2969eb662f12610eba28195924ccb90 dir="ltr" lang="en"}
name = 'Monty'
print('Hello, %s' % name)  # string interpolation
print('Hello, {}'.format(name))  # string formatting
```
:::
::::

Defining a function

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ce02b3e1fd086b3ce77e7042bd3e676eb8097257 dir="ltr" lang="en"}
def add_one(x):
    return x + 1
```
:::
::::

Testing variable equality

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-1780328f1646bd651365c88e08210b5319b9a39e dir="ltr" lang="en"}
x = 1
y = 2
print 'x is equal to y: %s' % (x == y)
z = 1
print 'x is equal to z: %s' % (x == z)
names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']
if names == words:
    print 'Names list is equal to words'
else:
    print "Names list isn't equal to words"
new_names = ['Donald', 'Jake', 'Phil']
print 'New names list is equal to names: %s' % (new_names == names)
```
:::
::::

Defining a class with two methods

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-e2a4128b267e8afe516d6d17eb69a20eeb752163 dir="ltr" lang="en"}
class Talker(object):
    def greet(self, name):
        print 'Hello, %s!' % name
    def farewell(self, name):
        print 'Farewell, %s!' % name
```
:::
::::

Defining a list

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-bad02cf240b15935bec05979051ac1ca4b3fd79f dir="ltr" lang="en"}
dynamic_languages = ['Python', 'Ruby', 'Groovy']
dynamic_languages.append('Lisp')
```
:::
::::

Defining a dictionary

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-22680c5442bf7744e3a13f40016b7b1b23c1149c dir="ltr" lang="en"}
numbered_words = dict()
numbered_words[2] = 'world'
numbered_words[1] = 'Hello'
numbered_words[3] = '!'
```
:::
::::

Defining a while loop

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-99a6e5e3f577ebbf736e50fd7bbcee17d19747d1 dir="ltr" lang="en"}
while True:
    if value == wanted_value:
        break
    else:
        pass
```
:::
::::

Defining multiline strings

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-4103ced4509853480fa305b3b8fd5417f7324785 dir="ltr" lang="en"}
string = '''This is a string with embedded newlines.
Also known as a tripled-quoted string.
    Whitespace at the beginning of lines is included,
so the above line is indented but the others are not.
'''
```
:::
::::

Splitting a long string over several lines of source code

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-2e0101f3f008d89dff8bb28eb86fddb19a65feb9 dir="ltr" lang="en"}
string = ('This is a single long, long string'
          ' written over many lines for convenience'
          ' using implicit concatenation to join each'
          ' piece into a single string without extra'
          ' newlines (unless you add them yourself).')
```
:::
::::

Defining a for loop

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-5a85f7face350a0741bb4823c4407f03a08f0dc9 dir="ltr" lang="en"}
for x in xrange(1, 4):
    print ('Hello, new Python user!'
           'This is time number %d') % x
```
:::
::::

List comprehension

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-520202d8b5c28480cacbaa329f28ff30cb7f0c41 dir="ltr" lang="en"}
l = [x**2 for x in range(4)]
print(l)
# [0, 1, 4, 9]
```
:::
::::

Set comprehension with condition

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-424877dea8b945d32255530f635130e4d78181e0 dir="ltr" lang="en"}
squares = {x**2 for x in [0,2,4] if x < 4}
print(squares)
# {0, 4}
```
:::
::::

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
:::::::::::::::::::::::::::::
