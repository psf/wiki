# tftp

::: {#content dir="ltr" lang="en"}
TFTP is an extremely simple (some would say trivial) file transfer protocol. This simplicity is achieved by only having 6 message types and only allowing a single message to be in flight at a given time. TFTP is often used in embedded environments where simplicity of implementation is more important than attempting to achieve high throughput. TFTP is often layered over UDP, though this is not necessary.

References to Python-related tftp servers:

- [TFTPy](http://tftpy.sourceforge.net/){.http} is a pure python TFTP client and server implementation under development.

- [http://code.google.com/p/tftpgui/](http://code.google.com/p/tftpgui/){.http} is a python TFTP server with GUI available for Python 2 and Python 3

- [https://github.com/psychomario/PyPXE](https://github.com/psychomario/PyPXE){.https} TFTP with DHCP for PXE. Python 3 support is not here yet but is planned.
:::
