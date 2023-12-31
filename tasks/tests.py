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

        self.token = Token.objects.first()


    def test_get_all_tasks(self):
        print("TEST CASE FOR LIST ACTION")
        url = "http://127.0.0.1:8000/tasks/"
        # self.tokens
        headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
        response = self.client.get(url,**headers)
        tasks = Task.objects.all()
        seraializer = TaskSerializer(tasks,many = True)

        self.assertEqual(response.data,seraializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class CreateNewTaskTests(TestCase):
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

        self.token = Token.objects.all()[0]


    def test_post_valid_task(self):
        print("TEST CASE FOR POST ACTION")

        url = "http://127.0.0.1:8000/tasks/"
        data = {
            "title" : "task99",
            "description": "This is task 99",
            "due_date" : "2023-12-13",
            "status": 1,
            "owner" : User.objects.first().id,
        }
        headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
        response = self.client.post(url,data=data,format = 'json',**headers)
        self.assertEqual(response.data['title'],data['title'])
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)



class DeleteTaskTest(TestCase):

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
            u = User.objects.create(**user_data)
            Token.objects.create(user=u)

        self.token = Token.objects.all()[0]

        self.task_content = {
            "title": "task100",
            "description": "This is task hundred",
            "due_date": "2023-12-13",
            "status": 1,
            "owner": User.objects.first()
        }
        self.task = Task.objects.create(**self.task_content)

    def test_delete_task(self):
        print("TEST CASE FOR DELETE ACTION")
        url = f"http://127.0.0.1:8000/tasks/{self.task.id}/"
        headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
        response = self.client.delete(url, **headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class RetrieveSingleTaskTest(TestCase):

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
            u = User.objects.create(**user_data)
            Token.objects.create(user=u)

        self.token = Token.objects.all()[0]

        self.task_content = {
            "title": "task100",
            "description": "This is task hundred",
            "due_date": "2023-12-13",
            "status": 1,
            "owner": User.objects.first()
        }
        self.task = Task.objects.create(**self.task_content)

    def test_retrieve_task(self):
        print("TEST CASE FOR SINGLE TASK RETRIEVAL")
        url = f"http://127.0.0.1:8000/tasks/{self.task.id}/"
        headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
        response = self.client.get(url, **headers)
        self.assertEqual(response.data['title'],self.task_content['title'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTaskTest(APITestCase):
    client = APIClient()

    def setUp(self):
        pswd = make_password("abc@123")

        self.user = User.objects.create(username = "user1",password = pswd)
        
        self.token = Token.objects.create(user = self.user)

        self.task = Task.objects.create(title = "task100",description = "This is task Hundred", due_date = "2023-12-13",status = 1, owner = self.user)

    
    def test_put_task(self):
        print("TEST CASE OF PUT ACTION")

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
        self.assertNotEqual(response.data['title'],self.task.title)
        self.assertEqual(response.data['title'],test_data['title'])
        self.assertEqual(response.status_code,status.HTTP_200_OK)



class UpdateTaskOtherThanOwner(APITestCase):

    def setUp(self):
        pswd = make_password("abc@123")
        self.user1 = User.objects.create(username = "user1",password = pswd)
        self.user2 = User.objects.create(username = "user2",password = pswd)

        self.token1 = Token.objects.create(user = self.user1)
        self.token2 = Token.objects.create(user = self.user2)

        self.task = Task.objects.create(title = "task100",description = "This is task Hundred", due_date = "2023-12-13",status = 1, owner = self.user1)
        
    def test_retrieve_other_than_owner(self):
        print("TEST CASE TO PREVENT CROSS ACCESS ")
        url = f"http://127.0.0.1:8000/tasks/{self.task.id}/"
        headers = {'HTTP_AUTHORIZATION': f'Token {self.token2.key}'}
        response = self.client.get(url,**headers)
        error_message = 'You do not have permission to perform this action.'
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'],error_message)






      




        
