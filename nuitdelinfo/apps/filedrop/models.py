from django.conf import settings
from django.db import models


class DocumentCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=64)

class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    file = models.FileField()
    category = models.ForeignKey(DocumentCategory,on_delete=models.DO_NOTHING) 

