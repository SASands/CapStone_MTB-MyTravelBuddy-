from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from authentication.serializers import UserSerializer
from authentication.models import User
from .serializers import FriendsSerializer
from .models import FriendList
# from .models import User
# from authentication.models import models


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def friends_list(request):
    if request.method == 'GET':
        friends = FriendList.objects.all()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_id(request, pk):
    users = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)


# send friend request  -post
# endpoint takes in person being requested's user id
# creates new friendrequest object, saves that object
# no need for serializer, respond with 200

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def send_friend_request(request, pk):
#     if request.method == 'POST':


# get pending requests  -get
# find all requests in DB with my user id as the receiver and is_active as true
# send back serialized friendrequests

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_pending_friend_request(request, pk):
#     if request.method == 'GET':

# approve friend request  -patch
# take in friendrequest_id, query for that object from friendreuqest table
# add sender into receiver's friendlist
# mark request's is_active to false
# no need for serializer, respond with 200

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def approve_friend_request(request, pk):
#     if request.method == 'PATCH':


# deny friend request  -patch
# take in friendrequest_id, query for that object
# DONT add sender into receiver's friendlist
# mark request's is_active to false
# no need for serializer, respond with 200

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def deny_friend_request(request, pk):
#     if request.method == 'PATCH':
