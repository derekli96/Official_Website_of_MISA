from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Member(models.Model):
	password = models.CharField(max_length=200)
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=300)
	email = models.CharField(max_length=300)

class Courserecord(models.Model):
	cID = models.CharField(max_length=100)
	cName = models.CharField(max_length=100)
	uploadername = models.CharField(max_length=300)
	uploadTime = models.CharField(max_length=100)
	clickTime = models.IntegerField(default=0)
	fileAddress = models.CharField(max_length=300)

class News(models.Model):
	topic = models.CharField(max_length=100)
	nName = models.CharField(max_length=300)
	createTime = models.TimeField()
	activityTime = models.TimeField()
	Location = models.CharField(max_length=200)
	signURL = models.URLField()

class Discussion(models.Model):
	topic = models.CharField(max_length=100)
	postId = models.ForeignKey(Member)
	discussTime = models.TimeField()
	content = models.TextField()
