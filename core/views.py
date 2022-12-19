from django.shortcuts import render,HttpResponse

# Create your views here.

def todos(request):
    return HttpResponse('<h1>')