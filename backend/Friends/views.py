from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import FriendsSerializer
from .models import Friends

# Create your views here.

@api_view(['Get'])
@permission_classes([IsAuthenticated])
def friends_list(request):

    if request.method == 'Get':
        friends = Friends.objects.all()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data)


    