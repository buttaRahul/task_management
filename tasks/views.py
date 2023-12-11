from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tasks.serializers import TaskSerializer
from tasks.models import Task
from rest_framework.response import Response
class ViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # def remove(self,request,pk):
    #     queryset = Task.objects.get(pk = pk)
    #     serializer = TaskSerializer(queryset)
    #     return Response(serializer.data)

    