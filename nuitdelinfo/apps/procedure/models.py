from django.conf import settings
from django.db import models

class ProcedureCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)


class ProcedureDocuments(models.Model):
    id = models.IntegerField(primary_key=True)


class Procedure(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(ProcedureCategory,on_delete=models.DO_NOTHING) 
