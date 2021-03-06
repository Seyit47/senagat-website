# Generated by Django 2.2.15 on 2020-09-03 12:13

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200902_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='tender/images')),
                ('image_crop', models.ImageField(upload_to='tender/images_crop')),
                ('thumbnail', models.ImageField(upload_to='tender/thumbnail')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'tender',
                'verbose_name_plural': 'tenders',
            },
        ),
    ]
