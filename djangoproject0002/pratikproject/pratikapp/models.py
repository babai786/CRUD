from django.db import models


class Student(models.Model):
    sname=models.CharField(max_length=30)
    sno=models.IntegerField()
    smarks=models.FloatField()
