# Generated by Django 3.0.14 on 2021-10-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterversion',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='characterversion',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
