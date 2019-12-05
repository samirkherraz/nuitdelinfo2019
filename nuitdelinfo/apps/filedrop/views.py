from . import models
from nuitdelinfo.utils import Backend

class DocumentCategoryView(Backend):
    
    def get(self):
        return list(models.DocumentCategory.objects.all().values())

    
    
class DocumentView(Backend):
    
    def get(self):
        return list(models.Document.objects.all().values())

    
    