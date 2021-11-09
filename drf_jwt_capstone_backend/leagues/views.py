from django.http.response import Http404, JsonResponse
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import League
from .serializers import LeagueSerializer
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_leagues(request):
    leagues = League.objects.all()
    serializer = LeagueSerializer(leagues, many=True)
    return Response(serializer.data)

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


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def get_league(request, pk):
    try:
        return League.objects.get(pk=pk)
    except:
        raise Http404
def league_detail(self, request, pk):
    if request.method == 'GET':
        league = self.get_league(pk)
        serializer = LeagueSerializer(league)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        league = self.get_league(pk)
        serializer = LeagueSerializer(league, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        league = get_league(pk)
        league.delete()
        return Response(status=status.HTTP_200_OK)