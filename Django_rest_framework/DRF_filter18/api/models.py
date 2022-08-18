from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    roll = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    passby = models.CharField(max_length=50, null=True)
