#coding:utf-8
from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Peopleinfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField(default=True)
    book=models.ForeignKey(Bookinfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
