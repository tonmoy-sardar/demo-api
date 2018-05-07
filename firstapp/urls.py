from django.contrib import admin
from django.urls import path
from rest_framework import routers
from firstapp import views
from django.conf.urls import url, include
from .views import CustomObtainAuthToken



urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', CustomObtainAuthToken.as_view()),

]
