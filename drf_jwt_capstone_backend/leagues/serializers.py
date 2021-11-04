from rest_framework import serializers
from .models import League

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'address', 'city', 'state', 'zipcode', 'cost', 'division', 'league_length', 'user_id']