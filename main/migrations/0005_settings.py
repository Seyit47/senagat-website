# Generated by Django 2.2.15 on 2020-08-31 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_magazine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_content', models.TextField()),
                ('about_video', models.FileField(upload_to='document/video')),
                ('contact_fax', models.TextField()),
                ('contact_phone', models.TextField()),
                ('contact_email', models.TextField()),
                ('contact_address', models.CharField(max_length=300)),
                ('document_title', models.CharField(max_length=200)),
                ('document_content', models.TextField()),
                ('document_image', models.ImageField(upload_to='document/images')),
            ],
            options={
                'verbose_name': 'settings',
                'verbose_name_plural': 'settings',
            },
        ),
    ]
