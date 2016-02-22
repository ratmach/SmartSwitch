from django.db import models

# Create your models here.
class user(models.Model):
	UID = models.CharField(max_length = 32, primary_key=True)
	username = models.CharField(max_length = 32, unique=True)
	password = models.CharField(max_length = 32)
	type = models.IntegerField()

class points(models.Model):
	name = models.CharField(max_length = 50)
	watt = models.FloatField()
	pID = models.IntegerField(primary_key=True)
	icon = models.CharField(max_length = 64)
	state = models.BooleanField()
	type = models.IntegerField()
	
class log(models.Model):
	username = models.CharField(max_length = 32)
	date = models.DateTimeField()
	lID = models.AutoField(primary_key=True)
	state = models.BooleanField()