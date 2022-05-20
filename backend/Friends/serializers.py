from rest_framework import serializers

from backend.authentication.models import User
from .models import Friends


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        Friends=(User)
