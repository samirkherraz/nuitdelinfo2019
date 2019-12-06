from . import models
import re
from nuitdelinfo.utils import Backend
class DefaultView(Backend):

    def put(self):
        message = self.request.PUT["message"].lower()
        for entity in models.Response.objects.all():
            match = re.match(entity.input, message)
            if match:
                res = re.sub(entity.input, entity.output, message)
                return res
        return "je n'ai pas bien compris ! "