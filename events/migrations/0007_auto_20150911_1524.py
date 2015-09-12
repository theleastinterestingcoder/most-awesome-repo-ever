# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import events.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150910_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='guests',
        ),
        migrations.AddField(
            model_name='entry',
            name='guest',
            field=models.CharField(default='', max_length=1000, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 19, 24, 51, 28729, tzinfo=utc), verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(validators=[events.models.validate_image], upload_to=b'event_images/', blank=True, help_text=b'To be displayed on the website. (Optional).', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 19, 24, 51, 28729, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 19, 24, 51, 28729, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 19, 24, 51, 28729, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 19, 24, 51, 28729, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 19, 24, 51, 28729, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
