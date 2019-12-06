from . import models
from nuitdelinfo.utils import Backend, to_list

from django.forms.models import model_to_dict

class CategoryView(Backend):
    def get(self):
        return list(models.Category.objects.all().values())

class DefaultView(Backend):
    
    def get(self):
        return list(models.Location.objects.all().values())
