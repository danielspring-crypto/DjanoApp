from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('novels/', views.novels, name='novels'),
    path('news/', views.news, name='news'),
]