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

`Shortly` 类是一个标准的WSGI应用，它的`__call__`方法直接将请求转发至`wsgi_app`。
因此我们通过中间件对`wsgi_app`方法进行再一次的包装，正如我们示例中那样。
在`dispatch_request`你甚至还可以继续返回另外一个WSGI应用。

`create_app`工厂函数能用来创建我们的WSGI应用，不仅可以传递参数，还能添加另外的中间件。
比如我们示例中的一个静态文件访问中间件。

现在我们可以通过运行这个python脚本来在本机启动一个服务器了。
```
$ python shortly.py
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 172-919-408
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

现在打开浏览器输入：`http://localhost:5000` 看看效果:
![](https://xnstatic-1253397658.file.myqcloud.com/flask20.png)

### 第3步：设置Environment
我们有了一个基本的框架类，可以在构造器中添加更多有用的东西，
后面我们要用到redis和jinja2模板，可以在这里初始化配置。

``` python
def __init__(self, config):
    self.redis = redis.Redis(config['redis_host'], config['redis_port'])
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                 autoescape=True)

def render_template(self, template_name, **context):
    t = self.jinja_env.get_template(template_name)
    return Response(t.render(context), mimetype='text/html')
```

### 第4步：路由
路由就是将不同的URL映射到相应的处理器上面，Werkzeug为我们提供了一个非常灵活的路由系统。
你只需要创建一个`Map`对象，并在里面添加许多`Rule`对象，
每一个`Rule`对象定义一个URL匹配规则和一个`endpoint`，
这个`endpoint`就是一个字符串并能唯一标示这个URL，
我们还可以利用它来逆向解析URL，不过这里我暂时不打算讲这个。

只需要在构造器中添加下面的Map:
``` python
self.url_map = Map([
    Rule('/', endpoint='new_url'),
    Rule('/<short_id>', endpoint='follow_short_link'),
    Rule('/<short_id>+', endpoint='short_link_details')
])
```
这里我们定义了三个URL规则，每个URL会分发给不同的处理函数，
那么怎样由`endpoint`得到正确的处理函数呢，这个取决于你自己定义规则，
比如这里我准备使用函数名为`on_`+`endpoint`的方式：
``` python
def dispatch_request(self, request):
    adapter = self.url_map.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        return getattr(self, 'on_' + endpoint)(request, **values)
    except HTTPException as e:
        return e
```

比如我们的URL为`http://localhost:5000/foo`，返回的值为:
``` python
endpoint = 'follow_short_link'
values = {'short_id': u'foo'}
```

如果没有找到匹配的规则就会抛出`NotFound`异常，也是`HTTPException`子类。
所有的HTTP异常本身也是一个WSGI应用，返回一个默认的错误页面。
因此我们只需要捕获它并直接抛出它即可。

如果一切正常，那么就会跑到函数`on_follow_short_link`上面处理。

### 第5步：第一个View
我们先来定义第一个view：
``` python
def on_new_url(self, request):
    error = None
    url = ''
    if request.method == 'POST':
        url = request.form['url']
        if not is_valid_url(url):
            error = 'Please enter a valid URL'
        else:
            short_id = self.insert_url(url)
            return redirect('/%s+' % short_id)
    return self.render_template('new_url.html', error=error, url=url)
```

这个方法很容易理解，如果请求是POST，先检查URL是否合法，如果合法就取出`url`值，
并插入数据库，并且重定向到详情页面。否则就返回`new_url.html`页面。

坚持URL是否合法的函数：
``` python
def is_valid_url(url):
    parts = urlparse.urlparse(url)
    return parts.scheme in ('http', 'https')
```

将url插入到redis数据库中：
``` python
def insert_url(self, url):
    short_id = self.redis.get('reverse-url:' + url)
    if short_id is not None:
        return short_id
    url_num = self.redis.incr('last-url-id')
    short_id = base36_encode(url_num)
    self.redis.set('url-target:' + short_id, url)
    self.redis.set('reverse-url:' + url, short_id)
    return short_id
```

数字的36位编码函数：
``` python
def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))
```

### 第6步：重定向view
这一步比较简单，就是从redis中找到长地址然后重定向到上面。
同时我还使用一个计数器来追踪到底这个链接被点击过多少次：
``` python
def on_follow_short_link(self, request, short_id):
    link_target = self.redis.get('url-target:' + short_id)
    if link_target is None:
        raise NotFound()
    self.redis.incr('click-count:' + short_id)
    return redirect(link_target)
```

### 第7步：详情页面
这个页面非常简单，只需要通过一个模板来显示即可。
除了展示原始链接外，还会将点击次数也显示出来，默认点击数为0：
``` python
def on_short_link_details(self, request, short_id):
    link_target = self.redis.get('url-target:' + short_id)
    if link_target is None:
        raise NotFound()
    click_count = int(self.redis.get('click-count:' + short_id) or 0)
    return self.render_template('short_link_details.html',
        link_target=link_target,
        short_id=short_id,
        click_count=click_count
    )
```
注意redis处理的是字符串，你必须手动转换为int计算。

### 第8步：模板
下面是所有模板，只需要将它们放到templates目录即可，Jinja2支持模板继承，
所以我们第一步就是创建一个基础模板，另外我们还设置Jinja2自动为我们转义HTML字符，
这可以防止XSS攻击和网页渲染错误：

`layout.html`
``` html
<!doctype html>
<title>{% block title %}{% endblock %} | shortly</title>
<link rel=stylesheet href=/static/style.css type=text/css>
<div class=box>
  <h1><a href=/>shortly</a></h1>
  <p class=tagline>Shortly is a URL shortener written with Werkzeug
  {% block body %}{% endblock %}
</div>
```

`new_url.html`
``` html
{% extends "layout.html" %}
{% block title %}Create New Short URL{% endblock %}
{% block body %}
  <h2>Submit URL</h2>
  <form action="" method=post>
    {% if error %}
      <p class=error><strong>Error:</strong> {{ error }}
    {% endif %}
    <p>URL:
      <input type=text name=url value="{{ url }}" class=urlinput>
      <input type=submit value="Shorten">
  </form>
{% endblock %}
```

`short_link_details.html`
``` html
{% extends "layout.html" %}
{% block title %}Details about /{{ short_id }}{% endblock %}
{% block body %}
  <h2><a href="/{{ short_id }}">/{{ short_id }}</a></h2>
  <dl>
    <dt>Full link
    <dd class=link><div>{{ link_target }}</div>
    <dt>Click count:
    <dd>{{ click_count }}
  </dl>
{% endblock %}
```

### 第9步：样式
另外我还简单添加了一些样式，让页面显示更加美观点，写到`static/style.css`文件中：
``` css
body        { background: #E8EFF0; margin: 0; padding: 0; }
body, input { font-family: 'Helvetica Neue', Arial,
              sans-serif; font-weight: 300; font-size: 18px; }
.box        { width: 500px; margin: 60px auto; padding: 20px;
              background: white; box-shadow: 0 1px 4px #BED1D4;
              border-radius: 2px; }
a           { color: #11557C; }
h1, h2      { margin: 0; color: #11557C; }
h1 a        { text-decoration: none; }
h2          { font-weight: normal; font-size: 24px; }
.tagline    { color: #888; font-style: italic; margin: 0 0 20px 0; }
.link div   { overflow: auto; font-size: 0.8em; white-space: pre;
              padding: 4px 10px; margin: 5px 0; background: #E5EAF1; }
dt          { font-weight: normal; }
.error      { background: #E8EFF0; padding: 3px 8px; color: #11557C;
              font-size: 0.9em; border-radius: 2px; }
.urlinput   { width: 300px; }
```

最后测试下你这个小应用看看，是否很有成就感，先打开`http://localhost:5000`，
然后输入某个网站比如`http://www.baidu.com`：

![](https://xnstatic-1253397658.file.myqcloud.com/flask21.png)

之后进入详情页面：

![](https://xnstatic-1253397658.file.myqcloud.com/flask22.png)

