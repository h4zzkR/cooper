from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone as time
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='users')

"""
Sync extended UserProfile with django's User
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


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