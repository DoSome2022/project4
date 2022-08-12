# Generated by Django 3.0.14 on 2021-12-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    import common.help_texts

    dependencies = [
        ('films', '0010_fix_help_text_migrations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.TextField(blank=True, help_text='\n<p>Format the content in <a href="https://commonmark.org/help/">Markdown</a>.</p>\n<div>\n    <p>\n        To make images float left or right of the text, use the following:\n    </p>\n    <p>\n        <code>\n        {attachment StaticAssetID class=\'float-start\'}\n        </code>\n    </p>\n    <p>\n        <code>\n        {attachment StaticAssetID class=\'float-end\'}\n        </code>\n    </p>\n</div>\n<p title="<a>, <abbr>, <acronym>, <b>, <blockquote>, <code>, <em>, <i>, <li>, <ol>, <strong>, <ul>, <a>, <audio>, <caption>, <cite>, <col>, <colgroup>, <figcaption>, <figure>, <footer>, <img>, <p>, <source>, <table>, <tbody>, <td>, <tfoot>, <th>, <thead>, <tr>">Some HTML tags are allowed&nbsp;<span class="help help-tooltip">ℹ</span>'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='text',
            field=models.TextField(blank=True, help_text='\n<p>Format the content in <a href="https://commonmark.org/help/">Markdown</a>.</p>\n<div>\n    <p>\n        To make images float left or right of the text, use the following:\n    </p>\n    <p>\n        <code>\n        {attachment StaticAssetID class=\'float-start\'}\n        </code>\n    </p>\n    <p>\n        <code>\n        {attachment StaticAssetID class=\'float-end\'}\n        </code>\n    </p>\n</div>\n'),
        ),
        migrations.AlterField(
            model_name='filmflatpage',
            name='content',
            field=models.TextField(blank=True, help_text='\n<p>Format the content in <a href="https://commonmark.org/help/">Markdown</a>.</p>\n<div>\n    <p>\n        To make images float left or right of the text, use the following:\n    </p>\n    <p>\n        <code>\n        {attachment StaticAssetID class=\'float-start\'}\n        </code>\n    </p>\n    <p>\n        <code>\n        {attachment StaticAssetID class=\'float-end\'}\n        </code>\n    </p>\n</div>\n<p title="<a>, <abbr>, <acronym>, <b>, <blockquote>, <code>, <em>, <i>, <li>, <ol>, <strong>, <ul>, <a>, <audio>, <caption>, <cite>, <col>, <colgroup>, <figcaption>, <figure>, <footer>, <img>, <p>, <source>, <table>, <tbody>, <td>, <tfoot>, <th>, <thead>, <tr>">Some HTML tags are allowed&nbsp;<span class="help help-tooltip">ℹ</span>'),
        ),
        migrations.RunPython(
            common.help_texts._replace_float_classes_bs5('films', 'Asset', 'description'),
            reverse_code=common.help_texts._replace_float_classes_bs4('films', 'Asset', 'description'),
        ),
        migrations.RunPython(
            common.help_texts._replace_float_classes_bs5('films', 'Collection', 'text'),
            reverse_code=common.help_texts._replace_float_classes_bs4('films', 'Collection', 'text'),
        ),
        migrations.RunPython(
            common.help_texts._replace_float_classes_bs5('films', 'FilmFlatPage', 'content'),
            reverse_code=common.help_texts._replace_float_classes_bs4('films', 'FilmFlatPage', 'content'),
        ),
        migrations.RunPython(
            common.help_texts._replace_float_classes_bs5('films', 'FilmFlatPage', 'content_html'),
            reverse_code=common.help_texts._replace_float_classes_bs4('films', 'FilmFlatPage', 'content_html'),
        ),
    ]
