# Powerful Python One-Liners

::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content dir="ltr" lang="en"}
# Powerful Python One-Liners {#Powerful_Python_One-Liners}

This page is devoted to short programs that can perform powerful operations called *Python One-Liners*.

You may ask: why should I care? The answer is profound: if you cannot read and write one-liner code snippets, how can you ever hope to read and write more complicated codebases? Python one-liners can be just as powerful as a long and tedious program written in another language designed to do the same thing. In other languages (think: Java) this would be nearly *impossible*, but in Python, it\'s a lot easier to do. The trick is to think of something that will \"do a lot with a little.\" Most importantly, reading and writing about Python one-liners (e.g., in this post) is a lot of fun! There\'s even a whole subculture around who can write the shortest code for a given problem.

It would be awesome if this page expanded to the point where it needs some sort of organization system. *(**Edit**: The one-liners are now sorted more or less by ease-of-understanding \-- from simple to hard. Please use a \"sorted insert\" for your new one-liner.)*

The source code is contributed from different Python coders \-\-- Thanks to all of them! Special thanks to the early contributor [JAM.](JAM)

Of course, there is debate on whether one-liners are even *Pythonic*. As a rule of thumb: if you use one-liners that are confusing, difficult to understand, or to show off your skills, they tend to be *Unpythonic*. However, if you use well-established one-liner tricks such as [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions){.https} or the [ternary operator](https://blog.finxter.com/python-one-line-ternary/){.https}, they tend to be Pythonic.

So, use your one-liner superpower wisely!

## Free Python One-Liners Learning Resources {#Free_Python_One-Liners_Learning_Resources}

- [Free \'\'Python One-Liners\'\' videos & book resources](https://pythononeliners.com/){.https}

- [Collection of \'\'One-Liners\'\' with interactive shell](https://blog.finxter.com/10-python-one-liners/){.https}

- [Book \'\'Python One-Liners\'\'](https://www.amazon.com/gp/product/B07ZY7XMX8){.https}

- [Interesting Quora Thread \'\'Python One-Liner\'\'](https://www.quora.com/What-are-some-of-the-most-elegant-greatest-Python-one-liners){.https}

- [Python One-Line X](https://blog.finxter.com/python-one-line-x/){.https} - How to accomplish different tasks in a single line

- [Subreddit \'\'\'Python One-Liners\'\'\'](https://www.reddit.com/r/PythonOneLiners/){.https}

- [Github \'\'\'Python One-Liners\'\'\'](https://github.com/finxter/PythonOneLiners/){.https} - Share your own one-liners with the community

## Overview: 10 one-liners that fit into a tweet {#Overview:_10_one-liners_that_fit_into_a_tweet}

I visited this page oftentimes and I loved studying the one-liners presented above. Thanks for creating this awesome resource, JAM, and RJW! ![:)](/wiki/europython/img/smile.png ":)"){height="16" width="16"}

Because I learned a lot from studying the one-liners, I thought why not revive the page (after almost ten years since the last change happened)?

After putting a lot of effort into searching the web for inspiration, I created the following ten one-liners. Some of them are more algorithmic (e.g. Quicksort). Some day, I will add a detailed explanation here - but for now, you can [read this blog article](https://blog.finxter.com/10-python-one-liners/){.https} to find explanations.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-2297a3ff1bd5d90c9364f42690091e8ce1ef2172 dir="ltr" lang="en"}
   1 # Palindrome Python One-Liner
   2 phrase.find(phrase[::-1])
   3 
   4 # Swap Two Variables Python One-Liner
   5 a, b = b, a
   6 
   7 # Sum Over Every Other Value Python One-Liner
   8 sum(stock_prices[::2])
   9 
  10 # Read File Python One-Liner
  11 [line.strip() for line in open(filename)]
  12 
  13 # Factorial Python One-Liner
  14 reduce(lambda x, y: x * y, range(1, n+1))
  15 
  16 # Performance Profiling Python One-Liner
  17 python -m cProfile foo.py
  18 
  19 # Power set Python One-Liner
  20 lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
  21 
  22 # Fibonacci Python One-Liner
  23 lambda x: x if x<=1 else fib(x-1) + fib(x-2)
  24 
  25 # Quicksort Python One-liner
  26 lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
  27 
  28 # Sieve of Eratosthenes Python One-liner
  29 reduce( (lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))
```
:::
::::

## Find All Indices of an Element in a List {#Find_All_Indices_of_an_Element_in_a_List}

Say, you want to do the same as the list.index(element) method but return all indices of the element in the list rather than only a single one.

In this one-liner, you're looking for element \'Alice\' in the list lst = \[1, 2, 3, \'Alice\', \'Alice\'\] so it even works if the element is not in the list (unlike the list.index() method).

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-841db20adb66dd7111a78d30a754e763c43e3871 dir="ltr" lang="en"}
   1 # List
   2 lst = [1, 2, 3, 'Alice', 'Alice']
   3 
   4 # One-Liner
   5 indices = [i for i in range(len(lst)) if lst[i]=='Alice']
   6 
   7 # Result
   8 print(indices)
   9 # [3, 4]
```
:::
::::

## echo unicode character: {#echo_unicode_character:}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-082d4ba455792a1aa5e48eac43344717ccc2b8b2 dir="ltr" lang="en"}
python -c "print unichr(234)"
```
:::
::::

This script echos \"ê\"

### Reimplementing cut {#Reimplementing_cut}

Print every line from an input file but remove the first two fields.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-03e682878800c96c7bc29434f731285030dfc09f dir="ltr" lang="en"}
python -c "import sys;[sys.stdout.write(' '.join(line.split(' ')[2:])) for line in sys.stdin]" < input.txt
```
:::
::::

### Decode a base64 encoded file {#Decode_a_base64_encoded_file}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0c418b9496bd9e3a156b6c7e9f79b147b0d756ae dir="ltr" lang="en"}
import base64, sys; base64.decode(open(sys.argv[1], "rb"), open(sys.argv[2], "wb"))
```
:::
::::

### Editing a list of files in place {#Editing_a_list_of_files_in_place}

I came up with this one-liner in response to an [article](http://linuxgazette.net/issue96/orr.html){.http} that said it couldn\'t be done as a one-liner in Python.

What this does is replace the substring \"at\" by \"op\" on all lines of all files (in place) under the path specified (here, the current path).

- ***Caution:*** Don\'t run this on your home directory or you\'re going to get **all your text files edited**.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-306ef18e3fad2542c5768c0607c92c1c1ed169d6 dir="ltr" lang="en"}
import sys,os,re,fileinput;a=[i[2] for i in os.walk('.') if i[2]] [0];[sys.stdout.write(re.sub('at','op',j)) for j in fileinput.input(a,inplace=1)]
```
:::
::::

Clearer is: `import os.path; a=[f for f in os.listdir('.') if not os.path.isdir(f)]`

### Set of all subsets {#Set_of_all_subsets}

- Function that returns the set of all subsets of its argument

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-87c83438d7677d679ba56feddd2e5b60abd3de01 dir="ltr" lang="en"}
f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
```
:::
::::

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-5fdd5905eb601ac685cd4082bdffe012c89a0fda dir="ltr" lang="en"}
>>>f([10,9,1,10,9,1,1,1,10,9,7])
[[], [9], [10], [9, 10], [7], [9, 7], [10, 7], [9, 10, 7], [1], [9, 1], [10, 1], [9, 10, 1], [7, 1], [9, 7, 1], [10, 7, 1], [9, 10, 7, 1]]
```
:::
::::

-RJW

Alternative (shorter, more functional version):

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-806ae6fc69b8cfa081f0cf2e22896487b7e852a4 dir="ltr" lang="en"}
f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
```
:::
::::

### Terabyte to Bytes {#Terabyte_to_Bytes}

Want to know many bytes a terabyte is? If you know further abbreviations, you can extend the list.

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b41923b17fe98e2063e84ba79cb52ba617d75fee dir="ltr" lang="en"}
import pprint;pprint.pprint(zip(('Byte', 'KByte', 'MByte', 'GByte', 'TByte'), (1 << 10*i for i in range(5))))
```
:::
::::

### Largest 8-Bytes Number {#Largest_8-Bytes_Number}

And what\'s the largest number that can be represented by 8 Bytes?

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-ac1dc0d9d77a8c1ed7b5533927cf67135b7cb1ff dir="ltr" lang="en"}
print '\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in range(8)))
```
:::
::::

Cute, isn\'t it?

## Display List of all users on Unix-like systems {#Display_List_of_all_users_on_Unix-like_systems}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9f6abcc304fc0ca6f70cd390ad54918a4e165d56 dir="ltr" lang="en"}
print '\n'.join(line.split(":",1)[0] for line in open("/etc/passwd"))
```
:::
::::

## CSV file to json {#CSV_file_to_json}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-466fd6eccd1e23a5eebd1ee02a176d6b68b57a79 dir="ltr" lang="en"}
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
```
:::
::::

## Compress CSS file {#Compress_CSS_file}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0236cd42438e5fd9005d215bed3cdb529c09ddde dir="ltr" lang="en"}
python -c 'import re,sys;print re.sub("\s*([{};,:])\s*", "\\1", re.sub("/\*.*?\*/", "", re.sub("\s+", " ", sys.stdin.read())))'
```
:::
::::

## Decode string written in Hex {#Decode_string_written_in_Hex}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-f35456592bb0d2c281d1896181dc6e6b781c2a24 dir="ltr" lang="en"}
python -c "print ''.join(chr(int(''.join(i), 16)) for i in zip(*[iter('474e552773204e6f7420556e6978')]*2))"
```
:::
::::

## Retrieve content text from HTTP data {#Retrieve_content_text_from_HTTP_data}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-78146a05772d7e005be8861344c4819bfaeeb627 dir="ltr" lang="en"}
python -c "import sys; print sys.stdin.read().replace('\r','').split('\n\n',2)[1]";
```
:::
::::

## Broadcast magic packet to power on wakeonlan enabled computer {#Broadcast_magic_packet_to_power_on_wakeonlan_enabled_computer}

Small [Wikipedia Python script](https://en.wikipedia.org/wiki/Wake-on-LAN#Creating_and_sending_the_magic_packet){.https} squeezed out to 166 characters length one-liner:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-41ecefd03acccb5a7c8721e08fda0705bf6118dd dir="ltr" lang="en"}
python -c "import socket as S;s=S.socket(S.AF_INET,S.SOCK_DGRAM);s.setsockopt(S.SOL_SOCKET,S.SO_BROADCAST,1);s.sendto(b'\xff'*6+b'\x84\x47\x09\x0b\x7f\xfd'*16,('<broadcast>',7))"
```
:::
::::

Uglier, with Python constant names replaced by their values, squeezed out to 123 characters only:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-afd4be15a35827b057ff04f42622a1cb0d4ab199 dir="ltr" lang="en"}
python -c "import socket as S;s=S.socket(2,2);s.setsockopt(1,6,1);s.sendto(b'\xff'*6+b'\x84\x47\x09\x0b\x7f\xfd'*16,('<broadcast>',9))"
```
:::
::::

Replace mac address \\x84\\x47\\x09\\x0b\\x7f\\xfd with mac address of computer that should be powered on.

## Prints file extension {#Prints_file_extension}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-6082cb80f46dda6851027135910c8ca5e6b8ac5e dir="ltr" lang="en"}
print '~/python/one-liners.py'.split('.')[-1]
```
:::
::::

## Escapes content from stdin {#Escapes_content_from_stdin}

This can be used to convert a string into a \"url safe\" string

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-22316894bbcef02a66bfd66e6ce2788bd88087ba dir="ltr" lang="en"}
python -c "import urllib, sys ; print urllib.quote_plus(sys.stdin.read())";
```
:::
::::

## Reverse lines in stdin {#Reverse_lines_in_stdin}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-0715489050fb91728dc0e50a6c907d17f08787d3 dir="ltr" lang="en"}
python -c "import sys; print '\n'.join(reversed(sys.stdin.read().split('\n')))"
```
:::
::::

## Print top 10 lines of stdin {#Print_top_10_lines_of_stdin}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-9fe2df81a19a45c38c2e2bd3b5e885c638dd4b44 dir="ltr" lang="en"}
python -c "import sys; sys.stdout.write(''.join(sys.stdin.readlines()[:10]))" < /path/to/your/file
```
:::
::::

## Apply regular expression to lines from stdin {#Apply_regular_expression_to_lines_from_stdin}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-8834de240d5908f12dc6bf5288fa7303481f2721 dir="ltr" lang="en"}
[another command] | python -c "import sys,re;[sys.stdout.write(re.sub('PATTERN', 'SUBSTITUTION', line)) for line in sys.stdin]"
```
:::
::::

## Modify lines from stdin using map {#Modify_lines_from_stdin_using_map}

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-eccb99419b801404f9058a68043f1cccf9409d5b dir="ltr" lang="en"}
python -c "import sys; tmp = lambda x: sys.stdout.write(x.split()[0]+'\t'+str(int(x.split()[1])+1)+'\n'); map(tmp, sys.stdin);"
```
:::
::::

### Cramming Python into Makefiles {#Cramming_Python_into_Makefiles}

A related issue is embedding Python into a Makefile. I had a really long script that I was trying to cram into a makefile so I automated the process:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-646b500484a5c3cb85505e3e58fed93c5f2a3248 dir="ltr" lang="en"}
   1 import sys,re
   2 
   3 def main():
   4     fh = open(sys.argv[1],'r')
   5     lines = fh.readlines()
   6     print '\tpython2.2 -c "`printf \\"if 1:\\n\\'
   7     for line in lines:
   8         line = re.sub('[\\\'\"()]','\\\g<0>',line)
   9         # grab leading white space (should be multiples of 4) and makes them into
  10         # tabs
  11         wh_spc_len = len(re.match('\s*',line).group())
  12 
  13         sys.stdout.write('\t')
  14         sys.stdout.write(wh_spc_len/4*'\\t'+line.rstrip().lstrip())
  15         sys.stdout.write('\\n\\\n')
  16     print '\t\\"`"'
  17 
  18 if __name__=='__main__':
  19     main()
```
:::
::::

This script generates a \"one-liner\" from make\'s point of view.

## Sony\'s Open Source command-line tool for performing python one-liners using unix-like pipes {#Sony.27s_Open_Source_command-line_tool_for_performing_python_one-liners_using_unix-like_pipes}

They call it \"The Pyed Piper\" or pyp. It\'s pretty similar to the -c way of executing python, but it imports common modules and has its own preset variable that help with splitting/joining, line counter, etc. You use pipes to pass information forward instead of nested parentheses, and then use your normal python string and list methods. Here is an example from the homepage:

Here, we take a Linux long listing, capture every other of the 5th through the 10th lines, keep the username and filename fields, replace \"hello\" with \"goodbye\", capitalize the first letter of every word, and then add the text \"is splendid\" to the end:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-038fbf1e51919e1858750f2b03608058ab044b0a dir="ltr" lang="en"}
ls -l | pyp "pp[5:11:2] | whitespace[2], w[-1] | p.replace('hello','goodbye') | p.title(),'is splendid'"
```
:::
::::

and the explanation:

This uses pyp\'s built-in string and list variables (p and pp), as well as the variable whitespace and its shortcut w, which both represent a list based on splitting each line on whitespace (whitespace = w = p.split()). The other functions and selection techniques are all standard Python. Notice the pipes (\"\|\") are inside the pyp command.

[http://code.google.com/p/pyp/](http://code.google.com/p/pyp/){.http} [http://opensource.imageworks.com/?p=pyp](http://opensource.imageworks.com/?p=pyp){.http}

## Contributed Code {#Contributed_Code}

- [JAM/Code/PlatformFinder](./JAM(2f)Code(2f)PlatformFinder.html) - This program tells you what platform you are using.

- [JAM/Code/ComPYiler](./JAM(2f)Code(2f)ComPYiler.html) - This program compiles every .py file in the Python directory.

- [Powerful Python One-Liners/Hostname](./Powerful(20)Python(20)One(2d)Liners(2f)Hostname.html) - This program tells you what your hostname is.
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
