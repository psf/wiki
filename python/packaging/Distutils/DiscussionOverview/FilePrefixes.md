# Distutils / Discussion Overview / File Prefixes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Rationale 

It is not possible to retrieve the installation paths of data, or other, files for all installation schemes supported by distutils right now. I propose the inclusion of a PREFIX file within the .egg-info directory that holds information on all prefixes set at installation time and a suitable API within pkgutil.

## Proposal 

### PREFIX 

The RECORD file is a CSV file, composed of records, one line per prefix. The csv module is used to read the file, with these options:

- field delimiter : `,`

- quoting char : `"`

- line terminator : `os.linesep` (so `\r\n` or `\n`)

Each record is composed of two elements:

- **prefix identifier**

  - Prefix identifiers differentiate between the various prefixes used within the installation process.

    Valid identifiers must adhere to the regular expression `^[a-z_]+`, i.e any combination of lowercase ASCII characters and the underscore.

- **path**

  - The path for the prefix identifier for this distribution.

    A `/` seperated path will be used regardless of the target system. The path definition can be either absolute or prefixed with one of the identifiers defined below. An absolute path is only used if the installation location is not relative to sys.prefix (\$base) or sys.exec_prefix (\$platbase).

#### Identifiers 

The list of standard identifiers comprises:

- `$base` - Base prefix

- `$platbase` - Platform specific base prefix

- `$purelib` - Pure Python distribution

- `$platlib` - Non-pure Python distribution (i.e one with extensions)

- `$scripts` - Executable Python scripts

- `$data` - Data files

#### Example 

Standard scheme installation on posix:

    base,/usr
    platbase,/usr
    purelib,$base/lib/pythonX.Y/site-packages
    platlib,$platbase/lib/pythonX.Y/site-packages
    scripts,$base/bin
    data,$base/share

User scheme installation on posix:

    base,/home/sirrobin/.local
    platbase,/home/sirrobin/.local
    purelib,$base/lib/pythonX.Y/site-packages
    platlib,$platbase/lib/pythonX.Y/site-packages
    scripts,$base/bin
    data,share

Custom installation scheme:

    base,/home/sirrobin/.local
    platbase,/home/sirrobin/.local
    purelib,$base/lib/pythonX.Y/site-packages
    platlib,$platbase/lib/pythonX.Y/site-packages
    scripts,/usr/local/bin
    data,/usr/local/share/

#### Default values 

Tables summarising the default values on different operating systems:

##### posix

| Prefix identifier | Default value: Standard scheme | Default value: User scheme | Environment variable | Command line option |
|---|---|---|---|---|
| `$base` | `sys.prefix` | `~/.local` | `$PYDIST_BASE` | `--prefix` |
| `$platbase` | `sys.exec_prefix` | `~/.local` | `$PYDIST_PLATBASE` | `--exec-prefix` |
| `$purelib` | `$base/lib/pythonX.Y/site-packages` | `$base/lib/pythonX.Y/site-packages` | `$PYDIST_PURELIB` | `--install-purelib` |
| `$platlib` | `$platbase/lib/pythonX.Y/site-packages` | `$platbase/lib/pythonX.Y/site-packages` | `$PYDIST_PLATLIB` | `--install-platlib` |
| `$scripts` | `$base/bin` | `$base/bin` | `$PYDIST_SCRIPTS` | `--install-scripts` |
| `$data` | `$base/share` | `$base/share` | `$PYDIST_DATA` | `--install-data` |

##### nt

| Prefix identifier | Default value: Standard scheme | Default value: User scheme | Environment variable | Command line option |
|---|---|---|---|---|
| `$base` | `sys.prefix` | `os.environ.get('%APPDATA%')` | `$PYDIST_BASE` | `--prefix` |
| `$platbase` | `sys.exec_prefix` | `os.environ.get('%APPDATA%')` | `$PYDIST_PLATBASE` | `--exec-prefix` |
| `$purelib` | `$base/Python` | `$base/Python/PythonXY/site-packages` | `$PYDIST_PURELIB` | `--install-purelib` |
| `$platlib` | `$platbase/Python` | `$platbase/Python/PythonXY/site-packages` | `$PYDIST_PLATLIB` | `--install-platlib` |
| `$scripts` | `$base/Scripts` | `$base/Python/Scripts` | `$PYDIST_SCRIPTS` | `--install-scripts` |
| `$data` | `$base/Data` | `$base/Python/Python26` | `$PYDIST_DATA` | `--install-data` |

##### mac

##### os2

##### ce

##### java

##### riscos

### API 

The Distribution class will get a new attribute `prefixes` which holds a dictionary mapping prefix identifiers to their absolute paths.

Usage example:

    >>> foo_dist = pkgutil.get_distribution('foo')
    >>> foo_dist.prefixes['$base']
    '/usr'
    >>> foo_dist.prefixes['$data']
    '/usr/share'
    >>> ni_wish = open(os.path.join(foo_dist.prefixes.get('$data'), 'foo', 'shrubbery.jpg'))
    >>> unladen = open(os.path.join(foo_dist.prefixes['$data'], 'foo', 'european.swallow'))
