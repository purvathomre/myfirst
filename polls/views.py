from django.http import HttpResponse


def index(request):
    return HttpResponse("<b>Hello,polls!..</b>")
def hello(b):
    return HttpResponse("<b>Hello, world!..</b>")    
