
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    url(r'^hello/', views.hello),
    url(r'^home/', views.home),
]
