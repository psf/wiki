# SSLModule

::: {#content dir="ltr" lang="en"}
Jython 2.7 fully supports the ssl module including as of 2.7.1 beta 2, most of ssl.SSLContext. The one major exception is server sockets that support STARTTLS protocols (FTP over SSL, \...) that negotiate from plain text to SSL-secured text, due to a limitation of Netty 4.
:::
