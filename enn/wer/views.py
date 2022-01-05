from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import itemsserializers
from .models import items
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(viewsets.ModelViewSet):
    queryset = items.objects.all()
    serializer_class = itemsserializers
    permission_classes = [permissions.AllowAny]