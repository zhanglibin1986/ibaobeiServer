from django.http import HttpResponse  # Create your views here.


def index(request):
    return HttpResponse("Hello world. You are now run the ibaobeiServer, this is index")
