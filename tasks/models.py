from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = {
        1 : "Pending",
        2 : "In Progress",
        3 : "Completed",
    }
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)  
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
