# Generated by Django 3.0.14 on 2021-10-25 15:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20201218_1135'),
        ('characters', '0003_characterversion_date_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charactershowcase',
            options={'ordering': ['order', '-date_published']},
        ),
        migrations.AddField(
            model_name='charactershowcase',
            name='date_published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='charactershowcase',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactershowcase',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charactershowcase',
            name='title',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CharacterShowcaseComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_showcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.CharacterShowcase')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comments.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='charactershowcase',
            name='comments',
            field=models.ManyToManyField(related_name='character_showcase', through='characters.CharacterShowcaseComment', to='comments.Comment'),
        ),
    ]
