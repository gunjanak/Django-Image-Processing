# Generated by Django 4.2 on 2023-05-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0004_remove_imageenhance_created_at_imageenhance_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageenhance',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
