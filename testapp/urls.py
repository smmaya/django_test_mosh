from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('page1/', views.page1),
    path('page2/', views.page2),
    path('hello/', views.say_hello),
]