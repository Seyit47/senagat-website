# Generated by Django 2.2.15 on 2020-09-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200904_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='title',
            field=models.CharField(max_length=900),
        ),
    ]
