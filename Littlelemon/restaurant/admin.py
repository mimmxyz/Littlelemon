from django.contrib import admin

from .models import MenuTable, BookingTable


admin.site.register(MenuTable)
admin.site.register(BookingTable)