# Generated by Django 2.2.15 on 2020-09-01 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200901_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image_2',
        ),
    ]
