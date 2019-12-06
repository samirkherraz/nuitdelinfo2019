from . import models
from nuitdelinfo.utils import Backend
from django.forms.models import model_to_dict


class DefaultView(Backend):
    def get(self):
        return list(models.Procedure.objects.all().values())


class DocumentView(Backend):
    def get(self):
        documents = models.ProcedureDocument.objects.filter(
            procedure=self.kwargs.get('id'))
        return [model_to_dict(o.document) for o in documents]


class ConstraintView(Backend):
    def get(self):
        constraints = models.Constraint.objects.filter(
            procedure=self.kwargs.get('id'))
        added = []
        res = []
        for o in constraints:
            if o.field not in added:
                res.append(model_to_dict(o, fields=["field", "type", "regex"]))
                added.append(o.field)
        return res

    def post(self):
        constraints = models.Constraint.objects.filter(
            procedure=self.kwargs.get('id'))
        access = True
        for e in constraints:
            if e.operator == "eq":
                if int(float(self.request.POST[e.field])) != int(float(e.controle)):
                    access = False
                    break
            elif e.operator == "ge":
                if int(float(self.request.POST[e.field])) < int(float(e.controle)):
                    access = False
                    break
            elif e.operator == "le":
                if int(float(self.request.POST[e.field])) > int(float(e.controle)):
                    access = False
                    break
        return access


class CategoryView(Backend):
    def get(self):
        return list(models.Category.objects.all().values())


class CategoryView(Backend):
    def get(self):
        return list(models.Category.objects.all().values())
