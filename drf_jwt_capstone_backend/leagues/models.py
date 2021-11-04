from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class League(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=True)
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    zipcode = models.CharField(max_length=5, null=True)
    cost = models.FloatField()
    division = models.CharField(max_length=300, null=True)
    league_length = models.CharField(max_length=300, null=True)