from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = "To List Tokens"
    def handle(self,*args,**options):
        for token in Token.objects.all():
            print(f"{token.user.username}  {token.key}")

        

