# Generated by Django 3.0.9 on 2020-12-21 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0003_add_follow_flag'),
        ('users', '0003_move_profile_fields'),
        ('profiles', '0004_move_notifications'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_read', models.DateTimeField(blank=True, null=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='actstream.Action')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
                'db_table': 'users_notification',
            },
            bases=(models.Model,),
        )
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
