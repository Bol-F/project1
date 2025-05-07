from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Code(models.Model):
    code = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='code')
    expired_date = models.DateTimeField(default=timezone.now)
