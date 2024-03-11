from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)