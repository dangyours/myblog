from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.
class BlogUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=1)
    # class Meta:
    #     ordering = ('-created',)
    
    # def __str__(self):
    #     return self.title
    def toDict(self):
        return {'name':self.name,
                'password':self.password,
                'created':self.created.strftime('%Y-%m-%d %H:%M:%S'),
                'status':self.status}