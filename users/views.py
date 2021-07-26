from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import MyUser
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = MyUser.objects.all()