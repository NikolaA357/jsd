import os
from django.db import models


class Country(models.Model):	
	Id = models.CharField(max_length=3),
	Name = models.CharField(max_length=20),
	Zip_Code = models.CharField(max_length=12),
class Cars(models.Model):	
	Country = models.ForeignKey(Country, on_delete=models.CASCADE)
	Mark = models.CharField(max_length=20),
	Type = models.CharField(max_length=20),
	Models = models.CharField(max_length=20),
	Used = models.
	Description = models.
	Price = models.ForeignKey(Price, on_delete=models.CASCADE)
	Email = models.EmailField(max_length=30),
	Color = models.CharField(max_length=20),
	EnginePower = models.ForeignKey(EnginePower, on_delete=models.CASCADE)
class Price(models.Model):	
	Models = models.ForeignKey(Models, on_delete=models.CASCADE)
	price = models.
	D_of_Pr = models.
class EnginePower(models.Model):	
	Power = models.
	Capacity = models.
	Torque = models.