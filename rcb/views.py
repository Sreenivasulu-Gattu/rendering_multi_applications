from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def kohli(request):
    return render(request,'kohli.html')