from django.db import models

# Create your models here.
# 用于继承Model
class bookInfo(models.Model):
    # 表示字符型数据，要设置字符长度
    name=models.CharField(max_length=20)
    data=models.DateTimeField()
    def __str__(self):
        return self.name

class heroinfo(models.Model):
    name=models.CharField(max_length=50)
    #bool
    ender=models.BooleanField()
    content=models.CharField(max_length=100)
    # 创建外键
    book=models.ForeignKey('bookinfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.name