---
title: Werkzeug简易教程
date: 2016-12-02 19:52:21
toc: true
categories: python
tags: werkzeug
---

Werkzeug是一个专门用来处理HTTP和WSGI的工具库，可以方便的在Python程序中处理HTTP协议相关内容。

这里稍微说一下，werkzeug不是一个web服务器，也不是一个web框架，而是一个工具包，
官方的介绍说是一个WSGI工具包，它可以作为一个Web框架的底层库，
因为它封装好了很多Web框架的东西，例如 Request，Response 等等。

例如我最常用的Flask框架就是以Werkzeug为基础开发的，这也是我要专门探究Werkzeug底层的原因，
因为我想知道Flask的实现逻辑以及底层控制。这篇文章没有涉及到Flask的相关内容，
只是以Werkzeug创建一个简单的Web应用，然后以这个Web应用为例剖析请求的处理以及响应的产生过程。<!--more-->

官网教程给了个例子，创建一个类似[TinyURL](http://tinyurl.com/)的WEB应用，我就用官网这个例子来说明。

另外我还提一下python里面另一个函数库就是[Requests](http://python-requests.org/)，这是一个HTTP客户端库。
跟Werkzeug没有可比性，一个客户端库，一个服务器端库。

## WSGI
关于WSGI我这里再不重复讲了，专门写了篇[《WGSI简易教程》](https://www.xncoding.com/2016/04/22/python/wsgi.html)说明，
读者如果不懂的可以去看看，写的比较详细了。

一个最简单的WSGI应用:
``` python
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!']
```

我们使用Werkzeug来包装请求和相应之后，变成这样:
``` python
from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    text = 'Hello %s!' % request.args.get('name', 'World')
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)
```

关于WSGI你知道这么多就足够了。

## 写一个简单的web应用

下面我一步步来写这个tinyurl应用，名字叫shortly行不，模板使用jinjia2，后台存储使用redis。

先按照相应的依赖
``` bash
pip install Jinja2 redis
```

注意上面按照的redis是python客户端，还需要有真正的redis-server，服务器怎样按照redis我就不多讲了。
我在windows上面写这个教程，所以方便起见直接用了一个[windows的版本](https://github.com/ServiceStack/redis-windows)

### 第1步：创建文件夹
首先创建下面这样结构的文件夹：
```
/shortly
    /static
    /templates
```
`shortly`文件夹不是python包，用来给我们放文件用，其实就是我们项目根目录，
`static`文件夹放css、js、图片等静态文件，`templates`文件夹放我们的jinjia2模板文件。

### 第2步：基本结构
我们在`shortly`文件夹下面创建`shortly.py`，这里面会引入很多包，
我一开始就把它们全部引入进来，省的后面再重复写，所有的引入如下:
``` python
import os
import redis
from urllib import parse as urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
```

现在来创建一个基本结构类，并通过一个函数来创建这个类的实例，
同时通过一个可选设置创建一个中间件，将`static`文件夹暴露给用户：
``` python
class Shortly(object):

    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])

    def dispatch_request(self, request):
        return Response('Hello World!')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Shortly({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app
```

最后我们启动一个开发环境服务器，带有自动代码热加载和调试功能：
``` python
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
```


