from django.shortcuts import render
from .serializers import DepartmentSerializer
from rest_framework import generics
from .models import Department, Personnel


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
