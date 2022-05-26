from rest_framework import serializers
from authentication.models import AbstractUser
from authentication.views import User
from .models import FriendList, FriendRequest


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = '__all__'

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'



       
