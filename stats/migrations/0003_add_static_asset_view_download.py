# Generated by Django 3.0.14 on 2021-11-01 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('static_assets', '0010_set_source_type_default'),
        ('stats', '0002_simplify_stats_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticAssetView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('user_id', models.PositiveIntegerField(null=True)),
                ('static_asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='static_assets.StaticAsset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticAssetDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('user_id', models.PositiveIntegerField(null=True)),
                ('static_asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='static_assets.StaticAsset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='staticassetview',
            index=models.Index(fields=['static_asset_id', 'user_id', 'ip_address'], name='stats_stati_static__d0873e_idx'),
        ),
        migrations.AddConstraint(
            model_name='staticassetview',
            constraint=models.UniqueConstraint(condition=models.Q(ip_address__isnull=False), fields=('static_asset_id', 'ip_address'), name='stats_staticassetview_ip_address_uniq_key'),
        ),
        migrations.AddConstraint(
            model_name='staticassetview',
            constraint=models.UniqueConstraint(condition=models.Q(user_id__isnull=False), fields=('static_asset_id', 'user_id'), name='stats_staticassetview_user_id_uniq_key'),
        ),
        migrations.AddIndex(
            model_name='staticassetdownload',
            index=models.Index(fields=['static_asset_id', 'user_id', 'ip_address'], name='stats_stati_static__4dfb13_idx'),
        ),
        migrations.AddConstraint(
            model_name='staticassetdownload',
            constraint=models.UniqueConstraint(condition=models.Q(ip_address__isnull=False), fields=('static_asset_id', 'ip_address'), name='stats_staticassetdownload_ip_address_uniq_key'),
        ),
        migrations.AddConstraint(
            model_name='staticassetdownload',
            constraint=models.UniqueConstraint(condition=models.Q(user_id__isnull=False), fields=('static_asset_id', 'user_id'), name='stats_staticassetdownload_user_id_uniq_key'),
        ),
    ]