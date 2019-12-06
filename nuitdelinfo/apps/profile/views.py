from . import models
from nuitdelinfo.utils import Backend
from django.forms.models import model_to_dict

class DefaultView(Backend):
    def get(self):
        return list(models.Profile.objects.all().values())

class ProfileView(Backend):
    def get(self):
        profile = models.Profile.objects.filter(
            id=self.kwargs.get('id'))
        if (len(profile) == 1):
            return model_to_dict(profile[0])
        else:
            return {}