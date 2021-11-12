from django.http.response import Http404, JsonResponse
from functools import partial
from django.views.generic.base import RedirectView
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q

from .models import League
from .serializers import LeagueSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_all_leagues(request):
#     leagues = League.objects.all()
#     serializer = LeagueSerializer(leagues, many=True)
#     return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_leagues(request):
    if request.method == 'POST':
        serializer = LeagueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        leagues = League.objects.filter(user_id=request.user.id)
        serializer = LeagueSerializer(leagues, many=True)
        return Response(serializer.data)


@api_view(['GET'])   
@permission_classes([IsAuthenticated])
def league_detail(request, pk):
    if request.method == 'GET':
        league = League.objects.get(pk=pk)
        serializer = LeagueSerializer(league)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])   
@permission_classes([IsAuthenticated])
def update_league_detail(request, pk):        
    if request.method == 'PUT':
        league = League.objects.get(pk=pk)
        league.name = request.data['name']
        league.address = request.data['address']
        league.city = request.data['city']
        league.state = request.data['state']
        league.zipcode = request.data['zipcode']
        league.cost = request.data['cost']
        league.division = request.data['division']
        league.league_length = request.data['league_length']
        league.save()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_league(request, pk):
    if request.method == "DELETE":
        League.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)