# Generated by Django 5.1.1 on 2024-10-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0009_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
