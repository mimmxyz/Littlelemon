from rest_framework import serializers
from .models import MenuTable, BookingTable



class MenuTableSerializer(serializers.ModelSerializer):
    class Meta:
        model= MenuTable
        fields = ['title', 'price', 'inventory']
                  

class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookingTable
        fields = ['name', 'noofguests', 'bookingdate']