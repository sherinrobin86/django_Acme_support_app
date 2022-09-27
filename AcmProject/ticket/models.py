from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import Profile

class Ticket(models.Model):
    user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50,default=1)
    desc=models.CharField(max_length=50)
    priority=models.CharField(max_length=20,default=1)
    email=models.EmailField()
    phone=models.IntegerField()

    
    