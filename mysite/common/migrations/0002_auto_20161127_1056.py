# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ComputerRoomStattus',
            new_name='ComputerRoomStatus',
        ),
        migrations.AlterModelTable(
            name='computerroomstatus',
            table='ComputerRoomStatus',
        ),
    ]
