from django.db import models

# Create your models here.
# 用于继承Model
class bookInfo(models.Model):
    # 表示字符型数据，要设置字符长度
    name=models.CharField(max_length=20,verbose_name='姓名')
    data=models.DateTimeField(verbose_name='出版日期')
    def __str__(self):
        return self.name

class heroinfo(models.Model):
    name=models.CharField(max_length=50,verbose_name='姓名')
    #bool
    # ender=models.BooleanField(verbose_name='性别')
    ender = models.CharField(max_length=20,verbose_name='性别',choices=(('男',0),('女',1)))
    content=models.CharField(max_length=100,verbose_name='简介')
    # 创建外键
    book=models.ForeignKey('bookinfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.name