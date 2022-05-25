from urllib import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from Friends import serializers
from authentication.models import User
from .models import Posts
from .serializers import PostsSerializer


# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_posts_list(request):
    if request.method == 'GET':
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    print('User', f"{request.user.id} {request.user.email} {request.user.username}")    
    if request.method == 'POST':
        serializer = PostsSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_post_by_id(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == 'GET':
        serializer = PostsSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def post_patch(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == 'PATCH':
        serializer = PostsSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def post_delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == 'DELETE':       
        custom_response = {
            "Your Post was succesfully Deleted": post.user 
        }
        post.delete()
        return Response(custom_response, status=status.HTTP_202_ACCEPTED)




    # if request.method == 'GET':
    #     post = Posts.objects.filter(post_id=request.post.id)
    #     serializer = PostsSerializer(post)
    #     return Response(serializer.data)