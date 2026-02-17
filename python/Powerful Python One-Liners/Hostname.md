# Powerful Python One-Liners/Hostname

::: {#content dir="ltr" lang="en"}
# Description {#Description}

This is a simple [Powerful Python One-Liners](./Powerful(20)Python(20)One(2d)Liners.html). It prints the systems\'s hostname to the screen.

# Code {#Code}

`from socket import gethostname; print gethostname()`

# Download {#Download}

This program has been uploaded to the Wiki. You can download it as an attachment from this page.

Well, sometimes. A lighter-weight variant with desirable properties is

`import os; print os.uname()[1]`

[lwickjr](lwickjr): \--which doesn\`t seem to work on Windows. ![:(](/wiki/europython/img/sad.png ":("){height="16" width="16"}

[snark](./snark.html){.nonexistent}: \-- use `import platform; print platform.uname()[1]`

[synthesis](./synthesis.html){.nonexistent}: \-- use `import platform; print platform.node()`
:::
