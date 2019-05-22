from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 分类类(继承Model类)
class Categroy(models.Model):
    # 如果是字符串形式的数据，就要规定长度length
    title=models.CharField(max_length=30)
    # 调用内部方法，返回title数据
    def __str__(self):
        return  self.title
    #改变admin里的表名
    # class Meta():
    #     # 自定义表名
    #     verbose_name='分类'
    #     # 当数据是复数时，仍为定义的表名，可去掉原有的s
    #     # 具体内容可通过查询  User类
    #     verbose_name_plural=verbose_name
# 标签类（继承Model方法）
class Tag(models.Model):
    # CharField类型的字段，需要规定长度
    title=models.CharField(max_length=30)
    # 类的内部方法，返回title数据
    def __str__(self):
        return self.title
    # class Meta():
    #     varbose_name='标签'
    #     varbose_name_plural=varbose_name
# 文章类（继承Model方法）
class Article(models.Model):
    # 标题
    title=models.CharField(max_length=50)
    # 文本框
    body=models.TextField()
    # 创建时间(auto_now_add表示自动添加创建的时间不可变)
    create_time=models.DateTimeField(auto_now_add=True)
    # 更改时间（auto_now表示修改的当前时间）
    update_time=models.DateTimeField(auto_now=True)

    # 接下来是外键(括号内第一部分写主键的类名，第二部分是级联的一些方法，注意格式)
    category=models.ForeignKey(Categroy,on_delete=models.CASCADE)
    # 多对多时，只需写主键的类名
    tags=models.ManyToManyField(Tag)
    auther=models.ForeignKey(User,models.CASCADE)
    def __str__(self):
        return  self.title
    # class Meta():
    #     verbose_name='文章'
    #     verbose_name_plural = verbose_name
