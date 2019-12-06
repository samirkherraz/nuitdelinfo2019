
from django.http import JsonResponse
from django.http import QueryDict
def to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]
class Backend:
    __DEPS__ = []

    def __init__(self, request=None, **kwargs):
        self.request = request
        self.kwargs = kwargs
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

    def __call__(self, request, **kwargs):
        inst = self.__new__(self.__class__)
        inst.__init__(request, **kwargs)
        data = None
        try:
            if request.method == 'GET':
                data = inst.get()
            if request.method == 'POST':
                data = inst.post()
            if request.method == 'DELETE':
                data = inst.delete()
            if request.method == 'PUT':
                data = inst.put()
        
        except ValueError as e: 
            return JsonResponse({
                "status": 1,
                "content": str(e)
            })

        if data is not None:
            return JsonResponse({
                "status": 0,
                "content": data
            })
        else:
            return JsonResponse({
                "status": 0,
                "content": True
            })
