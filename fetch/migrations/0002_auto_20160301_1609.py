# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetch', '0001_initial'),
    ]

    operations = [
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
            field=models.OneToOneField(primary_key=True, serialize=False, to='fetch.MasterUser'),
        ),
        migrations.AlterField(
            model_name='sharer',
            name='sharer_name',
            field=models.OneToOneField(primary_key=True, serialize=False, to='fetch.MasterUser'),
        ),
    ]
