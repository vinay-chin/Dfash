import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('dfash.urls')), 
]
