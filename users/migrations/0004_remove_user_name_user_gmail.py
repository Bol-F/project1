# Generated by Django 5.2 on 2025-05-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='gmail',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
