from django.db import models
from polls.models import Article
# Create your models here.
class Comment(models.Model):
    username=models.CharField(max_length=50)
    #
    email=models.EmailField(blank=True,null=True)
    url=models.URLField(blank=True,null=True)
    content=models.CharField(max_length=500)
    # article=models.ForeignKey(A)