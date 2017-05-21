from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    creationDate=models.DateTimeField(auto_now=True,blank=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    
