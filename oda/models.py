from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

class Wraptype(models.Model):
	wrap_type=models.CharField(max_length=20)
	price=models.IntegerField()
	def __str__(self):
		return self.wrap_type

class Brand(models.Model):
	manager=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	wrap_type=models.ForeignKey('Wraptype',on_delete=models.PROTECT)
	name=models.CharField(max_length=50)
	no_of_cars=models.IntegerField()
	region=models.CharField(max_length=50)
	duration=models.IntegerField()
	start_date=models.DateField()
	def __str__(self):
		return self.name

class Car_model(models.Model):
	car_model=models.CharField(max_length=20) 
	def __str__(self):
		return self.car_model

class Driver(models.Model):
	driver_name=models.CharField(max_length=50)
	car_model=models.ForeignKey('Car_model',on_delete=models.PROTECT)
	brand=models.ForeignKey('Brand',on_delete=models.PROTECT)
	car_no=models.CharField(max_length=20)
	phone_no=PhoneNumberField(null=False,blank=False)
	def __str__(self):
		return self.driver_name
# Create your models here.
class Pos_data(models.Model):
	brand=models.ForeignKey('Brand',null=True,on_delete=models.SET_NULL)
	driver=models.ForeignKey('Driver',null=True,on_delete=models.SET_NULL)
	latpos=models.FloatField()
	lonpos=models.FloatField()
