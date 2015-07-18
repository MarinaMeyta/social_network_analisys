# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('tweet_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tweet_text', models.CharField(max_length=140)),
                ('hashtags', models.TextField()),
                ('created_at', models.TextField()),
                ('user_name', models.TextField()),
                ('lang', models.TextField()),
                ('time_zone', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
    ]
