from django.urls import path
from accounts import views
from .views import *

urlpatterns = [
    path("register/", views.register),
    path("me/", views.me),
]