from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    middle_name = models.CharField(max_length=20, null=True)
    is_business_owner = models.BooleanField(default=False)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=5, null=True)
    state = models.CharField(max_length=30, null=True)
