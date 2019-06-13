from django.http import HttpResponse

class MyException(object):
    '''自定义中间件类'''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self,request, exception):
        return HttpResponse(exception)