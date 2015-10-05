# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20151005_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 5, 5, 54, 512028, tzinfo=utc), verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 5, 5, 54, 512028, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 5, 5, 54, 512028, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 5, 5, 54, 512028, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 5, 5, 54, 512028, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 5, 5, 54, 512028, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
