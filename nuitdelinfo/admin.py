from django.contrib import admin
from nuitdelinfo.models import *
from nuitdelinfo.apps.filedrop import models as filedrop_models
from nuitdelinfo.apps.chat import models as chat_models

admin.site.register(filedrop_models.Document)
admin.site.register(chat_models.Response)