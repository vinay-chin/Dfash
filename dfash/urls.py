from django.contrib import admin
from django.urls import path
from dfash import views

urlpatterns = [
    path('user', views.index, name="index"),
    path('started', views.started, name="index"),
]
