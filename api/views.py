# api/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Sandwich,Topping
from .serializers import SandwichSerializer, SandwichDetailSerializer, ToppingSerializer, SandwichToppingSerializer

class SandwichList(generics.ListCreateAPIView):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer


class SandwichDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichDetailSerializer


class ToppingList(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class ToppingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class SandwichToppingDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Sandwich.objects.all()
     serializer_class = SandwichToppingSerializer




