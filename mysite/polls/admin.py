from django.contrib import admin

# Register your models here.
#只需要再做一件事：我们得告诉管理，问题 Question 对象需要一个后台接口。打开 polls/admin.py 文件，把它编辑成下面这样：
from .models import Question

admin.site.register(Question)