from django.urls import path
from .views import *

app_name = 'v2'
urlpatterns = [
    path('', index, name='index'),
]