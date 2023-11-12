from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def rohit(request):
    return HttpResponse('<h1>Here is the Rohit sharma ..</h1>')