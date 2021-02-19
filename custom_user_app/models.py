from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyCustomUser(AbstractUser):
    Display_name = models.CharField(max_length=40, null=True, blank=True)
    Age = models.IntegerField(default=15, null=True, blank=True)
    Homepage = models.URLField(null=True, blank=True)
    password = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['Display_name', 'Age']
    

    def __str__(self):
        return self.Display_name