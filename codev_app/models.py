from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    idea = models.CharField(max_length=200)
    body = models.TextField(max_length=10000)
    # creation_date = models.DateTimeField()
    #У задания может быть несколько авторов:
    author = models.ManyToManyField(to=User, blank=True)

class PropertyImage(models.Model):
    name = models.ForeignKey(Task, related_name='Task', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)