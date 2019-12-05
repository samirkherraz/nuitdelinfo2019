from . import models
from nuitdelinfo.utils import Backend
from django.forms.models import model_to_dict
class DocumentView(Backend):
    
    def get(self):
        return model_to_dict(models.Document.objects.get(pk=self.kwargs.get("id")))



class CategoryView(Backend):
    
    def get(self):
        return list(models.Category.objects.all().values())

  
    
class DefaultView(Backend):
    
    def get(self):
        return list(models.Document.objects.all().values())

    def put(self):
        doc =  models.Document()
        doc.name = self.request.PUT['name']
        #doc.category = models.Category.objects.get(self.request.PUT['category'])
        doc.save_file(self.request.FILES['file'])
        doc.save()
    