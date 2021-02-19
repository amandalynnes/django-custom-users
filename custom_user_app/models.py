from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyCustomUser(AbstractUser):
    display_name = models.CharField(max_length=40, null=True, blank=True)
    age = models.IntegerField(default=15, null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)

    REQUIRED_FIELDS = ['display_name', 'age']