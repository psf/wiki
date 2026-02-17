# CubicTemp

::: {#content dir="ltr" lang="en"}
A small, elegant templating engine.

### Masthead {#Masthead}

URL

:   [https://pypi.python.org/pypi/cubictemp](https://pypi.python.org/pypi/cubictemp){.https}

version
:   2.0

licence
:   BSD

platforms
:   All

Python versions
:   2.4+

### Deployment Platforms {#Deployment_Platforms}

- Any

### Sample {#Sample}

            <select>
            <!--(for option in optionList)-->
                    <option @!if (option[1]) then "selected" else ""!@>
                    @!option[0]!@
                    </option>
            <!--(end)-->
            </select>

### Suitability {#Suitability}

CubicTemp should be used in association with a good web framework. It is small and simple enough to be modified on a per-project basis.

A back ported version of CubicTemp is available from my page [AshishShrestha](AshishShrestha). This works with Jython 2.1 This allows it to be used with servlet engines like Tomcat. I think the simplicity of CubicTemp and ease of Jython is a cool combination for web development.

### Development Interfaces {#Development_Interfaces}

### Environment Access {#Environment_Access}

### Session, Identification and Authentication {#Session.2C_Identification_and_Authentication}

### Persistence Support {#Persistence_Support}

### Presentation Support {#Presentation_Support}

### InTheirOwnWords {#InTheirOwnWords}

CubicTemp is an attempt to make a Python templating system that is simple, powerful and well designed. Cubictemp also has built-in protection against cross-site-scripting attac, a very common class of web application vulnerability.

### Comments {#Comments}

### Hosting {#Hosting}
:::
