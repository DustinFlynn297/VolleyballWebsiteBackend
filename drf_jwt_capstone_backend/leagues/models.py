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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.division = validated_data.get('division', instance.division)
        instance.league_length = validated_data.get('league_length', instance.league_length)
        return instance