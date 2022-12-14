# Generated by Django 3.0.14 on 2021-09-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20201218_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='show_landing_page',
            field=models.BooleanField(default=False, help_text='Show a landing page to non-subscribers instead of film content'),
        ),
    ]
