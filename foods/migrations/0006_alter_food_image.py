# Generated by Django 5.2 on 2025-05-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, default="'C:\\Users\\User\\Downloads\\ChatGPT Image 5 мая 2025 г., 19_00_51.png'", null=True, upload_to='food_images/'),
        ),
    ]
