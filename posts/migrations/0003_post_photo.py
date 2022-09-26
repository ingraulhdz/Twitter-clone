# Generated by Django 4.1.1 on 2022-09-26 21:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo'),
        ),
    ]
