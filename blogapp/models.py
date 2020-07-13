from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.
class Blog_Article(models.Model):
    title = models.CharField(max_length=400)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)