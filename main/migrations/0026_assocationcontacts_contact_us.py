# Generated by Django 2.2.15 on 2020-09-07 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20200905_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssocationContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.TextField()),
                ('fax', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_ts', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'associations contact',
                'verbose_name_plural': 'associations contacts',
            },
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
