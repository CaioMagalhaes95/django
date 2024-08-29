from django.shortcuts import render
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import TaskSerializer
from .filters import TaskFilter

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter