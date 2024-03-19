from django.urls import path
from articles import views
from .views import *

urlpatterns = [
    path("", views.article_list),
    path("<int:pk>/", views.article_detail),
    path("<int:pk>/comments/", views.comment_list),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
    path("<int:article_pk>/bookmarked_user/", views.bookmarked_user_list),
]