from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def myfunctioncall(request):
    return HttpResponse("Hello World")
def myfunctionabout(request):
    return HttpResponse("About Us")
def intro(request, name, age):
    mydictionary = {
        "name" : name,
        "age"  : age
    }
    return JsonResponse(mydictionary)
def myfirstpage(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

