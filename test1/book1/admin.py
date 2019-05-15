from django.contrib import admin
from .models import bookInfo,heroinfo
# Register your models here.
# 自定义管理页面

list_display=['name','data']



admin.site.register(bookInfo)
admin.site.register(heroinfo)