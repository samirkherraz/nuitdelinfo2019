from django.conf import settings
from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=64)

   
class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    #category = models.ForeignKey(Category,on_delete=models.DO_NOTHING) 

    def save_file(self, f):
        with open(f'{settings.BASE_DIR}/uploads/{self.name}-{f}', 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

