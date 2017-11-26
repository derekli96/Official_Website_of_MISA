后端服务器说明
后端server采用Django框架。数据库采用MySQL。下面对其中几个重要文件做一点说明。
（server主文件夹）
settings.py：这是Django项目的主要配置文件，包括数据库设置、网页语言、需要turn on的Django功能等。
urls.py：这是另外一个配置文件。它是介于URLS和用来处理它们的Python方法之间的匹配。
wsgi.py：我们的Django部署平台是uWSGI，该文件用来配置它。

（runningbear子文件夹）
models.py：与数据库相关的代码都包含在这个文件中。它是Django ORM（对象关系映射）中的重要一环。
views.py：该文件是我们后端代码中最重要的一个文件，包含了我们server的所有函数逻辑。我们通过views.py和urls.py及models.py相配合，在后端实现了10个函数接口，如下表所示。

函数接口  	功能说明
log	  	登录
register  	注册
search	  	资料查询
up	  	资料上传
Introduction	跳转至“关于我们”页面
News		跳转至“最新消息”页面
Resources	跳转至“课程资源”页面
Upload		跳转至“文件上传”页面
Login		跳转至“登录注册”页面
Sponsor		跳转至“赞助商”页面

前端网页说明
前端选用了Bootstrap框架，以HTML，JavaScript，CSS为基本开发语言，并实现了与后端服务器和数据库的交互。

Bootstrap框架
Bootstrap框架是来自 Twitter的目前很受欢迎的前端框架，其基于HTML、CSS、JavaScript。选择Bootstrap框架的优势在于其简单灵活，包含了具有全局性且具有若干个可扩展class的CSS、丰富的组件和若干个自定义的JQuery插件。一方面，使用Bootstrap框架减少了人工开发CSS和组件的难度和时间，可以通过调用其已有的类和组件来美观地实现布局。另一方面，Bootstrap框架具有较大的灵活性，对于需要自定义的布局，可以灵活地添加或修改相应的CSS代码。

JQuery
JQuery是一个快速、简洁的JavaScript框架。由于其封装了许多常用的JavaScript代码，因此选择JQuery可以优化对HTML的操作、事件处理和信息传输。此外，JQuery还具有可扩展机制和对各类浏览器的高兼容性。使用JQuery封装好的接口不仅可以降低JavaScript代码的冗余程度，同时还能根据网站需要灵活扩展功能。

AJAX
选择AJAX进行数据传输的优点在于， AJAX 可以通过与服务器进行少量数据交换，实现网页异步更新，而无须在更新后对整个网页进行重新加载。其减少了用户在网页数据更新后加载的时间，提高了用户体验。

JSON
网站前后端的数据交互使用了JSON数据交互格式。由于JSON的层次清晰简洁，因此其不仅利于机器的生成和解析，同时也方便我们在编程时进行阅读和编写，降低了数据传输和解析过程中的出错率。

