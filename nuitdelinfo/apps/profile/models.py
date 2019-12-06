from django.conf import settings
from django.db import models

class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthdate = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    primary_phone = models.CharField(max_length=32)
    secondary_phone = models.CharField(max_length=32)