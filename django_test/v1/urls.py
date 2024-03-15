from django.urls import path
from v1 import views
from .views import *

app_name = 'v1'
urlpatterns = [
    path("", views.v1_list),
]