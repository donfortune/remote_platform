# Generated by Django 5.1.1 on 2024-10-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0017_job_apply_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='viewed_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
