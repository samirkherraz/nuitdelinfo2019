
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

class Backend:
    __DEPS__ = []

    def __init__(self, request=None, ctx=None):
        self.request = request
        self.CTX = ctx

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def load(self):
        pass

    def __call__(self, request):
        inst = self.__new__(self.__class__)
        inst.__init__(request)
        data = None
        if request.method == 'GET':
            data = inst.get()
        if request.method == 'POST':
            data = inst.post()
        if request.method == 'DELETE':
            data = inst.delete()
        if request.method == 'PUT':
            data = inst.put()
        if data is not None:
            return JsonResponse({
                "content": data
            })
        else:
            return JsonResponse({
                "content": True
            })
