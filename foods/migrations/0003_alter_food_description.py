# Generated by Django 5.2 on 2025-04-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(default='None'),
        ),
    ]
