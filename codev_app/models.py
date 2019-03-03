from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone as time
import datetime

class Task(models.Model):
    idea = models.CharField(max_length=200)
    body = models.TextField(max_length=10000)
    creation_date = models.DateTimeField(default=time.now)
    author = models.ForeignKey(to=User, blank=True, on_delete=models.CASCADE, null=True)

class PropertyImage(models.Model):
    name = models.ForeignKey(Task, related_name='Task', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)