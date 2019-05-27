from django.db import models

# Create your models here.
# 问题类
class  Question(models.Model):
    title=models.CharField(max_length=50)
    class Meta():
        verbose_name='问题'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title
# class ChoiceManage(models.Manager):
#     def incressvotes(self,id):
#         c=self.get(pk=id)
#         c.votes+=1
#         c.save()

class Choice(models.Model):
    # 题目
    title=models.CharField(max_length=50)
    # 票数
    votes=models.IntegerField(default=0)
    # 外键（对象类型）,括号呢第一部分是关联的类，第二部分是关系，级联等
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    # objects=ChoiceManage()
    class Meta():
        verbose_name='选项'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title

