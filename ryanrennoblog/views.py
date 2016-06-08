from django.http import HttpResponse 
# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Ryan Renno</title></html>') 
