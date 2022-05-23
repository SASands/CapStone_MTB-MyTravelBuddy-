from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from authentication.serializers import UserSerializer
from authentication.models import AbstractUser
from .serializers import FriendsSerializer
from .models import Friends
from authentication.models import models
from authentication.serializers import serializers

# Create your views here.

@api_view(['Get'])
@permission_classes([IsAuthenticated])
def friends_list(request):
    if request.method == 'Get':
        friends = Friends.objects.all()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['Get'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    if request.method == 'GET':
        users = models.AbstractUser.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_by_id(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    