from django.conf import settings
from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=64)


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    x =  models.IntegerField()
    y =  models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING) 

