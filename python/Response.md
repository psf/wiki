# Response

:::: {#content dir="ltr" lang="en"}
Building **Response** object is a common way to return information from URL handler back to web framework for returning to client:

- Django: [https://docs.djangoproject.com/en/1.7/ref/request-response/#httpresponse-objects](https://docs.djangoproject.com/en/1.7/ref/request-response/#httpresponse-objects){.https}

- Flask: [http://flask.pocoo.org/docs/0.10/api/#response-objects](http://flask.pocoo.org/docs/0.10/api/#response-objects){.http}

- Bottle: [http://bottlepy.org/docs/dev/tutorial.html#tutorial-response](http://bottlepy.org/docs/dev/tutorial.html#tutorial-response){.http}

- webapp2/WebOb: [http://webapp-improved.appspot.com/api/webapp2.html#webapp2.Response](http://webapp-improved.appspot.com/api/webapp2.html#webapp2.Response){.http}

::: {}
+:---------------------------------------------------------------------------------------------------------------:+:-----------------------------------:+
| **Default Content-Type**                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [Django](https://docs.djangoproject.com/en/1.7/ref/request-response/#django.http.HttpResponse.__init__){.https} | text/html; charset=utf-8            |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [Flask](http://flask.pocoo.org/docs/0.10/api/#response-objects){.http}                                          | text/html; charset=utf-8            |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [Bottle](http://bottlepy.org/docs/dev/tutorial.html#generating-content){.http}                                  | ﻿text/html; charset=utf-8\           |
|                                                                                                                 | application/json\                   |
|                                                                                                                 | \<empty\>                           |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| [webapp2/WebOb](http://webapp-improved.appspot.com/guide/response.html#guide-response){.http}                   | ﻿﻿text/html; charset=utf-8            |
+-----------------------------------------------------------------------------------------------------------------+-------------------------------------+
:::
::::
