# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=255)),
                ('url', models.URLField(help_text=b'(Optional) - Link to a blog post with more information', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_start', models.DateTimeField(db_index=True)),
                ('date_end', models.DateTimeField(db_index=True, null=True, blank=True)),
            ],
        ),
    ]
