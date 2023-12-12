from django.test import TestCase
from rest_framework.test import APITestCase
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

# class GetAllTasksTests(TestCase):

#     client = APIClient()

#     def setUp(self):
#         pswd = make_password("abc123")
#         user_schema = [
#             {
#                 "username": "user1",
#                 "password" : pswd,
#             },
#             {
#                 "username": "user2",
#                 "password": pswd,
#             }

#         ]

#         for user_data in user_schema:
#            u =  User.objects.create(**user_data)
#            Token.objects.create(user = u)


#         users = User.objects.all()
#         for i in range(1,11):
#             rand_day = randint(1,4)
#             dd = datetime.now() + timedelta(rand_day)
#             task_data = {
#                 "title":f"task{i}",
#                 "description":f"This is task {num_words[i]}",
#                 "due_date": dd,
#                 "status" : 1,
#                 "owner": users[randint(0,1)]
#                 }
#             Task.objects.create(**task_data)

#         self.token = Token.objects.first()


#     def test_get_all_tasks(self):
#         url = "http://127.0.0.1:8000/tasks/"
#         # self.tokens
#         headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
#         response = self.client.get(url,**headers)
#         tasks = Task.objects.all()
#         seraializer = TaskSerializer(tasks,many = True)

#         self.assertEqual(response.data,seraializer.data)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)

# class CreateNewTaskTests(TestCase):
#     client = APIClient()


#     def setUp(self):
#         pswd = make_password("abc123")
#         user_schema = [
#             {
#                 "username": "user1",
#                 "password" : pswd,
#             },
#             {
#                 "username": "user2",
#                 "password": pswd,
#             }

#         ]

#         for user_data in user_schema:
#            u =  User.objects.create(**user_data)
#            Token.objects.create(user = u)

#         self.token = Token.objects.all()[0]


#     def test_post_valid_task(self):
#         url = "http://127.0.0.1:8000/tasks/"
#         data = {
#             "title" : "task99",
#             "description": "This is task 99",
#             "due_date" : "2023-12-13",
#             "status": 1,
#             "owner" : User.objects.first().id,
#         }
#         headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
#         response = self.client.post(url,data=data,format = 'json',**headers)

#         self.assertEqual(response.status_code,status.HTTP_201_CREATED)



# class DeleteTaskTest(TestCase):

#     client = APIClient()

#     def setUp(self):
#         pswd = make_password("abc123")
#         user_schema = [
#             {
#                 "username": "user1",
#                 "password" : pswd,
#             },
#             {
#                 "username": "user2",
#                 "password": pswd,
#             }
#         ]

#         for user_data in user_schema:
#             u = User.objects.create(**user_data)
#             Token.objects.create(user=u)

#         self.token = Token.objects.all()[0]

#         self.task_content = {
#             "title": "task100",
#             "description": "This is task hundred",
#             "due_date": "2023-12-13",
#             "status": 1,
#             "owner": User.objects.first()
#         }
#         self.task = Task.objects.create(**self.task_content)

#     def test_delete_task(self):
#         url = f"http://127.0.0.1:8000/tasks/{self.task.id}/"
#         headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
#         response = self.client.delete(url, **headers)
#         print("IN TEST DELETE TASK")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



# class RetrieveSingleTaskTest(TestCase):

#     client = APIClient()

#     def setUp(self):
#         pswd = make_password("abc123")
#         user_schema = [
#             {
#                 "username": "user1",
#                 "password" : pswd,
#             },
#             {
#                 "username": "user2",
#                 "password": pswd,
#             }
#         ]

#         for user_data in user_schema:
#             u = User.objects.create(**user_data)
#             Token.objects.create(user=u)

#         self.token = Token.objects.all()[0]

#         self.task_content = {
#             "title": "task100",
#             "description": "This is task hundred",
#             "due_date": "2023-12-13",
#             "status": 1,
#             "owner": User.objects.first()
#         }
#         self.task = Task.objects.create(**self.task_content)

#     def test_retrieve_task(self):
#         url = f"http://127.0.0.1:8000/tasks/{self.task.id}/"
#         headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
#         response = self.client.get(url, **headers)
#         print("IN RETREIVE SINGLE TASK")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTaskTest(APITestCase):
    client = APIClient()

    def setUp(self):
        pswd = make_password("abc@123")

        self.user = User.objects.create(username = "user1",password = pswd)
        
        self.token = Token.objects.create(user = self.user)

        self.task = Task.objects.create(title = "task100",description = "This is task Hundred", due_date = "2023-12-13",status = 1, owner = self.user)

    
    def test_put_task(self):

        test_data = {
            "title" : "task101",
            "description": "This is task Hundred",
            "due_date": "2023-12-13",
            "status": 1,
            "owner" : self.user.id,

        }

        url = f"http://127.0.0.1:8000/tasks/{self.task.id}/"
        print(url)
        headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'} 
        response = self.client.put(url,data=test_data,**headers)
        print("IN PUT TASK")
        self.assertEqual(response.status_code,status.HTTP_200_OK)







      

# python manage.py test -v 2



        
