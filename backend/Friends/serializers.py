from rest_framework import serializers
from authentication.models import AbstractUser
from .models import Friends


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
       
