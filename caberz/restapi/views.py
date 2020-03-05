from django.shortcuts import render
from .serializers import UserSerializer
# Create your views here.
from rest_framework import generics
from accounts.models import Profiles

class restapiview(generics.RetrieveUpdateDestroyAPIView):
    lookup_field ='id'
    serializer_class = UserSerializer
    def get_queryset(self):
        return Profiles.objects.all()
