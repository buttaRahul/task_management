from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tasks.serializers import TaskSerializer
from tasks.models import Task
from rest_framework.response import Response
from rest_framework import permissions

 
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
    
    def has_permission(self, request, view):
        return request.user.is_authenticated 
    
class TaksViewset(ModelViewSet):
    permission_classes = [IsOwner]
    # permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()




  
    