# Generated by Django 3.0.9 on 2021-08-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_assets', '0004_fill_image_thumbnails'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='loop',
            field=models.BooleanField(default=False),
        ),
    ]
