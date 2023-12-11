from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = "To Create Users"
    def handle(self,*args,**options):
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

        


        print(f"{User.objects.count()} users created")

        for token in Token.objects.all():
            print(f"{token.user.username}  {token.key}")

        

