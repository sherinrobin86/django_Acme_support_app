
from django.db import models
class Department(models.Model):
    def __str__(self):
        return self.name     
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    
