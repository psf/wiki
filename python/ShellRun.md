# ShellRun

::: {#content dir="ltr" lang="en"}
Page status - development of a library (public domain) to run commands through shell is moved to [https://bitbucket.org/techtonik/shellrun](https://bitbucket.org/techtonik/shellrun){.https} along with detailed notes, because it is easier to sync notes with code in repository.

Libraries to run command through system shell, because subprocess suxx:

- [https://github.com/kennethreitz/envoy](https://github.com/kennethreitz/envoy){.https}

- [http://shell-command.readthedocs.org/en/latest/](http://shell-command.readthedocs.org/en/latest/){.http}

subprocess deadlock example:

- TODO

##### API Comparison {#API_Comparison}

Running:

    r = envoy.run('command')

    r = shell_command.shell_call('command')

Return code, [https://en.wikipedia.org/wiki/Exit_status](https://en.wikipedia.org/wiki/Exit_status){.https}

    # subprocess
    p.returncode

    # envoy
    r.status_code

    # shell_command
    r
:::
