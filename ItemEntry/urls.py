
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('get_data', views.get_data),
]
