from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Obj1Cmn(models.Model):
    idobj = models.IntegerField(verbose_name='id объекта')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField()
    data = models.CharField(max_length=19)
    mode = models.FloatField()
    ai1 = models.FloatField()
    ai2 = models.FloatField()
    ai3 = models.FloatField()
    ai4 = models.FloatField()
    ai5 = models.FloatField()
    ai6 = models.FloatField()
    ai7 = models.FloatField()
    ai8 = models.FloatField()
    ai9 = models.FloatField()
    ai10 = models.FloatField()

class Obj2Cmn(models.Model):
    idobj = models.IntegerField(verbose_name='id объекта')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField()
    data = models.CharField(max_length=19)
    mode = models.FloatField()
    ai1 = models.FloatField()
    ai2 = models.FloatField()
    ai3 = models.FloatField()
    ai4 = models.FloatField()
    ai5 = models.FloatField()
    ai6 = models.FloatField()
    ai7 = models.FloatField()
    ai8 = models.FloatField()
    ai9 = models.FloatField()
    ai10 = models.FloatField()

class Obj1Ai(models.Model):
    idobj = models.IntegerField()
    idai = models.IntegerField()
    datain = models.CharField(max_length=19)
    mode = models.FloatField()
    aimax = models.FloatField()
    aimean = models.FloatField()
    aimin = models.FloatField()
    statmin = models.FloatField()
    statmax = models.FloatField()
    mlmin = models.FloatField()
    mlmax = models.FloatField()
    err = models.IntegerField()
    sts = models.IntegerField()
    dataout = models.CharField(max_length=19)
    datacheck = models.CharField(max_length=19)
    cmnt = models.CharField(max_length=50)

    def __str__(self):
        return self.datain

class Obj2Ai(models.Model):
    idobj = models.IntegerField()
    idai = models.IntegerField()
    datain = models.CharField(max_length=19)
    mode = models.FloatField()
    aimax = models.FloatField()
    aimean = models.FloatField()
    aimin = models.FloatField()
    statmin = models.FloatField()
    statmax = models.FloatField()
    mlmin = models.FloatField()
    mlmax = models.FloatField()
    err = models.IntegerField()
    sts = models.IntegerField()
    dataout = models.CharField(max_length=19)
    datacheck = models.CharField(max_length=19)
    cmnt = models.CharField(max_length=50)

    def __str__(self):
        return self.datain
