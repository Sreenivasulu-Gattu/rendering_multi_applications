from rcb.views import *
from django.urls import path

app_name = 'something'

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
]