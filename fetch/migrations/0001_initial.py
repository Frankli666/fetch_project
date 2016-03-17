# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conStatus', models.BinaryField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Getter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MasterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('alt_email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=254)),
                ('profession', models.CharField(max_length=254)),
                ('address', models.TextField()),
                ('mobile', models.IntegerField()),
                ('landline', models.IntegerField()),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('nationality', models.CharField(max_length=254)),
                ('language', models.CharField(max_length=254)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sharer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sharer_name', models.OneToOneField(to='fetch.MasterUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='getter',
            name='getter_name',
            field=models.OneToOneField(to='fetch.MasterUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='connection',
            name='destUser',
            field=models.ForeignKey(to='fetch.Getter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='connection',
            name='sourceUser',
            field=models.ForeignKey(to='fetch.Sharer'),
            preserve_default=True,
        ),
    ]
