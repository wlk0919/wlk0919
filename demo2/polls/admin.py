from django.contrib import admin

# Register your models here.
from .models import *
# 为了能够在Django的admin中显示创建的模型
admin.site.register(Question)

admin.site.register(Choice)