# Generated by Django 5.1.1 on 2024-10-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0016_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='apply_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
