# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerRoom',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('roomnumber', models.CharField(max_length=64, db_column=b'roomnumber', blank=True)),
                ('name', models.CharField(max_length=64, db_column=b'Name', blank=True)),
            ],
            options={
                'db_table': 'ComputerRoom',
            },
        ),
        migrations.CreateModel(
            name='ComputerRoomStattus',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('computerroomid', models.BigIntegerField(null=True, db_column=b'ComputerRoomId', blank=True)),
                ('personid', models.BigIntegerField(null=True, db_column=b'PersonId', blank=True)),
                ('entrytime', models.DateTimeField(null=True, db_column=b'EntryTime', blank=True)),
                ('outtime', models.DateTimeField(null=True, db_column=b'OutTime', blank=True)),
            ],
            options={
                'db_table': 'ComputerRoomStattus',
            },
        ),
        migrations.CreateModel(
            name='Personinfo',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('personnumber', models.CharField(max_length=64, db_column=b'personnumber', blank=True)),
                ('name', models.CharField(max_length=64, db_column=b'Name', blank=True)),
                ('sex', models.CharField(max_length=64, db_column=b'Sex', blank=True)),
                ('entrytime', models.DateTimeField(null=True, db_column=b'EntryTime', blank=True)),
            ],
            options={
                'db_table': 'PersonInfo',
            },
        ),
    ]
