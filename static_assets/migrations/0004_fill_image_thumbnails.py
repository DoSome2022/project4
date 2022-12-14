# Generated by Django 3.0.9 on 2021-01-07 10:04

from django.db import migrations
from django.db.models import Q


def fill_image_thumbnails(apps, schema_editor):
    StaticAsset = apps.get_model('static_assets', 'StaticAsset')
    images = StaticAsset.objects.filter(
        source_type='image',
    ).filter(
        Q(thumbnail='') | Q(thumbnail__isnull=True),
    )
    for asset in images:
        if asset.thumbnail or asset.source_type != 'image':
            continue
        asset.thumbnail.name = asset.source.name
        asset.save(update_fields=['thumbnail'])


class Migration(migrations.Migration):

    dependencies = [
        ('static_assets', '0003_delete_storagelocation'),
    ]

    operations = [
        migrations.RunPython(fill_image_thumbnails, reverse_code=migrations.RunPython.noop),
    ]
