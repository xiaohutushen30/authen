# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20161129_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerroom',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='computerroomstatus',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
