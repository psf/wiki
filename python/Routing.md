# Routing

::: {#content dir="ltr" lang="en"}
**Routing** (also known as `request routing`{.backtick} or `URL dispatching`{.backtick}) is mapping URLs to code that handles them.

Why routing is important? By directly connecting the content that you see on a web page (especially if it is an error), good routing drastically reduces time (and money) that required to improve this content (or fix the error). That\'s why Django has [this link](https://docs.djangoproject.com/en/1.6/topics/http/urls/){.https} on its front page.

Ever heard of spaghetti code? Web applications is a good example of that. When we start reading a book - we have only single **entrypoint** - start of the book. If you read source code of web applications - there are usually no defined entrypoints, so the first thing you do is find some webpage and the run search to find out where is the code for it. Clearly defined routing not only saves you time on searching, but URLs gathered in one place give a good overview of application capabilities.

Good routing map is a like a map of the city you\'re going to explore.

### Routing in Python Web Frameworks {#Routing_in_Python_Web_Frameworks}

Usability of routing component can be estimated with the help of the following questions:

1.  How easy is to get overview of all URLs that web application processes?
2.  How easy is to make reverse mapping (code to URL)?
3.  How easy is to serve static content URLs (css, js, images) by external server

#### Bottle Routing {#Bottle_Routing}

    @route('/hello/<name>')
    def index(name):
      return '<b>Hello {{name}}</b>!'

or

    def setup_routing():
      bottle.route('/', 'GET', index)
      bottle.route('/edit', ['GET', 'POST'], edit)

Get overview of URLs handled: search for \"@route\" or for \".route(\"

[http://bottlepy.org/docs/dev/index.html](http://bottlepy.org/docs/dev/index.html){.http}

#### Flask Routing {#Flask_Routing}

    @app.route('/hello/<username>')
    def show_user_message(username):
        return 'Hello %s' % username

Get overview of URLs handled: search for \".route(\"

[http://flask.pocoo.org/docs/0.10/quickstart/#routing](http://flask.pocoo.org/docs/0.10/quickstart/#routing){.http}

#### Django Routing Classic (pre 1.8 era) {#Django_Routing_Classic_.28pre_1.8_era.29}

    # --- urls.py ---
    from django.conf.urls import patterns, url

    urlpatterns = patterns('',  # <-- common prefix for sugar-coating, like 'news.views'
        url(r'^articles/2003/$', 'news.views.special_case_2003'),
        url(r'^articles/(\d{4})/$', 'news.views.year_archive'),
        url(r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),
        url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),
    )

Get overview of URLs handled: find settings.py, look for ROOT_URLCONF for name of Python modules with the location of URL map (usually named \'urls\'), find referenced module (\'urls.py\'), read urls.py to understand how `urlpatterns`{.backtick} is constructed (it may contain [included apps](https://docs.djangoproject.com/en/dev/intro/reusable-apps/){.https}).

[https://docs.djangoproject.com/en/1.6/topics/http/urls/](https://docs.djangoproject.com/en/1.6/topics/http/urls/){.https}

#### Django Routing (1.8+) {#Django_Routing_.281.8.2B-.29}

Classic routing scheme described above for historical reference [is deprecated](https://docs.djangoproject.com/en/dev/releases/1.8/#django-conf-urls-patterns){.https}. Implicit imports that reference modules as strings break static analysis of Python code, empty first parameter is confusing to new users, so the new scheme is:

    # --- urls.py ---
    from django.conf.urls import url
    import news.views

    urlpatterns = [
        url(r'^articles/2003/$', news.views.special_case_2003),
        url(r'^articles/(\d{4})/$', news.views.year_archive),
        url(r'^articles/(\d{4})/(\d{2})/$', news.views.month_archive),
        url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', news.views.article_detail),
    ]
:::
