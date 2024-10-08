from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# myapp/views.py

from rest_framework import generics
from .models import Case
from .serializers import CaseSerializer


# List all cases or create a new case
class CaseListCreate(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


# Retrieve, update, or delete a case by ID
class CaseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
