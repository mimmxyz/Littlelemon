from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# #from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .serializers import *
#from rest_framework import generics
from .models import *
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User, Group
# from django.shortcuts import get_object_or_404
from rest_framework import viewsets
# from LittleLemon.permissions import IsManager, IsDelivery, IsManagerOrDelivery
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from datetime import date
# from .throttles import CustomThrottleMixin, ManagerThrottle, DeliveryThrottle, CustomerThrottle







def index(request):
    return render(request, 'index.html', {})

#allow CRUD operation on MenuTabel
class Menu(viewsets.ModelViewSet):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # filterset_fields = []
    # ordering_fields = []
    # search_fields=[]
    
class Booking(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]