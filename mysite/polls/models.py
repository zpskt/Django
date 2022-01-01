from django.db import models

# Create your models here.
'''
在 Django 里写一个数据库驱动的 Web 应用的第一步是定义模型 - 也就是数据库结构设计和附加的其它元数据。
在这个投票应用中，需要创建两个模型：问题 Question 和选项 Choice。Question 模型包括问题描述和发布时间。
Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。
'''
'''
下面的一小段用于创建模型的代码给了 Django 很多信息，通过这些信息，Django 可以：

    为这个应用创建数据库 schema（生成 CREATE TABLE 语句）。
    创建可以与 Question 和 Choice 对象进行交互的 Python 数据库 API。

但是首先得把 polls 应用安装到我们的项目里。
'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
