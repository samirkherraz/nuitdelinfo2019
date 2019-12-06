from django.conf import settings
from django.db import models
class Response(models.Model):
    id = models.IntegerField(primary_key=True)
    input = models.CharField(max_length=255)
    output = models.CharField(max_length=255)
