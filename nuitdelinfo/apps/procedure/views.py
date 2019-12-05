from . import models
from nuitdelinfo.utils import Backend
class DefaultView(Backend):
    def get(self):
        return list(models.Procedure.objects.all().values())


class DocumentView(Backend):
    def get(self):
        return list(models.Document.objects.all().values())


class CategoryView(Backend):
    def get(self):
        return list(models.Category.objects.all().values())
