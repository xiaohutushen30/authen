from django.db import models
import django.utils.timezone as timezone

class Personinfo(models.Model):
    id = models.AutoField(primary_key=True)
    personnumber = models.CharField(max_length=64, db_column='personnumber', blank=True)
    name = models.CharField(max_length=64, db_column='Name', blank=True)
    sex = models.CharField(max_length=64, db_column='Sex', blank=True)
    class Meta:
        db_table = 'PersonInfo'

class ComputerRoom(models.Model):
    id = models.AutoField(primary_key=True)
    roomnumber = models.CharField(max_length=64, db_column='roomnumber', blank=True)
    name = models.CharField(max_length=64, db_column='Name', blank=True)
    class Meta:
        db_table = 'ComputerRoom'

class ComputerRoomStatus(models.Model):
    id = models.AutoField(primary_key=True)
    computerroomid = models.BigIntegerField(null=True, db_column='ComputerRoomId', blank=True)
    personid = models.BigIntegerField(null=True, db_column='PersonId', blank=True)
    status = models.BooleanField(default=True, db_column='Status', blank=True)
    optiontime = models.DateTimeField(null=True, db_column='OptionTime', blank=True)
    class Meta:
        db_table = 'ComputerRoomStatus'
