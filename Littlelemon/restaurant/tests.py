from multiprocessing.connection import Client
from django.test import TestCase
from .models import MenuTable
from .views import Menu
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from .serializers import MenuTableSerializer
import json
from rest_framework import status


class MenuTableTest(TestCase):
   
    def setUp(self):
        zucchina = MenuTable.objects.create(id = 1, title="zucchina", price=80.00, inventory=100)
        albicocca = MenuTable.objects.create(id = 2, title="albicocca", price="0.01", inventory=1000)
    
    def test_string_method(self):   
        item = MenuTable.objects.get(title = "zucchina")
        itemstr = item.__str__()
        self.assertEqual(itemstr, "zucchina")

    def test_item_price(self):
        albicocca = MenuTable.objects.get(title="albicocca")
        self.assertEqual(float(albicocca.price), 0.01)
        
class YourModelAPITest(APITestCase):
    def setUp(self):
        zucchina = MenuTable.objects.create(id = 1, title="zucchina", price=80.00, inventory=100)
        albicocca = MenuTable.objects.create(id = 2, title="albicocca", price="0.01", inventory=1000)
        self.c = APIRequestFactory()
        self.user =User.objects.create_user(username='testuser', password='123')
        
        
    def test_list_objects(self):
        
        self.view = Menu.as_view({'get': 'list'})
        request = self.c.get('/restaurant/menu/')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #check if the response content is correctly serialized and if is equal to the expected JSON    
    def test_serialized_response(self):
        self.view = Menu.as_view({'get': 'list'})
        request = self.c.get('/restaurant/menu/')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        expected =  """[{"id":1,"title":"zucchina","price":"80.00","inventory":100},{"id":2,"title":"albicocca","price":"0.01","inventory":1000}]"""
        #expectedjson = json.dumps(expected)
        receivedjson = response.rendered_content.decode()
        self.assertEqual(expected, receivedjson)
        
    def test_create_objects(self):
        
        self.view = Menu.as_view({'post': 'create'})
        request = self.c.post('/restaurant/menu/', {
                                                    "id" : 100,
                                                    "title" : "pollo",
                                                    "price" : 90.01,
                                                    "inventory" : 10
                                                    }, 
                                                    format = "json")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    
