from django.urls import path
from products import views
from .views import *

app_name = 'products'
urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
]