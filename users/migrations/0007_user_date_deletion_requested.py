# Generated by Django 3.0.9 on 2021-01-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_replace_profile_can_view_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_deletion_requested',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]