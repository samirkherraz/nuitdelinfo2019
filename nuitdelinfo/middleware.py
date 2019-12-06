from django.http import QueryDict
from django.http.multipartparser import MultiValueDict
import json


class RESTMiddleware():

    def process_request(self,request):
        request.PUT=QueryDict('')
        request.DELETE = QueryDict('')
        method = request.META.get('REQUEST_METHOD','').upper()
        if method == 'PUT':
            self.handle_PUT(request)
        elif method == 'DELETE':
            self.handle_DELETE(request)
        return request

    def handle_DELETE(self,request):
        request.DELETE, request._files = self.parse_request(request)
    
    def handle_PUT(self,request):
        request.PUT,request._files  =   self.parse_request(request)
    
    def parse_request(self,request):
        if request.META.get('CONTENT_TYPE', '').startswith('multipart'):
            return self.parse_multipart(request)
        elif request.META.get('CONTENT_TYPE', '').startswith('application/json'):
            return (self.parse_json(request),MultiValueDict())
        else:
            return (self.parse_form(request), MultiValueDict())
    
    def parse_json(self,request):
        return json.loads(request.body)
     
    def parse_form(self,request):
        return QueryDict(request.body)
    
    def parse_multipart(self,request):
        return request.parse_file_upload(request.META,request)
    



def AppManager(get_response):

    def middleware(request):
        #module = resolve(request.path_info).url_name.split("-")[0]
        #request.CTX = Context(request.session,None)
        response = get_response(RESTMiddleware().process_request(request))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        #request.CTX.perssist()
        return response
    return middleware
