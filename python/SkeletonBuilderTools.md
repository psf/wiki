# SkeletonBuilderTools

::: {#content dir="ltr" lang="en"}
## Skeleton Builder Tools {#Skeleton_Builder_Tools}

A skeleton builder tools are tools that takes a directory skeleton, copies over its directory structure to a target folder and uses a template engine to dynamically generate the files.

In alphabetical order:

- [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/){.http}

  - uses Jinja2 template engine.

  - config file can be in either json and yaml formats.

  - Tested for use with Python 3.3, 2.7, 2.6, Linux, Mac OS X, and Windows.

  - Extremely popular, with over 30 community contributed templates available for Python, Django, Flask, [JavaScript](./JavaScript.html){.nonexistent}, Ruby, C, Open Stack, and HTML.

  <!-- -->

  - List of [Full feature set](https://github.com/audreyr/cookiecutter#features){.https}

  - 3rd-party: [cookiedough](https://pypi.org/project/cookiedough/){.https} GUI browser/installer with \~4150 cookiecutter templates.

- [django-admin.py startproject](https://docs.djangoproject.com/en/1.5/intro/tutorial01/){.https}

  - (limited to [Django](https://docs.djangoproject.com/){.https} framework)

- [Echafaudage](http://harobed.github.io/echafaudage/){.http}

  - use [tempita](http://pythonpaste.org/tempita/){.http} template engine

  - config file is in json format

  - specific feature : standalone file executable directly with python -c \"\$(curl \...)\"

- [mr.bob](http://mrbob.readthedocs.org/en/latest/){.http}

  - use Jinja2 template engine

  - config file is in ini format

  - specific feature : pre, post [hooks](http://mrbob.readthedocs.org/en/latest/templateauthor.html#hooks){.http}

- [pcreate](http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html?highlight=pcreate){.http} (limited to [Pyramid](http://pyramid.readthedocs.org/en/latest/){.http} framework)

- [Paste Script](http://pythonpaste.org/script/){.http}

### Limited to package creation {#Limited_to_package_creation}

- [python-packager](https://github.com/fcurella/python-packager){.https}

- [modern-package-template](https://pypi.python.org/pypi/modern-package-template/){.https} (deprecated)
:::
