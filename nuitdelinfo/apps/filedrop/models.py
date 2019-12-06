from django.conf import settings
from django.db import models
from django.http import FileResponse

import os.path
import mimetypes
mimetypes.init()

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=64)

   
class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=64)
    #category = models.ForeignKey(Category,on_delete=models.DO_NOTHING) 
    def get_file(self):
        fsock =  open(self.path, 'rb')
        file_name = os.path.basename(self.path)
        mime_type_guess = mimetypes.guess_type(file_name)
        if mime_type_guess is not None:
            response = FileResponse(fsock, content_type=mime_type_guess[0])
            response['Content-Disposition'] = 'attachment; filename=' + file_name
            return response
        else:
            return None
            
    def save_file(self, f):
        self.path = f'{settings.BASE_DIR}/uploads/{self.name}-{f}'
        with open(self.path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

