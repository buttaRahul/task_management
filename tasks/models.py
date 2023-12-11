from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = {
        1 : "Pending",
        2 : "In Progress",
        3 : "Completed",
    }
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)  
    


    
