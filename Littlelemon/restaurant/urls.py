from django.contrib import admin 
from django.urls import path 
from . import views 
  
  
from .views import  Menu
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', Menu, basename='menu-items')
urlpatterns = [ 
    path('', views.index, name='index'), 
]

urlpatterns += router.urls