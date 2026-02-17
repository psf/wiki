# TcpCommunication

:::::::: {#content dir="ltr" lang="en"}
# TCP Communication {#TCP_Communication}

::: table-of-contents
Contents

1.  [TCP Communication](#TCP_Communication)
    1.  [Client](#Client)
    2.  [Server](#Server)
    3.  [Links](#Links)
2.  [Discussion](#Discussion)
:::

See also: [UdpCommunication](UdpCommunication)

## Client {#Client}

Here\'s simple code to send and receive data by TCP in Python:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-b22bc303d6d0b4c7af1a18623aacd1d0900b6ff3 dir="ltr" lang="en"}
   1 #!/usr/bin/env python
   2 
   3 import socket
   4 
   5 
   6 TCP_IP = '127.0.0.1'
   7 TCP_PORT = 5005
   8 BUFFER_SIZE = 1024
   9 MESSAGE = "Hello, World!"
  10 
  11 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  12 s.connect((TCP_IP, TCP_PORT))
  13 s.send(MESSAGE)
  14 data = s.recv(BUFFER_SIZE)
  15 s.close()
  16 
  17 print "received data:", data
```
:::
::::

## Server {#Server}

Here\'s simple code to serve TCP in Python:

:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-8322cd04487cb7048b047c5df45ee0c933d6a1c8 dir="ltr" lang="en"}
   1 #!/usr/bin/env python
   2 
   3 import socket
   4 
   5 
   6 TCP_IP = '127.0.0.1'
   7 TCP_PORT = 5005
   8 BUFFER_SIZE = 20  # Normally 1024, but we want fast response
   9 
  10 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  11 s.bind((TCP_IP, TCP_PORT))
  12 s.listen(1)
  13 
  14 conn, addr = s.accept()
  15 print 'Connection address:', addr
  16 while 1:
  17     data = conn.recv(BUFFER_SIZE)
  18     if not data: break
  19     print "received data:", data
  20     conn.send(data)  # echo
  21 conn.close()
```
:::
::::

## Links {#Links}

- [socket](http://www.python.org/doc/current/lib/module-socket.html){.http} \-- builtin Python module

- [telnetlib](http://www.python.org/doc/current/lib/module-telnetlib.html){.http} \-- builtin Python module

- [Introduction to TCP Sockets](http://woozle.org/~neale/papers/sockets.html){.http} \-- uses Python to explain. Note: substitute socket.AF_INET where socket.PF_INET is mentioned.

# Discussion {#Discussion}

- (none yet!)
::::::::
