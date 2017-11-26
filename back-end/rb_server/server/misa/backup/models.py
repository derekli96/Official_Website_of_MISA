from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    phone=models.CharField(max_length=15)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 200)
    gender=models.CharField(max_length=2)
    photoID=models.CharField(max_length=200)
    signature=models.CharField(max_length=1024)
    score=models.IntegerField(default=0)
    credit=models.FloatField(default=1)
    localPermission=models.CharField(max_length=2)
    logoninLongitude=models.FloatField(default=0)
    logoninLatitude=models.FloatField(default=0)
 
    
class AppointmentRun(models.Model):
    phone=models.CharField(max_length=15)
    username = models.CharField(max_length = 100)
    topic=models.CharField(max_length=1000)
    description=models.CharField(max_length=3000)
    due=models.NullBooleanField()
    beginTime = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)
    length=models.FloatField()
    place=models.CharField(max_length=1024)
    
   
class AppointmentToMe(models.Model):
    phone=models.CharField(max_length=15)
    topic=models.CharField(max_length=1000)
    description=models.CharField(max_length=3000)
    #acceptPeopleId=models.IntegerField(default=0)
    due=models.NullBooleanField()
    beginTime = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)
    length=models.FloatField()
    place=models.CharField(max_length=1024)

class AppointmentByMe(models.Model):
    phone=models.CharField(max_length=15)
    topic=models.CharField(max_length=1000)
    description=models.CharField(max_length=3000)
    due=models.NullBooleanField()
    beginTime = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)
    length=models.FloatField()
    place=models.CharField(max_length=1024)
    

class AppointmentToDo(models.Model):
    phone=models.CharField(max_length=15)
    topic=models.CharField(max_length=1000)
    description=models.CharField(max_length=3000)
    due=models.NullBooleanField()
    beginTime = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)
    length=models.FloatField()
    place=models.CharField(max_length=1024)

    
class MyRun(models.Model):
    phone=models.CharField(max_length=15)
    beginTime = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)
    length=models.FloatField()
    timeLength=models.FloatField()
    averageVelocity=models.FloatField(default=0)
    place=models.CharField(max_length=1024)
    
class Friendship(models.Model):
    friendshiptoken=models.NullBooleanField()
    sendphone=models.CharField(max_length=15)
    sendusername=models.CharField(max_length = 100)
    acceptphone=models.CharField(max_length=15)
    acceptusername=models.CharField(max_length=100)


class RunningTips(models.Model):
    tipsID=models.IntegerField(max_length=10)
    tipsName=models.CharField(max_length=1024)
    tipsDetail=models.CharField(max_length=3000)

    
class CompetitionInfo(models.Model):
    infoID=models.IntegerField(max_length=10)
    infoName=models.CharField(max_length=1024)
    infoDetail=models.CharField(max_length=3000)
