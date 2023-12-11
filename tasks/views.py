from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tasks.serializers import TaskSerializer
from tasks.models import Task
from rest_framework.response import Response
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        return request.user == obj.owner
    
class TaksViewset(ModelViewSet):
    permission_classes = [IsOwner]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()




  
    