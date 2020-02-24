from django.contrib import admin

# Register your models here.
from .models import Question
# 注册后，会在管理页面显示
admin.site.register(Question)
