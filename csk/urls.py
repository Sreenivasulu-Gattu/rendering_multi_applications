#import functions from csk->views 
from csk.views import * 

#import path from django.urls
from django.urls import path

app_name='anything'

urlpatterns = [
    path('msd/',msd,name='msd'),
    path('rohit/',rohit,name='rohit')
]