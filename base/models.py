from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
