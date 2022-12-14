# Generated by Django 3.0.9 on 2021-03-11 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('looper', '0058_adjust_tax_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('subscription', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team', to='looper.Subscription')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_users', to='subscriptions.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Team Users',
                'verbose_name_plural': 'Team Users',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(related_name='teams', through='subscriptions.TeamUsers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SubscriptionProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('seats', models.IntegerField(blank=True, null=True)),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='looper.Subscription')),
            ],
            options={
                'verbose_name': 'Subscription Properties',
                'verbose_name_plural': 'Subscription Properties',
            },
        ),
    ]
