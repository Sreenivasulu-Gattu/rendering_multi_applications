from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kishan(request):
    return render(request,'kishan.html')

def bumrah(request):
    return HttpResponse('<h1>Hello, This is Bumrah..</h1>')