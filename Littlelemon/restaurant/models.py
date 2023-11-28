from django.db import models

# Create your models here.
class BookingTable(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    noofguests = models.IntegerField() #max_length=6)
    bookingdate = models.DateTimeField()

    def __str__(self): 
        return self.name

from django.db import models

class MenuTable(models.Model):

    id = models.IntegerField(primary_key=True) #, max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField() #max_length=5)
    
    def __str__(self): 
        return self.title
