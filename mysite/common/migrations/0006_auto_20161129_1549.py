# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20161127_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computerroomstatus',
            old_name='entrytime',
            new_name='option_time',
        ),
        migrations.RemoveField(
            model_name='computerroomstatus',
            name='outtime',
        ),
        migrations.RemoveField(
            model_name='personinfo',
            name='entrytime',
        ),
        migrations.AddField(
            model_name='computerroomstatus',
            name='status',
            field=models.BooleanField(default=True, db_column=b'Status'),
        ),
        migrations.AlterField(
            model_name='computerroom',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='computerroomstatus',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
