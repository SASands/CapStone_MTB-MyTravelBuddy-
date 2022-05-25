from django.forms import CharField
from rest_framework import serializers;
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    model = Posts
    fields = (" ")