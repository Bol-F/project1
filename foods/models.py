from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    description = models.TextField(default='None')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price', 'name']
