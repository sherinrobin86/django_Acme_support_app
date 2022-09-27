from django.db import models
class Profile(models.Model):
    def __str__(self):
        return self.name     
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=40)
    phone=models.IntegerField(default=1)
    department=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    