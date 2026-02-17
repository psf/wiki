# YAML

::: {#content dir="ltr" lang="en"}
YAML is a human-friendly format for structured data, that is both easy to write for humans and still parsable by computers.

### PyYAML parser {#PyYAML_parser}

[PyYAML](http://pyyaml.org/){.http} is the most-used and go-to YAML package, which tries to be as compliant as possible with the YAML specs. It is, at its core, C-based. It can both read and write YAML. You can read the [official documentation](https://pyyaml.org/wiki/PyYAMLDocumentation){.https}, or try the condensed/simplified version of these docs, with usable example code on this [Python YAML tutorial](https://python.land/data-processing/python-yaml){.https}.

When using this package, be careful which function you use. The `load()`{.backtick} function is very powerful and allows arbitrary code execution, while the `safe_load()`{.backtick} function is enough for most use cases. It only allows a subset of the load function, making it a much safer choice. For more details, see also the [load deprecation notice](https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation){.https}.

### YAML examples and usage in notable Python apps {#YAML_examples_and_usage_in_notable_Python_apps}

YAML is a feature-rich language. Some packages that heavily depend on YAML are:

- tmuxp - [http://tmuxp.readthedocs.org/en/latest/examples.html](http://tmuxp.readthedocs.org/en/latest/examples.html){.http}

- ansible - [http://www.ansibleworks.com/docs/YAMLSyntax.html](http://www.ansibleworks.com/docs/YAMLSyntax.html){.http} and [http://www.ansibleworks.com/docs/playbooks.html#id9](http://www.ansibleworks.com/docs/playbooks.html#id9){.http}

- appengine - [https://developers.google.com/appengine/docs/python/config/appconfig](https://developers.google.com/appengine/docs/python/config/appconfig){.https} and [https://github.com/rietveld-codereview/rietveld/blob/master/app.yaml](https://github.com/rietveld-codereview/rietveld/blob/master/app.yaml){.https}

- salt - [http://docs.saltstack.com/topics/tutorials/starting_states.html#default-data-yaml](http://docs.saltstack.com/topics/tutorials/starting_states.html#default-data-yaml){.http}
:::
