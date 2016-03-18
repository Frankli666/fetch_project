# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0002_remove_action_data'),
        ('fetch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('user', models.ForeignKey(primary_key=True, serialize=False, to='fetch.MasterUser')),
                ('is_read', models.BooleanField(default=False)),
                ('action', models.ForeignKey(default=b'', to='actstream.Action')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='getter',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sharer',
            name='id',
        ),
        migrations.AlterField(
            model_name='getter',
            name='getter_name',
            field=models.ForeignKey(related_name=b'getter', primary_key=True, serialize=False, to='fetch.MasterUser'),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='address',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='alt_email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='city',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='country',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='landline',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='language',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='nationality',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='profession',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='state',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='masteruser',
            name='user',
            field=models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sharer',
            name='sharer_name',
            field=models.ForeignKey(related_name=b'sharer', primary_key=True, serialize=False, to='fetch.MasterUser'),
        ),
    ]
