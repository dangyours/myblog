from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.

class ArticlePost(models.Model):
    author = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title