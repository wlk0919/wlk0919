from django.db import models
# 引入django自带的用户
from django.contrib.auth.models import User

# Create your models here.

class myUser(User):
    url=models.URLField(blank=True,null=True,default='http://www.baidu.com')

    class Meta():
        verbose_name='用户'
        verbose_name_plural=verbose_name

class Rooms(models.Model):
    title=models.CharField(max_length=50)
    detail=models.CharField(max_length=100)
    price=models.IntegerField(default=500)
    class Meta():
        verbose_name='酒店房间'
        verbose_name_plural=verbose_name


class myRoom(models.Model):
    # id，房间名，房间价格，总价格 ，
    title=models.CharField(max_length=50)
