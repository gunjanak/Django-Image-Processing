# Generated by Django 4.2 on 2023-05-22 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0002_imageenhance_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageenhance',
            name='updated_at',
        ),
    ]
