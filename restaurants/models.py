from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	opening_time = models.TimeField()
	closing_time = models.TimeField()