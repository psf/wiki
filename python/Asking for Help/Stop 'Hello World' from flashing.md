# Asking for Help/Stop 'Hello World' from flashing

::::: {#content dir="ltr" lang="en"}
# Asking for Help: How do I stop the console/terminal/command line prompt from closing on Windows? {#Asking_for_Help:_How_do_I_stop_the_console.2Fterminal.2Fcommand_line_prompt_from_closing_on_Windows.3F}

Ok so, Let\'s say I want to run a program with a simple Print(\"hello world\"). How do I stop the console/terminal/command line prompt from closing immediately after it prints? I read somewhere that I\'m supposed to find some editpythonprefs, but I don\'t know where it is\... I am on Windows 7, if that helps

------------------------------------------------------------------------

Are you running the program from the file manager or do you already have the console open when running the program (by typing `python hello.py`{.backtick}, for example)? If the former is involved, which I suspect is the case, you could prevent the program from finishing by inserting something like the following at the end:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-adfb2d60d675f427d56bbd5133a6c65a6a90bda6 dir="ltr" lang="en"}
raw_input("Press Enter to exit.")
```
:::
::::

I found a [question](http://stackoverflow.com/questions/2322868/how-do-i-prevent-my-python-2-6-application-from-automatically-closing-once-reachi){.http} about this by searching the Internet for \"prevent Python program from exiting on Windows\". You\'ll find other more complicated suggestions if you follow various links from that question, but sometimes the simplest solutions are the best (or are at least good enough).

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
:::::
