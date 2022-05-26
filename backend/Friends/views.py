from ast import Delete
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from authentication.serializers import UserSerializer
from authentication.models import User
from .serializers import FriendListSerializer
from .serializers import FriendRequestSerializer
from .models import FriendList
from .models import FriendRequest
# from .models import User
# from authentication.models import models


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_friends_list(request):
    if request.method == 'GET':
        friends = FriendList.objects.all()
        serializer = FriendListSerializer(friends, many=True)
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
# creates new friendrequest object, save that object
# no need for serializer, respond with 200

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request, pk):
    sender = request.user.id
    receiver = User.objects.get(id=pk)
    print(receiver)
    request.data['sender'] = sender
    request.data['receiver'] = pk
    friend_request_created = FriendRequest.objects.get_or_create(sender=sender, receiver=receiver)
    if request.method == 'POST':
        serializer = FriendRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sender=request.user)
        if friend_request_created:
            return Response('friend request sent', status=status.HTTP_201_CREATED)
            

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_friend_request(request, pk):
    request_sender = request.user.id
    request_receiver = User.objects.get(id=pk)
    print(request_receiver)
    request.data['request_sender'] = request_sender
    request.data['request_receiver'] = pk
    friend_request_approve = FriendRequest.objects.filter(sender=request_sender, receiver=request_receiver)
    if request.method == 'PATCH':
        serializer = FriendListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(request_sender=request.user)
        if friend_request_approve:
            FriendRequest.is_active = False
            return Response("You are now friends! Check out eachothers Travel Experiences!", status=status.HTTP_200_OK)




# get pending requests  -get
# find all requests in DB with my user id as the receiver and is_active as true
# send back serialized friendrequests

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_pending_friend_request(request, pk):
#     if request.method == 'GET':


#user sends request to backend to accept friend request. 
#youll need to add the pk/id of the user in with the request to add to the "request_reciever" (request.user.id) field in the db + the id/pk of the friend request sender
# to fill the request_sender field in the db
# mark request's is_active to false

# deny friend request  -patch
# take in friendrequest_id, query for that object
# DONT add sender into receiver's friendlist
# mark request's is_active to false
# no need for serializer, respond with 200

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def deny_friend_request(request, pk):
#     if request.method == 'PATCH':



    # print('User ', f"{request.user.id} {request.user.email} {request.user.username}")
    # if request.method == 'POST':
    #     addFriend = FriendRequest.objects.all
    #     serializer = FriendRequestSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #     return Response(status=status.HTTP_201_CREATED)