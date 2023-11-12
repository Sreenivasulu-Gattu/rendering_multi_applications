from django.urls import path
from mi.views import *

app_name = 'nothing'

urlpatterns  = [
    path('kishan/',kishan,name='kishan'),
    path('bumrah/',bumrah,name='bumrah'),
]