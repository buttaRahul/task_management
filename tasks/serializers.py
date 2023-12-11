from rest_framework.serializers import ModelSerializer
from tasks.models import Task


class TaskSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Task

        