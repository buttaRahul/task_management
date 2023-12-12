from rest_framework.serializers import ModelSerializer
from tasks.models import Task
from datetime import datetime
from rest_framework import serializers
class TaskSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Task

    # def validate_due_date(self, value):
    #     current_datetime = datetime.now()
    #     print("VALUE",value)
    #     print("CURRENT",current_datetime)
    #     # if value <= current_datetime:
    #     #     raise serializers.ValidationError("Due date must be greater than the current date and time.")

    #     return value

