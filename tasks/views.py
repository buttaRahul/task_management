from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tasks.serializers import TaskSerializer
from tasks.models import Task
from rest_framework.response import Response
from rest_framework import permissions

class TaksViewset(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

  
    