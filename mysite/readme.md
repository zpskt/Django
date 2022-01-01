cd Django #到mysite的同级目录
django-admin startproject mysite #mysite是你网站名，失败了确认一下你安装了django，这个命令是快捷初始化配置

    最外层的 mysite/ 根目录只是你项目的容器， 根目录名称对 Django 没有影响，你可以将它重命名为任何你喜欢的名称。
    manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 django-admin 和 manage.py 获取所有 manage.py 的细节。
    里面一层的 mysite/ 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls).
    mysite/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 更多关于包的知识。
    mysite/settings.py：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 Django 配置 了解细节。
    mysite/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。阅读 URL调度器 文档来获取更多关于 URL 的内容。
    mysite/asgi.py：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 如何使用 ASGI 来部署 了解更多细节。
    mysite/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 如何使用 WSGI 进行部署 了解更多细节。
运行代码：python manage.py runserver 8080 #默认为8000可以自己修改端口,查看端口成功，证明demo ok了
新建一个应用：python manage.py startapp polls
默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下命令：
$ python manage.py migrate
#通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移。
新建了app应用后，并且也设置了model了，应该再执行命令
$ python manage.py makemigrations polls
Django 有一个自动执行数据库迁移并同步管理你的数据库结构的命令 - 这个命令是 migrate，我们马上就会接触它 - 
但是首先，让我们看看迁移命令会执行哪些 SQL 语句。sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：
$ python manage.py sqlmigrate polls 0001
如果你感兴趣，你也可以试试运行 python manage.py check ;这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。
现在，你只需要记住，改变模型需要这三步：

    编辑 models.py 文件，改变模型。
    运行 python manage.py makemigrations 为模型的改变生成迁移文件。
    运行 python manage.py migrate 来应用数据库迁移。

数据库迁移被分解成生成和应用两个命令是为了让你能够在代码控制系统上提交迁移数据并使其能在多个应用里使用；这不仅仅会让开发更加简单，也给别的开发者和生产环境中的使用带来方便。


创建一个管理员账号¶

首先，我们得创建一个能登录管理页面的用户。请运行下面的命令：
/ 

$ python manage.py createsuperuser

键入你想要使用的用户名，然后按下回车键：

Username: admin

然后提示你输入想要使用的邮件地址：

Email address: admin@example.com

最后一步是输入密码。你会被要求输入两次密码，第二次的目的是为了确认第一次输入的确实是你想要的密码。

Password: **********
Password (again): *********
Superuser created successfully.

