# Generated by Django 5.1.1 on 2024-10-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0003_category_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
