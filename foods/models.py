from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    description = models.TextField(default='None')
    image = models.ImageField(upload_to='food_images/', blank=True, null=True, default="'C:\\Users\\User\\Downloads\\ChatGPT Image 5 мая 2025 г., 19_00_51.png'")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price', 'name']
