from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response 


class allProducts(generics.ListAPIView):
    queryset=productModel.objects.all()
    serializer_class=productSerializer


class allView(generics.RetrieveUpdateDestroyAPIView,generics.CreateAPIView):
    queryset=productModel.objects.all()
    serializer_class=productSerializer