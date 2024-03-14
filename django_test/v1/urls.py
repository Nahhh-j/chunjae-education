from django.urls import path
from v1 import views
from .views import *

app_name = 'v1'
urlpatterns = [
		path("create/", views.create),
        path("read/", views.read),
        path("read/<int:id>", views.read_id),
]