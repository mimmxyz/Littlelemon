from django.contrib import admin 
from django.urls import path 
from . import views  
from .views import  Booking, Menu
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'menu', Menu, basename='menu-items')
router.register(r'booking', Booking, basename='booking')
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

urlpatterns += router.urls