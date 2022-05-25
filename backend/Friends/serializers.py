from rest_framework import serializers
from authentication.models import AbstractUser
from authentication.views import User
from .models import FriendList, FriendRequest


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList, FriendRequest

       
