# Generated by Django 5.1.1 on 2024-10-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0004_job_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
