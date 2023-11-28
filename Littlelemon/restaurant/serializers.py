from rest_framework import serializers
from .models import MenuTable, BookingTable



class MenuTableSerializer(serializers.ModelSerializer):
    class Meta:
        model= MenuTable
        fields = ['id', 'title', 'price', 'inventory']
                  

class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookingTable
        fields = ['id', 'name', 'noofguests', 'bookingdate']