# Generated by Django 2.2.15 on 2020-09-01 10:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_gallery_image_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content_2',
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
