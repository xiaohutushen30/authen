# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20161129_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computerroomstatus',
            name='option_time',
        ),
        migrations.AddField(
            model_name='computerroomstatus',
            name='optiontime',
            field=models.DateTimeField(null=True, db_column=b'OptionTime', blank=True),
        ),
    ]
