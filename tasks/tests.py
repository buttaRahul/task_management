from django.test import TestCase
from tasks.models import Task
from django.contrib.auth.models import User
from random import randint
from datetime import datetime,timedelta
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient
from tasks.serializers import TaskSerializer
from rest_framework import status


# Create your tests here.

num_words = ["","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN"]

class GetAllTasksTests(TestCase):

    client = APIClient()

    def setUp(self):
        pswd = make_password("abc123")
        user_schema = [
            {
                "username": "user1",
                "password" : pswd,
            },
            {
                "username": "user2",
                "password": pswd,
            }

        ]

        for user_data in user_schema:
           u =  User.objects.create(**user_data)
           Token.objects.create(user = u)


        users = User.objects.all()
        for i in range(1,11):
            rand_day = randint(1,4)
            dd = datetime.now() + timedelta(rand_day)
            task_data = {
                "title":f"task{i}",
                "description":f"This is task {num_words[i]}",
                "due_date": dd,
                "status" : 1,
                "owner": users[randint(0,1)]
                }
            Task.objects.create(**task_data)


    def test_get_all_tasks(self):
        url = "http://127.0.0.1:8000/tasks/"
        response = self.client.get(url)
        tasks = Task.objects.all()
        seraializer = TaskSerializer(tasks,many = True)

        self.assertEqual(response.data,seraializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
