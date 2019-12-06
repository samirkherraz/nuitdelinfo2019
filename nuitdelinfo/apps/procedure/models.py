from django.conf import settings
from django.db import models
from nuitdelinfo.apps.filedrop.models import Category as DocumentCategory
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

class Procedure(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING) 

class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(DocumentCategory,on_delete=models.DO_NOTHING) 



class ProcedureDocument(models.Model):
    id = models.IntegerField(primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.DO_NOTHING) 
    procedure = models.ForeignKey(Procedure,on_delete=models.DO_NOTHING) 

class Condition(models.Model):
    id = models.IntegerField(primary_key=True)
    field = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    operator = models.CharField(max_length=32)
    controle = models.CharField(max_length=64, blank=True, null=True, default=None)
    document = models.ForeignKey(ProcedureDocument, on_delete=models.DO_NOTHING)


class Constraint(models.Model):
    id = models.IntegerField(primary_key=True)
    field = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    regex = models.CharField(max_length=64)
    operator = models.CharField(max_length=32)
    controle = models.CharField(max_length=64, blank=True, null=True, default=None)
    procedure = models.ForeignKey(Procedure,on_delete=models.DO_NOTHING) 
